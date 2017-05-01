#!/usr/bin/env python
'''
Apply pT-dependant bTag SF errors to existing J1_pt.root files
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile
import TheParameters as p
import histoRange as hr

# get parameters to run on
lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,eventTreeLocation,extraCut = p.arams() 

leafs = ['J1_pt','J2_pt']

CSVT_errors=[0.0515703,0.0264008,0.0272757,0.0275565,0.0248745,0.0218456,0.0253845,0.0239588,0.0271791,0.0273912,0.0379822,0.0411624,0.0786307,0.0866832,0.0942053,0.102403]

CSVT_ptBins=[20, 30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600,800]

for leaf in leafs:
 steps,xmin,xmax,xtitle,xunits,setLogY = hr.ranger(leaf)
 name = []
 name.append(extraName+'_'+leaf)
 for i in name:
  log = open(path+i+'.log','a')
  log.write('\nMaking bTagSF up and dn with:\n')
  log.write('  Errors: '+str(CSVT_errors)+'\n')
  log.write('  Bins: '+str(CSVT_ptBins)+'\n')
  log.write('----------------------------\n')
  log.write('----------------------------\n')
  
  theFile = TFile(path+i+'.root')
