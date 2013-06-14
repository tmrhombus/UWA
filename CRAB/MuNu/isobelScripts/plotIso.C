//#include "MuNuPlotUncBIG.C"
#include "MuNuPlotUnc.C"
//#include "MuNuPlotUnc.C"

void plotIso(){

  gROOT->SetBatch();
  TString finalcuts= "muonPt>30&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.898&&J2CSVbtag>0.898)&&J1SVMassb>0&&J2SVMassb>0&&MtCal>50";
  TString weight = "EffweightCSVT2";
  /////Maria, I do the following: Create a folder in ~/www/ (this is specified in the MuNuPlotUnc Macro)
  /////then create test, csvm2_2j, presel
  /////some cuts are predefined and always applied; see these in the macro! (there is one for QCD region and one for Data/MC, of course QCD has MuNuRelPFIso>0.2)
  /////T&P reweighting is put in automatically in the MuNuPlotUnc.C Macro.
  /////the command below goes as follows
  /////MuNuPlotUnc(variable,Log,Save,folder/filename,bins,Lower X axis value, Upper X axis Value, input cuts,words on plot on left, weight to multiply by)
  /////Note!!! For this set of root files the LHE value is multiplied by a factor (I made a math error in the weights....) it matches the W+jets MC to within ~ 3 % before b-tagging
  /////Also please uses EffweightCSVM2 NOT EffWEIGHTCSVM2 the ones with capitalized "weight" have an error

  MuNuPlotUnc("highestJetPt",false,true,"test/highestJetPt",15,25,160,1.2,finalcuts,"",weight);

/*

  MuNuPlotUnc("met",false,true,"test/met",15,50,150,1.2,finalcuts,"",weight);
  MuNuPlotUnc("highestJetPt",false,true,"test/highestJetPt",15,25,160,1.2,finalcuts,"",weight);
  MuNuPlotUnc("secondJetPt",false,true,"test/secondJetPt",15,25,100,1.2,finalcuts,"",weight);
  MuNuPlotUnc("highestJetEta",false,true,"test/highestJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlotUnc("secondJetEta",false,true,"test/secondJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlotUnc("highestJetPhi",false,true,"test/highestJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlotUnc("secondJetPhi",false,true,"test/secondJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlotUnc("J1SVMassb",false,true,"csvl2_2/J1SVMass",15,0,7,1.2,finalcuts,"",weight);
  MuNuPlotUnc("J2SVMassb",false,true,"csvl2_2/J2SVMass",15,0,7,1.2,finalcuts,"",weight);
  MuNuPlotUnc("J1SVMassb+J2SVMassb",false,true,"csvl2_2/AddSVMass",15,0,8,1.2,finalcuts,"",weight);
  MuNuPlotUnc("MtCal",false,true,"test/MtCal",15,50,150,1.2,finalcuts,"",weight);
  MuNuPlotUnc("muonPt",false,true,"test/muonPt",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlotUnc("mJJ",false,true,"test/mJJ",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlotUnc("WPt",false,true,"test/WPt",15,0,250,1.2,finalcuts,"",weight);
  MuNuPlotUnc("ht",false,true,"test/ht",15,75,450,1.2,finalcuts,"",weight);
  MuNuPlotUnc("ptJJ",false,true,"test/J2CSVbtag",20,0.898,1,1.2,finalcuts,"",weight);
  MuNuPlotUnc("vertices",false,true,"test/vertices",20,0.898,1,1.2,finalcuts,"",weight);
  MuNuPlotUnc("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"test/J1J2_DeltaR",20,0,3,1.2,finalcuts,"",weight);
  //MuNuPlotUnc("((J1SVphi-J2SVphi)^2+(J1SVeta-J2SVeta))^(1/2)",false,true,"test/SV_DeltaR",20,0,3,1.2,finalcuts,"",weight);

  /////preselection cuts
  TString Initialcuts= "muonPt>30&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&MtCal>50";
  TString noweight = "1";

  MuNuPlotUnc("met",false,true,"presel/met",15,50,150,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("highestJetPt",false,true,"presel/highestJetPt",15,25,160,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("secondJetPt",false,true,"presel/secondJetPt",15,25,100,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("highestJetEta",false,true,"presel/highestJetEta",15,-3,3,1.9,Initialcuts,"",noweight);
  MuNuPlotUnc("secondJetEta",false,true,"presel/secondJetEta",15,-3,3,1.9,Initialcuts,"",noweight);
  MuNuPlotUnc("highestJetPhi",false,true,"presel/highestJetPhi",15,-3.14,3.14,1.9,Initialcuts,"",noweight);
  MuNuPlotUnc("secondJetPhi",false,true,"presel/secondJetPhi",15,-3.14,3.14,1.9,Initialcuts,"",noweight);
  MuNuPlotUnc("J1SVMassb",false,true,"csvl2_2/J1SVMass",15,0,7,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("J2SVMassb",false,true,"csvl2_2/J2SVMass",15,0,7,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("J1SVMassb+J2SVMassb",false,true,"csvl2_2/AddSVMass",15,0,8,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("MtCal",false,true,"presel/MtCal",15,50,150,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("muonPt",false,true,"presel/muonPt",15,25,130,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("mJJ",false,true,"presel/mJJ",15,25,130,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("WPt",false,true,"presel/WPt",15,0,250,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("ht",false,true,"presel/ht",15,75,450,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("ptJJ",false,true,"presel/J2CSVbtag",20,0.898,1,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("vertices",false,true,"presel/vertices",20,0.898,1,1.2,Initialcuts,"",noweight);
  MuNuPlotUnc("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"presel/J1J2_DeltaR",20,0,3,1.2,Initialcuts,"",noweight);


*/
	
}

//  LocalWords:  gROOT
