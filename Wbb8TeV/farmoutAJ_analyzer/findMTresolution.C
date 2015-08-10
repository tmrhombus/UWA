#define findMTresolution_cxx
#include "findMTresolution.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>
#include <iostream>
//#include <cmath>

void findMTresolution::matchGen(Float_t &genPt, Float_t &genEta, Float_t &genPhi,
                                Float_t recoEta, Float_t recoPhi, 
                                Bool_t isMu)  
{

 drBestMatch = 0.5;
 genPt = -1;
 genEta = -99;
 genPhi = -99;
 
 for (unsigned i=0; i < GEN_dressedLeptonPT->size(); i++) {

     if(isMu  && !(std::abs(int(GEN_dressedLeptonPDGID->at(i)))==13)){ continue; }
     if(!isMu && !(std::abs(int(GEN_dressedLeptonPDGID->at(i)))==11)){ continue; }
//     std::cout<<" isMu   " <<isMu<<std::endl;
//     std::cout<<" PDG ID " <<std::abs(int(GEN_dressedLeptonPDGID->at(i)))<<std::endl;
//     std::cout<<GEN_dressedLeptonPDGID->at(i)<<std::endl;
//     std::cout<<GEN_dressedLeptonPT->at(i)<<std::endl;

   //  std::cout<<GEN_dressedLeptonPHI->at(i)<<std::endl;
   //  std::cout<<recoPhi<<std::endl;
   //  std::cout<<GEN_dressedLeptonPHI->at(i) - Float_t(recoPhi)<<std::endl;
     dP = GEN_dressedLeptonPHI->at(i) - Float_t(recoPhi);
     if (dP > 3.14159) dP-=2*3.14159;
     if (dP < -3.14159) dP+=2*3.14159;
     //std::cout<<dP<<std::endl;

     dE = GEN_dressedLeptonETA->at(i) - Float_t(recoEta);
     //std::cout<<dE<<std::endl;

     dR = sqrt(dE*dE + dP*dP);
     if(dR<drBestMatch){
      genPt = GEN_dressedLeptonPT->at(i);
      genEta = GEN_dressedLeptonETA->at(i);
      genPhi = GEN_dressedLeptonPHI->at(i);
      drBestMatch = dR;
     }
 }
}

void findMTresolution::Loop(TString outfileName)
{
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;
      // if (Cut(ientry) < 0) continue;

     // count collections
     nbrGoodMu = 0; 
     nbrGoodMu = 
      std::count_if(
      goodMu_pt_vec->begin(),goodMu_pt_vec->end(), 
      std::bind2nd(std::greater_equal<int>(),30));
     nbrVetoMu=0;
     nbrVetoMu+=
      std::count_if(
      vetoMu_pt_vec->begin(),vetoMu_pt_vec->end(), 
      std::bind2nd(std::greater_equal<int>(),10));
     nbrVetoMu -= nbrGoodMu;
     //nbrQCDMu=
     // std::count_if(
     // qcdMu_pt_vec->begin(),qcdMu_pt_vec->end(), 
     // std::bind2nd(std::greater_equal<int>(),30));
   
     nbrGoodEle = 0; 
     nbrGoodEle = 
      std::count_if(
      goodEle_pt_vec->begin(),goodEle_pt_vec->end(), 
      std::bind2nd(std::greater_equal<int>(),30));
     nbrVetoEle=0;
     nbrVetoEle+=
      std::count_if(
      vetoEle_pt_vec->begin(),vetoEle_pt_vec->end(), 
      std::bind2nd(std::greater_equal<int>(),10));
     nbrVetoEle -= nbrGoodEle;
     //nbrQCDEle=
     // std::count_if(
     // qcdEle_pt_vec->begin(),qcdEle_pt_vec->end(), 
     // std::bind2nd(std::greater_equal<int>(),30));

     // filter variables
     oneGoodMuon =  kFALSE;
     //oneQCDMuon =   kFALSE;
     oneGoodElectron =  kFALSE;
     //oneQCDElectron =   kFALSE;

     oneGoodMuon =
       HLT_IsoMu24_eta2p1_v_fired
       && nbrGoodMu==1  && nbrVetoMu==0
       && nbrGoodEle==0 && nbrVetoEle==0;
     //oneQCDMuon =
     // HLT_IsoMu24_eta2p1_v_fired
     // && nbrQCDMu==1
     // && nbrGoodMu==0  && nbrVetoMu==0
     // && nbrGoodEle==0 && nbrVetoEle==0;
     oneGoodElectron =
      HLT_Ele27_WP80_fired
      && nbrGoodEle==1 && nbrVetoEle==0
      && nbrGoodMu==0  && nbrVetoMu==0;
     //oneQCDElectron =
     // HLT_Ele27_WP80_fired &&
     // nbrQCDEle==1
     // && nbrGoodEle==0 && nbrVetoEle==0
     // && nbrGoodMu==0  && nbrVetoMu==0;

     min2goodJs =
      goodJ1_pt>25 && goodJ2_pt>25 && fwdJ1_pt<25;
     exactly2goodJs =
      min2goodJs && goodJ3_pt<25;
     exactly2goodBJs =
        exactly2goodJs
        && goodJ1_CSV>0.898 && goodJ2_CSV>0.898;

     SF_top2BJs = goodJ1_SF_CSVT * goodJ2_SF_CSVT;

     pass_wbb_mu_good=kFALSE;
     pass_wbb_ele_good=kFALSE;

     gen_met_fv.SetPtEtaPhiM( GEN_neutrinoPT->at(0),
                              GEN_neutrinoETA->at(0),
                              GEN_neutrinoPHI->at(0), 0 );

  // gen_met_fv.SetPtEtaPhiM(0, 0, 0, 0);
  // for (unsigned i=0; i < GEN_neutrinoPT->size(); i++) {
  //  gen_met_tempfv.SetPtEtaPhiM( GEN_neutrinoPT->at(i),
  //                               GEN_neutrinoETA->at(i),
  //                               GEN_neutrinoPHI->at(i), 0 );
  //  gen_met_fv += gen_met_tempfv;
  // }

   if( oneGoodMuon && exactly2goodBJs ){
    pass_wbb_mu_good=kTRUE;
    SF_wjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    weight_wbb_mu_good  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * SF_top2BJs;


    matchGen( genMatchedLep_pt, genMatchedLep_eta, genMatchedLep_phi,
              goodMu_eta_vec->at(0), goodMu_phi_vec->at(0), kTRUE );
  
    dphiMu = genMatchedLep_phi - gen_met_fv.Phi();
    if( dphiMu > 3.14159 ){ dphiMu-=(2*3.14159); }
    else if( dphiMu < -3.14159 ){ dphiMu+=(2*3.14159); }

    mt_genMuon = sqrt(2. * genMatchedLep_pt * gen_met_fv.Pt() * (1. - cos(dphiMu)));
    res_Muon = (mt_goodMuon - mt_genMuon) / mt_genMuon;

    std::cout<<"EVENT: "<<EVENT<<std::endl;
std::cout<<"  "<<GEN_neutrinoPT->size()<<std::endl;
    std::cout<<"mt_goodMuon: "<<mt_goodMuon<<std::endl;
    std::cout<<"mt_genMuon:  "<<mt_genMuon<<std::endl;
    std::cout<<"pT reco: "<<goodMu_pt_vec->at(0)<<std::endl;
    std::cout<<"pT gen : "<<genMatchedLep_pt<<std::endl;
    std::cout<<"MET reco: "<<met_pt<<std::endl;
    std::cout<<"MET gen:  "<<gen_met_fv.Pt()<<std::endl;
    std::cout<<"dR(gen,reco) "<<drBestMatch<<std::endl;
    std::cout<<" "<<std::endl;
    if( genMatchedLep_pt>0 ){
     //hists_mt_reco_mu[0].Fill(mt_goodMuon,weight_wbb_mu_good) ;
     hists_mt_reco_mu[0].Fill(mt_goodMuon) ;
     hists_mt_gen_mu[0].Fill(mt_genMuon);//,weight_wbb_mu_good) ;
     hists_mt_res_mu[0].Fill(res_Muon) ;
    }
   }

   if( oneGoodElectron && exactly2goodBJs ){
    pass_wbb_ele_good=kTRUE;
    SF_wjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    weight_wbb_ele_good  = SF_wjj_ele_good_IDIsoHLT  * SF_lumiWeightPU * SF_top2BJs;

    matchGen( genMatchedLep_pt, genMatchedLep_eta, genMatchedLep_phi,
              goodEle_eta_vec->at(0), goodEle_phi_vec->at(0), kFALSE );
 
    dphiEle = genMatchedLep_pt - gen_met_fv.Pt();
    if( dphiEle > 3.14159 ){ dphiEle-=(2*3.14159); }
    else if( dphiEle < -3.14159 ){ dphiEle+=(2*3.14159); }

    mt_genEle = sqrt(2. * genMatchedLep_pt * gen_met_fv.Pt() * (1. - cos(dphiEle)));
    res_Ele = (mt_goodElectron - mt_genEle) / mt_genEle;


    std::cout<<"EVENT: "<<EVENT<<std::endl;
std::cout<<"  "<<GEN_neutrinoPT->size()<<std::endl;
    std::cout<<"mt_goodEle: "<<mt_goodElectron<<std::endl;
    std::cout<<"mt_genEle:  "<<mt_genEle<<std::endl;
    std::cout<<"pT reco: "<<goodEle_pt_vec->at(0)<<std::endl;
    std::cout<<"pT gen : "<<genMatchedLep_pt<<std::endl;
    std::cout<<"MET reco: "<<met_pt<<std::endl;
    std::cout<<"MET gen:  "<<gen_met_fv.Pt()<<std::endl;
    std::cout<<"dR(gen,reco) "<<drBestMatch<<std::endl;
    std::cout<<" "<<std::endl;
    std::cout<<" "<<std::endl;

    if( genMatchedLep_pt>0 ){
     //hists_mt_reco_ele[0].Fill(mt_goodElectron,weight_wbb_ele_good) ;
     hists_mt_reco_ele[0].Fill(mt_goodElectron) ;
     hists_mt_gen_ele[0].Fill(mt_genEle);//,weight_wbb_mu_good) ;
     hists_mt_res_ele[0].Fill(res_Ele) ;
    }

   }

   }

  TFile *outfile = new TFile(outfileName,"RECREATE");
  outfile->cd();
  
  hists_mt_reco_mu[0].Write();
  hists_mt_gen_mu[0].Write();
  hists_mt_res_mu[0].Write();
  hists_mt_reco_ele[0].Write();
  hists_mt_gen_ele[0].Write();
  hists_mt_res_ele[0].Write();

  outfile->Close();
  std::cout<<"done"<<std::endl;
}
