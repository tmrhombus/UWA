#!/usr/bin/env python
'''
for Wbb analysis, function outputs vector of cut strings
Author: T.M.Perry UW-Madison
'''

def utList(isolationValue=0.12,antiIsoValue=0.2,lumi=19429.,njetPt='25',jetPt='25',jetVeto=False):

 cuts={}

 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 oneMUoneELE = '(DiMuonMass<=60 && nElectrons==1 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 dimuon_selection = '(nMuons==2&&abs(muonEta)<2.1&&muonPt>25)'
 vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
 vertexNoDZ = '(abs(l1DXY)<0.02)'
 mt = '(Mt>45)'
 met = '(MET>30)'
 noFJ = '(nJets24Pt25==0)'
 oneFJ = '(nJets24Pt25==1)'
 muPlus = '(muonCharge > 0)'
 muMinus = '(muonCharge < 0)'
 Iso='(lPFIsoDB<'+str(isolationValue)+')'
 NonIso ='(lPFIsoDB>='+str(antiIsoValue)+')'

 twJ = '(highestJetPt >'+jetPt+' && secondJetPt>'+jetPt+' && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4)'
 thJ = '('+twJ+'&& thirdJetPt >'+jetPt+' && abs(thirdJetEta)<2.4)'
 frJ = '('+thJ+'&& mJ3J4 > 0)'
 cuts['twoJetsP'] = '('+twJ+' && nJetsPt'+njetPt+'>=2)'
 cuts['threeJetsP'] = '('+thJ+' && nJetsPt'+njetPt+'>=3)'
 cuts['fourJetsP'] = '('+frJ+' && nJetsPt'+njetPt+'>=4)'
 cuts['twoJetsE'] = '('+twJ+' && nJetsPt'+njetPt+'==2)'
 cuts['threeJetsE'] = '('+thJ+' && nJetsPt'+njetPt+'==3)'
 cuts['fourJetsE'] = '('+frJ+' && nJetsPt'+njetPt+'==4)'

 cuts['SkimControl']='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+twJ+')'
 #cuts['SkimControl']='('+trigger+'&&'+muon_selection+'&&'+vertex+')'
 cuts['mt']='('+mt+')'
 cuts['noFJ']='('+noFJ+')'
 cuts['SkimTT_me']='('+trigger+'&&'+oneMUoneELE+'&&'+vertex+')'
 cuts['SkimTT_m']='('+trigger+'&&'+muon_selection+'&&'+vertex+')'
 cuts['Skim_Z']='('+trigger+'&&'+dimuon_selection+'&&'+vertex+')'
 cuts['Iso']='('+Iso+')'
 cuts['NonIso']='('+NonIso+')'

 weightEff = '(weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig)'
 weight = '(weightFactor*'+str(lumi)+'*'+str(weightEff)+')'

 bcut = 0.898
  
 FirstBtag='(J1CSVbtag>'+str(bcut)+'&&J1SVMassb>0)'
 SecondBtag='(J2CSVbtag>'+str(bcut)+'&&J2SVMassb>0)'
 OneBtag='('+FirstBtag+'||'+SecondBtag+')'
 TwoBtag='('+FirstBtag+'&&'+SecondBtag+')'

 cuts['FirstBtag']  =  FirstBtag
 cuts['SecondBtag'] =  SecondBtag
 cuts['OneBtag']    =  OneBtag
 cuts['TwoBtag']    =  TwoBtag

 newCSVT1first = '((0.927563+(1.55479e-05*highestJetPt))+(-1.90666e-07*(highestJetPt*highestJetPt)))'
 newCSVT1second = '((0.927563+(1.55479e-05*secondJetPt))+(-1.90666e-07*(secondJetPt*secondJetPt)))'
 newCSVT2 = '('+newCSVT1first+'*'+newCSVT1second+')'

 oldCSVT2 = '(0.901615*(1+0.552628*highestJetPt)/(1+(0.547195*highestJetPt)))*(0.901615*(1+0.552628*secondJetPt)/(1+(0.547195*secondJetPt)))'

 cuts['oneTB']='(('+FirstBtag+'*'+newCSVT1first+')||('+SecondBtag+'*'+newCSVT1second+')))'
 cuts['twoTB']='('+TwoBtag+'*'+newCSVT2+')'

 # for splitting up the W sample 
 genB = '(nbHadrons>0)' #to do this correctly, must match to jets
 genC = '((ncCands+ncbarCands)>0)'
 evenC = '(((ncCands+ncbarCands)%2)==0)'
 
 Wl = '((!'+genB+'&&!'+genC+'))'
 Wc = '((!'+genB+'&&'+genC+'&&!'+evenC+'))'
 Wcc = '((!'+genB+'&&'+genC+'&&'+evenC+'))'
 Wbb = '('+genB+')'

 return cuts,Wl,Wc,Wcc,Wbb,Iso,NonIso,weight
