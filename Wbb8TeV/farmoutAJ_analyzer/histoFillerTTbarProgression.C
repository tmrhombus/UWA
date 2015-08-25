#define histoFillerTTbarProgression_cxx
#include "histoFillerTTbarProgression.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>
//#include <cmath>

void histoFillerTTbarProgression::Loop(
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
  if(!nb){std::cout<<"histoFillerTTbarProgression.C can't fChain->GetEntry(jentry)"<<std::endl;}

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
   nrW3J = 30358906;
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

//  // Dileptons
//  goodM1M2_pt   = -1.;
//  goodM1M2_eta  = -1.;
//  goodM1M2_phi  = -1.;
//  goodM1M2_mass = -1.;
//  goodE1E2_pt   = -1.;
//  goodE1E2_eta  = -1.;
//  goodE1E2_phi  = -1.;
//  goodE1E2_mass = -1.;
//
//  if (goodMu_pt_vec->size()>1){
//   fourVec_M1.SetPtEtaPhiM(goodMu_pt_vec->at(0), goodMu_eta_vec->at(0), goodMu_phi_vec->at(0), goodMu_mass_vec->at(0));
//   fourVec_M2.SetPtEtaPhiM(goodMu_pt_vec->at(1), goodMu_eta_vec->at(1), goodMu_phi_vec->at(1), goodMu_mass_vec->at(1));
//   fourVec_M1M2 = fourVec_M1 + fourVec_M2;
//   goodM1M2_pt   = fourVec_M1M2.Pt();
//   goodM1M2_eta  = fourVec_M1M2.Eta();
//   goodM1M2_phi  = fourVec_M1M2.Phi();
//   goodM1M2_mass = fourVec_M1M2.M();
//  }
//  if (goodEle_pt_vec->size()>1){
//   fourVec_E1.SetPtEtaPhiM(goodEle_pt_vec->at(0), goodEle_eta_vec->at(0), goodEle_phi_vec->at(0), goodEle_mass_vec->at(0));
//   fourVec_E2.SetPtEtaPhiM(goodEle_pt_vec->at(1), goodEle_eta_vec->at(1), goodEle_phi_vec->at(1), goodEle_mass_vec->at(1));
//   fourVec_E1E2 = fourVec_E1 + fourVec_E2;
//   goodE1E2_pt   = fourVec_E1E2.Pt();
//   goodE1E2_eta  = fourVec_E1E2.Eta();
//   goodE1E2_phi  = fourVec_E1E2.Phi();
//   goodE1E2_mass = fourVec_E1E2.M();
//  }

  // filter variables
  twoGoodLMuE = kFALSE; 
  twoGoodLEMu = kFALSE; 

  twoGoodLMuE = HLT_IsoMu24_eta2p1_v_fired
   && nbrGoodEle==1 && nbrVetoEle==0
   && nbrGoodMu==1  && nbrVetoMu==0;
  twoGoodLEMu = HLT_Ele27_WP80_fired
   && nbrGoodEle==1 && nbrVetoEle==0
   && nbrGoodMu==1  && nbrVetoMu==0;

  min2goodJs =
   goodJ1_pt>25 && goodJ2_pt>25 && fwdJ1_pt<25;
  vetoJ3 =
   min2goodJs && goodJ3_pt<25;

  btag0J = kTRUE ;
  btag1Jta = goodJ1_CSV>0.898 ;
  btag1Jtb = goodJ2_CSV>0.898 ;
  btag2Jt  = goodJ1_CSV>0.898 && goodJ2_CSV>0.898 ;
  btag1Jma = goodJ1_CSV>0.679 ;
  btag1Jmb = goodJ2_CSV>0.679 ;
  btag2Jm  = goodJ1_CSV>0.679 && goodJ2_CSV>0.679 ;

  // SFs for CSV
  SF_1bta = goodJ1_SF_CSVT;
  SF_1btb = goodJ2_SF_CSVT;
  SF_2bt  = goodJ1_SF_CSVT * goodJ2_SF_CSVT;
  SF_1bma = goodJ1_SF_CSVM;
  SF_1bmb = goodJ2_SF_CSVM;
  SF_2bm  = goodJ1_SF_CSVM * goodJ2_SF_CSVM;

  // define some variables that get plotted
  // MET
  MET_pt = met_pt;
  MET_phi = met_phi;

  // MT
  // good mu
  mt_mu_good = mt_goodMuon;
  if( nrGoodMu>0 ){
   lep_mu_good_pt = goodMu_pt_vec->at(0);
   lep_mu_good_eta = goodMu_eta_vec->at(0);
   lep_mu_good_phi = goodMu_phi_vec->at(0);
  }
  // good ele
  mt_ele_good = mt_goodElectron;
  if( nrGoodEle>0) {
   lep_ele_good_pt = goodEle_pt_vec->at(0);
   lep_ele_good_eta = goodEle_eta_vec->at(0);
   lep_ele_good_phi = goodEle_phi_vec->at(0);
  }

  // MT and MET Selection Requirements
  // make sure mT > 0
  if( mt_mu_good <= 0 ){ mt_mu_good=-1.; }
  if( mt_ele_good <= 0 ){ mt_ele_good=-1.; }

  //////////////////////////
  // begin ttme Selection 0
  //////////////////////////
  Bool_t pass_ttme0b_mu_good=kFALSE;
  Bool_t pass_ttme1bta_mu_good=kFALSE;
  Bool_t pass_ttme1btb_mu_good=kFALSE;
  Bool_t pass_ttme2bt_mu_good=kFALSE;
  Bool_t pass_ttme1bma_mu_good=kFALSE;
  Bool_t pass_ttme1bmb_mu_good=kFALSE;
  Bool_t pass_ttme2bm_mu_good=kFALSE;
  Bool_t pass_ttme0bJv_mu_good=kFALSE;
  Bool_t pass_ttme1btaJv_mu_good=kFALSE;
  Bool_t pass_ttme1btbJv_mu_good=kFALSE;
  Bool_t pass_ttme2btJv_mu_good=kFALSE;
  Bool_t pass_ttme1bmaJv_mu_good=kFALSE;
  Bool_t pass_ttme1bmbJv_mu_good=kFALSE;
  Bool_t pass_ttme2bmJv_mu_good=kFALSE;

  Bool_t pass_ttme0b_ele_good=kFALSE;
  Bool_t pass_ttme1bta_ele_good=kFALSE;
  Bool_t pass_ttme1btb_ele_good=kFALSE;
  Bool_t pass_ttme2bt_ele_good=kFALSE;
  Bool_t pass_ttme1bma_ele_good=kFALSE;
  Bool_t pass_ttme1bmb_ele_good=kFALSE;
  Bool_t pass_ttme2bm_ele_good=kFALSE;
  Bool_t pass_ttme0bJv_ele_good=kFALSE;
  Bool_t pass_ttme1btaJv_ele_good=kFALSE;
  Bool_t pass_ttme1btbJv_ele_good=kFALSE;
  Bool_t pass_ttme2btJv_ele_good=kFALSE;
  Bool_t pass_ttme1bmaJv_ele_good=kFALSE;
  Bool_t pass_ttme1bmbJv_ele_good=kFALSE;
  Bool_t pass_ttme2bmJv_ele_good=kFALSE;

  if( twoGoodLMuE && min2goodJs ){ // mu good
   if( btag0J )   { pass_ttme0b_mu_good=kTRUE; } 
   if( btag1Jta ) { pass_ttme1bta_mu_good=kTRUE; } 
   if( btag1Jtb ) { pass_ttme1btb_mu_good=kTRUE; } 
   if( btag2Jt )  { pass_ttme2bt_mu_good=kTRUE; } 
   if( btag1Jma ) { pass_ttme1bma_mu_good=kTRUE; } 
   if( btag1Jmb ) { pass_ttme1bmb_mu_good=kTRUE; } 
   if( btag2Jm )  { pass_ttme2bm_mu_good=kTRUE; } 
   if( vetoJ3 && btag0J )   { pass_ttme0bJv_mu_good=kTRUE; } 
   if( vetoJ3 && btag1Jta ) { pass_ttme1btaJv_mu_good=kTRUE; } 
   if( vetoJ3 && btag1Jtb ) { pass_ttme1btbJv_mu_good=kTRUE; } 
   if( vetoJ3 && btag2Jt )  { pass_ttme2btJv_mu_good=kTRUE; } 
   if( vetoJ3 && btag1Jma ) { pass_ttme1bmaJv_mu_good=kTRUE; } 
   if( vetoJ3 && btag1Jmb ) { pass_ttme1bmbJv_mu_good=kTRUE; } 
   if( vetoJ3 && btag2Jm )  { pass_ttme2bmJv_mu_good=kTRUE; } 
   if( isMC ){
    SF_ttme_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIso->at(0); 
   }
  }
  if( twoGoodLEMu && min2goodJs ){ // ele good
   if( btag0J )   { pass_ttme0b_ele_good=kTRUE; } 
   if( btag1Jta ) { pass_ttme1bta_ele_good=kTRUE; } 
   if( btag1Jtb ) { pass_ttme1btb_ele_good=kTRUE; } 
   if( btag2Jt )  { pass_ttme2bt_ele_good=kTRUE; } 
   if( btag1Jma ) { pass_ttme1bma_ele_good=kTRUE; } 
   if( btag1Jmb ) { pass_ttme1bmb_ele_good=kTRUE; } 
   if( btag2Jm )  { pass_ttme2bm_ele_good=kTRUE; } 
   if( vetoJ3 && btag0J )   { pass_ttme0bJv_ele_good=kTRUE; } 
   if( vetoJ3 && btag1Jta ) { pass_ttme1btaJv_ele_good=kTRUE; } 
   if( vetoJ3 && btag1Jtb ) { pass_ttme1btbJv_ele_good=kTRUE; } 
   if( vetoJ3 && btag2Jt )  { pass_ttme2btJv_ele_good=kTRUE; } 
   if( vetoJ3 && btag1Jma ) { pass_ttme1bmaJv_ele_good=kTRUE; } 
   if( vetoJ3 && btag1Jmb ) { pass_ttme1bmbJv_ele_good=kTRUE; } 
   if( vetoJ3 && btag2Jm )  { pass_ttme2bmJv_ele_good=kTRUE; } 
   if( isMC ){
    SF_ttme_ele_good_IDIsoHLT = SF_goodMu_IDIso->at(0) * SF_goodEle_IDIsoHLT->at(0);
   }
  }
  // total event weight
  if( isMC ){
   weight_ttme0b_mu_good   = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_ttme1bta_mu_good = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_1bta / nrEvents;
   weight_ttme1btb_mu_good = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_1btb / nrEvents;
   weight_ttme2bt_mu_good  = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_2bt  / nrEvents;
   weight_ttme1bma_mu_good = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_1bma / nrEvents;
   weight_ttme1bmb_mu_good = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_1bmb / nrEvents;
   weight_ttme2bm_mu_good  = SF_ttme_mu_good_IDIsoHLT * SF_lumiWeightPU * lumi_mu * crossSec * SF_2bm  / nrEvents;

   weight_ttme0b_ele_good   = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   weight_ttme1bta_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_1bta / nrEvents;
   weight_ttme1btb_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_1btb / nrEvents;
   weight_ttme2bt_ele_good  = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_2bt  / nrEvents;
   weight_ttme1bma_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_1bma / nrEvents;
   weight_ttme1bmb_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_1bmb / nrEvents;
   weight_ttme2bm_ele_good  = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_2bm  / nrEvents;
  }
  else{
   weight_ttme0b_mu_good   = 1.;
   weight_ttme1bta_mu_good = 1.; 
   weight_ttme1btb_mu_good = 1.; 
   weight_ttme2bt_mu_good  = 1.; 
   weight_ttme1bma_mu_good = 1.; 
   weight_ttme1bmb_mu_good = 1.; 
   weight_ttme2bm_mu_good  = 1.; 

   weight_ttme0b_ele_good   = 1.;
   weight_ttme1bta_ele_good = 1.;
   weight_ttme1btb_ele_good = 1.;
   weight_ttme2bt_ele_good  = 1.;
   weight_ttme1bma_ele_good = 1.;
   weight_ttme1bmb_ele_good = 1.;
   weight_ttme2bm_ele_good  = 1.;
  }

  mt_mu_qcd = 1.;
  mt_ele_qcd = 1.;
  // ttme0b
  fillHistWriter( pass_ttme0b_mu_good, kFALSE, pass_ttme0b_ele_good, kFALSE,
                  0, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme0b_mu_good, 1., weight_ttme0b_ele_good, 1.
                );
  // ttme1bta
  fillHistWriter( pass_ttme1bta_mu_good, kFALSE, pass_ttme1bta_ele_good, kFALSE,
                  1, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1bta_mu_good, 1., weight_ttme1bta_ele_good, 1.
                );
  // ttme1btb
  fillHistWriter( pass_ttme1btb_mu_good, kFALSE, pass_ttme1btb_ele_good, kFALSE,
                  2, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1btb_mu_good, 1., weight_ttme1btb_ele_good, 1.
                );
  // ttme2bt
  fillHistWriter( pass_ttme2bt_mu_good, kFALSE, pass_ttme2bt_ele_good, kFALSE,
                  3, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2bt_mu_good, 1., weight_ttme2bt_ele_good, 1.
                );
  // ttme1bma
  fillHistWriter( pass_ttme1bma_mu_good, kFALSE, pass_ttme1bma_ele_good, kFALSE,
                  4, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1bma_mu_good, 1., weight_ttme1bma_ele_good, 1.
                );
  // ttme1bmb
  fillHistWriter( pass_ttme1bmb_mu_good, kFALSE, pass_ttme1bmb_ele_good, kFALSE,
                  5, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1bmb_mu_good, 1., weight_ttme1bmb_ele_good, 1.
                );
  // ttme2bm
  fillHistWriter( pass_ttme2bm_mu_good, kFALSE, pass_ttme2bm_ele_good, kFALSE,
                  6, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2bm_mu_good, 1., weight_ttme2bm_ele_good, 1.
                );

  // ttme0bJv
  fillHistWriter( pass_ttme0bJv_mu_good, kFALSE, pass_ttme0bJv_ele_good, kFALSE,
                  7, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme0b_mu_good, 1., weight_ttme0b_ele_good, 1.
                );
  // ttme1bta
  fillHistWriter( pass_ttme1btaJv_mu_good, kFALSE, pass_ttme1btaJv_ele_good, kFALSE,
                  8, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1bta_mu_good, 1., weight_ttme1bta_ele_good, 1.
                );
  // ttme1btb
  fillHistWriter( pass_ttme1btbJv_mu_good, kFALSE, pass_ttme1btbJv_ele_good, kFALSE,
                  9, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1btb_mu_good, 1., weight_ttme1btb_ele_good, 1.
                );
  // ttme2bt
  fillHistWriter( pass_ttme2btJv_mu_good, kFALSE, pass_ttme2btJv_ele_good, kFALSE,
                  10, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2bt_mu_good, 1., weight_ttme2bt_ele_good, 1.
                );
  // ttme1bma
  fillHistWriter( pass_ttme1bmaJv_mu_good, kFALSE, pass_ttme1bmaJv_ele_good, kFALSE,
                  11, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1bma_mu_good, 1., weight_ttme1bma_ele_good, 1.
                );
  // ttme1bmb
  fillHistWriter( pass_ttme1bmbJv_mu_good, kFALSE, pass_ttme1bmbJv_ele_good, kFALSE,
                  12, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1bmb_mu_good, 1., weight_ttme1bmb_ele_good, 1.
                );
  // ttme2bm
  fillHistWriter( pass_ttme2bmJv_mu_good, kFALSE, pass_ttme2bmJv_ele_good, kFALSE,
                  13, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2bm_mu_good, 1., weight_ttme2bm_ele_good, 1.
                );


 } 

 // write these histograms to file
 TFile *outfile = new TFile(outfileName,"RECREATE");
 outfile->cd();
 
 writeHistWriter( 0, 0, isW );
 writeHistWriter( 1, 0, isW );
 writeHistWriter( 2, 0, isW );
 writeHistWriter( 3, 0, isW );
 writeHistWriter( 4, 0, isW );
 writeHistWriter( 5, 0, isW );
 writeHistWriter( 6, 0, isW );
 writeHistWriter( 7, 0, isW );
 writeHistWriter( 8, 0, isW );
 writeHistWriter( 9, 0, isW );
 writeHistWriter( 10, 0, isW );
 writeHistWriter( 11, 0, isW );
 writeHistWriter( 12, 0, isW );
 writeHistWriter( 13, 0, isW );

 outfile->Close();
 std::cout<<"done"<<std::endl;
}

