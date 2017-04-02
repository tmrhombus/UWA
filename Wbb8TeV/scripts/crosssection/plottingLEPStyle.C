//#############################################################################################
//# Original EWK style macro prepared by: Matthieu Marionneau and Gautier Hamel de Monchenault#
//# Some 2012 additions by M. Cepeda						            #
//#############################################################################################

#include <iostream>
#include <stdlib.h>
#include <vector>
#include <map>

#include "TFile.h"
#include "TH1F.h"
#include "TString.h"
#include "THStack.h"
#include "TLegend.h"
#include "TLegendEntry.h"
#include "TLatex.h"
#include "TStyle.h"
#include "TPad.h"
#include "TCanvas.h"
#include "TMarker.h"
#include "TGraphAsymmErrors.h"
#include "TGraphErrors.h"
#include "TLine.h"
#include "TPolyLine.h"

class LEPStyle
{
public:

  TString _name, _title;
  TCanvas* _canv;
  float _xmin, _xmax;
  float _ymin, _ymax;
  int _ndivx;

  float _scale;
  
  TH1* _hist;
  TAxis* _ax;
  TAxis* _ay;

  // Data points
  vector< TString > _dentry;
  vector< Float_t >   _dval;
  vector< Float_t >   _dstatup;
  vector< Float_t >   _dsystup;
  vector< Float_t >   _dtheoup;
  vector< Float_t >   _dstatlo;
  vector< Float_t >   _dsystlo;
  vector< Float_t >   _dtheolo;
  vector< Float_t >   _dlumi;
  vector< Int_t   >   _dmarker;
  vector< Float_t >   _dsize;
  vector< Int_t   >   _dcolor;
  vector< Int_t   >   _dndigit;

  TString _dfirstError ;
  TString _dsecondError;

  // MC points
  vector< TString > _entry;
  vector< Float_t >   _val;
  vector< Float_t >   _dpsup;
  vector< Float_t >   _pdfup;
  vector< Float_t >   _dpslo;
  vector< Float_t >   _pdflo;
  vector< Float_t >   _lumi;
  vector< Int_t   >   _marker;
  vector< Float_t >   _size;
  vector< Int_t   >   _color;
  vector< Int_t   >   _ndigit;

  TString _unit;

  size_t _n;
  Double_t _t;
  Double_t _b;
  Double_t _g;
  Double_t _d;
  Double_t _h;
  Double_t _w;  
  Double_t _W;
  Double_t _H;

  bool       _addArxivRef;
  TString    _textArxivRef;
  float      _xa,         _ya;
  float      _sizeRef;

  bool _band;
  Double_t _bx0;
  Double_t _bxmin;
  Double_t _bxmax;

  bool _innerband;
  Double_t _ibxmin;
  Double_t _ibxmax;

  bool _middleband;
  Double_t _mbxmin;
  Double_t _mbxmax;


  bool _colorLegend;


  float _x0;
  float _y0;

  float _dx;
  float _dy;
    
  bool _hasLegend;
  TString _legend;
  TString _theory;
  TString _theory2;

  TString _labelOuterBand, _labelInnerBand, _labelMiddleBand;

  double _intLumi;

  TString _txtLeft;
  TString _txtCenter;
  TString _txtRight;
  double _txtY;

  float _eps1;
  float _eps2;

  float _upDy;

  TString _firstError;
  TString _secondError;
  TString _thirdError;

  float e_;
  float E_;				

  bool _specifyPlacement;
  float _xx1, _xx2;
  float _e1, _e2;
  int _align1, _align2;
  float _size1, _size2;

  bool _centerTitle;
  
  int _bandFillStyle;
  int _bandFillColor;
  int _bandLineWidth;
  int _bandLineColor;


  int _middlebandFillStyle;
  int _middlebandFillColor;
  int _middlebandLineWidth;
  int _middlebandLineColor;


  int _innerbandFillStyle;
  int _innerbandFillColor;
  int _innerbandLineWidth;
  int _innerbandLineColor;



  bool _extraBand;
  float _xmin2, _xmax2;
  float _ymin2, _ymax2;

  bool _logX;
  bool _writeText;
  bool _cmsPrelim;
  //
  
  LEPStyle( const char* name, const char* title,
	    float xmin, float xmax, int ndivx=510, const char* unit=0 );
  ~LEPStyle() {}
 
  void addArxivReference(const char* TEXT, float a, float b, float sizeRef);
 
 
//  void addEntry( const char* entry=0, 
//		 float val=0, float stat=0, float syst=0, float lumi=0, 
//		 int marker=20, float size=1, int color=kBlack,
//		 int ndigit=3 );  
//  void addEntry( const char* entry, 
//		 float val, float stat, 
//		 float systexp, float systtheo, float lumi, 
//		 int marker=20, float size=1, int color=kBlack,
//		 int ndigit=3 );  
  void addEntry( const char* entry,
                 float val, 
                 float systPDF, float systDPS, TString statLabel, TString sysLabel,
                 int marker=20, float size=1, int color=kBlack,
                 int ndigit=3 );  

