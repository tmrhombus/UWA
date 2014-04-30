import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
#process.GlobalTag.globaltag = 'START53_V19PR::All' #for global tag with old data
process.GlobalTag.globaltag = 'START53_V27::All' # for global tag with re-reco data

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(500)
)

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
   #$inputFileNames
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-80136C46-8FE1-E211-BA7E-00266CFEFC5C.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-FC84B460-AC06-E211-9731-003048678B38.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-FC989FB7-1907-E211-A0C3-001E67396ACC.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-F8EF9511-5BEF-E211-92AA-0030487E5399.root'
#"file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/mc.root"
#'file:///hdfs/store/user/mcepeda/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/Spring2014PATTuples/patTuple_cfg-529DE452-5798-E211-9D62-0026189438B1.root' 
'file:///hdfs/store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-04557220-78E4-E211-8C2D-003048FFD7BE.root' 
 ),
 inputCommands=cms.untracked.vstring(
  'keep *',
  'drop *_finalState*_*_*',
  'drop *_patFinalStateEvent*_*_*'
 )
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load("PhysicsTools.PatAlgos.patSequences_cff")
from UWAnalysis.Configuration.tools.analysisToolsPT import *

defaultReconstructionPT(process,
 'HLT',
 ['HLT_IsoMu24_eta2p1_v','HLT_Mu40_eta2p1_v'],
 itsMC=True,itsData=False)

createGeneratedParticles(process,
 'genWs',
 ["keep++ pdgId = {W+}","keep++ pdgId = {W-}"]
)
createGeneratedParticles(process,
 'genbbCands',
 ["keep abs(pdgId) = 5"]
)
createGeneratedParticles(process,
 'genbbCandsMinus',
 ["keep pdgId = -5"]
)
createGeneratedParticles(process,
'genccCands',
 ["keep abs(pdgId) = 4"]
)
createGeneratedParticles(process,
'gentCands',
 ["keep pdgId = 6"]
)
createGeneratedParticles(process,
'gentbarCands',
 ["keep pdgId = -6"]
)

process.findMuons = cms.EDFilter("PATMuonSelector",
                                           src = cms.InputTag("cleanPatMuons"),
                                           cut = cms.string('pt>25&&abs(eta)<2.1'),
                                           filter = cms.bool(False)
)

process.jetsFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("jetsETARED"),
                                minNumber = cms.uint32(1)
                             )

process.muonsFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("findMuons"),
                                minNumber = cms.uint32(1)
                             )

process.jetsETARED = cms.EDProducer("PATJetCleaner",
   src = cms.InputTag("selectedPatJets"),
   preselection = cms.string('abs(eta)<3.&&pt>20&&userFloat("idLoose")>0'),
   checkOverlaps = cms.PSet(
       muons = cms.PSet(
        src = cms.InputTag("findMuons"),
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

process.preCleaning=cms.Sequence(process.findMuons*process.jetsETARED*process.jetsFilter*process.muonsFilter)



process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.preCleaning*process.selectionSequence) ##changing to multiples see below

process.selectionSequenceMuonUp    = createSystematics(process,process.selectionSequence,'MuonUp'  ,1.01, 1.0, 1.0, 0, 1.0)
process.selectionSequenceMuonDown  = createSystematics(process,process.selectionSequence,'MuonDown',0.99, 1.0, 1.0, 0, 1.0)
process.selectionSequenceJetUp     = createSystematics(process,process.selectionSequence,'JetUp'   ,1.00, 1.0, 1.0, 1, 1.0)
process.selectionSequenceJetDown   = createSystematics(process,process.selectionSequence,'JetDown' ,1.00, 1.0, 1.0,-1, 1.0)
process.selectionSequenceUCEUp     = createSystematics(process,process.selectionSequence,'UCEUp'   ,1.00, 1.0, 1.0, 0, 1.1)
process.selectionSequenceUCEDown   = createSystematics(process,process.selectionSequence,'UCEDown' ,1.00, 1.0, 1.0, 0, 0.9)

process.eventSelectionMuonUp    =  cms.Path(process.preCleaning*process.selectionSequenceMuonUp)
process.eventSelectionMuonDown  =  cms.Path(process.preCleaning*process.selectionSequenceMuonDown)
process.eventSelectionJetUp     =  cms.Path(process.preCleaning*process.selectionSequenceJetUp)
process.eventSelectionJetDown   =  cms.Path(process.preCleaning*process.selectionSequenceJetDown)
process.eventSelectionUCEUp     =  cms.Path(process.preCleaning*process.selectionSequenceUCEUp)
process.eventSelectionUCEDown   =  cms.Path(process.preCleaning*process.selectionSequenceUCEDown)




from UWAnalysis.Configuration.tools.ntupleToolsPTwbb import *
addMuNuEventTreePtMC(process,'muNuEventTree',lhep="externalLHEProducer")

addEventSummary(process,True)

addMuNuEventTreePtMC(process,'muNuEventTreeMuonUp','wCandsJetsMuonUp','diMuonsSortedMuonUp',lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeMuonDown','wCandsJetsMuonDown','diMuonsSortedMuonDown',lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeJetUp','wCandsJetsJetUp','diMuonsSortedJetUp',lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeJetDown','wCandsJetsJetDown','diMuonsSortedJetDown',lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeUCEUp','wCandsJetsUCEUp','diMuonsSortedUCEUp',lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeUCEDown','wCandsJetsUCEDown','diMuonsSortedUCEDown',lhep="externalLHEProducer")
process.TFileService.fileName = cms.string('mc.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
