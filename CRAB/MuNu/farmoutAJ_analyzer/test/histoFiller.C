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

 std::cout<<"    Nr. Entries: "<<nrEntries<<std::endl;
 for (Long64_t jentry=0; jentry<nrEntries;jentry++) {
  //std::cout<<" entry "<<jentry<<std::endl;
  if(jentry%5000==0) std::cout<<"    entry "<<jentry<<std::endl;
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
   std::cout<<isWl<<" "<<isWc<<" "<<isWcc<<" "<<isWbb<<std::endl;

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

  // define some filter variables
  oneGoodMuon = 
   HLT_IsoMu24_eta2p1_v_fired 
   && nrGoodMu==1 && nrVetoMu<=1 && nrVetoEle==0;
  twoGoodMuons = 
   HLT_IsoMu24_eta2p1_v_fired
   && nrGoodMu==2 && nrVetoMu<=2 && nrVetoEle==0;
  oneQCDMuon = 
   nrQCDMu==1 && nrVetoMu==0 && nrVetoEle==0;
  twoQCDMuons = 
   HLT_IsoMu24_eta2p1_v_fired
   && nrGoodMu==1 && nrQCDMu==1 && nrVetoMu<=1 && nrVetoEle==0;
 
  oneGoodElectron = 
   HLT_Ele27_WP80_fired
   && nrGoodEle==1 && nrVetoEle<=1 && nrVetoMu==0;
  twoGoodElectrons = 
   HLT_Ele27_WP80_fired
   && nrGoodEle==2 && nrVetoEle<=2 && nrVetoMu==0;
  oneQCDElectron = 
   nrQCDEle==1 && nrVetoEle==0 && nrVetoMu==0;
  twoQCDElectrons =  
   HLT_Ele27_WP80_fired
   && nrGoodEle==1 && nrQCDEle==1 && nrVetoEle<=1 && nrVetoMu==0;
  
  twoGoodLMuE = HLT_IsoMu24_eta2p1_v_fired
   && nrGoodEle==1 && nrVetoEle<=1
   && nrGoodMu==1  && nrVetoMu<=1;
  twoGoodLEMu = HLT_Ele27_WP80_fired
   && nrGoodEle==1 && nrVetoEle<=1
   && nrGoodMu==1  && nrVetoMu<=1;
  twoQCDLeptons = 
   nrQCDMu==1   && nrVetoMu==0 &&
   nrGoodEle==1 && nrVetoEle<=1;

  min2goodJs = 
   nrGoodJets>=2 && nrFwdJets==0;
  exactly2goodJs = 
   nrGoodJets==2 && nrFwdJets==0;
  min2goodBJs = 
   nrGoodJets>=2 && nrFwdJets==0
   && goodJ1_CSV>0.898 && goodJ2_CSV>0.898;
  exactly2goodBJs = 
   nrGoodJets==2 && nrFwdJets==0
   && goodJ1_CSV>0.898 && goodJ2_CSV>0.898;
  aGoodBJaFwdJ = 
   nrGoodJets==1 && nrFwdJets==1 
   && goodJ1_CSV>0.898;

  // SFs for CSV
  SF_top2BJs = goodJ1_SF_CSVT * goodJ2_SF_CSVT; 
  SF_top2BJs_errUp = goodJ1_SF_CSVT_errUp * goodJ2_SF_CSVT_errUp;
  SF_top2BJs_errDn = goodJ1_SF_CSVT_errDn * goodJ2_SF_CSVT_errDn; 
  SF_topBJ = goodJ1_SF_CSVT;

  //std::cout<<"SF_top2BJs: "<<SF_top2BJs
  // <<" SF_top2BJs_errUp: "<<SF_top2BJs_errUp
  // <<" SF_top2BJs_errDn: "<<SF_top2BJs_errDn<<std::endl;
  SF_CSVreweight = goodJ1_CSVreweight * goodJ2_CSVreweight;

  // define some variables that get plotted
  // good mu
  mt_mu_good = mt_goodMuon;
  mt_mu_good_uesUp   = mt_goodMuon_uesUp;
  mt_mu_good_uesDown = mt_goodMuon_uesDn;
  if( shift=="JESUp" ) { mt_mu_good = mt_goodMuon_jesUp; }
  if( shift=="JESDown" ) { mt_mu_good = mt_goodMuon_jesDn; }
  if( shift=="LESUp" )  { mt_mu_good = mt_goodMuon_eesUp; }
  if( shift=="LESDown" )  { mt_mu_good = 2 * mt_goodMuon - mt_goodMuon_eesUp; };// { mt = mt_goodMuon_eesDn; }
  if( nrGoodMu>0 ){
   lep_mu_good_pt = goodMu_pt_vec->at(0);
   lep_mu_good_eta = goodMu_eta_vec->at(0);
   lep_mu_good_phi = goodMu_phi_vec->at(0);
  }
  // qcd mu
  mt_mu_qcd = mt_qcdMuon;
  mt_mu_qcd_uesUp   = mt_qcdMuon_uesUp;
  mt_mu_qcd_uesDown = mt_qcdMuon_uesDn;
  if( shift=="JESUp" ) { mt_mu_qcd = mt_qcdMuon_jesUp; }
  if( shift=="JESDown" ) { mt_mu_qcd = mt_qcdMuon_jesDn; }
  if( shift=="LESUp" )  { mt_mu_qcd = mt_qcdMuon_eesUp; }
  if( shift=="LESDown" )  { mt_mu_qcd = 2 * mt_qcdMuon - mt_qcdMuon_eesUp; };// { mt = mt_qcdMuon_eesDn; }
  lep_mu_qcd_pt =  qcdMu_pt ;
  lep_mu_qcd_eta = qcdMu_eta;
  lep_mu_qcd_phi = qcdMu_phi;
  // good ele
  mt_ele_good = mt_goodElectron;
  mt_ele_good_uesUp   = mt_goodElectron_uesUp;
  mt_ele_good_uesDown = mt_goodElectron_uesDn;
  if( shift=="JESUp" ) { mt_ele_good = mt_goodElectron_jesUp; }
  if( shift=="JESDown" ) { mt_ele_good = mt_goodElectron_jesDn; }
  if( shift=="LESUp" )  { mt_ele_good = mt_goodElectron_eesUp; }
  if( shift=="LESDown" )  { mt_ele_good = 2 * mt_goodElectron - mt_goodElectron_eesUp; };// { mt = mt_goodElectron_eesDn; }
  if( nrGoodEle>0) {
   lep_ele_good_pt = goodEle_pt_vec->at(0);
   lep_ele_good_eta = goodEle_eta_vec->at(0);
   lep_ele_good_phi = goodEle_phi_vec->at(0);
  }
  // qcd ele
  mt_ele_qcd = mt_qcdElectron;
  mt_ele_qcd_uesUp   = mt_qcdElectron_uesUp;
  mt_ele_qcd_uesDown = mt_qcdElectron_uesDn;
  if( shift=="JESUp" ) { mt_ele_qcd = mt_qcdElectron_jesUp; }
  if( shift=="JESDown" ) { mt_ele_qcd = mt_qcdElectron_jesDn; }
  if( shift=="LESUp" )  { mt_ele_qcd = mt_qcdElectron_eesUp; }
  if( shift=="LESDown" )  { mt_ele_qcd = 2 * mt_qcdElectron - mt_qcdElectron_eesUp; };// { mt = mt_qcdElectron_eesDn; }
  lep_ele_qcd_pt =  qcdEle_pt ;
  lep_ele_qcd_eta = qcdEle_eta;
  lep_ele_qcd_phi = qcdEle_phi;

  // dr J1 J2
  dRgoodJ1J2 = -1.; 
  dphiJJ = dPhi(goodJ1_phi, goodJ2_phi);
  dRgoodJ1J2 = std::sqrt( ((goodJ1_eta-goodJ2_eta)*(goodJ1_eta-goodJ2_eta)) + (dphiJJ*dphiJJ) );

  // Dijet Mass
  fourVec_J1.SetPtEtaPhiM(goodJ1_pt, goodJ1_eta, goodJ1_phi, goodJ1_mass);
  fourVec_J2.SetPtEtaPhiM(goodJ2_pt, goodJ2_eta, goodJ2_phi, goodJ2_mass);
  fourVec_J3.SetPtEtaPhiM(goodJ3_pt, goodJ3_eta, goodJ3_phi, goodJ3_mass);
  fourVec_J4.SetPtEtaPhiM(goodJ4_pt, goodJ4_eta, goodJ4_phi, goodJ4_mass);
  fourVec_J1J2 = fourVec_J1 + fourVec_J2;
  fourVec_J3J4 = fourVec_J3 + fourVec_J4;
  goodJ1J2_mass = fourVec_J1J2.M();
  goodJ3J4_mass = fourVec_J3J4.M();

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
  if( oneGoodMuon && exactly2goodJs ){ // mu good
   pass_wjj_mu_good=kTRUE; 
   nrEntries_mu_wjj_good_postcut++;
   if ( exactly2goodBJs ){
    pass_wbb_mu_good=kTRUE; 
    nrEntries_mu_wbb_good_postcut++;
   }
   if( isMC ){
    SF_wjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    SF_wjj_mu_good_IDIsoHLT_errUp = SF_wjj_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
    SF_wjj_mu_good_IDIsoHLT_errDn = SF_wjj_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDMuon && exactly2goodJs ){ // mu qcd
   pass_wjj_mu_qcd=kTRUE; 
   nrEntries_mu_wjj_qcd_postcut++;
   if ( exactly2goodBJs ){
    pass_wbb_mu_qcd=kTRUE; 
    nrEntries_mu_wbb_qcd_postcut++;
   }
   if( isMC ){
    SF_wjj_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
    SF_wjj_mu_qcd_IDIsoHLT_errUp = SF_wjj_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
    SF_wjj_mu_qcd_IDIsoHLT_errDn = SF_wjj_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
   }
  }
  if( oneGoodElectron && exactly2goodJs ){ // ele good
   pass_wjj_ele_good=kTRUE; 
   nrEntries_ele_wjj_good_postcut++;
   if ( exactly2goodBJs ){
    pass_wbb_ele_good=kTRUE; 
    nrEntries_ele_wbb_good_postcut++;
   }
   if( isMC ){
    SF_wjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    SF_wjj_ele_good_IDIsoHLT_errUp = SF_wjj_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
    SF_wjj_ele_good_IDIsoHLT_errDn = SF_wjj_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDElectron && exactly2goodJs ){ // ele qcd
   pass_wjj_ele_qcd=kTRUE; 
   nrEntries_ele_wjj_qcd_postcut++;
   if ( exactly2goodBJs ){
    pass_wbb_ele_qcd=kTRUE; 
    nrEntries_ele_wbb_qcd_postcut++;
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
   weight_wjj_mu_good  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_wjj_mu_qcd   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_wjj_ele_good = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   weight_wjj_ele_qcd  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   // wjj EMu
   weight_wjj_mu_good_EMuUp  = SF_wjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_wjj_mu_qcd_EMuUp   = SF_wjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_wjj_ele_good_EMuUp = SF_wjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   weight_wjj_ele_qcd_EMuUp  = SF_wjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   weight_wjj_mu_good_EMuDown  = SF_wjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_wjj_mu_qcd_EMuDown   = SF_wjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
   weight_wjj_ele_good_EMuDown = SF_wjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   weight_wjj_ele_qcd_EMuDown  = SF_wjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
   // wbb
   weight_wbb_mu_good  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_mu_qcd   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_ele_good = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_ele_qcd  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   // wbb CSV
   weight_wbb_mu_good_CSVUp  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_wbb_mu_qcd_CSVUp   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_wbb_ele_good_CSVUp = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_wbb_ele_qcd_CSVUp  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_wbb_mu_good_CSVDown  = SF_wjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_wbb_mu_qcd_CSVDown   = SF_wjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_wbb_ele_good_CSVDown = SF_wjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_wbb_ele_qcd_CSVDown  = SF_wjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
   // wbb EMu
   weight_wbb_mu_good_EMuUp  = SF_wjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_mu_qcd_EMuUp   = SF_wjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_ele_good_EMuUp = SF_wjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_ele_qcd_EMuUp  = SF_wjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_mu_good_EMuDown  = SF_wjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_mu_qcd_EMuDown   = SF_wjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_ele_good_EMuDown = SF_wjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_wbb_ele_qcd_EMuDown  = SF_wjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
  }
  else{
   // wjj
   weight_wjj_mu_good  = 1.; 
   weight_wjj_mu_qcd   = 1.; 
   weight_wjj_ele_good = 1.; 
   weight_wjj_ele_qcd  = 1.; 
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
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_wjj_mu_good, weight_wjj_mu_qcd, weight_wjj_ele_good, weight_wjj_ele_qcd
               );
  if( shift=="SFs"){
   // wjj: EMu Up
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 3,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wjj_mu_good_EMuUp, weight_wjj_mu_qcd_EMuUp, weight_wjj_ele_good_EMuUp, weight_wjj_ele_qcd_EMuUp
                 );
   // wjj: EMu Down
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 4,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wjj_mu_good_EMuDown, weight_wjj_mu_qcd_EMuDown, weight_wjj_ele_good_EMuDown, weight_wjj_ele_qcd_EMuDown
                 );
   // wjj: UES Up
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 5,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_wjj_mu_good, weight_wjj_mu_qcd, weight_wjj_ele_good, weight_wjj_ele_qcd
                 );
   // wjj: UES Down
   fillHistWriter( pass_wjj_mu_good, pass_wjj_mu_qcd, pass_wjj_ele_good, pass_wjj_ele_qcd,
                   3, 6,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_wjj_mu_good, weight_wjj_mu_qcd, weight_wjj_ele_good, weight_wjj_ele_qcd
                 );
  }

  /////////
  // wbb 0
  /////////
  // wbb: simple
  fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                  0, 0,
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_wbb_mu_good, weight_wbb_mu_qcd, weight_wbb_ele_good, weight_wbb_ele_qcd
                );
  if( shift=="SFs"){
   // wbb: CSV Up
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 1,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_EMuUp, weight_wbb_mu_qcd_EMuUp, weight_wbb_ele_good_EMuUp, weight_wbb_ele_qcd_EMuUp
                 );
   // wbb: CSV Down
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 2,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_CSVDown, weight_wbb_mu_qcd_CSVDown, weight_wbb_ele_good_CSVDown, weight_wbb_ele_qcd_CSVDown
                 );
   // wbb: EMu Up
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 3,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_EMuUp, weight_wbb_mu_qcd_EMuUp, weight_wbb_ele_good_EMuUp, weight_wbb_ele_qcd_EMuUp
                 );
   // wbb: EMu Down
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 4,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_wbb_mu_good_EMuDown, weight_wbb_mu_qcd_EMuDown, weight_wbb_ele_good_EMuDown, weight_wbb_ele_qcd_EMuDown
                 );
   // wbb: UES Up
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 5,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_wbb_mu_good, weight_wbb_mu_qcd, weight_wbb_ele_good, weight_wbb_ele_qcd
                 );
   // wbb: UES Down
   fillHistWriter( pass_wbb_mu_good, pass_wbb_mu_qcd, pass_wbb_ele_good, pass_wbb_ele_qcd,
                   0, 6,
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
  if( twoGoodLMuE && exactly2goodBJs ){ // mu good
   pass_ttme_mu_good=kTRUE; 
   nrEntries_mu_ttme_good_postcut++;
   if( isMC ){
    SF_ttme_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0)
    SF_ttme_mu_good_IDIsoHLT_errUp = SF_ttme_mu_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
    SF_ttme_mu_good_IDIsoHLT_errDn = SF_ttme_mu_good_IDIsoHLT
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) );
   }
  }
  if( twoGoodLEMu && exactly2goodBJs ){ // ele good
   pass_ttme_ele_good=kTRUE; 
   nrEntries_ele_ttme_good_postcut++;
   if( isMC ){
    SF_ttme_ele_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0)
    SF_ttme_ele_good_IDIsoHLT_errUp = SF_ttme_ele_good_IDIsoHLT 
     + std::sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
    SF_ttme_ele_good_IDIsoHLT_errDn = SF_ttme_ele_good_IDIsoHLT
     - std::sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) );
   }
  }
  if( twoQCDLeptons && exactly2goodBJs ){ // mu/ele qcd
   pass_ttme_mu_qcd=kTRUE; 
   nrEntries_mu_ttme_qcd_postcut++;
   pass_ttme_ele_qcd=kTRUE; 
   nrEntries_ele_ttme_qcd_postcut++;
   if( isMC ){
     SF_ttme_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0);
     SF_ttme_mu_qcd_IDIsoHLT_errUp = SF_ttme_mu_qcd_IDIsoHLT 
      + std::sqrt( pow(SF_qcdMu_IDIso_errUp,2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
     SF_ttme_mu_qcd_IDIsoHLT_errDn = SF_ttme_mu_qcd_IDIsoHLT
      - std::sqrt( pow(SF_qcdMu_IDIso_errDn,2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2));

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
   weight_ttme_mu_good  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_mu_qcd   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_ele_good = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_ele_qcd  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   // ttme CSV
   weight_ttme_mu_good_CSVUp  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttme_mu_qcd_CSVUp   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttme_ele_good_CSVUp = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttme_ele_qcd_CSVUp  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttme_mu_good_CSVDown  = SF_ttme_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_ttme_mu_qcd_CSVDown   = SF_ttme_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_ttme_ele_good_CSVDown = SF_ttme_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_ttme_ele_qcd_CSVDown  = SF_ttme_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
   // ttme EMu
   weight_ttme_mu_good_EMuUp  = SF_ttme_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_mu_qcd_EMuUp   = SF_ttme_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_ele_good_EMuUp = SF_ttme_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_ele_qcd_EMuUp  = SF_ttme_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_mu_good_EMuDown  = SF_ttme_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_mu_qcd_EMuDown   = SF_ttme_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_ele_good_EMuDown = SF_ttme_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttme_ele_qcd_EMuDown  = SF_ttme_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
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
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttme_mu_good, weight_ttme_mu_qcd, weight_ttme_ele_good, weight_ttme_ele_qcd
                );
  if( shift=="SFs"){
   // ttme: CSV Up
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 1,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_EMuUp, weight_ttme_mu_qcd_EMuUp, weight_ttme_ele_good_EMuUp, weight_ttme_ele_qcd_EMuUp
                 );
   // ttme: CSV Down
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 2,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_CSVDown, weight_ttme_mu_qcd_CSVDown, weight_ttme_ele_good_CSVDown, weight_ttme_ele_qcd_CSVDown
                 );
   // ttme: EMu Up
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 3,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_EMuUp, weight_ttme_mu_qcd_EMuUp, weight_ttme_ele_good_EMuUp, weight_ttme_ele_qcd_EMuUp
                 );
   // ttme: EMu Down
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 4,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttme_mu_good_EMuDown, weight_ttme_mu_qcd_EMuDown, weight_ttme_ele_good_EMuDown, weight_ttme_ele_qcd_EMuDown
                 );
   // ttme: UES Up
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 5,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_ttme_mu_good, weight_ttme_mu_qcd, weight_ttme_ele_good, weight_ttme_ele_qcd
                 );
   // ttme: UES Down
   fillHistWriter( pass_ttme_mu_good, pass_ttme_mu_qcd, pass_ttme_ele_good, pass_ttme_ele_qcd,
                   1, 6,
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
  if( oneGoodMuon && min2goodBJs ){ // mu good
   pass_ttjjj_mu_good=kTRUE;
   nrEntries_mu_ttjjj_good_postcut++;
   if( isMC ){
    SF_ttjjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    SF_ttjjj_mu_good_IDIsoHLT_errUp = SF_ttjjj_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
    SF_ttjjj_mu_good_IDIsoHLT_errDn = SF_ttjjj_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDMuon && min2goodBJs ){ // mu qcd
   pass_ttjjj_mu_qcd=kTRUE;
   nrEntries_mu_ttjjj_qcd_postcut++;
   if( isMC ){
    SF_ttjjj_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
    SF_ttjjj_mu_qcd_IDIsoHLT_errUp = SF_ttjjj_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
    SF_ttjjj_mu_qcd_IDIsoHLT_errDn = SF_ttjjj_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
   }
  }
  if( oneGoodElectron && min2goodBJs ){ // ele good
   pass_ttjjj_ele_good=kTRUE;
   nrEntries_ele_ttjjj_good_postcut++;
   if( isMC ){
    SF_ttjjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    SF_ttjjj_ele_good_IDIsoHLT_errUp = SF_ttjjj_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
    SF_ttjjj_ele_good_IDIsoHLT_errDn = SF_ttjjj_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDElectron && min2goodBJs ){ // ele qcd
   pass_ttjjj_ele_qcd=kTRUE;
   nrEntries_ele_ttjjj_qcd_postcut++;
   if( isMC ){
    SF_ttjjj_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso;
    SF_ttjjj_ele_qcd_IDIsoHLT_errUp = SF_ttjjj_ele_qcd_IDIsoHLT + SF_qcdEle_IDIso_errUp;
    SF_ttjjj_ele_qcd_IDIsoHLT_errDn = SF_ttjjj_ele_qcd_IDIsoHLT - SF_qcdEle_IDIso_errDn;
   }
  }

  // total weight
  if( isMC ){
   // ttjjj 
   weight_ttjjj_mu_good  = SF_ttjjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_qcd   = SF_ttjjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_good = SF_ttjjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_qcd  = SF_ttjjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   // ttjjj CSV
   weight_ttjjj_mu_good_CSVUp  = SF_ttjjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_mu_qcd_CSVUp   = SF_ttjjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_ele_good_CSVUp = SF_ttjjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_ele_qcd_CSVUp  = SF_ttjjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
   weight_ttjjj_mu_good_CSVDown  = SF_ttjjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_ttjjj_mu_qcd_CSVDown   = SF_ttjjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_ttjjj_ele_good_CSVDown = SF_ttjjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
   weight_ttjjj_ele_qcd_CSVDown  = SF_ttjjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
   // ttjjj EMu
   weight_ttjjj_mu_good_EMuUp  = SF_ttjjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_qcd_EMuUp   = SF_ttjjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_good_EMuUp = SF_ttjjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_qcd_EMuUp  = SF_ttjjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_good_EMuDown  = SF_ttjjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_mu_qcd_EMuDown   = SF_ttjjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_good_EMuDown = SF_ttjjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
   weight_ttjjj_ele_qcd_EMuDown  = SF_ttjjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
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
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_ttjjj_mu_good, weight_ttjjj_mu_qcd, weight_ttjjj_ele_good, weight_ttjjj_ele_qcd
                );
  if( shift=="SFs"){
   // ttjjj: CSV Up
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 1,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_EMuUp, weight_ttjjj_mu_qcd_EMuUp, weight_ttjjj_ele_good_EMuUp, weight_ttjjj_ele_qcd_EMuUp
                 );
   // ttjjj: CSV Down
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 2,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_CSVDown, weight_ttjjj_mu_qcd_CSVDown, weight_ttjjj_ele_good_CSVDown, weight_ttjjj_ele_qcd_CSVDown
                 );
   // ttjjj: EMu Up
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 3,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_EMuUp, weight_ttjjj_mu_qcd_EMuUp, weight_ttjjj_ele_good_EMuUp, weight_ttjjj_ele_qcd_EMuUp
                 );
   // ttjjj: EMu Down
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 4,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_ttjjj_mu_good_EMuDown, weight_ttjjj_mu_qcd_EMuDown, weight_ttjjj_ele_good_EMuDown, weight_ttjjj_ele_qcd_EMuDown
                 );
   // ttjjj: UES Up
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 5,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_ttjjj_mu_good, weight_ttjjj_mu_qcd, weight_ttjjj_ele_good, weight_ttjjj_ele_qcd
                 );
   // ttjjj: UES Down
   fillHistWriter( pass_ttjjj_mu_good, pass_ttjjj_mu_qcd, pass_ttjjj_ele_good, pass_ttjjj_ele_qcd,
                   2, 6,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_ttjjj_mu_good, weight_ttjjj_mu_qcd, weight_ttjjj_ele_good, weight_ttjjj_ele_qcd
                 );
  }
  //////////////////////////
  // end ttjjj Selection 1
  //////////////////////////

  //////////////////////////
  // begin stt Selection 2
  //////////////////////////
  Bool_t pass_stt_mu_good=kFALSE;
  Bool_t pass_stt_mu_qcd=kFALSE;
  Bool_t pass_stt_ele_good=kFALSE;
  Bool_t pass_stt_ele_qcd=kFALSE;
  if( oneGoodMuon && aGoodBJaFwdJ ){ // mu good
   pass_stt_mu_good=kTRUE;
   nrEntries_mu_stt_good_postcut++;
   if( isMC ){
    SF_stt_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    SF_stt_mu_good_IDIsoHLT_errUp = SF_stt_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
    SF_stt_mu_good_IDIsoHLT_errDn = SF_stt_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDMuon && aGoodBJaFwdJ ){ // mu qcd
   pass_stt_mu_qcd=kTRUE;
   nrEntries_mu_stt_qcd_postcut++;
   if( isMC ){
    SF_stt_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
    SF_stt_mu_qcd_IDIsoHLT_errUp = SF_stt_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
    SF_stt_mu_qcd_IDIsoHLT_errDn = SF_stt_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
   }
  }
  if( oneGoodElectron && aGoodBJaFwdJ ){ // ele good
   pass_stt_ele_good=kTRUE;
   nrEntries_ele_stt_good_postcut++;
   if( isMC ){
    SF_stt_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    SF_stt_ele_good_IDIsoHLT_errUp = SF_stt_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
    SF_stt_ele_good_IDIsoHLT_errDn = SF_stt_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
   }
  }
  if( oneQCDElectron && aGoodBJaFwdJ ){ // ele qcd
   pass_stt_ele_qcd=kTRUE;
   nrEntries_ele_stt_qcd_postcut++;
   if( isMC ){
    SF_stt_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso;
    SF_stt_ele_qcd_IDIsoHLT_errUp = SF_stt_ele_qcd_IDIsoHLT + SF_qcdEle_IDIso_errUp;
    SF_stt_ele_qcd_IDIsoHLT_errDn = SF_stt_ele_qcd_IDIsoHLT - SF_qcdEle_IDIso_errDn;
   }
  }

  // total weight
  if( isMC ){
   // stt 
   weight_stt_mu_good  = SF_stt_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ / nrEvents;
   weight_stt_mu_qcd   = SF_stt_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ / nrEvents;
   weight_stt_ele_good = SF_stt_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ / nrEvents;
   weight_stt_ele_qcd  = SF_stt_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ / nrEvents;
   // stt CSV
   weight_stt_mu_good_CSVUp  = SF_stt_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ_errUp / nrEvents;
   weight_stt_mu_qcd_CSVUp   = SF_stt_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ_errUp / nrEvents;
   weight_stt_ele_good_CSVUp = SF_stt_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ_errUp / nrEvents;
   weight_stt_ele_qcd_CSVUp  = SF_stt_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ_errUp / nrEvents;
   weight_stt_mu_good_CSVDown  = SF_stt_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ_errDn / nrEvents;
   weight_stt_mu_qcd_CSVDown   = SF_stt_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ_errDn / nrEvents;
   weight_stt_ele_good_CSVDown = SF_stt_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ_errDn / nrEvents;
   weight_stt_ele_qcd_CSVDown  = SF_stt_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ_errDn / nrEvents;
   // stt EMu
   weight_stt_mu_good_EMuUp  = SF_stt_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ / nrEvents;
   weight_stt_mu_qcd_EMuUp   = SF_stt_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ / nrEvents;
   weight_stt_ele_good_EMuUp = SF_stt_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ / nrEvents;
   weight_stt_ele_qcd_EMuUp  = SF_stt_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ / nrEvents;
   weight_stt_mu_good_EMuDown  = SF_stt_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ / nrEvents;
   weight_stt_mu_qcd_EMuDown   = SF_stt_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_topBJ / nrEvents;
   weight_stt_ele_good_EMuDown = SF_stt_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ / nrEvents;
   weight_stt_ele_qcd_EMuDown  = SF_stt_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_topBJ / nrEvents;
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
                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                  weight_stt_mu_good, weight_stt_mu_qcd, weight_stt_ele_good, weight_stt_ele_qcd
                );
  if( shift=="SFs"){
   // stt: CSV Up
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 1,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_EMuUp, weight_stt_mu_qcd_EMuUp, weight_stt_ele_good_EMuUp, weight_stt_ele_qcd_EMuUp
                 );
   // stt: CSV Down
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 2,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_CSVDown, weight_stt_mu_qcd_CSVDown, weight_stt_ele_good_CSVDown, weight_stt_ele_qcd_CSVDown
                 );
   // stt: EMu Up
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 3,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_EMuUp, weight_stt_mu_qcd_EMuUp, weight_stt_ele_good_EMuUp, weight_stt_ele_qcd_EMuUp
                 );
   // stt: EMu Down
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 4,
                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
                   weight_stt_mu_good_EMuDown, weight_stt_mu_qcd_EMuDown, weight_stt_ele_good_EMuDown, weight_stt_ele_qcd_EMuDown
                 );
   // stt: UES Up
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 5,
                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
                   weight_stt_mu_good, weight_stt_mu_qcd, weight_stt_ele_good, weight_stt_ele_qcd
                 );
   // stt: UES Down
   fillHistWriter( pass_stt_mu_good, pass_stt_mu_qcd, pass_stt_ele_good, pass_stt_ele_qcd,
                   4, 6,
                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
                   weight_stt_mu_good, weight_stt_mu_qcd, weight_stt_ele_good, weight_stt_ele_qcd
                 );
  }

  //////////////////////////
  // end stt Selection 2
  //////////////////////////

