import FWCore.ParameterSet.Config as cms

from UWAnalysis.Configuration.tools.analysisToolsPT import TriggerPaths
jetRanks = [0,1,2,3,4,5,6,7]
jetNames = ['J1_','J2_','J3_','J4_','J5_','J6_','J7_','J8_']

# Helper Functions for defining variables in ntuple
def makeCollSize(srcName,tagName):
  PSet = cms.PSet(
        pluginType = cms.string("CollectionSizeFiller"),
        src        = cms.InputTag(srcName),
        tag        = cms.string(tagName)
  )
  return PSet

def makeElectron(tagName,methodName,sourceElectrons='smearedGoodElectrons',lo=True):
  PSet = cms.PSet(
        pluginType  = cms.string("PATElectronFiller"),
        src         = cms.InputTag(sourceElectrons),
        tag         = cms.string(tagName),
        method      = cms.string(methodName),
        leadingOnly = cms.untracked.bool(lo)
  )
  return PSet

def makeMuon(tagName,methodName,sourceMuons='smearedGoodMuons',lo=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuonFiller"),
         src         = cms.InputTag(sourceMuons),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(lo)
   )
   return PSet

def makeMET(tagName,methodName,sourceMET='metCorrected',lo=True):
  PSet = cms.PSet(
         pluginType  = cms.string("PATMETFiller"),
         src         = cms.InputTag(sourceMET),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(lo)
  )
  return PSet

def makeJetList(strName,methodName,pf='',xn='',sourceJets='smearedGoodJets'):
   PSet_List = []
   for rank,name in zip(jetRanks,jetNames):
    nameTag = pf+name+strName+xn
    PSet_List.append(cms.PSet(
          pluginType  = cms.string("PATJetFiller"),
          src         = cms.InputTag(sourceJets),
          tag         = cms.string(nameTag),
          method      = cms.string(methodName),
          leadingOnly = cms.untracked.bool(False),
          myrank      = cms.untracked.double(rank)
    ))
   return PSet_List

def makeJet(tagName,methodName,sourceJets='smearedGoodJets',lo=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATJetFiller"),
         src         = cms.InputTag(sourceJets),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(lo)
   )
   return PSet

def makeSimBHad(srcName,tagName,methodName):
  PSet = cms.PSet(
        pluginType  = cms.string("SimBHadronsFiller"),
        src         = cms.InputTag(srcName),
        tag         = cms.string(tagName),
        method      = cms.string(methodName+"()"),
        leadingOnly = cms.untracked.bool(False)
  )
  return PSet

def makeIVFBs(tagName,methodName):
  PSet = cms.PSet(
        pluginType  = cms.string("bCandidatesFiller"),
        src         = cms.InputTag('LCProducer','BCandFinalState'),
        tag         = cms.string(tagName),
        method      = cms.string(methodName+"()"),
        leadingOnly = cms.untracked.bool(True)
  )
  return PSet

electronLooseID = \
    '(( ' \
    'abs(superCluster.eta) < 1.442 & ' \
    'abs(deltaEtaSuperClusterTrackAtVtx) < 0.007 & ' \
    'abs(deltaPhiSuperClusterTrackAtVtx) < 0.15 & ' \
    'sigmaIetaIeta < 0.01 & ' \
    'hadronicOverEm < 0.12 ' \
    ')|( ' \
    'abs(superCluster.eta) > 1.566 & abs(superCluster.eta) < 2.5 & ' \
    'abs(deltaEtaSuperClusterTrackAtVtx) < 0.009 & ' \
    'abs(deltaPhiSuperClusterTrackAtVtx) < 0.10 & ' \
    'sigmaIetaIeta < 0.03 & ' \
    'hadronicOverEm < 0.10 ' \
    ')) & ' \
    'abs(dB) < 0.02 & ' \
    'abs(1./ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.05 & ' \
    'passConversionVeto & ' \
    'gsfTrack.trackerExpectedHitsInner.numberOfHits <= 1 & ' \
    'triggerObjectMatches.size >= 0 '

electronTightID =  \
    '(( ' \
    'abs(superCluster.eta) < 1.442 & ' \
    'abs(deltaEtaSuperClusterTrackAtVtx) < 0.004 & ' \
    'abs(deltaPhiSuperClusterTrackAtVtx) < 0.03 & ' \
    'sigmaIetaIeta < 0.01 & ' \
    'hadronicOverEm < 0.12 ' \
    ')|( ' \
    'abs(superCluster.eta) > 1.566 & abs(superCluster.eta) < 2.5 & ' \
    'abs(deltaEtaSuperClusterTrackAtVtx) < 0.005 & ' \
    'abs(deltaPhiSuperClusterTrackAtVtx) < 0.02 & ' \
    'sigmaIetaIeta < 0.03 & ' \
    'hadronicOverEm < 0.10 ' \
    ')) & ' \
    'abs(dB) < 0.02 & ' \
    'abs(1./ecalEnergy - eSuperClusterOverP/ecalEnergy) < 0.05 & ' \
    'passConversionVeto & ' \
    'gsfTrack.trackerExpectedHitsInner.numberOfHits < 1'

electronIso = '(chargedHadronIso + max((neutralHadronIso + photonIso - 0.5*puChargedHadronIso),0.0))/et'
muonIso = "(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt"

def makeGoodLeptons(srcGoodMuons='smearedGoodMuons',srcGoodElectrons='smearedGoodElectrons'):
  goodLeptons = cms.PSet(
      goodMu_pt_vec = makeMuon("goodMu_pt_vec","pt",sourceMuons=srcGoodMuons,lo=False),
      goodMu_eta_vec = makeMuon("goodMu_eta_vec","eta",sourceMuons=srcGoodMuons,lo=False),
      goodMu_phi_vec = makeMuon("goodMu_phi_vec","phi",sourceMuons=srcGoodMuons,lo=False),
      goodMu_charge_vec = makeMuon("goodMu_charge_vec","charge",sourceMuons=srcGoodMuons,lo=False),

      goodEle_pt_vec = makeElectron("goodEle_pt_vec","pt",sourceElectrons=srcGoodElectrons,lo=False),
      goodEle_eta_vec = makeElectron("goodEle_eta_vec","eta",sourceElectrons=srcGoodElectrons,lo=False),
      goodEle_phi_vec = makeElectron("goodEle_phi_vec","phi",sourceElectrons=srcGoodElectrons,lo=False),
      goodEle_charge_vec = makeElectron("goodEle_charge_vec","charge",sourceElectrons=srcGoodElectrons,lo=False),
  )
  return goodLeptons

def makeVetoLeptons(srcVetoMuons='smearedVetoMuons',srcVetoElectrons='smearedVetoElectrons'):
  vetoLeptons = cms.PSet(
      vetoMu_pt_vec = makeMuon("vetoMu_pt_vec","pt",sourceMuons=srcVetoMuons,lo=False),
      vetoMu_eta_vec = makeMuon("vetoMu_eta_vec","eta",sourceMuons=srcVetoMuons,lo=False),
      vetoMu_phi_vec = makeMuon("vetoMu_phi_vec","phi",sourceMuons=srcVetoMuons,lo=False),
      vetoMu_charge_vec = makeMuon("vetoMu_charge_vec","charge",sourceMuons=srcVetoMuons,lo=False),

      vetoEle_pt_vec = makeElectron("vetoEle_pt_vec","pt",sourceElectrons=srcVetoElectrons,lo=False),
      vetoEle_eta_vec = makeElectron("vetoEle_eta_vec","eta",sourceElectrons=srcVetoElectrons,lo=False),
      vetoEle_phi_vec = makeElectron("vetoEle_phi_vec","phi",sourceElectrons=srcVetoElectrons,lo=False),
      vetoEle_charge_vec = makeElectron("vetoEle_charge_vec","charge",sourceElectrons=srcVetoElectrons,lo=False),
  )
  return vetoLeptons

