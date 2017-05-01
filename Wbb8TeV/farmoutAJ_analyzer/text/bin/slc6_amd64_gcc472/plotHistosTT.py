#!/usr/bin/env python
'''
 Merges histograms from the output of
 callHistoFiller.cc into one file
 Author: T.M.Perry UW-Madison
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
#import fnmatch as fnm
import cmsPrelim as cpr

version="CestPi"
runname="ttCSVtSFnone"
#runname="ttCSVtSFfull"
#runname="tt012csvt"
#runname="tt012csvm"

path = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s/'%(version,runname)

leps = ['ele','mu']
cuts = [
 "ttme0b",
 "ttme1b",
 "ttme2b",
 "ttme0bJv",
 "ttme1bJv",
 "ttme2bJv",
 "ttme0bMt",
 "ttme1bMt",
 "ttme2bMt",
 "ttme0bJvMt",
 "ttme1bJvMt",
 "ttme2bJvMt",
]
#cuts = ['wbb', 'ttme', 'ttjjj', 'wjj', 'stt', 'dyjj', 'dybb']
variables = [ 
 "mt",
# "vertices",
# "met",
# "goodLep_pt",
# "goodJ1_pt",
# "goodJ2_pt",
# "goodJ1J2_dR",
# "goodJ1J2_mass",
# "goodJ1_CSV",
# #"goodJ1_mass_SV_unweighted",
# "goodJ1_mass_SV_corrected",
# #"goodJ1_mass_SV_weighted",
# "goodJ2_CSV",
# #"goodJ3J4_mass" 
]

for lep in leps:
 for variable in variables: 
  for cut in cuts:

   #canvas attributes
   canx = 1200
   cany = 900
   
   c = TCanvas('c','Canvas Named c',canx,cany)
   
   c.cd()
   p1 = TPad('p1','p1',0,0.25,1,1)
   p1.SetBottomMargin(0.04)
   p1.Draw()
   p1.SetLogy(0)
   p1.SetFrameLineWidth(2)
   c.cd()
   p2 = TPad('p2','p2',0,0,1,0.25)
   p2.SetTopMargin(0.02)
   p2.SetBottomMargin(0.3)
   p2.SetFrameLineWidth(2)
   p2.Draw()

   c.cd()
   p1.cd()
   
   theFilename = "%sHistograms_%s_%s_%s"%(path,cut,variable,lep)
   theFile = TFile(theFilename+".root")
   
   #
   #title = "Transverse Mass"
   #xlabel = "Transverse Mass [GeV]"
   
   # rebin factor
   rebin = 1
   
   # scale factors 
   sf_qcd = 1.  
   sf_z = 1.   
   sf_vv = 1.  
   sf_t = 1.  
   sf_tb = 1.  
   sf_ttb = 1. 
   sf_wl = 1.  
   sf_wc = 1.  
   sf_wcc = 1. 
   sf_wbb = 1.
   
   ratioRange = 0.3
   errorBand = True
   
   #color scheme
   c_data = 1
   c_qcd =   ROOT.EColor.kRed+1
   c_z =   ROOT.EColor.kOrange-3
   c_vv =   ROOT.EColor.kYellow-3
   c_t =  ROOT.EColor.kGreen+1
   c_tb =  ROOT.EColor.kGreen-5
   c_ttb = ROOT.EColor.kGreen-9
   c_wl =  ROOT.EColor.kAzure+10
   c_wc =  ROOT.EColor.kBlue+0
   c_wcc = ROOT.EColor.kBlue-9
   c_wbb = 51
   
   fillStyle = 1
   fillStyleTTs = 1
   fillStyleTTf = 1
   
   tex = ROOT.TLatex()
   tex.SetTextSize(0.07)
   tex.SetTextAlign(13)
   tex.SetNDC(True)
   gStyle.SetOptStat('')
   gStyle.SetLineWidth(3)
   gStyle.SetPadTickY(1)


   data_obs = theFile.Get("data_obs")
   data_obs.Rebin( rebin )
   data_obs.SetMarkerStyle(22)
   data_obs.SetMarkerSize(1.2)
   data_obs.SetMarkerSize(2)
   data_obs.Draw()
   max_data = data_obs.GetMaximum()
   datasize=data_obs.Integral()
   
   h_qcd = theFile.Get("h_qcd")
   h_qcd.SetFillColor( c_qcd )
   h_qcd.SetFillStyle( fillStyle )
   h_qcd.Rebin( rebin )
   h_qcd.Scale( sf_qcd )
   h_qcd.Draw()
   
   h_Drell = theFile.Get("h_Drell")
   h_Drell.SetFillColor( c_z )
   h_Drell.Rebin( rebin )
   h_Drell.Scale( sf_z )
   h_Drell.Draw()
   
   h_WW = theFile.Get("h_WW")
   h_WW.SetFillColor( c_vv )
   h_WW.SetFillStyle( fillStyle )
   h_WW.Rebin( rebin )
   h_WW.Scale( sf_vv )
   h_WW.Draw()
   
   h_WZ = theFile.Get("h_WZ")
   h_WZ.SetFillColor( c_vv )
   h_WZ.SetFillStyle( fillStyle )
   h_WZ.Rebin( rebin )
   h_WZ.Scale( sf_vv )
   h_WZ.Draw()
   
   h_ZZ = theFile.Get("h_ZZ")
   h_ZZ.SetFillColor( c_vv )
   h_ZZ.SetFillStyle( fillStyle )
   h_ZZ.Rebin( rebin )
   h_ZZ.Scale( sf_vv )
   h_ZZ.Draw()
   
   h_T_s = theFile.Get("h_T_s")
   h_T_s.SetFillColor( c_t )
   h_T_s.SetFillStyle( fillStyle )
   h_T_s.Rebin( rebin )
   h_T_s.Scale( sf_t )
   h_T_s.Draw()
   
   h_T_t = theFile.Get("h_T_t")
   h_T_t.SetFillColor( c_t )
   h_T_t.SetFillStyle( fillStyle )
   h_T_t.Rebin( rebin )
   h_T_t.Scale( sf_t )
   h_T_t.Draw()
   
   h_T_tW = theFile.Get("h_T_tW")
   h_T_tW.SetFillColor( c_t )
   h_T_tW.SetFillStyle( fillStyle )
   h_T_tW.Rebin( rebin )
   h_T_tW.Scale( sf_t )
   h_T_tW.Draw()
   
   h_Tbar_s = theFile.Get("h_Tbar_s")
   h_Tbar_s.SetFillColor( c_tb )
   h_Tbar_s.SetFillStyle( fillStyle )
   h_Tbar_s.Rebin( rebin )
   h_Tbar_s.Scale( sf_tb )
   h_Tbar_s.Draw()
   
   h_Tbar_t = theFile.Get("h_Tbar_t")
   h_Tbar_t.SetFillColor( c_tb )
   h_Tbar_t.SetFillStyle( fillStyle )
   h_Tbar_t.Rebin( rebin )
   h_Tbar_t.Scale( sf_tb )
   h_Tbar_t.Draw()
   
   h_Tbar_tW = theFile.Get("h_Tbar_tW")
   h_Tbar_tW.SetFillColor( c_tb )
   h_Tbar_tW.SetFillStyle( fillStyle )
   h_Tbar_tW.Rebin( rebin )
   h_Tbar_tW.Scale( sf_tb )
   h_Tbar_tW.Draw()
   
   h_TTbar_semi = theFile.Get("h_TTbar_semi")
   h_TTbar_semi.SetFillColor( c_ttb )
   h_TTbar_semi.SetFillStyle( fillStyleTTs )
   h_TTbar_semi.Rebin( rebin )
   h_TTbar_semi.Scale( sf_ttb )
   h_TTbar_semi.Draw()
   
   h_TTbar_full = theFile.Get("h_TTbar_full")
   h_TTbar_full.SetFillColor( c_ttb )
   h_TTbar_full.SetFillStyle( fillStyleTTf )
   h_TTbar_full.Rebin( rebin )
   h_TTbar_full.Scale( sf_ttb )
   h_TTbar_full.Draw()
   
   h_Wl = theFile.Get("h_Wl")
   h_Wl.SetFillColor( c_wl )
   h_Wl.SetFillStyle( fillStyle )
   h_Wl.Rebin( rebin )
   h_Wl.Scale( sf_wl )
   h_Wl.Draw()
   
   h_Wc = theFile.Get("h_Wc")
   h_Wc.SetFillColor( c_wc )
   h_Wc.SetFillStyle( fillStyle )
   h_Wc.Rebin( rebin )
   h_Wc.Scale( sf_wc )
   h_Wc.Draw()
   
   h_Wcc = theFile.Get("h_Wcc")
   h_Wcc.SetFillColor( c_wcc )
   h_Wcc.SetFillStyle( fillStyle )
   h_Wcc.Rebin( rebin )
   h_Wcc.Scale( sf_wcc )
   h_Wcc.Draw()
   
   h_Wbb5F = theFile.Get("h_Wbb5F")
   h_Wbb5F.SetFillColor( c_wbb )
   h_Wbb5F.SetFillStyle( fillStyle )
   h_Wbb5F.Rebin( rebin )
   h_Wbb5F.Scale( sf_wbb )
   h_Wbb5F.Draw()
   
   # make a stack to draw with
   s_mc = THStack('hs','')
   s_mc.SetTitle('')
   s_mc.Add(h_qcd)
   s_mc.Add(h_Drell)
   s_mc.Add(h_WW)
   s_mc.Add(h_WZ)
   s_mc.Add(h_ZZ)
   s_mc.Add(h_T_s)
   s_mc.Add(h_T_t)
   s_mc.Add(h_T_tW)
   s_mc.Add(h_Tbar_s)
   s_mc.Add(h_Tbar_t)
   s_mc.Add(h_Tbar_tW)
   s_mc.Add(h_TTbar_semi)
   s_mc.Add(h_TTbar_full)
   s_mc.Add(h_Wl)
   s_mc.Add(h_Wc)
   s_mc.Add(h_Wcc)
   s_mc.Add(h_Wbb5F)
   s_mc.Draw()
   max_mc = s_mc.GetMaximum()
   
   # add all MC for ratio plot
   h_mc = h_qcd.Clone()
   h_mc.SetName("h_mc")
   h_mc.Add(h_Drell)
   h_mc.Add(h_WW)
   h_mc.Add(h_WZ)
   h_mc.Add(h_ZZ)
   h_mc.Add(h_T_s)
   h_mc.Add(h_T_t)
   h_mc.Add(h_T_tW)
   h_mc.Add(h_Tbar_s)
   h_mc.Add(h_Tbar_t)
   h_mc.Add(h_Tbar_tW)
   h_mc.Add(h_TTbar_semi)
   h_mc.Add(h_TTbar_full)
   h_mc.Add(h_Wl)
   h_mc.Add(h_Wc)
   h_mc.Add(h_Wcc)
   h_mc.Add(h_Wbb5F)
   mcsize=h_mc.Integral()
   if errorBand:
    h_mc_err = h_mc.Clone()
    h_mc_err.SetName('h_mc_err')
    h_mc_err.SetFillColor(ROOT.EColor.kBlue-6)
    h_mc_err.SetFillStyle(3001)
   # make ratio plot
   h_r = data_obs.Clone()
   h_r.SetName("h_r")
   h_r.Divide(h_mc)
   if errorBand:
    h_r_err = h_mc.Clone()
    h_r_err.SetName("h_r_err")
    h_r_err.SetFillColor(ROOT.EColor.kBlue-6)
    h_r_err.SetFillStyle(3001)
    h_r_errDivisor = h_mc.Clone()
    for i in range( h_r_err.GetNbinsX() + 1 ):
     h_r_errDivisor.SetBinError( i, 0 )
    h_r_err.Divide(h_r_errDivisor)
   
   # set p1 title and axis labels
   s_mc.GetXaxis().SetLabelSize(0.03)
   s_mc.GetYaxis().SetLabelSize(0.03)
   s_mc.GetYaxis().SetTitleOffset(1.5)
   s_mc.GetYaxis().SetTitle( "Events / %s GeV"%(h_mc.GetBinWidth(1)) )
   
   
   # set p2 y ranges
   the_max = max( max_mc,max_data )
   s_mc.SetMaximum( 1.2*the_max )
   h_r.GetYaxis().SetRangeUser(1.-ratioRange,1+ratioRange)
   h_r.GetYaxis().SetLabelSize(0.10)
   h_r.GetXaxis().SetLabelSize(0.10)
   h_r.GetYaxis().SetTitleSize(0.10)
   h_r.GetXaxis().SetTitleSize(0.10)
   h_r.GetYaxis().SetTitle("Data / MC")
   h_r.GetYaxis().SetTitleOffset(0.5)
   xlabel = h_r.GetTitle()
   title =  cut+" "+lep+" "+xlabel
   h_r.GetXaxis().SetTitle( xlabel )
   h_r.SetTitle("")
   
   # fill legend
   leg=TLegend(0.58,0.3,0.78,0.88)
   leg.AddEntry(data_obs,"Data")
   leg.AddEntry(h_Wbb5F,"W+b#bar{b}","f")
   leg.AddEntry(h_Wcc,"W+c#bar{c}","f")
   leg.AddEntry(h_Wc,"W+c","f")
   leg.AddEntry(h_Wl,"W+udsg","f")
   leg.AddEntry(h_TTbar_full,"t#bar{t}","f")
   leg.AddEntry(h_Tbar_s,"#bar{t}","f")
   leg.AddEntry(h_T_s,"t","f")
   leg.AddEntry(h_WW,"WW,WZ,ZZ","f")
   leg.AddEntry(h_Drell,"Drell-Yan","f")
   leg.AddEntry(h_qcd,"QCD","f")
   leg.SetFillColor(0)
   leg.SetBorderSize(0)
   
   # and draw
   #c.cd()
   p1.cd()
   s_mc.Draw('hist')
   if errorBand: h_mc_err.Draw('sames,E2')
   data_obs.Draw('sames,E1')
   leg.Draw('sames')
   
   cpr.prelim_alt(19700,0.05)
   tex.SetTextAlign(11) #left, bottom
   tex.DrawLatex(0.1,0.9,title)
   
   #c.cd()
   p2.cd() 
   h_r.Draw("ep")
   if errorBand: h_r_err.Draw("sames,E2")
   
   l = TLine(h_r.GetXaxis().GetXmin(),1,h_r.GetXaxis().GetXmax(),1)
   l.SetLineStyle(3)
   l.Draw()
   c.Update()
   
   c.Print(theFilename+".png")
   print("MC Size: %s"%mcsize)
   print("Data Size: %s"%datasize)
   print("Data/MC:  %s"%(datasize/mcsize))
   print("xxxxxxxxxxxxxx  %s & %s & %s "%(datasize,mcsize,datasize/mcsize))
   print("you just finished with %s.png"%theFilename)
   print("")
   c.Close()
   #c.Clear()
   
