#include<TStyle.h>
#include<TFile.h>
#include<TDirectory.h>
#include<TTree.h>
#include<TCanvas.h>
#include<TPaveText.h>
#include<TH1F.h>
#include<TLegend.h>
#include<TROOT.h>
#include <fstream>
#include <THStack.h>
#include <TLatex.h>
#include <iostream>
#include <utility>
#include <TColor.h>
#include <algorithm>
//
// TDR style macro for plots in ROOT
// .L tdrstyle.C
// setTDRStyle()
//
#include <TLorentzVector.h>
#include<TGraphErrors.h>
#include "TStyle.h"
#include "TPad.h"
#include "./Event.C"
using namespace std;

class PlottingClass{
public:

	PlottingClass();
        PlottingClass( TString &, TString &, TString& );
	~PlottingClass();
  	void    RunOnTrees();
	void    initialize();

        double HLTScaleFactorsPerEvent( TLorentzVector&, TLorentzVector&, int );
        double offlineScaleFactors( TLorentzVector&, int );
        int    pickMuEfficiencyBin( TLorentzVector& );
        std::pair<int,int>  pickEleEfficiencyBin( TLorentzVector& );

	static const int Nfile=13;
	static const int NHisto=15;
	TString ProcessFile;
	TString ProcName[Nfile];

        static const int NVar=10;
        TString VarFile;
        TString VarName[NVar];
	int nbin[NVar];
	float xmin[NVar],xmax[NVar],islog[NVar];
	TString var[NVar];

	TFile *f[Nfile];
	TDirectory *sba[Nfile];
	TTree *tree[Nfile];
	Event *Evt[Nfile];

	int   nentries[Nfile];
	float xsec[Nfile];
	int nevt[Nfile];

	float Lumi;
};

PlottingClass::~PlottingClass()                 // destructor, just an example
{
}


class HistoClass{
public:

        HistoClass(const char*,TString &,int,float,float,const char*,int,TString&,float);
	~HistoClass();
	void FillHisto(TH1F *,float,float);
	PlottingClass *PT= new PlottingClass();
	int Nfile,Nhisto;
	TH1F *h[50];
	void GetPlot(int);
	int getColor(int);
private:
        THStack      *hs;
        TH1F         *rhisto;
        TH1F         *sum;
        TGraphErrors *Gsum;
        TGraphErrors *rerrgraph;
	TString _var;
        TString _axis;
        int _nbin;
        float _xmin;
        float _xmax;
        int _log;
        TString _tag;
        void setTDRStyle();
        int _isLog;
        float _lum;
        TString directory;
	TLegend *legend;
};

HistoClass::HistoClass(const char*var,TString &axis,int nbin,float xmin,float xmax,const char* tag,int isLog,TString &dir,float lum){
//	cout<<"In HistoClass constructor"<<endl;
	TH1F::SetDefaultSumw2(kTRUE);
	directory = dir;
	_lum = lum;
	_var=var;
	_axis=axis;
	_nbin=nbin;
	_xmin=xmin;
	_xmax=xmax;
	_tag=tag;
	Nfile=PT->Nfile;
	Nhisto=PT->NHisto;
	for(int i=0;i<20;i++){
		cout<<"Defining histo number "<<i<<endl;
		h[i]=new TH1F(Form("histo_%d_"+_var+_tag,i),_axis,_nbin,_xmin,_xmax);
		h[i]->GetYaxis()->SetTitle("N(events)/bin");
		if(i!=0)  h[i]->SetFillColor(getColor(i));
		h[i]->GetXaxis()->SetTitleOffset(0.2);
                h[i]->GetYaxis()->SetTitleOffset(0.85);
                h[i]->GetXaxis()->SetLabelOffset(0.1);
	}
	sum = new TH1F(Form("sum_%d"+_var+_tag),"Number of events;",_nbin,_xmin,_xmax);
	h[0]->SetMarkerStyle(20);
        h[0]->SetMarkerColor(1);
        h[0]->SetMarkerSize(1.25);
	legend = new TLegend(0.61,0.65,0.95,0.93);
        legend->SetBorderSize(0);
        legend->SetFillColor(0);
        legend->SetTextSize(0.03);
        legend->SetTextFont(42);

        legend->AddEntry(h[0],"data","p");
        legend->AddEntry(h[1],"W+light","f");
	legend->AddEntry(h[2],"W+nc","f");
	legend->AddEntry(h[3],"W+nb","f");	
        legend->AddEntry(h[4],"TTbar","f");
        legend->AddEntry(h[5],"Drell","f");
        legend->AddEntry(h[6],"T t-channel","f");
        legend->AddEntry(h[7],"T s-channel","f");
        legend->AddEntry(h[8],"Tbar t-channel","f");
        legend->AddEntry(h[9],"Tbar s-channel","f");
        legend->AddEntry(h[10],"Tbar t-W","f");
        legend->AddEntry(h[11],"Tbar t-W","f");
        legend->AddEntry(h[12],"WW","f");
        legend->AddEntry(h[13],"WZ","f");
        legend->AddEntry(h[14],"ZZ","f");
/*        legend->AddEntry(Gsum,"MC stat. uncertainty","f");
*///	cout<<"Histograms declared in constr"<<endl;
}


