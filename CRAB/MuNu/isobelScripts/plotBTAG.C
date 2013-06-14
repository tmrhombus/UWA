//#include "MuNuPlot2BIG.C"
//#include "MuNuPlotNOTE.C"
//#include "MuNuPlot2.C"
//#include "MuNuPlot2tt.C"
#include "MuNuPlot2.C"

void plotBTAG(){

  gROOT->ProcessLine(".L MuNuPlot2.C++");
  gROOT->SetBatch();

 TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&nJetsPt25>=4&&(J1CSVbtag>0.898&&J2CSVbtag>0.898)&&J1SVMassb>0&&J2SVMassb>0";
 TString finalcutsNOSV= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&nJetsPt25>=4&&(J1CSVbtag>0.898&&J2CSVbtag>0.898)";
 TString finalcutsSSVHE= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&nJetsPt25>=4&&(J1SSVHEbtag>1.74 && J2SSVHEbtag>1.74    )";

 TString finalcutsCSVM= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&nJetsPt25>=4&&(J1CSVbtag>0.679&&J2CSVbtag>0.679)&&J1SVMassb>0&&J2SVMassb>0";
 TString finalcutsNOSVCSVM= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&nJetsPt25>=4&&(J1CSVbtag>0.679&&J2CSVbtag>0.679)";

	  TString weight = "EffweightCSVT2";
          TString weightSSVHE = "SSVHEM2Jets";
          TString weightCSVM = "EffweightCSVM2";


//  MuNuPlot2("nJetsPt25+nJets24to5",false,true,"nJetsPt25FULL",10,0,10,1.9,finalcuts,"",weight);
//  MuNuPlot2("nJetsPt25",false,true,"nJetsPt25",10,0,10,1.9,finalcuts,"",weight);
//  MuNuPlot2("nJets24to5",false,true,"nJets24to5",10,0,10,1.9,finalcuts,"",weight);
//  MuNuPlot2("nElectrons",false,true,"nElectrons",10,0,10,1.9,finalcuts,"",weight);
//  MuNuPlot2("DiMuonMass",false,true,"DiMuonMass",20,0,200,1.9,finalcuts,"",weight);

/*
  MuNuPlot2("highestJetEta",false,true,"highestJetEta_BOTH",15,-3,3,1.9,finalcuts,"",weight,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_BOTH",15,-3,3,1.9,finalcuts,"",weight,0.45,false);

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_ONLYCSV",15,-3,3,1.9,finalcutsNOSV,"",weight,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_ONLYCSV",15,-3,3,1.9,finalcutsNOSV,"",weight,0.45,false);


  MuNuPlot2("secondJetPt",false,true,"secondJetPt_BOTH",15,25,200,1.2,finalcuts,"",weight,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_BOTH",15,25,200,1.2,finalcuts,"",weight,0.45, false);

  MuNuPlot2("secondJetPt",false,true,"secondJetPt_ONLYCSV",15,25,200,1.2,finalcutsNOSV,"",weight,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_ONLYCSV",15,25,200,1.2,finalcutsNOSV,"",weight,0.45, false);


  MuNuPlot2("highestJetEta",false,true,"highestJetEta_SSVHE",15,-3,3,1.9,finalcutsSSVHE,"",weightSSVHE,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_SSVHE",15,-3,3,1.9,finalcutsSSVHE,"",weightSSVHE,0.45,false);

  MuNuPlot2("secondJetPt",false,true,"secondJetPt_SSVHE",15,25,200,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_SSVHE",15,25,200,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);
*/

//  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_SSVHE",30,0,8,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);
//  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_SSVHE",30,0,8,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);

/*
  MuNuPlot2("highestJetEta",false,true,"highestJetEta_BOTH_CSVM",15,-3,3,1.9,finalcutsCSVM,"",weightCSVM,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_BOTH_CSVM",15,-3,3,1.9,finalcutsCSVM,"",weightCSVM,0.45,false);

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_ONLYCSVM",15,-3,3,1.9,finalcutsNOSVCSVM,"",weightCSVM,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_ONLYCSVM",15,-3,3,1.9,finalcutsNOSVCSVM,"",weightCSVM,0.45,false);

          
  MuNuPlot2("secondJetPt",false,true,"secondJetPt_BOTH_CSVM",15,25,200,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_BOTH_CSVM",15,25,200,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);

  MuNuPlot2("secondJetPt",false,true,"secondJetPt_ONLYCSVM",15,25,200,1.2,finalcutsNOSVCSVM,"",weightCSVM,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_ONLYCSVM",15,25,200,1.2,finalcutsNOSVCSVM,"",weightCSVM,0.45, false);

  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_CSVM",30,0,8,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);
*/
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_CSVME",30,0,8,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);



/*
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass",30,0,8,1.2,finalcutsNOSV,"",weight,0.45, false);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass",30,0,8,1.2,finalcutsNOSV,"",weight,0.45, false);

  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_NoSVFound",3,-778,-775,1.2,finalcutsNOSV,"",weight,0.45, false);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_NoSVFound",3,-778,-775,1.2,finalcutsNOSV,"",weight,0.45, false);

  MuNuPlot2("J1CSVbtag",false,true,"J1CSVbtag_BOTH",50,0,1,1.2,finalcuts,"","1",0.45,false);
  MuNuPlot2("J2CSVbtag",false,true,"J2CSVbtag_BOTH",50,0,1,1.2,finalcuts,"","1",0.45,false);
  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt_BOTH",20,1,21,1.2,finalcuts,"",weight,0.45,false);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt_BOTH",20,1,21,1.2,finalcuts,"",weight,0.45,false);

  MuNuPlot2("J1CSVbtag",false,true,"J1CSVbtag_ONLYCSV",50,0,1,1.2,finalcutsNOSV,"","1",0.45,false);
  MuNuPlot2("J2CSVbtag",false,true,"J2CSVbtag_ONLYCSV",50,0,1,1.2,finalcutsNOSV,"","1",0.45,false);
  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt_ONLYCSV",20,1,21,1.2,finalcutsNOSV,"",weight,0.45,false);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt_ONLYCSV",20,1,21,1.2,finalcutsNOSV,"",weight,0.45,false);
*/
  TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.898&&J2CSVbtag>0.898)&&J1SVMassb>0&&J2SVMassb>0&&MtCal>45";
  TString finalcutsNOSV= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.898&&J2CSVbtag>0.898)&&MtCal>45";
  TString finalcutsSSVHE= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&MtCal>45&&(J1SSVHEbtag>1.74 && J2SSVHEbtag>1.74)";
  TString finalcutsCSVM= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.679&&J2CSVbtag>0.679)&&J1SVMassb>0&&J2SVMassb>0&&MtCal>45";
  TString finalcutsNOSVCSVM= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==2&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.679&&J2CSVbtag>0.679)&&MtCal>45";

