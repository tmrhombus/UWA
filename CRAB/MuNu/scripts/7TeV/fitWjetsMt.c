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

void fitWjetsMt(TString histonameMC="h", bool fixedEWK=true, int startBin=0, int endBin=20,double rebinning=1,TString plotName="fitMjjCOMB", double FRACTION=0)
{  
  RooAbsData::ErrorType errorType = RooAbsData::SumW2;

  RooRealVar* mT= new RooRealVar("mT", "mT [GeV]",startBin+1,endBin+1);

  double  QCDNormMC=0, NData=0, WJetsMC=0;
  int mindat=0,maxdat=0,minw=0,maxw=0,minz=0,maxz=0,mind=0,maxd=0,mint=0,maxt=0,mintt=0,maxtt=0;
  gROOT->cd();
  char temp[50];

  // GET INPUT FILE
  TString identifier = "test2j0bIso2_0_20";
  TString filename = "../scratch/forQCD2j0bIso2_0_200.root";
  file = new TFile(filename);
// assuming all files are initlally sized from 0-200

  cout<<"From Bin:   "<<startBin<<endl;
  cout<<"To Bin:     "<<endBin<<endl;

  // Get Data
  cout<<"Looking for : "<<"data"+histonameMC<<endl;

  TH1D* hData=file->Get("data"+histonameMC); 
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
   //W Jets
  TH1D* hWJets=file->Get("w"+histonameMC);
  hWJets->SetName("hWJets");
  hWJets->Rebin(rebinning);
  int minw = hWJets->GetXaxis()->FindBin(startBin);
  int maxw = hWJets->GetXaxis()->FindBin(endBin);
  double WJetsMC=hWJets->Integral(minw,maxw);
  RooDataHist rdhwJets("rdhwJets","WJets",*mT,hWJets );
  RooHistPdf wJetsPdf("wJetspdf","",*mT,rdhwJets);
  cout << "Made W+Jets -->" <<WJetsMC<<" MC events"<< endl;
   //Di Bosons
  TH1D* hDibosons = file->Get("d"+histonameMC);
  hDibosons->SetName("hDibosons");
  hDibosons->Rebin(rebinning);
  int mind = hDibosons->GetXaxis()->FindBin(startBin);
  int maxd = hDibosons->GetXaxis()->FindBin(endBin);
  double DibosonsMC=hDibosons->Integral(mind,maxd);
  RooDataHist rdhdiBosons("Dibosons","Dibosons",*mT,hDibosons );
  RooHistPdf  diBosonsPdf("diBosonsPdf","",*mT,rdhdiBosons);
  cout << "Made Dibosons -->" << DibosonsMC<<" MC events"<< endl;
   //Z JEts (Other EWK)
  TH1D* hZJets = file->Get("z"+histonameMC);
  hZJets->SetName("hZJets");
  hZJets->Rebin(rebinning);
  int minz = hZJets->GetXaxis()->FindBin(startBin);
  int maxz = hZJets->GetXaxis()->FindBin(endBin);
  double ZJetsMC=hZJets->Integral(minz,maxz);
  RooDataHist rdhzJets("rdhzJets","ZJets",*mT,hZJets );
  RooHistPdf zJetsPdf("zJetsPdf","",*mT,rdhzJets);
  cout << "Made Z+Jets -->" <<ZJetsMC<<" MC events"<< endl;
   //TTbar
  TH1D* hTTBAR = file->Get("tt"+histonameMC);
  hTTBAR->SetName("hTTBAR");
  hTTBAR->Rebin(rebinning);
  int mintt = hTTBAR->GetXaxis()->FindBin(startBin);
  int maxtt = hTTBAR->GetXaxis()->FindBin(endBin);
  double TTBarMC=hTTBAR->Integral(mintt,maxtt);
  RooDataHist rdhtt("TTBAR","TTBAR",*mT,hTTBAR );
  RooHistPdf ttPdf("ttPdf","",*mT,rdhtt);
  cout << "Made TTBAR  --> "<<TTBarMC <<" MC events"<<  endl;
   //Single Top
  TH1D* hSingleTop = file->Get("t"+histonameMC);
  hSingleTop->SetName("hSingleTop");
  hSingleTop->Rebin(rebinning);
  int mint = hSingleTop->GetXaxis()->FindBin(startBin);
  int maxt = hSingleTop->GetXaxis()->FindBin(endBin);
  double TopMC=hSingleTop->Integral(mint,maxt);
  RooDataHist rdhsingletop("SingleTop","SingleTop",*mT,hSingleTop );
  RooHistPdf singleTopPdf("singleTopPdf","",*mT,rdhsingletop);
  cout << "Made SingleTop  -->" <<TopMC<<" MC events"<< endl;
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
  RooDataHist rdhqcd("rdhqcd","",*mT, hQCD);
  RooHistPdf qcdPdf("qcdPdf","",*mT,rdhqcd);
  cout << "Made QCD --> "<<QCDNormMC<<" MC events"<< endl;

  //define variables for fit

  RooRealVar nWjets("nWjets","nWjets",WJetsMC);//,     0,   10e9);
  RooRealVar nDiboson("nDiboson","nDiboson",DibosonsMC,DibosonsMC*0.8,DibosonsMC*1.2);
  RooRealVar nZjets("nZjets","nZjets", ZJetsMC);//,0,10e8);;
  RooRealVar nTTbar("nTTbar","", TTBarMC,TTBarMC*0.9,TTBarMC*1.1);//,0,100000);//,0,1.0200);
  RooRealVar nSingleTop("nSingleTop","", TopMC,TopMC*0.8,TopMC*1.2);//,0,10000);//,0,1.0200);
  RooRealVar nQCD("nQCD","nQCD", QCDNormMC,0,1e6);
  RooRealVar nVjets("nVjets","nVjets",WJetsMC+ZJetsMC,     0,   10e9);

  // I will combine Zs&Ws in the same pdf (historical reason again, technically this could be done with all the Non-QCD things)
  RooArgList* componentsV;
  RooArgList* yieldsV;
   componentsV = new RooArgList(wJetsPdf,zJetsPdf);
   yieldsV = new RooArgList(nWjets, nZjets);
  RooAddPdf vJetsPdf("vJetsPdf","extended sum pdf", *componentsV, *yieldsV);
   double WFRAC=WJetsMC/(WJetsMC+ZJetsMC);
   double ZFRAC=ZJetsMC/(WJetsMC+ZJetsMC);

  int nparam=2;
  
  RooArgList* components;
  RooArgList* yields;	
    components = new RooArgList(diBosonsPdf,vJetsPdf, ttPdf, singleTopPdf, qcdPdf);
    yields = new RooArgList(nDiboson, nVjets,nTTbar, nSingleTop, nQCD);
  RooAddPdf totalPdf("totalPdf","extended sum pdf", *components, *yields);

  // This can be used to leave these free in the fit, but centered around the default value
  RooGaussian constTTbar("constTTbar","", nTTbar, RooConst(TTBarMC),RooConst(0.1*TTBarMC)) ;
  RooGaussian constSingleTop("constSingleTop","", nSingleTop, RooConst(TopMC),RooConst(0.1*TopMC)) ;
  RooGaussian constDiboson("constDiboson","", nDiboson, RooConst(DibosonsMC),RooConst(0.1*DibosonsMC)) ;
  RooGaussian constVJets("constVJets","", nVjets, RooConst(WJetsMC+ZJetsMC),RooConst(0.1*(WJetsMC+ZJetsMC))) ;

  nTTbar.setConstant( kTRUE );  // By default all of these are fixed
  nSingleTop.setConstant( kTRUE );
  nDiboson.setConstant( kTRUE );
  if(fixedEWK){  // You can choose at .x level to free the W+Z component (but don't)
   nVjets.setConstant(kTRUE);  
  }
  
/*   RooArgList* constraints= new RooArgList(constTTbar,constSingleTop,constDiboson,constVJets);   */

  // The fit
  fitResult = totalPdf.fitTo(*data, Save(true),RooFit::Extended(true),
/*                               ExternalConstraints(*constraints),	     */
                              RooFit::Extended(true),
                              PrintEvalErrors(-1),
                              Warnings(false)
                              );

  // The rest is just plotting madness

  RooPlot* mTframe = mT->frame(Name("mTframe")) ;
  data->plotOn(mTframe,RooFit::DataError(errorType));

  totalPdf.plotOn(mTframe,ProjWData(*data),Components(RooArgSet(ttPdf,singleTopPdf,qcdPdf,zJetsPdf,diBosonsPdf,wJetsPdf)),
		  Name("h_total"));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(wJetsPdf),
		  LineColor(kPink+10), Name("h_Wjets"));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(zJetsPdf),
		  LineColor(kPink), Name("h_Zjets"));
  totalPdf.plotOn(mTframe,ProjWData(*data),
		  Components(RooArgSet(ttPdf,singleTopPdf,diBosonsPdf)),
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

  sprintf(temp, "W+jets = %d #pm %d", nVjets.getVal()*WFRAC, nVjets.getError()*WFRAC);
  plotlabel->AddText(temp);
  sprintf(temp, "Z+jets + WTauNu = %d #pm %d", nVjets.getVal()*ZFRAC,nVjets.getError()*ZFRAC);
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
  canvas->Print("../scratch/"+histonameMC+identifier+".png");
  canvas->Print("../scratch/fitted"+identifier+".root");

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
  canvasLOG->Print("../scratch/"+histonameMC+"_LOG"+identifier+".png");



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


  CanvasPulls->Print("../scratch/"+histonameMC+identifier+"b.png");

  RooPlot* compframe2 = mT->frame(Name("compframe2")) ;
  data->plotOn(compframe2);
  totalPdf.plotOn(compframe2,ProjWData(*data),
		  Components(RooArgSet(wJetsPdf,ttPdf,singleTopPdf,qcdPdf,zJetsPdf)),
		  Name("h_Background"),LineColor(kPink+10));
  RooHist* hresid2 = compframe2->residHist();
  totalPdf.plotOn(compframe2,ProjWData(*data),Components(diBosonsPdf),DrawOption("LF"),FillStyle(1.031),FillColor(kYellow), Name("h_Dibosons_2"));
  totalPdf.plotOn(compframe2,ProjWData(*data),LineColor(kAzure));

  fitResult->Print("v");
  cout << "======= chi^2/dof = " << chi2fit << endl;
  cout<<"====== TOTAL DATA = "<<(int)NData<<"\\pm"<<sqrt(NData)<<endl;
  cout<<"====== Expected Ws ="<<WJetsMC<<endl;
  //cout<<"====== Fitted   Ws ="<<nVjets.getVal()*WFRAC<<endl;
  //	double ACC=WJetsMC/(31314*4650);
  //cout<<"====== ACC         ="<<ACC<<endl;
  //cout<<"====== CROSS-SECTION ="<<nVjets.getVal()*WFRAC/ACC/4650<<endl;

  cout<<"Fraction of QCD events over cut in "<<FRACTION<<" :"<<endl;
  int BIN=hData->FindBin(FRACTION);
  double minq2 = hQCD->GetXaxis()->FindBin(startBin);
  double maxq2 = hQCD->GetXaxis()->FindBin(endBin);
  double minqtotf = hQCD->GetXaxis()->FindBin(0);
  double maxqtotf = hQCD->GetXaxis()->FindBin(200);
  double INTQCD=hQCD->Integral(minq2,maxq2);
  //double INTQCD=hQCD->Integral(minqtotf,maxqtotf);
  cout<<"Before Scaling QCD Part:  "<<INTQCD<<endl;
  double QCDnoscaleFin=hQCD->Integral(minqtotf,maxqtotf);
  cout<<"Before Scaling QCD total: "<<QCDnoscaleFin<<endl;
  cout<<"hQCD min bin: "<<minq2<<endl;
  cout<<"hQCD max bin: "<<maxq2<<endl;
  cout<<"nQCD.getVal:  "<<nQCD.getVal()<<endl;
  cout<<"QCDNormMC:    "<<QCDNormMC<<endl;
  cout<<"Try This One  "<<nQCD.getVal()/INTQCD<<endl;
  //scale by final QCD size over initial qcd size
  hQCD->Scale(nQCD.getVal()/INTQCD);

  cout<<endl<<endl<<endl;

  cout<<"========================"<<endl;

  //cout<<"Effi?"<<endl;

  //cout<<nVjets.getVal()*WFRAC/WJetsMC<<endl;


  cout<<"========================"<<endl;

  cout<<"Fraction of QCD events (no cut) "<<FRACTION<<" :"<<endl;
  cout<<hQCD->Integral()/hData->Integral()<<endl;
  cout<<"Initial QCD Size in range: "<<QCDNormMC<<endl;
  cout<<"Final QCD Size in range:   "<<hQCD->Integral(minq2,maxq2)<<endl;
  cout<<"QCD Scale Factor in range: "<<hQCD->Integral(minq2,maxq2)/QCDNormMC<<endl<<endl;
  cout<<"Initial QCD Size total: "<<QCDInitSize<<endl;
  double minq3 = hQCD->GetXaxis()->FindBin(0);
  double maxq3 = hQCD->GetXaxis()->FindBin(200);
  double FinalQCDSize = hQCD->Integral(minq3,maxq3);
  cout<<"Final QCD Size total:   "<<FinalQCDSize<<endl;
  cout<<"Total Scale Factor:     "<<FinalQCDSize/QCDInitSize<<endl;
  cout<<"Events from Fit?    --> "<<nQCD.getVal()<<"\\pm"<<nQCD.getError()<<endl;
  cout<<"========================"<<endl;


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

	latex.SetTextAlign(31); // align right
	latex.DrawLatex(0.90,0.96,"#sqrt{s} = 7 TeV");
	if (LUMINOSITY > 0.) {
		latex.SetTextAlign(11); // align left
		latex.DrawLatex(0.210,0.85,Form("#int #font[12]{L} dt = %.1f fb^{-1}", LUMINOSITY));
	}
	latex.SetTextAlign(11); // align left
	latex.DrawLatex(0.18,0.96,"CMS preliminary 2011");
}

//#endif