  void addData( const char* entry,
                 float val, 
                 float uncStat, float uncSyst, float uncTheo, float uncLumi,
                 int marker=20, float size=1, int color=kBlack,
                 int ndigit=3 );  

//  void addEntry( const char* entry,
//                 float val,
//                 float systPDF, float systPDFUp, float systDPS, TString statLabel, TString sysLabel,
//                 int marker=20, float size=1, int color=kBlack,
//                 int ndigit=2 );
//  void addEntry( const char* entry, 
//		 float val, 
//		 float statup, float statlo, 
//		 float systup, float systlo, 
//                 float lumi,
//                 TString statLabel, TString sysLabel, TString lumiLabel,
//		 int marker=20, float size=1, int color=kBlack,
//		 int ndigit=3 );  
  void setTheoryBandAndLegend( float val, float dminus, float dplus,
			       const char* legend=0, 
			       int nblk1=0, int nblk2=0 );

  void setCMSMeasurement( float val, float stat, float sys,
                               const char* legend=0,int ndecimals=2,
                               int nblk1=0, int nblk2=0 );

  void setCMSMeasurement2( float val, float stat, float syst, float theo, float lumi,
                               const char* legend=0,int ndecimals=2,
                               int nblk1=0, int nblk2=0 );

  void addColorLegend(const char* bandColorA, const char* bandColorB);
  void addColorLegend2(const char* bandColorA, const char* bandColorB, const char* bandColorC);

  void addText( const char* txt, float x1, float y1, int align, float size,
		float angle=0, int color=0 );
  void setHist();
  void setCanvas();  
  void clear();
  void draw();
  TPolyLine* drawExtraBand(const char* opt="FSame");
  void cmsPrelim( double lumi );
  void print(); 
};

LEPStyle::LEPStyle( const char* name, const char* title, float xmin, float xmax, int ndivx, const char* unit ) 
  : _name(name), _title(title), 
    _canv(0), _xmin(xmin), _xmax(xmax), _ymin(0), _ymax(0), 
    _ndivx(ndivx),
    _hist(0), _ax(0), _ay(0),
    _band(false),_innerband(false), _colorLegend(false),
    _t(40), _b(70), _g(42), _d(42), _h(140), _w(700),
    _x0(0), _y0(0), _dx(0), _dy(0),
    _intLumi(2.88), /*_txtLeft("CMS")*/_txtLeft(""), _txtCenter(""), 
    _txtRight("#sqrt{s} = 7 TeV"), _txtY(0.95), _eps1(0.005), _eps2(0.20),
    _upDy(1.5), _firstError("PDF"), _secondError("syst"), _thirdError("lumi"),
    e_(0.05), E_(-0.1), 
    _specifyPlacement(false), 
    _xx1(0), _xx2(0), _e1(0), _e2(0), _align1(11), _align2(13),
    _size1(0.07), _size2(0.05),
    _centerTitle(false),
    _bandFillStyle(1001), _bandFillColor(kYellow-7),
    _bandLineWidth(3), _bandLineColor(kOrange),
    _innerbandFillStyle(1001), //_innerbandFillColor(kRed),
    _innerbandFillStyle(1001), //_innerbandFillColor(kViolet),
    _innerbandLineWidth(1), //_innerbandLineColor(_innerbandFillColor),
    _middlebandFillStyle(1001), //_middlebandFillColor(kViolet),
    _middlebandLineWidth(1), //_middlebandLineColor(_middlebandFillColor),
    _extraBand(false), _xmin2(0), _xmax2(0), _ymin2(0), _ymax2(0), 
    _logX(false), _writeText(true), _cmsPrelim(true),
    _labelOuterBand(""), _labelInnerBand(""),_labelMiddleBand(""),
    _addArxivRef(false),_textArxivRef("")
{
  if( unit!=0 )
    {
      _unit = " ";
      _unit += unit;
    }
}

void LEPStyle::setHist()
{
  _hist = new TH1F( "bidon", "bidon", 100, _xmin, _xmax );
  
  _ax = _hist->GetXaxis();
  _ay = _hist->GetYaxis();

  _ax->SetTitle(_title);
  _ax->SetNdivisions(_ndivx);

  if( _logX )
    {
      _ax->SetMoreLogLabels();
    }

  _ax->SetLabelSize(_scale*0.060);
  //  _ax->SetLabelOffset(_scale*0.007);
  _ax->SetTitleSize(_scale*0.070);
  _ax->SetTitleOffset(0.9);
  _ax->CenterTitle( _centerTitle );

  _ay->SetNdivisions(0);

}

void LEPStyle::setCanvas()
{
  delete _canv;

  _n = _entry.size();

  //  _t = 40;
  //  _b = 70;
  //  _g = 42;
  //  _d = 42;
  //  _h = 130;
  //  _h = 100;
  //  _w = 700;
  
  _W = _g + _w + _d;
  _H = _t + _n*_h + _b ;
  //GHM  _H = _t + (_n+1)*_h + _b ;

  _scale = 400./_H;

  cout << "W/H= " << _W << "/" << _H << endl; 

  _canv=new TCanvas( _name, _title, 0, 0, _W, _H );  
  _canv->SetLeftMargin(  _g/_W );
  _canv->SetRightMargin( _d/_W );
  _canv->SetTopMargin(  _t/_H );
  _canv->SetBottomMargin( _b/_H ); 
  _canv->SetFillColor(0);
  _canv->SetTickx(1);
  _canv->SetTicky(1);
  if( _logX ) 
    {
      _canv->SetLogx();
      _canv->SetGridx();
    }
  _canv->SetFrameFillStyle(0);
  _canv->SetFrameLineWidth(2);
  _canv->SetFrameBorderMode(0);

  gStyle->SetTickLength( 1.2*gStyle->GetTickLength("X")*_scale, "X" );
  //  gStyle->SetEndErrorSize(5*_scale);
  gStyle->SetEndErrorSize(10*_scale);
}

