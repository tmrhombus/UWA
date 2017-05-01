import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(1000)
process = cms.Process("ANALYSIS")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'FT_53_V21_AN6::All' #new GT

process.maxEvents = cms.untracked.PSet(
 input = cms.untracked.int32(-1)
)

process.load("UWAnalysis/Configuration/2012FullJSON")
#import FWCore.PythonUtilities.LumiList as LumiList
#process.source.lumisToProcess = LumiList.LumiList(filename = '/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/weights/Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.json').getVLuminosityBlockRange()

process.source.fileNames= cms.untracked.vstring(
## Electron Data
 "file:///hdfs/store/user/tperry/PatTuples_8TeV/DataD_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-8032822F-F693-E211-99A5-003048678B12.root"
 #"file:///hdfs/store/user/tuanqui/DataD_8TeV_skimpattuple-skimpattuple_cfg/skimpattuple_cfg-skimpattuple_cfg-patTuple_cfg-8032822F-F693-E211-99A5-003048678B12.root"
#
)
process.source.inputCommands=cms.untracked.vstring(
 'keep *', 'drop *_finalState*_*_*',
 'drop *_patFinalStateEvent*_*_*'
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.cerr.FwkReport.reportEvery = 100000

process.load("PhysicsTools.PatAlgos.patSequences_cff")
from UWAnalysis.Configuration.tools.analysisToolsPT import *

defaultReconstructionPT(process,'HLT',
                        ['HLT_IsoMu24_eta2p1_v','HLT_Ele27_WP80'],
                        itsMC=False,itsData=True)

process.load("UWAnalysis.Configuration.countEvents_cff")
process.eventSelection = cms.Path(process.selectionSequence) 

from UWAnalysis.Configuration.tools.ntupleToolsPTwbbClean import *

addEventTreeData(process,'electronEventTree',
      'goodElectrons',
      'qcdElectrons',
      srcGMu='goodMuons',
      srcVMu='vetoMuons',
      srcQMu='qcdMuons',
      srcAMu='allMuons',
      srcGEle='goodElectrons',
      srcVEle='vetoElectrons',
      srcQEle='qcdElectrons',
      srcAEle='allElectrons',
      srcGJet='goodJets',
      srcFJet='fwdJets',
      srcAJet='allJets',
      srcCJet='cleanJets'
   )   
addEventSummary(process,True)
process.TFileService.fileName = cms.string('Full_Ele_8032822F-F693-E211-99A5-003048678B12.root')

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/data.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
