/*
 *  MuNuPlot.h
 *
 *  Created by Isobel Ojalvo on 3/29/12.
 *  University of Wisconsin Madison
 *
loop through background 
plot signal on top
Options--> cuts at top, cuts at command line? 
labels, separate area?

*/
#include <iostream>
#include <cmath>
#include "TLegend.h"
#include "TFile.h"
#include "TROOT.h"
#include "TCanvas.h"
#include "TPad.h"
#include "TLatex.h"
#include "TH1.h"
#include "TH1F.h"
#include "TH2.h"
#include "TF1.h"
#include "THStack.h"
#include "TStyle.h"
#include "TAxis.h"
#include "TGaxis.h"
#include "TTree.h"
#include "TPaveText.h"
#include "tdrstyle.C"
#include "TStyle.h"
#include "TMath.h"

using namespace std;

TFile *shfile;

TH1F * createhist(TString name,TString var,TString file,TString dir,Color_t color,TString weight,bool data,TString cuts,int bins,double lo,double hi);
THStack * addFunc(TH1F *first, TH1F *second, TH1F *third, TH1F *fourth, TH1F *fifth, TH1F *sixth, TH1F *seventh, TH1F *eighth, TH1F *ninth,TH1F *tenth,TH1F * eleventh,TH1F * twelfth);
TString GetXaxis(TString var);