HistoClass::~HistoClass()                 // destructor, just an example
{
		
}


void HistoClass::FillHisto(TH1F *histo,float value,float norm){
	TH1F *_histo=histo;
	float _value=value;
	float _norm=norm;
	_histo->Fill(_value,_norm);
}
void HistoClass::GetPlot(int log){
	_log=log;	
	cout<<"in GetPlot"<<endl;
        setTDRStyle();

	hs  = new THStack("hs","");
	cout<<"hs, sum declared"<<endl;
        float MuOverLFrac = 1.0;
        float MuWgtsimu = 0, ElWgtsimu = 0,MuWgtdata = 0, ElWgtdata = 0;


	// for chi square 
	float chisquare = 0;


	cout<<sum->Integral()<<endl;
	cout<<"legend declared"<<endl;	
	for(int kHisto=Nhisto-1;kHisto>0;kHisto--){
        	sum->Add(h[kHisto]);
		cout<<sum->Integral()<<endl;
        }
	cout<<"legend declared, sum filled"<<endl;
	for(int kHisto = Nhisto-1; kHisto>0; kHisto--){
                hs->Add(h[kHisto]);
	}
	cout<<"legend declared, sum filled, hs  filled"<<endl;
	TCanvas *can = new TCanvas("h", "bla",800,800);
	can->SetLeftMargin(0.1);
	can->SetTopMargin(0.075);
	can->SetRightMargin(0.05);
	can->SetBottomMargin(0.15);
	
	float binw = (_xmax - _xmin)/(float)_nbin;
	cout << _xmax << " " << _xmin << " " << _nbin << " bin width " << binw << endl;	

	float xbin[_nbin],ycontent[_nbin],xerr[_nbin],yerr[_nbin];
	float one[_nbin], ratioerr[_nbin];
	
	TPad *pad[2];
	pad[0]= new TPad("pad0","pad",0.0,0.25,1.0,1.0);
	pad[1]= new TPad("pad1","pad",0.0,0.0,1.0,0.25);
	pad[0]->SetLeftMargin(0.15);
	pad[1]->SetLeftMargin(0.15);
	pad[0]->SetRightMargin(0.03);
	pad[1]->SetRightMargin(0.03);
	pad[0]->SetTopMargin(0.05);
	pad[1]->SetTopMargin(0.0);
	pad[0]->SetBottomMargin(0.02);
	pad[1]->SetBottomMargin(0.35);
	pad[0]->Draw();
	pad[1]->Draw();

	
	pad[0]->cd();
	
	cout<<"in pad0"<<endl;
	h[0]->Draw("e1");

	float max,min;
	max = std::max(h[0]->GetBinContent(h[0]->GetMaximumBin())*1.5,sum->GetBinContent(h[0]->GetMaximumBin())*1.5);
	h[0]->SetMinimum(0);
	h[0]->SetMaximum(max);
	if(_isLog==1){
                gPad->SetLogy(1);
		h[0]->SetMaximum(h[0]->GetBinContent(h[0]->GetMaximumBin())*5000);
                h[0]->SetMinimum(h[0]->GetBinContent(h[0]->GetMaximumBin())/1000000);

        }
	cout<<"Looping on bins"<<endl; 
	for(int k=0;k<h[0]->GetNbinsX();k++){
                xbin[k]=sum->GetBinCenter(k+1);
                ycontent[k]=sum->GetBinContent(k+1);
                xerr[k]=(_xmax-_xmin)/(2.0*_nbin);
                yerr[k]=sum->GetBinError(k+1);
                cout<<ycontent[k]<<" "<<yerr[k]<<endl;

                float comberr = sqrt( sum->GetBinError(k+1)*sum->GetBinError(k+1) + h[0]->GetBinError(k+1)*h[0]->GetBinError(k+1) );
                float diff = ( h[0]->GetBinContent(k+1) - sum->GetBinContent(k+1) )/comberr;
                chisquare = chisquare + diff*diff;

                std::cout << " CHI SQUARE ...  data = " << h[0]->GetBinContent(k+1) <<
                        " MC = " << sum->GetBinContent(k+1) <<
                        " err = " << comberr <<
                        " chisq = " << chisquare << std::endl;

        }

        Gsum = new TGraphErrors(_nbin,xbin,ycontent,xerr,yerr);
	cout<<"Gsum declared"<<endl;

	hs->Draw("histsame");
	Gsum->SetFillColor(2);
        Gsum->SetFillStyle(3005);
        Gsum->Draw("e2same");
	//for(int i=12;i>0;i--)h[i]->Draw("same");

	h[0]->Draw("e1same");
	legend->Draw();
	TLatex *latex = new TLatex();
	latex->SetNDC();
	latex->SetTextFont(42);
	latex->SetTextSize(0.041);
	latex->SetTextAlign(31); // align right
	latex->DrawLatex(0.965,0.96,"#sqrt{s} = 8 TeV");
	latex->SetTextAlign(11); // align left
	latex->DrawLatex(0.15,0.96,Form("CMS preliminary, %.3g fb^{-1}",_lum/1000));
	//	TPaveText *constraint=new TPaveText(0.3,0.9,0.7,0.94,"NDC");
	gPad->RedrawAxis();

	TLatex *conditions = new TLatex();
	conditions->SetNDC();
	conditions->SetTextFont(42);
	conditions->SetTextSize(0.045);
	
	
	pad[1]->cd();
	cout<<"in pad1"<<endl;
	rhisto = (TH1F*)h[0]->Clone();
	rhisto->Divide(sum);

	cout << "ERROR ON RATIO" << endl;
	for(int ibi=0; ibi<_nbin; ibi++)
	  {
	    one[ibi] = 1;
	    ratioerr[ibi] = sum->GetBinError(ibi+1)/sum->GetBinContent(ibi+1);

	   
	    cout << "serr = " << sum->GetBinError(ibi+1) << " sum = " << sum->GetBinContent(ibi+1) << " res = " << ratioerr[ibi] << endl;
	  }
	
	rerrgraph = new TGraphErrors(_nbin,xbin,one,xerr,ratioerr);

	cout<<"rerrgraph declared"<<endl;
	rhisto->Draw("e1");
	rhisto->SetMaximum(2.2);
	rhisto->SetMinimum(0);
	rhisto->SetLineWidth(1);
	rhisto->GetXaxis()->SetLabelSize(0.135);
	rhisto->GetYaxis()->SetLabelSize(0.135);
	rhisto->GetXaxis()->SetTitleSize(0.18);
	rhisto->GetYaxis()->SetTitleSize(0.19);
	rhisto->GetYaxis()->SetTitle("Ratio");
	rhisto->GetXaxis()->SetTitle(_var);
	rhisto->GetXaxis()->SetLabelOffset(0.02);
	rhisto->GetXaxis()->SetTitleOffset(0.85);
	rhisto->GetYaxis()->SetTitleOffset(0.28);
	rhisto->GetYaxis()->SetNdivisions(603);
	//rhisto->SetMarkerStyle(20);
	rhisto->SetMarkerSize(1.25);

	rerrgraph->SetFillColor(2);
	rerrgraph->SetFillStyle(3005);
	rerrgraph->Draw("e2same");

	rhisto->Draw("e1same");
	
	TLine *line;
	line= new TLine(_xmin,1,_xmax,1);
	line->SetLineStyle(3);
	line->SetLineColor(kRed);
	line->Draw();
	//cout<<"creating the histo"<<endl;
	for(int kHisto=Nhisto-1;kHisto>0;kHisto--){
		cout<<"process number  "<<kHisto<<" ";
		for(int i=1;i<h[0]->GetNbinsX();i++){
			cout<<h[kHisto]->GetBinContent(i)<<" ";
		}
		cout<<endl;
	}
	
	TString filename=Form(_var+_tag+"_%d_%d_%d_%d.pdf",_nbin,(int)_xmin,(int)_xmax,_log);
	cout<<"name of the file "<<directory<<" "<<_var<<" "<<_tag<<"---> "<<filename<<endl;
	can->Print(filename);
	
	delete hs;
	delete sum;
	delete rhisto;
	for(int i=0;i<Nfile;i++){delete h[i];}
	delete can;

	
}

