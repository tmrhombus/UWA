/********************************
Instantiates histoFiller.C with
the correct chain and naming
for a definable set of parameters

Usage: 
root -l -b
.L Drell_SFs_callHistoFillerDrell.cc
Drell_SFs_callHistoFillerDrell()

root -l -b -q Drell_SFs_callHistoFillerDrell.cc

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

void Drell_SFs_callHistoFillerDrell()
{
 int error = 0;
 gROOT->ProcessLine(".L histoFillerDrell.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING histoFillerDrell.C"<<std::endl;}
 histoFillerDrell m;

// TChain *chainDataEle    = new TChain("electronEventTree/eventTree");
// TChain *chainDataMu     = new TChain("muonEventTree/eventTree");
// TChain *theChain        = new TChain("muEleEventTree/eventTree");
// TChain *theChainJESUp   = new TChain("muEleEventTreeJetUp/eventTree");
// TChain *theChainJESDown = new TChain("muEleEventTreeJetDown/eventTree");
// TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
// TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TString outfileName = "Drell_SFs_callHistoFillerDrell-mergeFilesJob-MuEle-PATMCs-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.root";
 TString inputListName = "Drell_list.inputs";
 //TString inputListName = "/nfs_scratch/tperry/Schweincomp_drell-Drell_SFs_callHistoFillerDrell/Drell_SFs_callHistoFillerDrell-mergeFilesJob-MuEle-PATMCs-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38/Drell_SFs_callHistoFillerDrell-mergeFilesJob-MuEle-PATMCs-patTuple_cfg-00037C53-AAD1-E111-B1BE-003048D45F38.inputs";

 TChain *theChain = new TChain("muEleEventTree/eventTree");

 // Define Sample Criteria
 UInt_t lumi_mu  = 19783 ;
 UInt_t lumi_ele = 19671 ;

 TString sample="Drell";
 UInt_t nrEvents = 29997285 ;
 Float_t crossSec = 3531.9 ;

 Bool_t isMC_ = kTRUE ;
 Bool_t isW_ = kFALSE ;
 TString shift="SFs";

 std::cout<<"Sample = "<<sample<<std::endl; 
 std::cout<<"Shift = "<<shift<<std::endl; 

 std::vector<TString> infileName_dump;
  
 ifstream inputList;
 inputList.open(inputListName);
 if( !inputList.good() ) { 
   std::cerr << "Cannot open the file: \"" << inputListName+"\""<<std::endl;
   abort();
 }

 // OK we have the file!
 TString infileName = ""; 
 while( !inputList.eof() ) { 
  infileName="";
  inputList >> infileName;
  
  std::cout << "Output File Name: " << outfileName << std::endl;
  std::cout << "Input File Name: "  << infileName <<  std::endl;
 
  theChain->Add( infileName );

  infileName_dump.push_back(infileName);
 } //while !inputList.eof()
 m.Init(theChain, isMC_); 
 m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 
} // void Drell_SFs_callHistoFillerDrell()

