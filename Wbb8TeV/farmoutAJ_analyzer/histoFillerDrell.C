#define histoFillerDrell_cxx
#include "histoFillerDrell.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>
//#include <cmath>

void histoFillerDrell::Loop(
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
  //std::cout<<"    entry "<<jentry<<std::endl;
  //if(jentry%100000==0) std::cout<<"    entry "<<jentry<<std::endl;
  Long64_t ientry = LoadTree(jentry);
  if (ientry < 0) break;
  nb = fChain->GetEntry(jentry);
  if(!nb){std::cout<<"histoFillerDrell.C can't fChain->GetEntry(jentry)"<<std::endl;}

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
   nrW3J = 29503114; // for Schweincomp // else 30358906;
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

  g1CJ = goodJ1_pt>25;
  g2CJ = g1CJ && goodJ2_pt>25;
  e2CJ = g2CJ && goodJ3_pt<25;
  xFJ = fwdJ1_pt<25;
  mB1 = goodJ1_CSV>0.679;
  tB1 = goodJ1_CSV>0.898;
  mB2 = mB1 && goodJ2_CSV>0.679;
  tB2 = tB1 && goodJ2_CSV>0.898;

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
  SF_mB1 = goodJ1_SF_CSVM;
  SF_mB2 = goodJ1_SF_CSVM * goodJ2_SF_CSVM;
  SF_tB1 = goodJ1_SF_CSVT;
  SF_tB2 = goodJ1_SF_CSVT * goodJ2_SF_CSVT;
  SF_mB1_errUp = goodJ1_SF_CSVM_errUp;
  SF_mB2_errUp = goodJ1_SF_CSVM_errUp * goodJ2_SF_CSVM_errUp;
  SF_tB1_errUp = goodJ1_SF_CSVT_errUp;
  SF_tB2_errUp = goodJ1_SF_CSVT_errUp * goodJ2_SF_CSVT_errUp;
  SF_mB1_errDn = goodJ1_SF_CSVM_errDn;
  SF_mB2_errDn = goodJ1_SF_CSVM_errDn * goodJ2_SF_CSVM_errDn;
  SF_tB1_errDn = goodJ1_SF_CSVT_errDn;
  SF_tB2_errDn = goodJ1_SF_CSVT_errDn * goodJ2_SF_CSVT_errDn;

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
  if( shift=="LESUp" ) { 
   MET_pt = met_eesUp_pt;
   MET_phi = met_eesUp_phi;
  }
  if( shift=="LESDown" ) {
   MET_pt = met_eesDn_pt;
   MET_phi = met_eesDn_phi;
  }

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

  ////////////////////////////////
  // begin dybb, dyjj Selection 5,6
  ////////////////////////////////

  pass_g0CJ_mu = kFALSE;
  pass_g1CJ_mu = kFALSE;
  pass_g2CJ_mu = kFALSE;
  pass_e2CJ_mu = kFALSE;
  pass_g2CJ_mB1_mu = kFALSE;
  pass_g2CJ_tB1_mu = kFALSE;
  pass_g2CJ_mB2_mu = kFALSE;
  pass_g2CJ_tB2_mu = kFALSE;
  pass_g2CJ_xFJ_mu = kFALSE;
  pass_e2CJ_xFJ_mu = kFALSE;
  pass_e2CJ_xFJ_mB1_mu = kFALSE;
  pass_e2CJ_xFJ_tB1_mu = kFALSE;
  pass_e2CJ_xFJ_mB2_mu = kFALSE;
  pass_e2CJ_xFJ_tB2_mu = kFALSE;
  pass_g0CJ_ele = kFALSE;
  pass_g1CJ_ele = kFALSE;
  pass_g2CJ_ele = kFALSE;
  pass_e2CJ_ele = kFALSE;
  pass_g2CJ_mB1_ele = kFALSE;
  pass_g2CJ_tB1_ele = kFALSE;
  pass_g2CJ_mB2_ele = kFALSE;
  pass_g2CJ_tB2_ele = kFALSE;
  pass_g2CJ_xFJ_ele = kFALSE;
  pass_e2CJ_xFJ_ele = kFALSE;
  pass_e2CJ_xFJ_mB1_ele = kFALSE;
  pass_e2CJ_xFJ_tB1_ele = kFALSE;
  pass_e2CJ_xFJ_mB2_ele = kFALSE;
  pass_e2CJ_xFJ_tB2_ele = kFALSE;
  weight_mu = 1.;
  weight_ele = 1.;

  //if( twoGoodMuons && exactly2goodJs ){ // mu good
  if( twoGoodMuons ){ 
                pass_g0CJ_mu=kTRUE;
   if ( g1CJ ){ pass_g1CJ_mu=kTRUE; }
   if ( g2CJ ){ pass_g2CJ_mu=kTRUE; }
   if ( e2CJ ){ pass_e2CJ_mu=kTRUE; }
   if ( g2CJ && mB1 ){ pass_g2CJ_mB1_mu=kTRUE; }
   if ( g2CJ && tB1 ){ pass_g2CJ_tB1_mu=kTRUE; }
   if ( g2CJ && mB2 ){ pass_g2CJ_mB2_mu=kTRUE; }
   if ( g2CJ && tB2 ){ pass_g2CJ_tB2_mu=kTRUE; }
   if ( g2CJ && xFJ ){ pass_g2CJ_xFJ_mu=kTRUE; }
   if ( e2CJ && xFJ ){ pass_e2CJ_xFJ_mu=kTRUE; }
   if ( e2CJ && xFJ && mB1 ){ pass_e2CJ_xFJ_mB1_mu=kTRUE; }
   if ( e2CJ && xFJ && tB1 ){ pass_e2CJ_xFJ_tB1_mu=kTRUE; }
   if ( e2CJ && xFJ && mB2 ){ pass_e2CJ_xFJ_mB2_mu=kTRUE; }
   if ( e2CJ && xFJ && tB2 ){ pass_e2CJ_xFJ_tB2_mu=kTRUE; }
   if( isMC ){
   weight_mu =
    ( SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents );
    SF_dyjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodMu_IDIso->at(1);
    SF_dyjj_mu_good_IDIsoHLT_errUp = SF_dyjj_mu_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodMu_IDIso_errUp->at(1),2) );
    SF_dyjj_mu_good_IDIsoHLT_errDn = SF_dyjj_mu_good_IDIsoHLT 
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodMu_IDIso_errDn->at(1),2) );
   }
  }
  
  if( twoGoodElectrons ){ //
                pass_g0CJ_ele=kTRUE;
   if ( g1CJ ){ pass_g1CJ_ele=kTRUE; }
   if ( g2CJ ){ pass_g2CJ_ele=kTRUE; }
   if ( e2CJ ){ pass_e2CJ_ele=kTRUE; }
   if ( g2CJ && mB1 ){ pass_g2CJ_mB1_ele=kTRUE; }
   if ( g2CJ && tB1 ){ pass_g2CJ_tB1_ele=kTRUE; }
   if ( g2CJ && mB2 ){ pass_g2CJ_mB2_ele=kTRUE; }
   if ( g2CJ && tB2 ){ pass_g2CJ_tB2_ele=kTRUE; }
   if ( g2CJ && xFJ ){ pass_g2CJ_xFJ_ele=kTRUE; }
   if ( e2CJ && xFJ ){ pass_e2CJ_xFJ_ele=kTRUE; }
   if ( e2CJ && xFJ && mB1 ){ pass_e2CJ_xFJ_mB1_ele=kTRUE; }
   if ( e2CJ && xFJ && tB1 ){ pass_e2CJ_xFJ_tB1_ele=kTRUE; }
   if ( e2CJ && xFJ && mB2 ){ pass_e2CJ_xFJ_mB2_ele=kTRUE; }
   if ( e2CJ && xFJ && tB2 ){ pass_e2CJ_xFJ_tB2_ele=kTRUE; }
   if( isMC ){
   weight_ele = 
    ( SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents );
    SF_dyjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(1);
    SF_dyjj_ele_good_IDIsoHLT_errUp = SF_dyjj_ele_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIso_errUp->at(1),2) );
    SF_dyjj_ele_good_IDIsoHLT_errDn = SF_dyjj_ele_good_IDIsoHLT 
     - std::sqrt( pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIso_errDn->at(1),2) );
   }
  }

  // total weight
  if( isMC ){
   weight_mB1_mu  = SF_mB1 * weight_mu;
   weight_tB1_mu  = SF_tB1 * weight_mu;
   weight_mB2_mu  = SF_mB2 * weight_mu;
   weight_tB2_mu  = SF_tB2 * weight_mu;
   weight_mB1_CSVUp_mu  = SF_mB1_errUp * weight_mu;
   weight_tB1_CSVUp_mu  = SF_tB1_errUp * weight_mu;
   weight_mB2_CSVUp_mu  = SF_mB2_errUp * weight_mu;
   weight_tB2_CSVUp_mu  = SF_tB2_errUp * weight_mu;
   weight_mB1_CSVDown_mu  = SF_mB1_errDn * weight_mu;
   weight_tB1_CSVDown_mu  = SF_tB1_errDn * weight_mu;
   weight_mB2_CSVDown_mu  = SF_mB2_errDn * weight_mu;
   weight_tB2_CSVDown_mu  = SF_tB2_errDn * weight_mu;
   
   weight_mB1_ele  = SF_mB1 * weight_ele;
   weight_tB1_ele  = SF_tB1 * weight_ele;
   weight_mB2_ele  = SF_mB2 * weight_ele;
   weight_tB2_ele  = SF_tB2 * weight_ele;
   weight_mB1_CSVUp_ele  = SF_mB1_errUp * weight_ele;
   weight_tB1_CSVUp_ele  = SF_tB1_errUp * weight_ele;
   weight_mB2_CSVUp_ele  = SF_mB2_errUp * weight_ele;
   weight_tB2_CSVUp_ele  = SF_tB2_errUp * weight_ele;
   weight_mB1_CSVDown_ele  = SF_mB1_errDn * weight_ele;
   weight_tB1_CSVDown_ele  = SF_tB1_errDn * weight_ele;
   weight_mB2_CSVDown_ele  = SF_mB2_errDn * weight_ele;
   weight_tB2_CSVDown_ele  = SF_tB2_errDn * weight_ele;
  }
  else{
   weight_mu = 1;
   weight_mB1_mu = 1.; 
   weight_tB1_mu = 1.; 
   weight_mB2_mu = 1.; 
   weight_tB2_mu = 1.; 
   weight_mB1_CSVUp_mu = 1.; 
   weight_tB1_CSVUp_mu = 1.; 
   weight_mB2_CSVUp_mu = 1.; 
   weight_tB2_CSVUp_mu = 1.; 
   weight_mB1_CSVDown_mu = 1.; 
   weight_tB1_CSVDown_mu = 1.; 
   weight_mB2_CSVDown_mu = 1.; 
   weight_tB2_CSVDown_mu = 1.; 
   weight_ele = 1;
   weight_mB1_ele = 1.; 
   weight_tB1_ele = 1.; 
   weight_mB2_ele = 1.; 
   weight_tB2_ele = 1.; 
   weight_mB1_CSVUp_ele = 1.; 
   weight_tB1_CSVUp_ele = 1.; 
   weight_mB2_CSVUp_ele = 1.; 
   weight_tB2_CSVUp_ele = 1.; 
   weight_mB1_CSVDown_ele = 1.; 
   weight_tB1_CSVDown_ele = 1.; 
   weight_mB2_CSVDown_ele = 1.; 
   weight_tB2_CSVDown_ele = 1.; 
  }

  /////////
  // dy
  /////////
  fillHistWriter( pass_g0CJ_mu, 0, pass_g0CJ_ele, 0,
                  0, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mu, 1., weight_ele, 1.
               );
  fillHistWriter( pass_g1CJ_mu, 0, pass_g1CJ_ele, 0,
                  1, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mu, 1., weight_ele, 1.
               );
  fillHistWriter( pass_g2CJ_mu, 0, pass_g2CJ_ele, 0,
                  2, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mu, 1., weight_ele, 1.
               );
  fillHistWriter( pass_e2CJ_mu, 0, pass_e2CJ_ele, 0,
                  3, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mu, 1., weight_ele, 1.
               );

  fillHistWriter( pass_g2CJ_mB1_mu, 0, pass_g2CJ_mB1_ele, 0,
                  4, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB1_mu, 1., weight_mB1_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_g2CJ_mB1_mu, 0, pass_g2CJ_mB1_ele, 0,
                  4, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB1_CSVUp_mu, 1., weight_mB1_CSVUp_ele, 1.
               );
  fillHistWriter( pass_g2CJ_mB1_mu, 0, pass_g2CJ_mB1_ele, 0,
                  4, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB1_CSVDown_mu, 1., weight_mB1_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_g2CJ_tB1_mu, 0, pass_g2CJ_tB1_ele, 0,
                  5, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB1_mu, 1., weight_tB1_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_g2CJ_tB1_mu, 0, pass_g2CJ_tB1_ele, 0,
                  5, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB1_CSVUp_mu, 1., weight_tB1_CSVUp_ele, 1.
               );
  fillHistWriter( pass_g2CJ_tB1_mu, 0, pass_g2CJ_tB1_ele, 0,
                  5, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB1_CSVDown_mu, 1., weight_tB1_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_g2CJ_mB2_mu, 0, pass_g2CJ_mB2_ele, 0,
                  6, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB2_mu, 1., weight_mB2_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_g2CJ_mB2_mu, 0, pass_g2CJ_mB2_ele, 0,
                  6, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB2_CSVUp_mu, 1., weight_mB2_CSVUp_ele, 1.
               );
  fillHistWriter( pass_g2CJ_mB2_mu, 0, pass_g2CJ_mB2_ele, 0,
                  6, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB2_CSVDown_mu, 1., weight_mB2_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_g2CJ_tB2_mu, 0, pass_g2CJ_tB2_ele, 0,
                  7, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB2_mu, 1., weight_tB2_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_g2CJ_tB2_mu, 0, pass_g2CJ_tB2_ele, 0,
                  7, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB2_CSVUp_mu, 1., weight_tB2_CSVUp_ele, 1.
               );
  fillHistWriter( pass_g2CJ_tB2_mu, 0, pass_g2CJ_tB2_ele, 0,
                  7, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB2_CSVDown_mu, 1., weight_tB2_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_g2CJ_xFJ_mu, 0, pass_g2CJ_xFJ_ele, 0,
                  8, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mu, 1., weight_ele, 1.
               );

  fillHistWriter( pass_e2CJ_xFJ_mu, 0, pass_e2CJ_xFJ_ele, 0,
                  9, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mu, 1., weight_ele, 1.
               );

  fillHistWriter( pass_e2CJ_xFJ_mB1_mu, 0, pass_e2CJ_xFJ_mB1_ele, 0,
                  10, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB1_mu, 1., weight_mB1_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_e2CJ_xFJ_mB1_mu, 0, pass_e2CJ_xFJ_mB1_ele, 0,
                  10, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB1_CSVUp_mu, 1., weight_mB1_CSVUp_ele, 1.
               );
  fillHistWriter( pass_e2CJ_xFJ_mB1_mu, 0, pass_e2CJ_xFJ_mB1_ele, 0,
                  10, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB1_CSVDown_mu, 1., weight_mB1_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_e2CJ_xFJ_tB1_mu, 0, pass_e2CJ_xFJ_tB1_ele, 0,
                  11, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB1_mu, 1., weight_tB1_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_e2CJ_xFJ_tB1_mu, 0, pass_e2CJ_xFJ_tB1_ele, 0,
                  11, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB1_CSVUp_mu, 1., weight_tB1_CSVUp_ele, 1.
               );
  fillHistWriter( pass_e2CJ_xFJ_tB1_mu, 0, pass_e2CJ_xFJ_tB1_ele, 0,
                  11, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB1_CSVDown_mu, 1., weight_tB1_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_e2CJ_xFJ_mB2_mu, 0, pass_e2CJ_xFJ_mB2_ele, 0,
                  12, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB2_mu, 1., weight_mB2_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_e2CJ_xFJ_mB2_mu, 0, pass_e2CJ_xFJ_mB2_ele, 0,
                  12, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB2_CSVUp_mu, 1., weight_mB2_CSVUp_ele, 1.
               );
  fillHistWriter( pass_e2CJ_xFJ_mB2_mu, 0, pass_e2CJ_xFJ_mB2_ele, 0,
                  12, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_mB2_CSVDown_mu, 1., weight_mB2_CSVDown_ele, 1.
               );
  }

  fillHistWriter( pass_e2CJ_xFJ_tB2_mu, 0, pass_e2CJ_xFJ_tB2_ele, 0,
                  13, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB2_mu, 1., weight_tB2_ele, 1.
               );
  if( shift=="SFs"){
  fillHistWriter( pass_e2CJ_xFJ_tB2_mu, 0, pass_e2CJ_xFJ_tB2_ele, 0,
                  13, 1,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB2_CSVUp_mu, 1., weight_tB2_CSVUp_ele, 1.
               );
  fillHistWriter( pass_e2CJ_xFJ_tB2_mu, 0, pass_e2CJ_xFJ_tB2_ele, 0,
                  13, 2,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_tB2_CSVDown_mu, 1., weight_tB2_CSVDown_ele, 1.
               );
  }


 } 