int HistoClass::getColor(int col){


  if( col==1 ) return 2;
  if( col==2 ) return 3;
  if( col==3 ) return 4;
  if( col==4 ) return 5;
  if( col==5 ) return 6;
  if( col==6 ) return 7;
  if( col==7 ) return 8;
  if( col==8 ) return 9;
  if( col==9 ) return 18;
  if( col==10 ) return 32;
  if( col==11 ) return 47;
  if( col==12 ) return 56;
  if( col==13 ) return 32;
  if( col==14 ) return 47;
  if( col==15 ) return 56;		
  //if( col==5 ) return  TColor::GetColor((Float_t)0.55294,(Float_t)0.55294,(Float_t)0.55294);  // grey


	return 0;	
}

PlottingClass::PlottingClass(){
}

PlottingClass::PlottingClass( TString &input, TString & inputVar,  TString& dir  ){
	ProcessFile = input;
	VarFile=inputVar;
	Lumi=13498;
}

// *********************************************************************************************

int PlottingClass::pickMuEfficiencyBin( TLorentzVector& lepton )
{

  int binindex = -9;

    if( fabs(lepton.Eta()) < 1.2 && lepton.Pt() < 30. )                        binindex = 0;
    else if( fabs(lepton.Eta()) < 1.2 && lepton.Pt() >= 30. && lepton.Pt() < 50. )   binindex = 1;
    else if( fabs(lepton.Eta()) < 1.2 && lepton.Pt() >= 50. )                   binindex = 2;
    else if( fabs(lepton.Eta()) >= 1.2 && lepton.Pt() < 30. )                   binindex = 3;
    else if( fabs(lepton.Eta()) >= 1.2 && lepton.Pt() >= 30. && lepton.Pt() < 50. ) binindex = 4;
    else if( fabs(lepton.Eta()) >= 1.2 && lepton.Pt() >= 50. )                   binindex = 5;
 
    return binindex;
}