void MuNuPlotFIT(TString var,bool log,bool save,char* savefile, int bins, double lo, double hi, double top, TString cutInput,char* notes1,TString weightinput, double QCDNORM, bool setLog){

  bool mconly = false;
  bool shapes = true;
  bool nEvents = false;

  //TString dir = "/scratch/ojalvo/sandbox_11_27_MC/";
  //TString dirW = "/scratch/ojalvo/sandbox_12_1_MCW2b/";

  //TString dir = "/scratch/ojalvo/sandbox_12_10_MC/";
  //TString dirW = "/scratch/ojalvo/sandbox_12_10_MCW2/";

  TString dir = "/scratch/ojalvo/sandbox_11_27_MC/";
//  TString dirW = "/scratch/ojalvo/sandbox_12_1_MCW2b/";
	TString dirW = "/scratch/mcepeda/backup_iso/";
  TString dirdat = "/scratch/ojalvo/sandbox_11_29_DataPat/";


  TLegend *leg = new TLegend(0.69,0.55,0.99,0.95);//  leg = new TLegend(0.74,0.65,0.99,0.95);
  TFile hfile("temp.root","RECREATE");
  gROOT->ProcessLine(".L tdrstyle.C");
  gROOT->SetBatch();
  setTDRStyle();
  TCanvas *Tcan= new TCanvas("Tcan","",100,20,600,800); 
  Tcan->cd();
  Tcan->SetFillColor(0); 
  TPad* pad1 = new TPad("pad1","The pad",0,0.2,1,1);  pad1->SetLogy(setLog);
  TPad* pad2 = new TPad("pad2","the other pad",0,0,1,0.2);
  pad1->SetFillColor(0);
  TString weight = "EffWEIGHTpt*EffWEIGHTtrigeta*__WEIGHT__*4850.";

  if(weightinput != "none")
    { weight = "EffWEIGHTpt*EffWEIGHTtrigeta*__WEIGHT__*4850*"+weightinput;}

  TString weightW = "EffWEIGHTpt*EffWEIGHTtrigeta*4850";
  //TString weightW = "31314*__WEIGHTPU__*EffWEIGHTpt*EffWEIGHTtrigeta*4900*0.98";
  TString cuts ="abs(muonEta)<2.1&&muonPt>25&&abs(l1DXY)<0.02&&nMuons==1&&abs(dz)<0.5&&muNuRelPFIso<0.12";//muNuRelPFIso<0.12&&
  TString cutsQCD ="abs(muonEta)<2.1&&muonPt>25&&abs(l1DXY)<0.02";

  shfile = new TFile("FIT2.root","RECREATE");
  cout << "Plotting"<< var <<endl;
  //TString bHadron = "(abs(J1JetParton)==5&&abs(J2JetParton)==5)";
  TString bHadron = "nbHadrons>0";
  TString Wcvareven = "((ncCands+ncbarCands)/2==1||(ncCands+ncbarCands)/2==2||(ncCands+ncbarCands)/2==3||(ncCands+ncbarCands)/2==4)";

  TH1F *Data = createhist("data_obs",var,"wMuNuData.root",dirdat,kCyan,weight,true,cuts+"&&"+cutInput,bins,lo,hi);
  TH1F *W = createhist("W",var,"Wbig.root",dirW,kAzure+1,weightW+"*__WEIGHTPU2__*__WEIGHTLHE__*0.000165*0.57963",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands<1)&&"+cutInput,bins,lo,hi);//1.571
  //TH1F *W2 = createhist("W2",var,"W.root",dir,kAzure+1,weight+"*1",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands<1)&&"+cutInput,bins,lo,hi);
  TH1F *Wbb = createhist("Wbb",var,"Wbig.root",dirW,kBlue-10,weightW+"*__WEIGHTPU2__*__WEIGHTLHE__*0.000165*0.566842",false,cuts+"&&"+bHadron+"&&"+cutInput,bins,lo,hi);//1.571
  //TH1F *Wbb2 = createhist("Wbb2",var,"W.root",dir,kAzure+1,weight+"*1",false,cuts+"&&"+bHadron+"&&"+cutInput,bins,lo,hi);
  //TH1F *Wbbf = createhist("Wbbf",var,"Wbig.root",dirW,kBlue-10,"1",false,cuts+"&&"+bHadron+"&&"+cutInput,bins,lo,hi);//1.571
  TH1F *Wc = createhist("Wc",var,"Wbig.root",dirW,kMagenta-4,weightW+"*__WEIGHTPU2__*__WEIGHTLHE__*0.000165*0.580816",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands>0)&&!"+Wcvareven+"&&"+cutInput,bins,lo,hi);//1.571
  //TH1F *Wcf = createhist("Wcf",var,"Wbig.root",dirW,kMagenta-4,"1",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands>0)&&!"+Wcvareven+"&&"+cutInput,bins,lo,hi);//1.571
  //TH1F *Wccf = createhist("Wccf",var,"Wbig.root",dirW,kViolet-6,"1",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands>0)&&"+Wcvareven+"&&"+cutInput,bins,lo,hi);//1.571
  TH1F *Wcc = createhist("Wcc",var,"Wbig.root",dirW,kViolet-6,weightW+"*__WEIGHTPU2__*__WEIGHTLHE__*0.000165*0.580816",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands>0)&&"+Wcvareven+"&&"+cutInput,bins,lo,hi);//1.571
  //TH1F *Wcc2 = createhist("Wcc2",var,"W.root",dir,kAzure+1,weight+"*1",false,cuts+"&&!"+bHadron+"&&(ncCands+ncbarCands>0)&&"+Wcvareven+"&&"+cutInput,bins,lo,hi);

  TH1F *TOP = createhist("TOP",var,"TOP.root",dir,kOrange-2,weight+"*1.",false,cuts+"&&"+cutInput,bins,lo,hi);
  TH1F *ZJets = createhist("Z_jets",var,"DYall.root",dir,kRed+2,weight+"*1.",false,cuts + "&&" + cutInput,bins,lo,hi);//+"*2*0.85"
  TH1F *WZ = createhist("WZ",var,"WZ.root",dir,kRed+2,weight,false,cuts+"&&"+cutInput,bins,lo,hi);
  TH1F *WW = createhist("WW",var,"WW.root",dir,kRed+2,weight,false,cuts+"&&"+cutInput,bins,lo,hi);
  TH1F *T = createhist("T",var,"Tt.root",dir,kOrange+7,weight,false,cuts+"&&"+cutInput,bins,lo,hi);
  TH1F *Tbar = createhist("Tbar",var,"Ts.root",dir,kOrange+7,weight+"*1",false,cuts+"&&"+cutInput,bins,lo,hi);
  TH1F *tW = createhist("tW",var,"TtWDR.root",dir,kOrange+7,weight,false,cuts+"&&"+cutInput,bins,lo,hi);
  
  TString cutsq ="abs(muonEta)<2.1&&muonPt>25&&abs(l1DXY)<0.02&&muNuRelPFIso>0.5";

  //qcd estimate
  TH1F *Wq = createhist("Wq",var,"W.root",dir,kAzure+1,weight+"*1",false,cutsq+"&&"+cutInput,bins,lo,hi);//1.571
  TH1F *TOPq = createhist("TOPq",var,"TOP.root",dir,kOrange-2,weight+"*1.",false,cutsq+"&&"+cutInput,bins,lo,hi);
  TH1F *ZJetsq = createhist("Z_jetsq",var,"DYall.root",dir,kRed+2,weight+"*1.",false,cutsq + "&&" + cutInput,bins,lo,hi);//+"*2*0.85"
  TH1F *WZq = createhist("WZq",var,"WZ.root",dir,kRed+2,weight,false,cutsq+"&&"+cutInput,bins,lo,hi);
  TH1F *WWq = createhist("WWq",var,"WW.root",dir,kRed+2,weight,false,cutsq+"&&"+cutInput,bins,lo,hi);
  TH1F *Tq = createhist("Tq",var,"Tt.root",dir,kOrange+7,weight,false,cutsq+"&&"+cutInput,bins,lo,hi);
  TH1F *Tbarq = createhist("Tbarq",var,"Ts.root",dir,kOrange+7,weight+"*1",false,cutsq+"&&"+cutInput,bins,lo,hi);
  TH1F *tWq = createhist("tWq",var,"TtWDR.root",dir,kOrange+7,weight,false,cutsq+"&&"+cutInput,bins,lo,hi);

  
  TH1F *subtract = new TH1F("sub","sub",bins,lo,hi);
  //TH1F *QCD = new TH1F("qcdshape","qcdshape",bins,lo,hi);
  TH1F *QCD = createhist("QCD",var,"wMuNuData.root",dirdat,kGreen-3,"1",false,cutsQCD+"&&"+cutInput+"&&muonPt>25&&muNuRelPFIso>0.2",bins,lo,hi);//.11
        QCD->Scale(QCDNORM);
  subtract->Add(Wq);subtract->Add(TOPq);subtract->Add(ZJetsq);subtract->Add(Tq);subtract->Add(Tbarq);subtract->Add(ZJetsq);

  QCD->Add(subtract,-1);
  
  shfile->cd();

  shfile->Close(); 

  float S = Wbb->Integral();
  float B = W->Integral()+Wc->Integral()+Wcc->Integral()+ TOP->Integral()+ZJets->Integral()+WZ->Integral()+WW->Integral()+QCD->Integral()+Tbar->Integral()+T->Integral()+tW->Integral();//+ZJetsbb->Integral();//Den->Add(W2);
  float mc = W->Integral()+Wbb->Integral()+Wc->Integral()+Wcc->Integral() + TOP->Integral()+ZJets->Integral()+WZ->Integral()+WW->Integral()+QCD->Integral()+T->Integral()+Tbar->Integral()+tW->Integral();//+ZJetsbb->Integral()
  float uncert = (Wbb->Integral()+W->Integral()+Wc->Integral()+Wcc->Integral())*.10 + ZJets->Integral()*0.10+TOP->Integral()*0.06+(Tbar->Integral()+T->Integral()+tW->Integral())*0.053+WW->Integral()*0.05+WZ->Integral()*0.04+QCD->Integral()*0.20;
  printf("Total MC = %f\n",mc);
  printf("S/B = %f\n",S/B);
  printf("S/sqrt(S+B) = %f\n",S/sqrt(S+B));
  printf("Excess Wbb? = %f\n",(Data->Integral()-mc+Wbb->Integral())/Wbb->Integral());
  printf("Excess Wcc? = %f\n",(Data->Integral()-mc+Wcc->Integral())/Wcc->Integral());
  float data_uncert = sqrt(Data->Integral());
  //cout << name <<  << endl;
  cout << Wbb->Integral() << W->Integral()<< "$\\pm$" << W->Integral()*.10 << ((float)Wc->Integral() + (float)Wcc->Integral()) << "$\\pm$"<< (Wc->Integral() + Wcc->Integral())*0.2 << ZJets->Integral() << "$\\pm$"<< ZJets->Integral()*0.10 << TOP->Integral() << "$\\pm$"<< TOP->Integral()*0.06 << Tbar->Integral()+T->Integral()+tW->Integral() << "$\\pm$" << (Tbar->Integral()+T->Integral()+tW->Integral())*0.053 << WW->Integral() << "$\\pm$" << WW->Integral()*0.05 << WZ->Integral() << "$\\pm$" << WZ->Integral()*0.04 << QCD->Integral() << "$\\pm$" << QCD->Integral()*0.20 << mc << "$\\pm$" << uncert << Data->Integral()<< "$\\pm$" << data_uncert << endl;

  printf("& %.1lf& %.1lf& %.1lf &%.1lf & %.1lf&%.1lf&%.1lf &%.1lf &%.1lf &%.1lf &%.1lf &%.1lf  \n",Wbb->Integral(),W->Integral(),Wc->Integral(),Wcc->Integral(),ZJets->Integral(),TOP->Integral(),Tbar->Integral()+T->Integral()+tW->Integral(),WW->Integral(),WZ->Integral(),QCD->Integral(),mc,Data->Integral());
  printf("& & $\\pm %.1lf$& $\\pm %.1lf$& $\\pm %.1lf$&$\\pm %.1lf$&$\\pm %.1lf$ &$\\pm %.1lf$ &$\\pm %.1lf$& $\\pm %.1lf$&$\\pm %.1lf$& $\\pm %.1lf$ \n",W->Integral()*.10,(Wc->Integral()+Wcc->Integral())*0.2,ZJets->Integral()*0.10,TOP->Integral()*0.06,(Tbar->Integral()+T->Integral()+tW->Integral())*0.053,WW->Integral()*0.05,WZ->Integral()*0.04,QCD->Integral()*0.20,uncert,data_uncert);
  //printf("& %.1lf& %.1lf$\\pm %.1lf$& %.1lf $\\pm %.1lf$& %.1lf$\\pm %.1lf$&%.1lf$\\pm %.1lf$&%.1lf$\\pm %.1lf$ &%.1lf$\\pm %.1lf$ &%.1lf $\\pm %.1lf$&%.1lf $\\pm %.1lf$&%.1lf $\\pm %.1lf$&%.1lf $\\pm %.1lf$&%.1lf $\\pm %.1lf$ \n",Wbb->Integral(),W->Integral(),W->Integral()*.10,Wc->Integral()+Wcc->Integral(),(Wc->Integral()+Wcc->Integral())*0.2,ZJets->Integral(),ZJets->Integral()*0.10,TOP->Integral(),TOP->Integral()*0.06,Tbar->Integral()+T->Integral()+tW->Integral(),(Tbar->Integral()+T->Integral()+tW->Integral())*0.053,WW->Integral(),WW->Integral()*0.05,WZ->Integral(),WZ->Integral()*0.04,QCD->Integral(),QCD->Integral()*0.20,mc,uncert,Data->Integral(),data_uncert);
  //printf("Excess Zbb? = %f\n",(Data->Integral()-mc+ZJetsbb->Integral())/ZJetsbb->Integral());

  THStack *stacked = new THStack("stack","stack");

  if(log){
    stacked = addFunc(Wbb,W,Wcc,Wc,QCD,ZJets,WZ,WW,T,tW,Tbar,TOP);
    pad1->SetLogy();
  }
  else{
    Wbb->SetFillStyle(3001);
    //THStack *stacked = addFunc(Tbar,WZ,WW,ZJets,QCD,T,Tbar,Tbar,TOP,W,W2,Wbb,bins,lo,hi);
    //THStack *stacked = addFunc(WZ,WW,ZJetsbb,ZJets,QCD,T,Tbar,tW,TOP,W,Wbb,bins,lo,hi);
    stacked = addFunc(WZ,WW,ZJets,QCD,T,tW,Tbar,TOP,Wcc,Wc,W,Wbb);
 }

  T->SetLineColor(kOrange+7);
  //Tbar->SetLineColor(kOrange+7);
  tW->SetLineColor(kOrange+7);
  WW->SetLineColor(kRed+2);
  WZ->SetLineColor(kRed+2);


  pad1->Draw();
  pad1->cd();
  pad1->SetLeftMargin(0.2);
  pad1->SetBottomMargin(0.13);
 
  //subtract->SetLineColor(kBlack);
  //qcdshape->SetLineWidth(4);
  //printf("subtract integral %f\n",subtract->Integral());
  stacked->Draw();
  //qcdshape->Draw("same");

  gStyle->SetErrorX(0.5);
  Data->SetMarkerSize(1.5);
  Data->SetMarkerColor(1);
  Data->SetMarkerStyle(13);


  Data->Draw("pEsame");

  TString xlabel = GetXaxis(var);
  stacked->GetXaxis()->SetTitle(xlabel);
  double y;
  if(mconly){
    y = TOP->GetMaximumBin();
    y = TOP->GetBinContent(y);
    stacked->SetMaximum(top*y);
    //stacked->SetMaximum(300);
    
  }
  else{
    y = Data->GetMaximumBin();
    y = Data->GetBinContent(y);
    stacked->SetMaximum(top*y);
    //stacked->SetMaximum(300);
  }

  if(log){
    stacked->SetMaximum(top*y);
    stacked->SetMinimum(1);
  }

  if(var == "MET" || var == "Mt"|| var == "muonPt" || var =="mJJ"|| var == "ptJJ" ){
  int nob = (hi-lo)/bins;
  stacked->GetYaxis()->SetTitle(TString::Format("Events / %i GeV",nob));
  }
  else
  stacked->GetYaxis()->SetTitle("Events");
  
  stacked->GetYaxis()->SetTitleOffset(1.7);

  leg->SetFillColor(0);
  leg->SetFillStyle(0);
  leg->SetBorderSize(0);
  leg->SetHeader("");
  leg->SetShadowColor(0);
  leg->AddEntry(Data,"Data","p");
  leg->AddEntry(Wbb,"W#rightarrow#mu#nu+bb","f");
  leg->AddEntry(Wcc,"Wcc","f");
  leg->AddEntry(Wc,"W#rightarrow#mu#nu+c","f");
  leg->AddEntry(W,"W#rightarrow#mu#nu+jj","f");
  leg->AddEntry(TOP,"t#bar{t}","f");
  leg->AddEntry(Tbar,"t / #bar{t}","f");

  leg->AddEntry(QCD,"QCD","f");
  leg->AddEntry(ZJets,"Z+jets/VV","f");
  //leg->AddEntry(qcdshape,"QCD SHAPE","l");
  //leg->AddEntry(ZJetsbb,"Z+jetsbb","f");
  leg->Draw();

  /////////write sqrts 7TeV
  TLegend* leg2 = new TLegend(0.72,0.95,1.1,.99); //left bottom right top   
  leg2->SetFillColor(0);
  leg2->SetFillStyle(0);
  leg2->SetBorderSize(0);
  leg2->SetHeader("#sqrt{s}= 7 TeV");
  leg2->SetShadowColor(0);
  leg2->Draw();


  /////////write CMS Preliminary
  TLegend* leg5 = new TLegend(0.3,0.95,0.6,.99); //left bottom right top   
  leg5->SetFillColor(0);
  leg5->SetFillStyle(0);
  leg5->SetBorderSize(0);
  leg5->SetHeader("CMS Preliminary");
  leg5->SetShadowColor(0);
  leg5->Draw();

  /////////write luminosity        
                                                                                                                                                                              
  TLegend* leg3 = new TLegend(0.22,0.86,0.42,0.91); //left bottom right top   
  leg3->SetFillColor(0);
  leg3->SetFillStyle(0);
  leg3->SetBorderSize(0);
  leg3->SetHeader("#int L dt = 5 fb^{-1}");
  leg3->SetShadowColor(0);
  leg3->Draw();


  TPaveText* notes = new TPaveText(0.15,0.0,0.65,0.07, "NDC"); //left bottom right top
  TText* text = notes->AddText(notes1);
  notes->SetFillColor(0); // text is black on white                                                                                         
  notes->SetTextSize(0.04);
  notes->SetTextAlign(12);
  notes->SetFillStyle(0);
  notes->SetBorderSize(0);
  notes->SetShadowColor(0);
  notes->Draw();

  if(nEvents){
    TLatex latex;
    latex.SetTextSize(0.03);
    latex.SetTextAlign(13); 
    latex.DrawLatex(.4,.2,TString::Format("DATA events=%f",Data->Integral()));
    latex.Draw();

  
  }

  //////////////////////////////////////ratio plot
  Tcan->cd();
  pad2->Draw();
  pad2->cd(); 
  
  pad2->SetBottomMargin(0.1);
  pad2->SetTopMargin(0.1);
  pad2->SetLeftMargin(0.2); 

  TH1F *Den = new TH1F("Den","hist",bins,lo,hi);
  TH1F *Num = new TH1F("Num","hist",bins,lo,hi);

  Den->Add(W);Den->Add(WZ);Den->Add(WW);Den->Add(ZJets);Den->Add(QCD);Den->Add(T);Den->Add(Tbar);Den->Add(tW);Den->Add(TOP);Den->Add(Wbb);Den->Add(Wc);Den->Add(Wcc);//Den->Add(Wb2);
  Num->Add(Data);


  TH1F *Eff = (TH1F*)Num->Clone();
  
  Num->Sumw2();
  Den->Sumw2();
  printf("Num: %f, Den: %f\n",Num->Integral(),Den->Integral());
  //TGraphAsymmErrors *ratio = new TGraphAsymmErrors(Data);
  
  Eff->Divide(Num,Den);
  Eff->SetMaximum(1.5);
  Eff->SetMinimum(0.5);

  float max = Eff->GetMaximum();
  float min = Eff->GetMinimum();

  TF1 *f2 = new TF1("f2","x",min,max);

  TGaxis *newyaxis = new TGaxis(lo,min,lo,max,"f2");
  newyaxis->SetLabelSize(0.12);


  pad2->cd();
  TLine *center = new TLine(lo,1,hi,1);
  center->SetLineStyle(2);
  Eff->Draw("ap");

  center->Draw();
  newyaxis->Draw();



  if(save){
    Tcan->SaveAs(TString::Format("~/www/darin/%s.png",savefile));
 }

    TCanvas *Tcan2= new TCanvas("Tcan2","",100,20,600,800); 
    if(shapes){
      TLegend *leg7 = new TLegend(0.7,0.55,0.99,0.95);//  leg = new TLegend(0.74,0.65,0.99,0.95);
      leg7->SetFillColor(0);
      leg7->SetFillStyle(0);
      leg7->SetBorderSize(0);
      leg7->SetShadowColor(0);
      Tcan2->cd();
      Tcan2->SetFillColor(0); 
      W->Scale(1/(W->Integral()));  //WZ->Scale(1/(WZ->Integral()));WW->Scale(1/(WW->Integral()));
      ZJets->Scale(1/(ZJets->Integral())); T->Scale(1/(T->Integral())); Tbar->Scale(1/(Tbar->Integral())); 
      tW->Scale(1/(tW->Integral())); TOP->Scale(1/(TOP->Integral()));Wbb->Scale(1/(Wbb->Integral()));//Wb1->Scale(1/(Wb1->Integral()));Wb2->Scale(1/(Wb2->Integral()));
      Wc->Scale(1/(Wc->Integral())); //TOPbb->Scale(1/(TOPbb->Integral()));
      W->SetLineColor(kAzure+1);ZJets->SetLineColor(kRed+2);TOP->SetLineColor(kOrange+3);tW->SetLineColor(kOrange-7);//TOPbb->SetLineColor(kMagenta-7);
      Tbar->SetLineColor(kGreen+1);T->SetLineColor(kGreen+4);Wc->SetLineColor(kViolet-6);Wbb->SetLineColor(kBlack);Wbb->SetLineWidth(3);//Wb1->SetLineColor(kOrange+2);Wb1->SetLineWidth(3);Wb2->SetLineColor(kGreen+3);Wb2->SetLineWidth(3);
      Wc->SetLineWidth(4);
      Wbb->SetLineWidth(4);
      TOP->SetLineWidth(4);
      TOP->SetLineStyle(2);
      W->SetFillColor(0);ZJets->SetFillColor(0);TOP->SetFillColor(0);tW->SetFillColor(0);//TOPbb->SetFillColor(0);
      Tbar->SetFillColor(0);T->SetFillColor(0);Wc->SetFillColor(0);Wbb->SetFillColor(0);//Wb1->SetFillColor(0);Wb2->SetFillColor(0);
      Wbb->Draw();//W->Draw("same");//ZJets->Draw("same");//
      Tbar->SetLineColor(kViolet-6);
      Tbar->SetLineWidth(4);
      tW->SetLineColor(kAzure+1);
      tW->SetLineWidth(4);
      Tbar->Draw("same");tW->Draw("same");
      Wbb->Draw("same");
      //Wb2->Draw();
      TOP->Draw("same");//TOPbb->Draw("same");
      Wbb->GetXaxis()->SetTitle(xlabel);
      leg7->AddEntry(Wbb,"W+bb","l");
      leg7->AddEntry(tW,"t-W","l");
      leg7->AddEntry(Tbar,"Single Top","l");
      leg7->AddEntry(TOP,"t#bar{t}","l");
      leg7->Draw(); 
//      Tcan2->SaveAs(TString::Format("~/www/1_28_13/%s_topshape.png",savefile));

      TLegend *leg8 = new TLegend(0.7,0.55,0.99,0.95);
      leg8->SetFillColor(0);
      leg8->SetFillStyle(0);
      leg8->SetBorderSize(0);
      leg8->SetShadowColor(0);
      Tcan2->cd();
      Tcan2->SetFillColor(0); 
      //W->Scale(1/(W->Integral()));  
      Wcc->Scale(1/(Wcc->Integral())); 
      W->SetLineColor(kAzure+1);
      Wc->SetLineColor(kRed+2);
      Wcc->SetLineColor(kViolet-6);
      Wbb->SetLineColor(kBlack);
      Wbb->SetLineWidth(3);//Wb1->SetLineColor(kOrange+2);Wb1->SetLineWidth(3);Wb2->SetLineColor(kGreen+3);Wb2->SetLineWidth(3);
      Wc->SetLineWidth(4);
      Wbb->SetLineWidth(4);
      W->SetFillColor(0);
      Wc->SetFillColor(0);Wbb->SetFillColor(0);
      Wcc->SetFillColor(0);
      Wc->Draw();//W->Draw("same");//ZJets->Draw("same");//
      Wbb->Draw("same");
      //W->Draw("same");
      Wcc->Draw("same");
      W->Draw("same");
      Wbb->GetXaxis()->SetTitle(xlabel);
      leg8->AddEntry(Wbb,"W+bb","l");
      leg8->AddEntry(Wc,"W+c","l");
      leg8->AddEntry(Wcc,"W+cc","l");
      leg8->AddEntry(W,"W+l","l");
      leg8->Draw();
 //     Tcan2->SaveAs(TString::Format("~/www/1_28_13/%s_Wshape.png",savefile));

  }
  //ww,wz

    // if(save&&shapes){

    //}


}