void
LEPStyle::setCMSMeasurement( float val, float stat, float sys,
                                  const char* legend, int ndecimals,
                                  int nblk1, int nblk2 )
{
  _band = true;
  _innerband=true;
  _bx0 = val;
  _bxmin = _bx0-sqrt(stat*stat+sys*sys);
  _bxmax = _bx0+sqrt(stat*stat+sys*sys);
  _ibxmin = _bx0-stat;
  _ibxmax = _bx0+stat;

   _innerbandFillColor=kYellow;
   _bandFillColor=kOrange;

  _hasLegend = false;
  if( legend!=0 )
    {
      _hasLegend = true;

      _legend = " ";
      _legend += legend;

      _theory = "";
      for( int ii=0; ii<nblk1; ii++ ) _theory += " ";
      char line_[512];
      if(ndecimals==3) sprintf( line_, "%-4.3f #pm %-4.3f (stat) #pm %-4.3f (sys)",_bx0,stat,sys);
	else sprintf( line_, "%-4.2f #pm %-4.2f (stat) #pm %-4.2f (sys)",_bx0,stat,sys);
      _theory += line_;
      _theory += _unit;
      for( int ii=0; ii<nblk2; ii++ ) _theory += " ";
    }

}


void
LEPStyle::setCMSMeasurement2( float val, float stat, float syst, float theo, float lumi,
                                  const char* legend, int ndecimals,
                                  int nblk1, int nblk2 )
{
  _band = true;
  _middleband=true;
  _innerband=true;
  _bx0 = val;
  //_bxmin = _bx0-sqrt(stat*stat+sys*sys+sys2*sys2);
  //_bxmax = _bx0+sqrt(stat*stat+sys*sys+sys2*sys2);
  //_mbxmin = _bx0-sqrt(stat*stat+sys*sys);
  //_mbxmax = _bx0+sqrt(stat*stat+sys*sys);
  //_ibxmin = _bx0-stat;
  //_ibxmax = _bx0+stat;

   _innerbandFillColor=kYellow;
   _bandFillColor=kOrange;
   _middlebandFillColor=kOrange-3;

  _hasLegend = false;
  if( legend!=0 )
    {
      _hasLegend = true;

      _legend = " ";
      _legend += legend;

//      _theory = "";
//      for( int ii=0; ii<nblk1; ii++ ) _theory += " ";
//      char line_[512];
//      if(ndecimals==3) sprintf( line_, "%-4.3f #pm %-4.3f (stat) #pm %-4.3f (syst) #pm %-4.3f (theo)  #pm %-4.3f (lumi) pb",_bx0,stat,syst,theo,lumi);
//       else  sprintf( line_, "%-4.2f #pm %-4.2f (stat) #pm %-4.2f (syst) #pm %-4.2f (theo)  #pm %-4.2f (lumi) pb",_bx0,stat,syst,theo,lumi);
//      _theory += line_;
//      _theory += _unit;
//      for( int ii=0; ii<nblk2; ii++ ) _theory += " ";
//


      _theory = "";
      _theory2 = "";
      for( int ii=0; ii<nblk1; ii++ ) _theory += " ";
      for( int ii=0; ii<nblk1; ii++ ) _theory2 += " ";
      char line_[512];
      char line2_[512];
      if(ndecimals==3) sprintf( line_, "%-4.3f #pm %-4.3f (stat) #pm %-4.3f (syst)",_bx0,stat,syst);
       else  sprintf( line_, "%-4.2f #pm %-4.2f (stat) #pm %-4.2f (syst)",_bx0,stat,syst);
      if(ndecimals==3) sprintf( line2_, "#pm %-4.3f (theo) #pm %-4.3f (lumi) pb",theo,lumi);
       else  sprintf( line2_, "#pm %-4.2f (theo) #pm %-4.2f (lumi) pb",theo,lumi);
      _theory += line_;
      _theory2 += line2_;
      for( int ii=0; ii<nblk2; ii++ ) _theory += " ";
    }

}

void LEPStyle::addArxivReference(const char* TEXT, float a, float b, float sizeRef){
	_addArxivRef=true;
	_textArxivRef=TEXT;
	_xa=a;
	_ya=b;
	_sizeRef=sizeRef;

}
void LEPStyle::addColorLegend(const char* bandColorA, const char* bandColorB){
   _innerbandFillColor=kYellow;
   _bandFillColor=kOrange;
   _labelOuterBand=bandColorA;
    _labelInnerBand=bandColorB;
   _colorLegend=true;

}