// *********************************************************************************************

std::pair<int,int> PlottingClass::pickEleEfficiencyBin( TLorentzVector& lepton )
{

  std::pair<int,int> indices;

 
  if( lepton.Pt() < 20 ) indices.first = 0;
  else if( lepton.Pt() >= 20 && lepton.Pt() < 30 ) indices.first = 1;
  else if( lepton.Pt() >= 30 && lepton.Pt() < 50 ) indices.first = 2;
  else if( lepton.Pt() >= 50 ) indices.first = 3;

  if( fabs(lepton.Eta()) < 0.8 ) indices.second = 0;
  else if( fabs(lepton.Eta()) > 0.8 && fabs(lepton.Eta()) <= 1.44)   indices.second = 1;
  else if( fabs(lepton.Eta()) > 1.44 && fabs(lepton.Eta()) <= 1.55 ) indices.second = 2;
  else if( fabs(lepton.Eta()) > 1.55 && fabs(lepton.Eta()) <= 2.0 )  indices.second = 3;
  else if( fabs(lepton.Eta()) > 2.0 ) indices.second = 4;

 
  return indices;
}

// *********************************************************************************************


double PlottingClass::HLTScaleFactorsPerEvent( TLorentzVector& leptonH, TLorentzVector& leptonL, int flavor )
{

  double pathScaleF      = 0.;
  double pathScaleF_13_8 = 0.;
  double pathScaleF_17_8 = 0.;
  double pathScaleF_7_7  = 0.;

  int indexsymmH = -1, indexsymmL = -1;

  if( flavor==13 ) {

    int indexH = pickMuEfficiencyBin( leptonH );
    int indexL = pickMuEfficiencyBin( leptonL );

    double effMu13[6] = { 0.967, 0.967, 0.968, 0.924, 0.927, 0.934 };
    double effMu8A[6] = { 0.968, 0.967, 0.968, 0.935, 0.933, 0.939 };
    double effMu17[6] = { 0.96, 0.965, 0.966, 0.907, 0.919, 0.923 };
    double effMu8B[6] = { 0.962, 0.967, 0.967, 0.919, 0.929, 0.93 };
    double effMu7[2]  = { 0.971, 0.948};

    double combeffH[6]; double combeffL[6];

    for( int ib=0; ib<6; ib++ ) {
      combeffH[ib] = (0.84*effMu13[ib]) + (0.16*effMu17[ib]);
      combeffL[ib] = (0.84*effMu8A[ib]) + (0.16*effMu8B[ib]);
    }

    if(fabs(leptonH.Eta())<1.2)   indexsymmH = 0;
    if(fabs(leptonH.Eta())>=1.2)  indexsymmH = 1;
    if(fabs(leptonL.Eta())<1.2)   indexsymmL = 0;
    if(fabs(leptonL.Eta())>=1.2)  indexsymmL = 1;
     
    pathScaleF_13_8 = effMu8A[indexH]*effMu13[indexL]+effMu13[indexH]*effMu8A[indexL]-effMu13[indexH]*effMu8A[indexL];
    pathScaleF_17_8 = effMu8B[indexH]*effMu17[indexL]+effMu17[indexH]*effMu8B[indexL]-effMu17[indexH]*effMu8B[indexL];
    pathScaleF_7_7  = effMu7[indexsymmH]*effMu7[indexsymmL];
    pathScaleF      = 0.044*pathScaleF_7_7+0.802*pathScaleF_13_8+0.154*pathScaleF_17_8;

  }

 else if( flavor==11 ) {

    std::pair<int,int> indicesH = pickEleEfficiencyBin( leptonH );
    std::pair<int,int> indicesL = pickEleEfficiencyBin( leptonL );

    double effEle17[4][5] = {
      { 0.984, 0.986, 1.0, 0.988, 0.98 },
      { 0.994, 0.995, 1.0, 0.994, 0.995 },
      { 0.995, 0.997, 1.0, 0.995, 0.997 },
      { 0.998, 0.997, 1.0, 0.998, 0.998 }
    };

    double effEle8[4][5] = {
      { 0.994, 0.998, 1.0, 0.997, 0.997 },
      { 0.997, 0.998, 1.0, 0.999, 0.999 },
      { 0.998, 0.999, 1.0, 0.998, 1.00 },
      { 0.999, 0.999, 1.0, 0.999, 0.999 }
    };
    
    pathScaleF = effEle8[indicesH.first][indicesH.second]*effEle17[indicesL.first][indicesL.second] + effEle17[indicesH.first][indicesH.second]*effEle8[indicesL.first][indicesL.second] - effEle17[indicesH.first][indicesH.second]*effEle17[indicesL.first][indicesL.second];

 }


  return pathScaleF;
}

