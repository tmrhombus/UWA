#!/usr/bin/env python
'''
Dump a .png for evey histogram in file
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT, TCanvas
import sys 
import fnmatch as fnm 
import time

inFileName = sys.argv[1]
prename = ""

rebin = 1

inFile = TFile(inFileName+".root")

canx = 900 
cany = 1200

c = TCanvas('c','Canvas Named c',canx,cany)

for key in inFile.GetListOfKeys():
 obj = key.ReadObj()
 if(obj.IsA().InheritsFrom("TH1")):
  h_name = obj.GetName()
  h_new = obj.Clone()
  h_new.Rebin( int(rebin) )
  h_new.SetLineColor(1)
  h_new.SetLineWidth(2)
  h_new.SetFillColor(0)
  h_new.Draw("hists")
  #time.sleep(1)
  c.Print(prename+inFileName+"_"+h_name+".png")
