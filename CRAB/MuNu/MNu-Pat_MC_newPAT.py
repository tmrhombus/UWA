import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V27::All' # for global tag with re-reco data

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(40)
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

#wbb 4flavor
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEDB7460-9B0D-E211-98E4-001E67398156.root"
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FED59502-1B0D-E211-BB50-D8D385FF4A7C.root"
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FECC1DD4-D80D-E211-88BA-001E673968A6.root"
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FECA6FC2-770D-E211-9105-001E67397094.root"
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEB6B2A5-870E-E211-A1FC-001E67396581.root"

#test of new v2c pats
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FED0991E-94CE-E111-84E9-003048673F2C.root", 

#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF7AC04-A9EE-E111-8FCD-0025B3E06484.root",
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF3D07A-A803-E211-8AB4-001E67397698.root", 
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEFD18A6-00E2-E211-A836-1CC1DE051028.root", 
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEFE64DC-3C05-E211-80E4-003048D438EA.root", 
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF3BE77-7CE4-E211-BB7A-002618FDA262.root", 
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEDEDCE3-0307-E211-BC69-003048D45FBA.root", 
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEF973CF-DCEE-E211-A115-00259081A2C8.root", 
#
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Spring2014PATTuples_v2c/patTuple_cfg-FEE65930-1407-E211-8EDF-003048678F6C.root", 

#synch TTbarMC
"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-5ACBC7A4-7D84-E211-A0B6-782BCB27B958.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-AED5F4C3-6E84-E211-B83B-0002C90EEE6E.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-002D70FC-7F84-E211-A7E6-782BCB6E0938.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Spring2014PATTuples/patTuple_cfg-5ADB775B-A284-E211-B0A2-90B11C18B19E.root"

#"file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/tt_14ocbr14_5ADB775B-A284-E211-B0A2-90B11C18B19E.root"
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

process.TFileService.fileName = cms.string('mc_testnoele01.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)

Pax = open("myConfig.py","w")
Pax.write(process.dumpPython())
