#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(leaf='J1_pt',isolationValue=0.12,antiIsoValue=0.2,lumi=19759.,bnr=0,btype='t',jnr=2,njetPt='20',jetPt='20',jetVeto=False,Control=True,Z_Region=False,Legacy=False,noMT=False,TT_m=False,TT_me=False,ST=False,Signal=False,Tomislav=False,extraCut='(2>1)',Ctl_Andrea=False):

 goodMu = '(abs(muon_eta)<2.1 && muon_pt>30 && HLT_IsoMu24_eta2p1_v_fired)'
 oneMu_noEle = '(nrMu==1 && nrEle==0)'
 oneMu_oneEle = '(nrMu==1 && nrEle==1 && ptEle>30)'
 twoMu_noEle = '(nrMu==2 && nrEle==0)'

 j1Cent = '(J1_pt>%s && abs(J1_eta)<2.4 && J1_idLooseJet)'%(jetPt)
 j2Cent = '(J2_pt>%s && abs(J2_eta)<2.4 && J2_idLooseJet)'%(jetPt)
 j3Cent = '(J3_pt>%s && abs(J3_eta)<2.4 && J3_idLooseJet)'%(jetPt)
 j4Cent = '(J4_pt>%s && abs(J4_eta)<2.4 && J4_idLooseJet)'%(jetPt)
 noFJ = '(nJets24Pt25==0)'
 j1Fwd = '(J1_pt>%s && abs(J1_eta)>=2.4 && abs(J1_eta)<5.0 && J1_idLooseJet)'%(jetPt)
 j2Fwd = '(J2_pt>%s && abs(J2_eta)>=2.4 && abs(J2_eta)<5.0 && J2_idLooseJet)'%(jetPt)
 j3Veto = '(J3_pt<%s)'%(njetPt)

 if leaf=="mt": mt='(2>1)'
 else: mt = '(mt>45)'

 if btype == 't': bcut = '0.898'
 if btype == 'm': bcut = '0.679'
 if btype == 'l': bcut = '0.244'
 if btype =='m' or btype=='l': print('YOUR BTAG SCALE FACTORS ARE WRONG.  DEAL WITH IT')
  
 realb_j1 = "(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4)"
 realb_j2 = "(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4)"

 #SFBJ1 = '((0.927563+(1.55479e-05*J1_pt))+(-1.90666e-07*(J1_pt*J1_pt)))'
 #SFBJ2 = '((0.927563+(1.55479e-05*J2_pt))+(-1.90666e-07*(J2_pt*J2_pt)))'
 #SFLJ1="(((1.00462+(0.00325971*J1_pt))+(-7.79184e-06*(J1_pt*J1_pt)))+(5.22506e-09*(J1_pt*(J1_pt*J1_pt))))"
 #SFLJ2="(((1.00462+(0.00325971*J2_pt))+(-7.79184e-06*(J2_pt*J2_pt)))+(5.22506e-09*(J2_pt*(J2_pt*J2_pt))))"
 #mc_j1btag  = '(J1_CSVbtag>%s && ((%s * %s)+(!%s * %s)))'%(bcut,realb_j1,realb_j1,SFBJ1,SFLJ1) 
 #mc_j2btag  = '(J2_CSVbtag>%s && ((%s * %s)+(!%s * %s)))'%(bcut,realb_j2,realb_j2,SFBJ2,SFLJ2) 

 j1btag = '(J1_CSVbtag>%s)'%(bcut)
 j2btag = '(J2_CSVbtag>%s)'%(bcut)
 j1btagSF  = '((%s * J1_CSVT_SFb)+(!%s * J1_CSVT_SFl))'%(realb_j1,realb_j1) 
 j2btagSF  = '((%s * J2_CSVT_SFb)+(!%s * J2_CSVT_SFl))'%(realb_j2,realb_j2) 
 weight_2b = '('+j1btagSF+' * '+j2btagSF+')'

 weightEff = 'weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig'
 weight = '(weightFactor * %s * %s)'%(lumi,weightEff)
 weightT = '(weightFactor * %s * %s * weightTop)'%(lumi,weightEff)
 weightTup = '(weightFactor * %s * %s * weightTop * weightTop)'%(lumi,weightEff)

 if Signal:
  skim='('+goodMu+' && '+oneMu_noEle+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if TT_m:
  skim='('+goodMu+' && '+oneMu_noEle+' && '+j1Cent+' && '+j2Cent+' && '+j3Cent+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if Z_Region:
  skim='('+goodMu+' && '+twoMu_noEle+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if TT_me:
  skim='('+goodMu+' && '+oneMu_oneEle+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if ST:
  skim='('+goodMu+' && '+oneMu_noEle+' && '+j1Cent+' && '+j2Fwd+' && '+j3Veto+' && '+j1btag+' && '+mt+')'
  weight    = '('+weight+' * %s)'%(j1btagSF)
  weightT   = '('+weightT+' * %s)'%(j1btagSF)
  weightTup = '('+weightTup+' * %s)'%(j1btagSF)

 # for splitting up the W samples, we should probably match to jets
 genB = '(nbHadrons>0)' 
 genC = '((nrC+nrCbar)>0)'
 evenC = '(((nrC+nrCbar)%2)==0)'
 
 Wl = '((!'+genB+'&&!'+genC+'))'
 Wc = '((!'+genB+'&&'+genC+'&&!'+evenC+'))'
 Wcc = '((!'+genB+'&&'+genC+'&&'+evenC+'))'
 Wbb = '('+genB+')'

 iso='(muNuRelPFIsoDB_A<'+str(isolationValue)+')'
 nonIso ='(muNuRelPFIsoDB_A>='+str(antiIsoValue)+')'

 cutDataNonIso   = '('+nonIso+'&&'+skim+')' #Data Non Iso
 cutDataIso      = '('+iso+'&&'+skim+')'    #Data Iso