void LEPStyle::addColorLegend2(const char* bandColorA, const char* bandColorB, const char* bandColorC){
   _innerbandFillColor=kYellow;
   _bandFillColor=kOrange;
   _middlebandFillColor=kOrange-3;
   _labelOuterBand=bandColorA;
    _labelInnerBand=bandColorB;
    _labelMiddleBand=bandColorC;
   _colorLegend=true;

}


void 
LEPStyle::setTheoryBandAndLegend( float val, float dminus, float dplus,
				  const char* legend, 
				  int nblk1, int nblk2 )  
{
  _band = true;
  _bx0 = val;
  _bxmin = _bx0-dminus;
  _bxmax = _bx0+dplus;

  _hasLegend = false;
  if( legend!=0 )
    {
      _hasLegend = true;

      _legend = " ";
      _legend += legend;
      
      _theory = "";
      for( int ii=0; ii<nblk1; ii++ ) _theory += " ";
      char line_[512];
      sprintf( line_, "%-4.2f #pm %-4.2f",_bx0,0.5*(dminus+dplus) );
      _theory += line_;
      _theory += _unit;
      for( int ii=0; ii<nblk2; ii++ ) _theory += " ";
    }

}

void LEPStyle::draw()
{
  if( _canv==0 )
    {
      setCanvas();
      setHist();
      _canv->Draw();
      if( _ymin==0 ) _ymin = 0.2;
      //  _ymax = _n*1.5; 
      if( _ymax==0 ) _ymax = _n+_upDy;
      _hist->SetMinimum( _ymin  );
      _hist->SetMaximum( _ymax );
      
      _hist->Draw();

      if( _cmsPrelim ) cmsPrelim( _intLumi );
    }

  //  size_t n_ = _entry.size();
  _n = _entry.size();
  if( _extraBand )
    {
      drawExtraBand();
    }




  if( _band )
    {
      Double_t xx_[5] = { _bxmin, _bxmax, _bxmax, _bxmin, _bxmin };
      float eps1_ = _eps1*(_ymax-_ymin);
      float eps2_ = _eps2*(_ymax-_ymin);
      Double_t yy_[5] = { _ymin+eps1_, _ymin+eps1_, _ymax-eps2_, _ymax-eps2_, _ymin+eps1_ };
      TPolyLine* pl_ = new TPolyLine( 5, xx_, yy_ );
      pl_->SetFillStyle(_bandFillStyle);
      pl_->SetFillColor(_bandFillColor);
      pl_->SetLineWidth(3);
      pl_->SetLineColor( kOrange );
      //pl_->DrawClone("FSame");

	TPolyLine* pl3_, *pl2_ ;

         if(_middleband){
         Double_t mxx_[5] = { _mbxmin, _mbxmax, _mbxmax, _mbxmin, _mbxmin };
        pl3_ = new TPolyLine( 5, mxx_, yy_ );
        pl3_->SetFillStyle(_middlebandFillStyle);
        pl3_->SetFillColor(_middlebandFillColor);
        pl3_->SetLineWidth(3);
        pl3_->SetLineColor( _middlebandFillColor );
        //pl3_->DrawClone("FSame");
	}


      if(_innerband){
         Double_t ixx_[5] = { _ibxmin, _ibxmax, _ibxmax, _ibxmin, _ibxmin };
      	pl2_ = new TPolyLine( 5, ixx_, yy_ );
      	pl2_->SetFillStyle(_innerbandFillStyle);
      	pl2_->SetFillColor(_innerbandFillColor);
      	pl2_->SetLineWidth(3);
      	pl2_->SetLineColor( _innerbandFillColor );
      	//pl2_->DrawClone("FSame");

      }

        if(_colorLegend){
         TLegend *legColor = new TLegend(0.08,0.75,0.4,0.9,NULL,"brNDC");
        legColor->SetLineColor(0);
        legColor->SetDrawOption(0);
        legColor->SetFillColor(0);
        legColor->SetBorderSize(0);

        TLegendEntry *entry=legColor->AddEntry(pl_,_labelOuterBand,"F");
        entry->SetFillColor(_bandFillColor);
        if(_middleband){  TLegendEntry *entry2=legColor->AddEntry(pl3_,_labelMiddleBand,"F");
        entry2->SetFillColor(_middlebandFillColor);}
        if(_innerband){
         TLegendEntry *entry3=legColor->AddEntry(pl2_,_labelInnerBand,"F");
        entry3->SetFillColor(_innerbandFillColor);
        }
        legColor->Draw();

        }


//      TLine* l_ = new TLine( _bx0, _ymin+eps1_, _bx0, _ymax-eps2_  );
//      l_->SetLineWidth(4);
//      l_->SetLineColor( kViolet );
//      l_->DrawClone();




      if( _hasLegend )
	{

	  //      _y0 = 4.0;
	  if( _y0==0 ) _y0 = _n+2*_upDy/3.;
	  if( _dy==0 ) _dy = 0.06;
	  _x0 = _xmax - 0.05*(_xmax-_xmin);
	  
	  TLatex leg1_;
	  leg1_.SetTextSize(_scale*0.08);      
	  leg1_.SetTextAlign(23); 
	  leg1_.DrawLatex( _bx0, _y0-_dy+0.35, _legend );
	  //leg1_.DrawLatex( _bx0, _y0-_dy+0.25, _legend );
	  
	  
	  TLatex leg2_;
	  leg2_.SetTextSize(_scale*0.05);      
	  leg2_.SetTextAlign(23); 
	  leg2_.DrawLatex( _bx0, _y0-_dy, _theory );

	  TLatex leg3_;
	  leg3_.SetTextSize(_scale*0.05);      
	  leg3_.SetTextAlign(23); 
	  leg3_.DrawLatex( _bx0, _y0-_dy-0.25, _theory2 );


	}

//       TLegend* legend=new TLegend(_x0,_y0, _x0+_dx, _y0+_dy );
//       legend->SetLineColor(0);
//       legend->SetFillColor(0);
      
//       //      legend->AddEntry(pl_,_legend,"lf");
//       legend->AddEntry(pl_,_legend,"");

//       legend->Draw("same");
      

    }


  // Draw MC points
  for( size_t ii=0; ii<_entry.size(); ii++ )
    {
      if( _entry[ii]==("SPACE") ) continue;
      Float_t xval_[1];
      Float_t yval_[1];
      Float_t ey_[1];
      Float_t epdfup_[1];
      Float_t epdflo_[1];
      Float_t edpsup_[1];
      Float_t edpslo_[1];
      Float_t etotup_[1];
      Float_t etotlo_[1];
      Float_t ectlup_[1];
      Float_t ectllo_[1];


      Float_t estatup_[1];
      Float_t ecombup_[1];
      Float_t ecomblo_[1];
      Float_t estatlo_[1];

      Double_t yyv2_ = (Double_t)_n-(Float_t)ii;
      //Double_t yy_[5] = { _ymin+eps1_, _ymin+eps1_, _ymax-eps2_, _ymax-eps2_, _ymin+eps1_ };
      //yy_[ii] = (Double_t)_n-(Double_t)ii;
      //float yy_ = _n-(Float_t)ii;
      //yy_ = _n-(Float_t)ii;
      //yy_ = (float)_n-(float)ii;
      xval_[0] = _val[ii];
      yval_[0] = yyv2_;
      ey_[0] = 0.2;

      ectllo_[0] = 0.001;
      ectlup_[0] = 0.001;
      epdfup_[0] = _pdfup[ii];
      epdflo_[0] = _pdflo[ii];
      edpsup_[0] = _dpsup[ii];
      edpslo_[0] = _dpslo[ii];
      etotup_[0] = sqrt( pow( _pdfup[ii],2 ) + pow( _dpsup[ii],2 ) );
      etotlo_[0] = sqrt( pow( _pdflo[ii],2 ) + pow( _dpslo[ii],2 ) );      

      //estatup_[0] = _statup[ii];
      //etotup_[0] = ecombup_[0] + _lumi[ii];

      //estatlo_[0] = _statlo[ii];
      //etotlo_[0] = ecomblo_[0] + _lumi[ii];

      TGraphAsymmErrors* gtot_ = new TGraphAsymmErrors( 1, xval_, yval_, etotlo_, etotup_, ey_, ey_ );
      TGraphAsymmErrors* gctl_ = new TGraphAsymmErrors( 1, xval_, yval_, ectllo_, ectlup_, ey_, ey_ );
      TGraphAsymmErrors* gpdf_ = new TGraphAsymmErrors( 1, xval_, yval_, epdflo_, epdfup_, ey_, ey_ );
      TGraphAsymmErrors* gdps_ = new TGraphAsymmErrors( 1, xval_, yval_, edpslo_, edpsup_, ey_, ey_ );

      gtot_->SetLineColor( kOrange   );
      gtot_->SetFillColor( kOrange   );
      gpdf_->SetLineColor( kOrange-3 );
      gpdf_->SetFillColor( kOrange-3 );
      gdps_->SetLineColor( kYellow   );
      gdps_->SetFillColor( kYellow   );
      gctl_->SetLineColor( kViolet   );
      gctl_->SetFillColor( kViolet   );
      //gcomb_->SetLineColor( kBlack );


//      gstat_->SetLineColor( kBlue );
//      gstat_->SetLineWidth( 2 );
//      gstat_->SetMarkerStyle( _marker[ii] );
//      gstat_->SetMarkerSize( _size[ii] );
//      gstat_->SetMarkerColor( _color[ii] );
//
//
//  kYellow
//  kOrange
//  kOrange-3
//
//      gcomb_->SetLineWidth( 2 );

      gtot_->SetLineWidth( 2 );


   gtot_->Draw("2,sames");
   gdps_->Draw("2,sames");
   gpdf_->Draw("2,sames");
   gctl_->Draw("2,sames");

//   //gtot_->SetFillColor(2);
//   gtot_->SetFillStyle(1001);
//	gtot_->Draw("P2,sames");
   //gtot_->Draw("a2,sames");
   //gtot_->Draw("p,sames");


//      if( _lumi[ii]>0 )
//	gtot_->Draw("P");
//
//      gcomb_->DrawClone();
//      //gstat_->DrawClone("a4");



      if( !_writeText ) continue;

      //   align = 10*HorizontalAlign + VerticalAlign
      // For Horizontal alignment the following convention applies:
      //   1=left adjusted, 2=centered, 3=right adjusted
      // For Vertical alignment the following convention applies:
      //   1=bottom adjusted, 2=centered, 3=top adjusted
      float xtxt_ = _xmin + 0.05*(_xmax-_xmin);
      TLatex ltx1_;

	TMarker a;
	a.SetMarkerStyle(_marker[ii]);	
        a.SetMarkerSize(_size[ii]);
	//a.DrawMarker(xtxt_-0.01*(_xmax-_xmin), yyv2_);

      ltx1_.SetTextSize(_scale*_size1);      
      ltx1_.SetTextAlign(_align1);
      if( _specifyPlacement )
	ltx1_.DrawLatex( _xx1+0.005, yyv2_+_e1, _entry[ii] );
      else
	ltx1_.DrawLatex( xtxt_+0.005*(_xmax-_xmin), yyv2_+E_+e_, _entry[ii] );

      TLatex ltx2_;

      char line_[512];

      TString str_;
      TString pmstr_;
      pmstr_ = " #pm  ";
//      TString pmstr_(" #pm ");
      TString format_;
      format_ = "%-4.";
      format_ += _ndigit[ii];
      format_ += "f";
      TString valstr_;
      TString statstr_;
      TString syststr_;
      TString lumistr_;

//      sprintf( line_, format_.Data(), _val[ii] );
       sprintf( line_,  "%-4.2f", _val[ii] );
      valstr_ = line_;

      if( fabs( _pdfup[ii]-_pdflo[ii] )<0.001 )
	{
	  sprintf( line_, format_.Data(), _pdflo[ii] );
	}
      else
	{
	  sprintf( line_, "#scale[0.7]{#splitline{+%-4.2f}{-%-4.2f}}", _pdfup[ii], _pdflo[ii] );
	}

      if( _firstError=="")  _firstError="PDF";

      statstr_ = line_;
      str_ = valstr_ + pmstr_ + statstr_;
      str_ += "_{ ";
      str_ +=  _firstError;
      str_ += "}";

      if( _dpsup[ii]>0 )
	{
	  if( fabs( _dpsup[ii]-_dpslo[ii] )<0.01 )
	    {
	      sprintf( line_, format_.Data(), _dpslo[ii] );
	    }
	  else 
	    {
	      sprintf( line_, "#scale[0.7]{#splitline{+%-4.2f}{- %-4.2f}}_", _dpsup[ii], _dpslo[ii] );
	    }
	  syststr_ = line_;
	  str_ += pmstr_;
	  str_ += syststr_;
	  str_ += "_{ ";
	  str_ += _secondError;
	  str_ += "}";
	}
        str_+= "  pb";
  
      if( _lumi[ii]>0 )
	{
	  sprintf( line_, format_.Data(), _lumi[ii] );
	  lumistr_ = line_;
	  lumistr_ += "_{lumi}";
	  str_ += pmstr_ + lumistr_;
	}

      //      TString str_(line_);
      
      str_ += _unit;
      cout << str_ << endl;
 
      ltx2_.SetTextSize(_scale*_size2);      
      ltx2_.SetTextAlign(_align2);
      if( _specifyPlacement )
	ltx2_.DrawLatex( _xx2, yyv2_+_e2, str_ );
      else
	ltx2_.DrawLatex( xtxt_+0.02*(_xmax-_xmin), yyv2_+E_-e_, str_ );
    }

  /// Draw Data Points 
  for( size_t ii=0; ii<_dentry.size(); ii++ )
    {
      if( _entry[ii]==("SPACE") ) continue;
      Float_t  xval_[1];
      Float_t  yval_[1];
      Float_t    ey_[1];
      Float_t estatup_[1];
      Float_t esystup_[1];
      Float_t etheoup_[1];
      Float_t elumiup_[1];
      Float_t etotup_[1];
      Float_t ecombup_[1]; //
      Float_t estatlo_[1];
      Float_t esystlo_[1];
      Float_t etheolo_[1];
      Float_t elumilo_[1];
      Float_t etotlo_[1];

      Double_t yyv2_ = (Double_t)_n-(Float_t)ii;
      //Double_t yy_[5] = { _ymin+eps1_, _ymin+eps1_, _ymax-eps2_, _ymax-eps2_, _ymin+eps1_ };
      //yy_[ii] = (Double_t)_n-(Double_t)ii;
      //float yy_ = _n-(Float_t)ii;
      //yy_ = _n-(Float_t)ii;
      //yy_ = (float)_n-(float)ii;
      xval_[0] = _dval[ii];
      yval_[0] = yyv2_;
      ey_[0] = 0;

      // stat, sys, theo, lumi
      estatup_[0] = _dstatup[ii];
      esystup_[0] = _dsystup[ii];
      etheoup_[0] = _dtheoup[ii];
      elumiup_[0] = _dlumi[ii];
      etotup_[0] = sqrt( pow(_dstatup[ii],2) + pow(_dsystup[ii],2) + pow(_dtheoup[ii],2) + pow(_dlumi[ii],2) );
  
      estatlo_[0] = _dstatlo[ii];
      esystlo_[0] = _dsystlo[ii];
      etheolo_[0] = _dtheolo[ii];
      elumilo_[0] = _dlumi[ii];
      etotlo_[0] = sqrt( pow(_dstatlo[ii],2) + pow(_dsystlo[ii],2) + pow(_dtheolo[ii],2) + pow(_dlumi[ii],2) );
  

      //ecombup_[0] = sqrt( pow( _dstatup[ii],2 ) + pow( _dsystup[ii],2 ) );
      //etotup_[0] = ecombup_[0] + _dlumi[ii];

      //estatlo_[0] = _dstatlo[ii];
      //ecomblo_[0] = sqrt( pow( _dstatlo[ii],2 ) + pow( _dsystlo[ii],2 ) );      
      //etotlo_[0] = ecomblo_[0] + _dlumi[ii];

      TGraphAsymmErrors* dgstat_ = new TGraphAsymmErrors( 1, xval_, yval_, estatlo_, estatup_, ey_, ey_ );
      TGraphAsymmErrors* dgsyst_ = new TGraphAsymmErrors( 1, xval_, yval_, esystlo_, esystup_, ey_, ey_ );
      TGraphAsymmErrors* dgtheo_ = new TGraphAsymmErrors( 1, xval_, yval_, etheolo_, etheoup_, ey_, ey_ );
      TGraphAsymmErrors* dglumi_ = new TGraphAsymmErrors( 1, xval_, yval_, elumilo_, elumiup_, ey_, ey_ );
      TGraphAsymmErrors* dgtot_ = new TGraphAsymmErrors( 1, xval_, yval_, etotlo_, etotup_, ey_, ey_ );


      //TGraphAsymmErrors* gtot_  = new TGraphAsymmErrors( 1, xval_, yval_, etotlo_, etotup_, ey_, ey_ );
      //TGraphAsymmErrors* gcomb_ = new TGraphAsymmErrors( 1, xval_, yval_, ecomblo_, ecombup_, ey_, ey_ );

      dgtot_->SetMarkerStyle( _marker[ii] );
      dgtot_->SetMarkerSize( _size[ii] );
      dgtot_->SetMarkerColor( _color[ii] );

      dgtot_->SetLineColor( kBlack );
      dgstat_->SetLineColor( kGreen-1 );
      dgsyst_->SetLineColor( kGreen+2 );
      dgtheo_->SetLineColor( kBlue );
      dglumi_->SetLineColor( kCyan+1 );

      dgtot_ ->SetLineWidth( 2 );
      dgstat_->SetLineWidth( 2 );
      dgsyst_->SetLineWidth( 2 );
      dgtheo_->SetLineWidth( 2 );
      dglumi_->SetLineWidth( 2 );

      dgtot_->Draw("P");
      dgsyst_->Draw();
      dgtheo_->Draw();
      dgstat_->Draw();
      dglumi_->Draw();

      //gcomb_->DrawClone();
      //gstat_->DrawClone("p");

    }


  if(_addArxivRef){
      TLatex ltxREF_;
      ltxREF_.SetTextSize(_sizeRef);
	ltxREF_.SetTextColor(kBlue);
	        ltxREF_.DrawLatex( _xa*(_xmax-_xmin), _ya, _textArxivRef);
   }

  _hist->Draw("Same");

  _canv->RedrawAxis();
}

