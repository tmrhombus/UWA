#!/usr/bin/env python
'''
for Wbb analysis, input a few values and function outputs cut strings
Author: T.M.Perry UW-Madison
'''

def cutmaker(leaf='J1_pt',isolationValue=0.12,antiIsoValue=0.2,lumi=19759.,bnr=0,btype='t',jnr=2,njetPt='20',jetPt='20',jetVeto=False,Control=True,Z_Region=False,Legacy=False,noMT=False,TT_m=False,TT_me=False,ST=False,Signal=False,Tomislav=False,extraCut='(2>1)',Ctl_Andrea=False):

 goodMu = '(abs(muon_eta)<2.1 && muon_pt>30)'
 oneMu_noEle = '(nrMuLoose==1 && nrEle==0)'
 oneMu_oneEle = '(nrMuLoose==1 && nrEle==1 && ele_pt>30)'
 twoMu_noEle = '(nrMuLoose==2 && nrEle==0)'
 #twoMu_noEle = '(nrMu==2 && nrEle==0)'
 noEleQCD = '(nrEle==0)'
 oneMu_noEleQCD = '(nrMuLoose==0 && nrEle==0)'
 oneMu_oneEleQCD = '(nrMuLoose==1 && nrEle==1 && ele_pt>30)'
 twoMu_noEleQCD = '(nrMuLoose==2 && nrEle==0)'

 j1Cent = '(J1_pt>%s && abs(J1_eta)<2.4 && J1_idLooseJet)'%(jetPt)
 j2Cent = '(J2_pt>%s && abs(J2_eta)<2.4 && J2_idLooseJet)'%(jetPt)
 j3Cent = '(J3_pt>%s && abs(J3_eta)<2.4 && J3_idLooseJet)'%(jetPt)
 j4Cent = '(J4_pt>%s && abs(J4_eta)<2.4 && J4_idLooseJet)'%(jetPt)
 #noFJ = '(2>1)'
 noFJ = '(nJets24Pt25==0)'
 j1Fwd = '(J1_pt>%s && abs(J1_eta)>=2.4 && abs(J1_eta)<5.0 && J1_idLooseJet)'%(jetPt)
 j2Fwd = '(J2_pt>%s && abs(J2_eta)>=2.4 && abs(J2_eta)<5.0 && J2_idLooseJet)'%(jetPt)
 j3Veto = '(J3_pt<%s)'%(njetPt)

 #if leaf=="mt_new": mt='(mt_new>45)'
 if leaf=="mt_new": mt='(2>1)'
 else: mt = '(mt_new>45)'

 realh_j1 = "(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4)"
 realh_j2 = "(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4)"
 realb_j1 = "(abs(J1_partonFlavour)==5)"
 realb_j2 = "(abs(J2_partonFlavour)==5)"
 realc_j1 = "(abs(J1_partonFlavour)==4)"
 realc_j2 = "(abs(J2_partonFlavour)==4)"

 if btype == 't':
  bcut = '0.898'
  j1btagSF = '((%s * J1_CSVT_SFb)+(!%s * J1_CSVT_SFl))'%(realh_j1,realh_j1) 
  j1btagSF_up  = '((%s * (J1_CSVT_SFb+J1_CSVT_errorb) ) + (%s * (J1_CSVT_SFb+2*J1_CSVT_errorb) ) + (!%s * J1_CSVT_SFl_up))'%(realb_j1,realc_j1,realb_j1) 
  j1btagSF_dn  = '((%s * (J1_CSVT_SFb-J1_CSVT_errorb) ) + (%s * (J1_CSVT_SFb-2*J1_CSVT_errorb) ) + (!%s * J1_CSVT_SFl_down))'%(realb_j1,realc_j1,realb_j1) 
  j2btagSF  = '((%s * J2_CSVT_SFb)+(!%s * J2_CSVT_SFl))'%(realh_j2,realh_j2) 
  j2btagSF_up  = '((%s * (J2_CSVT_SFb+J2_CSVT_errorb) ) + (%s * (J2_CSVT_SFb+2*J2_CSVT_errorb) ) + (!%s * J2_CSVT_SFl_up))'%(realb_j2,realc_j2,realb_j2) 
  j2btagSF_dn  = '((%s * (J2_CSVT_SFb-J2_CSVT_errorb) ) + (%s * (J2_CSVT_SFb-2*J2_CSVT_errorb) ) + (!%s * J2_CSVT_SFl_down))'%(realb_j2,realc_j2,realb_j2) 
 if btype == 'm':
  bcut = '0.679'
  j1btagSF  = '((%s * J1_CSVM_SFb)+(!%s * J1_CSVM_SFl))'%(realh_j1,realh_j1) 
  j2btagSF  = '((%s * J2_CSVM_SFb)+(!%s * J2_CSVM_SFl))'%(realh_j2,realh_j2) 
 if btype == 'l':
  bcut = '0.244'
  j1btagSF  = '((%s * J1_CSVL_SFb)+(!%s * J1_CSVL_SFl))'%(realh_j1,realh_j1) 
  j2btagSF  = '((%s * J2_CSVL_SFb)+(!%s * J2_CSVL_SFl))'%(realh_j2,realh_j2) 
  
 j1btag = '(J1_CSVbtag>%s)'%(bcut)
 j2btag = '(J2_CSVbtag>%s)'%(bcut)
 weight_2b = '('+j1btagSF+' * '+j2btagSF+')'
 weight_1b = j1btagSF
 weight_2bup = '('+j1btagSF_up+' * '+j2btagSF_up+')'
 weight_2bdn = '('+j1btagSF_dn+' * '+j2btagSF_dn+')'
 weight_1bup = j1btagSF_up
 weight_1bdn = j1btagSF_dn

 weightEff = 'weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig'
 weight = '(QweightFactor * %s * %s)'%(lumi,weightEff)
 weightT = '(QweightFactor * %s * %s * weightTop)'%(lumi,weightEff)
 weightTup = '(QweightFactor * %s * %s * weightTop * weightTop)'%(lumi,weightEff)

 if Control:
  skim= '('+goodMu+' && '+oneMu_noEle+   ' && '+j1Cent+' && '+j2Cent+' && '+mt+')'
  skimq='('+goodMu+' && '+oneMu_noEleQCD+' && '+j1Cent+' && '+j2Cent+' && '+mt+')'
 if Signal:
  skim= '('+goodMu+' && '+oneMu_noEle+   ' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  skimq='('+goodMu+' && '+oneMu_noEleQCD+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightBup = '('+weight+' * '+weight_2bup+')'
  weightBdn = '('+weight+' * '+weight_2bdn+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if TT_m:
  skim= '('+goodMu+' && '+oneMu_noEle+   ' && '+j1Cent+' && '+j2Cent+' && '+j3Cent+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  skimq='('+goodMu+' && '+oneMu_noEleQCD+' && '+j1Cent+' && '+j2Cent+' && '+j3Cent+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightBup = '('+weight+' * '+weight_2bup+')'
  weightBdn = '('+weight+' * '+weight_2bdn+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if Z_Region:
  skim= '('+goodMu+' && '+twoMu_noEle+   ' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+')'
  skimq='('+goodMu+' && '+twoMu_noEleQCD+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightBup = '('+weight+' * '+weight_2bup+')'
  weightBdn = '('+weight+' * '+weight_2bdn+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if TT_me:
  skim= '('+goodMu+' && '+oneMu_oneEle+   ' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  skimq='('+goodMu+' && '+oneMu_oneEleQCD+' && '+j1Cent+' && '+j2Cent+' && '+j3Veto+' && '+noFJ+' && '+j1btag+' && '+j2btag+' && '+mt+')'
  weight    = '('+weight+' * '+weight_2b+')'
  weightBup = '('+weight+' * '+weight_2bup+')'
  weightBdn = '('+weight+' * '+weight_2bdn+')'
  weightT   = '('+weightT+' * '+weight_2b+')'
  weightTup = '('+weightTup+' * '+weight_2b+')'
 if ST:
  skim= '('+goodMu+' && '+oneMu_noEle+   ' && '+j1Cent+' && '+j2Fwd+' && '+j3Veto+' && '+j1btag+' && '+mt+')'
  skimq='('+goodMu+' && '+oneMu_noEleQCD+' && '+j1Cent+' && '+j2Fwd+' && '+j3Veto+' && '+j1btag+' && '+mt+')'
  weight    = '('+weight+' * %s)'%(j1btagSF)
  weightBup = '('+weight+' * '+weight_1bup+')'
  weightBdn = '('+weight+' * '+weight_1bdn+')'
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

 iso='(muNuRelPFIsoDB_A<'+str(isolationValue)+' && HLT_IsoMu24_eta2p1_v_fired)'
 nonIso ='(muNuRelPFIsoDB_A>='+str(antiIsoValue)+')'

 cutDataNonIso   = '('+nonIso+'&&'+skimq+')' #Data Non Iso
 cutDataIso      = '('+iso+'&&'+skim+')'    #Data Iso

 cutMcNonIso     = '('+weight+' * ('+nonIso+' && '+skimq+'))' #MC Non Iso
 cutMcNonIsoW    = cutMcNonIso #'('+weightW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso        = '('+weight+' * ('+iso+' && '+skim+'))' #MC Iso
 cutMcNonIsoTup  = '('+weightTup+' * ('+nonIso+' && '+skimq+'))' #MC Non Iso
 cutMcIsoTup     = '('+weightTup+' * ('+iso+' && '+skim+'))' #MC Iso
 cutMcNonIsoTdn  = cutMcNonIso
 cutMcIsoTdn     = cutMcIso
 cutMcNonIsoT    = '('+weightT+' * ('+nonIso+' && '+skimq+'))' #MC Non Iso
 cutMcIsoT       = '('+weightT+' * ('+iso+   ' && '+skim +'))' #MC Iso
 cutMcWlNonIso   = '('+weight+' * ('+nonIso+' && '+skimq+' && '+Wl+'))'
 cutMcWlIso      = '('+weight+' * ('+iso+   ' && '+skim+ ' && '+Wl+'))'
 cutMcWcNonIso   = '('+weight+' * ('+nonIso+' && '+skimq+' && '+Wc+'))'
 cutMcWcIso      = '('+weight+' * ('+iso+   ' && '+skim+ ' && '+Wc+'))'
 cutMcWccNonIso  = '('+weight+' * ('+nonIso+' && '+skimq+' && '+Wcc+'))'
 cutMcWccIso     = '('+weight+' * ('+iso+   ' && '+skim+ ' && '+Wcc+'))'
 cutMcWbbNonIso  = '('+weight+' * ('+nonIso+' && '+skimq+' && '+Wbb+'))'
 cutMcWbbIso     = '('+weight+' * ('+iso+   ' && '+skim+ ' && '+Wbb+'))'

 # B sf up
 cutMcNonIso_Bup     = '('+weightBup+' * ('+nonIso+' && '+skimq+'))' #MC Non Iso
 cutMcNonIsoW_Bup    = cutMcNonIso #'('+weightBupW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso_Bup        = '('+weightBup+' * ('+iso+' && '+skim+'))' #MC Iso
 cutMcWlNonIso_Bup   = '('+weightBup+' * ('+nonIso+' && '+skimq+' && '+Wl+'))'
 cutMcWlIso_Bup      = '('+weightBup+' * ('+iso+   ' && '+skim+ ' && '+Wl+'))'
 cutMcWcNonIso_Bup   = '('+weightBup+' * ('+nonIso+' && '+skimq+' && '+Wc+'))'
 cutMcWcIso_Bup      = '('+weightBup+' * ('+iso+   ' && '+skim+ ' && '+Wc+'))'
 cutMcWccNonIso_Bup  = '('+weightBup+' * ('+nonIso+' && '+skimq+' && '+Wcc+'))'
 cutMcWccIso_Bup     = '('+weightBup+' * ('+iso+   ' && '+skim+ ' && '+Wcc+'))'
 cutMcWbbNonIso_Bup  = '('+weightBup+' * ('+nonIso+' && '+skimq+' && '+Wbb+'))'
 cutMcWbbIso_Bup     = '('+weightBup+' * ('+iso+   ' && '+skim+ ' && '+Wbb+'))'

 # B sf dn
 cutMcNonIso_Bdn     = '('+weightBdn+' * ('+nonIso+' && '+skimq+'))' #MC Non Iso
 cutMcNonIsoW_Bdn    = cutMcNonIso #'('+weightBdnW+'*('+NonIso+'&&'+theCut+'))' #MC Non IsoW
 cutMcIso_Bdn        = '('+weightBdn+' * ('+iso+' && '+skim+'))' #MC Iso
 cutMcWlNonIso_Bdn   = '('+weightBdn+' * ('+nonIso+' && '+skimq+' && '+Wl+'))'
 cutMcWlIso_Bdn      = '('+weightBdn+' * ('+iso+   ' && '+skim+ ' && '+Wl+'))'
 cutMcWcNonIso_Bdn   = '('+weightBdn+' * ('+nonIso+' && '+skimq+' && '+Wc+'))'
 cutMcWcIso_Bdn      = '('+weightBdn+' * ('+iso+   ' && '+skim+ ' && '+Wc+'))'
 cutMcWccNonIso_Bdn  = '('+weightBdn+' * ('+nonIso+' && '+skimq+' && '+Wcc+'))'
 cutMcWccIso_Bdn     = '('+weightBdn+' * ('+iso+   ' && '+skim+ ' && '+Wcc+'))'
 cutMcWbbNonIso_Bdn  = '('+weightBdn+' * ('+nonIso+' && '+skimq+' && '+Wbb+'))'
 cutMcWbbIso_Bdn     = '('+weightBdn+' * ('+iso+   ' && '+skim+ ' && '+Wbb+'))'

 return cutMcNonIso, cutMcNonIsoW, cutMcIso, cutDataNonIso, cutDataIso, cutMcWlNonIso, cutMcWlIso, cutMcWcNonIso, cutMcWcIso, cutMcWccNonIso, cutMcWccIso, cutMcWbbNonIso, cutMcWbbIso, cutMcNonIsoT, cutMcIsoT, cutMcNonIsoTup, cutMcIsoTup, cutMcNonIsoTdn, cutMcIsoTdn, cutMcNonIso_Bup, cutMcNonIsoW_Bup, cutMcIso_Bup, cutMcWlNonIso_Bup, cutMcWlIso_Bup, cutMcWcNonIso_Bup, cutMcWcIso_Bup, cutMcWccNonIso_Bup, cutMcWccIso_Bup, cutMcWbbNonIso_Bup, cutMcWbbIso_Bup, cutMcNonIso_Bdn, cutMcNonIsoW_Bdn, cutMcIso_Bdn, cutMcWlNonIso_Bdn, cutMcWlIso_Bdn, cutMcWcNonIso_Bdn, cutMcWcIso_Bdn, cutMcWccNonIso_Bdn, cutMcWccIso_Bdn, cutMcWbbNonIso_Bdn, cutMcWbbIso_Bdn   