// // write a log
// std::ofstream logfile (outfileName+".log", std::ofstream::out);
// logfile<<"isMC = "<<isMC<<std::endl;
// logfile<<"shift = "<<shift<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                 W+bb Selection                  --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_wbb_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_wbb_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_wbb_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_wbb_qcd_postcut<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                TT(me) Selection               --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_ttme_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_ttme_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_ttme_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_ttme_qcd_postcut<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                 TT(jjj) Selection                --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_ttjjj_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_ttjjj_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_ttjjj_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_ttjjj_qcd_postcut<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                  W+jj Selection                 --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_wjj_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_wjj_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_wjj_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_wjj_qcd_postcut<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--             Single Top (t) Selection            --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_stt_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_stt_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_stt_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_stt_qcd_postcut<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--              Drell-Yan+jj Selection             --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_dyjj_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_dyjj_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_dyjj_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_dyjj_qcd_postcut<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--              Drell-Yan+bb Selection             --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Mu: "<<nbrEntries_mu_dybb_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Mu: "<<nbrEntries_mu_dybb_qcd_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut Ele: "<<nbrEntries_ele_dybb_good_postcut<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut Ele: "<<nbrEntries_ele_dybb_qcd_postcut<<std::endl;
// logfile.close();
 

 // write these histograms to file
 TFile *outfile = new TFile(outfileName,"RECREATE");
 outfile->cd();
 
 // wbb
 writeHistWriter( 0, 0, isW );
 writeHistWriter( 1, 0, isW );
 writeHistWriter( 2, 0, isW );
 writeHistWriter( 3, 0, isW );
 writeHistWriter( 4, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 4, 1, isW );
  writeHistWriter( 4, 2, isW );
 }
 writeHistWriter( 5, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 5, 1, isW );
  writeHistWriter( 5, 2, isW );
 }
 writeHistWriter( 6, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 6, 1, isW );
  writeHistWriter( 6, 2, isW );
 }
 writeHistWriter( 7, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 7, 1, isW );
  writeHistWriter( 7, 2, isW );
 }
 writeHistWriter( 8, 0, isW );
 writeHistWriter( 9, 0, isW );
 writeHistWriter( 10, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 10, 1, isW );
  writeHistWriter( 10, 2, isW );
 }
 writeHistWriter( 11, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 11, 1, isW );
  writeHistWriter( 11, 2, isW );
 }
 writeHistWriter( 12, 0, isW );
 if( shift=="SFs"){
  writeHistWriter( 12, 1, isW );
  writeHistWriter( 12, 2, isW );
 }
 writeHistWriter( 13, 0, isW );
// if( shift=="SFs"){
//  writeHistWriter( 13, 1, isW );
//  writeHistWriter( 13, 2, isW );
// }


 outfile->Close();
 std::cout<<" Done "<<std::endl;
}

