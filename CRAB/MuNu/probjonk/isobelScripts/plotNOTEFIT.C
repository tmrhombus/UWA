//#include "MuNuPlotFITBIG.C"
#include "MuNuPlotFIT.C"
//#include "MuNuPlotUnc.C"

void plotNOTEFIT(){

  gROOT->SetBatch();

  TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt30==2&&nJets24Pt30==0&&nElectrons==0";
  TString weight = "1.000";
    MuNuPlotFIT("MtCal",false,true,"test2/MtCal_2Jets",25,0,150,1.2,finalcuts,"",weight,0.45,false);
    MuNuPlotFIT("MtCal",false,true,"test2/MtCal_2Jets_longrange",25,50,250,1.2,finalcuts+"&&MtCal>50","",weight,0.45,true);
    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_MTCal50_2Jets",25,25,125,1.2,finalcuts+"&&MtCal>50","",weight,0.45,false);
    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_MTCal50_2Jets_longrange",25,25,300,1.2,finalcuts+"&&MtCal>50","",weight,0.45,true);

    MuNuPlotFIT("Mt",false,true,"test2/Mt_2Jets",25,0,150,1.2,finalcuts,"",weight,0.45,false);
    MuNuPlotFIT("Mt",false,true,"test2/Mt_2Jets_longrange",25,50,250,1.2,finalcuts+"&&Mt>50","",weight,0.45,true);

    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_MT50_2Jets",25,25,125,1.2,finalcuts+"&&Mt>50","",weight,0.45,false);
    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_MT50_2Jets_longrange",25,25,300,1.2,finalcuts+"&&Mt>50","",weight,0.45,true);

    MuNuPlotFIT("MET",false,true,"test2/Met_MT50_2Jets",25,50,250,1.2,finalcuts+"&&Mt>50","",weight,0.45,true);

/*
  TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt30>=2&&nElectrons==0";
  TString weight = "1.000";
    MuNuPlotFIT("MtCal",false,true,"test2/MtCal_2Jets",30,0,145,1.2,finalcuts,"",weight,0.45);
    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_2Jets",25,25,125,1.2,finalcuts,"",weight,0.45);
    MuNuPlotFIT("Mt",false,true,"test2/Mt_2Jets",30,0,145,1.2,finalcuts,"",weight,0.45);
    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_MTCal50_2Jets",25,25,125,1.2,finalcuts+"&&MtCal>50","",weight,0.45);
    MuNuPlotFIT("muonPt",false,true,"test2/muonPt_MT50_2Jets",25,25,125,1.2,finalcuts+"&&Mt>50","",weight,0.45);
    MuNuPlotFIT("MET",false,true,"test2/Met_2Jets",30,0,145,1.2,finalcuts,"",weight,0.45);
    MuNuPlotFIT("MET",false,true,"test2/Met_MT50_2Jets",30,0,145,1.2,finalcuts+"&&Mt>50","",weight,0.45);
*/
 
/*

  TString finalcuts= "muonPt>30&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<45&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.244&&J2CSVbtag>0.244)&&J1SVMassb>0&&J2SVMassb>0&&MtCal>60";
  TString weight = "EffweightCSVL2";
  /////Maria, I do the following: Create a folder in ~/www/ (this is specified in the MuNuPlotFIT Macro)
  /////then create test2, csvm2_2j, presel
  /////some cuts are predefined and always applied; see these in the macro! (there is one for QCD region and one for Data/MC, of course QCD has MuNuRelPFIso>0.2)
  /////T&P reweighting is put in automatically in the MuNuPlotFIT.C Macro.
  /////the command below goes as follows
  /////MuNuPlotFIT(variable,Log,Save,folder/filename,bins,Lower X axis value, Upper X axis Value, input cuts,words on plot on left, weight to multiply by)
  /////Note!!! For this set of root files the LHE value is multiplied by a factor (I made a math error in the weights....) it matches the W+jets MC to within ~ 3 % before b-tagging
  /////Also please uses EffweightCSVM2 NOT EffWEIGHTCSVM2 the ones with capitalized "weight" have an error

  MuNuPlotFIT("met",false,true,"test2/met",15,60,160,1.2,finalcuts,"",weight);
  MuNuPlotFIT("highestJetPt",false,true,"test2/highestJetPt",15,25,160,1.2,finalcuts,"",weight);
  MuNuPlotFIT("secondJetPt",false,true,"test2/secondJetPt",15,25,100,1.2,finalcuts,"",weight);
  MuNuPlotFIT("highestJetEta",false,true,"test2/highestJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlotFIT("secondJetEta",false,true,"test2/secondJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlotFIT("highestJetPhi",false,true,"test2/highestJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlotFIT("secondJetPhi",false,true,"test2/secondJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlotFIT("J1SVMassb",false,true,"csvl2_2/J1SVMass",15,0,7,1.2,finalcuts,"",weight);
  MuNuPlotFIT("J2SVMassb",false,true,"csvl2_2/J2SVMass",15,0,7,1.2,finalcuts,"",weight);
  MuNuPlotFIT("J1SVMassb+J2SVMassb",false,true,"csvl2_2/AddSVMass",15,0,8,1.2,finalcuts,"",weight);
  MuNuPlotFIT("MtCal",false,true,"test2/MtCal",15,60,160,1.2,finalcuts,"",weight);
  MuNuPlotFIT("muonPt",false,true,"test2/muonPt",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlotFIT("mJJ",false,true,"test2/mJJ",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlotFIT("WPt",false,true,"test2/WPt",15,0,260,1.2,finalcuts,"",weight);
  MuNuPlotFIT("ht",false,true,"test2/ht",15,75,460,1.2,finalcuts,"",weight);
  MuNuPlotFIT("ptJJ",false,true,"test2/J2CSVbtag",20,0.244,1,1.2,finalcuts,"",weight);
  MuNuPlotFIT("vertices",false,true,"test2/vertices",20,0.244,1,1.2,finalcuts,"",weight);
  MuNuPlotFIT("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"test2/J1J2_DeltaR",20,0,3,1.2,finalcuts,"",weight);
  //MuNuPlotFIT("((J1SVphi-J2SVphi)^2+(J1SVeta-J2SVeta))^(1/2)",false,true,"test2/SV_DeltaR",20,0,3,1.2,finalcuts,"",weight);

  /////preselection cuts
  TString Initialcuts= "muonPt>30&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&MtCal>60";
  TString noweight = "1";

  MuNuPlotFIT("met",false,true,"presel/met",15,60,160,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("highestJetPt",false,true,"presel/highestJetPt",15,25,160,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("secondJetPt",false,true,"presel/secondJetPt",15,25,100,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("highestJetEta",false,true,"presel/highestJetEta",15,-3,3,1.9,Initialcuts,"",noweight);
  MuNuPlotFIT("secondJetEta",false,true,"presel/secondJetEta",15,-3,3,1.9,Initialcuts,"",noweight);
  MuNuPlotFIT("highestJetPhi",false,true,"presel/highestJetPhi",15,-3.14,3.14,1.9,Initialcuts,"",noweight);
  MuNuPlotFIT("secondJetPhi",false,true,"presel/secondJetPhi",15,-3.14,3.14,1.9,Initialcuts,"",noweight);
  MuNuPlotFIT("J1SVMassb",false,true,"csvl2_2/J1SVMass",15,0,7,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("J2SVMassb",false,true,"csvl2_2/J2SVMass",15,0,7,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("J1SVMassb+J2SVMassb",false,true,"csvl2_2/AddSVMass",15,0,8,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("MtCal",false,true,"presel/MtCal",15,60,160,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("muonPt",false,true,"presel/muonPt",15,25,130,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("mJJ",false,true,"presel/mJJ",15,25,130,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("WPt",false,true,"presel/WPt",15,0,260,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("ht",false,true,"presel/ht",15,75,460,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("ptJJ",false,true,"presel/J2CSVbtag",20,0.244,1,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("vertices",false,true,"presel/vertices",20,0.244,1,1.2,Initialcuts,"",noweight);
  MuNuPlotFIT("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"presel/J1J2_DeltaR",20,0,3,1.2,Initialcuts,"",noweight);


*/
	
}

//  LocalWords:  gROOT
