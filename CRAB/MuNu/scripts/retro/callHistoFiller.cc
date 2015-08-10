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

void callHistoFiller()
{
 int error = 0;
 gROOT->ProcessLine(".L histoFiller.C++", &error);
 if(error!=0){std::cout<<"ERROR LOADING histoFiller.C"<<std::endl;}
 histoFiller m;

 TChain *chain_DataMu = new TChain("muonEventTree/eventTree");
 TChain *chain_DataEle = new TChain("electronEventTree/eventTree");

 TChain *chain_TTbar_full =         new TChain("muEleEventTree/eventTree");
 TChain *chain_TTbar_full_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_TTbar_full_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_TTbar_full_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_TTbar_full_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_TTbar_semi =         new TChain("muEleEventTree/eventTree");
 TChain *chain_TTbar_semi_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_TTbar_semi_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_TTbar_semi_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_TTbar_semi_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");
 //chain_TTbar_semi->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
 //chain_TTbar_semi_JetUp->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
 //chain_TTbar_semi_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
 //chain_TTbar_semi_LepUp->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
 //chain_TTbar_semi_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root");
 //chain_TTbar_semi->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/MuEle-PATMC-patTuple_cfg-002D70FC-7F84-E211-A7E6-782BCB6E0938.root");

 TChain *chain_T_s =         new TChain("muEleEventTree/eventTree");
 TChain *chain_T_s_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_T_s_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_T_s_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_T_s_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_T_t =         new TChain("muEleEventTree/eventTree");
 TChain *chain_T_t_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_T_t_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_T_t_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_T_t_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");
 //chain_T_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");

 TChain *chain_T_tW =         new TChain("muEleEventTree/eventTree");
 TChain *chain_T_tW_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_T_tW_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_T_tW_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_T_tW_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_Tbar_s =         new TChain("muEleEventTree/eventTree");
 TChain *chain_Tbar_s_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_Tbar_s_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_Tbar_s_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_Tbar_s_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_Tbar_t =         new TChain("muEleEventTree/eventTree");
 TChain *chain_Tbar_t_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_Tbar_t_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_Tbar_t_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_Tbar_t_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_Tbar_tW =         new TChain("muEleEventTree/eventTree");
 TChain *chain_Tbar_tW_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_Tbar_tW_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_Tbar_tW_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_Tbar_tW_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_W1Jet =         new TChain("muEleEventTree/eventTree");
 TChain *chain_W1Jet_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_W1Jet_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_W1Jet_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_W1Jet_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_W2Jet =         new TChain("muEleEventTree/eventTree");
 TChain *chain_W2Jet_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_W2Jet_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_W2Jet_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_W2Jet_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_W3Jet =         new TChain("muEleEventTree/eventTree");
 TChain *chain_W3Jet_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_W3Jet_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_W3Jet_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_W3Jet_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_W4Jet =         new TChain("muEleEventTree/eventTree");
 TChain *chain_W4Jet_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_W4Jet_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_W4Jet_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_W4Jet_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_WJets =         new TChain("muEleEventTree/eventTree");
 TChain *chain_WJets_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_WJets_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_WJets_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_WJets_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_Wbb4F =         new TChain("muEleEventTree/eventTree");
 TChain *chain_Wbb4F_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_Wbb4F_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_Wbb4F_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_Wbb4F_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_WW =         new TChain("muEleEventTree/eventTree");
 TChain *chain_WW_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_WW_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_WW_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_WW_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_WZ =         new TChain("muEleEventTree/eventTree");
 TChain *chain_WZ_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_WZ_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_WZ_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_WZ_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 TChain *chain_ZZ =         new TChain("muEleEventTree/eventTree");
 TChain *chain_ZZ_JetUp =   new TChain("muEleEventTreeJetUp/eventTree");
 TChain *chain_ZZ_JetDown = new TChain("muEleEventTreeJetDown/eventTree");
 TChain *chain_ZZ_LepUp =   new TChain("muEleEventTreeMuonUp/eventTree");
 TChain *chain_ZZ_LepDown = new TChain("muEleEventTreeMuonDown/eventTree");

 // define the sample criteria by filling vectors
 std::vector<TString> Samples;
 std::vector<TString> EMu;
 std::vector<TString> MC;
 std::vector<TString> QCD;
 std::vector<TString> Cuts;
 std::vector<TString> Shifts;
 Bool_t isMu_;
 Bool_t isMC_;
 Bool_t isQCD_;
 Int_t jType;
 UInt_t lumi;
 UInt_t nrEvents;
 Float_t crossSec;
 Samples.push_back("TTbar_full");
 Samples.push_back("TTbar_semi");
 Samples.push_back("T_s");
 Samples.push_back("T_t");
 Samples.push_back("T_tW");
 Samples.push_back("Tbar_s");
 Samples.push_back("Tbar_t");
 Samples.push_back("Tbar_tW");
 Samples.push_back("WlN");
 Samples.push_back("Wl1");
 Samples.push_back("Wl2");
 Samples.push_back("Wl3");
 Samples.push_back("Wl4");
 Samples.push_back("WcN");
 Samples.push_back("Wc1");
 Samples.push_back("Wc2");
 Samples.push_back("Wc3");
 Samples.push_back("Wc4");
 Samples.push_back("WccN");
 Samples.push_back("Wcc1");
 Samples.push_back("Wcc2");
 Samples.push_back("Wcc3");
 Samples.push_back("Wcc4");
 Samples.push_back("WbbN");
 Samples.push_back("Wbb1");
 Samples.push_back("Wbb2");
 Samples.push_back("Wbb3");
 Samples.push_back("Wbb4");
 Samples.push_back("Wbb4F");
 Samples.push_back("WW");
 Samples.push_back("WZ");
 Samples.push_back("ZZ");// [32]
 EMu.push_back("ele");
 EMu.push_back("mu");
 MC.push_back("MC");
 //MC.push_back("Data"); // don't activate this, save data for another loop
 QCD.push_back("good");
 QCD.push_back("qcd");
 Cuts.push_back("wbb");
 Cuts.push_back("tt3j");
 Cuts.push_back("tt1m1e");
 Cuts.push_back("wjj");
 Cuts.push_back("stt");
 Cuts.push_back("dyjj");
 Cuts.push_back("dybb");
 Shifts.push_back("aucun");
 Shifts.push_back("SFs");
 Shifts.push_back("UESUp");
 Shifts.push_back("UESDown");
 Shifts.push_back("JetUp");
 Shifts.push_back("JetDown");
 Shifts.push_back("LepUp");
 Shifts.push_back("LepDown");
 for (std::vector<TString>::iterator mc = MC.begin(); mc != MC.end(); ++mc){
  std::cout<<"xxxxxx Starting New Loop: MC.mc = "<<*mc<<" xxxxxx"<<std::endl;
  for (std::vector<TString>::iterator cut = Cuts.begin(); cut != Cuts.end(); ++cut){
   std::cout<<"xxxxxx Starting New Loop: Cuts.cut = "<<*cut<<" xxxxxx"<<std::endl;
   for (std::vector<TString>::iterator qcd = QCD.begin(); qcd != QCD.end(); ++qcd){
    std::cout<<"xxxxxx Starting New Loop: QCD.qcd = "<<*qcd<<" xxxxxx"<<std::endl;
    for (std::vector<TString>::iterator sample = Samples.begin(); sample != Samples.end(); ++sample){
     std::cout<<"xxxxxx Starting New Loop: Samples.sample = "<<*sample<<" xxxxxx"<<std::endl;
     for (std::vector<TString>::iterator emu = EMu.begin(); emu != EMu.end(); ++emu){
      std::cout<<"xxxxxx Starting New Loop: EMu.emu = "<<*emu<<" xxxxxx"<<std::endl;
      for (std::vector<TString>::iterator shift = Shifts.begin(); shift != Shifts.end(); ++shift){
       std::cout<<"xxxxxx Starting New Loop: Shifts.shift = "<<*shift<<" xxxxxx"<<std::endl;
       //  std::vector<TString> Samples; sample
       //   {TTbar_full, TTbar_semi, 
       //    T_s, T_t, T_tW, 
       //    Tbar_s, Tbar_t, Tbar_tW, 
       //    WlN, Wl1, Wl2, Wl3, Wl4, 
       //    WcN, Wc1, Wc2, Wc3, Wc4, 
       //    WccN, Wcc1, Wcc2, Wcc3, Wcc4, 
       //    WbbN, Wbb1, Wbb2, Wbb3, Wbb4, 
       //    Wbb4F, WW, WZ, ZZ}
       //  std::vector<TString> EMu;     emu {ele, mu}
       //  std::vector<TString> MC;      mc  {MC, Data}
       //  std::vector<TString> QCD;     qcd {good, qcd}
       //  std::vector<TString> Cuts;    cut {wbb, tt3j, tt1m1e, wjj, stt, dyjj, dybb}
       //  std::vector<TString> Shifts;  shift 
       //   {aucun, SFs, UESUp, UESDown, JetUp, JetDown, LepUp, LepDown}

        // Name and set isMU_, isMC_, isQCD_ 
        TString name = *sample+"_"+*emu+*mc+*qcd+"_"+*cut+*shift;
        std::cout<<name<<std::endl;
        if(emu->EqualTo("ele")){isMu_ = kFALSE; lumi = 19757;}
        else if(emu->EqualTo("mu")) {isMu_ = kTRUE; lumi = 19778;}
        else {std::cout<<*emu<<" is your value for 'emu'"<<std::endl; break;}
        if(mc->EqualTo("MC")) {isMC_ = kTRUE;} 
        else if(mc->EqualTo("Data")) {isMC_ = kFALSE;} 
        else {std::cout<<*mc<<" is your value for 'mc'"<<std::endl; break;}
        if(qcd->EqualTo("good")) {isQCD_ = kFALSE;}
        else if(qcd->EqualTo("qcd")) {isQCD_ = kTRUE;}
        else {std::cout<<*qcd<<" is your value for 'qcd'"<<std::endl; break;}
        jType = 0; // for the timebeing, only change for WJets samples

        //  initialize the correct chain
        //   yes this is very long 
        if(sample->EqualTo("TTbar_full")){
         nrEvents = 10429331;
         crossSec = 25.257; //240.6*0.324*0.324
         if     (shift->EqualTo("UESUp"))   { 
          chain_TTbar_full->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_TTbar_full->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_TTbar_full_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_TTbar_full_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_TTbar_full_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_TTbar_full_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root"); 
          m.Init(chain_TTbar_full_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_TTbar_full->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full, isMC_);         }
         else                               {
          chain_TTbar_full->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_full-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_full, isMC_);         }
        }

        if(sample->EqualTo("TTbar_semi")){
         nrEvents = 23503785;
         crossSec = 105.394; //240.6*0.324*0.676*2
         if     (shift->EqualTo("UESUp"))   { 
          chain_TTbar_semi->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_TTbar_semi->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_TTbar_semi_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_TTbar_semi_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_TTbar_semi_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_TTbar_semi_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root"); 
          m.Init(chain_TTbar_semi_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_TTbar_semi->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi, isMC_);         }
         else                               {
          chain_TTbar_semi->Add        ("/hdfs/store/user/tperry/NouvelleYear_TTbar_semi-MuEle-PATMC/*.root");
          m.Init(chain_TTbar_semi, isMC_);         }
        }

        if(sample->EqualTo("T_s")){
         nrEvents = 259961;
         crossSec = 3.79;
         if     (shift->EqualTo("UESUp"))   { 
          chain_T_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_T_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_T_s_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_T_s_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_T_s_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_T_s_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root"); 
          m.Init(chain_T_s_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_T_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s, isMC_);         }
         else                               {
          chain_T_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_s-MuEle-PATMC/*.root");
          m.Init(chain_T_s, isMC_);         }
        }

        if(sample->EqualTo("T_t", isMC_)){
         nrEvents = 3915598;
         crossSec = 18.44; //56.4*0.327
         if     (shift->EqualTo("UESUp"))   { 
          chain_T_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_T_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_T_t_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_T_t_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_T_t_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_T_t_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root"); 
          m.Init(chain_T_t_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_T_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t, isMC_);         }
         else                               {
          chain_T_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_t-MuEle-PATMC/*.root");
          m.Init(chain_T_t, isMC_);         }
        }

        if(sample->EqualTo("T_tW")){
         nrEvents = 476173;
         crossSec = 11.1;
         if     (shift->EqualTo("UESUp"))   { 
          chain_T_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_T_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_T_tW_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_T_tW_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_T_tW_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_T_tW_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root"); 
          m.Init(chain_T_tW_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_T_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW, isMC_);         }
         else                               {
          chain_T_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_T_tW-MuEle-PATMC/*.root");
          m.Init(chain_T_tW, isMC_);         }
        }

        if(sample->EqualTo("Tbar_s")){
         nrEvents = 139974;
         crossSec = 1.76;
         if     (shift->EqualTo("UESUp"))   { 
          chain_Tbar_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_Tbar_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_Tbar_s_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_Tbar_s_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_Tbar_s_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_Tbar_s_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root"); 
          m.Init(chain_Tbar_s_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_Tbar_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s, isMC_);         }
         else                               {
          chain_Tbar_s->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_s-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_s, isMC_);         }
        }

        if(sample->EqualTo("Tbar_t")){
         nrEvents = 1711403;
         crossSec = 10.04;
         if     (shift->EqualTo("UESUp"))   { 
          chain_Tbar_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_Tbar_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_Tbar_t_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_Tbar_t_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_Tbar_t_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_Tbar_t_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root"); 
          m.Init(chain_Tbar_t_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_Tbar_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t, isMC_);         }
         else                               {
          chain_Tbar_t->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_t-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_t, isMC_);         }
        }

        if(sample->EqualTo("Tbar_tW")){
         nrEvents = 484502;
         crossSec = 11.1;
         if     (shift->EqualTo("UESUp"))   { 
          chain_Tbar_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_Tbar_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_Tbar_tW_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_Tbar_tW_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_Tbar_tW_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_Tbar_tW_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root"); 
          m.Init(chain_Tbar_tW_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_Tbar_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW, isMC_);         }
         else                               {
          chain_Tbar_tW->Add        ("/hdfs/store/user/tperry/NouvelleYear_Tbar_tW-MuEle-PATMC/*.root");
          m.Init(chain_Tbar_tW, isMC_);         }
        }

        if(sample->EqualTo("Wl1") || sample->EqualTo("Wc1") || sample->EqualTo("Wcc1") || sample->EqualTo("Wbb1") ){
         nrEvents = 1234567; // doesn't matter - hardcoded by jType
         crossSec = 36703.2;
         if     (sample->EqualTo("Wl1")){ jType=1; } 
         else if(sample->EqualTo("Wc1")){ jType=2; } 
         else if(sample->EqualTo("Wcc1")){ jType=3; } 
         else if(sample->EqualTo("Wbb1")){ jType=4; } 
         if     (shift->EqualTo("UESUp"))   { 
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_W1Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_W1Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_W1Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_W1Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root"); 
          chain_W1Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root"); 
          m.Init(chain_W1Jet_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet, isMC_);         }
         else                               {
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p1-MuEle-PATMC/*.root");
          chain_W1Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W1Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W1Jet, isMC_);         }
        }

        if(sample->EqualTo("Wl2") || sample->EqualTo("Wc2") || sample->EqualTo("Wcc2") || sample->EqualTo("Wbb2") ){
         nrEvents = 1234567; // doesn't matter - hardcoded by jType
         crossSec = 36703.2;
         if     (sample->EqualTo("Wl2")){ jType=1; } 
         else if(sample->EqualTo("Wc2")){ jType=2; } 
         else if(sample->EqualTo("Wcc2")){ jType=3; } 
         else if(sample->EqualTo("Wbb2")){ jType=4; } 
         if     (shift->EqualTo("UESUp"))   { 
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_W2Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_W2Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_W2Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_W2Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root"); 
          chain_W2Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root"); 
          m.Init(chain_W2Jet_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet, isMC_);         }
         else                               {
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p1-MuEle-PATMC/*.root");
          chain_W2Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W2Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W2Jet, isMC_);         }
        }

        if(sample->EqualTo("Wl3") || sample->EqualTo("Wc3") || sample->EqualTo("Wcc3") || sample->EqualTo("Wbb3") ){
         nrEvents = 1234567; // doesn't matter - hardcoded by jType
         crossSec = 36703.2;
         if     (sample->EqualTo("Wl3")){ jType=1; } 
         else if(sample->EqualTo("Wc3")){ jType=2; } 
         else if(sample->EqualTo("Wcc3")){ jType=3; } 
         else if(sample->EqualTo("Wbb3")){ jType=4; } 
         if     (shift->EqualTo("UESUp"))   { 
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_W3Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_W3Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_W3Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_W3Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root"); 
          chain_W3Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root"); 
          m.Init(chain_W3Jet_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet, isMC_);         }
         else                               {
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p1-MuEle-PATMC/*.root");
          chain_W3Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W3Jet_p2-MuEle-PATMC/*.root");
          m.Init(chain_W3Jet, isMC_);         }
        }

        if(sample->EqualTo("Wl4") || sample->EqualTo("Wc4") || sample->EqualTo("Wcc4") || sample->EqualTo("Wbb4") ){
         nrEvents = 1234567; // doesn't matter - hardcoded by jType
         crossSec = 36703.2;
         if     (sample->EqualTo("Wl4")){ jType=1; } 
         else if(sample->EqualTo("Wc4")){ jType=2; } 
         else if(sample->EqualTo("Wcc4")){ jType=3; } 
         else if(sample->EqualTo("Wbb4")){ jType=4; } 
         if     (shift->EqualTo("UESUp"))   { 
          chain_W4Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_W4Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_W4Jet_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_W4Jet_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_W4Jet_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_W4Jet_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root"); 
          m.Init(chain_W4Jet_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_W4Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet, isMC_);         }
         else                               {
          chain_W4Jet->Add        ("/hdfs/store/user/tperry/NouvelleYear_W4Jet-MuEle-PATMC/*.root");
          m.Init(chain_W4Jet, isMC_);         }
        }

        if(sample->EqualTo("WlN") || sample->EqualTo("WcN") || sample->EqualTo("WccN") || sample->EqualTo("WbbN") ){
         nrEvents = 1234567; // doesn't matter - hardcoded by jType
         crossSec = 36703.2;
         if     (sample->EqualTo("WlN")){ jType=1; } 
         else if(sample->EqualTo("WcN")){ jType=2; } 
         else if(sample->EqualTo("WccN")){ jType=3; } 
         else if(sample->EqualTo("WbbN")){ jType=4; } 
         if     (shift->EqualTo("UESUp"))   { 
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_WJets_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_WJets_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_WJets_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_WJets_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root"); 
          chain_WJets_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root"); 
          m.Init(chain_WJets_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets, isMC_);         }
         else                               {
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p1-MuEle-PATMC/*.root");
          chain_WJets->Add        ("/hdfs/store/user/tperry/NouvelleYear_WJets_p2-MuEle-PATMC/*.root");
          m.Init(chain_WJets, isMC_);         }
        }

        if(sample->EqualTo("Wbb4F")){
         nrEvents = 20294311;
         crossSec = 138.9; //46.3*3
         if     (shift->EqualTo("UESUp"))   { 
          chain_Wbb4F->Add        ("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_Wbb4F->Add        ("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_Wbb4F_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_Wbb4F_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_Wbb4F_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_Wbb4F_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root"); 
          m.Init(chain_Wbb4F_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_Wbb4F->Add        ("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F, isMC_);         }
         else                               {
          chain_Wbb4F->Add        ("/hdfs/store/user/tperry/NouvelleYear_Wbb4F-MuEle-PATMC/*.root");
          m.Init(chain_Wbb4F, isMC_);         }
        }

        if(sample->EqualTo("WW")){
         nrEvents = 10000431;
         crossSec = 56.75;
         if     (shift->EqualTo("UESUp"))   { 
          chain_WW->Add        ("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_WW->Add        ("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_WW_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_WW_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_WW_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_WW_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root"); 
          m.Init(chain_WW_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_WW->Add        ("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW, isMC_);         }
         else                               {
          chain_WW->Add        ("/hdfs/store/user/tperry/NouvelleYear_WW-MuEle-PATMC/*.root");
          m.Init(chain_WW, isMC_);         }
        }

        if(sample->EqualTo("WZ")){
         nrEvents = 9979363;
         crossSec = 33.21;
         if     (shift->EqualTo("UESUp"))   { 
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_WZ_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_WZ_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_WZ_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_WZ_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root"); 
          m.Init(chain_WZ_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
         else                               {
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
        }

        if(sample->EqualTo("ZZ")){
         nrEvents = 9799908;
         crossSec = 8.26;
         if     (shift->EqualTo("UESUp"))   { 
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
         else if(shift->EqualTo("UESDown")) {
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
         else if(shift->EqualTo("JetUp"))   {
          chain_WZ_JetUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ_JetUp, isMC_);   }
         else if(shift->EqualTo("JetDown")) {
          chain_WZ_JetDown->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ_JetDown, isMC_); }
         else if(shift->EqualTo("LepUp"))   {
          chain_WZ_LepUp->Add  ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ_LepUp, isMC_);   }
         else if(shift->EqualTo("LepDown")) {
          chain_WZ_LepDown->Add("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root"); 
          m.Init(chain_WZ_LepDown, isMC_); }
         else if(shift->EqualTo("SFs"))     {
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
         else                               {
          chain_WZ->Add        ("/hdfs/store/user/tperry/NouvelleYear_WZ-MuEle-PATMC/*.root");
          m.Init(chain_WZ, isMC_);         }
        }

        m.Loop("../plots/"+name, isMu_, isMC_, isQCD_, *cut, *shift, jType, lumi, nrEvents, crossSec);

        chain_TTbar_full->Reset();
        chain_TTbar_full_JetUp->Reset(); 
        chain_TTbar_full_JetDown->Reset(); 
        chain_TTbar_full_LepUp->Reset(); 
        chain_TTbar_full_LepDown->Reset(); 

        chain_TTbar_semi->Reset();           
        chain_TTbar_semi_JetUp->Reset();     
        chain_TTbar_semi_JetDown->Reset();   
        chain_TTbar_semi_LepUp->Reset();     
        chain_TTbar_semi_LepDown->Reset();   

        chain_T_s->Reset();
        chain_T_s_JetUp->Reset(); 
        chain_T_s_JetDown->Reset(); 
        chain_T_s_LepUp->Reset(); 
        chain_T_s_LepDown->Reset(); 

        chain_T_t->Reset();
        chain_T_t_JetUp->Reset(); 
        chain_T_t_JetDown->Reset(); 
        chain_T_t_LepUp->Reset(); 
        chain_T_t_LepDown->Reset(); 

        chain_T_tW->Reset();
        chain_T_tW_JetUp->Reset(); 
        chain_T_tW_JetDown->Reset(); 
        chain_T_tW_LepUp->Reset(); 
        chain_T_tW_LepDown->Reset(); 

        chain_Tbar_s->Reset();
        chain_Tbar_s_JetUp->Reset(); 
        chain_Tbar_s_JetDown->Reset(); 
        chain_Tbar_s_LepUp->Reset(); 
        chain_Tbar_s_LepDown->Reset(); 

        chain_Tbar_t->Reset();
        chain_Tbar_t_JetUp->Reset(); 
        chain_Tbar_t_JetDown->Reset(); 
        chain_Tbar_t_LepUp->Reset(); 
        chain_Tbar_t_LepDown->Reset(); 

        chain_Tbar_tW->Reset();
        chain_Tbar_tW_JetUp->Reset(); 
        chain_Tbar_tW_JetDown->Reset(); 
        chain_Tbar_tW_LepUp->Reset(); 
        chain_Tbar_tW_LepDown->Reset(); 

        chain_W1Jet->Reset();
        chain_W1Jet_JetUp->Reset(); 
        chain_W1Jet_JetDown->Reset(); 
        chain_W1Jet_LepUp->Reset(); 
        chain_W1Jet_LepDown->Reset(); 

        chain_W2Jet->Reset();
        chain_W2Jet_JetUp->Reset(); 
        chain_W2Jet_JetDown->Reset(); 
        chain_W2Jet_LepUp->Reset(); 
        chain_W2Jet_LepDown->Reset(); 

        chain_W3Jet->Reset();
        chain_W3Jet_JetUp->Reset(); 
        chain_W3Jet_JetDown->Reset(); 
        chain_W3Jet_LepUp->Reset(); 
        chain_W3Jet_LepDown->Reset(); 

        chain_W4Jet->Reset();
        chain_W4Jet_JetUp->Reset(); 
        chain_W4Jet_JetDown->Reset(); 
        chain_W4Jet_LepUp->Reset(); 
        chain_W4Jet_LepDown->Reset(); 

        chain_WJets->Reset();
        chain_WJets_JetUp->Reset(); 
        chain_WJets_JetDown->Reset(); 
        chain_WJets_LepUp->Reset(); 
        chain_WJets_LepDown->Reset(); 

        chain_Wbb4F->Reset();
        chain_Wbb4F_JetUp->Reset(); 
        chain_Wbb4F_JetDown->Reset(); 
        chain_Wbb4F_LepUp->Reset(); 
        chain_Wbb4F_LepDown->Reset(); 

        chain_WW->Reset();
        chain_WW_JetUp->Reset(); 
        chain_WW_JetDown->Reset(); 
        chain_WW_LepUp->Reset(); 
        chain_WW_LepDown->Reset(); 

        chain_WZ->Reset();
        chain_WZ_JetUp->Reset(); 
        chain_WZ_JetDown->Reset(); 
        chain_WZ_LepUp->Reset(); 
        chain_WZ_LepDown->Reset(); 

        chain_ZZ->Reset();
        chain_ZZ_JetUp->Reset(); 
        chain_ZZ_JetDown->Reset(); 
        chain_ZZ_LepUp->Reset(); 
        chain_ZZ_LepDown->Reset(); 

      }
     }
    }
   }
  }
 }

 Samples.clear();
 Samples.push_back("Data");// [32]
 MC.clear();
 MC.push_back("Data");
 Shifts.clear();
 Shifts.push_back("aucun");
 for (std::vector<TString>::iterator mc = MC.begin(); mc != MC.end(); ++mc){
  std::cout<<"xxxxxx Starting New Loop: MC.mc = "<<*mc<<" xxxxxx"<<std::endl;
  for (std::vector<TString>::iterator cut = Cuts.begin(); cut != Cuts.end(); ++cut){
   std::cout<<"xxxxxx Starting New Loop: Cuts.cut = "<<*cut<<" xxxxxx"<<std::endl;
   for (std::vector<TString>::iterator qcd = QCD.begin(); qcd != QCD.end(); ++qcd){
    std::cout<<"xxxxxx Starting New Loop: QCD.qcd = "<<*qcd<<" xxxxxx"<<std::endl;
    for (std::vector<TString>::iterator sample = Samples.begin(); sample != Samples.end(); ++sample){
     std::cout<<"xxxxxx Starting New Loop: Samples.sample = "<<*sample<<" xxxxxx"<<std::endl;
     for (std::vector<TString>::iterator emu = EMu.begin(); emu != EMu.end(); ++emu){
      std::cout<<"xxxxxx Starting New Loop: EMu.emu = "<<*emu<<" xxxxxx"<<std::endl;
      for (std::vector<TString>::iterator shift = Shifts.begin(); shift != Shifts.end(); ++shift){
       std::cout<<"xxxxxx Starting New Loop: Shifts.shift = "<<*shift<<" xxxxxx"<<std::endl;

        // Name and set isMU_, isMC_, isQCD_ 
        TString name = *sample+"_"+*emu+*mc+*qcd+"_"+*cut+*shift;
        std::cout<<name<<std::endl;
        if(emu->EqualTo("ele")){isMu_ = kFALSE; lumi = 19757;}
        else if(emu->EqualTo("mu")) {isMu_ = kTRUE; lumi = 19778;}
        else {std::cout<<*emu<<" is your value for 'emu'"<<std::endl; break;}
        if(mc->EqualTo("MC")) {isMC_ = kTRUE;} 
        else if(mc->EqualTo("Data")) {isMC_ = kFALSE;} 
        else {std::cout<<*mc<<" is your value for 'mc'"<<std::endl; break;}
        if(qcd->EqualTo("good")) {isQCD_ = kFALSE;}
        else if(qcd->EqualTo("qcd")) {isQCD_ = kTRUE;}
        else {std::cout<<*qcd<<" is your value for 'qcd'"<<std::endl; break;}
        jType = 0; // for the timebeing, only change for WJets samples

        //  initialize the correct chain
        if(emu->EqualTo("mu")){
         nrEvents = 1;
         crossSec = 1;
         chain_DataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataA_8TeVMu-Mu-PATData/*root");
         chain_DataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataB_8TeVMu-Mu-PATData/*root");
         chain_DataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataC_8TeVMu-Mu-PATData/*root");
         chain_DataMu->Add("/hdfs/store/user/tperry/NouvelleYear_DataD_8TeVMu-Mu-PATData/*root");
         m.Init(chain_DataMu,isMC_); 
        }

        if(emu->EqualTo("ele")){
         nrEvents = 1;
         crossSec = 1;
         chain_DataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataA_8TeVEle-Ele-PATData/*root");
         chain_DataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataB_8TeVEle-Ele-PATData/*root");
         chain_DataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataC_8TeVEle-Ele-PATData/*root");
         chain_DataEle->Add("/hdfs/store/user/tperry/NouvelleYear_DataD_8TeVEle-Ele-PATData/*root");
         m.Init(chain_DataEle,isMC_); 
        }

        m.Loop("../plots/"+name, isMu_, isMC_, isQCD_, *cut, *shift, jType, lumi, nrEvents, crossSec);

        chain_DataEle->Reset();
        chain_DataMu->Reset();
      }
     }
    }
   }
  }
 }
}
