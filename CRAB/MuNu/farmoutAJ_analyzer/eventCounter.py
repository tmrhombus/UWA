#!/usr/bin/python
'''
adds up the total number of evnts run over MC in a list of files
pulling info from summary/results

usage:
python eventCounter.py list_of_file_locations.txt

Author: T.M.Perry UW-Madison
'''

from sys import argv, stdout, stderr
import ROOT
import math

#Returns the number of lines in the files
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

counter = 0
total_events = 0

samplename = argv[1]
list_of_files = argv[2]
outfile_name = argv[3]

# count number of events
numfiles = file_len(list_of_files)
with open(list_of_files) as f:
 for filename in f:
  filename = filename.rstrip()
  ntuple_file = ROOT.TFile(filename)
  summary = ntuple_file.Get("summary/results")
  nr_events = summary.GetBinContent(1)
  total_events+=nr_events
  counter = counter+1

# read cross section from list 
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/StandardModelCrossSectionsat8TeV
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
if    samplename == "Drell" : xc="3531.9" # 1177.3*3 (Z/a* 50)
elif  samplename == "TTbar_full" : xc="25.1" # 239*0.324*0.324
elif  samplename == "TTbar_semi" : xc="104.7" # 239*0.324*0.676*2
elif  samplename == "T_s" : xc="3.79"
elif  samplename == "T_t" : xc="17.8" # 54.87*0.327
elif  samplename == "T_tW" : xc="11.1" 
elif  samplename == "Tbar_s" : xc="1.76"
elif  samplename == "Tbar_t" : xc="9.6" # 29.74*0.324 
elif  samplename == "Tbar_tW" : xc="11.1" 
elif  samplename == "W1Jet" : xc="36703.2" # 12234.4*3
elif  samplename == "W2Jet" : xc="36703.2" 
elif  samplename == "W3Jet" : xc="36703.2" 
elif  samplename == "W4Jet" : xc="36703.2" 
elif  samplename == "WJets" : xc="36703.2" 
elif  samplename == "Wbb4F" : xc="138.9" # 46.3*3 
elif  samplename == "WW" : xc="56.0" 
elif  samplename == "WZ" : xc="33.6"  # 21.0(W+) + 12.6(W-)
elif  samplename == "ZZ" : xc="8.2"  # m(ll)>40

outfile = open(outfile_name,'a')
outfile.write("%s Events: %s\n"%(samplename,int(total_events)))
outfile.write("%s XC: %s\n"%(samplename,xc))
outfile.close()
