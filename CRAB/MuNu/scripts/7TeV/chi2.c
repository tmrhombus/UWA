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

void chi2(int xmin = 0, int xmax = 200, TString filename="../DsubMC/met2j0bIso2ewkScale_0_200.root", int nparam = 2){
RooAbsData::ErrorType errorType = RooAbsData::SumW2;

file = new TFile(filename);
RooRealVar* h = new RooRealVar("h","h",xmin,xmax); 

//Get Data
TH1D* hData = file->Get("dataih");
hData->SetName("hData");
//hData->Draw();
RooDataHist* data = new RooDataHist("data","data",*h,hData);

//Get Summed MC
TH1D* hMC = file->Get("hh");
hMC->SetName("hMC");
hMC->Draw();
RooDataHist rdhMC("MC","MC",*h,hMC);
RooHistPdf pdfMC("MCpdf","MCpdf",*h,rdhMC);

//make (plot) the curves
RooPlot* hFrame = h->frame(Name("hFrame"));
data->plotOn(hFrame,RooFit::DataError(errorType));
pdfMC.plotOn(hFrame,ProjWData(*data),Components(pdfMC),Name("h_total"));

//Determine Chi^2
double chi2fit = hFrame->chiSquare("h_total", "h_data", nparam);
cout<<"Chi 2 / dof: "<<chi2fit<<endl;

//Determine K-S
double ks = hMC->KolmogorovTest(hData);
cout<<"Kolmogorov-Smirnov: "<<ks<<endl;
}

