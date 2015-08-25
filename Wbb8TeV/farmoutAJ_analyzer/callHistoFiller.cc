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

 //gROOT->ProcessLine(".L histoFillerDrell.C++", &error);
 //if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 //histoFillerDrell m;

 //gROOT->ProcessLine(".L histoFillerLLBF.C++", &error);
 //if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 //histoFillerLLBF m;

 //gROOT->ProcessLine(".L histoFillerTTbarProgression.C++", &error);
 //if(error!=0){std::cerr<<"ERROR LOADING histoFillerTTbarProgression.C"<<std::endl;}
 //histoFillerTTbarProgression m;

 gROOT->ProcessLine(".L histoFiller.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 histoFiller m;

 //TChain *theChain = new TChain("muonEventTree/eventTree");
 //TChain *theChain = new TChain("electronEventTree/eventTree");
 TChain *theChain     = new TChain("muEleEventTree/eventTree");

 TString path="./test/";

 TString shift="SFs";
 TString sample="Drell";
 Bool_t isMC_ = kFALSE ;
 Bool_t isW_ = kFALSE ;

 TString outfileName = path+"A_"+sample+"_"+shift+".root" ;
 TString infileName = "/hdfs/store/user/tperry/Interlochen/roots/ntuple/Interlochen_Drell-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.root";
 //TString infileName = "/hdfs/store/user/tperry/Interlochen/roots/ntuple/Interlochen_Tbar_s-MuEle-PATMCs/MuEle-PATMCs-*root";
 //TString infileName = "/hdfs/store/user/tperry/Interlochen/roots/ntuple/Interlochen_TTbar_full-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-000560C1-FD97-E211-9F33-00*root";
 //TString infileName = "/hdfs/store/user/tperry/Interlochen_TTbar_full-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-000560C1-FD97-E211-9F33-00304867924E.root";

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

  theChain->Add(infileName);
 
  m.Init(theChain, isMC_); 
    
  m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 

} // void callHistoFiller()

