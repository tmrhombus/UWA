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

 TChain *theChain    = new TChain("muonEventTree/eventTree");
// TChain *theChain    = new TChain("electronEventTree/eventTree");
// TChain *theChain        = new TChain("muEleEventTree/eventTree");
// TChain *theChainJESUp   = new TChain("muEleEventTreeJetUp/eventTree");
// TChain *theChainJESDown = new TChain("muEleEventTreeJetDown/eventTree");
// TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
// TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TString shift="SFs";
 TString sample="DataMu";
// TString sample="DataEle";
// TString sample="TTbar_semi";
 Bool_t isMC_ = kFalse ;
 Bool_t isW_ = kFALSE ;

 TString outfileName = sample+"-70D48CDB-4C77-E211-9C19-90E6BA19A204.root" ;
 TString infileName = "/hdfs/store/user/tperry/VVCheckExtended_DataC_8TeVMu-mergeFilesJob/mergeFilesJob-Mu-PATData-patTuple_cfg-70D48CDB-4C77-E211-9C19-90E6BA19A204.root" ;

// TString outfileName = sample+"-B8FE9CBF-9B85-E211-AEF3-0025904B0FC0.root" ;
// TString infileName = "/hdfs/store/user/tperry/VVCheckExtended_DataC_8TeVEle-mergeFilesJob/mergeFilesJob-Ele-PATData-skimpattuple_cfg-patTuple_cfg-B8FE9CBF-9B85-E211-AEF3-0025904B0FC0.root" ;

// TString outfileName = sample+"-00277FF2-7B84-E211-9475-782BCB27B958.root" ;
// TString infileName = "/hdfs/store/user/tperry/VVCheckExtended_TTbar_semi-MuEle-PATMC_V7A/MuEle-PATMC_V7A-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root" ;

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

