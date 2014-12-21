import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V27::All' # for global tag with re-reco data

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
  # $inputFileNames
  #'file:/afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/mc.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Spring2014PATTuples/patTuple_cfg-FEE55DEF-22F0-E111-9F78-001E67398633.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-FC989FB7-1907-E211-A0C3-001E67396ACC.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-FC84B460-AC06-E211-9731-003048678B38.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-02A0D7CE-75E4-E211-9EBB-002618943800.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-FC989FB7-1907-E211-A0C3-001E67396ACC.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-F8EF9511-5BEF-E211-92AA-0030487E5399.root'

#test of new v2c pats
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FED0991E-94CE-E111-84E9-003048673F2C.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF7AC04-A9EE-E111-8FCD-0025B3E06484.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF3D07A-A803-E211-8AB4-001E67397698.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEFD18A6-00E2-E211-A836-1CC1DE051028.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEFE64DC-3C05-E211-80E4-003048D438EA.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF3BE77-7CE4-E211-BB7A-002618FDA262.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEDEDCE3-0307-E211-BC69-003048D45FBA.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF973CF-DCEE-E211-A115-00259081A2C8.root", 
"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEE65930-1407-E211-8EDF-003048678F6C.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEDB7460-9B0D-E211-98E4-001E67398156.root", 
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
 ['HLT_IsoMu24_eta2p1_v','HLT_Mu40_eta2p1_v','HLT_Ele27_WP80'],
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

process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.selectionSequence) ##changing to multiples see below

process.selectionSequenceMuonUp    = createSystematics(process,process.selectionSequence,'MuonUp'  ,1.01, 1.0, 1.0, 0, 1.0)
process.selectionSequenceMuonDown  = createSystematics(process,process.selectionSequence,'MuonDown',0.99, 1.0, 1.0, 0, 1.0)
process.selectionSequenceJetUp     = createSystematics(process,process.selectionSequence,'JetUp'   ,1.00, 1.0, 1.0, 1, 1.0)
process.selectionSequenceJetDown   = createSystematics(process,process.selectionSequence,'JetDown' ,1.00, 1.0, 1.0,-1, 1.0)
process.selectionSequenceUCEUp     = createSystematics(process,process.selectionSequence,'UCEUp'   ,1.00, 1.0, 1.0, 0, 1.1)
process.selectionSequenceUCEDown   = createSystematics(process,process.selectionSequence,'UCEDown' ,1.00, 1.0, 1.0, 0, 0.9)

process.eventSelectionMuonUp    =  cms.Path(process.selectionSequenceMuonUp)
process.eventSelectionMuonDown  =  cms.Path(process.selectionSequenceMuonDown)
process.eventSelectionJetUp     =  cms.Path(process.selectionSequenceJetUp)
process.eventSelectionJetDown   =  cms.Path(process.selectionSequenceJetDown)
process.eventSelectionUCEUp     =  cms.Path(process.selectionSequenceUCEUp)
process.eventSelectionUCEDown   =  cms.Path(process.selectionSequenceUCEDown)

from UWAnalysis.Configuration.tools.ntupleToolsPTwbb import *
addMuNuEventTreePtMC(process,'muNuEventTree',lhep="source")
addEventSummary(process,True)

addMuNuEventTreePtMC(process,'muNuEventTreeMuonUp',   'wCandsJetsMuonUp',   'diMuonsSortedMuonUp',   lhep="source")
addMuNuEventTreePtMC(process,'muNuEventTreeMuonDown', 'wCandsJetsMuonDown', 'diMuonsSortedMuonDown', lhep="source")
addMuNuEventTreePtMC(process,'muNuEventTreeJetUp',    'wCandsJetsJetUp',    'diMuonsSortedJetUp',    lhep="source")
addMuNuEventTreePtMC(process,'muNuEventTreeJetDown',  'wCandsJetsJetDown',  'diMuonsSortedJetDown',  lhep="source")
addMuNuEventTreePtMC(process,'muNuEventTreeUCEUp',    'wCandsJetsUCEUp',    'diMuonsSortedUCEUp',    lhep="source")
addMuNuEventTreePtMC(process,'muNuEventTreeUCEDown',  'wCandsJetsUCEDown',  'diMuonsSortedUCEDown',  lhep="source")
process.TFileService.fileName = cms.string('W4Jet.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
