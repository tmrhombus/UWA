#!/usr/bin/env python
'''
Dump a .png for evey histogram in file
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT, TCanvas, TLegend, gStyle
import sys 
import fnmatch as fnm 

version = "Schweincomp"
runname = "wbb_csvt_mt0_v2"
inpath = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s'%(version,runname)

infileUnshifted = sys.argv[1]
infileJESUp     = sys.argv[2]
infileJESDown   = sys.argv[3]
prename = "JESshapes_norm_"
norm = True
ps = sys.argv[4]
lep = sys.argv [5]
sample = sys.argv[6]

tsample = sample
gsample = sample
if(sample=="h_Wbb4F"):
 gsample="h_Wbb5F"
if(sample=="h_qcd" and fnm.fnmatch(ps,"tt*")):
 gsample="h_TTqcd"

rebin = 1

gStyle.SetOptStat('')
gStyle.SetLineWidth(3)
gStyle.SetPadTickY(1)

tomfile = TFile("%s/Histograms_%s_mt_%s.root"%(inpath,ps,lep))
infileUnshifted = TFile(infileUnshifted)
infileJESUp     = TFile(infileJESUp)
infileJESDown   = TFile(infileJESDown)

canx = 1200 
cany = 900

c_Raw     = 1 
c_JESUp   = 2 
c_JESDown = 3 
w_Raw     = 3 
w_JESUp   = 2 
w_JESDown = 2 
s_TR      = 1 
s_WI      = 2 

c = TCanvas('c','Canvas Named c',canx,cany)

leg=TLegend(0.58,0.5,0.78,0.88)
leg.SetFillColor(0)
leg.SetBorderSize(0)

if(sample=="h_TTbar"):
 h_wi_unsh = tomfile.Get("h_TTbar_semi")
 h_wi_part = tomfile.Get("h_TTbar_full")
 h_wi_unsh.Add(h_wi_part)
else: h_wi_unsh = tomfile.Get(tsample)
h_wi_unsh.Rebin( int(rebin) )
h_wi_unsh.SetLineColor(c_Raw)
h_wi_unsh.SetFillColor(0)
h_wi_unsh.SetLineWidth(w_Raw)
h_wi_unsh.SetLineStyle(s_WI)
size_wi = h_wi_unsh.Integral(-1,1000)
if (size_wi > 0.1 and norm): h_wi_unsh.Scale(1./size_wi)
themax = h_wi_unsh.GetMaximum()
h_wi_unsh.Draw("hist")
#raw_input("hold")

if(sample=="h_TTbar"):
 h_wi_JESUp = tomfile.Get("h_TTbar_semi_JESUp")
 h_wi_part_JESUp = tomfile.Get("h_TTbar_full_JESUp")
 h_wi_JESUp.Add(h_wi_part_JESUp)
elif(sample=="h_qcd" or sample=="data_obs"):
 h_wi_JESUp = h_wi_unsh.Clone()
 h_wi_JESUp.SetName("h_wi_JESUp")
 if(norm): h_wi_JESUp.Scale(size_wi)
else: h_wi_JESUp = tomfile.Get(tsample+"_JESUp")
h_wi_JESUp.Rebin( int(rebin) )
h_wi_JESUp.SetLineColor(c_JESUp)
h_wi_JESUp.SetFillColor(0)
h_wi_JESUp.SetLineWidth(w_JESUp)
h_wi_JESUp.SetLineStyle(s_WI)
if (size_wi > 0.1 and norm): h_wi_JESUp.Scale(1./size_wi)
themax = max(themax,h_wi_JESUp.GetMaximum())
#raw_input("hold")

if(sample=="h_TTbar"):
 h_wi_JESDown = tomfile.Get("h_TTbar_semi_JESDown")
 h_wi_part_JESDown = tomfile.Get("h_TTbar_full_JESDown")
 h_wi_JESDown.Add(h_wi_part_JESDown)
elif(sample=="h_qcd" or sample=="data_obs"):
 h_wi_JESDown = h_wi_unsh.Clone()
 h_wi_JESDown.SetName("h_wi_JESDown")
 if(norm): h_wi_JESDown.Scale(size_wi)
else: h_wi_JESDown = tomfile.Get(tsample+"_JESDown")
h_wi_JESDown.Rebin( int(rebin) )
h_wi_JESDown.SetLineColor(c_JESDown)
h_wi_JESDown.SetFillColor(0)
h_wi_JESDown.SetLineWidth(w_JESDown)
h_wi_JESDown.SetLineStyle(s_WI)
if (size_wi > 0.1 and norm): h_wi_JESDown.Scale(1./size_wi)
themax = max(themax,h_wi_JESDown.GetMaximum())
#raw_input("hold")

h_tr_unsh = infileUnshifted.Get(gsample)
h_tr_unsh.Rebin( int(rebin) )
h_tr_unsh.SetLineColor(c_Raw)
h_tr_unsh.SetFillColor(0)
h_tr_unsh.SetLineWidth(w_Raw)
h_tr_unsh.SetLineStyle(s_TR)
size_tr = h_tr_unsh.Integral(-1,1000)
if (size_tr > 0.1 and norm): h_tr_unsh.Scale(1./size_tr)
themax = max(themax,h_tr_unsh.GetMaximum())
#raw_input("hold")

h_tr_JESUp = infileJESUp.Get(gsample)
h_tr_JESUp.Rebin( int(rebin) )
h_tr_JESUp.SetLineColor(c_JESUp)
h_tr_JESUp.SetFillColor(0)
h_tr_JESUp.SetLineWidth(w_JESUp)
h_tr_JESUp.SetLineStyle(s_TR)
if (size_tr > 0.1 and norm): h_tr_JESUp.Scale(1./size_tr)
themax = max(themax,h_tr_JESUp.GetMaximum())
#raw_input("hold")

h_tr_JESDown = infileJESDown.Get(gsample)
h_tr_JESDown.Rebin( int(rebin) )
h_tr_JESDown.SetLineColor(c_JESDown)
h_tr_JESDown.SetFillColor(0)
h_tr_JESDown.SetLineWidth(w_JESDown)
h_tr_JESDown.SetLineStyle(s_TR)
if (size_tr > 0.1 and norm): h_tr_JESDown.Scale(1./size_tr)
themax = max(themax,h_tr_JESDown.GetMaximum())
#raw_input("hold")

h_wi_unsh.SetMaximum( 1.2*themax )
h_wi_unsh.Draw("hist")
leg.AddEntry(h_wi_unsh,"WI Unshifted",)
h_wi_JESUp.Draw("hist,sames")
leg.AddEntry(h_wi_JESUp,"WI JES Up",)
h_wi_JESDown.Draw("hist,sames")
leg.AddEntry(h_wi_JESDown,"WI JES Down",)
h_tr_unsh.Draw("hist,sames")
leg.AddEntry(h_tr_unsh,"TR Unshifted",)
h_tr_JESUp.Draw("hist,sames")
leg.AddEntry(h_tr_JESUp,"TR JES Up",)
h_tr_JESDown.Draw("hist,sames")
leg.AddEntry(h_tr_JESDown,"TR JES Down",)

leg.Draw("sames")
##raw_input("hold on")

c.Print(prename+sample+"_"+ps+"_"+lep+".png")