def makeQCDLeptons(srcQCDMuons='smearedQCDMuons',srcQCDElectrons='smearedQCDElectrons'):
  qcdLeptons = cms.PSet(
      qcdMu_pt_vec = makeMuon("qcdMu_pt_vec","pt",sourceMuons=srcQCDMuons,lo=False),
      qcdMu_eta_vec = makeMuon("qcdMu_eta_vec","eta",sourceMuons=srcQCDMuons,lo=False),
      qcdMu_phi_vec = makeMuon("qcdMu_phi_vec","phi",sourceMuons=srcQCDMuons,lo=False),
      qcdMu_charge_vec = makeMuon("qcdMu_charge_vec","charge",sourceMuons=srcQCDMuons,lo=False),

      qcdEle_pt_vec = makeElectron("qcdEle_pt_vec","pt",sourceElectrons=srcQCDElectrons,lo=False),
      qcdEle_eta_vec = makeElectron("qcdEle_eta_vec","eta",sourceElectrons=srcQCDElectrons,lo=False),
      qcdEle_phi_vec = makeElectron("qcdEle_phi_vec","phi",sourceElectrons=srcQCDElectrons,lo=False),
      qcdEle_charge_vec = makeElectron("qcdEle_charge_vec","charge",sourceElectrons=srcQCDElectrons,lo=False),
  )
  return qcdLeptons

def makeAllLeptons(srcAllMuons='smearedAllMuons',srcAllElectrons='smearedAllElectrons'):
  allLeptons = cms.PSet(
      # muon Kinematics
      allMu_pt_vec = makeMuon("allMu_pt_vec","pt",sourceMuons=srcAllMuons,lo=False),
      allMu_eta_vec = makeMuon("allMu_eta_vec","eta",sourceMuons=srcAllMuons,lo=False),
      allMu_phi_vec = makeMuon("allMu_phi_vec","phi",sourceMuons=srcAllMuons,lo=False),
      allMu_charge_vec = makeMuon("allMu_charge_vec","charge",sourceMuons=srcAllMuons,lo=False),
      # muon ID
      allMu_looseID_vec = makeMuon("allMu_looseID_vec","userFloat('looseID')",sourceMuons=srcAllMuons,lo=False),
      allMu_tightID_vec = makeMuon("allMu_tightID_vec","userInt('tightID')",sourceMuons=srcAllMuons,lo=False),
      # muon Isolation
      allMu_Iso_vec = makeMuon("allMu_Iso_vec",muonIso,sourceMuons=srcAllMuons,lo=False),
      allMu_chIso_vec = makeMuon("allMu_chIso_vec","pfIsolationR04().sumChargedHadronPt",sourceMuons=srcAllMuons,lo=False),
      allMu_nhIso_vec = makeMuon("allMu_nhIso_vec","pfIsolationR04().sumNeutralHadronEt",sourceMuons=srcAllMuons,lo=False),
      allMu_phIso_vec = makeMuon("allMu_phIso_vec","pfIsolationR04().sumPhotonEt",sourceMuons=srcAllMuons,lo=False),
      allMu_puIso_vec = makeMuon("allMu_puIso_vec","pfIsolationR04().sumPUPt",sourceMuons=srcAllMuons,lo=False),

      # electron Kinematics
      allEle_pt_vec = makeElectron("allEle_pt_vec","pt",sourceElectrons=srcAllElectrons,lo=False),
      allEle_eta_vec = makeElectron("allEle_eta_vec","eta",sourceElectrons=srcAllElectrons,lo=False),
      allEle_phi_vec = makeElectron("allEle_phi_vec","phi",sourceElectrons=srcAllElectrons,lo=False),
      allEle_charge_vec = makeElectron("allEle_charge_vec","charge",sourceElectrons=srcAllElectrons,lo=False),
      ## electron ID
      #allEle_looseID_vec = makeElectron("allEle_looseID_vec",electronLooseID,sourceElectrons=srcAllElectrons,lo=False),
      #allEle_tightID_vec = makeElectron("allEle_tightID_vec",electronTightID,sourceElectrons=srcAllElectrons,lo=False),
       # variables
      allEle_scEta_vec = makeElectron("allEle_scEta_vec","superCluster.eta",sourceElectrons=srcAllElectrons,lo=False),
      allEle_dEscTratVtx_vec = makeElectron("allEle_dEscTratVtx_vec",
        "deltaEtaSuperClusterTrackAtVtx",sourceElectrons=srcAllElectrons,lo=False),
      allEle_dPscTratVtx_vec = makeElectron("allEle_dPscTratVtx_vec",
        "deltaPhiSuperClusterTrackAtVtx",sourceElectrons=srcAllElectrons,lo=False),
      allEle_sIeIe_vec = makeElectron("allEle_sIeIe_vec","sigmaIetaIeta",sourceElectrons=srcAllElectrons,lo=False),
      allEle_hoEM_vec = makeElectron("allEle_hoEM_vec","hadronicOverEm",sourceElectrons=srcAllElectrons,lo=False),
      allEle_dB_vec = makeElectron("allEle_dB_vec","dB",sourceElectrons=srcAllElectrons,lo=False),
      allEle_ecalE_vec = makeElectron("allEle_ecalE_vec","ecalEnergy",sourceElectrons=srcAllElectrons,lo=False),
      allEle_escoP_vec = makeElectron("allEle_escoP_vec","eSuperClusterOverP",sourceElectrons=srcAllElectrons,lo=False),
      allEle_IoEmIoP_vec = makeElectron("allEle_IoEmIoP_vec",
        "1./ecalEnergy - eSuperClusterOverP/ecalEnergy",sourceElectrons=srcAllElectrons,lo=False),
      allEle_pConvVto_vec = makeElectron("allEle_pConvVto_vec","passConversionVeto",sourceElectrons=srcAllElectrons,lo=False),
      allEle_trkNrH_vec = makeElectron("allEle_trkNrH_vec",
        "gsfTrack.trackerExpectedHitsInner.numberOfHits",sourceElectrons=srcAllElectrons,lo=False),
      # electron Isolation
      allEle_iso_vec = makeElectron("allEle_iso_vec",electronIso,sourceElectrons=srcAllElectrons,lo=False),
      allEle_chIso_vec = makeElectron("allEle_chIso_vec","chargedHadronIso",sourceElectrons=srcAllElectrons,lo=False),
      allEle_nhIso_vec = makeElectron("allEle_nhIso_vec","neutralHadronIso",sourceElectrons=srcAllElectrons,lo=False),
      allEle_phIso_vec = makeElectron("allEle_phIso_vec","photonIso",sourceElectrons=srcAllElectrons,lo=False),
      allEle_puIso_vec = makeElectron("allEle_puIso_vec","puChargedHadronIso",sourceElectrons=srcAllElectrons,lo=False),
  )
  return allLeptons

def makeGoodJetKinematics(srcGoodJets="smearedGoodJets"):
  goodJetKinematics = cms.PSet(
     goodJ1_pt = makeJetList(strName='pt',methodName='pt()',pf='good',xn='',sourceJets=srcGoodJets)[0],
     goodJ2_pt = makeJetList(strName='pt',methodName='pt()',pf='good',xn='',sourceJets=srcGoodJets)[1],
     goodJ3_pt = makeJetList(strName='pt',methodName='pt()',pf='good',xn='',sourceJets=srcGoodJets)[2],
     goodJ4_pt = makeJetList(strName='pt',methodName='pt()',pf='good',xn='',sourceJets=srcGoodJets)[3],
     goodJ1_eta = makeJetList(strName='eta',methodName='eta()',pf='good',xn='',sourceJets=srcGoodJets)[0],
     goodJ2_eta = makeJetList(strName='eta',methodName='eta()',pf='good',xn='',sourceJets=srcGoodJets)[1],
     goodJ3_eta = makeJetList(strName='eta',methodName='eta()',pf='good',xn='',sourceJets=srcGoodJets)[2],
     goodJ4_eta = makeJetList(strName='eta',methodName='eta()',pf='good',xn='',sourceJets=srcGoodJets)[3],
     goodJ1_phi = makeJetList(strName='phi',methodName='phi()',pf='good',xn='',sourceJets=srcGoodJets)[0],
     goodJ2_phi = makeJetList(strName='phi',methodName='phi()',pf='good',xn='',sourceJets=srcGoodJets)[1],
     goodJ3_phi = makeJetList(strName='phi',methodName='phi()',pf='good',xn='',sourceJets=srcGoodJets)[2],
     goodJ4_phi = makeJetList(strName='phi',methodName='phi()',pf='good',xn='',sourceJets=srcGoodJets)[3],
  )
  return goodJetKinematics

