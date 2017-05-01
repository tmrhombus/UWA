#!/usr/bin/env python
'''
Makes nice plots with ratio from histograms made using makeHistos.py
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
import sys
import cmsPrelim as cpr
import time

version = "Schweincomp"
runname = "wbb_csvt_mt0_v2"

inpath = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s'%(version,runname)
outpath = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s'%(version,runname)

sname='_normed'
leps = ["mu","ele"]
cuts = ["wbb",]#"ttme","ttjjj",]
vbls = [
 "mt",
# "met",
# "goodLep_pt",
# "goodJ1_pt",
# "goodJ2_pt",
# "goodJ3_pt",
]
#cuts = ["tt1m1e","tt3j"]

for lep in leps:
 for cut in cuts:
  for var in vbls:
   inname = "%s/Histograms_%s_%s_%s.root"%(inpath,cut,var,lep)
   outrname = "%s/shapeToNorm/ShapeSystematics_%s_%s_%s%s.root"%(outpath,cut,var,lep,sname)
   outpname = "%s/shapeToNorm/ShapeSystematics_%s_%s_%s%s.png"%(outpath,cut,var,lep,sname)
 
   infile = TFile(inname)
   outfile = TFile(outrname,'RECREATE','ShapeSystematics')
 
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
   
   #canvas attributes
   canx = 900 
   cany = 1200
   
   #color scheme
   c_data = 1
   c_Raw = 1 #ROOT.EColor.kRed+1
   c_UESUp   = ROOT.EColor.kGreen+2
   c_UESDown = ROOT.EColor.kGreen+2#3
   c_LESUp   = ROOT.EColor.kOrange+2
   c_LESDown = ROOT.EColor.kOrange+2#3
   c_JESUp   = ROOT.EColor.kCyan-4
   c_JESDown = ROOT.EColor.kGreen-4
   c_EMuUp   = ROOT.EColor.kAzure+2 
   c_EMuDown = ROOT.EColor.kAzure+2#3 
   c_CSVUp   = ROOT.EColor.kRed-4 
   c_CSVDown = ROOT.EColor.kMagenta-4
   
   w_Raw     = 4 
   w_UESUp   = 2 
   w_UESDown = 2 
   w_LESUp   = 2 
   w_LESDown = 2 
   w_JESUp   = 2 
   w_JESDown = 2 
   w_EMuUp   = 2 
   w_EMuDown = 2 
   w_CSVUp   = 3 
   w_CSVDown = 3 
   
   tex = ROOT.TLatex()
   tex.SetTextSize(0.07)
   tex.SetTextAlign(13)
   tex.SetNDC(True)
   gStyle.SetOptStat('')
   gStyle.SetLineWidth(3)
   gStyle.SetPadTickY(1)
   
   #
   title = "Transverse Mass"
   xlabel = "Transverse Mass [GeV]"
 
   c = TCanvas('c','Canvas Named c',canx,cany)
   c.cd()
 
   data_obs = infile.Get("data_obs")
   data_obs.Rebin( rebin )
   data_obs.SetMarkerStyle(22)
   data_obs.SetMarkerSize(1.2)
   data_obs.SetMarkerSize(2)
   data_obs.Draw("GOFF")
   max_data = data_obs.GetMaximum()
   data_obs.Write()
   
   integrals = []
 
   #shifts = ["","_JESUp","_JESDown"]
   #shifts = ["","_JESUp","_JESDown","_CSVUp","_CSVDown"]
   shifts = ["","_UESUp","_UESDown","_LESUp","_LESDown","_JESUp","_JESDown","_EMuUp","_EMuDown","_CSVUp","_CSVDown"]
   
   for shift in shifts:
    
    #h_qcd = infile.Get("h_TTqcd")
    #h_qcd.SetName("h_TTqcd")
    h_qcd = infile.Get("h_qcd")
    h_qcd.Rebin( rebin )
    h_qcd.Scale( sf_qcd )
    h_qcd.Draw("GOFF")
    
    h_Drell = infile.Get("h_Drell"+shift)
    h_Drell.Rebin( rebin )
    h_Drell.Scale( sf_z )
    h_Drell.Draw("GOFF")
    
    h_WW = infile.Get("h_WW"+shift)
    h_WW.Rebin( rebin )
    h_WW.Scale( sf_vv )
    h_WW.Draw("GOFF")
    
    h_WZ = infile.Get("h_WZ"+shift)
    h_WZ.Rebin( rebin )
    h_WZ.Scale( sf_vv )
    h_WZ.Draw("GOFF")
    
    h_ZZ = infile.Get("h_ZZ"+shift)
    h_ZZ.Rebin( rebin )
    h_ZZ.Scale( sf_vv )
    h_ZZ.Draw("GOFF")
    
    h_T_s = infile.Get("h_T_s"+shift)
    h_T_s.Rebin( rebin )
    h_T_s.Scale( sf_t )
    h_T_s.Draw("GOFF")
    
    h_T_t = infile.Get("h_T_t"+shift)
    h_T_t.Rebin( rebin )
    h_T_t.Scale( sf_t )
    h_T_t.Draw("GOFF")
    
    h_T_tW = infile.Get("h_T_tW"+shift)
    h_T_tW.Rebin( rebin )
    h_T_tW.Scale( sf_t )
    h_T_tW.Draw("GOFF")
    
    h_Tbar_s = infile.Get("h_Tbar_s"+shift)
    h_Tbar_s.Rebin( rebin )
    h_Tbar_s.Scale( sf_tb )
    h_Tbar_s.Draw("GOFF")
    
    h_Tbar_t = infile.Get("h_Tbar_t"+shift)
    h_Tbar_t.Rebin( rebin )
    h_Tbar_t.Scale( sf_tb )
    h_Tbar_t.Draw("GOFF")
    
    h_Tbar_tW = infile.Get("h_Tbar_tW"+shift)
    h_Tbar_tW.Rebin( rebin )
    h_Tbar_tW.Scale( sf_tb )
    h_Tbar_tW.Draw("GOFF")
    
    h_TTbar_semi = infile.Get("h_TTbar_semi"+shift)
    h_TTbar_semi.Rebin( rebin )
    h_TTbar_semi.Scale( sf_ttb )
    h_TTbar_semi.Draw("GOFF")
    
    h_TTbar_full = infile.Get("h_TTbar_full"+shift)
    h_TTbar_full.Rebin( rebin )
    h_TTbar_full.Scale( sf_ttb )
    h_TTbar_full.Draw("GOFF")
    
    h_Wl = infile.Get("h_Wl"+shift)
    h_Wl.Rebin( rebin )
    h_Wl.Scale( sf_wl )
    h_Wl.Draw("GOFF")
    
    h_Wc = infile.Get("h_Wc"+shift)
    h_Wc.Rebin( rebin )
    h_Wc.Scale( sf_wc )
    h_Wc.Draw("GOFF")
    
    h_Wcc = infile.Get("h_Wcc"+shift)
    h_Wcc.Rebin( rebin )
    h_Wcc.Scale( sf_wcc )
    h_Wcc.Draw("GOFF")
    
    h_Wbb = infile.Get("h_Wbb4F"+shift)
    h_Wbb.SetName("h_Wbb"+shift)
    h_Wbb.Rebin( rebin )
    h_Wbb.Scale( sf_wbb )
    h_Wbb.Draw("GOFF")
    
#######    h_mc = h_Wl.Clone()
#######    h_mc.SetName("h_mc%s"%(shift))
#######    h_mc.Add(h_Wc)
#######    h_mc.Add(h_Wcc)
#######    h_mc.Add(h_Wbb)
######    h_mc = h_WW.Clone()
######    h_mc.SetName("h_mc%s"%(shift))
######    h_mc.Add(h_WZ)
######    h_mc.Add(h_ZZ)
#####    h_mc = h_T_s.Clone()
#####    h_mc.SetName("h_mc%s"%(shift))
#####    h_mc.Add(h_T_t)
#####    h_mc.Add(h_T_tW)
#####    h_mc.Add(h_Tbar_s)
#####    h_mc.Add(h_Tbar_t)
#####    h_mc.Add(h_Tbar_tW)
####    h_mc = h_Drell.Clone()
####    h_mc.SetName("h_mc%s"%(shift))
###    h_mc = h_Wcc.Clone()
###    h_mc.SetName("h_mc%s"%(shift))
##    h_mc = h_Wbb.Clone()
##    h_mc.SetName("h_mc%s"%(shift))
#    h_mc = h_TTbar_semi.Clone()
#    h_mc.SetName("h_mc%s"%(shift))
#    h_mc.Add(h_TTbar_full)

    # add all MC for ratio plot
    h_mc = h_qcd.Clone()
    h_mc.SetName("h_mc%s"%(shift))
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
    h_mc.Add(h_Wbb)
 
    h_mc.Write()
    #print("h_mc.Integral(0,500): %s"%(h_mc.Integral(0,500)))
    integrals.append(h_mc.Integral(-1,-1))
 
   outfile.Write()
   outfile.Close
 
   #print(integrals)
   hfile = TFile(outrname) # reopen without write access
   print("Lepton : "+lep)
   print("P Space: "+cut)
   #print("Sample : "+sname)
   for i,j in zip(shifts,integrals):
    #print("h%s %s"%(i,j))
    print("h%s S/U: \t%s / %s =\t %s"%(i, j, integrals[0], j/max(integrals[0],1)))
 
   data_obs = hfile.Get("data_obs")
   data_obs.SetLineColor(c_data)
   data_obs.Draw("GOFF")
   max_data = data_obs.GetMaximum()
 
   h_mc = hfile.Get("h_mc")
   h_mc.SetLineColor(c_Raw)
   h_mc.SetLineWidth(w_Raw)
   h_mc.SetFillColor(0)
   h_mc_size = h_mc.Integral(-1,-1)
   if(h_mc_size>0.1): h_mc.Scale(1./h_mc_size)
   max_mc = max(h_mc.GetMaximum(),max_data)
   #max_mc = h_mc.GetMaximum()
   #print("h_mc: %s"%h_mc.Integral(0,100))
    
   h_mc_UESUp = hfile.Get("h_mc_UESUp")
   h_mc_UESUp.SetLineColor(c_UESUp)
   h_mc_UESUp.SetLineWidth(w_UESUp)
   h_mc_UESUp.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_UESUp.Scale(1./h_mc_UESUp.Integral(-1,-1))
   max_mc = max(h_mc_UESUp.GetMaximum(),max_mc)
   #print("h_mc_UESUp: %s"%h_mc_UESUp.Integral(0,100))
    
   h_mc_UESDown = hfile.Get("h_mc_UESDown")
   h_mc_UESDown.SetLineColor(c_UESDown)
   h_mc_UESDown.SetLineWidth(w_UESDown)
   h_mc_UESDown.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_UESDown.Scale(1./h_mc_UESDown.Integral(-1,-1))
   max_mc = max(h_mc_UESDown.GetMaximum(),max_mc)
   #print("h_mc_UESDown: %s"%h_mc_UESDown.Integral(0,100))
    
   h_mc_LESUp = hfile.Get("h_mc_LESUp")
   h_mc_LESUp.SetLineColor(c_LESUp)
   h_mc_LESUp.SetLineWidth(w_LESUp)
   h_mc_LESUp.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_LESUp.Scale(1./h_mc_LESUp.Integral(-1,-1))
   max_mc = max(h_mc_LESUp.GetMaximum(),max_mc)
   #print("h_mc_LESUp: %s"%h_mc_LESUp.Integral(0,100))
    
   h_mc_LESDown = hfile.Get("h_mc_LESDown")
   h_mc_LESDown.SetLineColor(c_LESDown)
   h_mc_LESDown.SetLineWidth(w_LESDown)
   h_mc_LESDown.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_LESDown.Scale(1./h_mc_LESDown.Integral(-1,-1))
   max_mc = max(h_mc_LESDown.GetMaximum(),max_mc)
   #print("h_mc_LESDown: %s"%h_mc_LESDown.Integral(0,100))
    
   h_mc_JESUp = hfile.Get("h_mc_JESUp")
   h_mc_JESUp.SetLineColor(c_JESUp)
   h_mc_JESUp.SetLineWidth(w_JESUp)
   h_mc_JESUp.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_JESUp.Scale(1./h_mc_JESUp.Integral(-1,-1))
   max_mc = max(h_mc_JESUp.GetMaximum(),max_mc)
   #print("h_mc_JESUp: %s"%h_mc_JESUp.Integral(0,100))
    
   h_mc_JESDown = hfile.Get("h_mc_JESDown")
   h_mc_JESDown.SetLineColor(c_JESDown)
   h_mc_JESDown.SetLineWidth(w_JESDown)
   h_mc_JESDown.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_JESDown.Scale(1./h_mc_JESDown.Integral(-1,-1))
   max_mc = max(h_mc_JESDown.GetMaximum(),max_mc)
   #print("h_mc_JESDown: %s"%h_mc_JESDown.Integral(0,100))
    
   h_mc_EMuUp = hfile.Get("h_mc_EMuUp")
   h_mc_EMuUp.SetLineColor(c_EMuUp)
   h_mc_EMuUp.SetLineWidth(w_EMuUp)
   h_mc_EMuUp.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_EMuUp.Scale(1./h_mc_EMuUp.Integral(-1,-1))
   max_mc = max(h_mc_EMuUp.GetMaximum(),max_mc)
   #print("h_mc_EMuUp: %s"%h_mc_EMuUp.Integral(0,100))
    
   h_mc_EMuDown = hfile.Get("h_mc_EMuDown")
   h_mc_EMuDown.SetLineColor(c_EMuDown)
   h_mc_EMuDown.SetLineWidth(w_EMuDown)
   h_mc_EMuDown.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_EMuDown.Scale(1./h_mc_EMuDown.Integral(-1,-1))
   max_mc = max(h_mc_EMuDown.GetMaximum(),max_mc)
   #print("h_mc_EMuDown: %s"%h_mc_EMuDown.Integral(0,100))
    
   h_mc_CSVUp = hfile.Get("h_mc_CSVUp")
   h_mc_CSVUp.SetLineColor(c_CSVUp)
   h_mc_CSVUp.SetLineWidth(w_CSVUp)
   h_mc_CSVUp.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_CSVUp.Scale(1./h_mc_CSVUp.Integral(-1,-1))
   max_mc = max(h_mc_CSVUp.GetMaximum(),max_mc)
   #print("h_mc_CSVUp: %s"%h_mc_CSVUp.Integral(0,100))
    
   h_mc_CSVDown = hfile.Get("h_mc_CSVDown")
   h_mc_CSVDown.SetLineColor(c_CSVDown)
   h_mc_CSVDown.SetLineWidth(w_CSVDown)
   h_mc_CSVDown.SetFillColor(0)
   if(h_mc_size>0.1): h_mc_CSVDown.Scale(1./h_mc_CSVDown.Integral(-1,-1))
   max_mc = max(h_mc_CSVDown.GetMaximum(),max_mc)
   #print("h_mc_CSVDown: %s"%h_mc_CSVDown.Integral(0,100))
 
   # fill legend
   leg=TLegend(0.58,0.5,0.78,0.88)
   #leg.AddEntry(data_obs,"Data")
   leg.AddEntry(h_mc,"Unshifted")
   leg.AddEntry(h_mc_UESUp,  "UES")# Up")
   #leg.AddEntry(h_mc_UESDown,"UES Down")
   leg.AddEntry(h_mc_LESUp,  "LES")# Up")
   #leg.AddEntry(h_mc_LESDown,"LES Down")
   leg.AddEntry(h_mc_JESUp,  "JES")
   #leg.AddEntry(h_mc_JESDown,"JES Down")
   leg.AddEntry(h_mc_EMuUp,  "ID/ISO/TRG")# Up")
   #leg.AddEntry(h_mc_EMuDown,"Id/Iso/Trg Down")
   leg.AddEntry(h_mc_CSVUp,  "b-Tag")
   #leg.AddEntry(h_mc_CSVDown,"b-Tag Down")
   leg.SetFillColor(0)
   leg.SetBorderSize(0)
 
   # set p1 title and axis labels
   h_mc.SetTitle("")
   h_mc.GetXaxis().SetTitle( xlabel )
   h_mc.GetXaxis().SetLabelSize(0.03)
   h_mc.GetYaxis().SetLabelSize(0.03)
   h_mc.GetYaxis().SetTitleOffset(1.5)
   h_mc.GetYaxis().SetTitle( "Events / 8 GeV" )
   #h_mc.GetYaxis().SetRangeUser(0,1.2*max_mc)
   #h_mc.GetYaxis().SetRangeUser(0,150)
   h_mc.GetYaxis().SetRangeUser(0,0.1)
 
   # and draw
   h_mc.Draw('hist')
   #print(h_mc.GetNBinsX())
   #for i in range(1,h_mc.GetNbinsX()+1):
   # h_mc.GetXaxis().SetBinLabel(i,"%s"%(i*15) ) 
   h_mc.Draw('hist')
   h_mc_CSVDown.Draw('hist,sames')
   h_mc_CSVUp.Draw('hist,sames')
   h_mc_EMuDown.Draw('hist,sames')
   h_mc_EMuUp.Draw('hist,sames')
   h_mc_JESDown.Draw('hist,sames')
   h_mc_JESUp.Draw('hist,sames')
   h_mc_LESDown.Draw('hist,sames')
   h_mc_LESUp.Draw('hist,sames')
   h_mc_UESDown.Draw('hist,sames')
   h_mc_UESUp.Draw('hist,sames')
   h_mc.Draw('hist,sames')
   #data_obs.Draw('sames,E1')
   leg.Draw()
 
   leg.Draw('sames')
   
   #cpr.wip(19700,0.05)
   cpr.prelim_alt(19700,0.05)
   tex.SetTextAlign(11) #left, bottom
   tex.DrawLatex(0.1,0.9,title)
   
   time.sleep(1)
   c.Print( outpname )
    
