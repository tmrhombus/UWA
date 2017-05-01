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
# https://github.com/amarini/VPlusJets/blob/master/post-process/xSec.ini
if    samplename == "Drell" : xc="3531.9" # 1177.3*3 (Z/a* 50)
elif  samplename == "DrellLM" : xc="860.5" 

# https://twiki.cern.ch/twiki/bin/view/LHCPhysics/TtbarNNLO 
# XC ttbar = 252.9 +- 14.5 (5.74 pc) 
elif  samplename == "TTbar_full" : xc="26.5" # 252.9*0.324*0.324
elif  samplename == "TTbar_semi" : xc="110.8" # 252.9*0.324*0.676*2
# XC t_t = 54.87 +- 2.3 (4.18 pc) 
# XC t_s = 3.79 +- 0.1 (3.90 pc) 
# XC t_w = 11.19 +- 0.8 (6.81 pc) 
# XC tb_t = 29.74 +- 1.7 (5.60 pc) 
# XC tb_s = 1.76 +- 0.1 (4.58 pc) 
# XC tb_w = 11.19 +- 0.8 (6.81 pc)
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/SingleTopSigma
elif  samplename == "T_t" : xc="17.8" # 54.87*0.327
elif  samplename == "T_s" : xc="3.79"
elif  samplename == "T_tW" : xc="11.19" 
elif  samplename == "Tbar_t" : xc="9.6" # 29.74*0.324 
elif  samplename == "Tbar_s" : xc="1.76"
elif  samplename == "Tbar_tW" : xc="11.19" 

elif  samplename == "W1Jet" : xc="36703.2" # 12234.4*3
elif  samplename == "W2Jet" : xc="36703.2" 
elif  samplename == "W3Jet" : xc="36703.2" 
elif  samplename == "W4Jet" : xc="36703.2" 
elif  samplename == "WJets" : xc="36703.2" 
elif  samplename == "Wbb4F" : xc="122.3" # 377.4 * 3(0.108)
#elif  samplename == "Wbb4F" : xc="138.9" # 46.3*3  .. where did this come from?
elif  samplename == "WW" : xc="56.0" 
elif  samplename == "WZ" : xc="33.6"  # 21.0(W+) + 12.6(W-)
elif  samplename == "ZZ" : xc="8.2"  # m(ll)>40
elif  samplename == "GJ40to100"  : xc="20709.1" 
elif  samplename == "GJ100to200" : xc="5319.97" 
elif  samplename == "GJ200to400" : xc="972.735"
elif  samplename == "GJ400toInf" : xc="106.721"
elif  samplename == "QCDBCtoE20to30"   : xc="167410.04" 
elif  samplename == "QCDBCtoE30to80"   : xc="167353.425" 
elif  samplename == "QCDBCtoE80to170"  : xc="12970.564" 
elif  samplename == "QCDBCtoE170to250" : xc="631.54728" 
elif  samplename == "QCDBCtoE250to350" : xc="103.119966" 
elif  samplename == "QCDBCtoE350toInf" : xc="23.893702" 

outfile = open(outfile_name,'a')
outfile.write("%s Events: %s\n"%(samplename,int(total_events)))
outfile.write("%s XC: %s\n"%(samplename,xc))
outfile.close()



 # ttbar from cms measurement  239 +-2(stat)+-11(syst)+-6(lumi)
 # ttbar from cms/atlas theory agreement 252.9 +6.4-8.6(scale) +-11.7(pdf+alpha_s)
#elif  samplename == "TTbar_full" : xc="25.1" # 239*0.324*0.324
#elif  samplename == "TTbar_semi" : xc="104.7" # 239*0.324*0.676*2