def makeFwdJetKinematics(srcFwdJets="smearedFwdJets"):
  fwdJetKinematics = cms.PSet(
     fwdJ1_pt = makeJetList(strName='pt',methodName='pt()',pf='fwd',xn='',sourceJets=srcFwdJets)[0],
     fwdJ2_pt = makeJetList(strName='pt',methodName='pt()',pf='fwd',xn='',sourceJets=srcFwdJets)[1],
     #fwdJ3_pt = makeJetList(strName='pt',methodName='pt()',pf='fwd',xn='',sourceJets=srcFwdJets)[2],
     #fwdJ4_pt = makeJetList(strName='pt',methodName='pt()',pf='fwd',xn='',sourceJets=srcFwdJets)[3],
     fwdJ1_eta = makeJetList(strName='eta',methodName='eta()',pf='fwd',xn='',sourceJets=srcFwdJets)[0],
     fwdJ2_eta = makeJetList(strName='eta',methodName='eta()',pf='fwd',xn='',sourceJets=srcFwdJets)[1],
     #fwdJ3_eta = makeJetList(strName='eta',methodName='eta()',pf='fwd',xn='',sourceJets=srcFwdJets)[2],
     #fwdJ4_eta = makeJetList(strName='eta',methodName='eta()',pf='fwd',xn='',sourceJets=srcFwdJets)[3],
     fwdJ1_phi = makeJetList(strName='phi',methodName='phi()',pf='fwd',xn='',sourceJets=srcFwdJets)[0],
     fwdJ2_phi = makeJetList(strName='phi',methodName='phi()',pf='fwd',xn='',sourceJets=srcFwdJets)[1],
     #fwdJ3_phi = makeJetList(strName='phi',methodName='phi()',pf='fwd',xn='',sourceJets=srcFwdJets)[2],
     #fwdJ4_phi = makeJetList(strName='phi',methodName='phi()',pf='fwd',xn='',sourceJets=srcFwdJets)[3],
  )
  return fwdJetKinematics

def makeCleanJetKinematics(srcCleanJets="smearedCleanJets"):
  cleanJetKinematics = cms.PSet(
     cleanJ1_pt = makeJetList(strName='pt',methodName='pt()',pf='clean',xn='',sourceJets=srcCleanJets)[0],
     cleanJ2_pt = makeJetList(strName='pt',methodName='pt()',pf='clean',xn='',sourceJets=srcCleanJets)[1],
     cleanJ3_pt = makeJetList(strName='pt',methodName='pt()',pf='clean',xn='',sourceJets=srcCleanJets)[2],
     cleanJ4_pt = makeJetList(strName='pt',methodName='pt()',pf='clean',xn='',sourceJets=srcCleanJets)[3],
     cleanJ1_eta = makeJetList(strName='eta',methodName='eta()',pf='clean',xn='',sourceJets=srcCleanJets)[0],
     cleanJ2_eta = makeJetList(strName='eta',methodName='eta()',pf='clean',xn='',sourceJets=srcCleanJets)[1],
     cleanJ3_eta = makeJetList(strName='eta',methodName='eta()',pf='clean',xn='',sourceJets=srcCleanJets)[2],
     cleanJ4_eta = makeJetList(strName='eta',methodName='eta()',pf='clean',xn='',sourceJets=srcCleanJets)[3],
     cleanJ1_phi = makeJetList(strName='phi',methodName='phi()',pf='clean',xn='',sourceJets=srcCleanJets)[0],
     cleanJ2_phi = makeJetList(strName='phi',methodName='phi()',pf='clean',xn='',sourceJets=srcCleanJets)[1],
     cleanJ3_phi = makeJetList(strName='phi',methodName='phi()',pf='clean',xn='',sourceJets=srcCleanJets)[2],
     cleanJ4_phi = makeJetList(strName='phi',methodName='phi()',pf='clean',xn='',sourceJets=srcCleanJets)[3],
  )
  return cleanJetKinematics

def makeAllJetKinematics(srcAllJets="smearedAllJets"):
  allJetKinematics = cms.PSet(
     allJ1_pt = makeJetList(strName='pt',methodName='pt()',pf='all',xn='',sourceJets=srcAllJets)[0],
     allJ2_pt = makeJetList(strName='pt',methodName='pt()',pf='all',xn='',sourceJets=srcAllJets)[1],
     allJ3_pt = makeJetList(strName='pt',methodName='pt()',pf='all',xn='',sourceJets=srcAllJets)[2],
     allJ4_pt = makeJetList(strName='pt',methodName='pt()',pf='all',xn='',sourceJets=srcAllJets)[3],
     allJ1_eta = makeJetList(strName='eta',methodName='eta()',pf='all',xn='',sourceJets=srcAllJets)[0],
     allJ2_eta = makeJetList(strName='eta',methodName='eta()',pf='all',xn='',sourceJets=srcAllJets)[1],
     allJ3_eta = makeJetList(strName='eta',methodName='eta()',pf='all',xn='',sourceJets=srcAllJets)[2],
     allJ4_eta = makeJetList(strName='eta',methodName='eta()',pf='all',xn='',sourceJets=srcAllJets)[3],
     allJ1_phi = makeJetList(strName='phi',methodName='phi()',pf='all',xn='',sourceJets=srcAllJets)[0],
     allJ2_phi = makeJetList(strName='phi',methodName='phi()',pf='all',xn='',sourceJets=srcAllJets)[1],
     allJ3_phi = makeJetList(strName='phi',methodName='phi()',pf='all',xn='',sourceJets=srcAllJets)[2],
     allJ4_phi = makeJetList(strName='phi',methodName='phi()',pf='all',xn='',sourceJets=srcAllJets)[3],
  )
  return allJetKinematics

def makeCSVJets(srcGoodJets='smearedGoodJets',srcFwdJets='smearedFwdJets'):
  csvJets = cms.PSet(
     goodJ1_CSV = makeJetList(strName='CSV',methodName='bDiscriminator("combinedSecondaryVertexBJetTags")',
       pf='good',xn='',sourceJets=srcGoodJets)[0],
     goodJ2_CSV = makeJetList(strName='CSV',methodName='bDiscriminator("combinedSecondaryVertexBJetTags")',
       pf='good',xn='',sourceJets=srcGoodJets)[1],
     goodJ3_CSV = makeJetList(strName='CSV',methodName='bDiscriminator("combinedSecondaryVertexBJetTags")',
       pf='good',xn='',sourceJets=srcGoodJets)[2],
     goodJ4_CSV = makeJetList(strName='CSV',methodName='bDiscriminator("combinedSecondaryVertexBJetTags")',
       pf='good',xn='',sourceJets=srcGoodJets)[3],
     fwdJ1_CSV = makeJetList(strName='CSV',methodName='bDiscriminator("combinedSecondaryVertexBJetTags")',
       pf='fwd',xn='',sourceJets=srcFwdJets)[0],
     fwdJ2_CSV = makeJetList(strName='CSV',methodName='bDiscriminator("combinedSecondaryVertexBJetTags")',
       pf='fwd',xn='',sourceJets=srcFwdJets)[1],

    ###  TO DO ADD SCALE FACTORS ** PUT THEM IN JETS ALREADY WITH APPROPRIATE FLAVOR
  )
  return csvJets