void LEPStyle::print() 
{ 
  if( _canv!=0 ) {_canv->Print(".png"); _canv->Print(".eps"); _canv->Print(".pdf"); }
}

//void LEPStyle::addEntry( const char* entry, 
//			 float val, float stat, float syst, 
//			 float lumi, 
//			 int marker, float size, int color, int ndigit )
//{
//  if( entry==0 )
//    {
//      entry = "SPACE";
//    }
//  _entry.push_back( entry );
//  _val.push_back( val );
//  _statup.push_back( stat );
//  _systup.push_back( syst );
//  _statlo.push_back( stat );
//  _systlo.push_back( syst );
//  _lumi.push_back( lumi );
//  _marker.push_back( marker );
//  _size.push_back( size );
//  _color.push_back( color );
//  _ndigit.push_back( ndigit );
//}
//
//void LEPStyle::addEntry( const char* entry, 
//			 float val, 
//			 float statup, float statlo, 
//			 float systup, float systlo,
//                         float lumi,
//			 TString statLabel, TString sysLabel, TString lumiLabel,
//			 int marker, float size, int color, int ndigit )
//{
//  if( entry==0 )
//    {
//      entry = "SPACE";
//    }
//  _entry.push_back( entry );
//  _val.push_back( val );
//  _statup.push_back( statup );
//  _systup.push_back( systup );
//  _statlo.push_back( statlo );
//  _systlo.push_back( systlo );
//  _firstError =statLabel ;
//  _secondError =sysLabel ;
//  _thirdError =lumiLabel ;
//  _lumi.push_back( lumi );
//  _marker.push_back( marker );
//  _size.push_back( size );
//  _color.push_back( color );
//  _ndigit.push_back( ndigit );
//}
//
//void LEPStyle::addEntry( const char* entry, 
//			 float val, 
//			 float stat, 
//			 float systexp, float systtheo,
//			 float lumi, 
//			 int marker, float size, int color, int ndigit )
//{
//  if( entry==0 )
//    {
//      entry = "SPACE";
//    }
//  float syst = sqrt( pow(systexp,2)+pow(systtheo,2) );
//  _entry.push_back( entry );
//  _val.push_back( val );
//  _statup.push_back( stat );
//  _systup.push_back( syst );
//  _statlo.push_back( stat );
//  _systlo.push_back( syst );
//  _lumi.push_back( lumi );
//  _marker.push_back( marker );
//  _size.push_back( size );
//  _color.push_back( color );
//  _ndigit.push_back( ndigit );
//}

