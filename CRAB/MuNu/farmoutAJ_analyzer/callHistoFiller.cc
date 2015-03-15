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
 if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 histoFiller m;

// TChain *theChain    = new TChain("electronEventTree/eventTree");
// TChain *theChain    = new TChain("muonEventTree/eventTree");
 TChain *theChain        = new TChain("muEleEventTree/eventTree");
// TChain *theChainJESUp   = new TChain("muEleEventTreeJetUp/eventTree");
// TChain *theChainJESDown = new TChain("muEleEventTreeJetDown/eventTree");
// TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
// TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TString shift="SFs";
 TString sample="ZZ_Val_";
 Bool_t isMC_ = kTRUE ;
 Bool_t isW_ = kFALSE ;

 //TString outfileName = "Drell-00037C53-AAD1-E111-B1BE-003048D45F38.root";
 //TString infileName = "/hdfs/store/user/tperry/Valentine_Drell-mergeFilesJob/mergeFilesJob-MuEle-PATMC_V7A-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.root";

// TString outfileName = "DataAMu-A2392A15-916F-E211-B34F-00237DA14F86.root" ;
// TString infileName = "/hdfs/store/user/tperry/Valentine_DataA_8TeVMu-Mu-PATData/Mu-PATData-patTuple_cfg-A2392A15-916F-E211-B34F-00237DA14F86.root" ;

 //TString outfileName = "TTbar_full_0218ED41-F398-E211-837B-003048FFD752.root" ;
 //TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_full-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-0218ED41-F398-E211-837B-003048FFD752.root" ;
// TString outfileName = "TTbar_full_0227D9C2-5498-E211-815E-003048FFD756.root" ;
// TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_full-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-0227D9C2-5498-E211-815E-003048FFD756.root" ;
// TString outfileName = "TTbar_full_02CE8FD4-EA97-E211-9DD0-003048678FB8.root" ;
// TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_full-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-02CE8FD4-EA97-E211-9DD0-003048678FB8.root" ;
// TString outfileName = "TTbar_full_02EFC4C7-4698-E211-8EEE-003048678FA0.root" ;
// TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_full-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-02EFC4C7-4698-E211-8EEE-003048678FA0.root" ;
// TString outfileName = "TTbar_full_041812B4-F197-E211-9D31-00261894397E.root" ;
// TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_full-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-041812B4-F197-E211-9D31-00261894397E.root" ;

 //TString outfileName = sample+"_000560C1-FD97-E211-9F33-00304867924E.root" ;
 //TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_full-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-000560C1-FD97-E211-9F33-00304867924E.root" ;
 //TString outfileName = sample+"00277FF2-7B84-E211-9475-782BCB27B958.root" ;
 //TString infileName = "/hdfs/store/user/tperry/VVCheckExtended_TTbar_semi-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root" ;
 //TString infileName = "/hdfs/store/user/tperry/Valentine_TTbar_semi-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root" ;

 TString outfileName = sample+"0000CAC5-D4DA-E111-8872-00A0D1EEF328.root" ;
 TString infileName = "/hdfs/store/user/tperry/Valentine_ZZ-mergeFilesJob/mergeFilesJob-MuEle-PATMC_V7A-patTuple_cfg-0000CAC5-D4DA-E111-8872-00A0D1EEF328.root" ;

 // Define Sample Criteria
 UInt_t lumi_mu  = 19778 ;
 UInt_t lumi_ele = 19757 ;

 UInt_t nrEvents = 23492957 ;
 Float_t crossSec = 105.394 ;

 std::cout<<"Sample = "<<sample<<std::endl; 
 std::cout<<"Shift = "<<shift<<std::endl; 

  std::cout << "Output File Name: " << outfileName << std::endl;
  std::cout << "Input File Name: "  << infileName <<  std::endl;
 
  theChain->Reset();
  theChain->Add( infileName );
 
  m.Init(theChain, isMC_); 
    
  m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 

} // void callHistoFiller()