#def makeCSVscalefactors(srcGoodJets='smearedGoodJets',srcFwdJets='smearedFwdJets'):
#  csvScalefactors = cms.PSet(
#    # from RecoTools/plugins/bTagSFer.h 
#    J1_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[0],
#    J2_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[1],
#    J3_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[2],
#    J4_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[3],
#    J1_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[0],
#    J2_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[1],
#    J3_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[2],
#    J4_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[3],
#    J1_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[0],
#    J2_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[1],
#    J3_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[2],
#    J4_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[3],
#    J1_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[0],
#    J2_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[1],
#    J3_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[2],
#    J4_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[3],
#    J1_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[0],
#    J2_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[1],
#    J3_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[2],
#    J4_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[3],
#
#    J1_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[0],
#    J2_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[1],
#    J3_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[2],
#    J4_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[3],
#    J1_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[0],
#    J2_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[1],
#    J3_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[2],
#    J4_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[3],
#    J1_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[0],
#    J2_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[1],
#    J3_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[2],
#    J4_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[3],
#    J1_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[0],
#    J2_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[1],
#    J3_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[2],
#    J4_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[3],
#    J1_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[0],
#    J2_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[1],
#    J3_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[2],
#    J4_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[3],
#
#    # from RecoTools/plugins/PATJetCSVreweight.h
#    J1_CSVreweight = makeJetUserFloat('CSVreweight','',source)[0],
#    J2_CSVreweight = makeJetUserFloat('CSVreweight','',source)[1],
#    J3_CSVreweight = makeJetUserFloat('CSVreweight','',source)[2],
#    J4_CSVreweight = makeJetUserFloat('CSVreweight','',source)[3],

#    J1_partonFlavour = makeJetStringPar('partonFlavour','',source)[0],
#    J2_partonFlavour = makeJetStringPar('partonFlavour','',source)[1],
#    J3_partonFlavour = makeJetStringPar('partonFlavour','',source)[2],
#    J4_partonFlavour = makeJetStringPar('partonFlavour','',source)[3],
#  )
#  return csvScalefactors

def makeSVJets(srcGoodJets='smearedGoodJets',srcFwdJets='smearedFwdJets'):
  svJets = cms.PSet(
  # SV info and tracks 
  )
  return svJets
## from RecoTools/plugins/PATSSVJetEmbedder.h 
#    J1_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[0],
#    J2_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[1],
#    J3_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[2],
#    J4_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[3],
#    J1_pt_SSV = makeJetUserFloat('pt_SSV','',source)[0],  
#    J2_pt_SSV = makeJetUserFloat('pt_SSV','',source)[1],
#    J3_pt_SSV = makeJetUserFloat('pt_SSV','',source)[2],
#    J4_pt_SSV = makeJetUserFloat('pt_SSV','',source)[3],
#    J1_eta_SSV = makeJetUserFloat('eta_SSV','',source)[0],  
#    J2_eta_SSV = makeJetUserFloat('eta_SSV','',source)[1],
#    J3_eta_SSV = makeJetUserFloat('eta_SSV','',source)[2],
#    J4_eta_SSV = makeJetUserFloat('eta_SSV','',source)[3],
#    J1_phi_SSV = makeJetUserFloat('phi_SSV','',source)[0],  
#    J2_phi_SSV = makeJetUserFloat('phi_SSV','',source)[1],
#    J3_phi_SSV = makeJetUserFloat('phi_SSV','',source)[2],
#    J4_phi_SSV = makeJetUserFloat('phi_SSV','',source)[3],
#    J1_mass_SSV = makeJetUserFloat('mass_SSV','',source)[0], # formerly J1SVMassb
#    J2_mass_SSV = makeJetUserFloat('mass_SSV','',source)[1],
#    J3_mass_SSV = makeJetUserFloat('mass_SSV','',source)[2],
#    J4_mass_SSV = makeJetUserFloat('mass_SSV','',source)[3],
#    J1_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[0],  
#    J2_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[1],
#    J3_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[2],
#    J4_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[3],
#
## from RecoTools/plugins/PATCSVVertex.cc
#    J1_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[0],
#    J2_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[1],
#    J3_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[2],
#    J4_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[3],
#    J1_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[0],
#    J2_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[1],
#    J3_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[2],
#    J4_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[3],
#    J1_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[0],
#    J2_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[1],
#    J3_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[2],
#    J4_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[3],
#    J1_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[0],
#    J2_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[1],
#    J3_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[2],
#    J4_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[3],
#    J1_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[0],
#    J2_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[1],
#    J3_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[2],
#    J4_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[3],
#    J1_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[0],
#    J2_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[1],
#    J3_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[2],
#    J4_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[3],
#    J1_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[0],
#    J2_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[1],
#    J3_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[2],
#    J4_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[3],
#    )

def makeAltBTags(srcGoodJets='smearedGoodJets',srcFwdJets='smearedFwdJets'):
  altBTags = cms.PSet(
  # other options for bTagging
  )
  return altBTags
# # Jet b Tagging
#    J1_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[0],
#    J2_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[1],
#    J3_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[2],
#    J4_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[3],
#    J1_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[0],
#    J2_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[1],
#    J3_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[2],
#    J4_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[3],
#    J1_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[0],
#    J2_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[1],
#    J3_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[2],
#    J4_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[3],
#    J1_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[0],
#    J2_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[1],
#    J3_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[2],
#    J4_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[3],

def makeMETobjects(srcMET='metCorrected',srcElectrons='smearedGoodElectrons',srcMuons='smearedGoodMuons'):
   metObjects = cms.PSet(
    met_pt = makeMET("met_pt","pt()",sourceMET=srcMET,lo=True),
    met_eta = makeMET("met_eta","eta()",sourceMET=srcMET,lo=True),
    met_eesUp_pt = makeMET("met_eesUp_pt",'userFloat("eesUp_pt")',sourceMET=srcMET,lo=True),
    met_eesDn_pt = makeMET("met_eesDn_pt",'userFloat("eesDn_pt")',sourceMET=srcMET,lo=True),
    met_uesUp_pt = makeMET("met_uesUp_pt",'userFloat("uesUp_pt")',sourceMET=srcMET,lo=True),
    met_uesDn_pt = makeMET("met_uesDn_pt",'userFloat("uesDn_pt")',sourceMET=srcMET,lo=True),
    met_jesUp_pt = makeMET("met_jesUp_pt",'userFloat("jesUp_pt")',sourceMET=srcMET,lo=True),
    met_jesDn_pt = makeMET("met_jesDn_pt",'userFloat("jesDn_pt")',sourceMET=srcMET,lo=True),
    met_eesUp_eta = makeMET("met_eesUp_eta","userFloat('eesUp_eta')",sourceMET=srcMET,lo=True),
    met_eesDn_eta = makeMET("met_eesDn_eta","userFloat('eesDn_eta')",sourceMET=srcMET,lo=True),
    met_uesUp_eta = makeMET("met_uesUp_eta","userFloat('uesUp_eta')",sourceMET=srcMET,lo=True),
    met_uesDn_eta = makeMET("met_uesDn_eta","userFloat('uesDn_eta')",sourceMET=srcMET,lo=True),
    met_jesUp_eta = makeMET("met_jesUp_eta","userFloat('jesUp_eta')",sourceMET=srcMET,lo=True),
    met_jesDn_eta = makeMET("met_jesDn_eta","userFloat('jesDn_eta')",sourceMET=srcMET,lo=True),
    mt_electron_vec = makeElectron('mt_electron_vec','userFloat("mt")',sourceElectrons=srcElectrons,lo=False),
    mt_muon_vec = makeMuon('mt_muon_vec','userFloat("mt")',sourceMuons=srcMuons,lo=False),
   )
   return metObjects

def makeVertexInfo():
  vertexInfo = cms.PSet(
    vertices = cms.PSet(
        pluginType = cms.string("VertexSizeFiller"),
        src = cms.InputTag("primaryVertexFilter"),
        tag = cms.string("vertices")
    ), 
    pu = cms.PSet(
        pluginType = cms.string("PUFiller"),
        src = cms.InputTag("addPileupInfo"),
        tag = cms.string("pu"),
    ),
    trigger = cms.PSet(
        pluginType = cms.string("TriggerFiller"),
        src = cms.InputTag("patTrigger"),
        paths = cms.vstring(TriggerPaths)
    ),
  )
  return vertexInfo

def makeCountedCollections(srcGoodMuons='smearedGoodMuons',
                           srcVetoMuons='smearedVetoMuons',
                           srcQCDMuons='smearedQCDMuons',
                           srcAllMuons='smearedAllMuons', #
                           srcGoodElectrons='smearedGoodElectrons',
                           srcVetoElectrons='smearedVetoElectrons',
                           srcQCDElectrons='smearedQCDElectrons',
                           srcAllElectrons='smearedAllElectrons', #
                           srcGoodJets='smearedGoodJets',
                           srcFwdJets='smearedFwdJets',
                           srcAllJets='smearedAllJets', #
                           srcCleanJets='smearedCleanJets', #
                          ):
  countedCollections = cms.PSet(
    nrGoodMu = makeCollSize(srcName=srcGoodMuons,tagName='nrGoodMu'),
    nrVetoMu = makeCollSize(srcName=srcVetoMuons,tagName='nrVetoMu'),
    nrQCDMu = makeCollSize(srcName=srcQCDMuons,tagName='nrQCDMu'),
    nrAllMu = makeCollSize(srcName=srcAllMuons,tagName='nrAllMu'), #

    nrGoodEle = makeCollSize(srcName=srcGoodElectrons,tagName='nrGoodEle'),
    nrVetoEle = makeCollSize(srcName=srcVetoElectrons,tagName='nrVetoEle'),
    nrQCDEle = makeCollSize(srcName=srcQCDElectrons,tagName='nrQCDEle'),
    nrAllEle = makeCollSize(srcName=srcAllElectrons,tagName='nrAllEle'), #

    nrGoodJets = makeCollSize(srcName=srcGoodJets,tagName='nrGoodJets'),
    nrFwdJets = makeCollSize(srcName=srcFwdJets,tagName='nrFwdJets'),
    nrAllJets = makeCollSize(srcName=srcAllJets,tagName='nrAllJets'), #
    nrCleanJets = makeCollSize(srcName=srcCleanJets,tagName='nrCleanJets'), #
  )
  return countedCollections


def makeIVFcandidates():
  ivfCandidates = cms.PSet(
    bCandidatenBC = makeIVFBs("bCandidatenBC","nBC"),
    bCandidate1Pt = makeIVFBs("bCandidate1Pt","BC1PT"),
    bCandidate2Pt = makeIVFBs("bCandidate2Pt","BC2PT"),
    bCandidate1Eta = makeIVFBs("bCandidate1Eta","BC1ETA"),
    bCandidate2Eta = makeIVFBs("bCandidate2Eta","BC2ETA"),
    bCandidate1Phi = makeIVFBs("bCandidate1Phi","BC1PHI"),
    bCandidate2Phi = makeIVFBs("bCandidate2Phi","BC2PHI"),
    bCandidateDeltaR = makeIVFBs("bCandidateDeltaR","BCDeltaR"),
    bCandidateDeltaPhi = makeIVFBs("bCandidateDeltaPhi","BDeltaPHI"),
    bCandidateBC1nTracks = makeIVFBs("bCandidateBC1nTracks","BC1nTracks"),
    bCandidateBC2nTracks = makeIVFBs("bCandidateBC2nTracks","BC2nTracks"),
    bCandidateBCEnergySum = makeIVFBs("bCandidateBCEnergySum","BCEnergySum"),
    bCandidateBCGenEnergySum = makeIVFBs("bCandidateBCGenEnergySum","BCGenEnergySum"),
    bCandidatenJetAssociatedToBC1 = makeIVFBs("bCandidatenJetAssociatedToBC1","nJetAssociatedToBC1"),
    bCandidatenJetAssociatedToBC2 = makeIVFBs("bCandidatenJetAssociatedToBC2","nJetAssociatedToBC2"),
    bCandidatenJetAssociatedToBC = makeIVFBs("bCandidatenJetAssociatedToBC","nJetAssociatedToBC"),
    bCandidateJet1BC1PT = makeIVFBs("bCandidateJet1BC1PT","Jet1BC1PT"),
    bCandidateJet2BC1PT = makeIVFBs("bCandidateJet2BC1PT","Jet2BC1PT"),
    bCandidateJet3BC1PT = makeIVFBs("bCandidateJet3BC1PT","Jet3BC1PT"),
    bCandidateJet4BC1PT = makeIVFBs("bCandidateJet4BC1PT","Jet4BC1PT"),
    bCandidateJet1BC1ETA = makeIVFBs("bCandidateJet1BC1ETA","Jet1BC1ETA"),
    bCandidateJet2BC1ETA = makeIVFBs("bCandidateJet2BC1ETA","Jet2BC1ETA"),
    bCandidateJet3BC1ETA = makeIVFBs("bCandidateJet3BC1ETA","Jet3BC1ETA"),
    bCandidateJet4BC1ETA = makeIVFBs("bCandidateJet4BC1ETA","Jet4BC1ETA"),
    bCandidateJet1BC1PHI = makeIVFBs("bCandidateJet1BC1PHI","Jet1BC1PHI"),
    bCandidateJet2BC1PHI = makeIVFBs("bCandidateJet2BC1PHI","Jet2BC1PHI"),
    bCandidateJet3BC1PHI = makeIVFBs("bCandidateJet3BC1PHI","Jet3BC1PHI"),
    bCandidateJet4BC1PHI = makeIVFBs("bCandidateJet4BC1PHI","Jet4BC1PHI"),
    bCandidateJet1BC2PT = makeIVFBs("bCandidateJet1BC2PT","Jet1BC2PT"),
    bCandidateJet2BC2PT = makeIVFBs("bCandidateJet2BC2PT","Jet2BC2PT"),
    bCandidateJet3BC2PT = makeIVFBs("bCandidateJet3BC2PT","Jet3BC2PT"),
    bCandidateJet4BC2PT = makeIVFBs("bCandidateJet4BC2PT","Jet4BC2PT"),
    bCandidateJet1BC2ETA = makeIVFBs("bCandidateJet1BC2ETA","Jet1BC2ETA"),
    bCandidateJet2BC2ETA = makeIVFBs("bCandidateJet2BC2ETA","Jet2BC2ETA"),
    bCandidateJet3BC2ETA = makeIVFBs("bCandidateJet3BC2ETA","Jet3BC2ETA"),
    bCandidateJet4BC2ETA = makeIVFBs("bCandidateJet4BC2ETA","Jet4BC2ETA"),
    bCandidateJet1BC2PHI = makeIVFBs("bCandidateJet1BC2PHI","Jet1BC2PHI"),
    bCandidateJet2BC2PHI = makeIVFBs("bCandidateJet2BC2PHI","Jet2BC2PHI"),
    bCandidateJet3BC2PHI = makeIVFBs("bCandidateJet3BC2PHI","Jet3BC2PHI"),
    bCandidateJet4BC2PHI = makeIVFBs("bCandidateJet4BC2PHI","Jet4BC2PHI"),
    bCandidateBCDeltaR = makeIVFBs("bCandidateBCDeltaR","BCDeltaR"),
    bCandidateBDeltaPHI = makeIVFBs("bCandidateBDeltaPHI","BDeltaPHI"),
    bCandidateBC1MASS = makeIVFBs("bCandidateBC1MASS","BC1MASS"),
    bCandidateBC2MASS = makeIVFBs("bCandidateBC2MASS","BC2MASS"),
  )
  return ivfCandidates

def makeMuon(tagName,methodName,sourceMuons='smearedGoodMuons',lo=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuonFiller"),
         src         = cms.InputTag(sourceMuons),
         tag         = cms.string(tagName),
         method      = cms.string(methodName),
         leadingOnly = cms.untracked.bool(lo)
   )
   return PSet

def makeMuNu(tagName,methodName,source='wCandsJets',lo=True):
  PSet = cms.PSet(
        pluginType  = cms.string("PATMuonNuPairFiller"),
        src         = cms.InputTag(source),
        tag         = cms.string(tagName),
        method      = cms.string(methodName),
        leadingOnly = cms.untracked.bool(lo)
  )
  return PSet

def makeScaleFactors(srcMuons='smearedGoodMuons'):
  scaleFactors = cms.PSet(
    EffWEIGHTCSVL    = makeMuon(tagName="EffWEIGHTCSVL",   methodName="SFCSVL1", sourceMuons=srcMuons,lo=False),
    EffWEIGHTCSVL2   = makeMuon(tagName="EffWEIGHTCSVL2",  methodName="SFCSVL2", sourceMuons=srcMuons,lo=False),
    EffWEIGHTCSVM    = makeMuon(tagName="EffWEIGHTCSVM",   methodName="SFCSVM1", sourceMuons=srcMuons,lo=False),
    EffWEIGHTCSVM2   = makeMuon(tagName="EffWEIGHTCSVM2",  methodName="SFCSVM2", sourceMuons=srcMuons,lo=False),
    EffWEIGHTCSVT    = makeMuon(tagName="EffWEIGHTCSVT",   methodName="SFCSVT1", sourceMuons=srcMuons,lo=False),
    EffWEIGHTCSVT2   = makeMuon(tagName="EffWEIGHTCSVT2",  methodName="SFCSVT2", sourceMuons=srcMuons,lo=False),
    EffWEIGHTSSVHEM  = makeMuon(tagName="EffWEIGHTSSVHEM", methodName="SFSSVHE1",sourceMuons=srcMuons,lo=False),
    EffWEIGHTSSVHEM2 = makeMuon(tagName="EffWEIGHTSSVHEM2",methodName="SFSSVHE2",sourceMuons=srcMuons,lo=False),
    # scale factors for electrons ?? 
    weight_mu_TR  = makeMuon(tagName='weight_mu_TR', methodName='EffWEIGHTeta_TR',sourceMuons=srcMuons,lo=False),
    weight_mu_Iso = makeMuon(tagName="weight_mu_Iso",methodName="EffWEIGHTeta_IS",sourceMuons=srcMuons,lo=False),
    weight_mu_ID  = makeMuon(tagName="weight_mu_ID", methodName="EffWEIGHTeta_ID",sourceMuons=srcMuons,lo=False),
  )
  return scaleFactors

def makeHenBHadrons():
  henBHadrons = cms.PSet(
    bHadronsPt = makeSimBHad("bhadrons","bHadronsPt","pt"),
    bHadronsEta = makeSimBHad("bhadrons","bHadronsEta","eta"),
    bHadronsPhi = makeSimBHad("bhadrons","bHadronsPhi","phi"),
    nbHadrons = makeCollSize("bhadrons","nbHadrons"),
    genTs = makeCollSize("gentCands","genTs"),
    genTbars = makeCollSize("gentbarCands","genTbars"),
    genBs = makeCollSize("genbbCands","genBs"),
    genCs = makeCollSize("genccCands","genCs"),
    genDs = makeCollSize("genddCands","genDs"),
    genUs = makeCollSize("genuuCands","genUs"),
    genSs = makeCollSize("genSSCands","genSs"),
    genWs = makeCollSize("genWs","genWs"),
  )
  return henBHadrons

def makeGenJetInfo(srcAllJets='smearedAllJets'):
   # Gen Jet information embedded from RecoTools/plugins/PATJetSmearer.h 
  jetGenInfo = cms.PSet(
    J1_pt_gen_NoNu = makeJetList(strName='pt_gen_NoNu',methodName='userFloat("pt_gen_NoNu")',xn='',sourceJets=srcAllJets)[0],
    J2_pt_gen_NoNu = makeJetList(strName='pt_gen_NoNu',methodName='userFloat("pt_gen_NoNu")',xn='',sourceJets=srcAllJets)[1],
    J3_pt_gen_NoNu = makeJetList(strName='pt_gen_NoNu',methodName='userFloat("pt_gen_NoNu")',xn='',sourceJets=srcAllJets)[2],
    J4_pt_gen_NoNu = makeJetList(strName='pt_gen_NoNu',methodName='userFloat("pt_gen_NoNu")',xn='',sourceJets=srcAllJets)[3],
    J1_eta_gen_NoNu = makeJetList(strName='eta_gen_NoNu',methodName='userFloat("eta_gen_NoNu")',xn='',sourceJets=srcAllJets)[0],
    J2_eta_gen_NoNu = makeJetList(strName='eta_gen_NoNu',methodName='userFloat("eta_gen_NoNu")',xn='',sourceJets=srcAllJets)[1],
    J3_eta_gen_NoNu = makeJetList(strName='eta_gen_NoNu',methodName='userFloat("eta_gen_NoNu")',xn='',sourceJets=srcAllJets)[2],
    J4_eta_gen_NoNu = makeJetList(strName='eta_gen_NoNu',methodName='userFloat("eta_gen_NoNu")',xn='',sourceJets=srcAllJets)[3],
    J1_phi_gen_NoNu = makeJetList(strName='phi_gen_NoNu',methodName='userFloat("phi_gen_NoNu")',xn='',sourceJets=srcAllJets)[0],
    J2_phi_gen_NoNu = makeJetList(strName='phi_gen_NoNu',methodName='userFloat("phi_gen_NoNu")',xn='',sourceJets=srcAllJets)[1],
    J3_phi_gen_NoNu = makeJetList(strName='phi_gen_NoNu',methodName='userFloat("phi_gen_NoNu")',xn='',sourceJets=srcAllJets)[2],
    J4_phi_gen_NoNu = makeJetList(strName='phi_gen_NoNu',methodName='userFloat("phi_gen_NoNu")',xn='',sourceJets=srcAllJets)[3],
    J1_pt_gen_Nu = makeJetList(strName='pt_gen_Nu',methodName='userFloat("pt_gen_Nu")',xn='',sourceJets=srcAllJets)[0],
    J2_pt_gen_Nu = makeJetList(strName='pt_gen_Nu',methodName='userFloat("pt_gen_Nu")',xn='',sourceJets=srcAllJets)[1],
    J3_pt_gen_Nu = makeJetList(strName='pt_gen_Nu',methodName='userFloat("pt_gen_Nu")',xn='',sourceJets=srcAllJets)[2],
    J4_pt_gen_Nu = makeJetList(strName='pt_gen_Nu',methodName='userFloat("pt_gen_Nu")',xn='',sourceJets=srcAllJets)[3],
    J1_eta_gen_Nu = makeJetList(strName='eta_gen_Nu',methodName='userFloat("eta_gen_Nu")',xn='',sourceJets=srcAllJets)[0],
    J2_eta_gen_Nu = makeJetList(strName='eta_gen_Nu',methodName='userFloat("eta_gen_Nu")',xn='',sourceJets=srcAllJets)[1],
    J3_eta_gen_Nu = makeJetList(strName='eta_gen_Nu',methodName='userFloat("eta_gen_Nu")',xn='',sourceJets=srcAllJets)[2],
    J4_eta_gen_Nu = makeJetList(strName='eta_gen_Nu',methodName='userFloat("eta_gen_Nu")',xn='',sourceJets=srcAllJets)[3],
    J1_phi_gen_Nu = makeJetList(strName='phi_gen_Nu',methodName='userFloat("phi_gen_Nu")',xn='',sourceJets=srcAllJets)[0],
    J2_phi_gen_Nu = makeJetList(strName='phi_gen_Nu',methodName='userFloat("phi_gen_Nu")',xn='',sourceJets=srcAllJets)[1],
    J3_phi_gen_Nu = makeJetList(strName='phi_gen_Nu',methodName='userFloat("phi_gen_Nu")',xn='',sourceJets=srcAllJets)[2],
    J4_phi_gen_Nu = makeJetList(strName='phi_gen_Nu',methodName='userFloat("phi_gen_Nu")',xn='',sourceJets=srcAllJets)[3],
  )
  return jetGenInfo

def addMuNuEventTreePtData(process,name):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
     makeGoodLeptons(),
     makeVetoLeptons(),
     makeQCDLeptons(),
     makeAllLeptons(),
     makeGoodJetKinematics(),
     makeFwdJetKinematics(),
     makeCleanJetKinematics(),
     makeAllJetKinematics(),
     makeCSVJets(),
     makeSVJets(), ##
     makeAltBTags(), ##
     makeMETobjects(),
     makeVertexInfo(),
     makeCountedCollections(),
     makeIVFcandidates(),
     coreCollections = cms.VInputTag(
       cms.InputTag("smearedAllMuons"),
       cms.InputTag("smearedAllElectrons"),
     ),
   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)

