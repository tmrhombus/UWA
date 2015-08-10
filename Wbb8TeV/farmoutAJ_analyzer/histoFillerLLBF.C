#define histoFillerLLBF_cxx
#include "histoFillerLLBF.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>
//#include <cmath>

void histoFillerLLBF::Loop(
      TString outfileName, TString shift, 
      Bool_t isMC, Bool_t isW,
      UInt_t lumi_mu, UInt_t lumi_ele, 
      UInt_t nrEvents, Float_t crossSec
     )
{

 if (fChain == 0) return;
 Long64_t nrEntries = fChain->GetEntriesFast();
 Long64_t nb = 0;

 for (Long64_t jentry=0; jentry<nrEntries;jentry++) {
 //std::cout<<"    entry "<<jentry<<std::endl;
  if(jentry%100000==0) std::cout<<"    entry "<<jentry<<std::endl;
  Long64_t ientry = LoadTree(jentry);
  if (ientry < 0) break;
  nb = fChain->GetEntry(jentry);
  if(!nb){std::cout<<"histoFillerLLBF.C can't fChain->GetEntry(jentry)"<<std::endl;}

  // For splitting/merging of inclusive/exclusive W+Jets samples
  isWl = kFALSE;
  isWc = kFALSE;
  isWcc = kFALSE;
  isWbb = kFALSE;
  if(isW){
   twoCs  = (std::abs(goodJ1_partonFlavour)==4 && std::abs(goodJ2_partonFlavour)==4);
   someCs = (std::abs(goodJ1_partonFlavour)==4 || std::abs(goodJ2_partonFlavour)==4);
   someBs = (std::abs(goodJ1_partonFlavour)==5 || std::abs(goodJ2_partonFlavour)==5);

   isWl  = !someBs && !someCs;
   isWc  = !someBs &&  someCs && !twoCs;
   isWcc = !someBs &&  someCs &&  twoCs;
   isWbb =  someBs;

   // these numbers are the total number of events in the samples
   //  output from UWAnalysis/CRAB/MuNu/countEvents.sh 
   //      WJets, W1Jet, W2Jet, W3Jet, W4Jet 
   Float_t nrWnJ, nrW1J, nrW2J, nrW3J, nrW4J;
   nrWnJ = 75865454;
   nrW1J = 52593689;
   nrW2J = 64409521;
   nrW3J = 29503114;
   nrW4J = 13042592;

   std::vector<Float_t> ev;
   ev.push_back(nrWnJ);
   ev.push_back(nrW1J/0.175999);
   ev.push_back(nrW2J/0.0562617);
   ev.push_back(nrW3J/0.0168926);
   ev.push_back(nrW4J/0.00692218); 
   
   if( LHEProduct==5 ){nrEvents=ev[0];}
   else if( LHEProduct==6 ){nrEvents=ev[0]+ev[1];}
   else if( LHEProduct==7 ){nrEvents=ev[0]+ev[2];}
   else if( LHEProduct==8 ){nrEvents=ev[0]+ev[3];}
   else {nrEvents=ev[0]+ev[4];}
  }

  nbrGoodMu = 0; 
  nbrGoodMu = 
   std::count_if(
   goodMu_pt_vec->begin(),goodMu_pt_vec->end(), 
   std::bind2nd(std::greater_equal<int>(),25));

  nbrGoodEle = 0; 
  nbrGoodEle = 
   std::count_if(
   goodEle_pt_vec->begin(),goodEle_pt_vec->end(), 
   std::bind2nd(std::greater_equal<int>(),25));

  diMu_pt   = -1.; 
  diMu_eta  = -1.; 
  diMu_phi  = -1.; 
  diMu_mass = -1.; 
  diEle_pt   = -1.; 
  diEle_eta  = -1.; 
  diEle_phi  = -1.; 
  diEle_mass = -1.; 
  diMu_charge = 999.;
  diEle_charge = 999.;

  // DiLeptons
  if (goodMu_pt_vec->size()>1){
   fourVec_M1.SetPtEtaPhiM(
    goodMu_pt_vec->at(0), goodMu_eta_vec->at(0), 
    goodMu_phi_vec->at(0), goodMu_mass_vec->at(0));
   fourVec_M2.SetPtEtaPhiM(
    goodMu_pt_vec->at(1), goodMu_eta_vec->at(1), 
    goodMu_phi_vec->at(1), goodMu_mass_vec->at(1));
   fourVec_M1M2 = fourVec_M1 + fourVec_M2;
   diMu_pt   = fourVec_M1M2.Pt();
   diMu_eta  = fourVec_M1M2.Eta();
   diMu_phi  = fourVec_M1M2.Phi();
   diMu_mass = fourVec_M1M2.M();
   diMu_charge = goodMu_charge_vec->at(0) * goodMu_charge_vec->at(1) ;
  }
  if (goodEle_pt_vec->size()>1){
   fourVec_E1.SetPtEtaPhiM(
    goodEle_pt_vec->at(0), goodEle_eta_vec->at(0),
    goodEle_phi_vec->at(0), goodEle_mass_vec->at(0));
   fourVec_E2.SetPtEtaPhiM(
    goodEle_pt_vec->at(1), goodEle_eta_vec->at(1),
    goodEle_phi_vec->at(1), goodEle_mass_vec->at(1));
   fourVec_E1E2 = fourVec_E1 + fourVec_E2;
   diEle_pt   = fourVec_E1E2.Pt();
   diEle_eta  = fourVec_E1E2.Eta();
   diEle_phi  = fourVec_E1E2.Phi();
   diEle_mass = fourVec_E1E2.M();
   diEle_charge = goodEle_charge_vec->at(0) * goodEle_charge_vec->at(1) ;
  }

  // filter variables
  twoGoodMuons = kFALSE;
  twoGoodElectrons = kFALSE;

  twoGoodMuons =
   HLT_IsoMu24_eta2p1_v_fired
   && nbrGoodMu>=2
   && diMu_charge<0 
   && diMu_mass>15 ;

  twoGoodElectrons =
   HLT_Ele27_WP80_fired
   && nbrGoodEle>=2 
   && diEle_charge<0 
   && diEle_mass>15 ;

  oneCentralJet =
   goodJ1_pt>30 && goodJ2_pt<30 ;
  oneBJtoneFJ =
   oneCentralJet && goodJ1_CSV>0.898 
   && nrFwdJets>=1 ;
  oneBJmoneFJ =
   oneCentralJet && goodJ1_CSV>0.679 
   && nrFwdJets>=1 ;

  // SFs for CSV
  SF_1bt = goodJ1_SF_CSVT;
  SF_1bm = goodJ1_SF_CSVM;

  // define some variables that get plotted
  // MET
  MET_pt = met_pt;
  MET_phi = met_phi;

  // MT
  // good mu
  mt_mu_good = mt_goodMuon;
  mt_mu_good_uesUp   = mt_goodMuon_uesUp;
  mt_mu_good_uesDown = mt_goodMuon_uesDn;
  if( shift=="JESUp" ) { mt_mu_good = mt_goodMuon_jesUp; }
  if( shift=="JESDown" ) { mt_mu_good = mt_goodMuon_jesDn; }
  if( shift=="LESUp" )  { mt_mu_good = mt_goodMuon_eesUp; }
  if( shift=="LESDown" ) { mt_mu_good = mt_goodMuon_eesDn; }
  lep_mu_good_pt = -99;
  lep_mu_good_eta = -99;
  lep_mu_good_phi = -99;
  lep_mu_good_mass = -99;
  if( nbrGoodMu>0 ){
   lep_mu_good_pt =   goodMu_pt_vec->at(0);
   lep_mu_good_eta =  goodMu_eta_vec->at(0);
   lep_mu_good_phi =  goodMu_phi_vec->at(0);
   lep_mu_good_mass = goodMu_mass_vec->at(0);
  }
  // good ele
  mt_ele_good = mt_goodElectron;
  mt_ele_good_uesUp   = mt_goodElectron_uesUp;
  mt_ele_good_uesDown = mt_goodElectron_uesDn;
  if( shift=="JESUp" ) { mt_ele_good = mt_goodElectron_jesUp; }
  if( shift=="JESDown" ) { mt_ele_good = mt_goodElectron_jesDn; }
  if( shift=="LESUp" )  { mt_ele_good = mt_goodElectron_eesUp; }
  if( shift=="LESDown" ) { mt_ele_good = mt_goodElectron_eesDn; }
  lep_ele_good_pt =   -99;
  lep_ele_good_eta =  -99;
  lep_ele_good_phi =  -99;
  lep_ele_good_mass = -99;
  if( nbrGoodEle>0) {
   lep_ele_good_pt =   goodEle_pt_vec->at(0);
   lep_ele_good_eta =  goodEle_eta_vec->at(0);
   lep_ele_good_phi =  goodEle_phi_vec->at(0);
   lep_ele_good_mass = goodEle_mass_vec->at(0);
  }

  // MT and MET Selection Requirements
  // make sure mT > 0
  if( mt_mu_good <= 0 ){ mt_mu_good=-1.; }
  if( mt_mu_good_uesUp <= 0 ){ mt_mu_good_uesUp=-1.; }
  if( mt_mu_good_uesDown <= 0 ){ mt_mu_good_uesDown=-1.; }
  if( mt_ele_good <= 0 ){ mt_ele_good=-1.; }
  if( mt_ele_good_uesUp <= 0 ){ mt_ele_good_uesUp=-1.; }
  if( mt_ele_good_uesDown <= 0 ){ mt_ele_good_uesDown=-1.; }

  //////////////////////////
  // begin Selections
  //////////////////////////

  pass_mmbf_t=kFALSE;
  pass_mmbf_m=kFALSE;
  pass_eebf_t=kFALSE;
  pass_eebf_m=kFALSE;

  if( twoGoodMuons && oneBJtoneFJ ){
   pass_mmbf_t=kTRUE; 
   if( isMC ){
     SF_mmbf_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodMu_IDIso->at(1); 
    }
  }
  if( twoGoodMuons && oneBJmoneFJ ){
   pass_mmbf_m=kTRUE; 
   if( isMC ){
     SF_mmbf_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodMu_IDIso->at(1); 
    }
  }
  if( twoGoodElectrons && oneBJtoneFJ ){
   pass_eebf_t=kTRUE; 
   if( isMC ){
     SF_eebf_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(1);
    }
  }
  if( twoGoodElectrons && oneBJmoneFJ ){
   pass_eebf_m=kTRUE; 
   if( isMC ){
     SF_eebf_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(1);
    }
  }

  // total weight
  if( isMC ){
   // ttme 
   weight_mmbf_t = SF_mmbf_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_1bt / nrEvents;
   weight_mmbf_m = SF_mmbf_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_1bm / nrEvents;
   weight_eebf_t = SF_eebf_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_1bt / nrEvents;
   weight_eebf_m = SF_eebf_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_1bm / nrEvents;
  }
  else{
   weight_mmbf_t = 1.;
   weight_mmbf_m = 1.;
   weight_eebf_t = 1.;
   weight_eebf_m = 1.;
  }

  // xxbf_t
  fillHistWriter( pass_mmbf_t, kFALSE, pass_eebf_t, kFALSE,
                  0, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, -1., mt_ele_good, -1.,
                  weight_mmbf_t, 1., weight_eebf_t, 1.
                );

  // xxbf_m
  fillHistWriter( pass_mmbf_m, kFALSE, pass_eebf_m, kFALSE,
                  1, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, -1., mt_ele_good, -1.,
                  weight_mmbf_m, 1., weight_eebf_m, 1.
                );
 }  //// END MAIN LOOP 

 // write these histograms to file
 TFile *outfile = new TFile(outfileName,"RECREATE");
 outfile->cd();
 
 writeHistWriter( 0, 0, isW );
 writeHistWriter( 1, 0, isW );

 outfile->Close();
}

