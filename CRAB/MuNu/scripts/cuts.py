#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(isolationValue=0.12,antiIsoValue=0.2,lumi=19109.,bnr=0,btype='t',jnr=2,njetPt='20',jetPt='20',jetVeto=False,wSplitting='had',Control=True,Z_Region=False,legacy=False,noMT=False):

 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 oneMUoneELE = '(DiMuonMass<=60 && nElectrons==1 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)'
 dimuon_selection = '(nMuons==2&&abs(muonEta)<2.1&&muonPt>25)'
 vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
 vertexNoDZ = '(abs(l1DXY)<0.02)'
 mt = '(Mt>45)'
 noFJ = '(nJets24Pt25==0)'
 muPlus = '(muonCharge > 0)'
 muMinus = '(muonCharge < 0)'

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

 Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+')'
 SkimNoMT='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+noFJ+')' #for QCD
 #Skim='('+trigger+'&&'+oneMUoneELE+'&&'+vertex+'&&'+mt+')' #for TTbar
 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertexNoDZ+'&&'+noFJ+')'
 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+'&&'+muPlus+')'
 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+'&&'+muMinus+')'

 Iso='(lPFIsoDB<'+str(isolationValue)+')'
 NonIso ='(lPFIsoDB>='+str(antiIsoValue)+')'
 Z='('+trigger+'&&'+dimuon_selection+'&&'+vertex+')'

 weightEff = '(weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig)'
 weight = '('+' weightFactor*' +str(lumi)+'*'+str(weightEff)+')'
 weightW = '('+'weightFactorW*'+str(lumi)+'*'+str(weightEff)+')'

 if legacy:
  Iso='(lPFIsoDB<0.12)'
  NonIso ='(lPFIsoDB>=0.2)'
  theCut = '(nMuons==1 && abs(muonEta)<2.1 && muonPt>25 && highestJetPt > 25 && secondJetPt > 25 && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4 && nJetsPt25==2 && (J1CSVbtag>0.898) && (J2CSVbtag>0.898) && J1SVMassb>0 && J2SVMassb>0 && DiMuonMass<=60 && nElectrons==0 && nJets24Pt25==0 && Mt > 45 && (abs(dz)<0.5&&abs(l1DXY)<0.02) )'
  weight = '(weightFactor*'+str(lumi)+'*'+str(weightEff)+'*EffWEIGHTCSVT)'
  weightW = '(weightFactorW*'+str(lumi)+'*'+str(weightEff)+'*EffWEIGHTCSVT)'


 if btype == 'tight' or btype == 't':
  bcut = 0.898
 if btype == 'medium' or btype == 'med' or btype == 'm':
  bcut = 0.679
 if btype == 'loose' or btype == 'l':
  bcut = 0.244
  
 OneBtag='((J1CSVbtag>'+str(bcut)+'&&J1SVMassb>0)||(J2CSVbtag>'+str(bcut)+'&&J2SVMassb>0))'
 TwoBtag='((J1CSVbtag>'+str(bcut)+'&&J1SVMassb>0)&&(J2CSVbtag>'+str(bcut)+'&&J2SVMassb>0))'

 if Control:
  theCut = Skim
 elif Z_Region:
  theCut = Z
 elif noMT:
  theCut = SkimNoMT
 else:
  print("\n\n In parameters.py, choose Control or Z_Region True\n\n")

 newCSVT2 = '(0.927563+(1.55479e-05*highestJetPt))+(-1.90666e-07*(highestJetPt*highestJetPt))*(0.927563+(1.55479e-05*secondJetPt))+(-1.90666e-07*(secondJetPt*secondJetPt))'
 oldCSVT2 = '(0.901615*(1+0.552628*highestJetPt)/(1+(0.547195*highestJetPt)))*(0.901615*(1+0.552628*secondJetPt)/(1+(0.547195*secondJetPt)))'

 if bnr == 1:
  if btype == 'tight' or btype == 't':
   beffWeight = 'EffWEIGHTCSVT'
  if btype == 'medium' or btype == 'med' or btype == 'm':
   beffWeight = 'EffWEIGHTCSVM'
  if btype == 'loose' or btype == 'l':
   beffWeight = 'EffWEIGHTCSVL'
  theCut = '('+theCut+'&&'+OneBtag+')'
  weight = '('+weight+'*'+beffWeight+')'

 if bnr == 2:
  if btype == 'tight' or btype == 't':
   beffWeight = newCSVT2
   #beffWeight = 'EffWEIGHTCSVT2'
  if btype == 'medium' or btype == 'med' or btype == 'm':
   beffWeight = 'EffWEIGHTCSVM2'
  if btype == 'loose' or btype == 'l':
   beffWeight = 'EffWEIGHTCSVL2'
  theCut = '('+theCut+'&&'+TwoBtag+')'
  weight = '('+weight+'*'+beffWeight+')'

 if jnr == 2:
  theCut = '('+theCut+'&&'+twoJets+')'
 if jnr == 3:
  theCut = '('+theCut+'&&'+threeJets+')'
 if jnr == 4:
  theCut = '('+theCut+'&&'+fourJets+')'

 if wSplitting == 'had':
  # for splitting up the W sample :: hadron splitting
  genB = '(nbHadrons>0)' #to do this correctly, must match to jets
  genC = '((ncCands+ncbarCands)>0)'
  evenC = '(((ncCands+ncbarCands)%2)==0)'
  
  Wl = '((!'+genB+'&&!'+genC+'))'
  Wc = '((!'+genB+'&&'+genC+'&&!'+evenC+'))'
  Wcc = '((!'+genB+'&&'+genC+'&&'+evenC+'))'
  Wbb = '('+genB+')'

 if wSplitting == 'par':
  # alternative way to split W  :: parton splitting
  twoBs = '(abs(J1JetParton)==5 && abs(J2JetParton)==5)'
  twoCs = '(abs(J1JetParton)==4 && abs(J2JetParton)==4)'
  oneC = '(abs(J1JetParton)==4 || abs(J2JetParton)==4)'
  
  Wl = '((!'+twoBs+'&&!'+oneC+'))'
  Wc = '((!'+twoBs+'&&'+oneC+'&&!'+twoCs+'))'
  Wcc = '((!'+twoBs+'&&'+oneC+'&&'+twoCs+'))'
  Wbb = '('+twoBs+')'
 
 cutDataNonIso   = '('+NonIso+'&&'+theCut+')' #Data Non Iso
 cutDataIso      = '('+Iso+'&&'+theCut+')'    #Data Iso
 cutMcNonIso     = '('+weight+ '*('+NonIso+'&&'+theCut+'))' #MC Non Iso
 cutMcNonIsoW    = '('+weightW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso        = '('+weight+ '*('+Iso+   '&&'+theCut+'))' #MC Iso
 cutMcWlNonIso   = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wl+'))'
 cutMcWlIso      = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wl+'))'
 cutMcWcNonIso   = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wc+'))'
 cutMcWcIso      = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wc+'))'
 cutMcWccNonIso  = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wcc+'))'
 cutMcWccIso     = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wcc+'))'
 cutMcWbbNonIso  = '('+weightW+'*('+NonIso+'&&'+theCut+'&&'+Wbb+'))'
 cutMcWbbIso     = '('+weightW+'*('+Iso+   '&&'+theCut+'&&'+Wbb+'))'
 return cutMcNonIso, cutMcNonIsoW, cutMcIso, cutDataNonIso, cutDataIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso

