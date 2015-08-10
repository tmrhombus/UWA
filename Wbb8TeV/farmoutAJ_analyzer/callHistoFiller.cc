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

// gROOT->ProcessLine(".L histoFillerDrell.C++", &error);
// if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
// histoFillerDrell m;

 //gROOT->ProcessLine(".L histoFillerLLBF.C++", &error);
 //if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 //histoFillerLLBF m;

// gROOT->ProcessLine(".L histoFillerTTbarProgression.C++", &error);
// if(error!=0){std::cerr<<"ERROR LOADING histoFillerTTbarProgression.C"<<std::endl;}
// histoFillerTTbarProgression m;

 gROOT->ProcessLine(".L histoFiller.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 histoFiller m;

// TChain *theChain    = new TChain("muonEventTree/eventTree");
// TChain *theChain    = new TChain("electronEventTree/eventTree");
 TChain *theChain        = new TChain("muEleEventTreeMuonDown/eventTree");
 //TChain *theChain        = new TChain("muEleEventTreeMuonUp/eventTree");
 //TChain *theChain        = new TChain("muEleEventTree/eventTree");

 TString path="./test/";

 TString shift="LESDown";
 TString sample="Wbb4F";
 Bool_t isMC_ = kTRUE ;
 Bool_t isW_ = kFALSE ;

 TString outfileName = "A_"+sample+"_"+shift+".root" ;
 TString infileName = "/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-mergeFilesJob/mergeFilesJob-MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root";
 //TString infileName = "/hdfs/store/user/tperry/Schweincomp/Schweincomp_TTbar_semi-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02032E82-3C89-E211-9BF9-90B11C18BEEA.root" ;
 //TString infileName = "/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root" ;
 //TString infileName = "/hdfs/store/user/tperry/Schweincomp/Schweincomp_Drell-mergeFilesJob/mergeFilesJob-MuEle-PATMCs-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.root" ;

 //TString infileName = "/hdfs/store/user/tperry/Schweincomp/Schweincomp_Drell-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.root" ;
 //TString infileName = "/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root" ;
 //TString infileName = "/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Wbb4F_BastilleTest.root" ;

// TString outfileName = sample+"-002F5062-346F-E211-BF00-1CC1DE04DF20.root" ;
// TString infileName = "/hdfs/store/user/tperry/Dercury/Dercury_DataA_8TeVMu-mergeFilesJob/mergeFilesJob-Mu-PATData-patTuple_cfg-002F5062-346F-E211-BF00-1CC1DE04DF20.root" ;


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

  //theChain->Add( infileName );
  theChain->Add("/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-mergeFilesJob/mergeFilesJob-MuEle-PATMCs-patTuple_cfg-0*.root");
 
  m.Init(theChain, isMC_); 
    
  m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 

} // void callHistoFiller()

