#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(isolationValue=0.12,antiIsoValue=0.2,lumi=19759.,bnr=0,btype='t',jnr=2,njetPt='20',jetPt='20',jetVeto=False,Control=True,Z_Region=False,Legacy=False,noMT=False,TT_m=False,TT_me=False,ST=False,Signal=False,Tomislav=False,extraCut='(2>1)'):

 trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
 muon_selection = '(DiMuonMass<=60 && nrEle==0 && nrMu==1 && abs(muon_eta)<2.1 && muon_pt>25)'
 muon_selection30 = '(nrEle==0 && nrMu==1 && abs(muon_eta)<2.1 && muon_pt>30)'
 oneMUoneELE = '(DiMuonMass<=60 && nrEle==1 && nrMu==1 && abs(muon_eta)<2.1 && muon_pt>25)'
 dimuon_selection = '(nrMu==2&&abs(muon_eta)<2.1&&muon_pt>25)'
 z_selection = '(DiMuonMass>70&&DiMuonMass<110)'
 vertex = '(abs(dz)<0.5&&abs(ipDXY)<0.02)'
 vertexNoDZ = '(abs(ipDXY)<0.02)'
 mt = '(mt>45)'
 mt50 = '(mt>50)'
 met = '(MET>30)'
 noFJ = '(nJets24Pt25==0)'
 #oneFJ = '(nJets24Pt25==1)'
 oneFJ = '( abs(J1_eta)<2.4 && abs(J2_eta)>2.4 )'
 #oneFJ = '((abs(J1_eta)>2.4 && abs(J2_eta)<2.4)||(abs(J1_eta)<2.4 && abs(J2_eta)>2.4))'
 muPlus = '(muonCharge > 0)'
 muMinus = '(muonCharge < 0)'
 jetCap = '(J1_pt < 30 && J2_pt < 30)'

 twJ = '(J1_pt >'+jetPt+' && J2_pt>'+jetPt+' && abs(J1_eta)<2.4 && abs(J2_eta)<2.4)'
 if ST: twJ = '(J1_pt >'+jetPt+' && J2_pt>'+jetPt+')'
 thJ = '('+twJ+'&& J3_pt  > '+jetPt+' && abs(J3_eta) <  2.4)'
 frJ = '('+thJ+'&& J4_pt > '+jetPt+' && abs(J4_eta) < 2.4)'

 if not jetVeto:
  twoJets   = '('+twJ+')'
  threeJets = '('+thJ+')'
  fourJets  = '('+frJ+')'
  #twoJets   = '('+twJ+' && nJetsPt'+njetPt+'>=2)'
  #threeJets = '('+thJ+' && nJetsPt'+njetPt+'>=3)'
  #fourJets  = '('+frJ+' && nJetsPt'+njetPt+'>=4)'
 if jetVeto:
  twoJets   = '('+twJ+'&& J3_pt<' +njetPt+')'
  threeJets = '('+thJ+'&& J4_pt<'+njetPt+')'
  fourJets  = '('+frJ+')'
  #twoJets   = '('+twJ+' && nJetsPt'+njetPt+'==2)'
  #threeJets = '('+thJ+' && nJetsPt'+njetPt+'==3)'
  #fourJets  = '('+frJ+' && nJetsPt'+njetPt+'==4)'

 if Control or Legacy or Signal:
  #Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+'&&'+jetCap+')'
  Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+')'
 elif noMT:
  Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+noFJ+')' #for QCD
 elif TT_me:
  Skim='('+trigger+'&&'+oneMUoneELE+'&&'+vertex+'&&'+mt+')' #for TTbar
 elif TT_m:
  Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+')' #for TTbar
 elif Z_Region:
  Skim='('+trigger+'&&'+dimuon_selection+'&&'+vertex+'&&'+z_selection+')'
 elif ST:
  Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+oneFJ+')'
 elif Tomislav:
  #Skim='('+trigger+'&&'+muon_selection30+'&&'+vertex+'&&'+met+')'#for Tomislav qcd
  Skim='('+trigger+'&&'+muon_selection30+'&&'+vertex+'&&'+mt50+'&&'+met+')'#for Tomislav
  #Skim='('+trigger+'&&'+dimuon_selection+'&&'+vertex+'&&'+z_selection+')' # Z
  
 theCut = '('+Skim+'&&'+extraCut+')'

 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertexNoDZ+'&&'+noFJ+')'
 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+'&&'+muPlus+')'
 #Skim='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+mt+'&&'+noFJ+'&&'+muMinus+')'

 Iso='(muNuRelPFIsoDB<'+str(isolationValue)+')'
 NonIso ='(muNuRelPFIsoDB>='+str(antiIsoValue)+')'

 weightEff = '(weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig)'
 weight = '('+' weightFactor*' +str(lumi)+'*'+str(weightEff)+')'

 if Legacy:
  Iso='(muNuRelPFIsoDB<0.12)'
  NonIso ='(muNuRelPFIsoDB>=0.2)'
  theCut = '(nrMu==1 && abs(muon_eta)<2.1 && muon_pt>25 && J1_pt > 25 && J2_pt > 25 && abs(J1_eta)<2.4 && abs(J2_eta)<2.4 && nJetsPt25==2 && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && J1_mass_SSV>0 && J2_mass_SSV>0 && DiMuonMass<=60 && nrEle==0 && nJets24Pt25==0 && mt > 45 && (abs(dz)<0.5&&abs(ipDXY)<0.02) )'
  weight = '(weightFactor*'+str(lumi)+'*'+str(weightEff)+'*EffWEIGHTCSVT)'
  weightW = '(weightFactor*'+str(lumi)+'*'+str(weightEff)+'*EffWEIGHTCSVT)'

 if btype == 'tight' or btype == 't':
  bcut = 0.898
 if btype == 'medium' or btype == 'med' or btype == 'm':
  bcut = 0.679
 if btype == 'loose' or btype == 'l':
  bcut = 0.244
  
 FirstBtag='(J1_CSVbtag>'+str(bcut)+'&&J1_mass_SSV>0)'
 SecondBtag='(J2_CSVbtag>'+str(bcut)+'&&J2_mass_SSV>0)'
 OneBtag='('+FirstBtag+'||'+SecondBtag+')'
 TwoBtag='('+FirstBtag+'&&'+SecondBtag+')'

 newCSVT1first = '((0.927563+(1.55479e-05*J1_pt))+(-1.90666e-07*(J1_pt*J1_pt)))'
 newCSVT1second = '((0.927563+(1.55479e-05*J2_pt))+(-1.90666e-07*(J2_pt*J2_pt)))'
 #newCSVT1first =  '1.'
 #newCSVT1second = '1.'
 newCSVT2 = '('+newCSVT1first+'*'+newCSVT1second+')'

 if bnr == 1:
  if btype == 'tight' or btype == 't':
   beffWeight = '1.'
   #beffWeight = 'EffWEIGHTCSVT'
  if btype == 'medium' or btype == 'med' or btype == 'm':
   beffWeight = 'EffWEIGHTCSVM'
  if btype == 'loose' or btype == 'l':
   beffWeight = 'EffWEIGHTCSVL'
  theCut = '('+theCut+'&&(('+FirstBtag+'*'+newCSVT1first+')))'
  #theCut = '('+theCut+'&&(('+FirstBtag+'*'+newCSVT1first+')||('+SecondBtag+'*'+newCSVT1second+')))'
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

 jidType = 'idLoose'
 #jidType = 'idTight'
 #puidType = 'fullIdTight'
 #puidType = 'fullIdLoose'
 #J1_PUID = '(J1_PUID_'+jidType+'&& J1_PUID_'+puidType+')' 
 #J2_PUID = '(J2_PUID_'+jidType+'&& J2_PUID_'+puidType+')' 
 #J3_PUID = '(J3_PUID_'+jidType+'&& J3_PUID_'+puidType+')' 
 #J4_PUID = '(J4_PUID_'+jidType+'&& J4_PUID_'+puidType+')' 
 J1_PUID = '(J1_'+jidType+'Jet)' 
 J2_PUID = '(J2_'+jidType+'Jet)' 
 J3_PUID = '(J3_'+jidType+'Jet)' 
 J4_PUID = '(J4_'+jidType+'Jet)' 

 PUID2 = '('+J1_PUID+'&&'+J2_PUID+')'
 PUID3 = '('+PUID2+'&&'+J3_PUID+')'
 PUID4 = '('+PUID3+'&&'+J4_PUID+')'

 if jnr == 2:
  theCut = '('+theCut+'&&'+twoJets+')'
  PUID = PUID2
 if jnr == 3:
  theCut = '('+theCut+'&&'+threeJets+')'
  PUID = PUID3
 if jnr == 4:
  theCut = '('+theCut+'&&'+fourJets+')'
  PUID = PUID4

 # for splitting up the W sample 
 genB = '(nbHadrons>0)' #to do this correctly, must match to jets
 genC = '((nrC+nrCbar)>0)'
 evenC = '(((nrC+nrCbar)%2)==0)'
 
 Wl = '((!'+genB+'&&!'+genC+'))'
 Wc = '((!'+genB+'&&'+genC+'&&!'+evenC+'))'
 Wcc = '((!'+genB+'&&'+genC+'&&'+evenC+'))'
 Wbb = '('+genB+')'

 cutDataNonIso   = '('+PUID+'&&'+NonIso+'&&'+theCut+')' #Data Non Iso
 cutDataIso      = '('+PUID+'&&'+Iso+'&&'+theCut+')'    #Data Iso
 cutMcNonIso     = '('+weight+'*('+PUID+'&&'+NonIso+'&&'+theCut+'))' #MC Non Iso
 cutMcNonIsoW    = cutMcNonIso #'('+weightW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso        = '('+weight+'*('+PUID+'&&'+Iso+   '&&'+theCut+'))' #MC Iso
 cutMcNonIsoTup  = '('+weight+'*weightTop*weightTop*('+PUID+'&&'+NonIso+'&&'+theCut+'))' #MC Non Iso
 cutMcIsoTup     = '('+weight+'*weightTop*weightTop*('+PUID+'&&'+Iso+'&&'+theCut+'))' #MC Iso
 cutMcNonIsoTdn  = cutMcNonIso
 cutMcIsoTdn     = cutMcIso
 cutMcNonIsoT    = '('+weight+'*weightTop*('+PUID+'&&'+NonIso+'&&'+theCut+'))' #MC Non Iso
 cutMcIsoT       = '('+weight+'*weightTop*('+PUID+'&&'+Iso+   '&&'+theCut+'))' #MC Iso
 cutMcWlNonIso   = '('+weight+'*('+PUID+'&&'+NonIso+'&&'+theCut+'&&'+Wl+'))'
 cutMcWlIso      = '('+weight+'*('+PUID+'&&'+Iso+   '&&'+theCut+'&&'+Wl+'))'
 cutMcWcNonIso   = '('+weight+'*('+PUID+'&&'+NonIso+'&&'+theCut+'&&'+Wc+'))'
 cutMcWcIso      = '('+weight+'*('+PUID+'&&'+Iso+   '&&'+theCut+'&&'+Wc+'))'
 cutMcWccNonIso  = '('+weight+'*('+PUID+'&&'+NonIso+'&&'+theCut+'&&'+Wcc+'))'
 cutMcWccIso     = '('+weight+'*('+PUID+'&&'+Iso+   '&&'+theCut+'&&'+Wcc+'))'
 cutMcWbbNonIso  = '('+weight+'*('+PUID+'&&'+NonIso+'&&'+theCut+'&&'+Wbb+'))'
 cutMcWbbIso     = '('+weight+'*('+PUID+'&&'+Iso+   '&&'+theCut+'&&'+Wbb+'))'
 return cutMcNonIso, cutMcNonIsoW, cutMcIso, cutDataNonIso, cutDataIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso, cutMcNonIsoT, cutMcIsoT, cutMcNonIsoTup, cutMcIsoTup, cutMcNonIsoTdn, cutMcIsoTdn

