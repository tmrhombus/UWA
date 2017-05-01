#!/usr/bin/env python
'''
Rebin histograms for 8TeV datacards 
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import sys 
import fnmatch as fnm 

inFileName = sys.argv[1]
prefix = sys.argv[2]

inFile = TFile(inFileName+".root")

outFile=gROOT.FindObject(prefix+inFileName+".root")
if outFile : outFile.Close()
outFile = TFile(prefix+inFileName+".root",'RECREATE','rebinned')

for key in inFile.GetListOfKeys():
 obj = key.ReadObj()
 if(obj.IsA().InheritsFrom("TH1")):
  h_name = obj.GetName()
  h_new = obj.Clone()
  if(fnm.fnmatch(h_name,"data_obs") or fnm.fnmatch(h_name,"*qcd*")): 
   outFile.cd()
   h_new.Write()
  elif(fnm.fnmatch(h_name,"*_*_*") and not fnm.fnmatch(h_name,"*JES*")):
   outFile.cd()
   h_new.Write()
  elif(not fnm.fnmatch(h_name,"*_*_*")):
   print("  Rescaling JES for: "+h_name)
   h_down = h_new 
   h_down.SetName(h_name+"_JESDown")
   h_norm = inFile.Get(h_name+"_JESUp")
   h_norm.SetName(h_name)
 
   h_diff = h_norm.Clone()
   h_diff.Add(h_down,-1)
 
   h_up = h_norm.Clone()
   h_up.Add(h_diff)
   h_up.SetName(h_name+"_JESUp")
 
   outFile.cd()
   h_down.Write()
   h_norm.Write()
   h_up.Write()
