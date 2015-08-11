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

 //TChain *theChain    = new TChain("muonEventTree/eventTree");
// TChain *theChain    = new TChain("electronEventTree/eventTree");
 //TChain *theChain        = new TChain("muEleEventTreeMuonDown/eventTree");
 //TChain *theChain        = new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *theChain        = new TChain("muEleEventTree/eventTree");

 TString path="./test/";

 TString shift="SFs";
 TString sample="Wbb4F";
 Bool_t isMC_ = kFALSE ;
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

  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-000A8A1E-C50D-E211-A5F4-001E67397E90.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00100304-E70E-E211-A4D5-001E67396793.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-001C0D8C-F40D-E211-9302-002590200814.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-001FB5DB-440E-E211-AB0A-001E67396DB5.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-002D5B5E-9B0D-E211-8210-001E67398E12.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00535982-B70D-E211-B084-001E67398B29.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-005E7CC0-310E-E211-86ED-002590200A7C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-007C916D-1F0E-E211-A431-0025B31E3C3C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-008CA080-290E-E211-97C0-F04DA23BBCCA.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0096580D-300E-E211-9125-003048D47A00.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00999F8E-F00E-E211-8FA6-001E67398CE1.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00C1C7A7-600D-E211-A24B-001E6739707B.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00D544B6-6F0E-E211-B6EB-001E6739830E.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-00E54084-590E-E211-B0A7-0025B31E3C3C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0224C09B-500D-E211-8F00-0025B3E05D74.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02359E2A-EF0E-E211-BB5E-002590200B50.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0237BD52-C50D-E211-BBAE-001E673986A6.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0237D065-940E-E211-ADD6-0025B31E3C0A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-023E47A0-A40E-E211-8261-001E67396BB7.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-024AD7EE-E10E-E211-86A0-002590200B6C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02525DFF-580D-E211-953E-00304867098C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-025820F2-FF0E-E211-B737-001E6739751C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02663807-D90E-E211-BB91-001E67397F35.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0285BCBC-E50D-E211-8584-001E673965FE.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-028BAB90-0E0D-E211-AD06-B499BAA2AC54.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02A8A650-350E-E211-984A-003048D4773A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02B37EB7-5A0D-E211-AB71-001E67397580.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02C9175E-9B0D-E211-8231-001E673973EB.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02D201CB-E50D-E211-9E02-001E67396581.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02DB3602-FC0E-E211-A770-001E673970FD.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-02F8E8FC-E60E-E211-957A-001E6739730A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-040DF9A5-F30E-E211-B74F-002590200A38.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04130B96-330D-E211-994F-0025B3E063CA.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0415ED59-940E-E211-814C-002590200824.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-041CBACD-A70D-E211-BE24-001E67396ACC.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-041F38D4-6F0E-E211-B678-003048D46296.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04347EF2-A00E-E211-B53D-0025902009C0.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-043FE2CF-C80D-E211-8A77-003048D45FD8.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0449F6D0-D50E-E211-BFAC-001E67398CAA.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0461CD95-810E-E211-953B-001E67397D5A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-046DF73F-C50D-E211-8679-002590200858.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04860F41-C50D-E211-A55B-001E67396928.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0490F206-120E-E211-84BC-001E67397454.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04945434-A70D-E211-8E13-001E6739732D.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-049C006C-5C0D-E211-9098-001E67397E13.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04AC2D4C-250E-E211-82B2-003048D45F94.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04B7CB07-F20E-E211-8168-002590200934.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04CAB018-A90D-E211-8616-001E67396653.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04E853AE-790E-E211-9F48-001E673970FD.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04ED3D7F-230E-E211-AEA4-003048D479DE.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-04FB7320-010F-E211-A260-001E6739677A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06069F0D-8C0E-E211-B7A8-002590200B34.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0615BA9D-550D-E211-B478-001E6739689C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06215901-650D-E211-B539-001E6739675C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-063DE65D-9B0D-E211-B274-001E6739834A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-066974F4-2A0F-E211-AD49-002590200908.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0685386E-130E-E211-81E4-001E673976ED.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-068F7101-B00E-E211-BBDB-001E6739689C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06A1CDBD-E50D-E211-9F33-003048D45F7A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06A45C97-880E-E211-B19A-0025902008C8.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06ACCCEE-C80D-E211-805A-003048D45F8A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06DF3FEE-B30E-E211-9D07-001E6739703A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06E8EDAE-330D-E211-94DA-001E67396ACC.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06E99E6B-560D-E211-9186-001E673973EB.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06EE4E7D-580D-E211-9772-001E67396E1E.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-06F98E28-8E0E-E211-BE7A-001E67396D10.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-081445BC-500D-E211-BD6D-002590200AD8.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-083E5813-CF0E-E211-94F2-002590200894.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08447936-270D-E211-B76D-001E67396E3C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-085AA41A-790E-E211-A94E-0025902008C4.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0862CB68-430D-E211-B664-001E67398CB9.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-086EEC9F-750D-E211-B3F1-001E6739702B.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-088B7187-590E-E211-83D2-001E67397238.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-088F0E71-6F0E-E211-AC33-001E67398D72.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-089E203B-C00E-E211-A745-003048D46006.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-089E9C5C-320E-E211-897E-003048670BE2.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08AD591A-BC0E-E211-992B-001E673972AB.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08BC93B8-D40E-E211-B6C4-001E6739677A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08CB53C4-8C0D-E211-8CE9-001E67398CA0.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08D140EC-520E-E211-BAF1-002590200B74.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08DD2AA1-B70D-E211-ABC6-001E67397396.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-08F3FF59-9B0D-E211-BDE7-001E67397620.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A0197EC-470E-E211-A0E4-0025B3E05CE4.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A02D220-740D-E211-94E3-002590200914.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A175DE3-C50D-E211-86C0-002590200938.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A18BB73-8A0E-E211-93F7-001E67397058.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A28950D-340E-E211-A9E4-0025902008F4.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A4A0CD2-850E-E211-BCB4-001E673975F8.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A5A19E2-9E0E-E211-8F41-0025B3E05D74.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A6C62D0-D80D-E211-B68A-001E673970FD.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A6CBB51-F40D-E211-8446-001E6739703A.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A919329-6F0E-E211-A5BC-003048D46062.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0A966213-7F0E-E211-8853-001E67397F26.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0AA3F181-5B0E-E211-8958-001E67396C9D.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0AB0D886-EE0E-E211-961E-003048673F2C.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0AB180AB-260E-E211-8F9C-002590200B68.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0AB1EE51-F40D-E211-9ED3-003048D47A54.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0AC55252-F40D-E211-8DC1-003048D47A7E.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0ADBBEAA-330D-E211-A6C1-001E6739801B.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0AFC6CB9-8C0D-E211-BCEF-001E67396761.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C00AD01-990E-E211-B1CE-003048D47A14.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C078508-E60D-E211-AEB6-001E673975F8.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C0D7AD5-C80D-E211-A7AE-003048D47A14.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C1C79D5-D80D-E211-9BF0-002590200850.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C34B81B-C20E-E211-AFAC-003048D46062.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C453A6D-420E-E211-9FCE-001E67398CA0.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C509016-790E-E211-9D9C-003048D47730.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C5F6E5C-0F0E-E211-9322-0025B3E05D26.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C6BDF94-3B0E-E211-8408-0025B3E063A8.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C74A142-F90E-E211-94CC-001E67397C33.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0C979321-A70D-E211-B400-001E67398011.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0CA311F2-1A0D-E211-83BD-001E67397431.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0CA6D9F2-520E-E211-9F0B-001E67398BE7.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0CD512C4-D80D-E211-BBE7-001E67397756.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0CD7E4C2-D80D-E211-8263-0025902009C0.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0CE8519A-330D-E211-8CCF-003048D479F0.root");
  theChain->Add("/hdfs/store/user/tperry/Interlochen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0CFD5684-E70E-E211-972F-0025902009B4.root");


 
  m.Init(theChain, isMC_); 
    
  m.Loop( outfileName, shift, isMC_, isW_, lumi_mu, lumi_ele, nrEvents, crossSec); 

} // void callHistoFiller()

