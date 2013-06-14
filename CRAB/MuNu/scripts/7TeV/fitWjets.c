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

void fitWjets(TString histonameMC="h", bool fixedEWK=true, int startBin=0, int endBin=200,double rebinning=2,TString plotName="fitMjjCOMB", double FRACTION=0)
{  
  RooAbsData::ErrorType errorType = RooAbsData::SumW2;
  RooRealVar* MET= new RooRealVar("MET", "MET [GeV]",startBin,endBin);

  double  QCDNormMC=0, NData=0;

  gROOT->cd();
  char temp[50];

  // GET INPUT FILE
  file = new TFile("../data/forQCDfitUnEbb.root");
  // Get Data
  cout<<"Looking for : "<<"data"+histonameMC<<endl;

  TH1D* hData=file->Get("data"+histonameMC); 
  hData->SetName("hData");
  double NData=hData->Integral(startBin+1,endBin);
  cout << "Made dataset --> " << NData <<" events"<< endl;
  hData->Rebin(rebinning);
  RooDataHist* data= new RooDataHist("data","data",*MET,hData);

  // Get Monte Carlos:	
   //W Jets
  TH1D* hWJets=file->Get("w"+histonameMC);
  hWJets->SetName("hWJets");
  double WJetsMC=hWJets->Integral(startBin+1,endBin);
  hWJets->Rebin(rebinning);
  RooDataHist rdhwJets("rdhwJets","WJets",*MET,hWJets );
  RooHistPdf wJetsPdf("wJetspdf","",*MET,rdhwJets);
  cout << "Made W+Jets -->" <<WJetsMC<<" MC events"<< endl;
   //Di Bosons
  TH1D* hDibosons = file->Get("d"+histonameMC);
  hDibosons->SetName("hDibosons");
  double DibosonsMC=hDibosons->Integral(startBin+1,endBin);
  hDibosons->Rebin(rebinning);
  RooDataHist rdhdiBosons("Dibosons","Dibosons",*MET,hDibosons );
  RooHistPdf  diBosonsPdf("diBosonsPdf","",*MET,rdhdiBosons);
  cout << "Made Dibosons -->" << DibosonsMC<<" MC events"<< endl;
   //Z JEts (Other EWK)
  TH1D* hZJets = file->Get("z"+histonameMC);
  hZJets->SetName("hZJets");
  double ZJetsMC=hZJets->Integral(startBin+1,endBin);
  hZJets->Rebin(rebinning);
  RooDataHist rdhzJets("rdhzJets","ZJets",*MET,hZJets );
  RooHistPdf zJetsPdf("zJetsPdf","",*MET,rdhzJets);
  cout << "Made Z+Jets -->" <<ZJetsMC<<" MC events"<< endl;
   //TTbar
  TH1D* hTTBAR = file->Get("tt"+histonameMC);
  hTTBAR->SetName("hTTBAR");
  double TTBarMC=hTTBAR->Integral(startBin+1,endBin);
  hTTBAR->Rebin(rebinning);
  RooDataHist rdhtt("TTBAR","TTBAR",*MET,hTTBAR );
  RooHistPdf ttPdf("ttPdf","",*MET,rdhtt);
  cout << "Made TTBAR  --> "<<TTBarMC <<" MC events"<<  endl;
   //Single Top
  TH1D* hSingleTop = file->Get("t"+histonameMC);
  hSingleTop->SetName("hSingleTop");
  double TopMC=hSingleTop->Integral(startBin+1,endBin);
  hSingleTop->Rebin(rebinning);
  RooDataHist rdhsingletop("SingleTop","SingleTop",*MET,hSingleTop );
  RooHistPdf singleTopPdf("singleTopPdf","",*MET,rdhsingletop);
  cout << "Made SingleTop  -->" <<TopMC<<" MC events"<< endl;
   //QCD
  TH1* hQCD = file->Get("q"+histonameMC);
  hQCD->SetName("hQCD");
  hQCD->Rebin(rebinning);
  QCDNormMC=hQCD->Integral(startBin+1,endBin);
  RooDataHist rdhqcd("rdhqcd","",*MET, hQCD);
  RooHistPdf qcdPdf("qcdPdf","",*MET,rdhqcd);
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
   yieldsV = new RooArgList(nVjets, nZjets);
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
  
  RooArgList* constraints= new RooArgList(constTTbar,constSingleTop,constDiboson,constVJets);

  // The fit
  fitResult = totalPdf.fitTo(*data, Save(true),RooFit::Extended(true),
                              ExternalConstraints(*constraints),
                              RooFit::Extended(true),
                              PrintEvalErrors(-1),
                              Warnings(false)
                              );


  // The rest is just plotting madness

  RooPlot* METframe = MET->frame(Name("METframe")) ;
  data->plotOn(METframe,RooFit::DataError(errorType));

  totalPdf.plotOn(METframe,ProjWData(*data),Components(RooArgSet(ttPdf,singleTopPdf,qcdPdf,zJetsPdf,diBosonsPdf,wJetsPdf)),
                  Name("h_total"));
  totalPdf.plotOn(METframe,ProjWData(*data),
                  Components(wJetsPdf),
                  LineColor(kPink+10), Name("h_Wjets"));
  totalPdf.plotOn(METframe,ProjWData(*data),
                  Components(zJetsPdf),
                  LineColor(kPink), Name("h_Zjets"));
  totalPdf.plotOn(METframe,ProjWData(*data),
                  Components(RooArgSet(ttPdf,singleTopPdf,diBosonsPdf)),
                  Name("h_Background"),LineColor(kViolet));
  totalPdf.plotOn(METframe,ProjWData(*data),
                  Components(RooArgSet(qcdPdf)),
                  Name("h_qcd"),LineColor(8));

  TCanvas *canvas=new TCanvas("canvas"); canvas->SetFillColor(0);
  METframe->Draw();
   METframe->SetMinimum(0);
   METframe->SetMaximum(1.25* METframe->GetMaximum());

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

   double chi2fit = METframe->chiSquare("h_total", "h_data", nparam);
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
   RooHist* datahist = METframe->getHist("h_data");
   RooCurve* totalhist = METframe->getCurve("h_total");
   //RooCurve* dibosonhist = METframe->getCurve("h_diboson");
   RooCurve* wjetshist = METframe->getCurve("h_Wjets");
   RooCurve* zjetshist = METframe->getCurve("h_Zjets");
   RooCurve* backgroundhist = METframe->getCurve("h_Background");
   RooCurve* littlehist = METframe->getCurve("h_qcd");

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
  canvas->Print("../plots/"+histonameMC+"UnEbb.png");
  canvas->Print("../data/fitMariaButAlittleTMPUnEbb.root");

  TCanvas *canvasLOG=new TCanvas("canvasLOG"); canvasLOG->SetFillColor(0);
  METframe->Draw();
   METframe->SetMinimum(0.05);
   METframe->SetMaximum(1e7);
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
  canvasLOG->Print("../plots/"+histonameMC+"_LOGUnEbb.png");
	


  RooPlot* compframe1 = MET->frame(Name("compframe1")) ;
  //signalmc.plotOn(signalframe1);
  data->plotOn(compframe1);
  totalPdf.plotOn(compframe1);//, Components(temp_sig),LineColor(kAzure),Range(5,00));
  RooHist* hresid1 = compframe1->residHist() ;
  RooHist* hpull1 = compframe1->pullHist() ;

  // Create a new frame to draw the residual distribution and add the distribution to the frame
  RooPlot* frameres1 = MET->frame(Title("Residual Distribution")) ;
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
  RooPlot* framepull1 = MET->frame(Title("Pull Distribution")) ;
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


  CanvasPulls->Print("../plots/"+histonameMC+"UnEbbtwo.png");

  RooPlot* compframe2 = MET->frame(Name("compframe2")) ;
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
			double INTQCD=hQCD->Integral();
		 hQCD->Scale(nQCD.getVal()/INTQCD);

	cout<<endl<<endl<<endl;

         cout<<"========================"<<endl;

	//cout<<"Effi?"<<endl;
	
	//cout<<nVjets.getVal()*WFRAC/WJetsMC<<endl;


	 cout<<"========================"<<endl;

        cout<<"Fraction of QCD events (no cut) "<<FRACTION<<" :"<<endl;
		  cout<<hQCD->Integral()/hData->Integral()<<endl;

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
