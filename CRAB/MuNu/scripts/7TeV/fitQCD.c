#ifndef __CINT__

#include "RooGlobalFunc.h"
#endif

// ROOT
#include <string.h>
#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TCanvas.h>
#include <TH1F.h>
#include <TH2F.h>
#include <TTree.h>
#include <TGraph.h>
#include <TCut.h>
// #include <RooRealVar.h>
// #include <RooAbsReal.h>
// #include <RooAbsPdf.h>
// #include <RooFormulaVar.h>
// #include <RooAddPdf.h>
// #include <RooDataSet.h>
// #include <RooFitResult.h>
// #include <RooKeysPdf.h>
// #include <RooPlot.h>
//#include <RooHist.h>
// #include <TPaveText.h>
// #include <TLatex.h>
// #include <RooGaussian.h>
// #include <TLegend.h>
// #include <RooCurve.h>

using namespace RooFit;
double IntLUMI=4895;

void fitQCD(TString histonameMC="h", bool fixedEWK=true, int startBin=0, int endBin=200,double rebinning=1,TString plotName="fitMjjCOMB", double FRACTION=0)
{  
  RooAbsData::ErrorType errorType = RooAbsData::SumW2;

  RooRealVar* mT= new RooRealVar("mT", "mT [GeV]",startBin+1,endBin+1);

  double  QCDNormMC=0, NData=0, WJetsMC=0;
  int mindat=0,maxdat=0,minw=0,maxw=0,minz=0,maxz=0,mind=0,maxd=0,mint=0,maxt=0,mintt=0,maxtt=0;
  gROOT->cd();
  char temp[50];

  // GET INPUT FILE
  TString identifier = "4j1bIso2_0_200";
  TString filename = "../MetLook/mt4j1bIso2unscaled_0_200.root";
  file = new TFile(filename);
// assuming all files are initlally sized from 0-200

  cout<<"From Bin:   "<<startBin<<endl;
  cout<<"To Bin:     "<<endBin<<endl;

  // Get Data
  cout<<"Looking for : "<<"datai"+histonameMC<<endl;
  TH1D* hData=file->Get("datai"+histonameMC); 
  hData->SetName("hData");
  hData->Rebin(rebinning);
  int mindat = hData->GetXaxis()->FindBin(startBin);
  int maxdat = hData->GetXaxis()->FindBin(endBin);
  cout<<"mindat= "<<mindat<<endl;
  cout<<"maxdat= "<<maxdat<<endl;
  double NData=hData->Integral(mindat,maxdat);
  cout << "Made dataset --> " << NData <<" events"<< endl;
  RooDataHist* data= new RooDataHist("data","data",*mT,hData);

  // Get Monte Carlos:	
   //Z JEts (Other EWK)
  TH1D* hZJets = file->Get("zi"+histonameMC);
  hZJets->SetName("hZJets");
  hZJets->Rebin(rebinning);
  int minz = hZJets->GetXaxis()->FindBin(startBin);
  int maxz = hZJets->GetXaxis()->FindBin(endBin);
  double ZJetsMC=hZJets->Integral(minz,maxz);
  RooDataHist rdhzJets("rdhzJets","rdhzJets",*mT,hZJets );
  RooHistPdf zJetsPdf("zJetsPdf","zJetsPdf",*mT,rdhzJets);
  cout << "Made Z+Jets -->" <<ZJetsMC<<" MC events"<< endl;
   //Di Bosons
  TH1D* hDibosons = file->Get("di"+histonameMC);
  hDibosons->SetName("hDibosons");
  hDibosons->Rebin(rebinning);
  int mind = hDibosons->GetXaxis()->FindBin(startBin);
  int maxd = hDibosons->GetXaxis()->FindBin(endBin);
  double DibosonsMC=hDibosons->Integral(mind,maxd);
  RooDataHist rdhdiBosons("rdhdiBosons","rdhdiBosons",*mT,hDibosons );
  RooHistPdf  diBosonsPdf("diBosonsPdf","diBosonsPdf",*mT,rdhdiBosons);
  cout << "Made Dibosons -->" << DibosonsMC<<" MC events"<< endl;
   //Single Top
	// t_t
  TH1D* htt = file->Get("tti"+histonameMC);
  htt->SetName("htt");
  htt->Rebin(rebinning);
  int mintt = htt->GetXaxis()->FindBin(startBin);
  int maxtt = htt->GetXaxis()->FindBin(endBin);
  double ttMC = htt->Integral(mintt,maxtt);
  RooDataHist rdhtt("rdhtt","rdhttt",*mT,htt);
  RooHistPdf ttPdf("ttPdf","ttPdf",*mT,rdhtt);
  cout<<"Made sTOP_t -->"<<ttMC<<" MC events"<<endl;
	// t_s
  TH1D* hts = file->Get("tsi"+histonameMC);
  hts->SetName("hts");
  hts->Rebin(rebinning);
  int mints = hts->GetXaxis()->FindBin(startBin);
  int maxts = hts->GetXaxis()->FindBin(endBin);
  double tsMC = hts->Integral(mints,maxts);
  RooDataHist rdhts("rdhts","rdhts",*mT,hts);
  RooHistPdf tsPdf("tsPdf","tsPdf",*mT,rdhts);
  cout<<"Made sTOP_s -->"<<tsMC<<" MC events"<<endl;
	// t_tW
  TH1D* httw = file->Get("ttwi"+histonameMC);
  httw->SetName("httw");
  httw->Rebin(rebinning);
  int minttw = httw->GetXaxis()->FindBin(startBin);
  int maxttw = httw->GetXaxis()->FindBin(endBin);
  double ttwMC = httw->Integral(minttw,maxttw);
  RooDataHist rdhttw("rdhttw","rdhttw",*mT,httw);
  RooHistPdf ttwPdf("ttwPdf","ttwPdf",*mT,rdhttw);
  cout<<"Made sTOP_tW -->"<<ttwMC<<" MC events"<<endl;
   //TTbar
  TH1D* httbar = file->Get("ttbi"+histonameMC);
  httbar->SetName("hTTBAR");
  httbar->Rebin(rebinning);
  int minttb = httbar->GetXaxis()->FindBin(startBin);
  int maxttb = httbar->GetXaxis()->FindBin(endBin);
  double TTBarMC=httbar->Integral(minttb,maxttb);
  RooDataHist rdhttb("rdhttb","rdhttb",*mT,httbar );
  RooHistPdf ttbPdf("ttbPdf","ttbPdf",*mT,rdhttb);
  cout << "Made TTBAR  --> "<<TTBarMC <<" MC events"<<  endl;
   //W Jets
	//W tau
  TH1D* hwt=file->Get("wti"+histonameMC);
  hwt->SetName("hwt");
  hwt->Rebin(rebinning);
  int minwt = hwt->GetXaxis()->FindBin(startBin);
  int maxwt = hwt->GetXaxis()->FindBin(endBin);
  double WTauMC=hwt->Integral(minwt,maxwt);
  RooDataHist rdhwt("rdhwt","rdhwt",*mT,hwt);
  RooHistPdf wtPdf("wtPdf","wtPdf",*mT,rdhwt);
  cout << "Made WTau -->" <<WTauMC<<" MC events"<< endl;
	//W b
  TH1D* hwb=file->Get("wbi"+histonameMC);
  hwb->SetName("hwb");
  hwb->Rebin(rebinning);
  int minwb = hwb->GetXaxis()->FindBin(startBin);
  int maxwb = hwb->GetXaxis()->FindBin(endBin);
  double WbMC=hwb->Integral(minwb,maxwb);
  RooDataHist rdhwb("rdhwb","rdhwb",*mT,hwb);
  RooHistPdf wbPdf("wbPdf","wbPdf",*mT,rdhwb);
  cout << "Made Wb -->" <<WbMC<<" MC events"<< endl;
	//W bb
  TH1D* hwbb=file->Get("wbbi"+histonameMC);
  hwbb->SetName("hwbb");
  hwbb->Rebin(rebinning);
  int minwbb = hwbb->GetXaxis()->FindBin(startBin);
  int maxwbb = hwbb->GetXaxis()->FindBin(endBin);
  double WbbMC=hwbb->Integral(minwbb,maxwbb);
  RooDataHist rdhwbb("rdhwbb","rdhwbb",*mT,hwbb);
  RooHistPdf wbbPdf("wbbPdf","wbbPdf",*mT,rdhwbb);
  cout << "Made Wbb -->" <<WbbMC<<" MC events"<< endl;
	//W cc
  TH1D* hwcc=file->Get("wcci"+histonameMC);
  hwcc->SetName("hwcc");
  hwcc->Rebin(rebinning);
  int minwcc = hwcc->GetXaxis()->FindBin(startBin);
  int maxwcc = hwcc->GetXaxis()->FindBin(endBin);
  double WccMC=hwcc->Integral(minwcc,maxwcc);
  RooDataHist rdhwcc("rdhwcc","rdhwcc",*mT,hwcc);
  RooHistPdf wccPdf("wccPdf","wccPdf",*mT,rdhwcc);
  cout << "Made Wcc -->" <<WccMC<<" MC events"<< endl;
	//W c
  TH1D* hwc=file->Get("wci"+histonameMC);
  hwc->SetName("hwc");
  hwc->Rebin(rebinning);
  int minwc = hwc->GetXaxis()->FindBin(startBin);
  int maxwc = hwc->GetXaxis()->FindBin(endBin);
  double WcMC=hwc->Integral(minwc,maxwc);
  RooDataHist rdhwc("rdhwc","rdhwc",*mT,hwc);
  RooHistPdf wcPdf("wcPdf","wcPdf",*mT,rdhwc);
  cout << "Made Wc -->" <<WcMC<<" MC events"<< endl;
	//W light 
  TH1D* hwl=file->Get("wli"+histonameMC);
  hwl->SetName("hwl");
  hwl->Rebin(rebinning);
  int minwl = hwl->GetXaxis()->FindBin(startBin);
  int maxwl = hwl->GetXaxis()->FindBin(endBin);
  double WlMC=hwl->Integral(minwl,maxwl);
  RooDataHist rdhwl("rdhwl","rdhwl",*mT,hwl);
  RooHistPdf wlPdf("wlPdf","wlPdf",*mT,rdhwl);
  cout << "Made Wl -->" <<WlMC<<" MC events"<< endl;
   //QCD
  TH1* hQCD = file->Get("q"+histonameMC);
  hQCD->SetName("hQCD");
  hQCD->Rebin(rebinning);
  int minq = hQCD->GetXaxis()->FindBin(startBin);
  int maxq = hQCD->GetXaxis()->FindBin(endBin);
  int minqtoti = hQCD->GetXaxis()->FindBin(0);
  int maxqtoti = hQCD->GetXaxis()->FindBin(200);
  QCDNormMC=hQCD->Integral(minq,maxq);
  double QCDInitSize=hQCD->Integral(minqtoti,maxqtoti);
  RooDataHist rdhqcd("rdhqcd","rdhqcd",*mT, hQCD);
  RooHistPdf qcdPdf("qcdPdf","qcdPdf",*mT,rdhqcd);
  cout << "Made QCD --> "<<QCDNormMC<<" MC events"<< endl;

  //define variables for fit

   RooRealVar nDiboson("nDiboson","nDiboson",DibosonsMC, DibosonsMC*0.8, DibosonsMC*1.2);
   RooRealVar nTTbar("nttbar","nttbar", TTBarMC, TTBarMC*0.8, TTBarMC*1.2);
   RooRealVar nQCD("nQCD","nQCD", QCDNormMC,0,1e6);

    RooRealVar ntt("ntt","ntt",ttMC, ttMC*0.8, ttMC*1.2);
    RooRealVar nts("nts","nts",tsMC, tsMC*0.8, tsMC*1.2);
    RooRealVar nttw("nttw","nttw",ttwMC, ttwMC*0.8, ttwMC*1.2);
  double TopMC = ttMC+tsMC+ttwMC;
  RooRealVar nSingleTop("nSingleTop","nSingleTop",TopMC, TopMC*0.8, TopMC*1.2);
    RooRealVar nwt("nwt","nwt",WTauMC, WTauMC*0.8, WTauMC*1.2);
    RooRealVar nwb("nwb","nwb",WbMC, WbMC*0.8, WbMC*1.2);
    RooRealVar nwbb("nwbb","nwbb",WbbMC, WbbMC*0.8, WbbMC*1.2);
    RooRealVar nwcc("nwcc","nwcc",WccMC, WccMC*0.8, WccMC*1.2);
    RooRealVar nwc("nwc","nwc",WcMC, WcMC*0.8, WcMC*1.2);
    RooRealVar nwl("nwl","nwl",WlMC, WlMC*0.8, WlMC*1.2);
    double WJetsMC = WTauMC+WbMC+WbbMC+WccMC+WcMC+WlMC;
    RooRealVar nWJets("nWJets","nWJets",WJetsMC, WJetsMC*0.8, WJetsMC*1.2);
    RooRealVar nZJets("nZJets","nZJets", ZJetsMC, ZJetsMC*0.8, ZJetsMC*1.2);
    double VJetsMC = WJetsMC+ZJetsMC;
  RooRealVar nVJets("nVJets","nVJets",VJetsMC,VJetsMC*0.8,VJetsMC*1.2);

  double WFRAC=WJetsMC/(VJetsMC);
  double ZFRAC=ZJetsMC/(VJetsMC);
  int nparam=2;

  RooArgList* tList;
   tList = new RooArgList(ttPdf,tsPdf,ttwPdf);
  RooArgList* yieldT;
   yieldT = new RooArgList(ntt,nts,nttw);
 RooAddPdf singleTopPdf("singleTopPdf","singleTopPdf",*tList,*yieldT);
 
  RooArgList* wList;
   wList = new RooArgList(wtPdf,wbPdf,wbbPdf,wccPdf,wcPdf,wlPdf);
  RooArgList* yieldW;	
   yieldW = new RooArgList(nwt, nwb, nwbb, nwcc, nwc, nwl);
 RooAddPdf wJetsPdf("wJetsPdf","wJetsPdf",*wList,*yieldW);

  RooArgList* vList;
   vList = new RooArgList(wJetsPdf, zJetsPdf);
  RooArgList* yieldV;
   yieldV = new RooArgList(nWJets,nZJets);
 RooAddPdf vJetsPdf("vJetsPdf","vJetsPdf",*vList,*yieldV);

  RooArgList* components;
  RooArgList* yields;
   components = new RooArgList(diBosonsPdf, vJetsPdf, ttbPdf, singleTopPdf, qcdPdf);
   yields = new RooArgList(nDiboson, nVJets, nTTbar, nSingleTop, nQCD);
  RooAddPdf totalPdf("totalPdf","extended sum pdf", *components, *yields);

  RooGaussian gausDiboson("gausDiboson","gausDiboson",nDiboson,RooConst(DibosonsMC),RooConst(0.1*DibosonsMC));
  RooGaussian gausVJets("gausVJets","gausVJets",nVJets,RooConst(VJetsMC),RooConst(0.1*(VJetsMC)));
  RooGaussian gausTTbar("gausTTbar","gausTTbar", nTTbar, RooConst(TTBarMC),RooConst(0.1*TTBarMC));
  RooGaussian gausSingleTop("gausSingleTop","gausSingleTop",nSingleTop,RooConst(TopMC),RooConst(0.1*TopMC));

  nDiboson.setConstant(kTRUE);
  nTTbar.setConstant(kTRUE);
  nVJets.setConstant(kTRUE);
  nSingleTop.setConstant(kTRUE);
  
  nZJets.setConstant(kTRUE);
  ntt.setConstant(kTRUE);
  nts.setConstant(kTRUE);
  nttw.setConstant(kTRUE);
  nwt.setConstant(kTRUE);
  nwb.setConstant(kTRUE);
  nwbb.setConstant(kTRUE);
  nwcc.setConstant(kTRUE);
  nwc.setConstant(kTRUE);
  nwl.setConstant(kTRUE);
  nWJets.setConstant(kTRUE);

 RooArgList* constraints = new RooArgList(gausDiboson,gausVJets,gausTTbar,gausSingleTop);

//////////////////////////////////////////////
  // The fit
  fitResult = totalPdf.fitTo(*data, Save(true),RooFit::Extended(true),
	ExternalConstraints(*constraints),
	RooFit::Extended(true),
	PrintEvalErrors(-1),
	Warnings(false)
	);
//////////////////////////////////////////////

  // The rest is just plotting madness

  RooPlot* mTframe = mT->frame(Name("mTframe")) ;
  data->plotOn(mTframe,RooFit::DataError(errorType));

  totalPdf.plotOn(mTframe,ProjWData(*data),Components(RooArgSet(ttbPdf,singleTopPdf,qcdPdf,zJetsPdf,diBosonsPdf,wJetsPdf)),
		  Name("h_total"));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(wJetsPdf),
		  LineColor(kPink+10), Name("h_Wjets"));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(zJetsPdf),
		  LineColor(kPink), Name("h_Zjets"));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(RooArgSet(ttbPdf,singleTopPdf,diBosonsPdf)),
		  Name("h_Background"),LineColor(kViolet));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(RooArgSet(qcdPdf)),
		  Name("h_qcd"),LineColor(8));

  TCanvas *canvas=new TCanvas("canvas"); canvas->SetFillColor(0);
  mTframe->Draw();
  mTframe->SetMinimum(0);
  mTframe->SetMaximum(1.25* mTframe->GetMaximum());

  TPaveText *plotlabel = new TPaveText(0.55,0.87,0.85,0.92,"NDC");
  plotlabel->SetTextColor(kBlack);
  plotlabel->SetFillColor(kWhite);
  plotlabel->SetBorderSize(0);
  plotlabel->SetTextAlign(12);
  plotlabel->SetTextSize(0.03);
  TPaveText *plotlabel5 = new TPaveText(0.55,0.82,0.85,0.87,"NDC");
  plotlabel5->SetTextColor(kBlack);
  plotlabel5->SetFillColor(kWhite);
  plotlabel5->SetBorderSize(0);
  plotlabel5->SetTextAlign(12);
  plotlabel5->SetTextSize(0.03);
  TPaveText *plotlabel6 = new TPaveText(0.55,0.77,0.85,0.82,"NDC");
  plotlabel6->SetTextColor(kBlack);
  plotlabel6->SetFillColor(kWhite);
  plotlabel6->SetBorderSize(0);
  plotlabel6->SetTextAlign(12);
  plotlabel6->SetTextSize(0.03);
  TPaveText *plotlabel7 = new TPaveText(0.55,0.72,0.85,0.77,"NDC");
  plotlabel7->SetTextColor(kBlack);
  plotlabel7->SetFillColor(kWhite);
  plotlabel7->SetBorderSize(0);
  plotlabel7->SetTextAlign(12);
  plotlabel7->SetTextSize(0.03);
  TPaveText *plotlabel8 = new TPaveText(0.55,0.67,0.85,0.72,"NDC");
  plotlabel8->SetTextColor(kBlack);
  plotlabel8->SetFillColor(kWhite);
  plotlabel8->SetBorderSize(0);
  plotlabel8->SetTextAlign(12);
  plotlabel8->SetTextSize(0.03);
  TPaveText *plotlabel9 = new TPaveText(0.55,0.62,0.85,0.67,"NDC");
  plotlabel9->SetTextColor(kBlack);
  plotlabel9->SetFillColor(kWhite);
  plotlabel9->SetBorderSize(0);
  plotlabel9->SetTextAlign(12);
  plotlabel9->SetTextSize(0.03);
  TPaveText *plotlabel10 = new TPaveText(0.62,0.35,0.82,0.30,"NDC");
  plotlabel10->SetTextColor(kBlack);
  plotlabel10->SetFillColor(0);
  plotlabel10->SetFillStyle(0);
  plotlabel10->SetBorderSize(0);
  plotlabel10->SetTextAlign(12);
  plotlabel10->SetTextSize(0.0);

  sprintf(temp, "W+jets = %d #pm %d", nVJets.getVal()*WFRAC, nVJets.getError()*WFRAC);
  plotlabel->AddText(temp);
  sprintf(temp, "Z+jets + WTauNu = %d #pm %d", nVJets.getVal()*ZFRAC,nVJets.getError()*ZFRAC);
  plotlabel5->AddText(temp);
  sprintf(temp, "t#bar{t}, Top (fixed) = %d", nSingleTop.getVal()+nTTbar.getVal());
  plotlabel7->AddText(temp);
  sprintf(temp, "QCD = %d (fixed)", nQCD.getVal());
  sprintf(temp, "QCD = %d #pm %d", nQCD.getVal(),nQCD.getError());
  plotlabel6->AddText(temp);
  sprintf(temp, "Di-boson (fixed) = %d", nDiboson.getVal());
  plotlabel8->AddText(temp);

  double chi2fit = mTframe->chiSquare("h_total", "h_data", nparam);
  sprintf(temp, "#chi^{2}/dof = %.2f",chi2fit );
  plotlabel10->AddText(temp);
  plotlabel->Draw();
  plotlabel5->Draw();
  plotlabel6->Draw();
  plotlabel7->Draw();
  plotlabel8->Draw();
  cmsPrelim2();
  // TLegend* legend = new TLegend(0.35,0.35,0.55,0.55);
  TLegend* legend = new TLegend(0.58,0.65,0.88,0.40);   // I can plot a legend with RooFit ;-)
  RooHist* datahist = mTframe->getHist("h_data");
  RooCurve* totalhist = mTframe->getCurve("h_total");
  //RooCurve* dibosonhist = mTframe->getCurve("h_diboson");
  RooCurve* wjetshist = mTframe->getCurve("h_Wjets");
  RooCurve* zjetshist = mTframe->getCurve("h_Zjets");
  RooCurve* backgroundhist = mTframe->getCurve("h_Background");
  RooCurve* littlehist = mTframe->getCurve("h_qcd");

  legend->AddEntry( datahist, "Data", "P");
  legend->AddEntry( totalhist, "Fit Result", "L");
  legend->AddEntry( wjetshist, "W+jets", "L");
  legend->AddEntry( zjetshist, "Z+jets", "L");
  legend->AddEntry( backgroundhist, "Top, t#bar{t}, Di-boson", "L");
  legend->AddEntry( littlehist, "QCD", "L");
  legend->SetFillColor(0);
  legend->SetFillStyle(0);
  legend->Draw();
  plotlabel10->Draw();
  canvas->Print("../MetLook/"+histonameMC+identifier+".png");
