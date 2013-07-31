#!/usr/bin/env python
'''
Parameters to be read by makeHistos.py and makePlotRatio.py
Author: T.M.Perry
'''

def arams():
 lumi = 19429. #19109. # old 13498.
 bNr = 0
 btype = 't'
 jNr = 2
 njetcut = '25' #20,25,26,30,40
 jetcut = '25'
 I = 0
 F = 20
 iso_value = 0.12
 antiIso_value = 0.2
 wSplitting = 'had'
 #wSplitting = 'par'

 #drawQCD = False
 drawQCD = True
 #drawData = False
 drawData = True
 drawW = False
 #drawW = True
 drawZ = False
 #drawZ = True

 jetVeto = True
 Control = True #one muon
 Z_Region = False # two muons, no mT cut
 legacy = False #voids everything else and puts parametrs from 7Tev analysis

 #naming where output goes
 path = '../plots/'
 fitrange = '_'+str(I)+'_'+str(F)
 extraName = str(jNr)+'j'+njetcut+jetcut+'_'+str(bNr)+'b'+btype

 return lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,drawW,drawZ,drawQCD,drawData,wSplitting,jetVeto,Control,Z_Region,legacy
