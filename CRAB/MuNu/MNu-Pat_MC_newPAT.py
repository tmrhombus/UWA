import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V27::All' # for global tag with re-reco data

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(1000)
)

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
   #$inputFileNames
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-80136C46-8FE1-E211-BA7E-00266CFEFC5C.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-04557220-78E4-E211-8C2D-003048FFD7BE.root' 
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTupleV2/patTuple_cfg-F8EF9511-5BEF-E211-92AA-0030487E5399.root'

#"file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/w1jet_v2.root"
#"file:///afs/hep.wisc.edu/cms/mcepeda/UpdateRecipe/patupleProdMarch14Ori/src/FinalStateAnalysis/PatTools/test/output2.root"
#"file:///afs/hep.wisc.edu/cms/tperry/FSAv3_slc6_472_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/output.root"

#'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root'
#'file:///hdfs/store/user/mcepeda/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/Spring2014PATTuples/patTuple_cfg-529DE452-5798-E211-9D62-0026189438B1.root' 
#"file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/mc.root"

#synch TTbarMC
"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root",
"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-5ACBC7A4-7D84-E211-A0B6-782BCB27B958.root",
"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-AED5F4C3-6E84-E211-B83B-0002C90EEE6E.root",
"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-002D70FC-7F84-E211-A7E6-782BCB6E0938.root",
"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-5ADB775B-A284-E211-B0A2-90B11C18B19E.root"
 ),
 inputCommands=cms.untracked.vstring(
  'keep *',
  'drop *_finalState*_*_*',
  'drop *_patFinalStateEvent*_*_*'
 )
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.cerr.FwkReport.reportEvery = 1000000

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

process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.selectionSequence) ##changing to multiples see below

# createSystematics in analysisToolsPT
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
addMuNuEventTreePtMC(process,'muNuEventTree',lhep="externalLHEProducer")

addEventSummary(process,True)

addMuNuEventTreePtMC(process,'muNuEventTreeMuonUp',   'wCandsJetsMuonUp',   'diMuonsSortedMuonUp',   lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeMuonDown', 'wCandsJetsMuonDown', 'diMuonsSortedMuonDown', lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeJetUp',    'wCandsJetsJetUp',    'diMuonsSortedJetUp',    lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeJetDown',  'wCandsJetsJetDown',  'diMuonsSortedJetDown',  lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeUCEUp',    'wCandsJetsUCEUp',    'diMuonsSortedUCEUp',    lhep="externalLHEProducer")
addMuNuEventTreePtMC(process,'muNuEventTreeUCEDown',  'wCandsJetsUCEDown',  'diMuonsSortedUCEDown',  lhep="externalLHEProducer")

#process.TFileService.fileName = cms.string('metCalibFalse.root') 
process.TFileService.fileName = cms.string('numbertest_a.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