//  canvas->Print("../DsubMC/"+identifier+".root");

  TCanvas *canvasLOG=new TCanvas("canvasLOG"); canvasLOG->SetFillColor(0);
  mTframe->Draw();
  mTframe->SetMinimum(0.05);
  mTframe->SetMaximum(1e7);
  TLegend* legend2 = new TLegend(0.55,0.90,0.85,0.65);
  legend2->AddEntry( datahist, "Data", "P");
  legend2->AddEntry( totalhist, "Fit Result", "L");
  legend2->AddEntry( wjetshist, "W+jets", "L");
  legend2->AddEntry( zjetshist, "Z+jets", "L");
  legend2->AddEntry( backgroundhist, "Top, t#bar{t}, Di-boson", "L");
  legend2->AddEntry( littlehist, "QCD", "L");
  legend2->SetFillColor(0);
  legend2->SetFillStyle(0);
  legend2->Draw();
  plotlabel10->Draw();
  canvasLOG->SetLogy();
  canvasLOG->Print("../MetLook/"+histonameMC+identifier+"_LOG"+".png");



  RooPlot* compframe1 = mT->frame(Name("compframe1")) ;
  //signalmc.plotOn(signalframe1);
  data->plotOn(compframe1);
  totalPdf.plotOn(compframe1);//, Components(temp_sig),LineColor(kAzure),Range(5,00));
  RooHist* hresid1 = compframe1->residHist() ;
  RooHist* hpull1 = compframe1->pullHist() ;

  // Create a new frame to draw the residual distribution and add the distribution to the frame
  RooPlot* frameres1 = mT->frame(Title("Residual Distribution")) ;
  frameres1->GetYaxis()->SetTitle(Form("(Data - Fit) / (%2.0f)",rebinning)) ;
  frameres1->GetYaxis()->CenterTitle(true);
  frameres1->addPlotable(hresid1,"P") ;
  TPaveText *plotlabelRes = new TPaveText(0.55,0.87,0.85,0.92,"NDC");
  plotlabelRes->SetTextColor(kBlack);
  plotlabelRes->SetFillColor(kWhite);
  plotlabelRes->SetBorderSize(0);
  plotlabelRes->SetTextAlign(12);
  plotlabelRes->SetTextSize(0.03);
  sprintf(temp, "Residual Distribution");
  plotlabelRes->AddText(temp);

  // Create a new frame to draw the pull distribution and add the distribution to the frame
  RooPlot* framepull1 = mT->frame(Title("Pull Distribution")) ;
  framepull1->GetYaxis()->SetTitle(Form("(Data - Fit)/Error / (%2.0f)",rebinning)) ;
  framepull1->GetYaxis()->CenterTitle(true);
  framepull1->addPlotable(hpull1,"P") ;
  TPaveText *plotlabelPull = new TPaveText(0.55,0.87,0.85,0.92,"NDC");
  plotlabelPull->SetTextColor(kBlack);
  plotlabelPull->SetFillColor(kWhite);
  plotlabelPull->SetBorderSize(0);
  plotlabelPull->SetTextAlign(12);
  plotlabelPull->SetTextSize(0.03);
  sprintf(temp, "Pulls");
  plotlabelPull->AddText(temp);
  // Create a new frame to draw the residual distribution and add the distribution to the frame

  TCanvas *CanvasPulls=new TCanvas("CanvasPulls",""); CanvasPulls->Divide(1,2);CanvasPulls->SetFillColor(0);
  CanvasPulls->cd(1); frameres1->Draw();
  CanvasPulls->cd(2); framepull1 ->Draw();


  CanvasPulls->Print("../MetLook/"+histonameMC+identifier+"_b.png");

  RooPlot* compframe2 = mT->frame(Name("compframe2")) ;
  data->plotOn(compframe2);
  totalPdf.plotOn(compframe2,ProjWData(*data),
		  Components(RooArgSet(wJetsPdf,ttbPdf,singleTopPdf,qcdPdf,zJetsPdf)),
		  Name("h_Background"),LineColor(kPink+10));
  RooHist* hresid2 = compframe2->residHist();
  totalPdf.plotOn(compframe2,ProjWData(*data),Components(diBosonsPdf),DrawOption("LF"),FillStyle(1.031),FillColor(kYellow), Name("h_Dibosons_2"));
  totalPdf.plotOn(compframe2,ProjWData(*data),LineColor(kAzure));

  fitResult->Print("v");
  cout << "chi^2/dof = " << chi2fit << " over range "<< startBin << " to "<< endBin<<endl;