void LEPStyle::addData( const char* entry,
                         float val,
                         float uncStat, float uncSyst, float uncTheo, float uncLumi,
                         int marker, float size, int color, int ndigit )
{
  if( entry==0 )
    {
      entry = "SPACE";
    }
  _dentry.push_back( entry );
  _dval.push_back( val );
  _dstatup.push_back( uncStat );
  _dstatlo.push_back( uncStat );
  _dsystup.push_back( uncSyst );
  _dsystlo.push_back( uncSyst );
  _dtheoup.push_back( uncTheo );
  _dtheolo.push_back( uncTheo );
  _dlumi.push_back( uncLumi );
  _dmarker.push_back( marker );
  _dsize.push_back( size );
  _dcolor.push_back( color );
  _dndigit.push_back( ndigit );
}

void LEPStyle::addEntry( const char* entry,
                         float val,
                 float systPDF, float systDPS, TString pdfLabel, TString sysLabelDPS,
                         int marker, float size, int color, int ndigit )
{
  if( entry==0 )
    {
      entry = "SPACE";
    }
  _entry.push_back( entry );
  _val.push_back( val );
  _pdfup.push_back( systPDF );
  _dpsup.push_back( systDPS );
  _pdflo.push_back( systPDF );
  _dpslo.push_back( systDPS );
  _firstError =pdfLabel;
  _secondError =sysLabelDPS ;
  _lumi.push_back( 0 );
  _marker.push_back( marker );
  _size.push_back( size );
  _color.push_back( color );
  _ndigit.push_back( ndigit );
}


