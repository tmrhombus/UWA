#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(leaf='J1_pt',isolationValue=0.12,antiIsoValue=0.2,lumi=19759.,bnr=0,btype='t',jnr=2,njetPt='20',jetPt='20',jetVeto=False,Control=True,Z_Region=False,Legacy=False,noMT=False,TT_m=False,TT_me=False,ST=False,Signal=False,Tomislav=False,extraCut='(2>1)',Ctl_Andrea=False):

 goodMu = '(abs(muon_eta)<2.1 && muon_pt>30 && HLT_IsoMu24_eta2p1_v_fired)'
 oneMu_noEle = '(nrMu==1 && nrEle==0)'
 oneMu_oneEle = '(nrMu==1 && nrEle==1)'
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
 else: mt = '(2>1)'
 #else: mt = '(mt>45)'

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

 mc_j1btag  = '(J1_CSVbtag>%s && ((%s * J1_CSVT_SFb)+(!%s * J1_CSVT_SFl)))'%(bcut,realb_j1,realb_j1) 
 mc_j2btag  = '(J2_CSVbtag>%s && ((%s * J2_CSVT_SFb)+(!%s * J2_CSVT_SFl)))'%(bcut,realb_j2,realb_j2) 
 data_j1btag = '(J1_CSVbtag>%s)'%(bcut)
 data_j2btag = '(J2_CSVbtag>%s)'%(bcut)

 weightEff = 'weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig'
 weight = '(weightFactor * %s * %s)'%(lumi,weightEff)
 weightT = '(weightFactor * %s * %s * weightTop)'%(lumi,weightEff)
 weightTup = '(weightFactor * %s * %s * weightTop * weightTop)'%(lumi,weightEff)

 if Signal:
  skim='('+goodMu+' && '+oneMu_noEle+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+mt+')'
  mc_skim = '('+skim+' && '+mc_j1btag+' && '+mc_j2btag+')'
  data_skim = '('+skim+' && '+data_j1btag+' && '+data_j2btag+')'
 if ST:
  skim='('+goodMu+' && '+oneMu_noEle+' && '+mt+')'
  mc_skim = '('+skim+' && (('+j1Cent+' && '+mc_j1btag+' && '+j2Fwd+') || ('+j2Cent+' && '+mc_j2btag+' && '+j1Fwd+')))'
  data_skim = '('+skim+' && (('+j1Cent+' && '+data_j1btag+' && '+j2Fwd+') || ('+j2Cent+' && '+data_j2btag+' && '+j1Fwd+')))'

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

 cutDataNonIso   = '('+nonIso+'&&'+data_skim+')' #Data Non Iso
 cutDataIso      = '('+iso+'&&'+data_skim+')'    #Data Iso

 cutMcNonIso     = '('+weight+' * ('+nonIso+' && '+mc_skim+'))' #MC Non Iso
 cutMcNonIsoW    = cutMcNonIso #'('+weightW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso        = '('+weight+' * ('+iso+' && '+mc_skim+'))' #MC Iso
 cutMcNonIsoTup  = '('+weightTup+' * ('+nonIso+' && '+mc_skim+'))' #MC Non Iso
 cutMcIsoTup     = '('+weightTup+' * ('+iso+' && '+mc_skim+'))' #MC Iso
 cutMcNonIsoTdn  = cutMcNonIso
 cutMcIsoTdn     = cutMcIso
 cutMcNonIsoT    = '('+weightT+' * ('+nonIso+' && '+mc_skim+'))' #MC Non Iso
 cutMcIsoT       = '('+weightT+' * ('+iso+   ' && '+mc_skim+'))' #MC Iso
 cutMcWlNonIso   = '('+weight+' * ('+nonIso+' && '+mc_skim+' && '+Wl+'))'
 cutMcWlIso      = '('+weight+' * ('+iso+   ' && '+mc_skim+' && '+Wl+'))'
 cutMcWcNonIso   = '('+weight+' * ('+nonIso+' && '+mc_skim+' && '+Wc+'))'
 cutMcWcIso      = '('+weight+' * ('+iso+   ' && '+mc_skim+' && '+Wc+'))'
 cutMcWccNonIso  = '('+weight+' * ('+nonIso+' && '+mc_skim+' && '+Wcc+'))'
 cutMcWccIso     = '('+weight+' * ('+iso+   ' && '+mc_skim+' && '+Wcc+'))'
 cutMcWbbNonIso  = '('+weight+' * ('+nonIso+' && '+mc_skim+' && '+Wbb+'))'
 cutMcWbbIso     = '('+weight+' * ('+iso+   ' && '+mc_skim+' && '+Wbb+'))'

 return cutMcNonIso, cutMcNonIsoW, cutMcIso, cutDataNonIso, cutDataIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso, cutMcNonIsoT, cutMcIsoT, cutMcNonIsoTup, cutMcIsoTup, cutMcNonIsoTdn, cutMcIsoTdn

