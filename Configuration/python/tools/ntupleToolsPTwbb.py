import FWCore.ParameterSet.Config as cms

from UWAnalysis.Configuration.tools.analysisToolsPT import TriggerPaths
jetRanks = [0,1,2,4]
jetNames = ['J1_','J2_','J3_','J4_']

def makeJetUserFloat(floatName,xn='',source = 'wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+floatName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src = cms.InputTag(source),
        tag = cms.string(nameTag),
        method = cms.string('userFloat("'+floatName+'")'),
        rank = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetStringPar(strName,xn='',source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+strName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src = cms.InputTag(source),
        tag = cms.string(nameTag),
        method = cms.string(strName+'()'),
        rank = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetString(strName,xn='',source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+strName+xn
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src = cms.InputTag(source),
        tag = cms.string(nameTag),
        method = cms.string(strName),
        rank = cms.untracked.double(rank)
  ))
 return PSet_List

def makeJetBTag(tagName,strName,source='wCandsJets'):
 PSet_List = []
 for rank,name in zip(jetRanks,jetNames):
  nameTag = name+tagName
  PSet_List.append(cms.PSet(
        pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
        src = cms.InputTag(source),
        tag = cms.string(nameTag),
        method = cms.string('bDiscriminator("'+strName+'")'),
        rank = cms.untracked.double(rank)
  ))
 return PSet_List

def makeNJets(pt,source='wCandsJets'):
  PSet = cms.PSet(
        pluginType = cms.string("PATMuonNuPairJetCountFiller"),
        src = cms.InputTag(source),
        tag = cms.string("nJetsPt"+str(pt)),
        method = cms.string('pt()>'+str(pt)+'&&abs(eta())<2.4'),
        leadingOnly=cms.untracked.bool(True)
  )
  return PSet

def makeCollSize(srcName,tagName):
  PSet = cms.PSet(
        pluginType = cms.string("CollectionSizeFiller"),
        src = cms.InputTag(srcName),
        tag = cms.string(tagName)
  )
  return PSet

def makeZColl(tagName,methodName,sourceZ='diMuonsSorted'):
  PSet = cms.PSet(
        pluginType = cms.string("PATMuPairFiller"),
        src = cms.InputTag(sourceZ),
        tag = cms.string(tagName),
        method = cms.string(methodName),
        leadingOnly=cms.untracked.bool(True)
  )
  return PSet

def makeMuNu(tagName,methodName,source='wCandsJets',lo=False):
  if lo:
   PSet = cms.PSet(
         pluginType = cms.string("PATMuonNuPairFiller"),
         src = cms.InputTag(source),
         tag = cms.string(tagName),
         method = cms.string(methodName),
         leadingOnly=cms.untracked.bool(True)
   )
  else:
   PSet = cms.PSet(
         pluginType = cms.string("PATMuonNuPairFiller"),
         src = cms.InputTag(source),
         tag = cms.string(tagName),
         method = cms.string(methodName),
   )
  return PSet

def makeSimBHad(srcName,tagName,methodName):
  PSet = cms.PSet(
        pluginType = cms.string("SimBHadronsFiller"),
        src = cms.InputTag(srcName),
        tag = cms.string(tagName),
        method = cms.string(methodName+"()"),
        leadingOnly=cms.untracked.bool(False)
  )
  return PSet

def makeIVFBs(tagName,methodName):
  PSet = cms.PSet(
        pluginType = cms.string("bCandidatesFiller"),
        src        = cms.InputTag('LCProducer','BCandFinalState'),
        tag        = cms.string(tagName),
        method     = cms.string(methodName+"()"),
        leadingOnly=cms.untracked.bool(False)
  )
  return PSet

def makeCollections(source = 'wCandsJets', sourceZ = 'diMuonsSorted',sourceE = 'weCandsJets'):
 commonCollections = cms.PSet(         
    electronPt = makeMuNu("electronPt","lepton.pt()",sourceE),
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

    J1_PUID_idTight = makeJetUserFloat('PUID_idTight','',source)[0], 
    J2_PUID_idTight = makeJetUserFloat('PUID_idTight','',source)[1], 
    J3_PUID_idTight = makeJetUserFloat('PUID_idTight','',source)[2], 
    J4_PUID_idTight = makeJetUserFloat('PUID_idTight','',source)[3], 
    J1_PUID_fullIdTight = makeJetUserFloat('PUID_fullIdTight','',source)[0], 
    J2_PUID_fullIdTight = makeJetUserFloat('PUID_fullIdTight','',source)[1], 
    J3_PUID_fullIdTight = makeJetUserFloat('PUID_fullIdTight','',source)[2], 
    J4_PUID_fullIdTight = makeJetUserFloat('PUID_fullIdTight','',source)[3], 
    J1_PUID_idLoose = makeJetUserFloat('PUID_idLoose','',source)[0], 
    J2_PUID_idLoose = makeJetUserFloat('PUID_idLoose','',source)[1], 
    J3_PUID_idLoose = makeJetUserFloat('PUID_idLoose','',source)[2], 
    J4_PUID_idLoose = makeJetUserFloat('PUID_idLoose','',source)[3], 
    J1_PUID_fullIdLoose = makeJetUserFloat('PUID_fullIdLoose','',source)[0], 
    J2_PUID_fullIdLoose = makeJetUserFloat('PUID_fullIdLoose','',source)[1], 
    J3_PUID_fullIdLoose = makeJetUserFloat('PUID_fullIdLoose','',source)[2], 
    J4_PUID_fullIdLoose = makeJetUserFloat('PUID_fullIdLoose','',source)[3], 
    J1_PUID_fullDiscriminant = makeJetUserFloat('PUID_fullDiscriminant','',source)[0], 
    J2_PUID_fullDiscriminant = makeJetUserFloat('PUID_fullDiscriminant','',source)[1], 
    J3_PUID_fullDiscriminant = makeJetUserFloat('PUID_fullDiscriminant','',source)[2], 
    J4_PUID_fullDiscriminant = makeJetUserFloat('PUID_fullDiscriminant','',source)[3], 
    J1_PUID_philv1Discriminant = makeJetUserFloat('PUID_philv1Discriminant','',source)[0], 
    J2_PUID_philv1Discriminant = makeJetUserFloat('PUID_philv1Discriminant','',source)[1], 
    J3_PUID_philv1Discriminant = makeJetUserFloat('PUID_philv1Discriminant','',source)[2], 
    J4_PUID_philv1Discriminant = makeJetUserFloat('PUID_philv1Discriminant','',source)[3], 
    J1_PUID_simpleDiscriminant = makeJetUserFloat('PUID_simpleDiscriminant','',source)[0], 
    J2_PUID_simpleDiscriminant = makeJetUserFloat('PUID_simpleDiscriminant','',source)[1], 
    J3_PUID_simpleDiscriminant = makeJetUserFloat('PUID_simpleDiscriminant','',source)[2], 
    J4_PUID_simpleDiscriminant = makeJetUserFloat('PUID_simpleDiscriminant','',source)[3], 
    J1_PUID_beta = makeJetUserFloat('PUID_beta','',source)[0],
    J2_PUID_beta = makeJetUserFloat('PUID_beta','',source)[1],
    J3_PUID_beta = makeJetUserFloat('PUID_beta','',source)[2],
    J4_PUID_beta = makeJetUserFloat('PUID_beta','',source)[3],
    J1_PUID_betaClassic = makeJetUserFloat('PUID_betaClassic','',source)[0],
    J2_PUID_betaClassic = makeJetUserFloat('PUID_betaClassic','',source)[1],
    J3_PUID_betaClassic = makeJetUserFloat('PUID_betaClassic','',source)[2],
    J4_PUID_betaClassic = makeJetUserFloat('PUID_betaClassic','',source)[3],
    J1_PUID_betaStar = makeJetUserFloat('PUID_betaStar','',source)[0],
    J2_PUID_betaStar = makeJetUserFloat('PUID_betaStar','',source)[1],
    J3_PUID_betaStar = makeJetUserFloat('PUID_betaStar','',source)[2],
    J4_PUID_betaStar = makeJetUserFloat('PUID_betaStar','',source)[3],
    J1_PUID_betaStarClassic = makeJetUserFloat('PUID_betaStarClassic','',source)[0],
    J2_PUID_betaStarClassic = makeJetUserFloat('PUID_betaStarClassic','',source)[1],
    J3_PUID_betaStarClassic = makeJetUserFloat('PUID_betaStarClassic','',source)[2],
    J4_PUID_betaStarClassic = makeJetUserFloat('PUID_betaStarClassic','',source)[3],
    J1_PUID_betaStarClassicMod = makeJetUserFloat('PUID_betaStarClassicMod','',source)[0],
    J2_PUID_betaStarClassicMod = makeJetUserFloat('PUID_betaStarClassicMod','',source)[1],
    J3_PUID_betaStarClassicMod = makeJetUserFloat('PUID_betaStarClassicMod','',source)[2],
    J4_PUID_betaStarClassicMod = makeJetUserFloat('PUID_betaStarClassicMod','',source)[3],
    J1_PUID_nTrack = makeJetUserFloat('PUID_nTrack','',source)[0],
    J2_PUID_nTrack = makeJetUserFloat('PUID_nTrack','',source)[1],
    J3_PUID_nTrack = makeJetUserFloat('PUID_nTrack','',source)[2],
    J4_PUID_nTrack = makeJetUserFloat('PUID_nTrack','',source)[3],
    J1_PUID_closestDz = makeJetUserFloat('PUID_closestDz','',source)[0],
    J2_PUID_closestDz = makeJetUserFloat('PUID_closestDz','',source)[1],
    J3_PUID_closestDz = makeJetUserFloat('PUID_closestDz','',source)[2],
    J4_PUID_closestDz = makeJetUserFloat('PUID_closestDz','',source)[3],
    J1_PUID_closestDxy = makeJetUserFloat('PUID_closestDxy','',source)[0],
    J2_PUID_closestDxy = makeJetUserFloat('PUID_closestDxy','',source)[1],
    J3_PUID_closestDxy = makeJetUserFloat('PUID_closestDxy','',source)[2],
    J4_PUID_closestDxy = makeJetUserFloat('PUID_closestDxy','',source)[3],

#    J1_SV_M = makeJetUserFloat('SV_M','',source)[0],
#    J2_SV_M = makeJetUserFloat('SV_M','',source)[1],
#    J3_SV_M = makeJetUserFloat('SV_M','',source)[2],
#    J4_SV_M = makeJetUserFloat('SV_M','',source)[3],
#    J1_SV_pt = makeJetUserFloat('SV_pt','',source)[0],
#    J2_SV_pt = makeJetUserFloat('SV_pt','',source)[1],
#    J3_SV_pt = makeJetUserFloat('SV_pt','',source)[2],
#    J4_SV_pt = makeJetUserFloat('SV_pt','',source)[3],
#    J1_SV_eta = makeJetUserFloat('SV_eta','',source)[0],
#    J2_SV_eta = makeJetUserFloat('SV_eta','',source)[1],
#    J3_SV_eta = makeJetUserFloat('SV_eta','',source)[2],
#    J4_SV_eta = makeJetUserFloat('SV_eta','',source)[3],
#    J1_SV_phi = makeJetUserFloat('SV_phi','',source)[0],
#    J2_SV_phi = makeJetUserFloat('SV_phi','',source)[1],
#    J3_SV_phi = makeJetUserFloat('SV_phi','',source)[2],
#    J4_SV_phi = makeJetUserFloat('SV_phi','',source)[3],
#    J1_Mu1Boost = makeJetUserFloat('Mu1Boost','',source)[0],
#    J2_Mu1Boost = makeJetUserFloat('Mu1Boost','',source)[1],
    J1_massBpmElecs = makeJetUserFloat('massBpmElecs','',source)[0],
    J2_massBpmElecs = makeJetUserFloat('massBpmElecs','',source)[1],
    J1_sec_massBpm = makeJetUserFloat('sec_massBpm','',source)[0],
    J2_sec_massBpm = makeJetUserFloat('sec_massBpm','',source)[1],
    J1_sec_massBpm_charge = makeJetUserFloat('sec_massBpm_charge','',source)[0],
    J2_sec_massBpm_charge = makeJetUserFloat('sec_massBpm_charge','',source)[1],
    J1_sec_massD0 = makeJetUserFloat('sec_massD0','',source)[0],
    J2_sec_massD0 = makeJetUserFloat('sec_massD0','',source)[1],
    J1_massD0 = makeJetUserFloat('massD0','',source)[0],
    J2_massD0 = makeJetUserFloat('massD0','',source)[1],
    J1_massBpm = makeJetUserFloat('massBpm','',source)[0],
    J2_massBpm = makeJetUserFloat('massBpm','',source)[1],
    J1_massBpm2 = makeJetUserFloat('massBpm2','',source)[0],
    J2_massBpm2 = makeJetUserFloat('massBpm2','',source)[1],
    J1_massDpm = makeJetUserFloat('massDpm','',source)[0],
    J2_massDpm = makeJetUserFloat('massDpm','',source)[1],
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
    J1_nTracksSSV = makeJetUserFloat('nTracksSSV','',source)[0],
    J2_nTracksSSV = makeJetUserFloat('nTracksSSV','',source)[1],
    J1_mass_SSV = makeJetUserFloat('mass_SSV','',source)[0], # formerly J1SVMassb
    J2_mass_SSV = makeJetUserFloat('mass_SSV','',source)[1],
    J3_mass_SSV = makeJetUserFloat('mass_SSV','',source)[2],
    J4_mass_SSV = makeJetUserFloat('mass_SSV','',source)[3],
    J1_partonFlavour = makeJetStringPar('partonFlavour','',source)[0],
    J2_partonFlavour = makeJetStringPar('partonFlavour','',source)[1],
    J1_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[0],
    J2_muonMultiplicity = makeJetStringPar('muonMultiplicity','',source)[1],
    J1_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[0],
    J2_chargedMultiplicity = makeJetStringPar('chargedMultiplicity','',source)[1],
    J1_electronMultiplicity = makeJetStringPar('electronMultiplicity','',source)[0],
    J2_electronMultiplicity = makeJetStringPar('electronMultiplicity','',source)[1],
    J1_photonMultiplicity = makeJetStringPar('photonMultiplicity','',source)[0],
    J2_photonMultiplicity = makeJetStringPar('photonMultiplicity','',source)[1],
    J1_jetCharge = makeJetString('jetCharge','',source)[0],
    J2_jetCharge = makeJetString('jetCharge','',source)[1],
    J1_mass = makeJetString('mass','',source)[0],
    J2_mass = makeJetString('mass','',source)[1],
    J1_photonEnergy = makeJetString('photonEnergy','',source)[0],
    J2_photonEnergy = makeJetString('photonEnergy','',source)[1],
    J1_photonEnergyFraction = makeJetString('photonEnergyFraction','',source)[0],
    J2_photonEnergyFraction = makeJetString('photonEnergyFraction','',source)[1],
    J1_electronEnergy = makeJetString('electronEnergy','',source)[0],
    J2_electronEnergy = makeJetString('electronEnergy','',source)[1],
    J1_chargedEmEnergyFraction = makeJetString('chargedEmEnergyFraction','',source)[0],
    J2_chargedEmEnergyFraction = makeJetString('chargedEmEnergyFraction','',source)[1],
    J1_chargedMuEnergy = makeJetString('chargedMuEnergy','',source)[0],
    J2_chargedMuEnergy = makeJetString('chargedMuEnergy','',source)[1],
    J1_muonEnergyFraction = makeJetString('muonEnergyFraction','',source)[0],
    J2_muonEnergyFraction = makeJetString('muonEnergyFraction','',source)[1],
    J1_chargedHadronMultiplicity = makeJetStringPar('chargedHadronMultiplicity','',source)[0],
    J2_chargedHadronMultiplicity = makeJetStringPar('chargedHadronMultiplicity','',source)[1],

    J1_pt = makeJetStringPar('pt','',source)[0], # formerly highestJetPt
    J2_pt = makeJetStringPar('pt','',source)[1],
    J3_pt = makeJetStringPar('pt','',source)[2],
    J4_pt = makeJetStringPar('pt','',source)[3],
    J1_phi = makeJetStringPar('phi','',source)[0],
    J2_phi = makeJetStringPar('phi','',source)[1],
    J3_phi = makeJetStringPar('phi','',source)[2],
    J4_phi = makeJetStringPar('phi','',source)[3],
    J1_eta = makeJetStringPar('eta','',source)[0],
    J2_eta = makeJetStringPar('eta','',source)[1],
    J3_eta = makeJetStringPar('eta','',source)[2],
    J4_eta = makeJetStringPar('eta','',source)[3],

    J1_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[0],
    J2_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[1],
    J3_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[2],
    J4_TCHEbtag = makeJetBTag('TCHEbtag','trackCountingHighEffBJetTags',source)[3],
    J1_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[0],
    J2_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[1],
    J3_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[2],
    J4_TCHPbtag = makeJetBTag('TCHPbtag','trackCountingHighPurBJetTags',source)[3],
#    J1_SSVHEbtag = makeJetBTag('SSVHEbtag','simpleSecondaryVertexHighEffBJetTags',source)[0],
#    J2_SSVHEbtag = makeJetBTag('SSVHEbtag','simpleSecondaryVertexHighEffBJetTags',source)[1],
#    J3_SSVHEbtag = makeJetBTag('SSVHEbtag','simpleSecondaryVertexHighEffBJetTags',source)[2],
#    J4_SSVHEbtag = makeJetBTag('SSVHEbtag','simpleSecondaryVertexHighEffBJetTags',source)[3],
    J1_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[0],
    J2_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[1],
    J3_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[2],
    J4_CSVbtag = makeJetBTag('CSVbtag','combinedSecondaryVertexBJetTags',source)[3],
    J1_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[0],
    J2_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[1],
    J3_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[2],
    J4_CSVMVAbtag = makeJetBTag('CSVMVAbtag','combinedSecondaryVertexMVABJetTags',source)[3],

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
    nrMu = makeCollSize('selectedPatMuons','nrMu'),
    nrEle = makeCollSize('selectedPatElectrons','nrEle'),

    DiMuonMass = makeZColl("DiMuonMass","mass",sourceZ),
    mu1_pt = makeZColl("mu1_pt","leg1.pt()",sourceZ),
    mu2_pt = makeZColl("mu2_pt","leg2.pt()",sourceZ),
    mu1_phi = makeZColl("mu1_phi","leg1.phi()",sourceZ),
    mu2_phi = makeZColl("mu2_phi","leg2.phi()",sourceZ),
    mu1_eta = makeZColl("mu1_pt","leg1.eta()",sourceZ),
    mu2_eta = makeZColl("mu2_pt","leg2.eta()",sourceZ),
    l1StdRelIso = makeZColl("l1StdRelIso",
     "(leg1.isolationR03.sumPt+leg1.isolationR03.emEt+leg1.isolationR03.hadEt)/leg1.pt()",sourceZ),
    l1PfIsoDB = makeZColl("l1StdRelIso",
     "(leg1.userIso(0)+max(leg1.photonIso()+leg1.neutralHadronIso()-0.5*leg1.puChargedHadronIso,0.0))/leg1.pt()",sourceZ),
    l2StdRelIso = makeZColl("l2StdRelIso",
     "(leg2.isolationR03.sumPt+leg2.isolationR03.emEt+leg2.isolationR03.hadEt)/leg2.pt()",sourceZ),
    l2PfIsoDB = makeZColl("l2StdRelIso",
     "(leg2.userIso(0)+max(leg2.photonIso()+leg2.neutralHadronIso()-0.5*leg2.puChargedHadronIso,0.0))/leg2.pt()",sourceZ),

    mJJ = makeMuNu("mJJ","mJJ",source,True),
    mJ3J4 = makeMuNu("mJ3J4","mJJ2",source,True),
    ptJJ = makeMuNu("ptJJ","ptJJ",source,True),
    muonPt = makeMuNu("muonPt","lepton().pt",source),
    muonEta = makeMuNu("muonEta","lepton.eta",source),
    muonPhi = makeMuNu("muonPhi","lepton.phi",source),
    muonCharge = makeMuNu("muonCharge","lepton.charge()",source),
    WPt = makeMuNu("WPt","corPt()",source),

    #calMET = makeMuNu("calMET","calibratedMET.pt()",source,True),
    MET = makeMuNu("MET","met().pt",source,True),
    #calMt = makeMuNu("calMt","corMt()",source),
    Mt = makeMuNu("Mt","mt",source),
    
    metJJ = makeMuNu("metjj","metjj",source),
    leptonjj = makeMuNu("leptonjj","leptonjj",source),
    muNuDPhi = makeMuNu("muNuDPhi","dPhi",source),
    muNuRecoil = makeMuNu("muNuRecoil","recoil().pt()",source),
    muNuRelPFIso = makeMuNu("muNuRelPFIso",
     "(lepton.chargedHadronIso()+lepton.photonIso()+lepton.neutralHadronIso())/lepton.pt()",source),
    PFIsoVeto = makeMuNu("PFIsoVeto","lepton.userIso(0)",source),
    PFIsoRho = makeMuNu("PFIsoRho","lepton.userFloat('rho')",source),
    muNuRelStdIso03 = makeMuNu("muNuRelStdIso03",
     "(lepton.isolationR03.sumPt+lepton.isolationR03.emEt+lepton.isolationR03.hadEt)/lepton.pt()",source),
    muNuRelPFIsoDB = makeMuNu("muNuRelPFIsoDB",
     "(lepton.userIso(0)+max(lepton.photonIso()+lepton.neutralHadronIso()-0.5*lepton.puChargedHadronIso,0.0))/lepton.pt()",
     source,True),
    ipDXY = makeMuNu("ipDXY","lepton.userFloat('ipDXY')",source,True),
#    DiSVMass = makeMuNu("DiSVMass","SV1SV2M",source),
#    DiSVPt = makeMuNu("DISVPt","SV1SV2Pt",source),

    dz = makeMuNu("dz",'abs(lepton.userFloat("dz"))',source,True),
    ht = makeMuNu("ht","ht",source,True),
 )
 return commonCollections

def addMuNuEventTreePtDat(process,name,source = 'wCandsJets',sourceZ = 'diMuonsSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
      makeCollections(source,sourceZ),
      coreCollections = cms.VInputTag( cms.InputTag(source) )
   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)

def addMuNuEventTreePtMC(process,name,source = 'wCandsJets',sourceZ = 'diMuonsSorted',lhep="externalLHEProducer"):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
      makeCollections(source,sourceZ),
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
  
      bCandidate1Pt = makeIVFBs("bCandidate1Pt","BC1PT"),
      bCandidate2Pt = makeIVFBs("bCandidate2Pt","BC2PT"),
      bCandidate1Eta = makeIVFBs("bCandidate1Eta","BC1ETA"),
      bCandidate2Eta = makeIVFBs("bCandidate2Eta","BC2ETA"),
      bCandidate1Phi = makeIVFBs("bCandidate1Phi","BC1PHI"),
      bCandidate2Phi = makeIVFBs("bCandidate2Phi","BC2PHI"),
      bCandidateDeltaR = makeIVFBs("bCandidateDeltaR","BCDeltaR"),
      bCandidateDeltaPhi = makeIVFBs("bCandidateDeltaPhi","BDeltaPHI"),

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
