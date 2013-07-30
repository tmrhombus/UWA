#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker():

 jetPt = '25'
 njetPt = '25'
 isolationValue=0.12

 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
 mt = '(Mt>45)'
 noFJ = '(nJets24Pt25==0)'

 twJ = '(highestJetPt >'+jetPt+' && secondJetPt>'+jetPt+' && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4)'
 twoJets   = '('+twJ+' && nJetsPt'+njetPt+'>=2)'

 Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+')'
 Iso='(lPFIsoDB<'+str(isolationValue)+')'

 #weightW = '1'
 weightW = '(weightFactorW)'
  
 theCut = '('+Skim+'&&'+twoJets+')'

 cutMcIso = '('+weightW+ '*('+Iso+'&&'+theCut+'))'
 return cutMcIso

