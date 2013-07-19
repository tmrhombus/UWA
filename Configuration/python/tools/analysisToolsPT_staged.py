
import FWCore.ParameterSet.Config as cms
from CommonTools.ParticleFlow.Isolation.tools_cfi import *

from PhysicsTools.PatAlgos.tools.jetTools import *
from PhysicsTools.PatAlgos.tools.helpers import *
from PhysicsTools.PatAlgos.tools.tauTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.metTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.tools.trigTools import *
import sys


def defaultReconstructionPTMC(process,triggerProcess = 'HLT',triggerPaths = ['HLT_Mu9','HLT_Mu11_PFTau15_v1','HLT_Mu11_PFTau15_v1','HLT_Mu11_PFTau15_v2','HLT_Mu15_v1','HLT_Mu15_v2']):
  process.load("UWAnalysis.Configuration.startUpSequence_cff")
  process.load("Configuration.Geometry.GeometryIdeal_cff")
  process.load("Configuration.StandardSequences.MagneticField_cff")
  process.load("Configuration.StandardSequences.Services_cff")
  process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
  process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
  process.load("DQMServices.Core.DQM_cfg")
  process.load("DQMServices.Components.DQMEnvironment_cfi")

  #Make the TriggerPaths Global variable to be accesed by the ntuples
  global TriggerPaths
  TriggerPaths= triggerPaths
  process.analysisSequence = cms.Sequence()

  #Add trigger Matching
  muonTriggerMatchPT(process,triggerProcess)     #adds to analysisSequence
  electronTriggerMatchPT(process,triggerProcess) #adds to analysisSequence
  tauTriggerMatchPT(process,triggerProcess)      #adds to analysisSequence

  #Build good vertex collection
  goodVertexFilter(process)                      #adds to analysisSequence

  #ReNameJetColl(process)  #just to make new collection with same name -- for data
  ReRunJetsMC(process)  #outputs patOverloadedJets       #adds to analysisSequence
  BpmReconstruction(process,"patOverloadedJets")
  BReconstruction(process,"patBpmRecoJets")

  ##jetMCMatching(process,"NewCleanedPatJets")
  ##jetMCMatching(process,"NewSelectedPatJets")
  #jetOverloading(process,"patJetMCMatched")
  #jetOverloading(process,"NewSelectedPatJets")
  #jetOverloading(process,"NewCleanedPatJets")
  #jetOverloading(process,"patJetMCMatched")


  applyDefaultSelectionsPT(process,"patBRecoJets")
  #Default selections for systematics
  #Build MVA MET
  #mvaMet(process)
  genHadrons(process)

  process.runAnalysisSequence = cms.Path(process.analysisSequence)
########## Rochester Corrections?
######  process.looseMu = cms.EDProducer("PATMuonCleanerBySegments",
######   src = cms.InputTag("cleanPatMuons"),
######   preselection = cms.string("track.isNonnull"),
######   passthrough = cms.string("isGlobalMuon && numberOfMatches >= 2"),
######   fractionOfSharedSegments = cms.double(0.499)
######  )
#####  process.corrMuons = cms.EDProducer("PATMuonCalibrationChooser",
#####   src = cms.InputTag("cleanPatMuons"),
#####   #src = cms.InputTag("looseMu"),
#####   rochcorType = cms.string("RochCor2012") # Rochester Correction types: RochCor2011A, RochCor2011B, RochCor2012
#####  #rochcorType = cms.string(rochCor) # Rochester Correction types: RochCor2011A, RochCor2011B, RochCor2012
#####  )
#####  process.recorrMuons = cms.EDProducer("PATMuonRochesterEmbedder",
#####   src = cms.InputTag("corrMuons"),
#####   #src = cms.InputTag("cleanPatMuons"),
#####   #src = cms.InputTag("looseMu"),
#####   isMC = cms.bool(False), #isMC and isSync don't do anything
#####   isSync = cms.bool(False), #use fake smearing for synchronization purposes
#####  )
#####
#####  #process.analysisSequence = cms.Sequence(process.analysisSequence*process.looseMu*process.recorrMuons)
#####  process.analysisSequence = cms.Sequence(process.analysisSequence*process.corrMuons*process.recorrMuons)

