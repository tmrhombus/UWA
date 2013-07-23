import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V27::All' #START52_V9

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
  # $inputFileNames
  'root://cmsxrootd.hep.wisc.edu//store/user/swanson/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/TTBAR/patTuple_cfg-A25A5BAE-E598-E211-ACC8-0025905964BE.root'
  #'root://cmsxrootd.hep.wisc.edu//store/user/swanson/TTBar_LL-SUB-MC/SUB-MC-patTuple_cfg-FE19EA66-3398-E211-A88B-003048FFD71A.root'
  #'root://cmsxrootd.hep.wisc.edu//store/user/swanson/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_v1_WJets8TeV-9ec8fe3/304ffda35e6a6d2ac3103ac6153835e2/output_1000_2_wBh.root'
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

defaultReconstructionPTMC(process,
 'HLT',
 ['HLT_IsoMu24_eta2p1_v','HLT_Mu40_eta2p1_v']
)



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
process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.selectionSequence) ##changing to multiples see below
process.eventSelectionMuonUp    = createSystematics(process,process.selectionSequence,'MuonUp',1.01,1.0,1.0,0,1.0)
process.eventSelectionMuonDown  = createSystematics(process,process.selectionSequence,'MuonDown',0.99,1.0,1.0,0,1.0)
process.eventSelectionJetUp     = createSystematics(process,process.selectionSequence,'JetUp',1.00,1.0,1.0,1,1.0)
process.eventSelectionJetDown   = createSystematics(process,process.selectionSequence,'JetDown',1.0,1.0,1.0,-1,1.0)
process.eventSelectionUCEUp     = createSystematics(process,process.selectionSequence,'UCEUp',1.00,1.0,1.0,0,1.1)
process.eventSelectionUCEDown   = createSystematics(process,process.selectionSequence,'UCEDown',1.0,1.0,1.0,0,0.9)

from UWAnalysis.Configuration.tools.ntupleToolsPT import *
addMuNuEventTreePt(process,'muNuEventTree')
#addMuNuEventTreePtPlot(process,'muNuEventTreePlot')
addEventSummary(process,True)

addMuNuEventTreePt(process,'muNuEventTreeMuonUp','wCandsJetsMuonUp','diMuonsSortedMuonUp')
addMuNuEventTreePt(process,'muNuEventTreeMuonDown','wCandsJetsMuonDown','diMuonsSortedMuonDown')
addMuNuEventTreePt(process,'muNuEventTreeJetUp','wCandsJetsJetUp','diMuonsSortedJetUp')
addMuNuEventTreePt(process,'muNuEventTreeJetDown','wCandsJetsJetDown','diMuonsSortedJetDown')
addMuNuEventTreePt(process,'muNuEventTreeJetUp','wCandsJetsUCEUp','diMuonsSortedUCEUp')
addMuNuEventTreePt(process,'muNuEventTreeJetDown','wCandsJetsUCEDown','diMuonsSortedUCEDown')
process.TFileService.fileName = cms.string('analysis.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
