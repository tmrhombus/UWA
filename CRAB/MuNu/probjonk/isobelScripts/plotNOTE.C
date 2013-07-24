//#include "MuNuPlot2BIG.C"
#include "MuNuPlot2.C"
//#include "MuNuPlotUnc.C"

void plotNOTE(){

  gROOT->SetBatch();

  TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt30>=2&&nElectrons==0&&MtCal>50";
  TString weight = "1.000";

  MuNuPlot2("nJetsPt30",false,true,"darin/nJets_log",6,2,8,1.2,finalcuts,"",weight,0.30,true);

/*    MuNuPlot2("highestJetEta",false,true,"darin/test4",100,-5,5,1.2,finalcuts,"",weight,0.30,false);
    MuNuPlot2("MtCal",false,true,"darin/test4/MtCal_2Jets",25,0,150,1.2,finalcuts,"",weight,0.30,false);
    MuNuPlot2("MtCal",false,true,"darin/test4/MtCal_2Jets_longrange",25,50,250,1.2,finalcuts+"&&MtCal>50","",weight,0.30,true);
    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_MTCal50_2Jets",25,25,125,1.2,finalcuts+"&&MtCal>50","",weight,0.30,false);
    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_MTCal50_2Jets_longrange",25,25,300,1.2,finalcuts+"&&MtCal>50","",weight,0.30,true);

    MuNuPlot2("Mt",false,true,"darin/test4/Mt_2Jets",25,0,150,1.2,finalcuts,"",weight,0.30,false);
    MuNuPlot2("Mt",false,true,"darin/test4/Mt_2Jets_longrange",25,50,250,1.2,finalcuts+"&&Mt>50","",weight,0.30,true);

    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_MT50_2Jets",25,25,125,1.2,finalcuts+"&&Mt>50","",weight,0.30,false);
    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_MT50_2Jets_longrange",25,25,300,1.2,finalcuts+"&&Mt>50","",weight,0.30,true);

    MuNuPlot2("MET",false,true,"darin/test4/Met_MT50_2Jets",25,50,250,1.2,finalcuts+"&&Mt>50","",weight,0.30,true);

*/

/*
  TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt30>=2&&nElectrons==0";
  TString weight = "1.000";
    MuNuPlot2("MtCal",false,true,"darin/test4/MtCal_2Jets",30,0,130,1.2,finalcuts,"",weight,0.30);
    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_2Jets",25,25,125,1.2,finalcuts,"",weight,0.30);
    MuNuPlot2("Mt",false,true,"darin/test4/Mt_2Jets",30,0,130,1.2,finalcuts,"",weight,0.30);
    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_MTCal50_2Jets",25,25,125,1.2,finalcuts+"&&MtCal>50","",weight,0.30);
    MuNuPlot2("muonPt",false,true,"darin/test4/muonPt_MT50_2Jets",25,25,125,1.2,finalcuts+"&&Mt>50","",weight,0.30);
    MuNuPlot2("MET",false,true,"darin/test4/Met_2Jets",30,0,130,1.2,finalcuts,"",weight,0.30);
    MuNuPlot2("MET",false,true,"darin/test4/Met_MT50_2Jets",30,0,130,1.2,finalcuts+"&&Mt>50","",weight,0.30);
*/
 
/*

  TString finalcuts= "muonPt>30&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<30&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.244&&J2CSVbtag>0.244)&&J1SVMassb>0&&J2SVMassb>0&&MtCal>60";
  TString weight = "EffweightCSVL2";
  /////Maria, I do the following: Create a folder in ~/www/ (this is specified in the MuNuPlot2 Macro)
  /////then create darin/test4, csvm2_2j, presel
  /////some cuts are predefined and always applied; see these in the macro! (there is one for QCD region and one for Data/MC, of course QCD has MuNuRelPFIso>0.2)
  /////T&P reweighting is put in automatically in the MuNuPlot2.C Macro.
  /////the command below goes as follows
  /////MuNuPlot2(variable,Log,Save,folder/filename,bins,Lower X axis value, Upper X axis Value, input cuts,words on plot on left, weight to multiply by)
  /////Note!!! For this set of root files the LHE value is multiplied by a factor (I made a math error in the weights....) it matches the W+jets MC to within ~ 3 % before b-tagging
  /////Also please uses EffweightCSVM2 NOT EffWEIGHTCSVM2 the ones with capitalized "weight" have an error

  MuNuPlot2("met",false,true,"darin/test4/met",15,60,160,1.2,finalcuts,"",weight);
  MuNuPlot2("highestJetPt",false,true,"darin/test4/highestJetPt",15,25,160,1.2,finalcuts,"",weight);
  MuNuPlot2("secondJetPt",false,true,"darin/test4/secondJetPt",15,25,100,1.2,finalcuts,"",weight);
  MuNuPlot2("highestJetEta",false,true,"darin/test4/highestJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlot2("secondJetEta",false,true,"darin/test4/secondJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlot2("highestJetPhi",false,true,"darin/test4/highestJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlot2("secondJetPhi",false,true,"darin/test4/secondJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlot2("J1SVMassb",false,true,"csvl2_2/J1SVMass",15,0,7,1.2,finalcuts,"",weight);
  MuNuPlot2("J2SVMassb",false,true,"csvl2_2/J2SVMass",15,0,7,1.2,finalcuts,"",weight);
  MuNuPlot2("J1SVMassb+J2SVMassb",false,true,"csvl2_2/AddSVMass",15,0,8,1.2,finalcuts,"",weight);
  MuNuPlot2("MtCal",false,true,"darin/test4/MtCal",15,60,160,1.2,finalcuts,"",weight);
  MuNuPlot2("muonPt",false,true,"darin/test4/muonPt",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlot2("mJJ",false,true,"darin/test4/mJJ",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlot2("WPt",false,true,"darin/test4/WPt",15,0,260,1.2,finalcuts,"",weight);
  MuNuPlot2("ht",false,true,"darin/test4/ht",15,75,460,1.2,finalcuts,"",weight);
  MuNuPlot2("ptJJ",false,true,"darin/test4/J2CSVbtag",20,0.244,1,1.2,finalcuts,"",weight);
  MuNuPlot2("vertices",false,true,"darin/test4/vertices",20,0.244,1,1.2,finalcuts,"",weight);
  MuNuPlot2("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"darin/test4/J1J2_DeltaR",20,0,3,1.2,finalcuts,"",weight);
  //MuNuPlot2("((J1SVphi-J2SVphi)^2+(J1SVeta-J2SVeta))^(1/2)",false,true,"darin/test4/SV_DeltaR",20,0,3,1.2,finalcuts,"",weight);

  /////preselection cuts
  TString Initialcuts= "muonPt>30&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&MtCal>60";
  TString noweight = "1";

  MuNuPlot2("met",false,true,"presel/met",15,60,160,1.2,Initialcuts,"",noweight);
  MuNuPlot2("highestJetPt",false,true,"presel/highestJetPt",15,25,160,1.2,Initialcuts,"",noweight);
  MuNuPlot2("secondJetPt",false,true,"presel/secondJetPt",15,25,100,1.2,Initialcuts,"",noweight);
  MuNuPlot2("highestJetEta",false,true,"presel/highestJetEta",15,-3,3,1.9,Initialcuts,"",noweight);
  MuNuPlot2("secondJetEta",false,true,"presel/secondJetEta",15,-3,3,1.9,Initialcuts,"",noweight);
  MuNuPlot2("highestJetPhi",false,true,"presel/highestJetPhi",15,-3.14,3.14,1.9,Initialcuts,"",noweight);
  MuNuPlot2("secondJetPhi",false,true,"presel/secondJetPhi",15,-3.14,3.14,1.9,Initialcuts,"",noweight);
  MuNuPlot2("J1SVMassb",false,true,"csvl2_2/J1SVMass",15,0,7,1.2,Initialcuts,"",noweight);
  MuNuPlot2("J2SVMassb",false,true,"csvl2_2/J2SVMass",15,0,7,1.2,Initialcuts,"",noweight);
  MuNuPlot2("J1SVMassb+J2SVMassb",false,true,"csvl2_2/AddSVMass",15,0,8,1.2,Initialcuts,"",noweight);
  MuNuPlot2("MtCal",false,true,"presel/MtCal",15,60,160,1.2,Initialcuts,"",noweight);
  MuNuPlot2("muonPt",false,true,"presel/muonPt",15,25,130,1.2,Initialcuts,"",noweight);
  MuNuPlot2("mJJ",false,true,"presel/mJJ",15,25,130,1.2,Initialcuts,"",noweight);
  MuNuPlot2("WPt",false,true,"presel/WPt",15,0,260,1.2,Initialcuts,"",noweight);
  MuNuPlot2("ht",false,true,"presel/ht",15,75,460,1.2,Initialcuts,"",noweight);
  MuNuPlot2("ptJJ",false,true,"presel/J2CSVbtag",20,0.244,1,1.2,Initialcuts,"",noweight);
  MuNuPlot2("vertices",false,true,"presel/vertices",20,0.244,1,1.2,Initialcuts,"",noweight);
  MuNuPlot2("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"presel/J1J2_DeltaR",20,0,3,1.2,Initialcuts,"",noweight);


*/
	
}

//  LocalWords:  gROOT