// *********************************************************************************************


double PlottingClass::offlineScaleFactors( TLorentzVector& lepton, int flavor ) {

  double singleLepScaleF = 0;
  int index = -9;

  if( flavor==13 ) {

    if( fabs(lepton.Eta()) < 0.9 ){                                 index = 0;}
    else if( fabs(lepton.Eta()) > 0.9 && fabs(lepton.Eta()) < 2.1 ){ index = 1;}
    else if( fabs(lepton.Eta()) > 2.1 )                            {index = 2;}

    double idScaleF[3]  = { 0.995, 0.972, 0.978 };
    double isoScaleF[3] = { 0.9926, 0.9977, 1.010 };
    double idSyst[3]    = { 0.002, 0.002, 0.004 };
    double isoSyst[3]   = { 0.002, 0.002, 0.004 };

    singleLepScaleF = ( idScaleF[index] )*( isoScaleF[index] );
  }

  else if( flavor==11 ) {

  double recoScaleF[4][5] = {
      { 0.998, 1.01, 1.01, 0.996, 0.999 },
      { 0.994, 0.995, 0.994, 0.993, 0.993 },
      { 0.997, 0.999, 0.988, 1.00, 0.993 },
      { 0.996, 0.996, 1.01, 1.00, 0.996 }
    };
    
    double idisoScaleF[4][5] = {
      { 0.983, 0.957, 0.894, 1.02, 1.01 },
      { 0.993, 0.982, 0.969, 0.987, 1.01 },
      { 0.993, 0.99, 0.981, 0.994, 1.01 },
      { 0.993, 0.99, 0.943, 1.00, 1.03 }
    };
	
    std::pair<int,int> indices = pickEleEfficiencyBin( lepton );
    singleLepScaleF = ( recoScaleF[indices.first][indices.second] )*( idisoScaleF[indices.first][indices.second] );

  }

  return singleLepScaleF;

}