THStack *addFunc(TH1F *first, TH1F *second, TH1F *third, TH1F *fourth, TH1F *fifth, TH1F *sixth, TH1F *seventh, TH1F *eighth, TH1F *ninth,TH1F *tenth,TH1F * eleventh,TH1F * twelfth){
  THStack *stacked = new THStack("stack","stack");
  stacked->Add(first);
  stacked->Add(second);
  stacked->Add(third);
  stacked->Add(fourth);
  stacked->Add(fifth);
  stacked->Add(sixth);
  stacked->Add(seventh);
  stacked->Add(eighth);
  stacked->Add(ninth);
  stacked->Add(tenth);
  stacked->Add(eleventh);
  stacked->Add(twelfth);
  //stacked->Add(thirteenth);
  //stacked->Add(fourteenth);
  return stacked;
}

TH1F *createhist(TString name,TString var,TString file,TString dir,Color_t color,TString weight,bool data,TString cuts,int bins,double lo,double hi){

  TFile *tempFile = new TFile(dir+file);

//  TString treeName = "muNuEventTree/eventTree";
  TString treeName = "muNuEventTreeFIT/eventTree";
  if(data==true||name=="QCD")
    treeName = "muNuEventTree/eventTree";

  TTree* tempTree = (TTree*)tempFile->Get(treeName);
  TH1F *tempHist = new TH1F("tempName","hist",bins,lo,hi);
  
  TString s = TString::Format("%i,%f,%f",bins,lo,hi);
  if(data){
    tempTree->Draw(var+">>+tempName",cuts);
  }
  else {
    tempTree->Draw(var+">>+tempName","("+cuts+")*("+weight+")");
    tempHist->SetFillColor(color);
    tempHist->SetLineWidth(2);
  }
  shfile->cd();
  tempHist->Write(name);
  float total = tempHist->Integral();
  cout << name << " Events = " << total << endl;
  return tempHist;
  delete tempTree;
}


