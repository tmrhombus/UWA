/********************************
Instantiates histoFiller.C with
the correct chain and naming
for a definable set of parameters

Usage: 
root -l -b
.L Wbb4F_LESDown_callHistoFillerDrell.cc
Wbb4F_LESDown_callHistoFillerDrell()

root -l -b -q Wbb4F_LESDown_callHistoFillerDrell.cc

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

void Wbb4F_LESDown_callHistoFillerDrell()
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

 TString outfileName = getenv("OUTPUT");
 TString inputListName = getenv("INPUT");

 TChain *theChain = new TChain("muEleEventTreeMuonDown/eventTree");

 // Define Sample Criteria
 UInt_t lumi_mu  = 19783 ;
 UInt_t lumi_ele = 19671 ;

 TString sample="Wbb4F";
 UInt_t nrEvents = 20294311 ;
 Float_t crossSec = 138.9 ;

 Bool_t isMC_ = kTRUE ;
 Bool_t isW_ = kFALSE ;
 TString shift="LESDown";

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
 std::cout<<" a"<<std::endl;
 m.Init(theChain, isMC_); 
 std::cout<<" b"<<std::endl;
 m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 
 std::cout<<" c"<<std::endl;
} // void Wbb4F_LESDown_callHistoFillerDrell()