// *********************************************************************************************

void PlottingClass::RunOnTrees(){


	


	
	int processindex=0;

	cout<<"Declaration of the histograms"<<endl;
	TString dir="Plots";
	TString tag="test";
	
	HistoClass *histo[NVar][4];
	
	for(int kVar=0;kVar<NVar;kVar++)for(int kCond=0;kCond<4;kCond++){
		cout<<"######### LIST:"<<nbin[kVar]<<" "<<xmin[kVar]<<" "<<xmax[kVar]<<endl;
		histo[kVar][kCond]= new HistoClass(Form(var[kVar]+"_cond%d",kCond),tag,nbin[kVar],xmin[kVar],xmax[kVar],Form("cond_%d",kCond),0,dir,Lumi);
	}
	
	cout<<"Histograms declared"<<endl;
	while(processindex<Nfile)
   	{
		cout<<"Processing file "<<processindex<<endl;
                
		float nevent=nevt[processindex];cout<<"---->"<<nevent<<endl;
		float crosssec=xsec[processindex];cout<<"---->"<<crosssec<<endl;
//		for(int ientry=0; ientry<300000/*nentries[processindex]*/; ientry++) {
                for(int ientry=0; ientry<nentries[processindex]; ientry++) {
			if(ientry%100000==1)cout<<"-->Processing entry "<<ientry<<endl;
			Evt[processindex]->GetEntry(ientry);
			float normfactor=1;
                	if(processindex>0)normfactor=xsec[processindex]/nevent*Lumi;
//			if(processindex>0)normfactor=Evt[processindex]->weightFactor*Lumi;
			bool trigger=Evt[processindex]->HLT_IsoMu24_eta2p1_v_fired==1;
                	bool muon_selection=Evt[processindex]->nMuons==1 && abs(Evt[processindex]->muonEta)<2.1 && Evt[processindex]->muonPt>25;
                	bool vertex=abs(Evt[processindex]->dz)<0.5&&abs(Evt[processindex]->l1DXY)<0.02;
                	bool mt=Evt[processindex]->Mt>50;
			bool isol=Evt[processindex]->lPFIsoDB<0.12;
			bool jetCond=(Evt[processindex]->nJetsPt30 >= 2 && Evt[processindex]->highestJetPt >30 && Evt[processindex]->secondJetPt>30 && abs(Evt[processindex]->highestJetEta)<2.5 && abs(Evt[processindex]->secondJetEta)<2.5);
                	bool MinimalSelection=trigger && muon_selection && vertex && mt && isol && jetCond;
			if(MinimalSelection){
				for(int kVar=0;kVar<NVar;kVar++){
					bool MuExcl=Evt[processindex]->nElectrons==0;
					bool MuElec=Evt[processindex]->nElectrons==1;
					bool bj1=Evt[processindex]->J1CSVbtag>0.65;
					bool bj2=Evt[processindex]->J2CSVbtag>0.65;
					bool bj3=Evt[processindex]->J3CSVbtag>0.65;
					bool OneBTag=(bj1 && !bj2 && !bj3) || (!bj1 && bj2 && !bj3) || (!bj1 && !bj2 && bj3) ;
					bool TwoBTag=(bj1 && bj2 && !bj3) || (bj1 && !bj2 && bj3) || (!bj1 && bj2 && bj3) ;
					int condition;
					if(MuExcl)condition=0;
					if(MuElec)condition=1;
					if(MuExcl && OneBTag)condition=2;
					if(MuExcl && TwoBTag)condition=3;
					if(processindex==1){
						int WCat=0,Wb=0,Wc=0;
						if(Evt[processindex]->nbHadrons>0)Wb=1;
						if(Evt[processindex]->ncCands+Evt[processindex]->ncbarCands>0)Wc=1;
						WCat=2*Wb+Wc;
						if(WCat>=2){
							histo[kVar][condition]->FillHisto(histo[kVar][condition]->h[3],Evt[processindex]->StringToFloat(var[kVar]),normfactor);
						}
						if(WCat==1){
							histo[kVar][condition]->FillHisto(histo[kVar][condition]->h[2],Evt[processindex]->StringToFloat(var[kVar]),normfactor);
						}
						if(WCat==0){
							histo[kVar][condition]->FillHisto(histo[kVar][condition]->h[1],Evt[processindex]->StringToFloat(var[kVar]),normfactor);
						}
					}	
					else if (processindex>1){
						histo[kVar][condition]->FillHisto(histo[kVar][condition]->h[processindex+2],Evt[processindex]->StringToFloat(var[kVar]),normfactor);
					}
					else {
						histo[kVar][condition]->FillHisto(histo[kVar][condition]->h[processindex],Evt[processindex]->StringToFloat(var[kVar]),normfactor);
					}
				}
			}

		}
	
		processindex++;
	}
	for(int kVar=0;kVar<NVar;kVar++)for(int kCond=0;kCond<4;kCond++){
		histo[kVar][kCond]->GetPlot(islog[kVar]);
	}
	
	
	

	//TLegend *legend=new TLegend(0.7,0.7,0.95,0.94);
	
	
}


