#define histoFiller_cxx
#include "histoFiller.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>

void histoFiller::Loop(TString outfileName, Bool_t isMu, Bool_t isMC, Bool_t isQCD,
      TString cutType, TString shift, Int_t jType, UInt_t luminosity, UInt_t nrEvents,
      Float_t crossSec)
{
 if (fChain == 0) return;
 Long64_t nrEntries = fChain->GetEntries();
 //Long64_t nrEntries = fChain->GetEntriesFast();
 //Long64_t nb = 0;
 Float_t nrEntries_postcut = 0.;

 TH1F *h_goodJ1_pt = new TH1F("h_goodJ1_pt","",12,25,205); h_goodJ1_pt->Sumw2();
 TH1F *h_goodJ2_pt = new TH1F("h_goodJ2_pt","",12,25,205); h_goodJ2_pt->Sumw2();
 TH1F *h_goodLep_pt = new TH1F("h_goodLep_pt","",12,25,205); h_goodLep_pt->Sumw2();
 TH1F *h_goodJ1_eta = new TH1F("h_goodJ1_eta","",20,-3,5); h_goodJ1_eta->Sumw2();
 TH1F *h_goodJ2_eta = new TH1F("h_goodJ2_eta","",20,-3,5); h_goodJ2_eta->Sumw2();
 TH1F *h_goodLep_eta = new TH1F("h_goodLep_eta","",20,-3,5); h_goodLep_eta->Sumw2();
 TH1F *h_goodJ1_phi = new TH1F("h_goodJ1_phi","",35,-3.4033,5.7594); h_goodJ1_phi->Sumw2();
 TH1F *h_goodJ2_phi = new TH1F("h_goodJ2_phi","",35,-3.4033,5.7594); h_goodJ2_phi->Sumw2();
 TH1F *h_goodLep_phi = new TH1F("h_goodLep_phi","",35,-3.4033,5.7594); h_goodLep_phi->Sumw2();
 TH1F *h_goodJ1_CSV = new TH1F("h_goodJ1_CSV","",30,0,1); h_goodJ1_CSV->Sumw2();
 TH1F *h_goodJ2_CSV = new TH1F("h_goodJ2_CSV","",30,0,1); h_goodJ2_CSV->Sumw2();
 TH1F *h_mt = new TH1F("h_mt","",40,0,200); h_mt->Sumw2();
 TH1F *h_dRgoodJ1J2 = new TH1F("h_dRgoodJ1J2","",20,0,6); h_dRgoodJ1J2->Sumw2();

 TH1F *h_goodJ1_pt_CSVerrUp = new TH1F("h_goodJ1_pt_CSVerrUp","",12,25,205); h_goodJ1_pt_CSVerrUp->Sumw2();
 TH1F *h_goodJ2_pt_CSVerrUp = new TH1F("h_goodJ2_pt_CSVerrUp","",12,25,205); h_goodJ2_pt_CSVerrUp->Sumw2();
 TH1F *h_goodLep_pt_CSVerrUp = new TH1F("h_goodLep_pt_CSVerrUp","",12,25,205); h_goodLep_pt_CSVerrUp->Sumw2();
 TH1F *h_goodJ1_eta_CSVerrUp = new TH1F("h_goodJ1_eta_CSVerrUp","",20,-3,5); h_goodJ1_eta_CSVerrUp->Sumw2();
 TH1F *h_goodJ2_eta_CSVerrUp = new TH1F("h_goodJ2_eta_CSVerrUp","",20,-3,5); h_goodJ2_eta_CSVerrUp->Sumw2();
 TH1F *h_goodLep_eta_CSVerrUp = new TH1F("h_goodLep_eta_CSVerrUp","",20,-3,5); h_goodLep_eta_CSVerrUp->Sumw2();
 TH1F *h_goodJ1_phi_CSVerrUp = new TH1F("h_goodJ1_phi_CSVerrUp","",35,-3.4033,5.7594); h_goodJ1_phi_CSVerrUp->Sumw2();
 TH1F *h_goodJ2_phi_CSVerrUp = new TH1F("h_goodJ2_phi_CSVerrUp","",35,-3.4033,5.7594); h_goodJ2_phi_CSVerrUp->Sumw2();
 TH1F *h_goodLep_phi_CSVerrUp = new TH1F("h_goodLep_phi_CSVerrUp","",35,-3.4033,5.7594); h_goodLep_phi_CSVerrUp->Sumw2();
 TH1F *h_goodJ1_CSV_CSVerrUp = new TH1F("h_goodJ1_CSV_CSVerrUp","",30,0,1); h_goodJ1_CSV_CSVerrUp->Sumw2();
 TH1F *h_goodJ2_CSV_CSVerrUp = new TH1F("h_goodJ2_CSV_CSVerrUp","",30,0,1); h_goodJ2_CSV_CSVerrUp->Sumw2();
 TH1F *h_mt_CSVerrUp = new TH1F("h_mt_CSVerrUp","",40,0,200); h_mt_CSVerrUp->Sumw2();
 TH1F *h_dRgoodJ1J2_CSVerrUp = new TH1F("h_dRgoodJ1J2_CSVerrUp","",20,0,6); h_dRgoodJ1J2_CSVerrUp->Sumw2();

 TH1F *h_goodJ1_pt_CSVerrDown = new TH1F("h_goodJ1_pt_CSVerrDown","",12,25,205); h_goodJ1_pt_CSVerrDown->Sumw2();
 TH1F *h_goodJ2_pt_CSVerrDown = new TH1F("h_goodJ2_pt_CSVerrDown","",12,25,205); h_goodJ2_pt_CSVerrDown->Sumw2();
 TH1F *h_goodLep_pt_CSVerrDown = new TH1F("h_goodLep_pt_CSVerrDown","",12,25,205); h_goodLep_pt_CSVerrDown->Sumw2();
 TH1F *h_goodJ1_eta_CSVerrDown = new TH1F("h_goodJ1_eta_CSVerrDown","",20,-3,5); h_goodJ1_eta_CSVerrDown->Sumw2();
 TH1F *h_goodJ2_eta_CSVerrDown = new TH1F("h_goodJ2_eta_CSVerrDown","",20,-3,5); h_goodJ2_eta_CSVerrDown->Sumw2();
 TH1F *h_goodLep_eta_CSVerrDown = new TH1F("h_goodLep_eta_CSVerrDown","",20,-3,5); h_goodLep_eta_CSVerrDown->Sumw2();
 TH1F *h_goodJ1_phi_CSVerrDown = new TH1F("h_goodJ1_phi_CSVerrDown","",35,-3.4033,5.7594); h_goodJ1_phi_CSVerrDown->Sumw2();
 TH1F *h_goodJ2_phi_CSVerrDown = new TH1F("h_goodJ2_phi_CSVerrDown","",35,-3.4033,5.7594); h_goodJ2_phi_CSVerrDown->Sumw2();
 TH1F *h_goodLep_phi_CSVerrDown = new TH1F("h_goodLep_phi_CSVerrDown","",35,-3.4033,5.7594); h_goodLep_phi_CSVerrDown->Sumw2();
 TH1F *h_goodJ1_CSV_CSVerrDown = new TH1F("h_goodJ1_CSV_CSVerrDown","",30,0,1); h_goodJ1_CSV_CSVerrDown->Sumw2();
 TH1F *h_goodJ2_CSV_CSVerrDown = new TH1F("h_goodJ2_CSV_CSVerrDown","",30,0,1); h_goodJ2_CSV_CSVerrDown->Sumw2();
 TH1F *h_mt_CSVerrDown = new TH1F("h_mt_CSVerrDown","",40,0,200); h_mt_CSVerrDown->Sumw2();
 TH1F *h_dRgoodJ1J2_CSVerrDown = new TH1F("h_dRgoodJ1J2_CSVerrDown","",20,0,6); h_dRgoodJ1J2_CSVerrDown->Sumw2();

 TH1F *h_goodJ1_pt_EMuerrUp = new TH1F("h_goodJ1_pt_EMuerrUp","",12,25,205); h_goodJ1_pt_EMuerrUp->Sumw2();
 TH1F *h_goodJ2_pt_EMuerrUp = new TH1F("h_goodJ2_pt_EMuerrUp","",12,25,205); h_goodJ2_pt_EMuerrUp->Sumw2();
 TH1F *h_goodLep_pt_EMuerrUp = new TH1F("h_goodLep_pt_EMuerrUp","",12,25,205); h_goodLep_pt_EMuerrUp->Sumw2();
 TH1F *h_goodJ1_eta_EMuerrUp = new TH1F("h_goodJ1_eta_EMuerrUp","",20,-3,5); h_goodJ1_eta_EMuerrUp->Sumw2();
 TH1F *h_goodJ2_eta_EMuerrUp = new TH1F("h_goodJ2_eta_EMuerrUp","",20,-3,5); h_goodJ2_eta_EMuerrUp->Sumw2();
 TH1F *h_goodLep_eta_EMuerrUp = new TH1F("h_goodLep_eta_EMuerrUp","",20,-3,5); h_goodLep_eta_EMuerrUp->Sumw2();
 TH1F *h_goodJ1_phi_EMuerrUp = new TH1F("h_goodJ1_phi_EMuerrUp","",35,-3.4033,5.7594); h_goodJ1_phi_EMuerrUp->Sumw2();
 TH1F *h_goodJ2_phi_EMuerrUp = new TH1F("h_goodJ2_phi_EMuerrUp","",35,-3.4033,5.7594); h_goodJ2_phi_EMuerrUp->Sumw2();
 TH1F *h_goodLep_phi_EMuerrUp = new TH1F("h_goodLep_phi_EMuerrUp","",35,-3.4033,5.7594); h_goodLep_phi_EMuerrUp->Sumw2();
 TH1F *h_goodJ1_CSV_EMuerrUp = new TH1F("h_goodJ1_CSV_EMuerrUp","",30,0,1); h_goodJ1_CSV_EMuerrUp->Sumw2();
 TH1F *h_goodJ2_CSV_EMuerrUp = new TH1F("h_goodJ2_CSV_EMuerrUp","",30,0,1); h_goodJ2_CSV_EMuerrUp->Sumw2();
 TH1F *h_mt_EMuerrUp = new TH1F("h_mt_EMuerrUp","",40,0,200); h_mt_EMuerrUp->Sumw2();
 TH1F *h_dRgoodJ1J2_EMuerrUp = new TH1F("h_dRgoodJ1J2_EMuerrUp","",20,0,6); h_dRgoodJ1J2_EMuerrUp->Sumw2();

 TH1F *h_goodJ1_pt_EMuerrDown = new TH1F("h_goodJ1_pt_EMuerrDown","",12,25,205); h_goodJ1_pt_EMuerrDown->Sumw2();
 TH1F *h_goodJ2_pt_EMuerrDown = new TH1F("h_goodJ2_pt_EMuerrDown","",12,25,205); h_goodJ2_pt_EMuerrDown->Sumw2();
 TH1F *h_goodLep_pt_EMuerrDown = new TH1F("h_goodLep_pt_EMuerrDown","",12,25,205); h_goodLep_pt_EMuerrDown->Sumw2();
 TH1F *h_goodJ1_eta_EMuerrDown = new TH1F("h_goodJ1_eta_EMuerrDown","",20,-3,5); h_goodJ1_eta_EMuerrDown->Sumw2();
 TH1F *h_goodJ2_eta_EMuerrDown = new TH1F("h_goodJ2_eta_EMuerrDown","",20,-3,5); h_goodJ2_eta_EMuerrDown->Sumw2();
 TH1F *h_goodLep_eta_EMuerrDown = new TH1F("h_goodLep_eta_EMuerrDown","",20,-3,5); h_goodLep_eta_EMuerrDown->Sumw2();
 TH1F *h_goodJ1_phi_EMuerrDown = new TH1F("h_goodJ1_phi_EMuerrDown","",35,-3.4033,5.7594); h_goodJ1_phi_EMuerrDown->Sumw2();
 TH1F *h_goodJ2_phi_EMuerrDown = new TH1F("h_goodJ2_phi_EMuerrDown","",35,-3.4033,5.7594); h_goodJ2_phi_EMuerrDown->Sumw2();
 TH1F *h_goodLep_phi_EMuerrDown = new TH1F("h_goodLep_phi_EMuerrDown","",35,-3.4033,5.7594); h_goodLep_phi_EMuerrDown->Sumw2();
 TH1F *h_goodJ1_CSV_EMuerrDown = new TH1F("h_goodJ1_CSV_EMuerrDown","",30,0,1); h_goodJ1_CSV_EMuerrDown->Sumw2();
 TH1F *h_goodJ2_CSV_EMuerrDown = new TH1F("h_goodJ2_CSV_EMuerrDown","",30,0,1); h_goodJ2_CSV_EMuerrDown->Sumw2();
 TH1F *h_mt_EMuerrDown = new TH1F("h_mt_EMuerrDown","",40,0,200); h_mt_EMuerrDown->Sumw2();
 TH1F *h_dRgoodJ1J2_EMuerrDown = new TH1F("h_dRgoodJ1J2_EMuerrDown","",20,0,6); h_dRgoodJ1J2_EMuerrDown->Sumw2();

 std::cout<<"Nr. Entries: "<<nrEntries<<std::endl;
 for (Long64_t jentry=0; jentry<nrEntries;jentry++) {
  if(jentry%100000==0) std::cout<<" entry "<<jentry<<std::endl;
  Long64_t ientry = LoadTree(jentry);
  if (ientry < 0) break;
  //nb = fChain->GetEntry(jentry);

  // split up the W samples
  //0 = ignore
  //1 = W+light
  //2 = W+c
  //3 = W+cc
  //4 = W+bb

  twoCs  = (abs(goodJ1_partonFlavour)==4 && abs(goodJ2_partonFlavour)==4);
  someCs = (abs(goodJ1_partonFlavour)==4 || abs(goodJ2_partonFlavour)==4);
  someBs = (abs(goodJ1_partonFlavour)==5 || abs(goodJ2_partonFlavour)==5);

  isWl  = !someBs && !someCs;
  isWc  = !someBs &&  someCs && !twoCs;
  isWcc = !someBs &&  someCs &&  twoCs;
  isWbb =  someBs;

  if( isMC && jType==1 && !isWl){ continue; }
  if( isMC && jType==2 && !isWc){ continue; }
  if( isMC && jType==3 && !isWcc){ continue; }
  if( isMC && jType==4 && !isWbb){ continue; }

  // take care of scaling for inclusive/exclusive WJets samples
  if( isMC && jType!=0){
   if( LHEProduct<5 ){
    std::cout<<"LHEProduct: "<<LHEProduct<<" Event: "<<EVENT<<std::endl;
    break;
   }
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
  
  twoGoodLeptons = HLT_IsoMu24_eta2p1_v_fired
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

  // does the event pass our filter
  // wbb
  if( cutType=="wbb" ){
   if( !isQCD && isMu ){
    if( ! (oneGoodMuon && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
    }
   }
   else if( isQCD && isMu){
    if( ! (oneQCDMuon && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso;
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_qcdMu_IDIso_errUp;
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_qcdMu_IDIso_errDn;
    }
   }
   else if( !isQCD && !isMu ){
    if( ! (oneGoodElectron && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
    }
   }
   else if( isQCD && !isMu){
    if( ! (oneQCDElectron && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdEle_IDIso;
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_qcdEle_IDIso_errUp;
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_qcdEle_IDIso_errDn;
    }
   }
   // total weight
   if( isMC ){
    weight =          SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
    weight_CSVerrUp = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs_errUp / nrEvents;
    weight_CSVerrDn = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs_errDn / nrEvents;
    weight_EMuerrUp = SF_IDIsoHLT_errUp * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
    weight_EMuerrDn = SF_IDIsoHLT_errDn * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
   }
  }

  // tt3j
  if( cutType=="tt3j" ){
   if( !isQCD && isMu ){
    if( ! (oneGoodMuon && min2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_goodMu_IDIsoHLT_errUp->at(0);
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_goodMu_IDIsoHLT_errDn->at(0);
    }
   }
   else if( isQCD && isMu){
    if( ! (oneQCDMuon && min2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso;
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_qcdMu_IDIso_errUp;
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_qcdMu_IDIso_errDn;
    }
   }
   else if( !isQCD && !isMu ){
    if( ! (oneGoodElectron && min2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_goodEle_IDIsoHLT_errUp->at(0);
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_goodEle_IDIsoHLT_errDn->at(0);
    }
   }
   else if( isQCD && !isMu){
    if( ! (oneQCDElectron && min2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdEle_IDIso;
     SF_IDIsoHLT_errUp = SF_IDIsoHLT + SF_qcdEle_IDIso_errUp;
     SF_IDIsoHLT_errDn = SF_IDIsoHLT - SF_qcdEle_IDIso_errDn;
    }
   }
   if( isMC ){
    weight =          SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
    weight_CSVerrUp = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs_errUp / nrEvents;
    weight_CSVerrDn = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs_errDn / nrEvents;
    weight_EMuerrUp = SF_IDIsoHLT_errUp * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
    weight_EMuerrDn = SF_IDIsoHLT_errDn * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
   }
  }

  // tt1m1e
  if( cutType=="tt1m1e" ){
   if( !isQCD ){ 
    if( ! (twoGoodLeptons && min2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0)
     SF_IDIsoHLT_errUp = SF_IDIsoHLT 
      + sqrt( pow(SF_goodMu_IDIsoHLT_errUp->at(0),2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
      // + sqrt(SF_goodMu_IDIsoHLT_errUp->at(0)**2 + SF_goodEle_IDIso_errUp->at(0)**2);
     SF_IDIsoHLT_errDn = SF_IDIsoHLT
      - sqrt( pow(SF_goodMu_IDIsoHLT_errDn->at(0),2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2) );
      // - sqrt(SF_goodMu_IDIsoHLT_errDn->at(0)**2 + SF_goodEle_IDIso_errDn->at(0)**2);
    }
   }
   else if( isQCD ){
    if( ! (twoQCDLeptons && min2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso * SF_goodEle_IDIsoHLT->at(0); // SF_goodEle_IDIso->at(0);
     SF_IDIsoHLT_errUp = SF_IDIsoHLT 
      + sqrt( pow(SF_qcdMu_IDIso_errUp,2) + pow(SF_goodEle_IDIsoHLT_errUp->at(0),2) );
      // + sqrt(SF_qcdMu_IDIso_errUp**2 + SF_goodEle_IDIso_errUp->at(0)**2);
     SF_IDIsoHLT_errDn = SF_IDIsoHLT
      - sqrt( pow(SF_qcdMu_IDIso_errDn,2) + pow(SF_goodEle_IDIsoHLT_errDn->at(0),2));
      // - sqrt(SF_qcdMu_IDIso_errDn**2 + SF_goodEle_IDIso_errDn->at(0)**2);
    }
   }
   if( isMC ){
     weight =          SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
     weight_CSVerrUp = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs_errUp / nrEvents;
     weight_CSVerrDn = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs_errDn / nrEvents;
     weight_EMuerrUp = SF_IDIsoHLT_errUp * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
     weight_EMuerrDn = SF_IDIsoHLT_errDn * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
   }
  }

  // wjj
  if( cutType=="wjj" ){
   if( !isQCD && isMu ){
    if( ! (oneGoodMuon && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    }
   }
   else if( isQCD && isMu){
    if( ! (oneQCDMuon && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso;
    }
   }
   else if( !isQCD && !isMu ){
    if( ! (oneGoodElectron && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    }
   }
   else if( isQCD && !isMu){
    if( ! (oneQCDElectron && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdEle_IDIso;
    }
   }
   if( isMC ){
    weight = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec / nrEvents;
   }
  }

  // stt
  if( cutType=="stt" ){
   if( !isQCD && isMu ){
    if( ! (oneGoodMuon && aGoodBJaFwdJ) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0);
    }
   }
   else if( isQCD && isMu){
    if( ! (oneQCDMuon && aGoodBJaFwdJ) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso;
    }
   }
   else if( !isQCD && !isMu ){
    if( ! (oneGoodElectron && aGoodBJaFwdJ) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0);
    }
   }
   else if( isQCD && !isMu){
    if( ! (oneQCDElectron && aGoodBJaFwdJ) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdEle_IDIso;
    }
   }
   if( isMC ){
    weight = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_topBJ / nrEvents;
   }
  }

  // dyjj 
  if( cutType=="dyjj" ){
   if( !isQCD && isMu ){
    if( ! (twoGoodMuons && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodMu_IDIsoHLT->at(1); // * SF_goodMu_IDIso->at(1);
    }
   }
   else if( isQCD && isMu){
    if( ! (twoQCDMuons && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso * SF_goodMu_IDIsoHLT->at(0); // * SF_goodMu_IDIso->at(0);
    }
   }
   else if( !isQCD && !isMu ){
    if( ! (twoGoodElectrons && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(1); // * SF_goodEle_IDIso->at(1);
    }
   }
   else if( isQCD && !isMu){
    if( ! (twoQCDElectrons && exactly2goodJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdEle_IDIso * SF_goodEle_IDIsoHLT->at(0); // * SF_goodEle_IDIso->at(0);
    }
   }
   if( isMC ){
    weight = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec / nrEvents;
   }
  }

  // dybb 
  if( cutType=="dybb" ){
   if( !isQCD && isMu ){
    if( ! (twoGoodMuons && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodMu_IDIsoHLT->at(0) * SF_goodMu_IDIsoHLT->at(1); // * SF_goodMu_IDIso->at(1);
    }
   }
   else if( isQCD && isMu){
    if( ! (twoQCDMuons && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdMu_IDIso * SF_goodMu_IDIsoHLT->at(0); // * SF_goodMu_IDIso->at(0);
    }
   }
   else if( !isQCD && !isMu ){
    if( ! (twoGoodElectrons && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_goodEle_IDIsoHLT->at(0) * SF_goodEle_IDIsoHLT->at(1); // * SF_goodEle_IDIso->at(1);
    }
   }
   else if( isQCD && !isMu){
    if( ! (twoQCDElectrons && exactly2goodBJs) ){ continue; }
    nrEntries_postcut++;
    if( isMC ){
     SF_IDIsoHLT = SF_qcdEle_IDIso * SF_goodEle_IDIsoHLT->at(0); // * SF_goodEle_IDIso->at(0);
    }
   }
   if( isMC ){
    weight = SF_IDIsoHLT * SF_lumiWeightPU * luminosity * crossSec * SF_top2BJs / nrEvents;
   }
  }

  if( !isMC ){ weight=1.; }
  // then fill the histograms

  // jets
  h_goodJ1_pt->Fill(goodJ1_pt,weight);
  h_goodJ2_pt->Fill(goodJ2_pt,weight);
  h_goodJ1_eta->Fill(goodJ1_eta,weight);
  h_goodJ2_eta->Fill(goodJ2_eta,weight);
  h_goodJ1_phi->Fill(goodJ1_phi,weight);
  h_goodJ2_phi->Fill(goodJ2_phi,weight);
  h_goodJ1_CSV->Fill(goodJ1_CSV,weight);
  h_goodJ2_CSV->Fill(goodJ2_CSV,weight);
  dRgoodJ1J2 = -1.;
  if( min2goodJs ){
   dphiJJ = abs(goodJ1_phi - goodJ2_phi);
   if( dphiJJ>3.1416 ){ dphiJJ-=6.2832; }
   dRgoodJ1J2 = sqrt( ((goodJ1_eta-goodJ2_eta)*(goodJ1_eta-goodJ2_eta)) + (dphiJJ*dphiJJ) );
   h_dRgoodJ1J2->Fill(dRgoodJ1J2,weight);
  }
  // leptons + met
  if( isMu && !isQCD ){
   mt = mt_goodMuon;
   if( shift=="JetUp" ) { mt = mt_goodMuon_jesUp; }
   if( shift=="JetDown" ) { mt = mt_goodMuon_jesDn; }
   if( shift=="LepUp" )  { mt = mt_goodMuon_eesUp; }
   if( shift=="LepDown" )  { mt = 2 * mt_goodMuon - mt_goodMuon_eesUp; };// { mt = mt_goodMuon_eesDn; }
   if( shift=="UESUp" )  { mt = mt_goodMuon_uesUp; }
   if( shift=="UESDown" )  { mt = mt_goodMuon_uesDn; }
   lep_pt = goodMu_pt_vec->at(0);
   lep_eta = goodMu_eta_vec->at(0);
   lep_phi = goodMu_phi_vec->at(0);
  }
  else if( !isMu && !isQCD ){
   mt = mt_goodElectron;
   if( shift=="JetUp" ) { mt = mt_goodElectron_jesUp; }
   if( shift=="JetDown" ) { mt = mt_goodElectron_jesDn; }
   if( shift=="LepUp" )  { mt = mt_goodElectron_eesUp; }
   if( shift=="LepDown" ) { mt = 2 * mt_goodElectron - mt_goodElectron_eesUp; }// { mt = mt_goodElectron_eesDn; }
   if( shift=="UESUp" )  { mt = mt_goodElectron_uesUp; }
   if( shift=="UESDown" )  { mt = mt_goodElectron_uesDn; }
   lep_pt = goodEle_pt_vec->at(0);
   lep_eta = goodEle_eta_vec->at(0);
   lep_phi = goodEle_phi_vec->at(0);
  }
  else if( isMu && isQCD ){
   mt = mt_qcdMuon;
   if( shift=="JetUp" ) { mt = mt_qcdMuon_jesUp; }
   if( shift=="JetDown" ) { mt = mt_qcdMuon_jesDn; }
   if( shift=="LepUp" )  { mt = mt_qcdMuon_eesUp; }
   if( shift=="LepDown" )  { mt = 2 * mt_goodMuon - mt_qcdMuon_eesUp; }// { mt = mt_qcdMuon_eesDn; }
   if( shift=="UESUp" )  { mt = mt_qcdMuon_uesUp; }
   if( shift=="UESDown" )  { mt = mt_qcdMuon_uesDn; }
   lep_pt = qcdMu_pt;
   lep_eta = qcdMu_eta;
   lep_phi = qcdMu_phi;
  }
  else if( !isMu && isQCD ){
   mt = mt_qcdElectron;
   if( shift=="JetUp" ) { mt = mt_qcdElectron_jesUp; }
   if( shift=="JetDown" ) { mt = mt_qcdElectron_jesDn; }
   if( shift=="LepUp" )  { mt = mt_qcdElectron_eesUp; }
   if( shift=="LepDown" )  { mt = 2 * mt_goodElectron - mt_qcdElectron_eesUp; }// { mt = mt_qcdElectron_eesDn; }
   if( shift=="UESUp" )  { mt = mt_qcdElectron_uesUp; }
   if( shift=="UESDown" )  { mt = mt_qcdElectron_uesDn; }
   lep_pt = qcdEle_pt;
   lep_eta = qcdEle_eta;
   lep_phi = qcdEle_phi;
  }
  //std::cout<<"shift: "<<shift<<" mt: "<<mt<<std::endl;
  h_mt->Fill(mt,weight);
  h_goodLep_pt->Fill(lep_pt,weight);
  h_goodLep_eta->Fill(lep_eta,weight);
  h_goodLep_phi->Fill(lep_phi,weight);

  if( shift=="SFs" ){
   h_goodJ1_pt_CSVerrUp->Fill(goodJ1_pt,weight_CSVerrUp);
   h_goodJ2_pt_CSVerrUp->Fill(goodJ2_pt,weight_CSVerrUp);
   h_goodJ1_eta_CSVerrUp->Fill(goodJ1_eta,weight_CSVerrUp);
   h_goodJ2_eta_CSVerrUp->Fill(goodJ2_eta,weight_CSVerrUp);
   h_goodJ1_phi_CSVerrUp->Fill(goodJ1_phi,weight_CSVerrUp);
   h_goodJ2_phi_CSVerrUp->Fill(goodJ2_phi,weight_CSVerrUp);
   h_goodJ1_CSV_CSVerrUp->Fill(goodJ1_CSV,weight_CSVerrUp);
   h_goodJ2_CSV_CSVerrUp->Fill(goodJ2_CSV,weight_CSVerrUp);
   h_dRgoodJ1J2_CSVerrUp->Fill(dRgoodJ1J2,weight_CSVerrUp);
   h_mt_CSVerrUp->Fill(mt,weight_CSVerrUp);
   h_goodLep_pt_CSVerrUp->Fill(lep_pt,weight_CSVerrUp);
   h_goodLep_eta_CSVerrUp->Fill(lep_eta,weight_CSVerrUp);
   h_goodLep_phi_CSVerrUp->Fill(lep_phi,weight_CSVerrUp);

   h_goodJ1_pt_CSVerrDown->Fill(goodJ1_pt,weight_CSVerrDn);
   h_goodJ2_pt_CSVerrDown->Fill(goodJ2_pt,weight_CSVerrDn);
   h_goodJ1_eta_CSVerrDown->Fill(goodJ1_eta,weight_CSVerrDn);
   h_goodJ2_eta_CSVerrDown->Fill(goodJ2_eta,weight_CSVerrDn);
   h_goodJ1_phi_CSVerrDown->Fill(goodJ1_phi,weight_CSVerrDn);
   h_goodJ2_phi_CSVerrDown->Fill(goodJ2_phi,weight_CSVerrDn);
   h_goodJ1_CSV_CSVerrDown->Fill(goodJ1_CSV,weight_CSVerrDn);
   h_goodJ2_CSV_CSVerrDown->Fill(goodJ2_CSV,weight_CSVerrDn);
   h_dRgoodJ1J2_CSVerrDown->Fill(dRgoodJ1J2,weight_CSVerrDn);
   h_mt_CSVerrDown->Fill(mt,weight_CSVerrDn);
   h_goodLep_pt_CSVerrDown->Fill(lep_pt,weight_CSVerrDn);
   h_goodLep_eta_CSVerrDown->Fill(lep_eta,weight_CSVerrDn);
   h_goodLep_phi_CSVerrDown->Fill(lep_phi,weight_CSVerrDn);

   h_goodJ1_pt_EMuerrUp->Fill(goodJ1_pt,weight_EMuerrUp);
   h_goodJ2_pt_EMuerrUp->Fill(goodJ2_pt,weight_EMuerrUp);
   h_goodJ1_eta_EMuerrUp->Fill(goodJ1_eta,weight_EMuerrUp);
   h_goodJ2_eta_EMuerrUp->Fill(goodJ2_eta,weight_EMuerrUp);
   h_goodJ1_phi_EMuerrUp->Fill(goodJ1_phi,weight_EMuerrUp);
   h_goodJ2_phi_EMuerrUp->Fill(goodJ2_phi,weight_EMuerrUp);
   h_dRgoodJ1J2_EMuerrUp->Fill(dRgoodJ1J2,weight_EMuerrUp);
   h_mt_EMuerrUp->Fill(mt,weight_EMuerrUp);
   h_goodLep_pt_EMuerrUp->Fill(lep_pt,weight_EMuerrUp);
   h_goodLep_eta_EMuerrUp->Fill(lep_eta,weight_EMuerrUp);
   h_goodLep_phi_EMuerrUp->Fill(lep_phi,weight_EMuerrUp);

   h_goodJ1_pt_EMuerrDown->Fill(goodJ1_pt,weight_EMuerrDn);
   h_goodJ2_pt_EMuerrDown->Fill(goodJ2_pt,weight_EMuerrDn);
   h_goodJ1_eta_EMuerrDown->Fill(goodJ1_eta,weight_EMuerrDn);
   h_goodJ2_eta_EMuerrDown->Fill(goodJ2_eta,weight_EMuerrDn);
   h_goodJ1_phi_EMuerrDown->Fill(goodJ1_phi,weight_EMuerrDn);
   h_goodJ2_phi_EMuerrDown->Fill(goodJ2_phi,weight_EMuerrDn);
   h_dRgoodJ1J2_EMuerrDown->Fill(dRgoodJ1J2,weight_EMuerrDn);
   h_mt_EMuerrDown->Fill(mt,weight_EMuerrDn);
   h_goodLep_pt_EMuerrDown->Fill(lep_pt,weight_EMuerrDn);
   h_goodLep_eta_EMuerrDown->Fill(lep_eta,weight_EMuerrDn);
   h_goodLep_phi_EMuerrDown->Fill(lep_phi,weight_EMuerrDn);
  }
  //std::cout<<"Made it: "<<EVENT<<std::endl;
 } 

 std::cout<<"Nr. Entries Passing Cut: "<<nrEntries_postcut<<std::endl;
 std::cout<<"Nr. Events After Weight: "<<h_goodLep_eta->Integral()<<std::endl;
 std::cout<<"Weight: "<<weight<<std::endl;

 // write a log
 std::ofstream logfile (outfileName+".log", std::ofstream::out);
 logfile<<"Nr. Initial Entries: "<<nrEntries<<std::endl;
 logfile<<"Nr. Entries Passing Cut: "<<nrEntries_postcut<<std::endl;
 logfile<<"Nr. Events After Weight: "<<h_goodLep_eta->Integral()<<std::endl;
 logfile<<"Weight: "<<weight<<std::endl;
 logfile.close();
 
 // write these histograms to file
 TFile *outfile = new TFile(outfileName+".root","RECREATE");
 outfile->cd();

 h_goodJ1_pt->Write(); h_goodJ1_pt->Delete();
 h_goodJ2_pt->Write(); h_goodJ2_pt->Delete(); 
 h_goodJ1_eta->Write(); h_goodJ1_eta->Delete();
 h_goodJ2_eta->Write(); h_goodJ2_eta->Delete();
 h_goodJ1_phi->Write(); h_goodJ1_phi->Delete();
 h_goodJ2_phi->Write(); h_goodJ2_phi->Delete();
 h_goodJ1_CSV->Write(); h_goodJ1_CSV->Delete();
 h_goodJ2_CSV->Write(); h_goodJ2_CSV->Delete();
 h_dRgoodJ1J2->Write(); h_dRgoodJ1J2->Delete();
 h_mt->Write(); h_mt->Delete();
 h_goodLep_pt->Write(); h_goodLep_pt->Delete();
 h_goodLep_eta->Write(); h_goodLep_eta->Delete();
 h_goodLep_phi->Write(); h_goodLep_phi->Delete();

 if( shift=="SFs" ){
  h_goodJ1_pt_CSVerrUp->Write();  
  h_goodJ2_pt_CSVerrUp->Write();  
  h_goodJ1_eta_CSVerrUp->Write(); 
  h_goodJ2_eta_CSVerrUp->Write(); 
  h_goodJ1_phi_CSVerrUp->Write(); 
  h_goodJ2_phi_CSVerrUp->Write(); 
  h_goodJ1_CSV_CSVerrUp->Write(); 
  h_goodJ2_CSV_CSVerrUp->Write(); 
  h_dRgoodJ1J2_CSVerrUp->Write(); 
  h_mt_CSVerrUp->Write();         
  h_goodLep_pt_CSVerrUp->Write(); 
  h_goodLep_eta_CSVerrUp->Write();
  h_goodLep_phi_CSVerrUp->Write();

  h_goodJ1_pt_CSVerrDown->Write();  
  h_goodJ2_pt_CSVerrDown->Write();  
  h_goodJ1_eta_CSVerrDown->Write(); 
  h_goodJ2_eta_CSVerrDown->Write(); 
  h_goodJ1_phi_CSVerrDown->Write(); 
  h_goodJ2_phi_CSVerrDown->Write(); 
  h_goodJ1_CSV_CSVerrDown->Write(); 
  h_goodJ2_CSV_CSVerrDown->Write(); 
  h_dRgoodJ1J2_CSVerrDown->Write(); 
  h_mt_CSVerrDown->Write();         
  h_goodLep_pt_CSVerrDown->Write(); 
  h_goodLep_eta_CSVerrDown->Write();
  h_goodLep_phi_CSVerrDown->Write();

  h_goodJ1_pt_EMuerrUp->Write();  
  h_goodJ2_pt_EMuerrUp->Write();  
  h_goodJ1_eta_EMuerrUp->Write(); 
  h_goodJ2_eta_EMuerrUp->Write(); 
  h_goodJ1_phi_EMuerrUp->Write(); 
  h_goodJ2_phi_EMuerrUp->Write(); 
  h_goodJ1_CSV_EMuerrUp->Write(); 
  h_goodJ2_CSV_EMuerrUp->Write(); 
  h_dRgoodJ1J2_EMuerrUp->Write(); 
  h_mt_EMuerrUp->Write();         
  h_goodLep_pt_EMuerrUp->Write(); 
  h_goodLep_eta_EMuerrUp->Write();
  h_goodLep_phi_EMuerrUp->Write();

  h_goodJ1_pt_EMuerrDown->Write();  
  h_goodJ2_pt_EMuerrDown->Write();  
  h_goodJ1_eta_EMuerrDown->Write(); 
  h_goodJ2_eta_EMuerrDown->Write(); 
  h_goodJ1_phi_EMuerrDown->Write(); 
  h_goodJ2_phi_EMuerrDown->Write(); 
  h_goodJ1_CSV_EMuerrDown->Write(); 
  h_goodJ2_CSV_EMuerrDown->Write(); 
  h_dRgoodJ1J2_EMuerrDown->Write(); 
  h_mt_EMuerrDown->Write();         
  h_goodLep_pt_EMuerrDown->Write(); 
  h_goodLep_eta_EMuerrDown->Write();
  h_goodLep_phi_EMuerrDown->Write();
 }

 h_goodJ1_pt_CSVerrUp->Delete();
 h_goodJ2_pt_CSVerrUp->Delete(); 
 h_goodJ1_eta_CSVerrUp->Delete();
 h_goodJ2_eta_CSVerrUp->Delete();
 h_goodJ1_phi_CSVerrUp->Delete();
 h_goodJ2_phi_CSVerrUp->Delete();
 h_goodJ1_CSV_CSVerrUp->Delete();
 h_goodJ2_CSV_CSVerrUp->Delete();
 h_dRgoodJ1J2_CSVerrUp->Delete();
 h_mt_CSVerrUp->Delete();
 h_goodLep_pt_CSVerrUp->Delete();
 h_goodLep_eta_CSVerrUp->Delete();
 h_goodLep_phi_CSVerrUp->Delete();
                                   
 h_goodJ1_pt_CSVerrDown->Delete();
 h_goodJ2_pt_CSVerrDown->Delete(); 
 h_goodJ1_eta_CSVerrDown->Delete();
 h_goodJ2_eta_CSVerrDown->Delete();
 h_goodJ1_phi_CSVerrDown->Delete();
 h_goodJ2_phi_CSVerrDown->Delete();
 h_goodJ1_CSV_CSVerrDown->Delete();
 h_goodJ2_CSV_CSVerrDown->Delete();
 h_dRgoodJ1J2_CSVerrDown->Delete();
 h_mt_CSVerrDown->Delete();
 h_goodLep_pt_CSVerrDown->Delete();
 h_goodLep_eta_CSVerrDown->Delete();
 h_goodLep_phi_CSVerrDown->Delete();
                                   
 h_goodJ1_pt_EMuerrUp->Delete();
 h_goodJ2_pt_EMuerrUp->Delete(); 
 h_goodJ1_eta_EMuerrUp->Delete();
 h_goodJ2_eta_EMuerrUp->Delete();
 h_goodJ1_phi_EMuerrUp->Delete();
 h_goodJ2_phi_EMuerrUp->Delete();
 h_goodJ1_CSV_EMuerrUp->Delete();
 h_goodJ2_CSV_EMuerrUp->Delete();
 h_dRgoodJ1J2_EMuerrUp->Delete();
 h_mt_EMuerrUp->Delete();
 h_goodLep_pt_EMuerrUp->Delete();
 h_goodLep_eta_EMuerrUp->Delete();
 h_goodLep_phi_EMuerrUp->Delete();
                                   
 h_goodJ1_pt_EMuerrDown->Delete();
 h_goodJ2_pt_EMuerrDown->Delete(); 
 h_goodJ1_eta_EMuerrDown->Delete();
 h_goodJ2_eta_EMuerrDown->Delete();
 h_goodJ1_phi_EMuerrDown->Delete();
 h_goodJ2_phi_EMuerrDown->Delete();
 h_goodJ1_CSV_EMuerrDown->Delete();
 h_goodJ2_CSV_EMuerrDown->Delete();
 h_dRgoodJ1J2_EMuerrDown->Delete();
 h_mt_EMuerrDown->Delete();
 h_goodLep_pt_EMuerrDown->Delete();
 h_goodLep_eta_EMuerrDown->Delete();
 h_goodLep_phi_EMuerrDown->Delete();

 outfile->Close();
}