//void LEPStyle::addEntry( const char* entry,
//                         float val,
//                 float systPDF, float systPDFUp, float systDPS, TString pdfLabel, TString sysLabelDPS,
//                         int marker, float size, int color, int ndigit )
//{
//  if( entry==0 )
//    {
//      entry = "SPACE";
//    }
//  _entry.push_back( entry );
//  _val.push_back( val );
//  _statup.push_back( systPDFUp );
//  _systup.push_back(  systDPS );
//  _statlo.push_back( systPDF );
//  _systlo.push_back( systDPS );
//  _firstError =pdfLabel;
//  _secondError =sysLabelDPS ;
//  _lumi.push_back( 0 );
//  _marker.push_back( marker );
//  _size.push_back( size );
//  _color.push_back( color );
//  _ndigit.push_back( 3 );
//}

void
LEPStyle::addText( const char* txt, float x1, float y1, int align, float size,
		   float angle, int color )
{
  std::cout << txt << std::endl;
	  
  TLatex leg1_;
  leg1_.SetTextSize( size );      
  leg1_.SetTextAlign( align ); 
  leg1_.SetTextAngle( angle ); 
  leg1_.SetTextAngle( angle ); 
  leg1_.SetTextColor( color ); 
  leg1_.DrawLatex( x1, y1, txt );
}

