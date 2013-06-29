#!/usr/bin/env python
'''
Parameters to be read by makeHistos.py and makePlotRatio.py
Author: T.M.Perry
'''

def arams():
 lumi = 13498. #luminosity 
 bNr = 2       # nr of b's
 btype = 't'   # tag t,m,l
 jNr = 2       # nr of jets
 I = 0         # print integral from 
 F = 20        # ... to in .log
 iso_value = 0.12
 antiIso_value = 0.2

 #drawQCD = False
 drawQCD = True
 drawW = False
 #drawW = True
 drawZ = False
 #drawZ = True

 #naming where output goes
 path = '../plots/jets20_'
 fitrange = '_'+str(I)+'_'+str(F)
 extraName = str(jNr)+'j'+str(bNr)+'b'+btype+fitrange

 leafs = ['muonPt','MET','vertices','muonPhi','WPt','DiMuonMass','mJ3J4','ptJJ','met','MtCal','muonEta','ht','highestJetEta','secondJetEta','thirdJetEta','highestJetPhi','secondJetPhi','thirdJetPhi','highestJetPt','secondJetPt','thirdJetPt']

 return lumi,bNr,btype,jNr,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD
