#!/usr/bin/env python
'''
Dump a .png for evey histogram in file
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT, TCanvas, TLegend, gStyle
import sys 
import fnmatch as fnm 

version = "Qercury"
runname = "wbb_csvt_mt0_counting4"
inpath = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s'%(version,runname)

infileUnshifted = sys.argv[1]
infileJESUp     = sys.argv[2]
infileJESDown   = sys.argv[3]
prename = ""
ps = sys.argv[4]
lep = sys.argv [5]
sample = sys.argv[6]

tsample = sample
gsample = sample
if(sample=="wbb"):
 tsample="h_Wbb4F"
 gsample="h_Wbb5F"

sampleinfo = "_"+ps+"_"+lep+"_normalized" # "_tttjjj_mu"
rebin = 1

gStyle.SetOptStat('')
gStyle.SetLineWidth(3)
gStyle.SetPadTickY(1)

tomfile = TFile("%s/Histograms_%s_mt_%s.root"%(inpath,ps,lep))
infileUnshifted = TFile(infileUnshifted)
infileJESUp     = TFile(infileJESUp)
infileJESDown   = TFile(infileJESDown)

canx = 900 
cany = 900

c_Raw = 4 
c_JESUp   = 5 
c_JESDown = 6 
w_Raw     = 3 
w_JESUp   = 2 
w_JESDown = 2 
s_Raw     = 2 
s_JESUp   = 2 
s_JESDown = 2 

shifts = ["","_JESUp","_JESDown"]
for shift in shifts:
 h_t_unsh = infile.Get(tsample)

 # add all MC for ratio plot
 h_mc = h_qcd.Clone()
 h_mc.SetName("h_mc%s"%(shift))
 h_mc.Add(h_Drell)

for key in infileUnshifted.GetListOfKeys():
 c = TCanvas('c','Canvas Named c',canx,cany)
 obj = key.ReadObj()
 if(obj.IsA().InheritsFrom("TH1")):
  h_name_unsh = obj.GetName()
  h_unsh = obj.Clone()
  h_unsh.Rebin( int(rebin) )
  h_unsh.SetLineColor(1)
  h_unsh.SetFillColor(0)
  h_unsh.SetLineWidth(3)
  unsh_size = h_unsh.Integral(-1,1000)
  #print("unsh_size: %s"%(unsh_size))
  if (unsh_size > 0.1): h_unsh.Scale(1./unsh_size)
  h_unsh.Draw("hist")

 leg=TLegend(0.58,0.5,0.78,0.88)
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 leg.AddEntry(h_unsh,"TR Unshifted")
 for keyJESUp in infileJESUp.GetListOfKeys():
  objJESUp = keyJESUp.ReadObj()
  if(objJESUp.IsA().InheritsFrom("TH1")):
   h_name_JESUp = objJESUp.GetName()
   if(h_name_JESUp==h_name_unsh):
    h_JESUp = objJESUp.Clone()
    h_JESUp.Rebin( int(rebin) )
    h_JESUp.SetLineColor(2)
    h_JESUp.SetFillColor(0)
    h_JESUp.SetLineWidth(2)
    #print("unsh_size: %s"%(unsh_size))
    #print("h_JESUp.Integral(-1,1000): %s"%(h_JESUp.Integral(-1,1000)))
    if (unsh_size > 0.1):
     h_JESUp.Scale(1./unsh_size)
     #print("unsh_size > 0.1")
    #print("h_JESUp.Integral(-1,1000): %s"%(h_JESUp.Integral(-1,1000)))
    h_JESUp.Draw("hist,sames")
    leg.AddEntry(h_JESUp,"TR JES Up")

    for keyJESDown in infileJESDown.GetListOfKeys():
     objJESDown = keyJESDown.ReadObj()
     if(objJESDown.IsA().InheritsFrom("TH1")):
      h_name_JESDown = objJESDown.GetName()
      if(h_name_JESDown==h_name_unsh):
       h_JESDown = objJESDown.Clone()
       h_JESDown.Rebin( int(rebin) )
       h_JESDown.SetLineColor(3)
       h_JESDown.SetFillColor(0)
       h_JESDown.SetLineWidth(2)
       #print("unsh_size: %s"%(unsh_size))
       #print("h_JESDown.Integral(-1,1000): %s"%(h_JESDown.Integral(-1,1000)))
       if (unsh_size > 0.1): h_JESDown.Scale(1./unsh_size)
       #print("h_JESDown.Integral(-1,1000): %s"%(h_JESDown.Integral(-1,1000)))
       h_JESDown.Draw("hist,sames")
       leg.AddEntry(h_JESDown,"TR JES Down")
   

       leg.Draw('sames')

       c.Print(prename+h_name_unsh+sampleinfo+".png")

