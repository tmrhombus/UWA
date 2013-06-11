import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")


process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V10::All' #START52_V9

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
                   # $inputFileNames
    #'root://cmsxrootd.hep.wisc.edu//store/user/tapas/2012-08-30-8TeV-PatTuple/data_SingleMu_Run2012C_PromptReco_v2_Run198934_201264/9/patTuple_cfg-FAC8CABE-47D8-E111-A6E0-003048F024FE.root',
    #'/store/user/friis/TTJets_TuneZ2star_8TeV-madgraph-tauola/TTplusJets_madgraph_2012-05-28-8TeV-PatTuple-8a107b9/4729152ae17d7e4009729a1d0d9e952d/output_30_1_0T5.root',

#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/Tbar_t-channel_TuneZ2star_8TeV-powheg-tauola/Tbar_t_powheg_tauola_2012-07-06-8TeV-PatTuple-4c0a0c1/d0c3c22b2afca27fe5c9667f3986711f/output_86_2_80X.root'
# 'root://cmsxrootd.hep.wisc.edu//store/user/tapas/2012-09-18-8TeV-53X-PatTuple/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_v2/patTuple_cfg-82CEACD1-EEEF-E111-B840-001E6739850C.root'
 'root://cmsxrootd.hep.wisc.edu//store/user/swanson/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball_v1_WJets8TeV-9ec8fe3/304ffda35e6a6d2ac3103ac6153835e2/output_1000_2_wBh.root'
#
        ),
        inputCommands=cms.untracked.vstring(
						'keep *',
						'drop *_finalState*_*_*',
						'drop *_patFinalStateEvent*_*_*'
		)
)

process.load("PhysicsTools.PatAlgos.patSequences_cff")
from UWAnalysis.Configuration.tools.analysisToolsPT import *
defaultReconstructionPTMC(process,'HLT',['HLT_IsoMu24_eta2p1_v',
                                      'HLT_Mu40_eta2p1_v'
                                      ])



createGeneratedParticles(process,
                         'genWs',
                          [
                           "keep++ pdgId = {W+}",
                           "keep++ pdgId = {W-}"
                          ]
)
createGeneratedParticles(process,
                         'genbbCands',
                          [
                           "keep abs(pdgId) = 5"
                          ]
)

createGeneratedParticles(process,
                          'genbbCandsMinus',
                           [
                            "keep pdgId = -5" 
                           ]
)

createGeneratedParticles(process,
                          'genccCands',
                           [
                            "keep abs(pdgId) = 4" 
                           ]
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



