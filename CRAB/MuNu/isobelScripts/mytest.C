//#include "MuNuPlot2BIG.C"
//#include "MuNuPlotNOTE.C"
//#include "MuNuPlotUnc.C"
//#include "MuNuPlotUnctt.C"
#include "MuNuPlotUncMed.C"

void mytest(){

  gROOT->ProcessLine(".L MuNuPlotUnc.C++");
  gROOT->SetBatch();

 TString finalcuts= "muonPt>25&&(HLT_IsoMu24_v_fired||HLT_IsoMu24_eta2p1_v_fired)&&fabs(l1DXY)<0.02&&DiMuonMass<60&&nJetsPt25>=2&&nElectrons==0";
	  TString weight = "1";
  MuNuPlotUnc("MtCal",false,true,"darin/MtCal",11,45,150,1.2,finalcuts,"",weight);
  MuNuPlotUnc("MET",false,true,"darin/MET",15,0,150,1.2,finalcuts,"",weight);
  MuNuPlotUnc("muonPt",false,true,"darin/muonPt",15,25,130,1.2,finalcuts,"",weight);

}