# cutMcNonIso     = cutDataNonIso 
# cutMcNonIsoW    = cutDataNonIso  
# cutMcIso        = cutDataIso 
# cutMcNonIsoTup  = cutDataNonIso 
# cutMcIsoTup     = cutDataIso 
# cutMcNonIsoTdn  = cutDataNonIso 
# cutMcIsoTdn     = cutDataIso 
# cutMcNonIsoT    = cutDataNonIso 
# cutMcIsoT       = cutDataIso 
# cutMcWlNonIso   = cutDataNonIso 
# cutMcWlIso      = cutDataIso 
# cutMcWcNonIso   = cutDataNonIso 
# cutMcWcIso      = cutDataIso 
# cutMcWccNonIso  = cutDataNonIso 
# cutMcWccIso     = cutDataIso 
# cutMcWbbNonIso  = cutDataNonIso 
# cutMcWbbIso     = cutDataIso 

 cutMcNonIso     = '('+weight+' * ('+nonIso+' && '+skim+'))' #MC Non Iso
 cutMcNonIsoW    = cutMcNonIso #'('+weightW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso        = '('+weight+' * ('+iso+' && '+skim+'))' #MC Iso
 cutMcNonIsoTup  = '('+weightTup+' * ('+nonIso+' && '+skim+'))' #MC Non Iso
 cutMcIsoTup     = '('+weightTup+' * ('+iso+' && '+skim+'))' #MC Iso
 cutMcNonIsoTdn  = cutMcNonIso
 cutMcIsoTdn     = cutMcIso
 cutMcNonIsoT    = '('+weightT+' * ('+nonIso+' && '+skim+'))' #MC Non Iso
 cutMcIsoT       = '('+weightT+' * ('+iso+   ' && '+skim+'))' #MC Iso
 cutMcWlNonIso   = '('+weight+' * ('+nonIso+' && '+skim+' && '+Wl+'))'
 cutMcWlIso      = '('+weight+' * ('+iso+   ' && '+skim+' && '+Wl+'))'
 cutMcWcNonIso   = '('+weight+' * ('+nonIso+' && '+skim+' && '+Wc+'))'
 cutMcWcIso      = '('+weight+' * ('+iso+   ' && '+skim+' && '+Wc+'))'
 cutMcWccNonIso  = '('+weight+' * ('+nonIso+' && '+skim+' && '+Wcc+'))'
 cutMcWccIso     = '('+weight+' * ('+iso+   ' && '+skim+' && '+Wcc+'))'
 cutMcWbbNonIso  = '('+weight+' * ('+nonIso+' && '+skim+' && '+Wbb+'))'
 cutMcWbbIso     = '('+weight+' * ('+iso+   ' && '+skim+' && '+Wbb+'))'

 return cutMcNonIso, cutMcNonIsoW, cutMcIso, cutDataNonIso, cutDataIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso, cutMcNonIsoT, cutMcIsoT, cutMcNonIsoTup, cutMcIsoTup, cutMcNonIsoTdn, cutMcIsoTdn