TPolyLine*
LEPStyle::drawExtraBand( const char* opt )
{
  Double_t xx_[5] = { _xmin2, _xmax2, _xmax2, _xmin2, _xmin2 };
  Double_t yy_[5] = { _ymin2, _ymin2, _ymax2, _ymax2, _ymin2 };
  TPolyLine* pl_ = new TPolyLine( 5, xx_, yy_ );
  pl_->SetFillColor(_bandFillColor);
  pl_->SetFillStyle(_bandFillStyle);
  pl_->SetLineWidth(_bandLineWidth);
  pl_->SetLineColor(_bandLineColor);
  pl_->SetLineStyle(kSolid);
  pl_->DrawClone(opt);
  return pl_;
}

void
LEPStyle::clear()
{
  _entry.clear();
  _val.clear();
  _statup.clear();
  _systup.clear();
  _statlo.clear();
  _systlo.clear();
  _lumi.clear();
  _marker.clear();
  _size.clear();
  _color.clear();
  _ndigit.clear();
}

void 
LEPStyle::cmsPrelim( double intLumi )
{
  TLatex latex;
  latex.SetNDC();
  latex.SetTextSize(_scale*0.055);

  latex.SetTextAlign(31); // align right
  latex.DrawLatex(1-_d/_W,_txtY,_txtRight);
  if (intLumi > 0.) {
    latex.SetTextAlign(11); // align right
    latex.DrawLatex(2.5*_g/_W,0.80,Form("#int #font[12]{L} dt = %.1f pb^{-1}",intLumi));
  }
  latex.SetTextAlign(11); // align left
  latex.DrawLatex(_g/_W,_txtY,_txtLeft);

  //  latex.SetTextAlign(01);
  //  latex.DrawLatex(0.5,_txtY,_txtCenter);  
}