/*   cout<<"====== TOTAL DATA = "<<(int)NData<<"\\pm"<<sqrt(NData)<<endl;    */
/*   cout<<"====== Expected Ws ="<<WJetsMC<<endl;			     */
/*   //cout<<"====== Fitted   Ws ="<<nVjets.getVal()*WFRAC<<endl;	     */
/*   //	double ACC=WJetsMC/(31314*4650);				     */
/*   //cout<<"====== ACC         ="<<ACC<<endl;				     */
/*   //cout<<"====== CROSS-SECTION ="<<nVjets.getVal()*WFRAC/ACC/4650<<endl;   */
/*									     */
/*   cout<<"Fraction of QCD events over cut in "<<FRACTION<<" :"<<endl;	     */
/*   int BIN=hData->FindBin(FRACTION);					     */
/*   double minq2 = hQCD->GetXaxis()->FindBin(startBin);		     */
/*   double maxq2 = hQCD->GetXaxis()->FindBin(endBin);			     */
/*   double minqtotf = hQCD->GetXaxis()->FindBin(0);			     */
/*   double maxqtotf = hQCD->GetXaxis()->FindBin(200);			     */
/*   double INTQCD=hQCD->Integral(minq2,maxq2);				     */
/*   //double INTQCD=hQCD->Integral(minqtotf,maxqtotf);			     */
/*   cout<<"Before Scaling QCD Part:  "<<INTQCD<<endl;			     */
/*   double QCDnoscaleFin=hQCD->Integral(minqtotf,maxqtotf);		     */
/*   cout<<"Before Scaling QCD total: "<<QCDnoscaleFin<<endl;		     */
/*   cout<<"hQCD min bin: "<<minq2<<endl;				     */
/*   cout<<"hQCD max bin: "<<maxq2<<endl;				     */
/*   cout<<"nQCD.getVal:  "<<nQCD.getVal()<<endl;			     */
/*   cout<<"QCDNormMC:    "<<QCDNormMC<<endl;				     */
/*   cout<<"Try This One  "<<nQCD.getVal()/INTQCD<<endl;		     */
/*   //scale by final QCD size over initial qcd size			     */
/*   hQCD->Scale(nQCD.getVal()/INTQCD);					     */
/*									     */
/*   cout<<"========================"<<endl;				     */
/*									     */
/*   //cout<<"Effi?"<<endl;						     */
/*									     */
/*   //cout<<nVjets.getVal()*WFRAC/WJetsMC<<endl;			     */
/*									     */
/*									     */
/*   cout<<"========================"<<endl;				     */
/*									     */
/*   cout<<"Fraction of QCD events (no cut) "<<FRACTION<<" :"<<endl;	     */
/*   cout<<hQCD->Integral()/hData->Integral()<<endl;			     */
/*   cout<<"Initial QCD Size in range: "<<QCDNormMC<<endl;		     */
/*   cout<<"Final QCD Size in range:   "<<hQCD->Integral(minq2,maxq2)<<endl;   */
/*   cout<<"QCD Scale Factor in range: "<<hQCD->Integral(minq2,maxq2)/QCDNormMC<<endl<<endl;   */
/*   cout<<"Initial QCD Size total: "<<QCDInitSize<<endl;		     */
/*   double minq3 = hQCD->GetXaxis()->FindBin(0);			     */
/*   double maxq3 = hQCD->GetXaxis()->FindBin(200);			     */
/*   double FinalQCDSize = hQCD->Integral(minq3,maxq3);			     */
/*   cout<<"Final QCD Size total:   "<<FinalQCDSize<<endl;		     */
/*   cout<<"Total Scale Factor:     "<<FinalQCDSize/QCDInitSize<<endl;	     */
/*   cout<<"Events from Fit?    --> "<<nQCD.getVal()<<"\\pm"<<nQCD.getError()<<endl;   */
/*   cout<<"========================"<<endl;				     */