def defaultReconstructionPT(process,triggerProcess = 'HLT',triggerPaths = ['HLT_Mu9','HLT_Mu11_PFTau15_v1','HLT_Mu11_PFTau15_v1','HLT_Mu11_PFTau15_v2','HLT_Mu15_v1','HLT_Mu15_v2']):
  process.load("UWAnalysis.Configuration.startUpSequence_cff")
  process.load("Configuration.Geometry.GeometryIdeal_cff")
  process.load("Configuration.StandardSequences.MagneticField_cff")
  process.load("Configuration.StandardSequences.Services_cff")
  process.load("TrackingTools.TransientTrack.TransientTrackBuilder_cfi")
  process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
  process.load("DQMServices.Core.DQM_cfg")
  process.load("DQMServices.Components.DQMEnvironment_cfi")

  #Make the TriggerPaths Global variable to be accesed by the ntuples
  global TriggerPaths
  TriggerPaths= triggerPaths
  process.analysisSequence = cms.Sequence()
  
  #Add trigger Matching
  muonTriggerMatchPT(process,triggerProcess)
  electronTriggerMatchPT(process,triggerProcess)
  tauTriggerMatchPT(process,triggerProcess)
  #jetOverloading(process)
  #Build good vertex collection
  goodVertexFilter(process)

  jetOverloading(process,"selectedPatJets")
  BpmReconstruction(process,"patOverloadedJets")
  BReconstruction(process,"patBpmRecoJets")
  applyDefaultSelectionsPT(process)
  #Default selections for systematics

  #Build MVA MET
  #mvaMet(process)

  process.runAnalysisSequence = cms.Path(process.analysisSequence)


def jetMCMatching(process,jets):

  process.patJetMCMatched = cms.EDProducer('MCBHadronJetProducer',
                                        src = cms.InputTag(jets)

  )

  process.jetMCMatching = cms.Sequence(process.patJetMCMatched)
  #process.patDefaultSequence*=process.jetOverloading
  process.createJetMCMatching=cms.Path(process.jetMCMatching)


def BReconstruction(process,jets):
  process.patBRecoJets = cms.EDProducer('PATJetBReco',
                                        src = cms.InputTag(jets),
                                        leptons = cms.InputTag("cleanPatMuons"),
                                        vertices=cms.InputTag("offlinePrimaryVertices")
  )

  process.BReconstruction = cms.Sequence(process.patBRecoJets)
  #process.analysisSequence *= process.BReconstruction
  process.createBRecoJets=cms.Path(process.BReconstruction)

def BpmReconstruction(process,jets):
  process.patBpmRecoJets = cms.EDProducer('PATJetBpmReco',
                                        src = cms.InputTag(jets),
                                        leptons = cms.InputTag("cleanPatMuons"),
                                        vertices=cms.InputTag("offlinePrimaryVertices")
  )

  process.BpmReconstruction = cms.Sequence(process.patBpmRecoJets)
  #process.analysisSequence *= process.BpmReconstruction
  process.createBpmRecoJets=cms.Path(process.BpmReconstruction)


def jetOverloading(process,jets):
  process.patOverloadedJets = cms.EDProducer('PATJetOverloader',
                                        src = cms.InputTag(jets),
                                        leptons = cms.InputTag("cleanPatMuons"),
                                        vertices=cms.InputTag("offlinePrimaryVertices")
  )

  process.jetOverloading = cms.Sequence(process.patOverloadedJets)
  process.analysisSequence *= process.jetOverloading
  #process.patDefaultSequence*=process.jetOverloading
  #process.createOverloadedJets=cms.Path(process.jetOverloading)


def genHadrons(process):
  
  process.bhadrons = cms.EDProducer('MCBHadronProducer',
                                    quarkId = cms.uint32(5)
                                    )
  
  process.cbarCands=cms.EDProducer("GenParticlePruner",
                                   src = cms.InputTag("genParticles"),
                                   select = cms.vstring("keep pdgId = -4",
                                                        )
                                   )
  
  process.cCands=cms.EDProducer("GenParticlePruner",
                                src = cms.InputTag("genParticles"),
                                select = cms.vstring("keep pdgId= 4 ",
                                                     )
                                )
  
  process.analysisSequence = cms.Sequence(process.analysisSequence * process.bhadrons * process.cbarCands * process.cCands)
  #process.createSimCollections=cms.Path(process.bhadrons*process.cbarCands*process.cCands)


def mvaMet(process):
  
  process.load("RecoMET.METProducers.mvaPFMET_cff")
  process.load("PhysicsTools.PatAlgos.producersLayer1.metProducer_cfi")
  
  process.metEleTaus = cms.EDFilter("PATTauSelector",
                                           src = cms.InputTag("cleanPatTaus"),
                                           cut = cms.string('abs(userFloat("dz"))<0.2&&pt>20&&tauID("byLooseIsolationMVA")&&tauID("againstElectronMedium")&&tauID("againstElectronMVA")&&tauID("againstMuonLoose")&&abs(eta())<2.3'),
                                           filter = cms.bool(False)
   )
  process.metMuTaus = cms.EDFilter("PATTauSelector",
                                           src = cms.InputTag("cleanPatTaus"),
                                           cut = cms.string('abs(userFloat("dz"))<0.2&&pt>20&&tauID("byLooseIsolationMVA")&&tauID("againstElectronLoose")&&tauID("againstMuonTight")&&abs(eta())<2.3'),
                                           filter = cms.bool(False)
   )
  process.metElectrons = cms.EDFilter("PATElectronSelector",
                                           src = cms.InputTag("cleanPatElectrons"),
                                           cut = cms.string('abs(userFloat("dz"))<0.2&&pt>20&&userFloat("wp95V")>0&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.1&&!(userFloat("hasConversion")>0)&&userInt("missingHits")==0&&abs(userFloat("ipDXY"))<0.045&&abs(eta())<2.1'),
                                           filter = cms.bool(False)
   )
  process.metMuons = cms.EDFilter("PATMuonSelector",
                                           src = cms.InputTag("cleanPatMuons"),
                                           cut = cms.string('abs(userFloat("dz"))<0.2&&pt>17&&userInt("tightID")>0&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.1&&abs(eta())<2.1&&abs(userFloat("ipDXY"))<0.045'),
                                           filter = cms.bool(False)
   )
  
  process.pfMEtMVA2.inputFileNames.U = cms.FileInPath('pharris/MVAMet/data/gbrmet_52.root')
  process.pfMEtMVA2.inputFileNames.DPhi = cms.FileInPath('pharris/MVAMet/data/gbrmetphi_52.root')
  process.pfMEtMVA2.inputFileNames.CovU1 = cms.FileInPath('pharris/MVAMet/data/gbrmetu1cov_52.root')
  process.pfMEtMVA2.inputFileNames.CovU2 = cms.FileInPath('pharris/MVAMet/data/gbrmetu2cov_52.root')
  

  process.mvaMetMuTau = process.pfMEtMVA2.clone()
  process.mvaMetMuTau.srcLeptons = cms.VInputTag('metMuons', 'metMuTaus')
  process.patMVAMetMuTau = process.patMETs.clone(
   metSource = cms.InputTag('mvaMetMuTau'),
   addMuonCorrections = cms.bool(False),
   addGenMET = cms.bool(False)
  )
  
  process.mvaMetEleTau = process.pfMEtMVA2.clone()
  process.mvaMetEleTau.srcLeptons = cms.VInputTag('metElectrons', 'metEleTaus')
  process.patMVAMetEleTau = process.patMETs.clone(
   metSource = cms.InputTag('mvaMetEleTau'),
   addMuonCorrections = cms.bool(False),
   addGenMET = cms.bool(False)
  )
  
  process.mvaMetMuTauSequence = cms.Sequence(process.metMuTaus*process.metMuons*process.mvaMetMuTau*process.patMVAMetMuTau)
  process.mvaMetEleTauSequence = cms.Sequence(process.metEleTaus*process.metElectrons*process.mvaMetEleTau*process.patMVAMetEleTau)
  process.analysisSequence = cms.Sequence(process.analysisSequence*process.mvaMetMuTauSequence*process.mvaMetEleTauSequence)
  



def applyDefaultSelectionsPT(process,jets):
  #DONT CHANGE THOSE HERE:: THEY ARE NOT USED FOR YOUR SELECTIONS!!!
  #ONLY FOR SYSTEMATICS . PLEASE CHANGE THEM in YOUR CFG FILE IF REALLY NEEDED
  process.selectedPatTaus = cms.EDFilter("PATTauSelector",
                                           src = cms.InputTag("cleanPatTaus"),
                                           cut = cms.string('pt>15&&tauID("byLooseIsolationMVA")&&tauID("againstElectronLoose")&&tauID("againstMuonLoose")'),
                                           filter = cms.bool(False)
   )
  process.selectedPatElectrons = cms.EDFilter("PATElectronSelector",
                                           src = cms.InputTag("cleanPatElectrons"),
                                           cut = cms.string('pt>20&&userFloat("wp95")>0&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.3'),
                                           filter = cms.bool(False)
   )
  process.selectedPatMuons = cms.EDFilter("PATMuonSelector",
                                           src = cms.InputTag("cleanPatMuons"),
                                           cut = cms.string('pt>20&&userInt("tightID")&&(userIso(0)+max(photonIso+neutralHadronIso()-0.5*userIso(2),0.0))/pt()<0.3'),
                                           filter = cms.bool(False)
   )
  process.cleanPatJets = cms.EDProducer("PATJetCleaner",
                                        src = cms.InputTag(jets),
                                        preselection = cms.string('abs(eta)<5.0&&userFloat("idLoose")>0&&pt>10&&userInt("fullIdLoose")>0'),#&&userFloat("fullDiscriminant")>0
                                        checkOverlaps = cms.PSet( 
                                         muons = cms.PSet(
                                          src = cms.InputTag("cleanPatMuons"),
                                          algorithm = cms.string("byDeltaR"),
                                          preselection = cms.string("pt>10&&isGlobalMuon&&isTrackerMuon&&(chargedHadronIso()+max(photonIso+neutralHadronIso(),0.0))/pt()<0.3"),
                                          deltaR = cms.double(0.5),
                                          checkRecoComponents = cms.bool(False),
                                          pairCut = cms.string(""),
                                          requireNoOverlaps = cms.bool(True),
                                         ),
                                         electrons = cms.PSet(
                                          src = cms.InputTag("cleanPatElectrons"),
                                          algorithm = cms.string("byDeltaR"),
                                          preselection = cms.string("pt>10&&(chargedHadronIso()+max(photonIso()+neutralHadronIso(),0.0))/pt()<0.3"),
                                          deltaR = cms.double(0.5),
                                          checkRecoComponents = cms.bool(False),
                                          pairCut = cms.string(""),
                                          requireNoOverlaps = cms.bool(True),
                                         ),
                                        ),
                                        finalCut = cms.string('')
                                        )	
  process.selectedObjectsForSyst = cms.Sequence(process.selectedPatTaus+process.selectedPatElectrons+process.selectedPatMuons+process.cleanPatJets)
  process.analysisSequence = cms.Sequence(process.analysisSequence*process.selectedObjectsForSyst)


def muonTriggerMatchPT(process,triggerProcess):

   process.triggeredPatMuons = cms.EDProducer("MuonTriggerMatcher",
                                            src = cms.InputTag("cleanPatMuons"),
                                            trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
                                            filters = cms.VInputTag(
                                                cms.InputTag('hltSingleMuIsoL3IsoFiltered12','',triggerProcess),
                                                cms.InputTag('hltSingleMuIsoL3IsoFiltered15','',triggerProcess),
                                                cms.InputTag('hltSingleMuIsoL3IsoFiltered24','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu15IsoPFTau15','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu12IsoPFTau10','',triggerProcess),
                                                cms.InputTag('hltSingleMuIsoL3IsoFiltered17','',triggerProcess),
                                                cms.InputTag('hltSingleMuIsoL1s14L3IsoFiltered15eta2p1',"",triggerProcess),
                                                cms.InputTag('hltL3IsoL1sMu14Eta2p1L1f0L2f14QL2IsoL3f24L3IsoFiltered','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu15IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f18QL3crIsoFiltered10','',triggerProcess),
                                                cms.InputTag('hltL3crIsoL1sMu16Eta2p1L1f0L2f16QL3f24QL3crIsoFiltered10','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu18LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu17LooseIsoPFTau20','',triggerProcess)
                                            ),
                                            pdgId = cms.int32(13)
   )
  
   process.analysisSequence*= process.triggeredPatMuons

def electronTriggerMatchPT(process,triggerProcess):

   process.triggeredPatElectronsL = cms.EDProducer("ElectronTriggerMatcher",
                                            src = cms.InputTag("cleanPatElectrons"),
                                            trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
                                            filters = cms.VInputTag(
                                                cms.InputTag('hltEle17CaloIdLCaloIsoVLPixelMatchFilterDoubleEG125','',triggerProcess),
                                            ),
                                            pdgId = cms.int32(0)
   )
   process.triggeredPatElectrons = cms.EDProducer("ElectronTriggerMatcher",
                                            src = cms.InputTag("triggeredPatElectronsL"),
                                            trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
                                            filters = cms.VInputTag(
                                                cms.InputTag('hltOverlapFilterIsoEle15IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle15TightIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle18MediumIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle18TightIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle18IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20MediumIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20WP90LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltEle17CaloIdVTCaloIsoVTTrkIdTTrkIsoVTEle8PMMassFilter','',triggerProcess),
                                                cms.InputTag('hltEle20CaloIdVTCaloIsoTTrkIdTTrkIsoTTrackIsoFilterL1IsoEG18OrEG20','',triggerProcess)
                                            ),
                                            pdgId = cms.int32(11)
   )
   
   process.analysisSequence=cms.Sequence(process.analysisSequence*process.triggeredPatElectronsL*process.triggeredPatElectrons)

def tauTriggerMatchPT(process,triggerProcess):
   strTrig=''
   for i in TriggerPaths:
    if i==TriggerPaths[0]:
      strTrig+='path(\"'+i+'\")'
    else:
      strTrig+='|| path(\"'+i+'\")'


   #Match With The triggers
   process.preTriggeredPatTaus = cms.EDProducer("TauTriggerMatcher",
                                            src = cms.InputTag("cleanPatTaus"),
                                            trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
                                            filters = cms.VInputTag(
                                                cms.InputTag('hltFilterDoubleIsoPFTau20Trk5LeadTrack5IsolationL1HLTMatched','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu18LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20WP90LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu17LooseIsoPFTau20','',triggerProcess)
                                            ),
                                            pdgId = cms.int32(0)
   )

   process.triggeredPatTaus = cms.EDProducer("TauTriggerMatcher",
                                            src = cms.InputTag("preTriggeredPatTaus"),
                                            trigEvent = cms.InputTag("hltTriggerSummaryAOD"),
                                            filters = cms.VInputTag(
                                                cms.InputTag('hltOverlapFilterIsoMu15IsoPFTau15','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu15IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu15MediumIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu15TightIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterMu15IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu12IsoPFTau10','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu15IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle15IsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle15TightIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle18MediumIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20MediumIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu18LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoEle20WP90LooseIsoPFTau20','',triggerProcess),
                                                cms.InputTag('hltOverlapFilterIsoMu17LooseIsoPFTau20','',triggerProcess)
                                            ),
                                            pdgId = cms.int32(15)
   )
                                            
   process.analysisSequence=cms.Sequence(process.analysisSequence*process.preTriggeredPatTaus*process.triggeredPatTaus)
  

def getAllEventCounters(process,path,onSkim = False):
        stringList = []
        if onSkim:
          stringList.append('processedEvents')

        modules = listModules(path)
    
        for mod in modules:
            if(hasattr(mod,'label')):
                if mod.label().find('Counter') !=-1 :
                    stringList.append(mod.name.value())
        print 'List Of Filters'
        print stringList
        
        return cms.untracked.vstring(stringList)

def addEventSummary(process,onSkim = False,name = 'summary',path = 'eventSelection'):
    
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )

   summary = cms.EDAnalyzer('EventSummary',
                            src =getAllEventCounters(process,getattr(process,path),onSkim)
   )

   setattr(process,name,summary)
   if onSkim:
        process.EDMtoMEConverter = cms.EDAnalyzer("EDMtoMEConverter",
                                               Name = cms.untracked.string('EDMtoMEConverter'),
                                               Verbosity = cms.untracked.int32(1), # 0 provides no output
                                               # 1 provides basic output
                                               Frequency = cms.untracked.int32(50),
                                               convertOnEndLumi = cms.untracked.bool(True),
                                               convertOnEndRun = cms.untracked.bool(True)
                                               )
        eventSummaryPath=cms.EndPath(process.EDMtoMEConverter+getattr(process,name))
        setattr(process,name+"Path",eventSummaryPath)
   else:
        eventSummaryPath=cms.EndPath(getattr(process,name))
        setattr(process,name+"Path",eventSummaryPath)



def createGeneratedParticles(process,name,commands):


  refObjects = cms.EDProducer("GenParticlePruner",
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
    "drop * "
    )
   )
  refObjects.select.extend(commands)
  setattr(process,name,refObjects)
  process.analysisSequence*= getattr(process,name)


def createGeneratedTaus(process,decayMode,fiducialCuts):
  process.generatedTaus = cms.EDFilter("TauGenJetDecayModeSelector",
                                       src = cms.InputTag("tauGenJets"),
                                       select = cms.vstring(decayMode),
                                       filter = cms.bool(False)
                                       )
  process.generatedTausInAcceptance = cms.EDFilter("GenJetSelector",
                                           src = cms.InputTag("generatedTaus"),
                                           cut = cms.string(fiducialCuts),
                                           filter = cms.bool(False)
                                           )

  process.analysisSequence*= process.generatedTaus
  process.analysisSequence*= process.generatedTausInAcceptance


def goodVertexFilter(process):

  process.primaryVertexFilter = cms.EDFilter("VertexSelector",
                                        src = cms.InputTag('offlinePrimaryVertices'),
                                        cut = cms.string('ndof()>4&&position().rho()<2&&abs(z())<24'),
                                        filter = cms.bool(False)
  )
  process.analysisSequence*= process.primaryVertexFilter


def cloneAndReplaceInputTag(process,sequence,oldValue,newValue,postfix):
  #First Clone the sequence
  p = cloneProcessingSnippet(process, sequence, postfix)
  massSearchReplaceAnyInputTag(p,oldValue,newValue )
  modules = listModules(p)

  #Change the labels of the counters
  for mod in modules:
    if(hasattr(mod,'label')):
      if mod.label().find('Counter') !=-1 :
        if(hasattr(mod,'name')):
          newValue = mod.name.value()+postfix
          mod.name=cms.string(newValue)
  return p



def createSystematics(process,sequence,postfix,muScale,eScale,tauScale,jetScale,unclusteredScale,electronresb = 0.0, electronrese = 0.0):

  #First Clone the sequence
  p = cloneProcessingSnippet(process, sequence, postfix)
  modules = listModules(p)

  #Change the labels of the counters and the smearign modules
  for mod in modules:
    if(hasattr(mod,'label')):
      if mod.label().find('Counter') !=-1 :
        if(hasattr(mod,'name')):
          newValue = mod.name.value()+postfix
          mod.name=cms.string(newValue)
      if mod.label().find('smearedMuons') !=-1 :
          mod.energyScale = cms.double(muScale)
      if mod.label().find('smearedTaus') !=-1 :
          mod.energyScale = cms.double(tauScale)
      if mod.label().find('smearedElectrons') !=-1 :
          mod.energyScale = cms.double(eScale)
          mod.deltaPtB = cms.double(electronresb)
          mod.deltaPtE = cms.double(electronrese)
      if mod.label().find('smearedJets') !=-1 :
          mod.energyScaleDB = cms.double(jetScale) ##changed from int32 to double
      if mod.label().find('smearedMET') !=-1 :
          mod.unclusteredScale= cms.double(unclusteredScale)
  return cms.Path(p)





def createRecoilSystematics(process,sequence,postfix,metScale,metResolution):

  #First Clone the sequence
  p = cloneProcessingSnippet(process, sequence, postfix)
  modules = listModules(p)

  #Change the labels of the counters and the smearign modules
  for mod in modules:
    if(hasattr(mod,'label')):
      if mod.label().find('Counter') !=-1 :
        if(hasattr(mod,'name')):
          newValue = mod.name.value()+postfix
          mod.name=cms.string(newValue)
    if(hasattr(mod,'metCalibration')):
          mod.metCalibration.shiftScale = cms.untracked.double(metScale)
          mod.metCalibration.shiftRes = cms.untracked.double(metResolution)
      
  return cms.Path(p)


def addTagAndProbePlotter(process,type,name,src,ref,selections,methods,triggers,triggersProbe):

  process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
  muonAnalysis = cms.EDAnalyzer(type,
                                src=cms.InputTag(src),
                                vertices=cms.InputTag("primaryVertexFilter"),
                                ref=cms.InputTag(ref),
                                patTrigger = cms.InputTag("patTrigger"),
                                id= cms.vstring(selections),
                                methods= cms.vstring(methods),
                                triggers = cms.vstring(triggers),
                                triggersProbe = cms.vstring(triggersProbe),
  )
  
  setattr(process,'tagAndProbe'+name,muonAnalysis)
  p = cms.EndPath(getattr(process,'tagAndProbe'+name))
  setattr(process,'tagAndProbePath'+name,p)

