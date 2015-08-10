#define histoFiller_cxx
#include "histoFiller.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>
//#include <cmath>

void histoFiller::Loop(
      TString outfileName, TString shift, 
      Bool_t isMC, Bool_t isW,
      UInt_t lumi_mu, UInt_t lumi_ele, 
      UInt_t nrEvents, Float_t crossSec
     )
{

 if (fChain == 0) return;
 //Long64_t nrEntries = fChain->GetEntries();
 Long64_t nrEntries = fChain->GetEntriesFast();
 Long64_t nb = 0;

 for (Long64_t jentry=0; jentry<nrEntries;jentry++) {
  // std::cout<<"    entry "<<jentry<<std::endl;
  if(jentry%100000==0) std::cout<<"    entry "<<jentry<<std::endl;
  Long64_t ientry = LoadTree(jentry);
  if (ientry < 0) break;
  nb = fChain->GetEntry(jentry);
  if(!nb){std::cout<<"histoFiller.C can't fChain->GetEntry(jentry)"<<std::endl;}

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
   nrW2J = 64409521; //for CestPi Mars // 63806612; //for CestPiVV  
   nrW3J = 29503114; //for Schweincomp//  30358906;  
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
   std::bind2nd(std::greater_equal<int>(),30));
  nbrVetoMu=0;
  nbrVetoMu+=
   std::count_if(
   vetoMu_pt_vec->begin(),vetoMu_pt_vec->end(), 
   std::bind2nd(std::greater_equal<int>(),10));
  nbrVetoMu -= nbrGoodMu;
  nbrQCDMu=
   std::count_if(
   qcdMu_pt_vec->begin(),qcdMu_pt_vec->end(), 
   std::bind2nd(std::greater_equal<int>(),30));

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
  nbrQCDEle=
   std::count_if(
   qcdEle_pt_vec->begin(),qcdEle_pt_vec->end(), 
   std::bind2nd(std::greater_equal<int>(),30));


  // dr J1 J2
  goodJ1J2_dR = -1.; 
  dphiJJ = dPhi(goodJ1_phi, goodJ2_phi);
  detaJJ = dEta(goodJ1_eta, goodJ2_eta);
  goodJ1J2_dR = std::sqrt( ((goodJ1_eta-goodJ2_eta)*(goodJ1_eta-goodJ2_eta)) + (dphiJJ*dphiJJ) );

  // Dijets
  fourVec_J1.SetPtEtaPhiM(goodJ1_pt, goodJ1_eta, goodJ1_phi, goodJ1_mass);
  fourVec_J2.SetPtEtaPhiM(goodJ2_pt, goodJ2_eta, goodJ2_phi, goodJ2_mass);
  fourVec_J3.SetPtEtaPhiM(goodJ3_pt, goodJ3_eta, goodJ3_phi, goodJ3_mass);
  fourVec_J4.SetPtEtaPhiM(goodJ4_pt, goodJ4_eta, goodJ4_phi, goodJ4_mass);

  fourVec_J1J2 = fourVec_J1 + fourVec_J2;
  fourVec_J3J4 = fourVec_J3 + fourVec_J4;

  goodJ1J2_pt   = fourVec_J1J2.Pt();
  goodJ1J2_eta  = fourVec_J1J2.Eta();
  goodJ1J2_phi  = fourVec_J1J2.Phi();
  goodJ1J2_mass = fourVec_J1J2.M();

  goodJ3J4_pt   = fourVec_J3J4.Pt();
  goodJ3J4_eta  = fourVec_J3J4.Eta();
  goodJ3J4_phi  = fourVec_J3J4.Phi();
  goodJ3J4_mass = fourVec_J3J4.M();

  goodM1M2_pt   = -1.; 
  goodM1M2_eta  = -1.; 
  goodM1M2_phi  = -1.; 
  goodM1M2_mass = -1.; 
  goodE1E2_pt   = -1.; 
  goodE1E2_eta  = -1.; 
  goodE1E2_phi  = -1.; 
  goodE1E2_mass = -1.; 
  // DiLeptons

  //if ( nbrGoodMu > 1 ){ 
  if (goodMu_pt_vec->size()>1){
   fourVec_M1.SetPtEtaPhiM(goodMu_pt_vec->at(0), goodMu_eta_vec->at(0), goodMu_phi_vec->at(0), goodMu_mass_vec->at(0));
   fourVec_M2.SetPtEtaPhiM(goodMu_pt_vec->at(1), goodMu_eta_vec->at(1), goodMu_phi_vec->at(1), goodMu_mass_vec->at(1));
   fourVec_M1M2 = fourVec_M1 + fourVec_M2;
   goodM1M2_pt   = fourVec_M1M2.Pt();
   goodM1M2_eta  = fourVec_M1M2.Eta();
   goodM1M2_phi  = fourVec_M1M2.Phi();
   goodM1M2_mass = fourVec_M1M2.M();
  }
  //if ( nbrGoodEle > 1 ){ 
  if (goodEle_pt_vec->size()>1){
   fourVec_E1.SetPtEtaPhiM(goodEle_pt_vec->at(0), goodEle_eta_vec->at(0), goodEle_phi_vec->at(0), goodEle_mass_vec->at(0));
   fourVec_E2.SetPtEtaPhiM(goodEle_pt_vec->at(1), goodEle_eta_vec->at(1), goodEle_phi_vec->at(1), goodEle_mass_vec->at(1));
   fourVec_E1E2 = fourVec_E1 + fourVec_E2;
   goodE1E2_pt   = fourVec_E1E2.Pt();
   goodE1E2_eta  = fourVec_E1E2.Eta();
   goodE1E2_phi  = fourVec_E1E2.Phi();
   goodE1E2_mass = fourVec_E1E2.M();
  }

  // filter variables
  oneGoodMuon =  kFALSE; 
  twoGoodMuons = kFALSE; 
  oneQCDMuon =   kFALSE; 
  twoQCDMuons =  kFALSE; 
  oneGoodElectron =  kFALSE; 
  twoGoodElectrons = kFALSE; 
  oneQCDElectron =   kFALSE; 
  twoQCDElectrons =  kFALSE;  
  twoGoodLMuE = kFALSE; 
  twoGoodLEMu = kFALSE; 
  twoQCDLMuE =  kFALSE; 
  twoQCDLEMu =  kFALSE; 

//   nbrFwdJets;
//   nbrGoodJets;
  oneGoodMuon = 
    HLT_IsoMu24_eta2p1_v_fired 
    && nbrGoodMu==1  && nbrVetoMu==0 
    && nbrGoodEle==0 && nbrVetoEle==0;
  twoGoodMuons = 
   HLT_IsoMu24_eta2p1_v_fired
   && nbrGoodMu==2  && nbrVetoMu==0
   && nbrGoodEle==0 && nbrVetoEle==0;
  oneQCDMuon = 
   HLT_IsoMu24_eta2p1_v_fired 
   && nbrQCDMu==1 
   && nbrGoodMu==0  && nbrVetoMu==0 
   && nbrGoodEle==0 && nbrVetoEle==0;
  twoQCDMuons = 
   HLT_IsoMu24_eta2p1_v_fired
   && nbrQCDMu==1 && nbrGoodMu==1 && nbrVetoMu==0 
   && nbrGoodEle==0 && nbrVetoEle==0;
 
  oneGoodElectron = 
   HLT_Ele27_WP80_fired
   && nbrGoodEle==1 && nbrVetoEle==0 
   && nbrGoodMu==0  && nbrVetoMu==0;
  twoGoodElectrons = 
   HLT_Ele27_WP80_fired
   && nbrGoodEle==2 && nbrVetoEle==0 
   && nbrGoodMu==0  && nbrVetoMu==0;
  oneQCDElectron = 
   HLT_Ele27_WP80_fired && 
   nbrQCDEle==1 
   && nbrGoodEle==0 && nbrVetoEle==0
   && nbrGoodMu==0  && nbrVetoMu==0;
  twoQCDElectrons =  
   HLT_Ele27_WP80_fired
   && nbrQCDEle==1 && nbrGoodEle==1 && nbrVetoEle==0
   && nbrGoodMu==0 && nbrVetoMu==0;
  
  twoGoodLMuE = HLT_IsoMu24_eta2p1_v_fired
   && nbrGoodEle==1 && nbrVetoEle==0
   && nbrGoodMu==1  && nbrVetoMu==0;
  twoGoodLEMu = HLT_Ele27_WP80_fired
   && nbrGoodEle==1 && nbrVetoEle==0
   && nbrGoodMu==1  && nbrVetoMu==0;
  twoQCDLMuE =  HLT_IsoMu24_eta2p1_v_fired 
   && nbrQCDMu==1   && nbrVetoMu==0 
   && nbrGoodEle==1 && nbrVetoEle==0;
  twoQCDLEMu =  HLT_Ele27_WP80_fired  
   && nbrQCDEle==1   && nbrVetoEle==0 
   && nbrGoodMu==1 && nbrVetoMu==0;

  min2goodJs = 
   goodJ1_pt>25 && goodJ2_pt>25 && fwdJ1_pt<25;
  exactly2goodJs = 
   min2goodJs && goodJ3_pt<25;
//  min2goodBJs = 
//   min2goodJs
//   && goodJ1_CSV>0.679 && goodJ2_CSV>0.679;
//  exactly2goodBJs = 
//   exactly2goodJs 
//   && goodJ1_CSV>0.679 && goodJ2_CSV>0.679;
//  aGoodBJaFwdJ = 
//   nrGoodJets==1 && nrFwdJets==1 
//   && goodJ1_CSV>0.679;
  min2goodBJs = 
     min2goodJs
     && goodJ1_CSV>0.898 && goodJ2_CSV>0.898;
  exactly2goodBJs = 
     exactly2goodJs 
     && goodJ1_CSV>0.898 && goodJ2_CSV>0.898;
  exactly2goodJsOneB = 
     exactly2goodJs 
     && goodJ1_CSV>0.898;
  aGoodBJaFwdJ = 
     goodJ1_pt>25 && fwdJ1_pt>25
     && goodJ1_CSV>0.898;
  min3gJs2gBJs = 
     min2goodBJs && goodJ3_pt>25;

  // SFs for CSV
//  SF_top2BJs = goodJ1_SF_CSVM * goodJ2_SF_CSVM; 
//  SF_top2BJs_errUp = goodJ1_SF_CSVM_errUp * goodJ2_SF_CSVM_errUp;
//  SF_top2BJs_errDn = goodJ1_SF_CSVM_errDn * goodJ2_SF_CSVM_errDn; 
//  SF_oneGoodBJ = goodJ1_SF_CSVM;
  SF_top2BJs = goodJ1_SF_CSVT * goodJ2_SF_CSVT; 
  SF_top2BJs_errUp = goodJ1_SF_CSVT_errUp * goodJ2_SF_CSVT_errUp;
  SF_top2BJs_errDn = goodJ1_SF_CSVT_errDn * goodJ2_SF_CSVT_errDn; 
  SF_oneGoodBJ = goodJ1_SF_CSVT;
  SF_oneGoodBJ_errUp = goodJ1_SF_CSVT_errUp;
  SF_oneGoodBJ_errDn = goodJ1_SF_CSVT_errDn;

  //SF_top2BJs =       1.; 
  //SF_top2BJs_errUp = 1.; 
  //SF_top2BJs_errDn = 1.; 
  //SF_oneGoodBJ =   1.; 

  SF_CSVrwtgJfJ = 1.; //goodJ1_CSVreweight ;
  SF_CSVrwt2gJs = 1.; //goodJ1_CSVreweight * goodJ2_CSVreweight;

  // define some variables that get plotted
  // MET
  MET_pt = met_pt;
  MET_phi = met_phi;
  MET_pt_uesUp = met_uesUp_pt;
  MET_pt_uesDown = met_uesDn_pt;
  MET_phi_uesUp = met_uesUp_phi;
  MET_phi_uesDown = met_uesDn_phi;
  if( shift=="JESUp" ) { 
   MET_pt = met_jesUp_pt;
   MET_phi = met_jesUp_phi;
  }
  if( shift=="JESDown" ) {
   MET_pt = met_jesDn_pt;
   MET_phi = met_jesDn_phi;
  }
  //if( shift=="LESUp" ) { 
  // MET_pt = met_eesUp_pt;
  // MET_phi = met_eesUp_phi;
  //}
  //if( shift=="LESDown" ) {
  // MET_pt = met_eesDn_pt;
  // MET_phi = met_eesDn_phi;
  //}

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
  // qcd mu
  mt_mu_qcd = mt_qcdMuon;
  mt_mu_qcd_uesUp   = mt_qcdMuon_uesUp;
  mt_mu_qcd_uesDown = mt_qcdMuon_uesDn;
  if( shift=="JESUp" ) { mt_mu_qcd = mt_qcdMuon_jesUp; }
  if( shift=="JESDown" ) { mt_mu_qcd = mt_qcdMuon_jesDn; }
  if( shift=="LESUp" )  { mt_mu_qcd = mt_qcdMuon_eesUp; }
  if( shift=="LESDown" )  { mt_mu_qcd = mt_qcdMuon_eesDn; }
  lep_mu_qcd_pt =   -99; 
  lep_mu_qcd_eta =  -99; 
  lep_mu_qcd_phi =  -99; 
  lep_mu_qcd_mass = -99; 
  if( nbrQCDMu>0 ){
   lep_mu_qcd_pt =   qcdMu_pt_vec->at(0);
   lep_mu_qcd_eta =  qcdMu_eta_vec->at(0);
   lep_mu_qcd_phi =  qcdMu_phi_vec->at(0);
   lep_mu_qcd_mass = -1; //qcdMu_mass_vec->at(0);
  }
  // good ele
  mt_ele_good = mt_goodElectron;
  mt_ele_good_uesUp   = mt_goodElectron_uesUp;
  mt_ele_good_uesDown = mt_goodElectron_uesDn;
  if( shift=="JESUp" ) { mt_ele_good = mt_goodElectron_jesUp; }
  if( shift=="JESDown" ) { mt_ele_good = mt_goodElectron_jesDn; }
  if( shift=="LESUp" )  { mt_ele_good = mt_goodElectron_eesUp; }
  if( shift=="LESDown" ) { mt_ele_good = mt_goodElectron_eesDn; }
  lep_ele_good_pt =   0; 
  lep_ele_good_eta =  0; 
  lep_ele_good_phi =  0; 
  lep_ele_good_mass = 0; 
  if( nbrGoodEle>0) {
   lep_ele_good_pt =   goodEle_pt_vec->at(0);
   lep_ele_good_eta =  goodEle_eta_vec->at(0);
   lep_ele_good_phi =  goodEle_phi_vec->at(0);
   lep_ele_good_mass = goodEle_mass_vec->at(0);
  }
  // qcd ele
  mt_ele_qcd = mt_qcdElectron;
  mt_ele_qcd_uesUp   = mt_qcdElectron_uesUp;
  mt_ele_qcd_uesDown = mt_qcdElectron_uesDn;
  if( shift=="JESUp" ) { mt_ele_qcd = mt_qcdElectron_jesUp; }
  if( shift=="JESDown" ) { mt_ele_qcd = mt_qcdElectron_jesDn; }
  if( shift=="LESUp" )  { mt_ele_qcd = mt_qcdElectron_eesUp; }
  if( shift=="LESDown" )  { mt_ele_qcd = mt_qcdElectron_eesDn; }
  lep_ele_qcd_pt =   -99; 
  lep_ele_qcd_eta =  -99; 
  lep_ele_qcd_phi =  -99; 
  lep_ele_qcd_mass = -99; 
  if( nbrQCDEle>0 ){
   lep_ele_qcd_pt =   qcdEle_pt_vec->at(0);
   lep_ele_qcd_eta =  qcdEle_eta_vec->at(0);
   lep_ele_qcd_phi =  qcdEle_phi_vec->at(0);
   lep_ele_qcd_mass = -1; //qcdEle_mass_vec->at(0);
  }

  // MT and MET Selection Requirements
  // make sure mT > 0
  if( mt_mu_good <= 0 ){ mt_mu_good=-1.; }
  if( mt_mu_good_uesUp <= 0 ){ mt_mu_good_uesUp=-1.; }
  if( mt_mu_good_uesDown <= 0 ){ mt_mu_good_uesDown=-1.; }
  if( mt_mu_qcd <= 0 ){ mt_mu_qcd=-1.; }
  if( mt_mu_qcd_uesUp <= 0 ){ mt_mu_qcd_uesUp=-1.; }
  if( mt_mu_qcd_uesDown <= 0 ){ mt_mu_qcd_uesDown=-1.; }
  if( mt_ele_good <= 0 ){ mt_ele_good=-1.; }
  if( mt_ele_good_uesUp <= 0 ){ mt_ele_good_uesUp=-1.; }
  if( mt_ele_good_uesDown <= 0 ){ mt_ele_good_uesDown=-1.; }
  if( mt_ele_qcd <= 0 ){ mt_ele_qcd=-1.; }
  if( mt_ele_qcd_uesUp <= 0 ){ mt_ele_qcd_uesUp=-1.; }
  if( mt_ele_qcd_uesDown <= 0 ){ mt_ele_qcd_uesDown=-1.; }

  // For Ilya
  dphiJ1Met = dPhi(goodJ1_phi, MET_phi);
  diJetVVcut =  kTRUE; // For Ilya, DiJet Cuts
    // goodJ1_pt>40 && goodJ2_pt>35 && goodJ1J2_pt>70 && detaJJ<1.5;

  passMET =        kTRUE; // MET_pt > 25. && dphiJ1Met > 0.4; // kTRUE; // 
  passMT_goodMu =  kTRUE; // mt_mu_good  > 45; // 30; 
  passMT_qcdMu =   kTRUE; // mt_mu_qcd   > 45; // 30; 
  passMT_goodEle = kTRUE; // mt_ele_good > 45; // 30; 
  passMT_qcdEle =  kTRUE; // mt_ele_qcd  > 45; // 30; 


  ////////////////////////////////
  // begin wjj, wbb Selection 3,0
  ////////////////////////////////
  Bool_t pass_wjj_mu_good=kFALSE;
  Bool_t pass_wjj_mu_qcd=kFALSE;
  Bool_t pass_wbb_mu_good=kFALSE;
  Bool_t pass_wbb_mu_qcd=kFALSE;
  Bool_t pass_wjj_ele_good=kFALSE;
  Bool_t pass_wjj_ele_qcd=kFALSE;
  Bool_t pass_wbb_ele_good=kFALSE;
  Bool_t pass_wbb_ele_qcd=kFALSE;
  //if( oneGoodMuon && exactly2goodJsOneB && diJetVVcut && passMET && passMT_goodMu ){ // mu good
  if( oneGoodMuon && exactly2goodJs && diJetVVcut && passMET && passMT_goodMu ){ // mu good
   pass_wjj_mu_good=kTRUE; 
   nbrEntries_mu_wjj_good_postcut++;
   //std::cout<<"Pass wjj mu"<<std::endl;
   //std::cout<<"CSVrwt J1: "<<goodJ1_CSVreweight<<" CSVrwt J2: "<<goodJ2_CSVreweight<<std::endl;
   if ( exactly2goodBJs ){
    if ( isWl ){  
//    std::cout<<"Wl EVENT passing wbb Mu: "<<EVENT<<std::endl;   //////////////////////
//    std::cout<<"SF_top2BJs_errUp: "<<SF_top2BJs_errUp<<std::endl;
//    std::cout<<"SF_top2BJs      : "<<SF_top2BJs      <<std::endl;
//    std::cout<<"SF_top2BJs_errDn: "<<SF_top2BJs_errDn<<std::endl;
//    std::cout<<" goodJ1_pt: "<<goodJ1_pt<<std::endl;
//    std::cout<<" goodJ2_pt: "<<goodJ2_pt<<std::endl;
//    std::cout<<" goodJ3_pt: "<<goodJ3_pt<<std::endl;
//    std::cout<<" goodJ4_pt: "<<goodJ4_pt<<std::endl;
//    std::cout<<" fwdJ1_pt: "<<fwdJ1_pt<<std::endl;
//    std::cout<<" fwdJ2_pt: "<<fwdJ2_pt<<std::endl;
//    std::cout<<" nrCleanJets: "<<nrCleanJets<<std::endl;
//    std::cout<<" nrAllJets: "<<nrAllJets<<std::endl;
//    std::cout<<" met_pt: "<<met_pt<<std::endl;
//    std::cout<<" met_jesDn_pt: "<<met_jesDn_pt<<std::endl;
//    std::cout<<" met_jesUp_pt: "<<met_jesUp_pt<<std::endl;
//    std::cout<<" mt_goodMuon: "<<mt_goodMuon<<std::endl;
//    std::cout<<" mt_goodMuon_jesUp: "<<mt_goodMuon_jesUp<<std::endl;
//    std::cout<<" mt_goodMuon_jesDn: "<<mt_goodMuon_jesDn<<std::endl;
    }
    pass_wbb_mu_good=kTRUE; 
    nbrEntries_mu_wbb_good_postcut++;
    //std::cout<<"Pass wbb mu"<<std::endl;
    //std::cout<<"CSVrwt J1: "<<goodJ1_CSVreweight<<" CSVrwt J2: "<<goodJ2_CSVreweight<<std::endl;
   }
   if( isMC ){
    SF_wjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    SF_wjj_mu_good_IDIsoHLT_errUp = SF_wjj_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
    SF_wjj_mu_good_IDIsoHLT_errDn = SF_wjj_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
   }
  }
  //if( oneQCDMuon && exactly2goodJs ){ // mu qcd'
  //if( oneQCDMuon && exactly2goodJsOneB && diJetVVcut && passMET && passMT_qcdMu ){ // mu qcd
  if( oneQCDMuon && exactly2goodJs && diJetVVcut && passMET && passMT_qcdMu ){ // mu qcd
   pass_wjj_mu_qcd=kTRUE; 
   nbrEntries_mu_wjj_qcd_postcut++;
   if ( exactly2goodBJs ){
    pass_wbb_mu_qcd=kTRUE; 
    nbrEntries_mu_wbb_qcd_postcut++;
   }
   if( isMC ){
    SF_wjj_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
    SF_wjj_mu_qcd_IDIsoHLT_errUp = SF_wjj_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
    SF_wjj_mu_qcd_IDIsoHLT_errDn = SF_wjj_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
   }
  }
  if( oneGoodElectron && exactly2goodJs && diJetVVcut && passMET && passMT_goodEle ){ // ele good
  //if( oneGoodElectron && exactly2goodJsOneB && diJetVVcut && passMET && passMT_goodEle ){ // ele good
   pass_wjj_ele_good=kTRUE; 
   nbrEntries_ele_wjj_good_postcut++;
   if ( exactly2goodBJs ){
//    if ( isWl ){
//     std::cout<<"Wl EVENT passing wbb Ele: "<<EVENT<<std::endl;   //////////////////////
//    }
//    std::cout<<"SF_top2BJs_errUp: "<<SF_top2BJs_errUp<<std::endl;
//    std::cout<<"SF_top2BJs      : "<<SF_top2BJs      <<std::endl;
//    std::cout<<"SF_top2BJs_errDn: "<<SF_top2BJs_errDn<<std::endl;
//    std::cout<<" goodJ1_pt: "<<goodJ1_pt<<std::endl;
//    std::cout<<" goodJ2_pt: "<<goodJ2_pt<<std::endl;
//    std::cout<<" goodJ3_pt: "<<goodJ3_pt<<std::endl;
//    std::cout<<" goodJ4_pt: "<<goodJ4_pt<<std::endl;
//    std::cout<<" fwdJ1_pt: "<<fwdJ1_pt<<std::endl;
//    std::cout<<" fwdJ2_pt: "<<fwdJ2_pt<<std::endl;
//    std::cout<<" nrCleanJets: "<<nrCleanJets<<std::endl;
//    std::cout<<" nrAllJets: "<<nrAllJets<<std::endl;
//    std::cout<<" met_pt: "<<met_pt<<std::endl;
//    std::cout<<" met_jesDn_pt: "<<met_jesDn_pt<<std::endl;
//    std::cout<<" met_jesUp_pt: "<<met_jesUp_pt<<std::endl;
//    std::cout<<" met_uesDn_pt: "<<met_uesDn_pt<<std::endl;
//    std::cout<<" met_uesUp_pt: "<<met_uesUp_pt<<std::endl;
//    std::cout<<" met_eesDn_pt: "<<met_eesDn_pt<<std::endl;
//    std::cout<<" met_eesUp_pt: "<<met_eesUp_pt<<std::endl;
//    std::cout<<" mt_goodElectron: "<<mt_goodMuon<<std::endl;
//    std::cout<<" mt_goodElectron_jesUp: "<<mt_goodMuon_jesUp<<std::endl;
//    std::cout<<" mt_goodElectron_jesDn: "<<mt_goodMuon_jesDn<<std::endl;
//    std::cout<<" mt_goodElectron_uesUp: "<<mt_goodMuon_uesUp<<std::endl;
//    std::cout<<" mt_goodElectron_uesDn: "<<mt_goodMuon_uesDn<<std::endl;
//    std::cout<<" mt_goodElectron_eesUp: "<<mt_goodMuon_eesUp<<std::endl;
//    std::cout<<" mt_goodElectron_eesDn: "<<mt_goodMuon_eesDn<<std::endl;
    pass_wbb_ele_good=kTRUE; 
    nbrEntries_ele_wbb_good_postcut++;
   }
   if( isMC ){
    SF_wjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    SF_wjj_ele_good_IDIsoHLT_errUp = SF_wjj_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
    SF_wjj_ele_good_IDIsoHLT_errDn = SF_wjj_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
   }
  }
  //if( oneQCDElectron && exactly2goodJs ){ // ele qcd'
  if( oneQCDElectron && exactly2goodJs && diJetVVcut && passMET && passMT_qcdEle ){ // ele qcd
  //if( oneQCDElectron && exactly2goodJsOneB && diJetVVcut && passMET && passMT_qcdEle ){ // ele qcd
   pass_wjj_ele_qcd=kTRUE; 
   nbrEntries_ele_wjj_qcd_postcut++;
   if ( exactly2goodBJs ){
    pass_wbb_ele_qcd=kTRUE; 
    nbrEntries_ele_wbb_qcd_postcut++;
   }
   if( isMC ){
    SF_wjj_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso;
    SF_wjj_ele_qcd_IDIsoHLT_errUp = SF_wjj_ele_qcd_IDIsoHLT + SF_qcdEle_IDIso_errUp;
    SF_wjj_ele_qcd_IDIsoHLT_errDn = SF_wjj_ele_qcd_IDIsoHLT - SF_qcdEle_IDIso_errDn;
   }
  }
  // total weight
  if( isMC ){
   // wjj
   weight_wjj_mu_good  = SF_oneGoodBJ * ( SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_mu_qcd   = SF_oneGoodBJ * ( SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_ele_good = SF_oneGoodBJ * ( SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_ele_qcd  = SF_oneGoodBJ * ( SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   // wjj CSV 
   weight_wjj_mu_good_CSVUp    = SF_oneGoodBJ_errUp * ( SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_mu_qcd_CSVUp     = SF_oneGoodBJ_errUp * ( SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_ele_good_CSVUp   = SF_oneGoodBJ_errUp * ( SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_ele_qcd_CSVUp    = SF_oneGoodBJ_errUp * ( SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_mu_good_CSVDown  = SF_oneGoodBJ_errDn * ( SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_mu_qcd_CSVDown   = SF_oneGoodBJ_errDn * ( SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_ele_good_CSVDown = SF_oneGoodBJ_errDn * ( SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_ele_qcd_CSVDown  = SF_oneGoodBJ_errDn * ( SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   // wjj EMu
   weight_wjj_mu_good_EMuUp    = SF_oneGoodBJ  * ( SF_wjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_mu_qcd_EMuUp     = SF_oneGoodBJ  * ( SF_wjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_ele_good_EMuUp   = SF_oneGoodBJ  * ( SF_wjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_ele_qcd_EMuUp    = SF_oneGoodBJ  * ( SF_wjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_mu_good_EMuDown  = SF_oneGoodBJ  * ( SF_wjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_mu_qcd_EMuDown   = SF_oneGoodBJ  * ( SF_wjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents);
   weight_wjj_ele_good_EMuDown = SF_oneGoodBJ  * ( SF_wjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   weight_wjj_ele_qcd_EMuDown  = SF_oneGoodBJ  * ( SF_wjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents);
   // wbb
   weight_wbb_mu_good  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_mu_qcd   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_ele_good = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_ele_qcd  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   // wbb CSV
   weight_wbb_mu_good_CSVUp  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_wbb_mu_qcd_CSVUp   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_wbb_ele_good_CSVUp = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_wbb_ele_qcd_CSVUp  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_wbb_mu_good_CSVDown  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_wbb_mu_qcd_CSVDown   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_wbb_ele_good_CSVDown = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_wbb_ele_qcd_CSVDown  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   // wbb EMu
   weight_wbb_mu_good_EMuUp  = SF_wjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_mu_qcd_EMuUp   = SF_wjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_ele_good_EMuUp = SF_wjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_ele_qcd_EMuUp  = SF_wjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_mu_good_EMuDown  = SF_wjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_mu_qcd_EMuDown   = SF_wjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_ele_good_EMuDown = SF_wjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_wbb_ele_qcd_EMuDown  = SF_wjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
  }
  else{
   // wjj
   weight_wjj_mu_good  = 1.; 
   weight_wjj_mu_qcd   = 1.; 
   weight_wjj_ele_good = 1.; 
   weight_wjj_ele_qcd  = 1.; 
   // wjj CSV
   weight_wjj_mu_good_CSVUp  = 1.; 
   weight_wjj_mu_qcd_CSVUp   = 1.; 
   weight_wjj_ele_good_CSVUp = 1.; 
   weight_wjj_ele_qcd_CSVUp  = 1.; 
   weight_wjj_mu_good_CSVDown  = 1.;
   weight_wjj_mu_qcd_CSVDown   = 1.;
   weight_wjj_ele_good_CSVDown = 1.;
   weight_wjj_ele_qcd_CSVDown  = 1.;
   // wjj EMu
   weight_wjj_mu_good_EMuUp  = 1.; 
   weight_wjj_mu_qcd_EMuUp   = 1.; 
   weight_wjj_ele_good_EMuUp = 1.; 
   weight_wjj_ele_qcd_EMuUp  = 1.; 
   weight_wjj_mu_good_EMuDown  = 1.;
   weight_wjj_mu_qcd_EMuDown   = 1.;
   weight_wjj_ele_good_EMuDown = 1.;
   weight_wjj_ele_qcd_EMuDown  = 1.;
   // wbb
   weight_wbb_mu_good  = 1.; 
   weight_wbb_mu_qcd   = 1.; 
   weight_wbb_ele_good = 1.; 
   weight_wbb_ele_qcd  = 1.; 
   // wbb CSV
   weight_wbb_mu_good_CSVUp  = 1.; 
   weight_wbb_mu_qcd_CSVUp   = 1.; 
   weight_wbb_ele_good_CSVUp = 1.; 
   weight_wbb_ele_qcd_CSVUp  = 1.; 
   weight_wbb_mu_good_CSVDown  = 1.;
   weight_wbb_mu_qcd_CSVDown   = 1.;
   weight_wbb_ele_good_CSVDown = 1.;
   weight_wbb_ele_qcd_CSVDown  = 1.;
   // wbb EMu
   weight_wbb_mu_good_EMuUp  = 1.; 
   weight_wbb_mu_qcd_EMuUp   = 1.; 
   weight_wbb_ele_good_EMuUp = 1.; 
   weight_wbb_ele_qcd_EMuUp  = 1.; 
   weight_wbb_mu_good_EMuDown  = 1.;
   weight_wbb_mu_qcd_EMuDown   = 1.;
   weight_wbb_ele_good_EMuDown = 1.;
   weight_wbb_ele_qcd_EMuDown  = 1.;
  }

  /////////
  // wjj 3
  /////////
  // wjj: simple
  fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                  3, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_wjj_mu_good, weight_wjj_mu_qcd, weight_wjj_ele_good, weight_wjj_ele_qcd
               );
  if( shift=="SFs"){
   // wjj: CSV Up
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wjj_mu_good_CSVUp, weight_wjj_mu_qcd_CSVUp, weight_wjj_ele_good_CSVUp, weight_wjj_ele_qcd_CSVUp
                 );
   // wjj: CSV Down
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wjj_mu_good_CSVDown, weight_wjj_mu_qcd_CSVDown, weight_wjj_ele_good_CSVDown, weight_wjj_ele_qcd_CSVDown
                 );
   // wjj: EMu Up
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wjj_mu_good_EMuUp, weight_wjj_mu_qcd_EMuUp, weight_wjj_ele_good_EMuUp, weight_wjj_ele_qcd_EMuUp
                 );
   // wjj: EMu Down
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wjj_mu_good_EMuDown, weight_wjj_mu_qcd_EMuDown, weight_wjj_ele_good_EMuDown, weight_wjj_ele_qcd_EMuDown
                 );
   // wjj: UES Up
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_wjj_mu_good, weight_wjj_mu_qcd, weight_wjj_ele_good, weight_wjj_ele_qcd
                 );
   // wjj: UES Down
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_wjj_mu_good, weight_wjj_mu_qcd, weight_wjj_ele_good, weight_wjj_ele_qcd
                 );
  }

  /////////
  // wbb 0
  /////////
  // wbb: simple
   if( pass_wbb_mu_good ){
//  std::cout<<"EVENT "<<EVENT<<std::endl;
//  std::cout<<"SF_wjj_mu_good_IDIsoHLT "<<SF_wjj_mu_good_IDIsoHLT <<std::endl;
//  std::cout<<"SF_lumiWeightPU         "<<SF_lumiWeightPU<<std::endl;
//  std::cout<<"lumi_mu                 "<<lumi_mu<<std::endl;
//  std::cout<<"crossSec                "<<crossSec<<std::endl;
//  std::cout<<"SF_CSVrwt2gJs           "<<SF_CSVrwt2gJs<<std::endl;
//  std::cout<<"SF_top2BJs_errUp        "<<SF_top2BJs_errUp<<std::endl;
//  std::cout<<"nrEvents                "<<nrEvents                <<std::endl;       
//   std::cout<<" weight_wbb_mu_good_CSVDn: "<<weight_wbb_mu_good_CSVDown<<std::endl;
//   std::cout<<" weight_wbb_mu_good:       "<<weight_wbb_mu_good<<std::endl;
//   std::cout<<" weight_wbb_mu_good_CSVUp: "<<weight_wbb_mu_good_CSVUp<<std::endl;

//   std::cout<<"  SF_wjj_mu_good_IDIsoHLT: "<<SF_wjj_mu_good_IDIsoHLT<<std::endl;
//   std::cout<<"  SF_lumiWeightPU: "<<SF_lumiWeightPU<<std::endl;
//   std::cout<<"  lumi_mu: "<<lumi_mu<<std::endl;
//   std::cout<<"  crossSec: "<<crossSec<<std::endl;
//   std::cout<<"  SF_CSVrwt2gJs: "<<SF_CSVrwt2gJs<<std::endl;
//   std::cout<<"  SF_top2BJs: "<<SF_top2BJs<<std::endl;
//   std::cout<<"  nrEvents: "<<nrEvents<<std::endl;
  }
  fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                  0, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_wbb_mu_good, weight_wbb_mu_qcd, weight_wbb_ele_good, weight_wbb_ele_qcd
                );
  if( shift=="SFs"){
   // wbb: CSV Up
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_CSVUp, weight_wbb_mu_qcd_CSVUp, weight_wbb_ele_good_CSVUp, weight_wbb_ele_qcd_CSVUp
                 );
   // wbb: CSV Down
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_CSVDown, weight_wbb_mu_qcd_CSVDown, weight_wbb_ele_good_CSVDown, weight_wbb_ele_qcd_CSVDown
                 );
   // wbb: EMu Up
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_EMuUp, weight_wbb_mu_qcd_EMuUp, weight_wbb_ele_good_EMuUp, weight_wbb_ele_qcd_EMuUp
                 );
   // wbb: EMu Down
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_EMuDown, weight_wbb_mu_qcd_EMuDown, weight_wbb_ele_good_EMuDown, weight_wbb_ele_qcd_EMuDown
                 );
   // wbb: UES Up
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_wbb_mu_good, weight_wbb_mu_qcd, weight_wbb_ele_good, weight_wbb_ele_qcd
                 );
   // wbb: UES Down
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_wbb_mu_good, weight_wbb_mu_qcd, weight_wbb_ele_good, weight_wbb_ele_qcd
                 );
  }
  ////////////////////////////////
  // end wjj, wbb Selection 3,0
  ////////////////////////////////

  //////////////////////////
  // begin ttme Selection 1
  //////////////////////////
  Bool_t pass_ttme_mu_good=kFALSE;
  Bool_t pass_ttme_mu_qcd=kFALSE;
  Bool_t pass_ttme_ele_good=kFALSE;
  Bool_t pass_ttme_ele_qcd=kFALSE;
  if( twoGoodLMuE && exactly2goodBJs && passMET && passMT_goodMu ){ // mu good
   pass_ttme_mu_good=kTRUE; 
   nbrEntries_mu_ttme_good_postcut++;
   if( isMC ){
    SF_ttme_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(0);
    SF_ttme_mu_good_IDIsoHLT_errUp = SF_ttme_mu_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIso_errUp->at(0),2) );
    SF_ttme_mu_good_IDIsoHLT_errDn = SF_ttme_mu_good_IDIsoHLT
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIso_errDn->at(0),2) );
   }
  }
  if( twoGoodLEMu && exactly2goodBJs && passMET && passMT_qcdMu ){ // ele good
   pass_ttme_ele_good=kTRUE; 
   nbrEntries_ele_ttme_good_postcut++;
   if( isMC ){
    SF_ttme_ele_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(0); 
    SF_ttme_ele_good_IDIsoHLT_errUp = SF_ttme_ele_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIso_errUp->at(0),2) );
    SF_ttme_ele_good_IDIsoHLT_errDn = SF_ttme_ele_good_IDIsoHLT
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIso_errDn->at(0),2) );
   }
  }
  if( twoQCDLMuE && exactly2goodBJs && passMET && passMT_goodEle ){ // mu qcd
   pass_ttme_mu_qcd=kTRUE; 
   nbrEntries_mu_ttme_qcd_postcut++;
   if( isMC ){
     SF_ttme_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso * SF_goodEle_IDIso->at(0); 
     SF_ttme_mu_qcd_IDIsoHLT_errUp = SF_ttme_mu_qcd_IDIsoHLT 
      + std::sqrt( pow(SF_qcdMu_IDIso_errUp,2) + pow(SF_goodEle_IDIso_errUp->at(0),2) );
     SF_ttme_mu_qcd_IDIsoHLT_errDn = SF_ttme_mu_qcd_IDIsoHLT
      - std::sqrt( pow(SF_qcdMu_IDIso_errDn,2) + pow(SF_goodEle_IDIso_errDn->at(0),2));
   }
  }
  if( twoQCDLEMu && exactly2goodBJs && passMET && passMT_qcdEle ){ // ele qcd
   pass_ttme_ele_qcd=kTRUE; 
   nbrEntries_ele_ttme_qcd_postcut++;
   if( isMC ){
     SF_ttme_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso * SF_goodMu_IDIso->at(0); 
     SF_ttme_ele_qcd_IDIsoHLT_errUp = SF_ttme_ele_qcd_IDIsoHLT 
      + std::sqrt( pow(SF_qcdEle_IDIso_errUp,2) + pow(SF_goodMu_IDIso_errUp->at(0),2) );
     SF_ttme_ele_qcd_IDIsoHLT_errDn = SF_ttme_ele_qcd_IDIsoHLT
      - std::sqrt( pow(SF_qcdEle_IDIso_errDn,2) + pow(SF_goodMu_IDIso_errDn->at(0),2));
   }
  }
  // total weight
  if( isMC ){
   // ttme 
   weight_ttme_mu_good  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_mu_qcd   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_ele_qcd  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   // ttme CSV
   weight_ttme_mu_good_CSVUp  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttme_mu_qcd_CSVUp   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttme_ele_good_CSVUp = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttme_ele_qcd_CSVUp  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttme_mu_good_CSVDown  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_ttme_mu_qcd_CSVDown   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_ttme_ele_good_CSVDown = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_ttme_ele_qcd_CSVDown  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   // ttme EMu
   weight_ttme_mu_good_EMuUp  = SF_ttme_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_mu_qcd_EMuUp   = SF_ttme_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_ele_good_EMuUp = SF_ttme_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_ele_qcd_EMuUp  = SF_ttme_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_mu_good_EMuDown  = SF_ttme_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_mu_qcd_EMuDown   = SF_ttme_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_ele_good_EMuDown = SF_ttme_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme_ele_qcd_EMuDown  = SF_ttme_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
  }
  else{
   // ttme
   weight_ttme_mu_good  = 1.; 
   weight_ttme_mu_qcd   = 1.; 
   weight_ttme_ele_good = 1.; 
   weight_ttme_ele_qcd  = 1.; 
   // ttme CSV
   weight_ttme_mu_good_CSVUp  = 1.; 
   weight_ttme_mu_qcd_CSVUp   = 1.; 
   weight_ttme_ele_good_CSVUp = 1.; 
   weight_ttme_ele_qcd_CSVUp  = 1.; 
   weight_ttme_mu_good_CSVDown  = 1.;
   weight_ttme_mu_qcd_CSVDown   = 1.;
   weight_ttme_ele_good_CSVDown = 1.;
   weight_ttme_ele_qcd_CSVDown  = 1.;
   // ttme EMu
   weight_ttme_mu_good_EMuUp  = 1.; 
   weight_ttme_mu_qcd_EMuUp   = 1.; 
   weight_ttme_ele_good_EMuUp = 1.; 
   weight_ttme_ele_qcd_EMuUp  = 1.; 
   weight_ttme_mu_good_EMuDown  = 1.;
   weight_ttme_mu_qcd_EMuDown   = 1.;
   weight_ttme_ele_good_EMuDown = 1.;
   weight_ttme_ele_qcd_EMuDown  = 1.;
  }

  // ttme: simple
  fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                  1, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme_mu_good, weight_ttme_mu_qcd, weight_ttme_ele_good, weight_ttme_ele_qcd
                );
  if( shift=="SFs"){
   // ttme: CSV Up
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_CSVUp, weight_ttme_mu_qcd_CSVUp, weight_ttme_ele_good_CSVUp, weight_ttme_ele_qcd_CSVUp
                 );
   // ttme: CSV Down
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_CSVDown, weight_ttme_mu_qcd_CSVDown, weight_ttme_ele_good_CSVDown, weight_ttme_ele_qcd_CSVDown
                 );
   // ttme: EMu Up
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_EMuUp, weight_ttme_mu_qcd_EMuUp, weight_ttme_ele_good_EMuUp, weight_ttme_ele_qcd_EMuUp
                 );
   // ttme: EMu Down
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_EMuDown, weight_ttme_mu_qcd_EMuDown, weight_ttme_ele_good_EMuDown, weight_ttme_ele_qcd_EMuDown
                 );
   // ttme: UES Up
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_ttme_mu_good, weight_ttme_mu_qcd, weight_ttme_ele_good, weight_ttme_ele_qcd
                 );
   // ttme: UES Down
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_ttme_mu_good, weight_ttme_mu_qcd, weight_ttme_ele_good, weight_ttme_ele_qcd
                 );
  }
  //////////////////////////
  // end ttme Selection 1
  //////////////////////////

  //////////////////////////
  // begin ttjjj Selection 2
  //////////////////////////
  Bool_t pass_ttjjj_mu_good=kFALSE;
  Bool_t pass_ttjjj_mu_qcd=kFALSE;
  Bool_t pass_ttjjj_ele_good=kFALSE;
  Bool_t pass_ttjjj_ele_qcd=kFALSE;
  if( oneGoodMuon && min3gJs2gBJs && passMET && passMT_goodMu ){ // mu good
   pass_ttjjj_mu_good=kTRUE;
   nbrEntries_mu_ttjjj_good_postcut++;
   if( isMC ){
    SF_ttjjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    SF_ttjjj_mu_good_IDIsoHLT_errUp = SF_ttjjj_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
    SF_ttjjj_mu_good_IDIsoHLT_errDn = SF_ttjjj_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDMuon && min3gJs2gBJs && passMET && passMT_qcdMu ){ // mu qcd
   pass_ttjjj_mu_qcd=kTRUE;
   nbrEntries_mu_ttjjj_qcd_postcut++;
   if( isMC ){
    SF_ttjjj_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
    SF_ttjjj_mu_qcd_IDIsoHLT_errUp = SF_ttjjj_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
    SF_ttjjj_mu_qcd_IDIsoHLT_errDn = SF_ttjjj_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
   }
  }
  if( oneGoodElectron && min3gJs2gBJs && passMET && passMT_goodEle ){ // ele good
   pass_ttjjj_ele_good=kTRUE;
   nbrEntries_ele_ttjjj_good_postcut++;
   if( isMC ){
    SF_ttjjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    SF_ttjjj_ele_good_IDIsoHLT_errUp = SF_ttjjj_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
    SF_ttjjj_ele_good_IDIsoHLT_errDn = SF_ttjjj_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDElectron && min3gJs2gBJs && passMET && passMT_qcdEle ){ // ele qcd
   pass_ttjjj_ele_qcd=kTRUE;
   nbrEntries_ele_ttjjj_qcd_postcut++;
   if( isMC ){
    SF_ttjjj_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso;
    SF_ttjjj_ele_qcd_IDIsoHLT_errUp = SF_ttjjj_ele_qcd_IDIsoHLT + SF_qcdEle_IDIso_errUp;
    SF_ttjjj_ele_qcd_IDIsoHLT_errDn = SF_ttjjj_ele_qcd_IDIsoHLT - SF_qcdEle_IDIso_errDn;
   }
  }

  // total weight
  if( isMC ){
   // ttjjj 
   weight_ttjjj_mu_good  = SF_ttjjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_qcd   = SF_ttjjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_good = SF_ttjjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_qcd  = SF_ttjjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   // ttjjj CSV
   weight_ttjjj_mu_good_CSVUp  = SF_ttjjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_mu_qcd_CSVUp   = SF_ttjjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_ele_good_CSVUp = SF_ttjjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_ele_qcd_CSVUp  = SF_ttjjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_mu_good_CSVDown  = SF_ttjjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_ttjjj_mu_qcd_CSVDown   = SF_ttjjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_ttjjj_ele_good_CSVDown = SF_ttjjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_ttjjj_ele_qcd_CSVDown  = SF_ttjjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   // ttjjj EMu
   weight_ttjjj_mu_good_EMuUp  = SF_ttjjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_qcd_EMuUp   = SF_ttjjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_good_EMuUp = SF_ttjjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_qcd_EMuUp  = SF_ttjjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_good_EMuDown  = SF_ttjjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_qcd_EMuDown   = SF_ttjjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_good_EMuDown = SF_ttjjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_qcd_EMuDown  = SF_ttjjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
  }
  else{
   // ttjjj
   weight_ttjjj_mu_good  = 1.; 
   weight_ttjjj_mu_qcd   = 1.; 
   weight_ttjjj_ele_good = 1.; 
   weight_ttjjj_ele_qcd  = 1.; 
   // ttjjj CSV
   weight_ttjjj_mu_good_CSVUp  = 1.; 
   weight_ttjjj_mu_qcd_CSVUp   = 1.; 
   weight_ttjjj_ele_good_CSVUp = 1.; 
   weight_ttjjj_ele_qcd_CSVUp  = 1.; 
   weight_ttjjj_mu_good_CSVDown  = 1.;
   weight_ttjjj_mu_qcd_CSVDown   = 1.;
   weight_ttjjj_ele_good_CSVDown = 1.;
   weight_ttjjj_ele_qcd_CSVDown  = 1.;
   // ttjjj EMu
   weight_ttjjj_mu_good_EMuUp  = 1.; 
   weight_ttjjj_mu_qcd_EMuUp   = 1.; 
   weight_ttjjj_ele_good_EMuUp = 1.; 
   weight_ttjjj_ele_qcd_EMuUp  = 1.; 
   weight_ttjjj_mu_good_EMuDown  = 1.;
   weight_ttjjj_mu_qcd_EMuDown   = 1.;
   weight_ttjjj_ele_good_EMuDown = 1.;
   weight_ttjjj_ele_qcd_EMuDown  = 1.;
  }

  // ttjjj: simple
  fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                  2, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttjjj_mu_good, weight_ttjjj_mu_qcd, weight_ttjjj_ele_good, weight_ttjjj_ele_qcd
                );
  if( shift=="SFs"){
   // ttjjj: CSV Up
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_CSVUp, weight_ttjjj_mu_qcd_CSVUp, weight_ttjjj_ele_good_CSVUp, weight_ttjjj_ele_qcd_CSVUp
                 );
   // ttjjj: CSV Down
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_CSVDown, weight_ttjjj_mu_qcd_CSVDown, weight_ttjjj_ele_good_CSVDown, weight_ttjjj_ele_qcd_CSVDown
                 );
   // ttjjj: EMu Up
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_EMuUp, weight_ttjjj_mu_qcd_EMuUp, weight_ttjjj_ele_good_EMuUp, weight_ttjjj_ele_qcd_EMuUp
                 );
   // ttjjj: EMu Down
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_EMuDown, weight_ttjjj_mu_qcd_EMuDown, weight_ttjjj_ele_good_EMuDown, weight_ttjjj_ele_qcd_EMuDown
                 );
   // ttjjj: UES Up
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_ttjjj_mu_good, weight_ttjjj_mu_qcd, weight_ttjjj_ele_good, weight_ttjjj_ele_qcd
                 );
   // ttjjj: UES Down
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_ttjjj_mu_good, weight_ttjjj_mu_qcd, weight_ttjjj_ele_good, weight_ttjjj_ele_qcd
                 );
  }
  //////////////////////////
  // end ttjjj Selection 2
  //////////////////////////

  //////////////////////////
  // begin stt Selection 4
  //////////////////////////
  Bool_t pass_stt_mu_good=kFALSE;
  Bool_t pass_stt_mu_qcd=kFALSE;
  Bool_t pass_stt_ele_good=kFALSE;
  Bool_t pass_stt_ele_qcd=kFALSE;
  if( oneGoodMuon && aGoodBJaFwdJ && passMET && passMT_goodMu ){ // mu good
   pass_stt_mu_good=kTRUE;
   nbrEntries_mu_stt_good_postcut++;
   if( isMC ){
    SF_stt_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    SF_stt_mu_good_IDIsoHLT_errUp = SF_stt_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
    SF_stt_mu_good_IDIsoHLT_errDn = SF_stt_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDMuon && aGoodBJaFwdJ && passMET && passMT_qcdMu ){ // mu qcd
   pass_stt_mu_qcd=kTRUE;
   nbrEntries_mu_stt_qcd_postcut++;
   if( isMC ){
    SF_stt_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
    SF_stt_mu_qcd_IDIsoHLT_errUp = SF_stt_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
    SF_stt_mu_qcd_IDIsoHLT_errDn = SF_stt_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
   }
  }
  if( oneGoodElectron && aGoodBJaFwdJ && passMET && passMT_goodEle ){ // ele good
   pass_stt_ele_good=kTRUE;
   nbrEntries_ele_stt_good_postcut++;
   if( isMC ){
    SF_stt_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    SF_stt_ele_good_IDIsoHLT_errUp = SF_stt_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
    SF_stt_ele_good_IDIsoHLT_errDn = SF_stt_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDElectron && aGoodBJaFwdJ && passMET && passMT_qcdEle ){ // ele qcd
   pass_stt_ele_qcd=kTRUE;
   nbrEntries_ele_stt_qcd_postcut++;
   if( isMC ){
    SF_stt_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso;
    SF_stt_ele_qcd_IDIsoHLT_errUp = SF_stt_ele_qcd_IDIsoHLT + SF_qcdEle_IDIso_errUp;
    SF_stt_ele_qcd_IDIsoHLT_errDn = SF_stt_ele_qcd_IDIsoHLT - SF_qcdEle_IDIso_errDn;
   }
  }

  // total weight
  if( isMC ){
   // stt 
   weight_stt_mu_good  = SF_stt_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_mu_qcd   = SF_stt_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_ele_good = SF_stt_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_ele_qcd  = SF_stt_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   // stt CSV
   weight_stt_mu_good_CSVUp  = SF_stt_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errUp / nrEvents;
   weight_stt_mu_qcd_CSVUp   = SF_stt_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errUp / nrEvents;
   weight_stt_ele_good_CSVUp = SF_stt_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errUp / nrEvents;
   weight_stt_ele_qcd_CSVUp  = SF_stt_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errUp / nrEvents;
   weight_stt_mu_good_CSVDown  = SF_stt_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errDn / nrEvents;
   weight_stt_mu_qcd_CSVDown   = SF_stt_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errDn / nrEvents;
   weight_stt_ele_good_CSVDown = SF_stt_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errDn / nrEvents;
   weight_stt_ele_qcd_CSVDown  = SF_stt_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ_errDn / nrEvents;
   // stt EMu
   weight_stt_mu_good_EMuUp  = SF_stt_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_mu_qcd_EMuUp   = SF_stt_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_ele_good_EMuUp = SF_stt_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_ele_qcd_EMuUp  = SF_stt_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_mu_good_EMuDown  = SF_stt_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_mu_qcd_EMuDown   = SF_stt_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_ele_good_EMuDown = SF_stt_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
   weight_stt_ele_qcd_EMuDown  = SF_stt_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwtgJfJ * SF_oneGoodBJ / nrEvents;
  }
  else{
   // stt
   weight_stt_mu_good  = 1.; 
   weight_stt_mu_qcd   = 1.; 
   weight_stt_ele_good = 1.; 
   weight_stt_ele_qcd  = 1.; 
   // stt CSV
   weight_stt_mu_good_CSVUp  = 1.; 
   weight_stt_mu_qcd_CSVUp   = 1.; 
   weight_stt_ele_good_CSVUp = 1.; 
   weight_stt_ele_qcd_CSVUp  = 1.; 
   weight_stt_mu_good_CSVDown  = 1.;
   weight_stt_mu_qcd_CSVDown   = 1.;
   weight_stt_ele_good_CSVDown = 1.;
   weight_stt_ele_qcd_CSVDown  = 1.;
   // stt EMu
   weight_stt_mu_good_EMuUp  = 1.; 
   weight_stt_mu_qcd_EMuUp   = 1.; 
   weight_stt_ele_good_EMuUp = 1.; 
   weight_stt_ele_qcd_EMuUp  = 1.; 
   weight_stt_mu_good_EMuDown  = 1.;
   weight_stt_mu_qcd_EMuDown   = 1.;
   weight_stt_ele_good_EMuDown = 1.;
   weight_stt_ele_qcd_EMuDown  = 1.;
  }

  // stt: simple
  fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                  4, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_stt_mu_good, weight_stt_mu_qcd, weight_stt_ele_good, weight_stt_ele_qcd
                );
  if( shift=="SFs"){
   // stt: CSV Up
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_CSVUp, weight_stt_mu_qcd_CSVUp, weight_stt_ele_good_CSVUp, weight_stt_ele_qcd_CSVUp
                 );
   // stt: CSV Down
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_CSVDown, weight_stt_mu_qcd_CSVDown, weight_stt_ele_good_CSVDown, weight_stt_ele_qcd_CSVDown
                 );
   // stt: EMu Up
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_EMuUp, weight_stt_mu_qcd_EMuUp, weight_stt_ele_good_EMuUp, weight_stt_ele_qcd_EMuUp
                 );
   // stt: EMu Down
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_EMuDown, weight_stt_mu_qcd_EMuDown, weight_stt_ele_good_EMuDown, weight_stt_ele_qcd_EMuDown
                 );
   // stt: UES Up
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_stt_mu_good, weight_stt_mu_qcd, weight_stt_ele_good, weight_stt_ele_qcd
                 );
   // stt: UES Down
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_stt_mu_good, weight_stt_mu_qcd, weight_stt_ele_good, weight_stt_ele_qcd
                 );
  }

  //////////////////////////
  // end stt Selection 4
  //////////////////////////

  ////////////////////////////////
  // begin dybb, dyjj Selection 5,6
  ////////////////////////////////
  Bool_t pass_dyjj_mu_good=kFALSE;
  Bool_t pass_dyjj_mu_qcd=kFALSE;
  Bool_t pass_dybb_mu_good=kFALSE;
  Bool_t pass_dybb_mu_qcd=kFALSE;
  Bool_t pass_dyjj_ele_good=kFALSE;
  Bool_t pass_dyjj_ele_qcd=kFALSE;
  Bool_t pass_dybb_ele_good=kFALSE;
  Bool_t pass_dybb_ele_qcd=kFALSE;
  //if( twoGoodMuons && exactly2goodJs ){ // mu good
  if( twoGoodMuons && exactly2goodJsOneB ){ // mu good
   pass_dyjj_mu_good=kTRUE; 
   nbrEntries_mu_dyjj_good_postcut++;
   if ( exactly2goodBJs ){
    pass_dybb_mu_good=kTRUE; 
    nbrEntries_mu_dybb_good_postcut++;
   }
   if( isMC ){
    SF_dyjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodMu_IDIso->at(1);
    SF_dyjj_mu_good_IDIsoHLT_errUp = SF_dyjj_mu_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodMu_IDIso_errUp->at(1),2) );
    SF_dyjj_mu_good_IDIsoHLT_errDn = SF_dyjj_mu_good_IDIsoHLT 
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodMu_IDIso_errDn->at(1),2) );
   }
  }
  //if( twoQCDMuons && exactly2goodJs ){ // mu qcd
  if( twoQCDMuons && exactly2goodJsOneB ){ // mu qcd
   pass_dyjj_mu_qcd=kTRUE; 
   nbrEntries_mu_dyjj_qcd_postcut++;
   if ( exactly2goodBJs ){
    pass_dybb_mu_qcd=kTRUE; 
    nbrEntries_mu_dybb_qcd_postcut++;
   }
   if( isMC ){
    SF_dyjj_mu_qcd_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_qcdMu_IDIso;
    SF_dyjj_mu_qcd_IDIsoHLT_errUp = SF_dyjj_mu_qcd_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_qcdMu_IDIso_errUp,2) );
    SF_dyjj_mu_qcd_IDIsoHLT_errDn = SF_dyjj_mu_qcd_IDIsoHLT 
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_qcdMu_IDIso_errDn,2) );
   }
  }
  //if( twoGoodElectrons && exactly2goodJs ){ // ele good
  if( twoGoodElectrons && exactly2goodJsOneB ){ // ele good
   pass_dyjj_ele_good=kTRUE; 
   nbrEntries_ele_dyjj_good_postcut++;
   if ( exactly2goodBJs ){
    pass_dybb_ele_good=kTRUE; 
    nbrEntries_ele_dybb_good_postcut++;
   }
   if( isMC ){
    SF_dyjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(1);
    SF_dyjj_ele_good_IDIsoHLT_errUp = SF_dyjj_ele_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIso_errUp->at(1),2) );
    SF_dyjj_ele_good_IDIsoHLT_errDn = SF_dyjj_ele_good_IDIsoHLT 
     - std::sqrt( pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIso_errDn->at(1),2) );
   }
  }
  //if( twoQCDElectrons && exactly2goodJs ){ // ele qcd
  if( twoQCDElectrons && exactly2goodJsOneB ){ // ele qcd
   pass_dyjj_ele_qcd=kTRUE; 
   nbrEntries_ele_dyjj_qcd_postcut++;
   if ( exactly2goodBJs ){
    pass_dybb_ele_qcd=kTRUE; 
    nbrEntries_ele_dybb_qcd_postcut++;
   }
   if( isMC ){
    SF_dyjj_ele_qcd_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_qcdEle_IDIso;
    SF_dyjj_ele_qcd_IDIsoHLT_errUp = SF_dyjj_ele_qcd_IDIsoHLT 
     + std::sqrt( pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) + pow(SF_qcdEle_IDIso_errUp,2) );
    SF_dyjj_ele_qcd_IDIsoHLT_errDn = SF_dyjj_ele_qcd_IDIsoHLT 
     - std::sqrt( pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) + pow(SF_qcdEle_IDIso_errDn,2) );
   }
  }
  // total weight
  if( isMC ){
   // dyjj
   weight_dyjj_mu_good  = SF_oneGoodBJ * ( SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_mu_qcd   = SF_oneGoodBJ * ( SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_ele_good = SF_oneGoodBJ * ( SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_ele_qcd  = SF_oneGoodBJ * ( SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   // dyjj CSV
   weight_dyjj_mu_good_CSVUp    = SF_oneGoodBJ_errUp * ( SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_mu_qcd_CSVUp     = SF_oneGoodBJ_errUp * ( SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_ele_good_CSVUp   = SF_oneGoodBJ_errUp * ( SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_ele_qcd_CSVUp    = SF_oneGoodBJ_errUp * ( SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_mu_good_CSVDown  = SF_oneGoodBJ_errDn * ( SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_mu_qcd_CSVDown   = SF_oneGoodBJ_errDn * ( SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_ele_good_CSVDown = SF_oneGoodBJ_errDn * ( SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_ele_qcd_CSVDown  = SF_oneGoodBJ_errDn * ( SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   // dyjj EMu
   weight_dyjj_mu_good_EMuUp    = SF_oneGoodBJ * ( SF_dyjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_mu_qcd_EMuUp     = SF_oneGoodBJ * ( SF_dyjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_ele_good_EMuUp   = SF_oneGoodBJ * ( SF_dyjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_ele_qcd_EMuUp    = SF_oneGoodBJ * ( SF_dyjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_mu_good_EMuDown  = SF_oneGoodBJ * ( SF_dyjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_mu_qcd_EMuDown   = SF_oneGoodBJ * ( SF_dyjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
   weight_dyjj_ele_good_EMuDown = SF_oneGoodBJ * ( SF_dyjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   weight_dyjj_ele_qcd_EMuDown  = SF_oneGoodBJ * ( SF_dyjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
   // dybb
   weight_dybb_mu_good  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_mu_qcd   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_ele_good = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_ele_qcd  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   // dybb CSV
   weight_dybb_mu_good_CSVUp  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_dybb_mu_qcd_CSVUp   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_dybb_ele_good_CSVUp = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_dybb_ele_qcd_CSVUp  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errUp / nrEvents;
   weight_dybb_mu_good_CSVDown  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_dybb_mu_qcd_CSVDown   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_dybb_ele_good_CSVDown = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   weight_dybb_ele_qcd_CSVDown  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs_errDn / nrEvents;
   // dybb EMu
   weight_dybb_mu_good_EMuUp  = SF_dyjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_mu_qcd_EMuUp   = SF_dyjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_ele_good_EMuUp = SF_dyjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_ele_qcd_EMuUp  = SF_dyjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_mu_good_EMuDown  = SF_dyjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_mu_qcd_EMuDown   = SF_dyjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_ele_good_EMuDown = SF_dyjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_dybb_ele_qcd_EMuDown  = SF_dyjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
  }
  else{
   // dyjj
   weight_dyjj_mu_good  = 1.; 
   weight_dyjj_mu_qcd   = 1.; 
   weight_dyjj_ele_good = 1.; 
   weight_dyjj_ele_qcd  = 1.; 
   // dyjj CSV
   weight_dyjj_mu_good_CSVUp  = 1.; 
   weight_dyjj_mu_qcd_CSVUp   = 1.; 
   weight_dyjj_ele_good_CSVUp = 1.; 
   weight_dyjj_ele_qcd_CSVUp  = 1.; 
   weight_dyjj_mu_good_CSVDown  = 1.;
   weight_dyjj_mu_qcd_CSVDown   = 1.;
   weight_dyjj_ele_good_CSVDown = 1.;
   weight_dyjj_ele_qcd_CSVDown  = 1.;
   // dyjj EMu
   weight_dyjj_mu_good_EMuUp  = 1.; 
   weight_dyjj_mu_qcd_EMuUp   = 1.; 
   weight_dyjj_ele_good_EMuUp = 1.; 
   weight_dyjj_ele_qcd_EMuUp  = 1.; 
   weight_dyjj_mu_good_EMuDown  = 1.;
   weight_dyjj_mu_qcd_EMuDown   = 1.;
   weight_dyjj_ele_good_EMuDown = 1.;
   weight_dyjj_ele_qcd_EMuDown  = 1.;
   // dybb
   weight_dybb_mu_good  = 1.; 
   weight_dybb_mu_qcd   = 1.; 
   weight_dybb_ele_good = 1.; 
   weight_dybb_ele_qcd  = 1.; 
   // dybb CSV
   weight_dybb_mu_good_CSVUp  = 1.; 
   weight_dybb_mu_qcd_CSVUp   = 1.; 
   weight_dybb_ele_good_CSVUp = 1.; 
   weight_dybb_ele_qcd_CSVUp  = 1.; 
   weight_dybb_mu_good_CSVDown  = 1.;
   weight_dybb_mu_qcd_CSVDown   = 1.;
   weight_dybb_ele_good_CSVDown = 1.;
   weight_dybb_ele_qcd_CSVDown  = 1.;
   // dybb EMu
   weight_dybb_mu_good_EMuUp  = 1.; 
   weight_dybb_mu_qcd_EMuUp   = 1.; 
   weight_dybb_ele_good_EMuUp = 1.; 
   weight_dybb_ele_qcd_EMuUp  = 1.; 
   weight_dybb_mu_good_EMuDown  = 1.;
   weight_dybb_mu_qcd_EMuDown   = 1.;
   weight_dybb_ele_good_EMuDown = 1.;
   weight_dybb_ele_qcd_EMuDown  = 1.;
  }

  /////////
  // dyjj 6
  /////////
  // dyjj: simple
  fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                  6, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_dyjj_mu_good, weight_dyjj_mu_qcd, weight_dyjj_ele_good, weight_dyjj_ele_qcd
               );
  if( shift=="SFs"){
   // dyjj: CSV Up
   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                   6, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dyjj_mu_good_CSVUp, weight_dyjj_mu_qcd_CSVUp, weight_dyjj_ele_good_CSVUp, weight_dyjj_ele_qcd_CSVUp
                 );
   // dyjj: CSV Down
   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                   6, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dyjj_mu_good_CSVDown, weight_dyjj_mu_qcd_CSVDown, weight_dyjj_ele_good_CSVDown, weight_dyjj_ele_qcd_CSVDown
                 );
   // dyjj: EMu Up
   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                   6, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dyjj_mu_good_EMuUp, weight_dyjj_mu_qcd_EMuUp, weight_dyjj_ele_good_EMuUp, weight_dyjj_ele_qcd_EMuUp
                 );
   // dyjj: EMu Down
   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                   6, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dyjj_mu_good_EMuDown, weight_dyjj_mu_qcd_EMuDown, weight_dyjj_ele_good_EMuDown, weight_dyjj_ele_qcd_EMuDown
                 );
   // dyjj: UES Up
   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                   6, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_dyjj_mu_good, weight_dyjj_mu_qcd, weight_dyjj_ele_good, weight_dyjj_ele_qcd
                 );
   // dyjj: UES Down
   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
                   6, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_dyjj_mu_good, weight_dyjj_mu_qcd, weight_dyjj_ele_good, weight_dyjj_ele_qcd
                 );
  }

  /////////
  // dybb 5
  /////////
  // dybb: simple
  fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                  5, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_dybb_mu_good, weight_dybb_mu_qcd, weight_dybb_ele_good, weight_dybb_ele_qcd
                );
  if( shift=="SFs"){
   // dybb: CSV Up
   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                   5, 1,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dybb_mu_good_CSVUp, weight_dybb_mu_qcd_CSVUp, weight_dybb_ele_good_CSVUp, weight_dybb_ele_qcd_CSVUp
                 );
   // dybb: CSV Down
   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                   5, 2,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dybb_mu_good_CSVDown, weight_dybb_mu_qcd_CSVDown, weight_dybb_ele_good_CSVDown, weight_dybb_ele_qcd_CSVDown
                 );
   // dybb: EMu Up
   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                   5, 3,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dybb_mu_good_EMuUp, weight_dybb_mu_qcd_EMuUp, weight_dybb_ele_good_EMuUp, weight_dybb_ele_qcd_EMuUp
                 );
   // dybb: EMu Down
   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                   5, 4,
                   MET_pt, MET_phi,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_dybb_mu_good_EMuDown, weight_dybb_mu_qcd_EMuDown, weight_dybb_ele_good_EMuDown, weight_dybb_ele_qcd_EMuDown
                 );
   // dybb: UES Up
   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                   5, 5,
                   MET_pt_uesUp, MET_phi_uesUp,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_dybb_mu_good, weight_dybb_mu_qcd, weight_dybb_ele_good, weight_dybb_ele_qcd
                 );
   // dybb: UES Down
   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
                   5, 6,
                   MET_pt_uesDown, MET_phi_uesDown,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_dybb_mu_good, weight_dybb_mu_qcd, weight_dybb_ele_good, weight_dybb_ele_qcd
                 );
  }
  ////////////////////////////////
  // end dybb, dyjj Selection 5,6
  ////////////////////////////////

 } 

 // write a log
 std::ofstream logfile (outfileName+".log", std::ofstream::out);
 logfile<<"isMC = "<<isMC<<std::endl;
 logfile<<"shift = "<<shift<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--                 W+bb Selection                  --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_wbb_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_wbb_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_wbb_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_wbb_qcd_postcut<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--                TT(me) Selection               --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_ttme_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_ttme_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_ttme_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_ttme_qcd_postcut<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--                 TT(jjj) Selection                --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_ttjjj_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_ttjjj_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_ttjjj_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_ttjjj_qcd_postcut<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--                  W+jj Selection                 --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_wjj_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_wjj_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_wjj_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_wjj_qcd_postcut<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--             Single Top (t) Selection            --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_stt_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_stt_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_stt_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_stt_qcd_postcut<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--              Drell-Yan+jj Selection             --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_dyjj_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_dyjj_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_dyjj_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_dyjj_qcd_postcut<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"--              Drell-Yan+bb Selection             --"<<std::endl;
 logfile<<"-----------------------------------------------------"<<std::endl;
 logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_dybb_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_dybb_qcd_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_dybb_good_postcut<<std::endl;
 logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_dybb_qcd_postcut<<std::endl;
 logfile.close();
 

 // write these histograms to file
 TFile *outfile = new TFile(outfileName,"RECREATE");
 outfile->cd();
 
 // wbb
 writeHistWriter( 0, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 0, 1, isW );
  writeHistWriter( 0, 2, isW );
  writeHistWriter( 0, 3, isW );
  writeHistWriter( 0, 4, isW );
  writeHistWriter( 0, 5, isW );
  writeHistWriter( 0, 6, isW );
 }
 // ttme
 writeHistWriter( 1, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 1, 1, isW );
  writeHistWriter( 1, 2, isW );
  writeHistWriter( 1, 3, isW );
  writeHistWriter( 1, 4, isW );
  writeHistWriter( 1, 5, isW );
  writeHistWriter( 1, 6, isW );
 }
 // ttjjj
 writeHistWriter( 2, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 2, 1, isW );
  writeHistWriter( 2, 2, isW );
  writeHistWriter( 2, 3, isW );
  writeHistWriter( 2, 4, isW );
  writeHistWriter( 2, 5, isW );
  writeHistWriter( 2, 6, isW );
 }
 // wjj
 writeHistWriter( 3, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 3, 1, isW );
  writeHistWriter( 3, 2, isW );
  writeHistWriter( 3, 3, isW );
  writeHistWriter( 3, 4, isW );
  writeHistWriter( 3, 5, isW );
  writeHistWriter( 3, 6, isW );
 }
 // stt
 writeHistWriter( 4, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 4, 1, isW );
  writeHistWriter( 4, 2, isW );
  writeHistWriter( 4, 3, isW );
  writeHistWriter( 4, 4, isW );
  writeHistWriter( 4, 5, isW );
  writeHistWriter( 4, 6, isW );
 }
 // dybb
 writeHistWriter( 5, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 5, 1, isW );
  writeHistWriter( 5, 2, isW );
  writeHistWriter( 5, 3, isW );
  writeHistWriter( 5, 4, isW );
  writeHistWriter( 5, 5, isW );
  writeHistWriter( 5, 6, isW );
 }
 // dyjj
 writeHistWriter( 6, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 6, 1, isW );
  writeHistWriter( 6, 2, isW );
  writeHistWriter( 6, 3, isW );
  writeHistWriter( 6, 4, isW );
  writeHistWriter( 6, 5, isW );
  writeHistWriter( 6, 6, isW );
 }

 outfile->Close();
 std::cout<<" Done "<<std::endl;
}