// *********************************************************************************************

void PlottingClass::initialize(){
	std::cout<<"initalize"<<std::endl;
	ifstream Processes;
	Processes.open(ProcessFile);
	string processline;
	int processindex=0;
	/*   for(int i=0;i<Nfile;i++){
	 sba[i]=(TDirectory *) f[i]->Get("WSVA");
	 tree[i] = (TTree*) sba[i]->Get("event");
	 }
	 */
	std::cout<<"running over the files"<<std::endl;
	while(processindex<Nfile)
	{
		Processes >>   ProcName[processindex] >> xsec[processindex] >> nevt[processindex];
		cout<<"Process number "<<processindex<<": reading the line "<<ProcName[processindex]<<" "<<xsec[processindex]<<" "<<nevt[processindex]<<endl;
		Evt[processindex] = new Event(ProcName[processindex]);
		//	cout<<"ok"<<endl;
		nentries[processindex] = Evt[processindex]->fChain->GetEntriesFast();
        processindex++;
	//cout<<"processindex="<<processindex<<endl;
        
	}
	ifstream Variables;	
	Variables.open(VarFile);
	int varindex=0;
	while(varindex<NVar)
        {
                Variables >>   var[varindex] >> nbin[varindex] >> xmin[varindex] >> xmax[varindex] >> islog[varindex];
                cout<<"Variable number "<<varindex<<": reading the line "<<var[varindex]<<" "<<nbin[varindex]<<" "<<xmin[varindex]<<" "<<xmax[varindex]<<" "<<islog[varindex]<<endl;
        	varindex++;
        }	
}

