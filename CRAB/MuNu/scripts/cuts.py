#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(isolationValue=0.12,antiIsoValue=0.2,lumi=13498.,massTrans=50,bnr=0,btype='t',jnr=2):
 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(nMuons==1&&abs(muonEta)<2.1&&muonPt>25)'
 dimuon_selection = '(nMuons==2&&abs(muonEta)<2.1&&muonPt>25)'
 vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
 twoJets = '(nJetsPt25>=2 && highestJetPt>30 && secondJetPt>30 && abs(highestJetEta)<2.5 && abs(secondJetEta)<2.5)'
 threeJets = '('+twoJets+'&& nJetsPt25>=3 && thirdJetPt>30 && abs(thirdJetEta)<2.5)'
 mt = '(Mt>'+str(massTrans)+')'

 Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+')'
 Z='('+trigger+'&&'+dimuon_selection+'&&'+vertex+')'
 Iso='(lPFIsoDB<'+str(isolationValue)+')'
 NonIso ='(lPFIsoDB>='+str(antiIsoValue)+')'
 
 trigEff = 0.98
 #trigEff= '(EffWEIGHTpt*EffWEIGHTtrigeta)'
 weight = '('+'theWeight2*'+str(lumi)+'*'+str(trigEff)+')'
 weightW = '('+'__WEIGHT__*'+str(lumi)+'*'+str(trigEff)+')'

 if btype == 'tight' or 't':
  bcut = 0.898
 if btype == 'medium' or 'med' or 'm':
  bcut = 0.679
 if btype == 'loose' or 'l':
  bcut = 0.244
  
 OneBtag='((J1CSVbtag>'+str(bcut)+')||(J2CSVbtag>'+str(bcut)+')'
 TwoBtag='((J1CSVbtag>'+str(bcut)+')&&(J2CSVbtag>'+str(bcut)+')'

 theCut = Skim
 if bnr == 1:
  if btype == 'tight' or 't':
   beffWeight = EffWEIGHTCSVT
  if btype == 'medium' or 'med' or 'm':
   beffWeight = EffWEIGHTCSVM
  if btype == 'loose' or 'l':
   beffWeight = EffWEIGHTCSVL
  theCut = '('+theCut+'&&'+OneBtag+')'
  weight = '('+weight+'*'+beffWeight+')'

 if bnr == 2:
  if btype == 'tight' or 't':
   beffWeight = EffWEIGHTCSVT2
  if btype == 'medium' or 'med' or 'm':
   beffWeight = EffWEIGHTCSVM2
  if btype == 'loose' or 'l':
   beffWeight = EffWEIGHTCSVL2
  theCut = '('+theCut+'&&'+TwoBtag+')'
  weight = '('+weight+'*'+beffWeight+')'

 if jnr == 2:
  theCut = '('+theCut+'&&'+twoJets+')'
 if jnr >= 3:
  theCut = '('+theCut+'&&'+threeJets+')'
 
 cutMcNonIso = '('+weight+'*('+NonIso+'&&'+theCut+'))'
 cutMcIso = '('+weight+'*('+Iso+'&&'+theCut+'))'
 cutDataNonIso = '('+NonIso+'&&'+theCut+')'
 cutDataIso = '('+Iso+'&&'+theCut+')'
 cutMcWNonIso = '('+weightW+'*('+NonIso+'&&'+theCut+'))'
 cutMcWIso = '('+weightW+'*('+Iso+'&&'+theCut+'))'

 # for splitting up the W sample
 genB = '(nbHadrons>0)'
 genC = '((ncCands+ncbarCands)>0)'
 evenC = '(((ncCands+ncbarCands)%2)==0)'
 
 Wl = '((!'+genB+'&&!'+genC+'))'
 Wc = '((!'+genB+'&&'+genC+'&&!'+evenC+'))'
 Wcc = '((!'+genB+'&&'+genC+'&&'+evenC+'))'
 Wbb = '('+genB+')'

 cutMcWlNonIso  = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wl+'))'
 cutMcWlIso     = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wl+'))'
 cutMcWcNonIso  = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wc+'))'
 cutMcWcIso     = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wc+'))'
 cutMcWccNonIso = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wcc+'))'
 cutMcWccIso    = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wcc+'))'
 cutMcWbbNonIso = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wbb+'))'
 cutMcWbbIso    = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wbb+'))'
 return cutMcNonIso, cutMcIso, cutDataNonIso, cutDataIso, cutMcWNonIso, cutMcWIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso

#CutsMCn,CutsMCi,CutsDatan,CutsDatai,CutsMCnw,CutsMCiw,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb 
#Wtau = '(abs(genWLeptonID)!=13)'
#Wbx = '(genWBs==1&&abs(genWLeptonID)==13)'
#Wbb = '(genWBs>1&&abs(genWLeptonID)==13)'
#Wcc='(genWBs<1&&(foundC>0&&foundCbar>0)&&(abs(foundC-foundCbar)%2==0&&abs(genWLeptonID)==13))'
#Wc='(genWBs<1&&(foundC>0||foundCbar>0)&&(abs(foundC-foundCbar)%2!=0)&&abs(genWLeptonID)==13)'
#Wl = '(genWBs<1&&foundC<=0&&foundCbar<=0&&abs(genWLeptonID)==13)'

#CutsWtaui =  '('+TD+'*('+Wtau+'&&'+Iso+theCut+'))'
#CutsWbxi = '('+TD+'*('+Wbx+'&&'+Iso+theCut+'))'
#CutsWbbi = '('+TD+'*('+Wbb+'&&'+Iso+theCut+'))'
#CutsWcci =  '('+TD+'*('+Wcc+'&&'+Iso+theCut+'))'
#CutsWci =  '('+TD+'*('+Wc+'&&'+Iso+theCut+'))'
#CutsWli = '('+TD+'*('+Wl+'&&'+Iso+theCut+'))'
