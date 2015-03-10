/********************************
Instantiates histoFiller.C with
the correct chain and naming
for a definable set of parameters

Usage: 
root -l -b
.L callHistoFiller.cc
callHistoFiller()

root -l -b -q callHistoFiller.cc

Author: T.M.Perry UW-Madison
********************************/

#include <TStyle.h>
#include <vector>
#include <TChain.h>
#include "TROOT.h"
#include "TSystem.h"
#include "TApplication.h"
#include <iostream>
#include <exception>

void callHistoFiller()
{
 int error = 0;
 gROOT->ProcessLine(".L histoFiller.C++", &error);
 if(error!=0){std::cout<<"ERROR LOADING histoFiller.C"<<std::endl;}
 histoFiller m;

 TChain *chainDataEle    = new TChain("electronEventTree/eventTree");
 TChain *chainDataMu     = new TChain("muonEventTree/eventTree");
 TChain *theChain        = new TChain("muEleEventTree/eventTree");
 TChain *theChainJESUp   = new TChain("muEleEventTreeJetUp/eventTree");
 TChain *theChainJESDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");
 TTree* tree;
 TString dirName;
 
 UInt_t lumi_mu  = 19778;
 UInt_t lumi_ele = 19757;

 // define the sample criteria by filling vectors
 std::vector<TString> Samples;
 std::vector<TString> MC;
 std::vector<TString> Shifts;
 Bool_t isMu_;
 Bool_t isMC_;
 UInt_t lumi;
 UInt_t nrEvents;
 Float_t crossSec;
 UInt_t counter = 0;
 Float_t nrLoops;
 MC.push_back("MC");
 //MC.push_back("Data"); // don't activate this, save data for another loop
 //Samples.push_back("Drell");
 //Samples.push_back("TTbar_full");
 Samples.push_back("TTbar_semi");
 //Samples.push_back("T_s");
 //Samples.push_back("T_t");
 //Samples.push_back("T_tW");
 //Samples.push_back("Tbar_s");
 //Samples.push_back("Tbar_t");
 //Samples.push_back("Tbar_tW");
 //Samples.push_back("WJets");
 //Samples.push_back("W1Jet");
 //Samples.push_back("W2Jet");
 //Samples.push_back("W3Jet");
 //Samples.push_back("W4Jet");
 //Samples.push_back("Wbb4F");
 //Samples.push_back("WW");
 //Samples.push_back("WZ");
 //Samples.push_back("ZZ"); 
 //Shifts.push_back("aucun");
 Shifts.push_back("SFs");
 Shifts.push_back("JESUp");
 Shifts.push_back("JESDown");
 Shifts.push_back("LESUp");
 Shifts.push_back("LESDown");
 nrLoops = MC.size() * Samples.size() *  Shifts.size() ;
 for (std::vector<TString>::iterator mc = MC.begin(); mc != MC.end(); ++mc){
  std::cout<<"xxxxxx Starting New Loop: MC.mc = "<<*mc<<" xxxxxx"<<std::endl;
  if(mc->EqualTo("MC")) {isMC_ = kTRUE;} 
  else if(mc->EqualTo("Data")) {isMC_ = kFALSE;} 
  else {std::cout<<*mc<<" is your value for 'mc'"<<std::endl; break;}

  for (std::vector<TString>::iterator sample = Samples.begin(); sample != Samples.end(); ++sample){
   std::cout<<" xxxxxx Starting New Loop: Samples.sample = "<<*sample<<" xxxxxx"<<std::endl;
   theChain->Reset();
   theChainJESUp   ->Reset();
   theChainJESDown ->Reset();
   theChainLESUp   ->Reset();
   theChainLESDown ->Reset();
   if(sample->EqualTo("TTbar_full")){
    nrEvents = 10429331;
    crossSec = 25.257; //240.6*0.324*0.324
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
    //theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
    //theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
    //theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
    //theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("TTbar_semi")){
    nrEvents = 23503785;
    crossSec = 105.394; //240.6*0.324*0.676*2
    //theChain        ->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/*.root");
    //theChainJESUp   ->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/*.root");
    //theChainJESDown ->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/*.root");
    //theChainLESUp   ->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/*.root");
    //theChainLESDown ->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/*.root");
    theChain->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
    //theChain->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-002D70FC-7F84-E211-A7E6-782BCB6E0938.root");
    //theChain->Add("/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-00*.root");
   }
   if(sample->EqualTo("T_s")){
    nrEvents = 259961;
    crossSec = 3.79;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("T_t")){
    nrEvents = 3915598;
    crossSec = 18.44; //56.4*0.327
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("T_tW")){
    nrEvents = 476173;
    crossSec = 11.1;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("Tbar_s")){
    nrEvents = 139974;
    crossSec = 1.76;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("Tbar_t")){
    nrEvents = 1711403;
    crossSec = 10.04;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("Tbar_tW")){
    nrEvents = 484502;
    crossSec = 11.1;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("W1Jet")){
    nrEvents = 1234567; // doesn't matter - hardcoded by jType
    crossSec = 36703.2;
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p1-MuEle-PATMC_V7A/*root");
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p2-MuEle-PATMC_V19/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p1-MuEle-PATMC_V7A/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p2-MuEle-PATMC_V19/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p1-MuEle-PATMC_V7A/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p2-MuEle-PATMC_V19/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p1-MuEle-PATMC_V7A/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p2-MuEle-PATMC_V19/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p1-MuEle-PATMC_V7A/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W1Jet_p2-MuEle-PATMC_V19/*root");
   }
   if(sample->EqualTo("W2Jet")){
    nrEvents = 1234567; // doesn't matter - hardcoded by jType
    crossSec = 36703.2;
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p1-MuEle-PATMC_V7A/*root");
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p2-MuEle-PATMC_V19/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p1-MuEle-PATMC_V7A/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p2-MuEle-PATMC_V19/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p1-MuEle-PATMC_V7A/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p2-MuEle-PATMC_V19/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p1-MuEle-PATMC_V7A/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p2-MuEle-PATMC_V19/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p1-MuEle-PATMC_V7A/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W2Jet_p2-MuEle-PATMC_V19/*root");
   }
   if(sample->EqualTo("W3Jet")){
    nrEvents = 1234567; // doesn't matter - hardcoded by jType
    crossSec = 36703.2;
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p1-MuEle-PATMC_V7A/*root");
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p2-MuEle-PATMC_V19/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p1-MuEle-PATMC_V7A/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p2-MuEle-PATMC_V19/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p1-MuEle-PATMC_V7A/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p2-MuEle-PATMC_V19/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p1-MuEle-PATMC_V7A/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p2-MuEle-PATMC_V19/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p1-MuEle-PATMC_V7A/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W3Jet_p2-MuEle-PATMC_V19/*root");
   }
   if(sample->EqualTo("W4Jet")){
    nrEvents = 1234567; // doesn't matter - hardcoded by jType
    crossSec = 36703.2;
    theChain->Add("/hdfs/store/user/tperry/NeuYear_W4Jet-MuEle-PATMC_V7A/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W4Jet-MuEle-PATMC_V7A/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_W4Jet-MuEle-PATMC_V7A/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_W4Jet-MuEle-PATMC_V7A/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_W4Jet-MuEle-PATMC_V7A/*root");
   }
   if(sample->EqualTo("WJets")){
    nrEvents = 1234567; // doesn't matter - hardcoded by jType
    crossSec = 36703.2;
    theChain->Add("/hdfs/store/user/tperry/NeuYear_WJets_p1-MuEle-PATMC_V7A/*root");
    theChain->Add("/hdfs/store/user/tperry/NeuYear_WJets_p2-MuEle-PATMC_V7A/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p1-MuEle-PATMC_V7A/*root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p2-MuEle-PATMC_V7A/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p1-MuEle-PATMC_V7A/*root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p2-MuEle-PATMC_V7A/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p1-MuEle-PATMC_V7A/*root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p2-MuEle-PATMC_V7A/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p1-MuEle-PATMC_V7A/*root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NeuYear_WJets_p2-MuEle-PATMC_V7A/*root");
   }
   if(sample->EqualTo("Wbb4F")){
    nrEvents = 20294311;
    crossSec = 138.9; //46.3*3
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("WW")){
    nrEvents = 10000431;
    crossSec = 56.75;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("WZ")){
    nrEvents = 9979363;
    crossSec = 33.21;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
   }
   if(sample->EqualTo("ZZ")){
    nrEvents = 9799908;
    crossSec = 8.26;
    theChain->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainJESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainJESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainLESUp   ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
    theChainLESDown ->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
   }

   for (std::vector<TString>::iterator shift = Shifts.begin(); shift != Shifts.end(); ++shift){
    std::cout<<"   xxxxxx Starting New Loop: Shifts.shift = "<<*shift<<" xxxxxx"<<std::endl;
    counter++;
    std::cout<<"   On Loop "<<counter<<" of "<< nrLoops<<std::endl;

    if(shift->EqualTo("JESUp"))        { m.Init(theChainJESUp, isMC_); }
    else if(shift->EqualTo("JESDown")) { m.Init(theChainJESDown, isMC_); }
    else if(shift->EqualTo("LESUp"))   { m.Init(theChainLESUp, isMC_); }
    else if(shift->EqualTo("LESDown")) { m.Init(theChainLESDown, isMC_); }
    else if(shift->EqualTo("SFs"))     { m.Init(theChain, isMC_); }
    else                               { m.Init(theChain, isMC_); }
    
    TString name = "NewHistofiller_"+*sample+"_"+*mc+"_"+*shift;
    std::cout<<"    "<<name<<std::endl;

    if(sample->EqualTo("WJets")
     || sample->EqualTo("W1Jet")
     || sample->EqualTo("W2Jet")
     || sample->EqualTo("W3Jet") 
     || sample->EqualTo("W4Jet") ){
     m.Loop("./plots/"+name, *shift, isMC_, kTRUE, lumi_mu, lumi_ele, nrEvents, crossSec);
    }
    else{ m.Loop("./plots/"+name, *shift, isMC_, kFALSE, lumi_mu, lumi_ele, nrEvents, crossSec); }
   }
  }
 }

 //std::vector<TString> EMu;
 //EMu.push_back("mu");
 //EMu.push_back("ele");
 //for (std::vector<TString>::iterator emu = EMu.begin(); emu != EMu.end(); ++emu){
 // std::cout<<"xxxxxx Starting New Data Loop: EMu.emu = "<<*emu<<" xxxxxx"<<std::endl;

 //   // Name and set isMU_, isMC_, 
 //   TString name = "ETrg_Data_"+*emu+"Data_aucun";
 //   isMC_ = kFALSE;
 //   std::cout<<name<<std::endl;

 //   //  initialize the correct chain
 //   if(emu->EqualTo("mu")){
 //    chainDataMu->Reset();
 //    chainDataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataA_8TeVMu-Mu-PATData/*root");
 //    chainDataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataB_8TeVMu-Mu-PATData/*root");
 //    chainDataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataC_8TeVMu-Mu-PATData/*root");
 //    chainDataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataD_8TeVMu-Mu-PATData/*root");
 //    m.Init(chainDataMu,isMC_); 
 //   }

 //   if(emu->EqualTo("ele")){
 //    chainDataEle->Reset();
 //    chainDataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataA_8TeVEle-Ele-PATData/*root");
 //    chainDataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataB_8TeVEle-Ele-PATData/*root");
 //    chainDataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataC_8TeVEle-Ele-PATData/*root");
 //    chainDataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataD_8TeVEle-Ele-PATData/*root");
 //    m.Init(chainDataEle,isMC_); 
 //   }

 //   m.Loop("../plots/"+name, "aucun", isMC_, kFALSE, 1, 1, 1, 1);
 //}
}
