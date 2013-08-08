#!/usr/bin/env python
'''
Parameters to be read by makeHistos.py and makePlotRatio.py
Author: T.M.Perry
'''

def arams():
 lumi = 19429.
 btype = 't'
 njetcut = '25' #20,25,26,30,40
 jetcut = '25'
 I = 0
 F = 20
 iso_value = 0.12
 antiIso_value = 0.2

 drawQCD = True
 drawData = True

 Control = False #one muon
 Signal = False
 noMT = False # control but no mT cut
 TT_m = False #1 mu, 2b's, 4 j
 TT_me = False #no b's, 1mu 1e
 ST = True
 Z_Region = False # two muons, no mT cut
 Legacy = False #voids everything else and puts parametrs from 7Tev analysis
 
 bNr = 0
 jNr = 2
 jetVeto = False

 if Signal or Legacy:
  bNr = 2
  jNr = 2
  jetVeto = True
 elif Control or noMT:
  bNr = 0 
  jNr = 2
  jetVeto = False
 elif TT_m:
  bNr = 2
  jNr = 4
  jetVeto = True
 elif TT_me:
  bNr = 0 
  jNr = 4
  jetVeto = False
 elif Z_Region:
  bNr = 0
  jNr = 2
  jetVeto = False
 elif ST:
  bNr = 1
  jNr = 2
  jetVeto = False

 drawW = False # line at W when plotting
 drawZ = False # line at Z when plotting

 #naming where output goes
 path = '../plots/'
 fitrange = '_'+str(I)+'_'+str(F)
 extraName = str(jNr)+'j'+njetcut+jetcut+'_'+str(bNr)+'b'+btype+'_oldT'

 jet1_2dr2 = '(((highestJetEta-secondJetEta)*(highestJetEta-secondJetEta))+((highestJetPhi-secondJetPhi)*(highestJetPhi-secondJetPhi)))'

 #leafs = ['highestJetPt','highestJetEta','highestJetPhi','secondJetPt','secondJetEta','secondJetPhi','MET']
 #leafs = ['secondJetPt','secondJetEta','secondJetPhi']
 #leafs = ['highestJetPt']
 leafs = ['highestJetPt','highestJetEta','highestJetPhi','muonCharge']
 #leafs =['J1DR','J2DR']
 #leafs=['muonPt']
 #leafs=['nJetsPt30']
 #leafs=['muonPt','muonEta','muonPhi']
 #leafs = ['DiMuonMass']
 
 #leafs = ['J1SVMassb',jet1_2dr2]
 #leafs = ['J2SVMassb']
 #leafs = ['J1SVMassb','J2SVMassb']

 #leafs = ['dz']
 #leafs = ['muonCharge']
 #leafs=['J1CSVbtag','J2CSVbtag']
 #leafs=['J1JetParton','J2JetParton']
 #leafs = ['LHEProduct']

 #leafs=['MET','WPt','ptJJ','ht']
 #leafs=['Mt']

 #leafs = ['mJ3J4','thirdJetEta','thirdJetPhi','thirdJetPt']

 #leafs = ['MET','vertices']
 #leafs = ['vertices']

 #leafs = ['secondJetEta','secondJetPhi','J1DR','J2DR','muonPt','muonEta','muonPhi','Mt','WPt','ptJJ','ht','MET','vertices']
 #leafs = ['highestJetPt','highestJetEta','highestJetPhi','secondJetPt','secondJetEta','secondJetPhi','J1DR','J2DR','muonPt','muonEta','muonPhi','Mt','WPt','ptJJ','ht','MET','vertices']
 #leafs = ['J1DR','J2DR','muonPt','muonEta','muonPhi','Mt','WPt','ptJJ','ht','MET','vertices',jet1_2dr2,'nJetsPt30','nJetsPt20']

 return lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal

