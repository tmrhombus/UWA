import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")


process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V10::All' 

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
    'root://cmsxrootd.hep.wisc.edu//store/user/tapas/2012-09-18-8TeV-53X-PatTuple/ZZJetsTo2L2Q_TuneZ2star_8TeV-madgraph-tauola/1/patTuple_cfg-C4E6DFFC-A7D8-E111-9C62-001A645BF218.root'


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



#createGeneratedParticles(process,
#                         'genWs',
#                          [
#                           "keep++ pdgId = {Z}"
#                          ]
#)

process.load("UWAnalysis.Configuration.BASE_cff")

process.eventSelection = cms.Path(process.selectionSequence) 
process.eventSelectionMuonUp    = createSystematics(process,process.selectionSequence,'MuonUp',1.01,1.0,1.0,0,1.0)
process.eventSelectionMuonDown  = createSystematics(process,process.selectionSequence,'MuonDown',0.99,1.0,1.0,0,1.0)


from UWAnalysis.Configuration.tools.ntupleToolsPT import *

addBASEEventTree(process,'BASEEventTree')
addEventSummary(process,True)

addBASEEventTree(process,'BASEEventTreeMuonUp','BASEMuonUp','BASE2MuonUp')
addBASEEventTree(process,'BASEEventTreeMuonDown','BASEMuonDown','BASE2MuonDown')



