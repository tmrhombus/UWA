/********************************
Instantiates histoFiller.C with
the correct chain and naming
for a definable set of parameters

Usage: 
root -l -b
.L call_X_class.cc
call_X_class()

root -l -b -q call_X_class.cc

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

void call_X_class()
{
 int error = 0;

 gROOT->ProcessLine(".L Q_class.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 Q_class m;

// TChain *theChain    = new TChain("muonEventTree/eventTree");
// TChain *theChain    = new TChain("electronEventTree/eventTree");
 TChain *theChain        = new TChain("muEleEventTree/eventTree");
// TChain *theChain   = new TChain("muEleEventTreeJetUp/eventTree");
// TChain *theChain = new TChain("muEleEventTreeJetDown/eventTree");
// TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
// TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");


TString outfileName = "W1Jet.root";
TString inputListName = "list_Q_Wbb4F_b.txt";
//TString inputListName = "list_W1Jet.txt";

// TString sample="Q_tt_semi_";
//
// TString infileName = "/hdfs/store/user/tperry/Qercury_TTbar_semi-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08F6FC91-AA84-E211-A2E6-001EC9AAA058.root";
// //TString infileName = "/hdfs/store/user/tperry/NouvelleYear/roots/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-08F6FC91-AA84-E211-A2E6-001EC9AAA058.root";
//
////  /hdfs/store/user/tperry/NouvelleYear/roots/NouvelleYear_DataB_8TeVEle-Ele-PATData/Ele-PATData-patTuple_cfg-001C002F-AA80-E211-AE67-003048F009D0.root
//
 
 std::vector<TString> infileName_dump;
  
 ifstream inputList;
 inputList.open(inputListName);
 if( !inputList.good() ) { 
   std::cerr << "Cannot open the file: \"" << inputListName+"\""<<std::endl;
   abort();
 }

 // OK we have the file!
 std::cout << "Output File Name: " << outfileName << std::endl;
 TString infileName = ""; 
 while( !inputList.eof() ) { 
  infileName="";
  inputList >> infileName;
  
  std::cout << "Input File Name: "  << infileName <<  std::endl;
 
  theChain->Add( infileName );

  infileName_dump.push_back(infileName);
 } //while !inputList.eof()
  m.Init(theChain); 
  m.Loop( ); 

} // void call_X_class()

