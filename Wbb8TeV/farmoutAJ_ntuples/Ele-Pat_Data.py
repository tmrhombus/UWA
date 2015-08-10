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
#'file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/data_Cut5_00176847-0073-E211-9FFE-0030487DE7C5.root'
#'file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/data_FullOut_00176847-0073-E211-9FFE-0030487DE7C5.root'
#'file:///nfs_scratch/taroni/prova.root'
#'file:///hdfs/store/user/taroni/SingleElectron/Run2012A-22Jan2013-v1/AOD/Fall2014PATTuples_V1/patTuple_cfg-00176847-0073-E211-9FFE-0030487DE7C5.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/taroni/SingleElectron/Run2012C-22Jan2013-v1/AOD/Fall2014PATTuples_V1/patTuple_cfg-0000284C-308B-E211-90D5-003048FEB8AE.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/TEST3_DataA_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-00176847-0073-E211-9FFE-0030487DE7C5.root'

#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataA_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-44A90D36-9B72-E211-BFBF-002481E0D50C.root',
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataB_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-B017536D-7D7F-E211-85FA-003048F16F9C.root',
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataC_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-2A57BDF5-E984-E211-A19A-003048FEADCC.root',
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataD_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-0076C476-BE92-E211-9437-002354EF3BE3.root',
'root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataD_8TeVEle-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-D6E0E8C3-8695-E211-B77E-0025905964B4.root',

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
process.TFileService.fileName = cms.string('V1_DataD_Ele_D6E0E8C3-8695-E211-B77E-0025905964B4.root')

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/data.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