/*
  MuNuPlot2("highestJetEta",false,true,"highestJetEta_BOTH_SIGNAL",15,-3,3,1.9,finalcuts,"",weight,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_BOTH_SIGNAL",15,-3,3,1.9,finalcuts,"",weight,0.45,false);
  MuNuPlot2("secondJetPt",false,true,"secondJetPt_BOTH_SIGNAL",15,25,200,1.2,finalcuts,"",weight,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_BOTH_SIGNAL",15,25,200,1.2,finalcuts,"",weight,0.45, false);

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_ONLYCSV_SIGNAL",15,-3,3,1.9,finalcutsNOSV,"",weight,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_ONLYCSV_SIGNAL",15,-3,3,1.9,finalcutsNOSV,"",weight,0.45,false);
  MuNuPlot2("secondJetPt",false,true,"secondJetPt_ONLYCSV_SIGNAL",15,25,200,1.2,finalcutsNOSV,"",weight,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_ONLYCSV_SIGNAL",15,25,200,1.2,finalcutsNOSV,"",weight,0.45, false);

  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_SIGNAL",30,0,8,1.2,finalcutsNOSV,"",weight,0.45, false);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_SIGNAL",30,0,8,1.2,finalcutsNOSV,"",weight,0.45, false);

  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_NoSVFound_SIGNAL",3,-778,-775,1.2,finalcutsNOSV,"",weight,0.45, false);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_NoSVFound_SIGNAL",3,-778,-775,1.2,finalcutsNOSV,"",weight,0.45, false);
*/
/*
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_SIGNAL_SSVHE",30,0,8,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_SIGNAL_SSVHE",30,0,8,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_SIGNAL_SSVHE",15,-3,3,1.9,finalcutsSSVHE,"",weightSSVHE,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_SIGNAL_SSVHE",15,-3,3,1.9,finalcutsSSVHE,"",weightSSVHE,0.45,false);

  MuNuPlot2("secondJetPt",false,true,"secondJetPt_SIGNAL_SSVHE",15,25,200,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_SIGNAL_SSVHE",15,25,200,1.2,finalcutsSSVHE,"",weightSSVHE,0.45, false);
*/
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_SIGNAL_CSVM",30,0,8,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_SIGNAL_CSVM",30,0,8,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_SIGNAL_CSVM",15,-3,3,1.9,finalcutsCSVM,"",weightCSVM,0.45,false);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta_SIGNAL_CSVM",15,-3,3,1.9,finalcutsCSVM,"",weightCSVM,0.45,false);

  MuNuPlot2("secondJetPt",false,true,"secondJetPt_SIGNAL_CSVM",15,25,200,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_SIGNAL_CSVM",15,25,200,1.2,finalcutsCSVM,"",weightCSVM,0.45, false);



/*
  MuNuPlot2("J1CSVbtag",false,true,"J1CSVbtag_BOTH_SIGNAL",50,0,1,1.2,finalcuts,"","1",0.45,false);
  MuNuPlot2("J2CSVbtag",false,true,"J2CSVbtag_BOTH_SIGNAL",50,0,1,1.2,finalcuts,"","1",0.45,false);
  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt_BOTH_SIGNAL",20,1,21,1.2,finalcuts,"",weight,0.45,false);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt_BOTH_SIGNAL",20,1,21,1.2,finalcuts,"",weight,0.45,false);

  MuNuPlot2("J1CSVbtag",false,true,"J1CSVbtag_ONLYCSV_SIGNAL",50,0,1,1.2,finalcutsNOSV,"","1",0.45,false);
  MuNuPlot2("J2CSVbtag",false,true,"J2CSVbtag_ONLYCSV_SIGNAL",50,0,1,1.2,finalcutsNOSV,"","1",0.45,false);
  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt_ONLYCSV_SIGNAL",20,1,21,1.2,finalcutsNOSV,"",weight,0.45,false);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt_ONLYCSV_SIGNAL",20,1,21,1.2,finalcutsNOSV,"",weight,0.45,false);



  MuNuPlot2("secondJetPt",false,true,"secondJetPt",15,25,200,1.2,finalcuts,"",weight);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt",15,25,200,1.2,finalcuts,"",weight);
  MuNuPlot2("mJJ",false,true,"mJJ",25,0,500,1.2,finalcuts,"",weight);
  MuNuPlot2("MtCal",false,true,"MtCal",20,0,200,1.2,finalcuts,"",weight);
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass",20,0,8,1.2,finalcuts,"",weight);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass",20,0,8,1.2,finalcuts,"",weight);
  MuNuPlot2("mJ3J4",false,true,"mJ3J4",40,0,200,1.2,finalcuts,"",weight);
  MuNuPlot2("J1CSVbtag",false,true,"J1CSVbtag",50,0,1,1.2,finalcuts,"",weight);
  MuNuPlot2("J2CSVbtag",false,true,"J2CSVbtag",50,0,1,1.2,finalcuts,"",weight);
  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt",20,1,21,1.2,finalcuts,"",weight);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt",20,1,21,1.2,finalcuts,"",weight);
   TString finalcuts2= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25==4&&nJets24to5==0&&nElectrons==0&&(J1CSVbtag>0.898&&J2CSVbtag>0.898)";

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_NoSV",15,-3,3,1.9,finalcuts2,"",weight);
   MuNuPlot2("secondJetEta",false,true,"secondJetEta_NoSV",15,-3,3,1.9,finalcuts2,"",weight);
  MuNuPlot2("secondJetPt",false,true,"secondJetPt_NoSV",15,25,150,1.2,finalcuts2,"",weight);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_NoSV",13,25,220,1.2,finalcuts2,"",weight);
  MuNuPlot2("mJJ",false,true,"mJJ_NoSV",50,0,500,1.2,finalcuts2,"",weight);
  MuNuPlot2("MtCal",false,true,"MtCal_NoSV",20,0,200,1.2,finalcuts2,"",weight);
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_NoSV",35,0,7,1.2,finalcuts2,"",weight);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_NoSV",35,0,7,1.2,finalcuts2,"",weight);
  MuNuPlot2("mJ3J4",false,true,"mJ3J4_NoSV",50,0,500,1.2,finalcuts2,"",weight);

  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt_NoSV",20,0,20,1.2,finalcuts2,"",weight);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt_NoSV",20,0,20,1.2,finalcuts2,"",weight);

   TString finalcuts3= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25>=4&&nElectrons==0&&nJets24to5==0";

  MuNuPlot2("highestJetEta",false,true,"highestJetEta_NOBTAG",15,-3,3,1.9,finalcuts3,"",1.0);
   MuNuPlot2("secondJetEta",false,true,"secondJetEta_NOBTAG",15,-3,3,1.9,finalcuts3,"",1.0);
  MuNuPlot2("secondJetPt",false,true,"secondJetPt_NOBTAG",15,25,150,1.2,finalcuts3,"",1.0);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt_NOBTAG",13,25,220,1.2,finalcuts3,"",1.0);
  MuNuPlot2("mJJ",false,true,"mJJ_NOBTAG",50,0,500,1.2,finalcuts3,"",1.0);
  MuNuPlot2("MtCal",false,true,"MtCal_NOBTAG",20,0,200,1.2,finalcuts3,"",1.0);
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass_NOBTAG",35,0,7,1.2,finalcuts3,"",1.0);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass_NOBTAG",35,0,7,1.2,finalcuts3,"",1.0);
  MuNuPlot2("mJ3J4",false,true,"mJ3J4_NOBTAG",50,0,500,1.2,finalcuts3,"",1.0);
  MuNuPlot2("J1muon1pt",false,true,"J1muon1pt_NOBTAG",20,0,20,1.2,finalcuts3,"",1.);
  MuNuPlot2("J2muon2pt",false,true,"J2muon2pt_NOBTAG",20,0,20,1.2,finalcuts3,"",1.);
  MuNuPlot2("J1CSVbtag",false,true,"J1CSVbtag",50,0,1,1.2,finalcuts3,"",1.);
  MuNuPlot2("J2CSVbtag",false,true,"J2CSVbtag",50,0,1,1.2,finalcuts3,"",1.);

  MuNuPlot2("ht",false,true,"ht",15,75,450,1.2,finalcuts,"",weight);
  MuNuPlot2("highestJetPt",false,true,"highestJetPt",13,25,220,1.2,finalcuts,"",weight);
  MuNuPlot2("ptJJ",false,true,"ptJJ",16,0,240,1.2,finalcuts,"",weight);
  MuNuPlot2("J1SVMassb+J2SVMassb",false,true,"AddSVMass",14,1,8,1.2,finalcuts,"",weight);
  MuNuPlot2("mJJ",false,true,"mJJ",12,25,265,1.2,finalcuts,"",weight);
  MuNuPlot2("((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)",false,true,"J1J2_DeltaR",15,0,6.5,1.2,finalcuts,"",weight);


  MuNuPlot2("mJJ",false,true,"mJJ",15,25,250,1.2,finalcuts,"",weight);
  MuNuPlot2("J1SVMassb",false,true,"J1SVMass",35,0,7,1.2,finalcuts,"",weight);
  MuNuPlot2("J2SVMassb",false,true,"J2SVMass",35,0,7,1.2,finalcuts,"",weight);
  MuNuPlot2("MET",false,true,"MET",15,0,150,1.2,finalcuts,"",weight);
  MuNuPlot2("secondJetPt",false,true,"secondJetPt",15,25,150,1.2,finalcuts,"",weight);
  MuNuPlot2("highestJetEta",false,true,"highestJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlot2("secondJetEta",false,true,"secondJetEta",15,-3,3,1.9,finalcuts,"",weight);
  MuNuPlot2("highestJetPhi",false,true,"highestJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlot2("secondJetPhi",false,true,"secondJetPhi",15,-3.14,3.14,1.9,finalcuts,"",weight);
  MuNuPlot2("MtCal",false,true,"MtCal",11,45,150,1.2,finalcuts,"",weight);
  MuNuPlot2("muonPt",false,true,"muonPt",15,25,130,1.2,finalcuts,"",weight);
  MuNuPlot2("WPt",false,true,"WPt",15,0,250,1.2,finalcuts,"",weight);

  MuNuPlot2("vertices",false,true,"vertices",20,0,40,1.2,finalcuts,"",weight);
*/
}