TString GetXaxis(TString var){
  TString title;
  //TString var = var1;
  if( var == "Mt"){return " Mt(#mu#nu) [GeV]";}  
  else if(var == "((bHadronsEta.[1]-secondJetEta)*(bHadronsEta.[1]-secondJetEta)+(bHadronsPhi.[1]-secondJetPhi)*(bHadronsPhi.[1]-secondJetPhi))^(1/2)"){return "#DeltaR bHadron, Reco Jet";}
  else if(var == "((bHadronsEta.[0]-J1SVeta)^2+(J1SVphi-bHadronsPhi.[0])^2)^(1/2)"){return "#DeltaR SV bHadron";}
  else if(var == "((bHadronsEta.[0]-bHadronsEta.[1])*(bHadronsEta.[0]-bHadronsEta.[1])+(bHadronsPhi.[0]-bHadronsPhi.[1])*(bHadronsPhi.[0]-bHadronsPhi.[1]))^(1/2)"){return "#DeltaR Gen bHadrons";}
  else if(var == "1/sqrt(2)*((ptJJ/(highestJetPt+secondJetPt))^2+(WPt/(muonPt+MET))^2)^(1/2)"){return " S_{P_{T}}'";}  
  else if(var == "ht/max(J1SVMassb,J2SVMassb)"){return "ht/MaxSVMass";}  
  else if(var == "max(J1SVMassb,J2SVMassb)"){return "MaxSVMass";}  
  else if(var == "muNuDPhi"){return " d#Phi(#mu#nu)";}  
  else if(var == "MtCal"){return " Mt(#mu#nu) [GeV]";}  
  else if(var == "MET"){return "MET [GeV]";}  
  else if(var == "met"){return "\cancel{E_{T}} [GeV]";}  
  else if(var == "WPt"){return "WPt [GeV]";}  
  else if(var == "J1SVMassb+J2SVMassb"){return "J1+J2 SVMass [GeV]";}
  else if(var == "J1SVMassb"){return "J1SVMass [GeV]";}
  else if(var == "J2SVMassb"){return "J2SVMass [GeV]";}
  else if(var == "mJJ"){return " M(jet1 +jet2) [GeV]";}
  else if(var == "ptJJ"){return " P_{T}(jet1 +jet2) Pt [GeV]";}
  else if(var == "muonPt"){return " #mu P_{T} [GeV]";}
  else if(var == "muonPhi"){return " #mu #phi";}
  else if(var == "muonEta"){return " #mu #eta";}
  else if(var == "nJets24to5"){return " nJets #eta>2.4";}
  else if(var == "nMuons"){return " nMuons";}
  else if(var == "nElectrons"){return " nElectrons";}
  else if(var == "vertices"){return " Vertex Distribution";}  
  else if(var == "((J1SVphi-J2SVphi)^2+(J1SVeta-J2SVeta))^(1/2)"){return "#Delta R SV";}  
  else if(var == "DiMuonMass"){return " M(#mu#mu) [GeV]";}
  else if(var == "muNuRelPFIso"){return " PF Relative Isolation";}
  else if(var == "muNuRecoil"){return " W Recoil";}
  else if(var == "secondJetEta"){
    return " jet2  #eta ";
  }
  else if(var == "highestJetEta"){
    return " jet1  #eta ";
  }
  else if(var == "highestJetPhi"){
    return " jet1  #phi ";
  }
  else if(var == "secondJetPhi"){
    return " jet2  #phi ";
  }
  else if(var == "highestJetPt"){
    return " jet1  Pt [GeV] ";
  }
  else if(var == "secondJetPt"){
    return " jet2  Pt [GeV] ";
  }
  else if(var == "((muonEta-highestJetEta)^2+(muonPhi-highestJetPhi)^2)^(1/2)"){
    return " #DeltaR #mu, Highest P_{T} Jet";
  }
  else if(var == "((muonEta-secondJetEta)^2+(muonPhi-secondJetPhi)^2)^(1/2)"){
    return " #DeltaR #mu, 2nd Highest P_{T} Jet";
  }
  else if(var == "((highestJetEta-secondJetEta)^2+(highestJetPhi-secondJetPhi)^2)^(1/2)"){
    return " #DeltaR J1,J2";
  }
  else if(var == "(RUN<5)*0.9983*DiMuonMass+(RUN>5)*DiMuonMass"){
    return "Z #mu#mu Mass";
  }
  else{
    return var;
  }
  
  return title;
}
