#!/usr/bin/env python
'''
Parameters to be read by makeHistos.py and makePlotRatio.py
Author: T.M.Perry
'''

def arams():
 lumi = 13498. #luminosity 
 bNr = 0
 btype = 't'
 jNr = 2
 njetcut = '30' #20,25,26,30,40
 jetcut = '30'
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

 jetVeto = False
 Control = True #one muon
 Z_Region = False # two muons, no mT cut

 #naming where output goes
 path = '../plots/'
 fitrange = '_'+str(I)+'_'+str(F)
 extraName = str(jNr)+'j'+njetcut+jetcut+'_'+str(bNr)+'b'+btype+'_'+wSplitting
 #extraName = str(jNr)+'j'+str(bNr)+'b'+btype+fitrange
 #extraName = str(jNr)+'j'+njetcut+jetcut+'_'+str(bNr)+'b'+btype+fitrange

 #leafs = ['highestJetPt','highestJetEta','highestJetPhi','secondJetPt','secondJetEta','secondJetPhi']
 #leafs =['J1DR','J2DR']
 #leafs=['muonPt','muonEta','muonPhi']
 #leafs = ['DiMuonMass']

 #leafs=['J1CSVbtag','J2CSVbtag']
 #leafs=['J1JetParton','J2JetParton']
 #leafs = ['LHEProduct']

 leafs=['Mt','WPt','ptJJ','ht']

 #leafs = ['mJ3J4','thirdJetEta','thirdJetPhi','thirdJetPt']

 #leafs = ['MET','vertices']

 #leafs = ['highestJetPt','highestJetEta','highestJetPhi','secondJetPt','secondJetEta','secondJetPhi','J1DR','J2DR','muonPt','muonEta','muonPhi','Mt','WPt','ptJJ','ht','MET','vertices']
 return lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,wSplitting,jetVeto,Control,Z_Region
