import FWCore.ParameterSet.Config as cms

from UWAnalysis.Configuration.tools.analysisToolsPT import TriggerPaths
jetRanks = [0,1,2,3,4,5,6,7]
jetNames = ['J1_','J2_','J3_','J4_','J5_','J6_','J7_','J8_']

def makeJetUserFloat(floatName,xn='',source = 'wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+floatName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src        = cms.InputTag(source),
        tag        = cms.string(nameTag),
        method     = cms.string('userFloat("'+floatName+'")'),
        rank       = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetUserInt(intName,xn='',source = 'wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+intName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src        = cms.InputTag(source),
        tag        = cms.string(nameTag),
        method     = cms.string('userInt("'+intName+'")'),
        rank       = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetStringPar(strName,xn='',source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+strName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src        = cms.InputTag(source),
        tag        = cms.string(nameTag),
        method     = cms.string(strName+'()'),
        rank       = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetString(strName,xn='',source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+strName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src        = cms.InputTag(source),
        tag        = cms.string(nameTag),
        method     = cms.string(strName),
        rank       = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetStringName(strName,mthName,xn='',source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+strName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src        = cms.InputTag(source),
        tag        = cms.string(nameTag),
        method     = cms.string(mthName),
        rank       = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetBTag(tagName,strName,source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+tagName
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src        = cms.InputTag(source),
        tag        = cms.string(nameTag),
        method     = cms.string('bDiscriminator("'+strName+'")'),
        rank       = cms.untracked.double(rank)
  ))
 return PSet_List

def makeNJets(pt,source='wCandsJets'):
  PSet = cms.PSet(
        pluginType  = cms.string("PATMuonNuPairJetCountFiller"),
        src         = cms.InputTag(source),
        tag         = cms.string("nJetsPt"+str(pt)),
        method      = cms.string('pt()>'+str(pt)+'&&abs(eta())<2.4'),
        leadingOnly = cms.untracked.bool(True)
  )
  return PSet

def makeCollSize(srcName,tagName):
  PSet = cms.PSet(
        pluginType = cms.string("CollectionSizeFiller"),
        src        = cms.InputTag(srcName),
        tag        = cms.string(tagName)
  )
  return PSet

def makeZColl(tagName,methodName,sourceZ='diMuonsSorted'):
  PSet = cms.PSet(
        pluginType  = cms.string("PATMuPairFiller"),
        src         = cms.InputTag(sourceZ),
        tag         = cms.string(tagName),
        method      = cms.string(methodName),
        leadingOnly = cms.untracked.bool(True)
  )
  return PSet

def makeBasicEle(tagName,methodName,sourceEle='selectedPatElectrons'):
  PSet = cms.PSet(
        pluginType  = cms.string("PATElectronFiller"),
        src         = cms.InputTag(sourceEle),
        tag         = cms.string(tagName),
        method      = cms.string(methodName),
        leadingOnly = cms.untracked.bool(True)
  )
  return PSet

def makeMuon(tagName,methodName,sourceMuon='selectedPatMuons',lo=True):
   PSet = cms.PSet(
         pluginType  = cms.string("PATMuonFiller"),
         src         = cms.InputTag(sourceMuon),
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

def makeJetSVInfo(source = 'wCandsJets'):
    jetSVInfo = cms.PSet(
 # Jet b Tagging
    J1_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[0],
    J2_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[1],
    J3_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[2],
    J4_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[3],
    J1_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[0],
    J2_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[1],
    J3_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[2],
    J4_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[3],
    J1_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[0],
    J2_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[1],
    J3_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[2],
    J4_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[3],
    J1_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[0],
    J2_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[1],
    J3_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[2],
    J4_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[3],
 # from RecoTools/plugins/bTagSFer.h 
   J1_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[0],
   J2_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[1],
   J3_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[2],
   J4_CSVM_SFb = makeJetUserFloat('CSVM_SFb','',source)[3],
   J1_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[0],
   J2_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[1],
   J3_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[2],
   J4_CSVM_errorb = makeJetUserFloat('CSVM_errorb','',source)[3],
   J1_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[0],
   J2_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[1],
   J3_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[2],
   J4_CSVM_SFl = makeJetUserFloat('CSVM_SFl','',source)[3],
   J1_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[0],
   J2_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[1],
   J3_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[2],
   J4_CSVM_SFl_down = makeJetUserFloat('CSVM_SFl_down','',source)[3],
   J1_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[0],
   J2_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[1],
   J3_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[2],
   J4_CSVM_SFl_up = makeJetUserFloat('CSVM_SFl_up','',source)[3],

   J1_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[0],
   J2_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[1],
   J3_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[2],
   J4_CSVT_SFb = makeJetUserFloat('CSVT_SFb','',source)[3],
   J1_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[0],
   J2_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[1],
   J3_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[2],
   J4_CSVT_errorb = makeJetUserFloat('CSVT_errorb','',source)[3],
   J1_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[0],
   J2_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[1],
   J3_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[2],
   J4_CSVT_SFl = makeJetUserFloat('CSVT_SFl','',source)[3],
   J1_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[0],
   J2_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[1],
   J3_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[2],
   J4_CSVT_SFl_down = makeJetUserFloat('CSVT_SFl_down','',source)[3],
   J1_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[0],
   J2_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[1],
   J3_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[2],
   J4_CSVT_SFl_up = makeJetUserFloat('CSVT_SFl_up','',source)[3],

# from RecoTools/plugins/PATSSVJetEmbedder.h 
    J1_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[0],
    J2_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[1],
    J3_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[2],
    J4_nTracks_SSV = makeJetUserFloat('nTracks_SSV','',source)[3],
    J1_pt_SSV = makeJetUserFloat('pt_SSV','',source)[0],  
    J2_pt_SSV = makeJetUserFloat('pt_SSV','',source)[1],
    J3_pt_SSV = makeJetUserFloat('pt_SSV','',source)[2],
    J4_pt_SSV = makeJetUserFloat('pt_SSV','',source)[3],
    J1_eta_SSV = makeJetUserFloat('eta_SSV','',source)[0],  
    J2_eta_SSV = makeJetUserFloat('eta_SSV','',source)[1],
    J3_eta_SSV = makeJetUserFloat('eta_SSV','',source)[2],
    J4_eta_SSV = makeJetUserFloat('eta_SSV','',source)[3],
    J1_phi_SSV = makeJetUserFloat('phi_SSV','',source)[0],  
    J2_phi_SSV = makeJetUserFloat('phi_SSV','',source)[1],
    J3_phi_SSV = makeJetUserFloat('phi_SSV','',source)[2],
    J4_phi_SSV = makeJetUserFloat('phi_SSV','',source)[3],
    J1_mass_SSV = makeJetUserFloat('mass_SSV','',source)[0], # formerly J1SVMassb
    J2_mass_SSV = makeJetUserFloat('mass_SSV','',source)[1],
    J3_mass_SSV = makeJetUserFloat('mass_SSV','',source)[2],
    J4_mass_SSV = makeJetUserFloat('mass_SSV','',source)[3],
    J1_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[0],  
    J2_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[1],
    J3_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[2],
    J4_mass_SSV_alt = makeJetUserFloat('mass_SSV_alt','',source)[3],

# from RecoTools/plugins/PATCSVVertex.cc
    J1_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[0],
    J2_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[1],
    J3_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[2],
    J4_pt_SV_weighted = makeJetUserFloat('pt_SV_weighted','',source)[3],
    J1_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[0],
    J2_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[1],
    J3_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[2],
    J4_pt_SV_unweighted = makeJetUserFloat('pt_SV_unweighted','',source)[3],
    J1_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[0],
    J2_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[1],
    J3_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[2],
    J4_mass_SV_weighted = makeJetUserFloat('mass_SV_weighted','',source)[3],
    J1_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[0],
    J2_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[1],
    J3_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[2],
    J4_mass_SV_unweighted = makeJetUserFloat('mass_SV_unweighted','',source)[3],
    J1_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[0],
    J2_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[1],
    J3_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[2],
    J4_normChi2_SV = makeJetUserFloat('normChi2_SV','',source)[3],
    J1_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[0],
    J2_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[1],
    J3_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[2],
    J4_nTracks_SV = makeJetUserFloat('nTracks_SV','',source)[3],
    J1_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[0],
    J2_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[1],
    J3_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[2],
    J4_mass_SV_corrected = makeJetUserFloat('mass_SV_corrected','',source)[3],
    )
    return jetSVInfo


def makeJetIDInfo(source = 'wCandsJets'):
   jetIDInfo = cms.PSet( 
    
     # variables going in to Jet ID  https://twiki.cern.ch/twiki/bin/viewauth/CMS/JetID#Documentation
    #J1_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[0],
    #J1_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[0],
    #J1_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[0],
    #J1_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[0],
    #J1_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[0],
    #J1_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[0],
    #J1_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[0],
    #J2_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[1],
    #J2_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[1],
    #J2_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[1],
    #J2_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[1],
    #J2_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[1],
    #J2_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[1],
    #J2_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[1],
    #J3_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[2],
    #J3_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[2],
    #J3_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[2],
    #J3_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[2],
    #J3_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[2],
    #J3_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[2],
    #J3_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[2],
    #J4_jetID_neutHadEnFr = makeJetStringName("jetID_neutHadEnFr","neutralHadronEnergyFraction()",xn='',source='wCandsJets')[3],
    #J4_jetID_neutEmEnFr  = makeJetStringName("jetID_neutEmEnFr","neutralEmEnergyFraction()",xn='',source='wCandsJets')[3],
    #J4_jetID_nrPFConstit = makeJetStringName("jetID_nrPFConstit","getPFConstituents().size()",xn='',source='wCandsJets')[3],
    #J4_jetID_chHadEnFr   = makeJetStringName("jetID_chHadEnFr","chargedHadronEnergyFraction()",xn='',source='wCandsJets')[3],
    #J4_jetID_chHadMult   = makeJetStringName("jetID_chHadMult","chargedHadronMultiplicity()",xn='',source='wCandsJets')[3],
    #J4_jetID_chMult      = makeJetStringName("jetID_chMult","chargedMultiplicity()",xn='',source='wCandsJets')[3],
    #J4_jetID_chEmEnFr    = makeJetStringName("jetID_chEmEnFr","chargedEmEnergyFraction()",xn='',source='wCandsJets')[3],

    # Jet ID and Pu ID
    J1_idTightJet = makeJetUserFloat('idTight','Jet',source)[0], 
    J2_idTightJet = makeJetUserFloat('idTight','Jet',source)[1], 
    J3_idTightJet = makeJetUserFloat('idTight','Jet',source)[2], 
    J4_idTightJet = makeJetUserFloat('idTight','Jet',source)[3], 
    J1_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[0], 
    J2_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[1], 
    J3_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[2], 
    J4_idLooseJet = makeJetUserFloat('idLoose','Jet',source)[3], 
    J1_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[0], 
    J2_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[1], 
    J3_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[2], 
    J4_fullIdTightPu = makeJetUserInt('fullIdTight','Pu',source)[3], 
    J1_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[0], 
    J2_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[1], 
    J3_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[2], 
    J4_fullIdLoosePu = makeJetUserInt('fullIdLoose','Pu',source)[3], 
    #J1_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[0], 
    #J2_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[1], 
    #J3_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[2], 
    #J4_fullDiscriminantPu = makeJetUserFloat('fullDiscriminant','Pu',source)[3], 
    #J1_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[0], 
    #J2_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[1], 
    #J3_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[2], 
    #J4_philv1DiscriminantPu = makeJetUserFloat('philv1Discriminant','Pu',source)[3], 
    #J1_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[0], 
    #J2_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[1], 
    #J3_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[2], 
    #J4_simpleDiscriminantPu = makeJetUserFloat('simpleDiscriminant','Pu',source)[3], 
    J1_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[0],
    J2_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[1],
    J3_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[2],
    J4_idBetaPu = makeJetUserFloat('idBeta','Pu',source)[3],
    #J1_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[0],
    #J2_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[1],
    #J3_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[2],
    #J4_idBetaClassicPu = makeJetUserFloat('idBetaClassic','Pu',source)[3],
    J1_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[0],
    J2_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[1],
    J3_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[2],
    J4_idBetaStarPu = makeJetUserFloat('idBetaStar','Pu',source)[3],
    J1_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[0],
    J2_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[1],
    J3_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[2],
    J4_idBetaStarClassicPu = makeJetUserFloat('idBetaStarClassic','Pu',source)[3],
    J1_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[0],
    J2_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[1],
    J3_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[2],
    J4_idBetaStarClassicModPu = makeJetUserFloat('idBetaStarClassicMod','Pu',source)[3],
    J1_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[0],
    J2_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[1],
    J3_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[2],
    J4_id_nTrackPu = makeJetUserFloat('id_nTrack','Pu',source)[3],
    #J1_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[0],
    #J2_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[1],
    #J3_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[2],
    #J4_idClosestDzPu = makeJetUserFloat('idClosestDz','Pu',source)[3],
    #J1_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[0],
    #J2_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[1],
    #J3_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[2],
    #J4_idClosestDxyPu = makeJetUserFloat('idClosestDxy','Pu',source)[3],
   )
   return jetIDInfo

def makeJetCorrectionInfo():
    # Jets at Various Levels of Correction from RecoTools/plugins/PATJetOverloader.h
   jetCorrectionInfo = cms.PSet(
    J1_pt_L1 = makeJetUserFloat('pt_L1')[0],
    J1_eta_L1 = makeJetUserFloat('eta_L1')[0],
    J1_phi_L1 = makeJetUserFloat('phi_L1')[0],
    J1_pt_L2 = makeJetUserFloat('pt_L2')[0],
    J1_eta_L2 = makeJetUserFloat('eta_L2')[0],
    J1_phi_L2 = makeJetUserFloat('phi_L2')[0],
    J1_pt_L3 = makeJetUserFloat('pt_L3')[0],
    J1_eta_L3 = makeJetUserFloat('eta_L3')[0],
    J1_phi_L3 = makeJetUserFloat('phi_L3')[0],
    J1_pt_L23 = makeJetUserFloat('pt_L23')[0],
    J2_pt_L1 = makeJetUserFloat('pt_L1')[1],
    J2_eta_L1 = makeJetUserFloat('eta_L1')[1],
    J2_phi_L1 = makeJetUserFloat('phi_L1')[1],
    J2_pt_L2 = makeJetUserFloat('pt_L2')[1],
    J2_eta_L2 = makeJetUserFloat('eta_L2')[1],
    J2_phi_L2 = makeJetUserFloat('phi_L2')[1],
    J2_pt_L3 = makeJetUserFloat('pt_L3')[1],
    J2_eta_L3 = makeJetUserFloat('eta_L3')[1],
    J2_phi_L3 = makeJetUserFloat('phi_L3')[1],
    J2_pt_L23 = makeJetUserFloat('pt_L23')[1],
    J3_pt_L1 = makeJetUserFloat('pt_L1')[2],
    J3_eta_L1 = makeJetUserFloat('eta_L1')[2],
    J3_phi_L1 = makeJetUserFloat('phi_L1')[2],
    J3_pt_L2 = makeJetUserFloat('pt_L2')[2],
    J3_eta_L2 = makeJetUserFloat('eta_L2')[2],
    J3_phi_L2 = makeJetUserFloat('phi_L2')[2],
    J3_pt_L3 = makeJetUserFloat('pt_L3')[2],
    J3_eta_L3 = makeJetUserFloat('eta_L3')[2],
    J3_phi_L3 = makeJetUserFloat('phi_L3')[2],
    J3_pt_L23 = makeJetUserFloat('pt_L23')[2],
    J4_pt_L1 = makeJetUserFloat('pt_L1')[3],
    J4_eta_L1 = makeJetUserFloat('eta_L1')[3],
    J4_phi_L1 = makeJetUserFloat('phi_L1')[3],
    J4_pt_L2 = makeJetUserFloat('pt_L2')[3],
    J4_eta_L2 = makeJetUserFloat('eta_L2')[3],
    J4_phi_L2 = makeJetUserFloat('phi_L2')[3],
    J4_pt_L3 = makeJetUserFloat('pt_L3')[3],
    J4_eta_L3 = makeJetUserFloat('eta_L3')[3],
    J4_phi_L3 = makeJetUserFloat('phi_L3')[3],
    J4_pt_L23 = makeJetUserFloat('pt_L23')[3],
   )
   return jetCorrectionInfo


def makeCollections(source = 'wCandsJets', sourceZ = 'diMuonsSorted',sourceE = 'weCandsJets', sourceEle="selectedPatElectrons"):
 commonCollections = cms.PSet(         
    #electronPt = makeMuNu("electronPt","lepton.pt()",sourceE),
    PVs = cms.PSet(
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

    J1_flightDistance = makeJetUserFloat('flightDistance','',source)[0],
    J2_flightDistance = makeJetUserFloat('flightDistance','',source)[1],
    J1_errorFlightDistance = makeJetUserFloat('errorFlightDistance','',source)[0],
    J2_errorFlightDistance = makeJetUserFloat('errorFlightDistance','',source)[1],
    J1_DR = makeJetUserFloat('DR','',source)[0],
    J2_DR = makeJetUserFloat('DR','',source)[1],
    J1_ptRMS = makeJetUserFloat('ptRMS','',source)[0],
    J2_ptRMS = makeJetUserFloat('ptRMS','',source)[1],
    J1_dxy = makeJetUserFloat('dxy','_track',source)[0],
    J2_dxy = makeJetUserFloat('dxy','_track',source)[1],
    J1_dz = makeJetUserFloat('dz','_track',source)[0],
    J2_dz = makeJetUserFloat('dz','_track',source)[1],
    J1_pt_PV = makeJetUserFloat('pt_PV','',source)[0],  
    J2_pt_PV = makeJetUserFloat('pt_PV','',source)[1],
    J3_pt_PV = makeJetUserFloat('pt_PV','',source)[2],
    J4_pt_PV = makeJetUserFloat('pt_PV','',source)[3],
    J1_eta_PV = makeJetUserFloat('eta_PV','',source)[0],  
    J2_eta_PV = makeJetUserFloat('eta_PV','',source)[1],
    J3_eta_PV = makeJetUserFloat('eta_PV','',source)[2],
    J4_eta_PV = makeJetUserFloat('eta_PV','',source)[3],
    J1_phi_PV = makeJetUserFloat('phi_PV','',source)[0],  
    J2_phi_PV = makeJetUserFloat('phi_PV','',source)[1],
    J3_phi_PV = makeJetUserFloat('phi_PV','',source)[2],
    J4_phi_PV = makeJetUserFloat('phi_PV','',source)[3],
    J1_mass_PV = makeJetUserFloat('mass_PV','',source)[0], 
    J2_mass_PV = makeJetUserFloat('mass_PV','',source)[1],
    J3_mass_PV = makeJetUserFloat('mass_PV','',source)[2],
    J4_mass_PV = makeJetUserFloat('mass_PV','',source)[3],
    J1_partonFlavour = makeJetStringPar('partonFlavour','',source)[0],
    J2_partonFlavour = makeJetStringPar('partonFlavour','',source)[1],
    J3_partonFlavour = makeJetStringPar('partonFlavour','',source)[2],
    J4_partonFlavour = makeJetStringPar('partonFlavour','',source)[3],
    #J1_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[0],
    #J2_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[1],
    #J1_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[0],
    #J2_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[1],
    #J1_electronMultiplicity = makeJetStringPar('electronMultiplicity','',source)[0],
    #J2_electronMultiplicity = makeJetStringPar('electronMultiplicity','',source)[1],
    #J1_photonMultiplicity = makeJetStringPar('photonMultiplicity','',source)[0],
    #J2_photonMultiplicity = makeJetStringPar('photonMultiplicity','',source)[1],
    J1_jetCharge = makeJetString('jetCharge','',source)[0],
    J2_jetCharge = makeJetString('jetCharge','',source)[1],
    J1_mass = makeJetString('mass','',source)[0],
    J2_mass = makeJetString('mass','',source)[1],
    #J1_photonEnergy = makeJetString('photonEnergy','',source)[0],
    #J2_photonEnergy = makeJetString('photonEnergy','',source)[1],
    #J1_photonEnergyFraction = makeJetString('photonEnergyFraction','',source)[0],
    #J2_photonEnergyFraction = makeJetString('photonEnergyFraction','',source)[1],
    #J1_electronEnergy = makeJetString('electronEnergy','',source)[0],
    #J2_electronEnergy = makeJetString('electronEnergy','',source)[1],
    #J1_chargedEmEnergyFraction = makeJetString('chargedEmEnergyFraction','',source)[0],
    #J2_chargedEmEnergyFraction = makeJetString('chargedEmEnergyFraction','',source)[1],
    #J1_chargedMuEnergy = makeJetString('chargedMuEnergy','',source)[0],
    #J2_chargedMuEnergy = makeJetString('chargedMuEnergy','',source)[1],
    #J1_muonEnergyFraction = makeJetString('muonEnergyFraction','',source)[0],
    #J2_muonEnergyFraction = makeJetString('muonEnergyFraction','',source)[1],
    #J1_chargedHadronMultiplicity = makeJetStringPar('chargedHadronMultiplicity','',source)[0],
    #J2_chargedHadronMultiplicity = makeJetStringPar('chargedHadronMultiplicity','',source)[1],
# Jet Kinematic Variables
    J1_pt = makeJetStringPar('pt','',source)[0], # formerly highestJetPt
    J2_pt = makeJetStringPar('pt','',source)[1],
    J3_pt = makeJetStringPar('pt','',source)[2],
    J4_pt = makeJetStringPar('pt','',source)[3],
    J5_pt = makeJetStringPar('pt','',source)[4], # formerly highestJetPt
    J6_pt = makeJetStringPar('pt','',source)[5],
    J7_pt = makeJetStringPar('pt','',source)[6],
    J8_pt = makeJetStringPar('pt','',source)[7],
    J1_phi = makeJetStringPar('phi','',source)[0],
    J2_phi = makeJetStringPar('phi','',source)[1],
    J3_phi = makeJetStringPar('phi','',source)[2],
    J4_phi = makeJetStringPar('phi','',source)[3],
    J5_phi = makeJetStringPar('phi','',source)[4],
    J6_phi = makeJetStringPar('phi','',source)[5],
    J7_phi = makeJetStringPar('phi','',source)[6],
    J8_phi = makeJetStringPar('phi','',source)[7],
    J1_eta = makeJetStringPar('eta','',source)[0],
    J2_eta = makeJetStringPar('eta','',source)[1],
    J3_eta = makeJetStringPar('eta','',source)[2],
    J4_eta = makeJetStringPar('eta','',source)[3],
    J5_eta = makeJetStringPar('eta','',source)[4],
    J6_eta = makeJetStringPar('eta','',source)[5],
    J7_eta = makeJetStringPar('eta','',source)[6],
    J8_eta = makeJetStringPar('eta','',source)[7],

    nJetsPt20 = makeNJets(20,source),
    nJetsPt25 = makeNJets(25,source),
    nJetsPt30 = makeNJets(30,source),
    nJetsPt35 = makeNJets(35,source),
    nJetsPt40 = makeNJets(40,source),

    nJets24to5 = makeMuNu("nJets24to5","nJets24to5",source),
    nJets24Pt20 = makeMuNu("nJets24Pt20","nJets24Pt20",source),
    nJets24Pt25 = makeMuNu("nJets24Pt25","nJets24Pt25",source),
    nJets24Pt30 = makeMuNu("nJets24Pt30","nJets24Pt30",source),

    nrCbar = makeCollSize('cbarCands','nrCbar'), 
    nrC = makeCollSize('cCands','nrC'), 
    nrW = makeCollSize(source,'nrW'), 

# Few Electron Variables for MuEle control region
# BIG WARNING: This ID is super outdated. We need to go over the new EGamma ID and actualize it. WP80 is similar to the new "medium" one
    ptEle = makeBasicEle("ele_pt","pt",sourceEle),
    phiEle = makeBasicEle("ele_phi","phi",sourceEle),
    etaEle = makeBasicEle("ele_eta","eta",sourceEle),
    wp80Ele = makeBasicEle("ele_wp80","userFloat('wp80')",sourceEle),
    chargeEle = makeBasicEle("ele_charge","charge",sourceEle),
    isoEleDB = makeBasicEle("isoEleDB","(userIso(0)+max(userIso(1)+neutralHadronIso()-0.5*userIso(2),0.0))/pt",sourceEle),

# Z Variables
    DiMuonMass = makeZColl("DiMuonMass","mass",sourceZ),
    DiMuonPt = makeZColl("DiMuonPt","pt",sourceZ),
    mu1_pt = makeZColl("mu1_pt","leg1.pt()",sourceZ),
    mu2_pt = makeZColl("mu2_pt","leg2.pt()",sourceZ),
    mu1_phi = makeZColl("mu1_phi","leg1.phi()",sourceZ),
    mu2_phi = makeZColl("mu2_phi","leg2.phi()",sourceZ),
    mu1_eta = makeZColl("mu1_eta","leg1.eta()",sourceZ),
    mu2_eta = makeZColl("mu2_eta","leg2.eta()",sourceZ),
    l1StdRelIso = makeZColl("l1StdRelIso",
     "(leg1.isolationR03.sumPt+leg1.isolationR03.emEt+leg1.isolationR03.hadEt)/leg1.pt()",sourceZ),
    l1PfIsoDB = makeZColl("l1PfIsoDB",
     "(leg1.userIso(0)+max(leg1.photonIso()+leg1.neutralHadronIso()-0.5*leg1.puChargedHadronIso,0.0))/leg1.pt()",sourceZ),
    l2StdRelIso = makeZColl("l2StdRelIso",
     "(leg2.isolationR03.sumPt+leg2.isolationR03.emEt+leg2.isolationR03.hadEt)/leg2.pt()",sourceZ),
    l2PfIsoDB = makeZColl("l2PfIsoDB",
     "(leg2.userIso(0)+max(leg2.photonIso()+leg2.neutralHadronIso()-0.5*leg2.puChargedHadronIso,0.0))/leg2.pt()",sourceZ),

    mJJ = makeMuNu("mJJ","mJJ",source,True),
    mJ3J4 = makeMuNu("mJ3J4","mJJ2",source,True),
    ptJJ = makeMuNu("ptJJ","ptJJ",source,True),

    nrvtx = makeMuon("nrvtx",'userFloat("nvtx")',sourceMuon='selectedPatMuons'),
    nrPU  = makeMuon("nrPU",'userFloat("nrPU")',sourceMuon='selectedPatMuons'),
    preWeight = makeMuon("preWeight",'userFloat("preWeight")',sourceMuon='selectedPatMuons'),

    #muon_sel_pt          = makeMuon("muon_sel_pt","pt",sourceMuon='selectedPatMuons'),
    #muon_sel_eta         = makeMuon("muon_sel_eta","eta",sourceMuon='selectedPatMuons'),
    #muon_sel_phi         = makeMuon("muon_sel_phi","phi",sourceMuon='selectedPatMuons'),
    #muon_sel_charge      = makeMuon("muon_sel_charge","charge",sourceMuon='selectedPatMuons'),
    #muon_sel_iso         = makeMuon("muon_sel_iso","(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt",sourceMuon='selectedPatMuons'),
    #muon_sel_pt_vec      = makeMuon("muon_sel_pt_vec","pt",sourceMuon='selectedPatMuons',lo=False),
    #muon_sel_eta_vec     = makeMuon("muon_sel_eta_vec","eta",sourceMuon='selectedPatMuons',lo=False),
    #muon_sel_phi_vec     = makeMuon("muon_sel_phi_vec","phi",sourceMuon='selectedPatMuons',lo=False),
    #muon_sel_charge_vec  = makeMuon("muon_sel_charge_vec","charge",sourceMuon='selectedPatMuons',lo=False),
    #muon_sel_iso_vec     = makeMuon("muon_sel_iso_vec","(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt",sourceMuon='selectedPatMuons',lo=False),

    #muon_loose_pt          = makeMuon("muon_loose_pt","pt",sourceMuon='QCDvetoPatMuons'),
    #muon_loose_eta         = makeMuon("muon_loose_eta","eta",sourceMuon='QCDvetoPatMuons'),
    #muon_loose_phi         = makeMuon("muon_loose_phi","phi",sourceMuon='QCDvetoPatMuons'),
    #muon_loose_charge      = makeMuon("muon_loose_charge","charge",sourceMuon='QCDvetoPatMuons'),
    #muon_loose_iso         = makeMuon("muon_loose_iso","(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt",sourceMuon='QCDvetoPatMuons'),
    #muon_loose_pt_vec      = makeMuon("muon_loose_pt_vec","pt",sourceMuon='QCDvetoPatMuons',lo=False),
    #muon_loose_eta_vec     = makeMuon("muon_loose_eta_vec","eta",sourceMuon='QCDvetoPatMuons',lo=False),
    #muon_loose_phi_vec     = makeMuon("muon_loose_phi_vec","phi",sourceMuon='QCDvetoPatMuons',lo=False),
    #muon_loose_charge_vec  = makeMuon("muon_loose_charge_vec","charge",sourceMuon='QCDvetoPatMuons',lo=False),
    #muon_loose_iso_vec     = makeMuon("muon_loose_iso_vec","(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt",sourceMuon='QCDvetoPatMuons',lo=False),

    #muon_loose_withIso_pt          = makeMuon("muon_loose_withIso_pt","pt",sourceMuon='preselectedPatMuons'),
    #muon_loose_withIso_eta         = makeMuon("muon_loose_withIso_eta","eta",sourceMuon='preselectedPatMuons'),
    #muon_loose_withIso_phi         = makeMuon("muon_loose_withIso_phi","phi",sourceMuon='preselectedPatMuons'),
    #muon_loose_withIso_charge      = makeMuon("muon_loose_withIso_charge","charge",sourceMuon='preselectedPatMuons'),
    #muon_loose_withIso_iso         = makeMuon("muon_loose_withIso_iso","(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt",sourceMuon='preselectedPatMuons'),
    #muon_loose_withIso_pt_vec      = makeMuon("muon_loose_withIso_pt_vec","pt",sourceMuon='preselectedPatMuons',lo=False),
    #muon_loose_withIso_eta_vec     = makeMuon("muon_loose_withIso_eta_vec","eta",sourceMuon='preselectedPatMuons',lo=False),
    #muon_loose_withIso_phi_vec     = makeMuon("muon_loose_withIso_phi_vec","phi",sourceMuon='preselectedPatMuons',lo=False),
    #muon_loose_withIso_charge_vec  = makeMuon("muon_loose_withIso_charge_vec","charge",sourceMuon='preselectedPatMuons',lo=False),
    #muon_loose_withIso_iso_vec     = makeMuon("muon_loose_withIso_iso_vec","(pfIsolationR04().sumChargedHadronPt + max((pfIsolationR04().sumNeutralHadronEt + pfIsolationR04().sumPhotonEt - 0.5*pfIsolationR04().sumPUPt),0.0))/pt",sourceMuon='preselectedPatMuons',lo=False),

    nrMu = makeCollSize('selectedPatMuons','nrMu'),
    nrEle = makeCollSize('selectedPatElectrons','nrEle'),
    nrMuLoose = makeCollSize('preselectedPatMuons','nrMuLoose'),
    nrEleLoose = makeCollSize('preselectedPatElectrons','nrEleLoose'),
    nrMuQCD = makeCollSize('QCDvetoPatMuons','nrMuQCD'),

    muon_pt = makeMuNu("muon_pt","lepton().pt",source),
    muon_eta = makeMuNu("muon_eta","lepton.eta",source),
    muon_phi = makeMuNu("muon_phi","lepton.phi",source),
    muon_charge = makeMuNu("muon_charge","lepton.charge()",source),
    muon_pt_vec = makeMuNu("muon_pt_vec","lepton().pt",source,lo=False),
    muon_eta_vec  = makeMuNu("muon_eta_vec","lepton.eta",source,lo=False),
    muon_phi_vec  = makeMuNu("muon_phi_vec","lepton.phi",source,lo=False),
    muon_charge_vec  = makeMuNu("muon_charge_vec","lepton.charge()",source,lo=False),
    Wpt = makeMuNu("Wpt","corPt()",source),

    #muNuRelPFIso = makeMuNu("muNuRelPFIso",
    # "(lepton.chargedHadronIso()+lepton.photonIso()+lepton.neutralHadronIso())/lepton.pt()",source,lo=True),
    #muNuRelPFIso_vec = makeMuNu("muNuRelPFIso",
    # "(lepton.chargedHadronIso()+lepton.photonIso()+lepton.neutralHadronIso())/lepton.pt()",source,lo=False),

    muNuRelPFIsoDB_A = makeMuNu("muNuRelPFIsoDB_A",
      "(lepton.pfIsolationR04().sumChargedHadronPt + max((lepton.pfIsolationR04().sumNeutralHadronEt + lepton.pfIsolationR04().sumPhotonEt - 0.5*lepton.pfIsolationR04().sumPUPt),0.0))/lepton.pt",
      source,lo=True),
    muNuRelPFIsoDB_A_vec = makeMuNu("muNuRelPFIsoDB_A_vec",
      "(lepton.pfIsolationR04().sumChargedHadronPt + max((lepton.pfIsolationR04().sumNeutralHadronEt + lepton.pfIsolationR04().sumPhotonEt - 0.5*lepton.pfIsolationR04().sumPUPt),0.0))/lepton.pt",
      source,lo=False),

    #muNuRelPFIsoDB_B = makeMuNu("muNuRelPFIsoDB_B",
    # "(lepton.userIso(0)+max(lepton.photonIso()+lepton.neutralHadronIso()-0.5*lepton.puChargedHadronIso,0.0))/lepton.pt()",
    # source,lo=True),
    #muNuRelPFIsoDB_B_vec = makeMuNu("muNuRelPFIsoDB_B_vec",
    # "(lepton.userIso(0)+max(lepton.photonIso()+lepton.neutralHadronIso()-0.5*lepton.puChargedHadronIso,0.0))/lepton.pt()",
    # source,lo=False),
    #PFIsoRho = makeMuNu("PFIsoRho","lepton.userFloat('rho')",source),
    #muNuRelStdIso03 = makeMuNu("muNuRelStdIso03",
    # "(lepton.isolationR03.sumPt+lepton.isolationR03.emEt+lepton.isolationR03.hadEt)/lepton.pt()",source),


    ipDXY = makeMuNu("ipDXY","lepton.userFloat('ipDXY')",source,True),
    met_pt = makeMuNu("met_pt","met().pt",source,True),
    met_phi = makeMuNu("met_phi","met().phi",source,True),
    mt = makeMuNu("mt","mt",source),
    
    metJJ = makeMuNu("metjj","metjj",source),
    leptonjj = makeMuNu("leptonjj","leptonjj",source),
    muNuDPhi = makeMuNu("muNuDPhi","dPhi",source),
    muNuRecoil = makeMuNu("muNuRecoil","recoil().pt()",source),

    dz = makeMuNu("dz",'abs(lepton.userFloat("dz"))',source,True),
    ht = makeMuNu("ht","ht",source,True),
 )
 return commonCollections

def addMuNuEventTreePtData(process,name,source = 'wCandsJets',sourceZ = 'diMuonsSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
      makeCollections(source,sourceZ),
      makeJetIDInfo(source),
      #makeJetCorrectionInfo(),
      makeJetSVInfo(source),
      coreCollections = cms.VInputTag( cms.InputTag(source) ),
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
      J1_eta_L23 = makeJetUserFloat('eta_L23')[0],
      J1_phi_L23 = makeJetUserFloat('phi_L23')[0],
      J2_eta_L23 = makeJetUserFloat('eta_L23')[1],
      J2_phi_L23 = makeJetUserFloat('phi_L23')[1],
      J3_eta_L23 = makeJetUserFloat('eta_L23')[2],
      J3_phi_L23 = makeJetUserFloat('phi_L23')[2],
      J4_eta_L23 = makeJetUserFloat('eta_L23')[3],
      J4_phi_L23 = makeJetUserFloat('phi_L23')[3]
   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)

def addMuNuEventTreePtMC(process,name,source = 'wCandsJets',sourceZ = 'diMuonsSorted',lhep="externalLHEProducer"):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
      makeCollections(source,sourceZ),
      makeJetIDInfo(source),
      #makeJetCorrectionInfo(),
      makeJetSVInfo(source),
      coreCollections = cms.VInputTag(
           cms.InputTag(source)
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
      bHadronsPt = makeSimBHad("bhadrons","bHadronsPt","pt"),
      bHadronsEta = makeSimBHad("bhadrons","bHadronsEta","eta"),
      bHadronsPhi = makeSimBHad("bhadrons","bHadronsPhi","phi"),
  
      ## Jet pT Reco + Gen from RecoTools/plugins/PATJetSmearer.h
      #J1_pt_gen = makeJetUserFloat('pt_gen')[0],
      #J1_pt_gen_two = makeJetUserFloat('pt_gen_two')[0],
      #J1_pt_uncorr = makeJetUserFloat('pt_uncorr','',source)[0], 
      #J1_pt_smearedUp = makeJetUserFloat('pt_smearedUp','',source)[0], 
      #J1_pt_smearedDown = makeJetUserFloat('pt_smearedDown','',source)[0], 
      #J2_pt_gen = makeJetUserFloat('pt_gen')[1],
      #J2_pt_gen_two = makeJetUserFloat('pt_gen_two')[1],
      #J2_pt_uncorr = makeJetUserFloat('pt_uncorr','',source)[1], 
      #J2_pt_smearedUp = makeJetUserFloat('pt_smearedUp','',source)[1], 
      #J2_pt_smearedDown = makeJetUserFloat('pt_smearedDown','',source)[1], 
      #J3_pt_gen = makeJetUserFloat('pt_gen')[2],
      #J3_pt_gen_two = makeJetUserFloat('pt_gen_two')[2],
      #J3_pt_uncorr = makeJetUserFloat('pt_uncorr','',source)[2], 
      #J3_pt_smearedUp = makeJetUserFloat('pt_smearedUp','',source)[2], 
      #J3_pt_smearedDown = makeJetUserFloat('pt_smearedDown','',source)[2], 
      #J4_pt_gen = makeJetUserFloat('pt_gen')[3],
      #J4_pt_gen_two = makeJetUserFloat('pt_gen_two')[3],
      #J4_pt_uncorr = makeJetUserFloat('pt_uncorr','',source)[3], 
      #J4_pt_smearedUp = makeJetUserFloat('pt_smearedUp','',source)[3], 
      #J4_pt_smearedDown = makeJetUserFloat('pt_smearedDown','',source)[3], 

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
      nbHadrons = makeCollSize("bhadrons","nbHadrons"),
      genTs = makeCollSize("gentCands","genTs"),
      genTbars = makeCollSize("gentbarCands","genTbars"),
      genBs = makeCollSize("genbbCands","genBs"),
      genCs = makeCollSize("genccCands","genCs"),
      genDs = makeCollSize("genddCands","genDs"),
      genUs = makeCollSize("genuuCands","genUs"),
      genSs = makeCollSize("genSSCands","genSs"),
      genWs = makeCollSize("genWs","genWs"),
 
      EffWEIGHTCSVL = makeMuNu("EffWEIGHTCSVL","SFCSVL1",source,True),
      EffWEIGHTCSVL2 = makeMuNu("EffWEIGHTCSVL2","SFCSVL2",source,True),
      EffWEIGHTCSVM = makeMuNu("EffWEIGHTCSVM","SFCSVM1",source,True),
      EffWEIGHTCSVM2 = makeMuNu("EffWEIGHTCSVM2","SFCSVM2",source,True),
      EffWEIGHTCSVT = makeMuNu("EffWEIGHTCSVT","SFCSVT1",source,True),
      EffWEIGHTCSVT2 = makeMuNu("EffWEIGHTCSVT2","SFCSVT2",source,True),
      EffWEIGHTSSVHEM = makeMuNu("EffWEIGHTSSVHEM","SFSSVHE1",source,True),
      EffWEIGHTSSVHEM2 = makeMuNu("EffWEIGHTSSVHEM2","SFSSVHE2",source,True),
      weightEtaMuonIso = makeMuNu("weightEtaMuonIso","EffWEIGHTeta_IS",source,True),
      weightEtaMuonID = makeMuNu("weightEtaMuonID","EffWEIGHTeta_ID",source,True),
      weightEtaMuonTrig = makeMuNu("weightEtaMuonTrig","EffWEIGHTeta_TR",source,True),
   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)
