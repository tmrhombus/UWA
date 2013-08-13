#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(bNr,jNr,jetVeto):

 jetPt = '25'
 njetPt = '25'
 isolationValue=0.12

 weight = '(weightFactor * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig * 19429.0)'
 Iso='(lPFIsoDB<'+str(isolationValue)+')'

 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 oneMUoneELE = '(DiMuonMass<=60 && nElectrons==1 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
 mt = '(Mt>45)'
 noFJ = '(nJets24Pt25==0)'

 twJ = '(highestJetPt >'+jetPt+' && secondJetPt>'+jetPt+' && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4)'
 thJ = '('+twJ+'&& thirdJetPt >'+jetPt+' && abs(thirdJetEta)<2.4)'
 frJ = '('+thJ+'&& mJ3J4 > 0)'
 if not jetVeto:
  twoJets   = '('+twJ+' && nJetsPt'+njetPt+'>=2)'
  threeJets = '('+thJ+' && nJetsPt'+njetPt+'>=3)'
  fourJets  = '('+frJ+' && nJetsPt'+njetPt+'>=4)'
 if jetVeto:
  twoJets   = '('+twJ+' && nJetsPt'+njetPt+'==2)'
  threeJets = '('+thJ+' && nJetsPt'+njetPt+'==3)'
  fourJets  = '('+frJ+' && nJetsPt'+njetPt+'==4)'


 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+')' #control or signal
 #Skim='('+trigger+'&&'+oneMUoneELE+'&&'+vertex+'&&'+mt+')' #for TTbar
 Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+')' #for TTbar
 #Skim='('+trigger+'&&'+dimuon_selection+'&&'+vertex+')' # Z region
  
 FirstBtag='(J1CSVbtag>0.898 && J1SVMassb>0)'
 SecondBtag='(J2CSVbtag>0.898 && J2SVMassb>0)'
 OneBtag='('+FirstBtag+'||'+SecondBtag+')'
 TwoBtag='('+FirstBtag+'&&'+SecondBtag+')'

 newCSVT1first = '((0.927563+(1.55479e-05*highestJetPt))+(-1.90666e-07*(highestJetPt*highestJetPt)))'
 newCSVT1second = '((0.927563+(1.55479e-05*secondJetPt))+(-1.90666e-07*(secondJetPt*secondJetPt)))'
 newCSVT2 = '('+newCSVT1first+'*'+newCSVT1second+')'

 #theCut = '('+Skim+'&&'+twoJets+')'        #control
 #theCut = '('+Skim+'&&'+exactlyTwoJets+')' #signal
 theCut = '('+Skim+'&&'+fourJets+')'       #ttbar 4 jets

 weight = '('+weight+'*'+newCSVT2+')'      # TWO BTAGS
 theCut = '('+theCut+'&&'+TwoBtag+')'      # TWO BTAGS

 cutMc = '('+weight+'*weightTop*('+Iso+'&&'+theCut+'))'
 cutMcUp = '('+weight+'*weightTop*weightTop*('+Iso+'&&'+theCut+'))'
 cutMcDown = '('+weight+'*('+Iso+'&&'+theCut+'))'
 return cutMc,cutMcUp,cutMcDown

