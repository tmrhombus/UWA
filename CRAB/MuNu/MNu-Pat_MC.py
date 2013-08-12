import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V27::All' 

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(100)
)

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
  # $inputFileNames
  #'root://cmsxrootd.hep.wisc.edu///store/user/tapas/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-E0F748E5-E8E0-E211-842E-1CC1DE046FB0.root'
  #'root://cmsxrootd.hep.wisc.edu//store/user/swanson/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/W2JetsToLNu_TuneZ2Star_8TeV-madgraph_WJets8TeV-9ec8fe3/1f55d8c665139ad478fb31eac9310214/output_2198_1_wmz.root'
  'root://cmsxrootd.hep.wisc.edu//store/user/swanson/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/TTBAR/patTuple_cfg-A25A5BAE-E598-E211-ACC8-0025905964BE.root'
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
process.eventSelectionMuonUp    = createSystematics(process,process.selectionSequence,'MuonUp',1.01,1.0,1.0,0,1.0)
process.eventSelectionMuonDown  = createSystematics(process,process.selectionSequence,'MuonDown',0.99,1.0,1.0,0,1.0)
process.eventSelectionJetUp     = createSystematics(process,process.selectionSequence,'JetUp',1.00,1.0,1.0,1,1.0)
process.eventSelectionJetDown   = createSystematics(process,process.selectionSequence,'JetDown',1.0,1.0,1.0,-1,1.0)
process.eventSelectionUCEUp     = createSystematics(process,process.selectionSequence,'UCEUp',1.00,1.0,1.0,0,1.1)
process.eventSelectionUCEDown   = createSystematics(process,process.selectionSequence,'UCEDown',1.0,1.0,1.0,0,0.9)

#from UWAnalysis.Configuration.tools.ntupleToolsPT import *
from UWAnalysis.Configuration.tools.ntupleToolsPTwbb import *
addMuNuEventTreePt(process,'muNuEventTree')
#addMuNuEventTreePtPlot(process,'muNuEventTreePlot')
addEventSummary(process,True)

addMuNuEventTreePt(process,'muNuEventTreeMuonUp','wCandsJetsMuonUp','diMuonsSortedMuonUp')
addMuNuEventTreePt(process,'muNuEventTreeMuonDown','wCandsJetsMuonDown','diMuonsSortedMuonDown')
addMuNuEventTreePt(process,'muNuEventTreeJetUp','wCandsJetsJetUp','diMuonsSortedJetUp')
addMuNuEventTreePt(process,'muNuEventTreeJetDown','wCandsJetsJetDown','diMuonsSortedJetDown')
addMuNuEventTreePt(process,'muNuEventTreeJetUp','wCandsJetsUCEUp','diMuonsSortedUCEUp')
addMuNuEventTreePt(process,'muNuEventTreeJetDown','wCandsJetsUCEDown','diMuonsSortedUCEDown')
process.TFileService.fileName = cms.string('analysis_nwb.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