//  ////////////////////////////////
//  // begin dyjj, dybb Selection 3,0
//  ////////////////////////////////
//  Bool_t pass_dyjj_mu_good=kFALSE;
//  Bool_t pass_dyjj_mu_qcd=kFALSE;
//  Bool_t pass_dybb_mu_good=kFALSE;
//  Bool_t pass_dybb_mu_qcd=kFALSE;
//  Bool_t pass_dyjj_ele_good=kFALSE;
//  Bool_t pass_dyjj_ele_qcd=kFALSE;
//  Bool_t pass_dybb_ele_good=kFALSE;
//  Bool_t pass_dybb_ele_qcd=kFALSE;
//  if( oneGoodMuon && exactly2goodJs ){ // mu good
//   pass_dyjj_mu_good=kTRUE; 
//   nrEntries_mu_dyjj_good_postcut++;
//   if ( exactly2goodBJs ){
//    pass_dybb_mu_good=kTRUE; 
//    nrEntries_mu_dybb_good_postcut++;
//   }
//   if( isMC ){
//    SF_dyjj_mu_good_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
//    SF_dyjj_mu_good_IDIsoHLT_errUp = SF_dyjj_mu_good_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
//    SF_dyjj_mu_good_IDIsoHLT_errDn = SF_dyjj_mu_good_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
//   }
//  }
//  if( oneQCDMuon && exactly2goodJs ){ // mu qcd
//   pass_dyjj_mu_qcd=kTRUE; 
//   nrEntries_mu_dyjj_qcd_postcut++;
//   if ( exactly2goodBJs ){
//    pass_dybb_mu_qcd=kTRUE; 
//    nrEntries_mu_dybb_qcd_postcut++;
//   }
//   if( isMC ){
//    SF_dyjj_mu_qcd_IDIsoHLT = SF_qcdMu_IDIso;
//    SF_dyjj_mu_qcd_IDIsoHLT_errUp = SF_dyjj_mu_qcd_IDIsoHLT + SF_qcdMu_IDIso_errUp;
//    SF_dyjj_mu_qcd_IDIsoHLT_errDn = SF_dyjj_mu_qcd_IDIsoHLT - SF_qcdMu_IDIso_errDn;
//   }
//  }
//  if( oneGoodElectron && exactly2goodJs ){ // ele good
//   pass_dyjj_ele_good=kTRUE; 
//   nrEntries_ele_dyjj_good_postcut++;
//   if ( exactly2goodBJs ){
//    pass_dybb_ele_good=kTRUE; 
//    nrEntries_ele_dybb_good_postcut++;
//   }
//   if( isMC ){
//    SF_dyjj_ele_good_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
//    SF_dyjj_ele_good_IDIsoHLT_errUp = SF_dyjj_ele_good_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
//    SF_dyjj_ele_good_IDIsoHLT_errDn = SF_dyjj_ele_good_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
//   }
//  }
//  if( oneQCDElectron && exactly2goodJs ){ // ele qcd
//   pass_dyjj_ele_qcd=kTRUE; 
//   nrEntries_ele_dyjj_qcd_postcut++;
//   if ( exactly2goodBJs ){
//    pass_dybb_ele_qcd=kTRUE; 
//    nrEntries_ele_dybb_qcd_postcut++;
//   }
//   if( isMC ){
//    SF_dyjj_ele_qcd_IDIsoHLT = SF_qcdEle_IDIso;
//    SF_dyjj_ele_qcd_IDIsoHLT_errUp = SF_dyjj_ele_qcd_IDIsoHLT + SF_qcdEle_IDIso_errUp;
//    SF_dyjj_ele_qcd_IDIsoHLT_errDn = SF_dyjj_ele_qcd_IDIsoHLT - SF_qcdEle_IDIso_errDn;
//   }
//  }
//  // total weight
//  if( isMC ){
//   // dyjj
//   weight_dyjj_mu_good  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
//   weight_dyjj_mu_qcd   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
//   weight_dyjj_ele_good = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
//   weight_dyjj_ele_qcd  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
//   // dyjj EMu
//   weight_dyjj_mu_good_EMuUp  = SF_dyjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
//   weight_dyjj_mu_qcd_EMuUp   = SF_dyjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
//   weight_dyjj_ele_good_EMuUp = SF_dyjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
//   weight_dyjj_ele_qcd_EMuUp  = SF_dyjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
//   weight_dyjj_mu_good_EMuDown  = SF_dyjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
//   weight_dyjj_mu_qcd_EMuDown   = SF_dyjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec / nrEvents;
//   weight_dyjj_ele_good_EMuDown = SF_dyjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
//   weight_dyjj_ele_qcd_EMuDown  = SF_dyjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec / nrEvents;
//   // dybb
//   weight_dybb_mu_good  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_mu_qcd   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_ele_good = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_ele_qcd  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
//   // dybb CSV
//   weight_dybb_mu_good_CSVUp  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
//   weight_dybb_mu_qcd_CSVUp   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errUp / nrEvents;
//   weight_dybb_ele_good_CSVUp = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
//   weight_dybb_ele_qcd_CSVUp  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errUp / nrEvents;
//   weight_dybb_mu_good_CSVDown  = SF_dyjj_mu_good_IDIsoHLT  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
//   weight_dybb_mu_qcd_CSVDown   = SF_dyjj_mu_qcd_IDIsoHLT   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs_errDn / nrEvents;
//   weight_dybb_ele_good_CSVDown = SF_dyjj_ele_good_IDIsoHLT * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
//   weight_dybb_ele_qcd_CSVDown  = SF_dyjj_ele_qcd_IDIsoHLT  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs_errDn / nrEvents;
//   // dybb EMu
//   weight_dybb_mu_good_EMuUp  = SF_dyjj_mu_good_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_mu_qcd_EMuUp   = SF_dyjj_mu_qcd_IDIsoHLT_errUp   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_ele_good_EMuUp = SF_dyjj_ele_good_IDIsoHLT_errUp * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_ele_qcd_EMuUp  = SF_dyjj_ele_qcd_IDIsoHLT_errUp  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_mu_good_EMuDown  = SF_dyjj_mu_good_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_mu_qcd_EMuDown   = SF_dyjj_mu_qcd_IDIsoHLT_errDn   * SF_lumiWeightPU * lumi_mu * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_ele_good_EMuDown = SF_dyjj_ele_good_IDIsoHLT_errDn * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
//   weight_dybb_ele_qcd_EMuDown  = SF_dyjj_ele_qcd_IDIsoHLT_errDn  * SF_lumiWeightPU * lumi_ele * crossSec * SF_top2BJs / nrEvents;
//  }
//  else{
//   // dyjj
//   weight_dyjj_mu_good  = 1.; 
//   weight_dyjj_mu_qcd   = 1.; 
//   weight_dyjj_ele_good = 1.; 
//   weight_dyjj_ele_qcd  = 1.; 
//   // dyjj EMu
//   weight_dyjj_mu_good_EMuUp  = 1.; 
//   weight_dyjj_mu_qcd_EMuUp   = 1.; 
//   weight_dyjj_ele_good_EMuUp = 1.; 
//   weight_dyjj_ele_qcd_EMuUp  = 1.; 
//   weight_dyjj_mu_good_EMuDown  = 1.;
//   weight_dyjj_mu_qcd_EMuDown   = 1.;
//   weight_dyjj_ele_good_EMuDown = 1.;
//   weight_dyjj_ele_qcd_EMuDown  = 1.;
//   // dybb
//   weight_dybb_mu_good  = 1.; 
//   weight_dybb_mu_qcd   = 1.; 
//   weight_dybb_ele_good = 1.; 
//   weight_dybb_ele_qcd  = 1.; 
//   // dybb CSV
//   weight_dybb_mu_good_CSVUp  = 1.; 
//   weight_dybb_mu_qcd_CSVUp   = 1.; 
//   weight_dybb_ele_good_CSVUp = 1.; 
//   weight_dybb_ele_qcd_CSVUp  = 1.; 
//   weight_dybb_mu_good_CSVDown  = 1.;
//   weight_dybb_mu_qcd_CSVDown   = 1.;
//   weight_dybb_ele_good_CSVDown = 1.;
//   weight_dybb_ele_qcd_CSVDown  = 1.;
//   // dybb EMu
//   weight_dybb_mu_good_EMuUp  = 1.; 
//   weight_dybb_mu_qcd_EMuUp   = 1.; 
//   weight_dybb_ele_good_EMuUp = 1.; 
//   weight_dybb_ele_qcd_EMuUp  = 1.; 
//   weight_dybb_mu_good_EMuDown  = 1.;
//   weight_dybb_mu_qcd_EMuDown   = 1.;
//   weight_dybb_ele_good_EMuDown = 1.;
//   weight_dybb_ele_qcd_EMuDown  = 1.;
//  }
//
//  /////////
//  // dyjj 3
//  /////////
//  // dyjj: simple
//  fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
//                  3, 0,
//                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                  weight_dyjj_mu_good, weight_dyjj_mu_qcd, weight_dyjj_ele_good, weight_dyjj_ele_qcd
//               );
//  if( shift=="SFs"){
//   // dyjj: EMu Up
//   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
//                   3, 3,
//                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                   weight_dyjj_mu_good_EMuUp, weight_dyjj_mu_qcd_EMuUp, weight_dyjj_ele_good_EMuUp, weight_dyjj_ele_qcd_EMuUp
//                 );
//   // dyjj: EMu Down
//   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
//                   3, 4,
//                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                   weight_dyjj_mu_good_EMuDown, weight_dyjj_mu_qcd_EMuDown, weight_dyjj_ele_good_EMuDown, weight_dyjj_ele_qcd_EMuDown
//                 );
//   // dyjj: UES Up
//   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
//                   3, 5,
//                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
//                   weight_dyjj_mu_good, weight_dyjj_mu_qcd, weight_dyjj_ele_good, weight_dyjj_ele_qcd
//                 );
//   // dyjj: UES Down
//   fillHistWriter( pass_dyjj_mu_good, pass_dyjj_mu_qcd, pass_dyjj_ele_good, pass_dyjj_ele_qcd,
//                   3, 6,
//                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
//                   weight_dyjj_mu_good, weight_dyjj_mu_qcd, weight_dyjj_ele_good, weight_dyjj_ele_qcd
//                 );
//  }
//
//  /////////
//  // dybb 0
//  /////////
//  // dybb: simple
//  fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                  0, 0,
//                  mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                  weight_dybb_mu_good, weight_dybb_mu_qcd, weight_dybb_ele_good, weight_dybb_ele_qcd
//                );
//  if( shift=="SFs"){
//   // dybb: CSV Up
//   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                   0, 1,
//                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                   weight_dybb_mu_good_EMuUp, weight_dybb_mu_qcd_EMuUp, weight_dybb_ele_good_EMuUp, weight_dybb_ele_qcd_EMuUp
//                 );
//   // dybb: CSV Down
//   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                   0, 2,
//                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                   weight_dybb_mu_good_CSVDown, weight_dybb_mu_qcd_CSVDown, weight_dybb_ele_good_CSVDown, weight_dybb_ele_qcd_CSVDown
//                 );
//   // dybb: EMu Up
//   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                   0, 3,
//                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                   weight_dybb_mu_good_EMuUp, weight_dybb_mu_qcd_EMuUp, weight_dybb_ele_good_EMuUp, weight_dybb_ele_qcd_EMuUp
//                 );
//   // dybb: EMu Down
//   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                   0, 4,
//                   mt_mu_good, mt_mu_qcd, mt_ele_good, mt_ele_qcd,
//                   weight_dybb_mu_good_EMuDown, weight_dybb_mu_qcd_EMuDown, weight_dybb_ele_good_EMuDown, weight_dybb_ele_qcd_EMuDown
//                 );
//   // dybb: UES Up
//   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                   0, 5,
//                   mt_mu_good_uesUp, mt_mu_qcd_uesUp, mt_ele_good_uesUp, mt_ele_qcd_uesUp,
//                   weight_dybb_mu_good, weight_dybb_mu_qcd, weight_dybb_ele_good, weight_dybb_ele_qcd
//                 );
//   // dybb: UES Down
//   fillHistWriter( pass_dybb_mu_good, pass_dybb_mu_qcd, pass_dybb_ele_good, pass_dybb_ele_qcd,
//                   0, 6,
//                   mt_mu_good_uesDown, mt_mu_qcd_uesDown, mt_ele_good_uesDown, mt_ele_qcd_uesDown,
//                   weight_dybb_mu_good, weight_dybb_mu_qcd, weight_dybb_ele_good, weight_dybb_ele_qcd
//                 );
//  }
//  ////////////////////////////////
//  // end wjj, wbb Selection 3,0
//  ////////////////////////////////

 } 
