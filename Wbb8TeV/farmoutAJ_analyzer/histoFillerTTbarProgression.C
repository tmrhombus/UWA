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

  // dr J1 J2
  dRgoodJ1J2 = -1.; 
  dphiJJ = dPhi(goodJ1_phi, goodJ2_phi);
  detaJJ = dEta(goodJ1_eta, goodJ2_eta);
  dRgoodJ1J2 = std::sqrt( ((goodJ1_eta-goodJ2_eta)*(goodJ1_eta-goodJ2_eta)) + (dphiJJ*dphiJJ) );

  // Dijet Mass
  fourVec_J1.SetPtEtaPhiM(goodJ1_pt, goodJ1_eta, goodJ1_phi, goodJ1_mass);
  fourVec_J2.SetPtEtaPhiM(goodJ2_pt, goodJ2_eta, goodJ2_phi, goodJ2_mass);
  fourVec_J3.SetPtEtaPhiM(goodJ3_pt, goodJ3_eta, goodJ3_phi, goodJ3_mass);
  fourVec_J4.SetPtEtaPhiM(goodJ4_pt, goodJ4_eta, goodJ4_phi, goodJ4_mass);
  fourVec_J1J2 = fourVec_J1 + fourVec_J2;
  fourVec_J3J4 = fourVec_J3 + fourVec_J4;
  goodJ1J2_mass = fourVec_J1J2.M();
  goodJ1J2_pt = fourVec_J1J2.Pt();
  goodJ3J4_mass = fourVec_J3J4.M();

  // filter variables
  twoGoodLMuE = HLT_IsoMu24_eta2p1_v_fired
   && nrGoodEle==1 && nrVetoEle<=1
   && nrGoodMu==1  && nrVetoMu<=1;
  twoGoodLEMu = HLT_Ele27_WP80_fired
   && nrGoodEle==1 && nrVetoEle<=1
   && nrGoodMu==1  && nrVetoMu<=1;
  twoQCDLMuE =  HLT_IsoMu24_eta2p1_v_fired && //
   nrQCDMu==1   && nrVetoMu==0 &&
   nrGoodEle==1 && nrVetoEle<=1;
  twoQCDLEMu =  HLT_Ele27_WP80_fired && //
   nrQCDEle==1   && nrVetoEle==0 &&
   nrGoodMu==1 && nrVetoMu<=1;

  min2goodJs = 
   nrGoodJets>=2 && nrFwdJets==0;
  vetoJ3 = 
   nrGoodJets==2 && nrFwdJets==0;
  btag0J = kTRUE ;
  btag1J = goodJ1_CSV>0.679 ;
  btag2J = goodJ1_CSV>0.679 && goodJ2_CSV>0.679 ;
  //btag1J = goodJ1_CSV>0.898 ;
  //btag2J = goodJ1_CSV>0.898 && goodJ2_CSV>0.898 ;

  // SFs for CSV
  SF_top2BJs = goodJ1_SF_CSVM * goodJ2_SF_CSVM; 
  SF_topBJ = goodJ1_SF_CSVM;
  //SF_top2BJs = goodJ1_SF_CSVT * goodJ2_SF_CSVT; 
  //SF_topBJ = goodJ1_SF_CSVT;
  //SF_top2BJs = 1.; 
  //SF_topBJ =   1.;

  //SF_top2BJs =       1.; 
  //SF_top2BJs_errUp = 1.; 
  //SF_top2BJs_errDn = 1.; 
  //SF_goodBJfwdJ =   1.; 

  SF_CSVrwtgJfJ = 1.; //goodJ1_CSVreweight ;
  SF_CSVrwt2gJs = 1.; //goodJ1_CSVreweight * goodJ2_CSVreweight;

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
  // qcd mu
  mt_mu_qcd = mt_qcdMuon;
  lep_mu_qcd_pt =  qcdMu_pt ;
  lep_mu_qcd_eta = qcdMu_eta;
  lep_mu_qcd_phi = qcdMu_phi;
  // good ele
  mt_ele_good = mt_goodElectron;
  if( nrGoodEle>0) {
   lep_ele_good_pt = goodEle_pt_vec->at(0);
   lep_ele_good_eta = goodEle_eta_vec->at(0);
   lep_ele_good_phi = goodEle_phi_vec->at(0);
  }
  // qcd ele
  mt_ele_qcd = mt_qcdElectron;
  lep_ele_qcd_pt =  qcdEle_pt ;
  lep_ele_qcd_eta = qcdEle_eta;
  lep_ele_qcd_phi = qcdEle_phi;

  // MT and MET Selection Requirements
  // make sure mT > 0
  if( mt_mu_good <= 0 ){ mt_mu_good=-1.; }
  if( mt_mu_qcd <= 0 ){ mt_mu_qcd=-1.; }
  if( mt_ele_good <= 0 ){ mt_ele_good=-1.; }
  if( mt_ele_qcd <= 0 ){ mt_ele_qcd=-1.; }

  mtOver45_mu_good =  mt_mu_good > 45;
  mtOver45_mu_qcd =   mt_mu_qcd > 45;
  mtOver45_ele_good = mt_ele_good > 45;
  mtOver45_ele_qcd =  mt_ele_qcd > 45;

  //////////////////////////
  // begin ttme Selection 0
  //////////////////////////
  Bool_t pass_ttme0b_mu_good=kFALSE;
  Bool_t pass_ttme0b_mu_qcd=kFALSE;
  Bool_t pass_ttme0b_ele_good=kFALSE;
  Bool_t pass_ttme0b_ele_qcd=kFALSE;

  Bool_t pass_ttme1b_mu_good=kFALSE;
  Bool_t pass_ttme1b_mu_qcd=kFALSE;
  Bool_t pass_ttme1b_ele_good=kFALSE;
  Bool_t pass_ttme1b_ele_qcd=kFALSE;

  Bool_t pass_ttme2b_mu_good=kFALSE;
  Bool_t pass_ttme2b_mu_qcd=kFALSE;
  Bool_t pass_ttme2b_ele_good=kFALSE;
  Bool_t pass_ttme2b_ele_qcd=kFALSE;

  Bool_t pass_ttme0bJv_mu_good=kFALSE;
  Bool_t pass_ttme0bJv_mu_qcd=kFALSE;
  Bool_t pass_ttme0bJv_ele_good=kFALSE;
  Bool_t pass_ttme0bJv_ele_qcd=kFALSE;

  Bool_t pass_ttme1bJv_mu_good=kFALSE;
  Bool_t pass_ttme1bJv_mu_qcd=kFALSE;
  Bool_t pass_ttme1bJv_ele_good=kFALSE;
  Bool_t pass_ttme1bJv_ele_qcd=kFALSE;

  Bool_t pass_ttme2bJv_mu_good=kFALSE;
  Bool_t pass_ttme2bJv_mu_qcd=kFALSE;
  Bool_t pass_ttme2bJv_ele_good=kFALSE;
  Bool_t pass_ttme2bJv_ele_qcd=kFALSE;

  Bool_t pass_ttme0bMt_mu_good=kFALSE;
  Bool_t pass_ttme0bMt_mu_qcd=kFALSE;
  Bool_t pass_ttme0bMt_ele_good=kFALSE;
  Bool_t pass_ttme0bMt_ele_qcd=kFALSE;

  Bool_t pass_ttme1bMt_mu_good=kFALSE;
  Bool_t pass_ttme1bMt_mu_qcd=kFALSE;
  Bool_t pass_ttme1bMt_ele_good=kFALSE;
  Bool_t pass_ttme1bMt_ele_qcd=kFALSE;

  Bool_t pass_ttme2bMt_mu_good=kFALSE;
  Bool_t pass_ttme2bMt_mu_qcd=kFALSE;
  Bool_t pass_ttme2bMt_ele_good=kFALSE;
  Bool_t pass_ttme2bMt_ele_qcd=kFALSE;

  Bool_t pass_ttme0bJvMt_mu_good=kFALSE;
  Bool_t pass_ttme0bJvMt_mu_qcd=kFALSE;
  Bool_t pass_ttme0bJvMt_ele_good=kFALSE;
  Bool_t pass_ttme0bJvMt_ele_qcd=kFALSE;

  Bool_t pass_ttme1bJvMt_mu_good=kFALSE;
  Bool_t pass_ttme1bJvMt_mu_qcd=kFALSE;
  Bool_t pass_ttme1bJvMt_ele_good=kFALSE;
  Bool_t pass_ttme1bJvMt_ele_qcd=kFALSE;

  Bool_t pass_ttme2bJvMt_mu_good=kFALSE;
  Bool_t pass_ttme2bJvMt_mu_qcd=kFALSE;
  Bool_t pass_ttme2bJvMt_ele_good=kFALSE;
  Bool_t pass_ttme2bJvMt_ele_qcd=kFALSE;

  // if( twoGoodLMuE && exactly2goodBJs && passMET && passMT_goodMu ){ // mu good
  if( twoGoodLMuE && min2goodJs ){ // mu good
   if( btag0J ) { pass_ttme0b_mu_good=kTRUE; } 
   if( btag1J ) { pass_ttme1b_mu_good=kTRUE; } 
   if( btag2J ) { pass_ttme2b_mu_good=kTRUE; } 
   if( btag0J && vetoJ3 ) { pass_ttme0bJv_mu_good=kTRUE; }
   if( btag1J && vetoJ3 ) { pass_ttme1bJv_mu_good=kTRUE; }
   if( btag2J && vetoJ3 ) { pass_ttme2bJv_mu_good=kTRUE; }
   if( btag0J && mtOver45_mu_good ) { pass_ttme0bMt_mu_good=kTRUE; }
   if( btag1J && mtOver45_mu_good ) { pass_ttme1bMt_mu_good=kTRUE; }
   if( btag2J && mtOver45_mu_good ) { pass_ttme2bMt_mu_good=kTRUE; }
   if( btag0J && vetoJ3 && mtOver45_mu_good ) { pass_ttme0bJvMt_mu_good=kTRUE; }
   if( btag1J && vetoJ3 && mtOver45_mu_good ) { pass_ttme1bJvMt_mu_good=kTRUE; }
   if( btag2J && vetoJ3 && mtOver45_mu_good ) { pass_ttme2bJvMt_mu_good=kTRUE; }
   if( isMC ){
    SF_ttme_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(0); 
    SF_ttme_mu_good_IDIsoHLT_errUp = SF_ttme_mu_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
    SF_ttme_mu_good_IDIsoHLT_errDn = SF_ttme_mu_good_IDIsoHLT
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) );
   }
  }
  //if( pass_ttme1b_mu_good==kTRUE ){ std::cout<<"passed 1b "<<std::endl;}
  if( twoGoodLEMu && min2goodJs ){ // ele good
   if( btag0J ) { pass_ttme0b_ele_good=kTRUE; }
   if( btag1J ) { pass_ttme1b_ele_good=kTRUE; }
   if( btag2J ) { pass_ttme2b_ele_good=kTRUE; }
   if( btag0J && vetoJ3 ) { pass_ttme0bJv_ele_good=kTRUE; }
   if( btag1J && vetoJ3 ) { pass_ttme1bJv_ele_good=kTRUE; }
   if( btag2J && vetoJ3 ) { pass_ttme2bJv_ele_good=kTRUE; }
   if( btag0J && mtOver45_ele_good ) { pass_ttme0bMt_ele_good=kTRUE; }
   if( btag1J && mtOver45_ele_good ) { pass_ttme1bMt_ele_good=kTRUE; }
   if( btag2J && mtOver45_ele_good ) { pass_ttme2bMt_ele_good=kTRUE; }
   if( btag0J && vetoJ3 && mtOver45_ele_good ) { pass_ttme0bJvMt_ele_good=kTRUE; }
   if( btag1J && vetoJ3 && mtOver45_ele_good ) { pass_ttme1bJvMt_ele_good=kTRUE; }
   if( btag2J && vetoJ3 && mtOver45_ele_good ) { pass_ttme2bJvMt_ele_good=kTRUE; }
   if( isMC ){
    SF_ttme_ele_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0)
    SF_ttme_ele_good_IDIsoHLT_errUp = SF_ttme_ele_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
    SF_ttme_ele_good_IDIsoHLT_errDn = SF_ttme_ele_good_IDIsoHLT
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) );
   }
  }
  if( twoQCDLMuE && min2goodJs ){ // mu qcd
   if( btag0J ) { pass_ttme0b_mu_qcd=kTRUE; }
   if( btag1J ) { pass_ttme1b_mu_qcd=kTRUE; }
   if( btag2J ) { pass_ttme2b_mu_qcd=kTRUE; }
   if( btag0J && vetoJ3 ) { pass_ttme0bJv_mu_qcd=kTRUE; }
   if( btag1J && vetoJ3 ) { pass_ttme1bJv_mu_qcd=kTRUE; }
   if( btag2J && vetoJ3 ) { pass_ttme2bJv_mu_qcd=kTRUE; }
   if( btag0J && mtOver45_mu_qcd ) { pass_ttme0bMt_mu_qcd=kTRUE; }
   if( btag1J && mtOver45_mu_qcd ) { pass_ttme1bMt_mu_qcd=kTRUE; }
   if( btag2J && mtOver45_mu_qcd ) { pass_ttme2bMt_mu_qcd=kTRUE; }
   if( btag0J && vetoJ3 && mtOver45_mu_qcd ) { pass_ttme0bJvMt_mu_qcd=kTRUE; }
   if( btag1J && vetoJ3 && mtOver45_mu_qcd ) { pass_ttme1bJvMt_mu_qcd=kTRUE; }
   if( btag2J && vetoJ3 && mtOver45_mu_qcd ) { pass_ttme2bJvMt_mu_qcd=kTRUE; }
   if( isMC ){
     SF_ttme_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0);
     SF_ttme_mu_qcd_IDIsoHLT_errUp = SF_ttme_mu_qcd_IDIsoHLT 
      + std::sqrt( pow(SF_qcdMu_IDIso_errUp,2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
     SF_ttme_mu_qcd_IDIsoHLT_errDn = SF_ttme_mu_qcd_IDIsoHLT
      - std::sqrt( pow(SF_qcdMu_IDIso_errDn,2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2));
   }
  }
  if( twoQCDLEMu && min2goodJs ){ // ele qcd
   if( btag0J ) { pass_ttme0b_ele_qcd=kTRUE; }
   if( btag1J ) { pass_ttme1b_ele_qcd=kTRUE; }
   if( btag2J ) { pass_ttme2b_ele_qcd=kTRUE; }
   if( btag0J && vetoJ3 ) { pass_ttme0bJv_ele_qcd=kTRUE; }
   if( btag1J && vetoJ3 ) { pass_ttme1bJv_ele_qcd=kTRUE; }
   if( btag2J && vetoJ3 ) { pass_ttme2bJv_ele_qcd=kTRUE; }
   if( btag0J && mtOver45_ele_qcd ) { pass_ttme0bMt_ele_qcd=kTRUE; }
   if( btag1J && mtOver45_ele_qcd ) { pass_ttme1bMt_ele_qcd=kTRUE; }
   if( btag2J && mtOver45_ele_qcd ) { pass_ttme2bMt_ele_qcd=kTRUE; }
   if( btag0J && vetoJ3 && mtOver45_ele_qcd ) { pass_ttme0bJvMt_ele_qcd=kTRUE; }
   if( btag1J && vetoJ3 && mtOver45_ele_qcd ) { pass_ttme1bJvMt_ele_qcd=kTRUE; }
   if( btag2J && vetoJ3 && mtOver45_ele_qcd ) { pass_ttme2bJvMt_ele_qcd=kTRUE; }
   if( isMC ){
     SF_ttme_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso * SF_goodMu_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0);
     SF_ttme_ele_qcd_IDIsoHLT_errUp = SF_ttme_ele_qcd_IDIsoHLT 
      + std::sqrt( pow(SF_qcdEle_IDIso_errUp,2) + pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) );
     SF_ttme_ele_qcd_IDIsoHLT_errDn = SF_ttme_ele_qcd_IDIsoHLT
      - std::sqrt( pow(SF_qcdEle_IDIso_errDn,2) + pow(SF_goodMu_IDIsoHLT_errDn->at(0),2));
   }
  }
  // total weight
  if( isMC ){
   // ttme 
   weight_ttme0b_mu_good  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec *  SF_CSVrwt2gJs / nrEvents;
   weight_ttme0b_mu_qcd   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec *  SF_CSVrwt2gJs / nrEvents;
   weight_ttme0b_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs / nrEvents;
   weight_ttme0b_ele_qcd  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs / nrEvents;
   weight_ttme1b_mu_good  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec *  SF_CSVrwt2gJs * SF_topBJ / nrEvents;
   weight_ttme1b_mu_qcd   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec *  SF_CSVrwt2gJs * SF_topBJ / nrEvents;
   weight_ttme1b_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_topBJ / nrEvents;
   weight_ttme1b_ele_qcd  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_topBJ / nrEvents;
   weight_ttme2b_mu_good  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec *  SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme2b_mu_qcd   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec *  SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme2b_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
   weight_ttme2b_ele_qcd  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_CSVrwt2gJs * SF_top2BJs / nrEvents;
  }
  else{
   // ttme
   weight_ttme0b_mu_good  = 1.; 
   weight_ttme0b_mu_qcd   = 1.; 
   weight_ttme0b_ele_good = 1.; 
   weight_ttme0b_ele_qcd  = 1.; 
   weight_ttme1b_mu_good  = 1.; 
   weight_ttme1b_mu_qcd   = 1.; 
   weight_ttme1b_ele_good = 1.; 
   weight_ttme1b_ele_qcd  = 1.; 
   weight_ttme2b_mu_good  = 1.; 
   weight_ttme2b_mu_qcd   = 1.; 
   weight_ttme2b_ele_good = 1.; 
   weight_ttme2b_ele_qcd  = 1.; 
  }

  // ttme0b
  fillHistWriter( pass_ttme0b_mu_good, pass_ttme0b_mu_qcd, pass_ttme0b_ele_good, pass_ttme0b_ele_qcd,
                  0, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme0b_mu_good, weight_ttme0b_mu_qcd, weight_ttme0b_ele_good, weight_ttme0b_ele_qcd
                );
  // ttme1b
  fillHistWriter( pass_ttme1b_mu_good, pass_ttme1b_mu_qcd, pass_ttme1b_ele_good, pass_ttme1b_ele_qcd,
                  1, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1b_mu_good, weight_ttme1b_mu_qcd, weight_ttme1b_ele_good, weight_ttme1b_ele_qcd
                );
  // ttme2b
  fillHistWriter( pass_ttme2b_mu_good, pass_ttme2b_mu_qcd, pass_ttme2b_ele_good, pass_ttme2b_ele_qcd,
                  2, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2b_mu_good, weight_ttme2b_mu_qcd, weight_ttme2b_ele_good, weight_ttme2b_ele_qcd
                );
  // ttme0bJv
  fillHistWriter( pass_ttme0bJv_mu_good, pass_ttme0bJv_mu_qcd, pass_ttme0bJv_ele_good, pass_ttme0bJv_ele_qcd,
                  3, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme0b_mu_good, weight_ttme0b_mu_qcd, weight_ttme0b_ele_good, weight_ttme0b_ele_qcd
                );
  // ttme1bJv
  fillHistWriter( pass_ttme1bJv_mu_good, pass_ttme1bJv_mu_qcd, pass_ttme1bJv_ele_good, pass_ttme1bJv_ele_qcd,
                  4, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1b_mu_good, weight_ttme1b_mu_qcd, weight_ttme1b_ele_good, weight_ttme1b_ele_qcd
                );
  // ttme2bJv
  fillHistWriter( pass_ttme2bJv_mu_good, pass_ttme2bJv_mu_qcd, pass_ttme2bJv_ele_good, pass_ttme2bJv_ele_qcd,
                  5, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2b_mu_good, weight_ttme2b_mu_qcd, weight_ttme2b_ele_good, weight_ttme2b_ele_qcd
                );

  // ttme0bMt
  fillHistWriter( pass_ttme0bMt_mu_good, pass_ttme0bMt_mu_qcd, pass_ttme0bMt_ele_good, pass_ttme0bMt_ele_qcd,
                  6, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme0b_mu_good, weight_ttme0b_mu_qcd, weight_ttme0b_ele_good, weight_ttme0b_ele_qcd
                );
  // ttme1bMt
  fillHistWriter( pass_ttme1bMt_mu_good, pass_ttme1bMt_mu_qcd, pass_ttme1bMt_ele_good, pass_ttme1bMt_ele_qcd,
                  7, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1b_mu_good, weight_ttme1b_mu_qcd, weight_ttme1b_ele_good, weight_ttme1b_ele_qcd
                );
  // ttme2bMt
  fillHistWriter( pass_ttme2bMt_mu_good, pass_ttme2bMt_mu_qcd, pass_ttme2bMt_ele_good, pass_ttme2bMt_ele_qcd,
                  8, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2b_mu_good, weight_ttme2b_mu_qcd, weight_ttme2b_ele_good, weight_ttme2b_ele_qcd
                );

  // ttme0bJvMt
  fillHistWriter( pass_ttme0bJvMt_mu_good, pass_ttme0bJvMt_mu_qcd, pass_ttme0bJvMt_ele_good, pass_ttme0bJvMt_ele_qcd,
                  9, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme0b_mu_good, weight_ttme0b_mu_qcd, weight_ttme0b_ele_good, weight_ttme0b_ele_qcd
                );
  // ttme1bJvMt
  fillHistWriter( pass_ttme1bJvMt_mu_good, pass_ttme1bJvMt_mu_qcd, pass_ttme1bJvMt_ele_good, pass_ttme1bJvMt_ele_qcd,
                  10, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme1b_mu_good, weight_ttme1b_mu_qcd, weight_ttme1b_ele_good, weight_ttme1b_ele_qcd
                );
  // ttme2bJvMt
  fillHistWriter( pass_ttme2bJvMt_mu_good, pass_ttme2bJvMt_mu_qcd, pass_ttme2bJvMt_ele_good, pass_ttme2bJvMt_ele_qcd,
                  11, 0,
                  MET_pt, MET_phi,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme2b_mu_good, weight_ttme2b_mu_qcd, weight_ttme2b_ele_good, weight_ttme2b_ele_qcd
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

 outfile->Close();
}