// *********************************************************************************************

void HistoClass::setTDRStyle() {
	gStyle->SetCanvasBorderMode(0);
	gStyle->SetCanvasColor(kWhite);
	gStyle->SetCanvasDefH(1500); //Height of canvas
	gStyle->SetCanvasDefW(1500); //Width of canvas
	gStyle->SetCanvasDefX(0);   //POsition on screen
	gStyle->SetCanvasDefY(0);
	
	gStyle->SetPadBorderMode(0);
	gStyle->SetPadColor(kWhite);
	gStyle->SetPadGridX(false);
	gStyle->SetPadGridY(false);
	gStyle->SetGridColor(0);
	gStyle->SetGridStyle(3);
	gStyle->SetGridWidth(1);
	
	gStyle->SetFrameBorderMode(0);
	gStyle->SetFrameBorderSize(0.1);
	gStyle->SetFrameFillColor(0);
	gStyle->SetFrameFillStyle(0);
	gStyle->SetFrameLineColor(1);
	gStyle->SetFrameLineStyle(1);
	gStyle->SetFrameLineWidth(0.1);
	
	gStyle->SetHistLineColor(1);
	gStyle->SetHistLineStyle(0);
	gStyle->SetHistLineWidth(0.1);
	
	gStyle->SetEndErrorSize(2);
	gStyle->SetErrorX(0.);
	gStyle->SetEndErrorSize(1.2);
	gStyle->SetMarkerStyle(20);
	
	gStyle->SetOptFit(1);
	gStyle->SetFitFormat("5.4g");
	gStyle->SetFuncColor(2);
	gStyle->SetFuncStyle(1);
	gStyle->SetFuncWidth(1);
	
	gStyle->SetOptDate(0);
	gStyle->SetOptStat(0);
	
	// Margins:
	gStyle->SetPadTopMargin(0.05);
	gStyle->SetPadBottomMargin(0.13);
	gStyle->SetPadLeftMargin(0.16);
	gStyle->SetPadRightMargin(0.02);
	
	// For the Global title:
	
	gStyle->SetOptTitle(0);
	gStyle->SetTitleFont(42);
	gStyle->SetTitleColor(1);
	gStyle->SetTitleTextColor(1);
	gStyle->SetTitleFillColor(10);
	gStyle->SetTitleFontSize(0.05);
	
	// For the axis titles:
	
	gStyle->SetTitleColor(1, "XYZ");
	gStyle->SetTitleFont(42, "XYZ");
	gStyle->SetTitleSize(0.06, "XYZ");
	// gStyle->SetTitleXSize(Float_t size = 0.02); // Another way to set the size?
	// gStyle->SetTitleYSize(Float_t size = 0.02);
	gStyle->SetTitleXOffset(0.9);
	gStyle->SetTitleYOffset(1.25);
	// gStyle->SetTitleOffset(1.1, "Y"); // Another way to set the Offset
	
	// For the axis labels:
	
	gStyle->SetLabelColor(1, "XYZ");
	gStyle->SetLabelFont(42, "XYZ");
	gStyle->SetLabelOffset(0.007, "XYZ");
	gStyle->SetLabelSize(0.045, "XYZ");
	
	// For the axis:
	
	gStyle->SetAxisColor(1, "XYZ");
	gStyle->SetStripDecimals(kTRUE);
	gStyle->SetTickLength(0.03, "XYZ");
	gStyle->SetNdivisions(510, "XYZ");
	gStyle->SetPadTickX(1);  // To get tick marks on the opposite side of the frame
	gStyle->SetPadTickY(1);
	
	// Change for log plots:
	gStyle->SetOptLogx(0);
	gStyle->SetOptLogy(0);
	gStyle->SetOptLogz(0);
	
	gROOT->ForceStyle();
	
}