def addMuNuEventTreePtMC(process,name,lhep="externalLHEProducer"):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
     makeGoodLeptons(),
     makeVetoLeptons(),
     makeQCDLeptons(),
     makeAllLeptons(),
     makeGoodJetKinematics(),
     makeFwdJetKinematics(),
     makeCleanJetKinematics(),
     makeAllJetKinematics(),
     makeCSVJets(),
     makeSVJets(), ##
     makeAltBTags(), ##
     makeMETobjects(),
     makeVertexInfo(),
     makeCountedCollections(),
     makeIVFcandidates(),
     #makeScaleFactors(srcMuons='smearedGoodMuons'),
     makeHenBHadrons(),
     makeGenJetInfo(),
     coreCollections = cms.VInputTag(
       cms.InputTag("smearedAllMuons"),
       cms.InputTag("smearedAllElectrons"),
       cms.InputTag("smearedAllJets"),
     ),
     topweight= cms.PSet(
           pluginType = cms.string("TopWeight"),
           src = cms.InputTag("genParticles")
      ),
     muNuLHEProduct = cms.PSet(
          pluginType = cms.string("LHEProductFiller"),
          src = cms.InputTag(lhep), 
          tag = cms.string("LHEProduct"),
      ),
   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)


#def makeJetIDInfo(source = 'wCandsJets'):
#   jetIDInfo = cms.PSet( 
#    
#     # variables going in to Jet ID  https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Documentation
#    #J1_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[0],
#    #J1_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[0],
#    #J1_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[0],
#    #J1_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[0],
#    #J1_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[0],
#    #J1_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[0],
#    #J1_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[0],
#    #J2_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[1],
#    #J2_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[1],
#    #J2_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[1],
#    #J2_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[1],
#    #J2_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[1],
#    #J2_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[1],
#    #J2_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[1],
#    #J3_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[2],
#    #J3_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[2],
#    #J3_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[2],
#    #J3_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[2],
#    #J3_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[2],
#    #J3_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[2],
#    #J3_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[2],
#    #J4_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[3],
#    #J4_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[3],
#    #J4_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[3],
#    #J4_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[3],
#    #J4_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[3],
#    #J4_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[3],
#    #J4_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[3],
#
#    # Jet ID and Pu ID
#    J1_idTightJet = makeJetUserFloat('idTight','Jet',source)[0], 
#    J2_idTightJet = makeJetUserFloat('idTight','Jet',source)[1], 
#    J3_idTightJet = makeJetUserFloat('idTight','Jet',source)[2], 
#    J4_idTightJet = makeJetUserFloat('idTight','Jet',source)[3], 
#    J1_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[0], 
#    J2_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[1], 
#    J3_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[2], 
#    J4_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[3], 
#    J1_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[0], 
#    J2_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[1], 
#    J3_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[2], 
#    J4_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[3], 
#    J1_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[0], 
#    J2_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[1], 
#    J3_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[2], 
#    J4_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[3], 
#    #J1_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[0], 
#    #J2_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[1], 
#    #J3_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[2], 
#    #J4_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[3], 
#    #J1_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[0], 
#    #J2_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[1], 
#    #J3_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[2], 
#    #J4_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[3], 
#    #J1_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[0], 
#    #J2_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[1], 
#    #J3_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[2], 
#    #J4_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[3], 
#    J1_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[0],
#    J2_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[1],
#    J3_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[2],
#    J4_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[3],
#    #J1_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[0],
#    #J2_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[1],
#    #J3_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[2],
#    #J4_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[3],
#    J1_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[0],
#    J2_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[1],
#    J3_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[2],
#    J4_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[3],
#    J1_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[0],
#    J2_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[1],
#    J3_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[2],
#    J4_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[3],
#    J1_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[0],
#    J2_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[1],
#    J3_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[2],
#    J4_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[3],
#    J1_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[0],
#    J2_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[1],
#    J3_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[2],
#    J4_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[3],
#    #J1_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[0],
#    #J2_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[1],
#    #J3_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[2],
#    #J4_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[3],
#    #J1_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[0],
#    #J2_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[1],
#    #J3_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[2],
#    #J4_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[3],
#   )
#   return jetIDInfo
#
#def makeJetCorrectionInfo(source = 'wCandsJets'):
#    # Jets at Various Levels of Correction from RecoTools/plugins/PATJetOverloader.h
#   jetCorrectionInfo = cms.PSet(
#    J1_pt_L1  = makeJetUserFloat('pt_L1' ,'',source)[0],
#    J1_eta_L1 = makeJetUserFloat('eta_L1','',source)[0],
#    J1_phi_L1 = makeJetUserFloat('phi_L1','',source)[0],
#    J1_pt_L2  = makeJetUserFloat('pt_L2' ,'',source)[0],
#    J1_eta_L2 = makeJetUserFloat('eta_L2','',source)[0],
#    J1_phi_L2 = makeJetUserFloat('phi_L2','',source)[0],
#    J1_pt_L3  = makeJetUserFloat('pt_L3' ,'',source)[0],
#    J1_eta_L3 = makeJetUserFloat('eta_L3','',source)[0],
#    J1_phi_L3 = makeJetUserFloat('phi_L3','',source)[0],
#    J2_pt_L1  = makeJetUserFloat('pt_L1' ,'',source)[1],
#    J2_eta_L1 = makeJetUserFloat('eta_L1','',source)[1],
#    J2_phi_L1 = makeJetUserFloat('phi_L1','',source)[1],
#    J2_pt_L2  = makeJetUserFloat('pt_L2' ,'',source)[1],
#    J2_eta_L2 = makeJetUserFloat('eta_L2','',source)[1],
#    J2_phi_L2 = makeJetUserFloat('phi_L2','',source)[1],
#    J2_pt_L3  = makeJetUserFloat('pt_L3' ,'',source)[1],
#    J2_eta_L3 = makeJetUserFloat('eta_L3','',source)[1],
#    J2_phi_L3 = makeJetUserFloat('phi_L3','',source)[1],
#    J3_pt_L1  = makeJetUserFloat('pt_L1' ,'',source)[2],
#    J3_eta_L1 = makeJetUserFloat('eta_L1','',source)[2],
#    J3_phi_L1 = makeJetUserFloat('phi_L1','',source)[2],
#    J3_pt_L2  = makeJetUserFloat('pt_L2' ,'',source)[2],
#    J3_eta_L2 = makeJetUserFloat('eta_L2','',source)[2],
#    J3_phi_L2 = makeJetUserFloat('phi_L2','',source)[2],
#    J3_pt_L3  = makeJetUserFloat('pt_L3' ,'',source)[2],
#    J3_eta_L3 = makeJetUserFloat('eta_L3','',source)[2],
#    J3_phi_L3 = makeJetUserFloat('phi_L3','',source)[2],
#    J4_pt_L1  = makeJetUserFloat('pt_L1' ,'',source)[3],
#    J4_eta_L1 = makeJetUserFloat('eta_L1','',source)[3],
#    J4_phi_L1 = makeJetUserFloat('phi_L1','',source)[3],
#    J4_pt_L2  = makeJetUserFloat('pt_L2' ,'',source)[3],
#    J4_eta_L2 = makeJetUserFloat('eta_L2','',source)[3],
#    J4_phi_L2 = makeJetUserFloat('phi_L2','',source)[3],
#    J4_pt_L3  = makeJetUserFloat('pt_L3' ,'',source)[3],
#    J4_eta_L3 = makeJetUserFloat('eta_L3','',source)[3],
#    J4_phi_L3 = makeJetUserFloat('phi_L3','',source)[3],
#   )
#   return jetCorrectionInfo