double qcdSize = hQCD->Integral(minq,maxq);
double zSize = hZJets->Integral(minz,maxz);
double diboSize = hDibosons->Integral(mind,maxd);
double ttSize = htt->Integral(mintt,maxtt);
double tsSize = hts->Integral(mints,maxts);
double ttwSize = httw->Integral(minttw,maxttw);
double ttbarSize = httbar->Integral(minttb,maxttb);
double wtSize = hwt->Integral(minwt,maxwt);
double wbSize = hwb->Integral(minwb,maxwb);
double wbbSize = hwbb->Integral(minwbb,maxwbb);
double wccSize = hwcc->Integral(minwcc,maxwcc);
double wcSize = hwc->Integral(minwc,maxwc);
double wlSize = hwl->Integral(minwl,maxwl);

cout<<"Dib Scale:   "<<nDiboson.getVal()/diboSize<<endl;
cout<<"QCD Scale:   "<<nQCD.getVal()/qcdSize<<endl;
cout<<"t Scale:     "<<nSingleTop.getVal()/TopMC<<endl;
cout<<"V Scale:     "<<nVJets.getVal()/VJetsMC<<endl;
cout<<"ttBar Scale: "<<nTTbar.getVal()/ttbarSize<<endl;
cout<<endl;
cout<<"Z Scale:     "<<nZJets.getVal()/zSize<<endl;
cout<<"t_t Scale:   "<<ntt.getVal()/ttSize<<endl;
cout<<"t_s Scale:   "<<nts.getVal()/tsSize<<endl;
cout<<"t_tW Scale:  "<<nttw.getVal()/ttwSize<<endl;
cout<<"wtau Scale:  "<<nwt.getVal()/wtSize<<endl;
cout<<"wb Scale:    "<<nwb.getVal()/wbSize<<endl;
cout<<"wbb Scale:   "<<nwbb.getVal()/wbbSize<<endl;
cout<<"wcc Scale:   "<<nwcc.getVal()/wccSize<<endl;
cout<<"wc Scale:    "<<nwc.getVal()/wcSize<<endl;
cout<<"wl Scale:    "<<nwl.getVal()/wlSize<<endl;

  cmsPrelim2();

  return;

}


