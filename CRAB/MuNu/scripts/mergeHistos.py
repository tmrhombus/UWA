#!/usr/bin/env python
'''
 Merges histograms from the output of
 callHistoFiller.cc into one file
 Author: T.M.Perry UW-Madison
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import fnmatch as fnm

lep = 'ele'
lep = 'mu'
cut = 'wbb'
shift = 'SFs'
doShifts = False

variable = 'mt'

path = '../plots/'

mc_samples = [
 "TTbar_full", 
 "TTbar_semi", 
 "T_s", 
# "T_t", 
# "T_tW", 
# "Tbar_s", 
# "Tbar_t", 
# "Tbar_tW", 
# "Wbb4F", 
# "WW", 
# "WZ", 
# "ZZ" 
]
w_samples = [
 "WlN", "WcN", "WccN", "WbbN",
 "Wl1", "Wc1", "Wcc1", "Wbb1",
 "Wl2", "Wc2", "Wcc2", "Wbb2",
 "Wl3", "Wc3", "Wcc3", "Wbb3",
 "Wl4", "Wc4", "Wcc4", "Wbb4"
]
data_samples = [ "Data" ]

outFile=gROOT.FindObject(path+'Histograms_'+variable+"_"+cut+"_"+lep+'.root')
if outFile : outFile.Close()
outFile = TFile(path+'Histograms_'+variable+"_"+cut+"_"+lep+'.root','RECREATE','Histograms')

for mc_sample in mc_samples:
 name = mc_sample+"_"+lep+"MC"+qcd+"_"+cut+shift
 print name
 inFile = TFile(path+name+'.root')
 if( fnm.fnmatch(shift,"aucun") or fnm.fnmatch(shift,"SFs") ):
  for key in inFile.GetListOfKeys():
   obj = key.ReadObj()
   if(obj.IsA().InheritsFrom("TH1")):
    h_name = obj.GetName() 
    if( fnm.fnmatch(h_name,'h_'+variable) ):
     #nBins = obj.GetNbinsX()
     #h_new = TH1F(mc_sample,mc_sample,nBins+1,0,nBins+1)
     #print h_name
     #for i in xrange(1,nBins+2):
     # content = max(0.000000001,obj.GetBinContent(i))
     # h_new.SetBinContent(i,content)
     #h_new.Draw()
     obj.Draw()
     raw_input("hold on")
     outFile.cd()
     outFile.Write()