#    J1_flightDistance = makeJetUserFloat('flightDistance','',source)[0],
#    J2_flightDistance = makeJetUserFloat('flightDistance','',source)[1],
#    J1_errorFlightDistance = makeJetUserFloat('errorFlightDistance','',source)[0],
#    J2_errorFlightDistance = makeJetUserFloat('errorFlightDistance','',source)[1],
#    J1_DR = makeJetUserFloat('DR','',source)[0],
#    J2_DR = makeJetUserFloat('DR','',source)[1],
#    J1_ptRMS = makeJetUserFloat('ptRMS','',source)[0],
#    J2_ptRMS = makeJetUserFloat('ptRMS','',source)[1],
#    J1_dxy = makeJetUserFloat('dxy','_track',source)[0],
#    J2_dxy = makeJetUserFloat('dxy','_track',source)[1],
#    J1_dz = makeJetUserFloat('dz','_track',source)[0],
#    J2_dz = makeJetUserFloat('dz','_track',source)[1],
#    J1_pt_PV = makeJetUserFloat('pt_PV','',source)[0],  
#    J2_pt_PV = makeJetUserFloat('pt_PV','',source)[1],
#    J3_pt_PV = makeJetUserFloat('pt_PV','',source)[2],
#    J4_pt_PV = makeJetUserFloat('pt_PV','',source)[3],
#    J1_eta_PV = makeJetUserFloat('eta_PV','',source)[0],  
#    J2_eta_PV = makeJetUserFloat('eta_PV','',source)[1],
#    J3_eta_PV = makeJetUserFloat('eta_PV','',source)[2],
#    J4_eta_PV = makeJetUserFloat('eta_PV','',source)[3],
#    J1_phi_PV = makeJetUserFloat('phi_PV','',source)[0],  
#    J2_phi_PV = makeJetUserFloat('phi_PV','',source)[1],
#    J3_phi_PV = makeJetUserFloat('phi_PV','',source)[2],
#    J4_phi_PV = makeJetUserFloat('phi_PV','',source)[3],
#    J1_mass_PV = makeJetUserFloat('mass_PV','',source)[0], 
#    J2_mass_PV = makeJetUserFloat('mass_PV','',source)[1],
#    J3_mass_PV = makeJetUserFloat('mass_PV','',source)[2],
#    J4_mass_PV = makeJetUserFloat('mass_PV','',source)[3],
#    J1_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[0],
#    J2_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[1],
#    J3_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[2],
#    J4_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[3],
#    J1_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[0],
#    J2_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[1],
#    J3_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[2],
#    J4_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[3],
#    J1_electronMultiplicity = makeJetStringPar('electronMultiplicity','',source)[0],
#    J2_electronMultiplicity = makeJetStringPar('electronMultiplicity','',source)[1],
#    J1_photonMultiplicity = makeJetStringPar('photonMultiplicity','',source)[0],
#    J2_photonMultiplicity = makeJetStringPar('photonMultiplicity','',source)[1],
#    J1_jetCharge = makeJetString('jetCharge','',source)[0],
#    J2_jetCharge = makeJetString('jetCharge','',source)[1],
#    J3_jetCharge = makeJetString('jetCharge','',source)[2],
#    J4_jetCharge = makeJetString('jetCharge','',source)[3],
#    J1_mass = makeJetString('mass','',source)[0],
#    J2_mass = makeJetString('mass','',source)[1],
#    #J1_photonEnergy = makeJetString('photonEnergy','',source)[0],
#    #J2_photonEnergy = makeJetString('photonEnergy','',source)[1],
#    #J1_photonEnergyFraction = makeJetString('photonEnergyFraction','',source)[0],
#    #J2_photonEnergyFraction = makeJetString('photonEnergyFraction','',source)[1],
#    #J1_electronEnergy = makeJetString('electronEnergy','',source)[0],
#    #J2_electronEnergy = makeJetString('electronEnergy','',source)[1],
#    #J1_chargedEmEnergyFraction = makeJetString('chargedEmEnergyFraction','',source)[0],
#    #J2_chargedEmEnergyFraction = makeJetString('chargedEmEnergyFraction','',source)[1],
#    #J1_chargedMuEnergy = makeJetString('chargedMuEnergy','',source)[0],
#    #J2_chargedMuEnergy = makeJetString('chargedMuEnergy','',source)[1],
#    #J1_muonEnergyFraction = makeJetString('muonEnergyFraction','',source)[0],
#    #J2_muonEnergyFraction = makeJetString('muonEnergyFraction','',source)[1],
#    #J1_chargedHadronMultiplicity = makeJetStringPar('chargedHadronMultiplicity','',source)[0],
#    #J2_chargedHadronMultiplicity = makeJetStringPar('chargedHadronMultiplicity','',source)[1],


#def makeCollections(source = 'wCandsJets', sourceZ = 'diMuonsSorted',sourceE = 'weCandsJets', srcElectrons="smearedElectrons",srcMuons="smearedMuons"):
# commonCollections = cms.PSet(         
#
#    nrCbar = makeCollSize('cbarCands','nrCbar'), 
#    nrC = makeCollSize('cCands','nrC'), 
#    nrW = makeCollSize(source,'nrW'), 
#
## Few Electron Variables for MuEle control region
## BIG WARNING: This ID is super outdated. We need to go over the new EGamma ID and actualize it. WP80 is similar to the new "medium" one
## Z Variables
#    DiMuonMass = makeZColl("DiMuonMass","mass",sourceZ),
#    DiMuonPt = makeZColl("DiMuonPt","pt",sourceZ),
#    mu1_pt = makeZColl("mu1_pt","leg1.pt()",sourceZ),
#    mu2_pt = makeZColl("mu2_pt","leg2.pt()",sourceZ),
#    mu1_phi = makeZColl("mu1_phi","leg1.phi()",sourceZ),
#    mu2_phi = makeZColl("mu2_phi","leg2.phi()",sourceZ),
#    mu1_eta = makeZColl("mu1_eta","leg1.eta()",sourceZ),
#    mu2_eta = makeZColl("mu2_eta","leg2.eta()",sourceZ),
#    l1StdRelIso = makeZColl("l1StdRelIso",
#     "(leg1.isolationR03.sumPt+leg1.isolationR03.emEt+leg1.isolationR03.hadEt)/leg1.pt()",sourceZ),
#    l1PfIsoDB = makeZColl("l1PfIsoDB",
#     "(leg1.userIso(0)+max(leg1.photonIso()+leg1.neutralHadronIso()-0.5*leg1.puChargedHadronIso,0.0))/leg1.pt()",sourceZ),
#    l2StdRelIso = makeZColl("l2StdRelIso",
#     "(leg2.isolationR03.sumPt+leg2.isolationR03.emEt+leg2.isolationR03.hadEt)/leg2.pt()",sourceZ),
#    l2PfIsoDB = makeZColl("l2PfIsoDB",
#     "(leg2.userIso(0)+max(leg2.photonIso()+leg2.neutralHadronIso()-0.5*leg2.puChargedHadronIso,0.0))/leg2.pt()",sourceZ),
#
#    mJJ = makeMuNu("mJJ","mJJ",source,True),
#    mJ3J4 = makeMuNu("mJ3J4","mJJ2",source,True),
#    ptJJ = makeMuNu("ptJJ","ptJJ",source,True),
#
#    nrvtx = makeMuon("nrvtx",'userFloat("nvtx")',sourceMuons=srcMuons),
#    nrPU  = makeMuon("nrPU",'userFloat("nrPU")',sourceMuons=srcMuons),
#    preWeight = makeMuon("preWeight",'userFloat("preWeight")',sourceMuons=srcMuons),
#
#    Wpt = makeMuNu("Wpt","corPt()",source),
#
#    ipDXY = makeMuNu("ipDXY","lepton.userFloat('ipDXY')",source,True),
#    
#    metJJ = makeMuNu("metjj","metjj",source),
#    leptonjj = makeMuNu("leptonjj","leptonjj",source),
#    muNuDPhi = makeMuNu("muNuDPhi","dPhi",source),
#    muNuRecoil = makeMuNu("muNuRecoil","recoil().pt()",source),
#
#    dz = makeMuNu("dz",'abs(lepton.userFloat("dz"))',source,True),
#    ht = makeMuNu("ht","ht",source,True),
# )
# return commonCollections