def ReNameJetColl(process):

  process.load("PhysicsTools.PatAlgos.patSequences_cff")
  process.NewSelectedPatJets = process.selectedPatJets.clone(src = cms.InputTag("selectedPatJets"))
  process.analysisSequence*= process.NewSelectedPatJets
  

def ReRunJetsMC(process):

  process.load("RecoJets.Configuration.RecoPFJets_cff") 
  import PhysicsTools.PatAlgos.tools.jetTools as jettools
  process.load("PhysicsTools.PatAlgos.patSequences_cff")
  process.load("UWAnalysis.Configuration.tools.patJetPUId_cfi")
  process.pileupJetIdProducer.applyJec = cms.bool(True)

  # Define options for BTagging - these are release dependent.
  btag_options = {'doBTagging': True}
  btag_options['btagInfo'] = [
            'secondaryVertexTagInfos',
  ]
  btag_options['btagdiscriminators'] = [
            'combinedSecondaryVertexMVABJetTags',
            'combinedSecondaryVertexBJetTags',
  ]
  jec = ['L1FastJet', 'L2Relative', 'L3Absolute']
  # For Data jec.extend(['L2L3Residual'])
  
  jettools.switchJetCollection(
        process,
        cms.InputTag('ak5PFJets'),
        doJTA=False,
        jetCorrLabel=('AK5PF', jec), #= None,
        doType1MET=False,
        doJetID=True,
        genJetCollection=cms.InputTag("ak5GenJets"),
        outputModules=[],
        **btag_options       
  )
  process.patJets.embedPFCandidates = False
  process.patJets.embedCaloTowers = False
  process.patJets.embedGenJetMatch = False
  process.patJets.addAssociatedTracks = False
  process.patJets.embedGenPartonMatch = False
  process.patJets.tagInfoSources = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
  process.patJets.discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexMVABJetTags"), cms.InputTag("combinedSecondaryVertexBJetTags"))
  process.patJets.addBTagInfo = cms.bool(True)
  
  process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
   	      tracks       = cms.InputTag("generalTracks"),
	      jets         = cms.InputTag("ak5PFJets"),
              coneSize     = cms.double(0.5)
  )
  
  process.load('UWAnalysis.Configuration.tools.RecoBTag_cff')  
  process.patJetCharge.src = cms.InputTag("ak5JetTracksAssociatorAtVertex")
  process.NewSelectedPatJets = process.selectedPatJets.clone(src = cms.InputTag("patJetId"))
  #process.NewCleanedPatJets = process.cleanPatJets.clone(src = cms.InputTag("NewSelectedPatJets")) #added cleaning module

  process.patOverloadedJets = cms.EDProducer('PATJetOverloader',
                                        src = cms.InputTag("NewSelectedPatJets"),
                                        leptons = cms.InputTag("cleanPatMuons"),
                                        vertices=cms.InputTag("offlinePrimaryVertices")
  )

  process.analysisSequence = cms.Sequence(
  #process.reJetSequence = cms.Sequence(
  					process.analysisSequence*
  					process.ak5PFJets*
  					process.ak5JetTracksAssociatorAtVertex*
  					process.btagging*
  					process.pileupJetIdProducer*
  					process.makePatJets*
  					process.patJetsPUID*
  					process.patJetId*
  					process.NewSelectedPatJets#*
                                        #process.NewCleanedPatJets   #put cleaning in path
					*process.patOverloadedJets
  					)
  #process.runJetSequence = cms.Path(process.reJetSequence)

