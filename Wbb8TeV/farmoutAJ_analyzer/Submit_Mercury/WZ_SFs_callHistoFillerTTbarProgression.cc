/********************************
Instantiates histoFillerTTbarProgression.C with
the correct chain and naming
for a definable set of parameters

Usage: 
root -l -b
.L WZ_SFs_callHistoFillerTTbarProgression.cc
WZ_SFs_callHistoFillerTTbarProgression()

root -l -b -q WZ_SFs_callHistoFillerTTbarProgression.cc

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

void WZ_SFs_callHistoFillerTTbarProgression()
{
 int error = 0;
 //gROOT->ProcessLine(".L histoFiller.C++", &error);
 //if(error!=0){std::cerr<<"ERROR LOADING histoFiller.C"<<std::endl;}
 //histoFiller m;

 gROOT->ProcessLine(".L histoFillerTTbarProgression.C++", &error);
 if(error!=0){std::cerr<<"ERROR LOADING histoFillerTTbarProgression.C"<<std::endl;}
 histoFillerTTbarProgression m;

// TChain *chainDataEle    = new TChain("electronEventTree/eventTree");
// TChain *chainDataMu     = new TChain("muonEventTree/eventTree");
// TChain *theChain        = new TChain("muEleEventTree/eventTree");
// TChain *theChainJESUp   = new TChain("muEleEventTreeJetUp/eventTree");
// TChain *theChainJESDown = new TChain("muEleEventTreeJetDown/eventTree");
// TChain *theChainLESUp   = new TChain("muEleEventTreeMuonUp/eventTree");
// TChain *theChainLESDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TString outfileName = getenv("OUTPUT");
 TString inputListName = getenv("INPUT");

 TChain *theChain = new TChain("muEleEventTree/eventTree");

 // Define Sample Criteria
 UInt_t lumi_mu  = 19778 ;
 UInt_t lumi_ele = 19661 ;

 TString sample="WZ";
 UInt_t nrEvents = 9979363 ;
 Float_t crossSec = 33.6 ;

 Bool_t isMC_ = kTRUE ;
 Bool_t isW_ = kFALSE ;
 TString shift="SFs";

 std::cout<<"Sample = "<<sample<<std::endl; 
 std::cout<<"Shift = "<<shift<<std::endl; 

 std::cout << "Output File Name: " << outfileName << std::endl;

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
  std::cout << "Input File Name: "  << infileName <<  std::endl;
 
  theChain->Add( infileName );
 
  infileName_dump.push_back(infileName);
 } //while !inputList.eof()
 m.Init(theChain, isMC_); 
 m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 
} // void WZ_SFs_callHistoFillerTTbarProgression()


 //std::vector<TString> EMu;
 //EMu.push_back("mu");
 //EMu.push_back("ele");
 //for (std::vector<TString>::iterator emu = EMu.begin(); emu != EMu.end(); ++emu){
 // std::cout<<"xxxxxx Starting New Data Loop: EMu.emu = "<<emu<<" xxxxxx"<<std::endl;

 //   // Name and set isMU_, isMC_, 
 //   TString name = "ETrg_Data_"+emu+"Data_aucun";
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