////CMS Preliminary label and lumu
void cmsPrelim()
{
	const float LUMINOSITY = IntLUMI;
	TLatex latex;
	latex.SetNDC();
	latex.SetTextSize(0.0);

	latex.SetTextAlign(31); // align right
	latex.DrawLatex(0.90,0.96,"#sqrt{s} = 7 TeV");
	if (LUMINOSITY > 0.) {
		latex.SetTextAlign(31); // align right
		latex.DrawLatex(0.82,0.7,Form("#int #font[12]{L} dt = %.1f fb^{-1}", LUMINOSITY/1000));
	}
	latex.SetTextAlign(11); // align left
	latex.DrawLatex(0.18,0.96,"CMS preliminary 2011");
}




////CMS Preliminary label and lumu -- upper left corner
void cmsPrelim2()
{
	const float LUMINOSITY = IntLUMI/1000.;
	TLatex latex;
	latex.SetNDC();
	latex.SetTextSize(0.0);

	latex.SetTextAlign(31); // align righ2
	latex.DrawLatex(0.90,0.96,"#sqrt{s} = 7 TeV");
	if (LUMINOSITY > 0.) {
		latex.SetTextAlign(11); // align left
		latex.DrawLatex(0.210,0.85,Form("#int #font[12]{L} dt = %.1f fb^{-1}", LUMINOSITY));
	}
	latex.SetTextAlign(11); // align left
	latex.DrawLatex(0.18,0.96,"CMS preliminary 2011");
}

 //#endif