def ReRunJets(process):

  process.load("RecoJets.Configuration.RecoPFJets_cff") 
  import PhysicsTools.PatAlgos.tools.jetTools as jettools
  process.load("PhysicsTools.PatAlgos.patSequences_cff")
  process.load("UWAnalysis.Configuration.tools.patJetPUId_cfi")
  
  process.pileupJetIdProducer.applyJec = cms.bool(True)

  # Define options for BTagging - these are release dependent.
  btag_options = {'doBTagging': True}
  btag_options['btagInfo'] = [
            'secondaryVertexTagInfos',
  ]
  btag_options['btagdiscriminators'] = [
            'combinedSecondaryVertexMVABJetTags',
            'combinedSecondaryVertexBJetTags',
  ]

  jec = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']

  
  jettools.switchJetCollection(
        process,
        cms.InputTag('ak5PFJets'),
        doJTA=False,
        jetCorrLabel=('AK5PF', jec),
        #jetCorrLabel = None,
        doType1MET=False,
        doJetID=True,
        genJetCollection=cms.InputTag("ak5GenJets"),
        outputModules=[],
        **btag_options       
  )
  process.patJets.embedPFCandidates = False
  process.patJets.embedCaloTowers = False
  process.patJets.embedGenJetMatch = False
  process.patJets.addAssociatedTracks = False
  process.patJets.embedGenPartonMatch = False
  process.patJets.tagInfoSources = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
  process.patJets.discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexMVABJetTags"), cms.InputTag("combinedSecondaryVertexBJetTags"))
  process.patJets.addBTagInfo = cms.bool(True)
  
  process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
   	  tracks       = cms.InputTag("generalTracks"),
      jets         = cms.InputTag("ak5PFJets"),
      coneSize     = cms.double(0.5)
  )
  
  process.load('UWAnalysis.Configuration.tools.RecoBTag_cff')  
  process.patJetCharge.src = cms.InputTag("ak5JetTracksAssociatorAtVertex")
  process.NewSelectedPatJets = process.selectedPatJets.clone(src = cms.InputTag("patJetId"))
  process.makePatJetsData = cms.Sequence(process.patJetCorrFactors+
  										process.patJetCharge+
  										process.patJets)
  
  process.analysisSequence = cms.Sequence(
  					process.analysisSequence*
  					process.ak5PFJets*
  					process.ak5JetTracksAssociatorAtVertex*
  					process.btagging*
  					process.pileupJetIdProducer*
  					process.makePatJetsData*
  					process.patJetsPUID*
  					process.patJetId*
  					process.NewSelectedPatJets  					
  					)


def ReRunJetsEMB(process):

  process.load("RecoJets.Configuration.RecoPFJets_cff") 
  import PhysicsTools.PatAlgos.tools.jetTools as jettools
  process.load("PhysicsTools.PatAlgos.patSequences_cff")
  process.load("UWAnalysis.Configuration.tools.patJetPUId_cfi")
  
  process.pileupJetIdProducer.applyJec = cms.bool(True)

  # Define options for BTagging - these are release dependent.
  btag_options = {'doBTagging': True}
  btag_options['btagInfo'] = [
            'secondaryVertexTagInfos',
  ]
  btag_options['btagdiscriminators'] = [
            'combinedSecondaryVertexMVABJetTags',
            'combinedSecondaryVertexBJetTags',
  ]

  jec = ['L1FastJet', 'L2Relative', 'L3Absolute', 'L2L3Residual']

  
  jettools.switchJetCollection(
        process,
        cms.InputTag('ak5PFJets'),
        doJTA=False,
        jetCorrLabel=('AK5PF', jec),
        #jetCorrLabel = None,
        doType1MET=False,
        doJetID=True,
        genJetCollection=cms.InputTag("ak5GenJets"),
        outputModules=[],
        **btag_options       
  )
  process.patJets.embedPFCandidates = False
  process.patJets.embedCaloTowers = False
  process.patJets.embedGenJetMatch = False
  process.patJets.addAssociatedTracks = False
  process.patJets.embedGenPartonMatch = False
  process.patJets.tagInfoSources = cms.VInputTag(cms.InputTag("secondaryVertexTagInfos"))
  process.patJets.discriminatorSources = cms.VInputTag(cms.InputTag("combinedSecondaryVertexMVABJetTags"), cms.InputTag("combinedSecondaryVertexBJetTags"))
  process.patJets.addBTagInfo = cms.bool(True)
  
  process.ak5JetTracksAssociatorAtVertex = cms.EDProducer("JetTracksAssociatorAtVertex",
   	  tracks       = cms.InputTag("tmfTracks"),
      jets         = cms.InputTag("ak5PFJets"),
      coneSize     = cms.double(0.5)
  )
  
  process.load('UWAnalysis.Configuration.tools.RecoBTag_cff')  
  process.patJetCharge.src = cms.InputTag("ak5JetTracksAssociatorAtVertex")
  process.NewSelectedPatJets = process.selectedPatJets.clone(src = cms.InputTag("patJetId"))
  process.analysisSequence = cms.Sequence(
  					process.analysisSequence*
  					process.ak5PFJets*
  					process.ak5JetTracksAssociatorAtVertex*
  					process.btagging*
  					process.pileupJetIdProducer*
  					process.makePatJets*
  					process.patJetsPUID*
  					process.patJetId*
  					process.NewSelectedPatJets  					
  					)