//
// Float_t bmin = h_wbb_good_mt.GetXaxis()->FindBin(0.);
// Float_t bmax = h_wbb_good_mt.GetXaxis()->FindBin(20.);
// // write a log
// std::ofstream logfile (outfileName+".log", std::ofstream::out);
// logfile<<"isMu = "<<isMu<<std::endl;
// logfile<<"isMC = "<<isMC<<std::endl;
// logfile<<"shift = "<<shift<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                 W+bb Selection                  --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_wbb_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_wbb_good_lep_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_wbb_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_wbb_qcd_lep_eta.Integral()<<std::endl;
//  Float_t size_wbb_mt_good020 = h_wbb_good_mt.Integral(bmin,bmax);
//  Float_t size_wbb_mt_qcd020 = h_wbb_qcd_mt.Integral(bmin,bmax);
// logfile<<"  Nr. Good Events in 0<mT<20: "<<size_wbb_mt_good020<<std::endl;
// logfile<<"  Nr. QCD Events in 0<mT<20: "<<size_wbb_mt_qcd020<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                TT(1m1e) Selection               --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_tt1m1e_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_tt1m1e_good_lep_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_tt1m1e_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_tt1m1e_qcd_lep_eta.Integral()<<std::endl;
//  Float_t size_tt1m1e_mt_good020 = h_tt1m1e_good_mt.Integral(bmin,bmax);
//  Float_t size_tt1m1e_mt_qcd020 = h_tt1m1e_qcd_mt.Integral(bmin,bmax);
// logfile<<"  Nr. Good Events in 0<mT<20: "<<size_tt1m1e_mt_good020<<std::endl;
// logfile<<"  Nr. QCD Events in 0<mT<20: "<<size_tt1m1e_mt_qcd020<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                 TT(3j) Selection                --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_tt3j_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_tt3j_good_lep_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_tt3j_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_tt3j_qcd_lep_eta.Integral()<<std::endl;
//  Float_t size_tt3j_mt_good020 = h_tt3j_good_mt.Integral(bmin,bmax);
//  Float_t size_tt3j_mt_qcd020 = h_tt3j_qcd_mt.Integral(bmin,bmax);
// logfile<<"  Nr. Good Events in 0<mT<20: "<<size_tt3j_mt_good020<<std::endl;
// logfile<<"  Nr. QCD Events in 0<mT<20: "<<size_tt3j_mt_qcd020<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--                  W+jj Selection                 --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_wjj_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_wjj_good_lep_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_wjj_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_wjj_qcd_lep_eta.Integral()<<std::endl;
//  Float_t size_wjj_mt_good020 = h_wjj_good_mt.Integral(bmin,bmax);
//  Float_t size_wjj_mt_qcd020 = h_wjj_qcd_mt.Integral(bmin,bmax);
// logfile<<"  Nr. Good Events in 0<mT<20: "<<size_wjj_mt_good020<<std::endl;
// logfile<<"  Nr. QCD Events in 0<mT<20: "<<size_wjj_mt_qcd020<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--             Single Top (t) Selection            --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_stt_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_stt_good_lep_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_stt_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_stt_qcd_lep_eta.Integral()<<std::endl;
//  Float_t size_stt_mt_good020 = h_stt_good_mt.Integral(bmin,bmax);
//  Float_t size_stt_mt_qcd020 = h_stt_qcd_mt.Integral(bmin,bmax);
// logfile<<"  Nr. Good Events in 0<mT<20: "<<size_stt_mt_good020<<std::endl;
// logfile<<"  Nr. QCD Events in 0<mT<20: "<<size_stt_mt_qcd020<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--              Drell-Yan+jj Selection             --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_dyjj_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_dyjj_good_lep1_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_dyjj_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_dyjj_qcd_lep1_eta.Integral()<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"--              Drell-Yan+bb Selection             --"<<std::endl;
// logfile<<"-----------------------------------------------------"<<std::endl;
// logfile<<"  Nr. Initial Entries: "<<nrEntries<<std::endl;
// logfile<<"  Nr. Entries Passing Good Cut: "<<nrEntries_dybb_good_postcut<<std::endl;
// logfile<<"  Nr. Good Events After Weight: "<<h_dybb_good_lep1_eta.Integral()<<std::endl;
// logfile<<"  Nr. Entries Passing QCD Cut: "<<nrEntries_dybb_qcd_postcut<<std::endl;
// logfile<<"  Nr. QCD Events After Weight: "<<h_dybb_qcd_lep1_eta.Integral()<<std::endl;
// logfile.close();
// 
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
// // dybb
// writeHistWriter( 5, 0, isW );
// if( shift=="SFs"){
//  writeHistWriter( 5, 1, isW );
//  writeHistWriter( 5, 2, isW );
//  writeHistWriter( 5, 3, isW );
//  writeHistWriter( 5, 4, isW );
//  writeHistWriter( 5, 5, isW );
//  writeHistWriter( 5, 6, isW );
// }
// // dyjj
// writeHistWriter( 6, 0, isW );
// if( shift=="SFs"){
//  writeHistWriter( 6, 1, isW );
//  writeHistWriter( 6, 2, isW );
//  writeHistWriter( 6, 3, isW );
//  writeHistWriter( 6, 4, isW );
//  writeHistWriter( 6, 5, isW );
//  writeHistWriter( 6, 6, isW );
// }

 outfile->Close();
}

