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
 'root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples_v3/patTuple_cfg-F25282EE-2077-E211-B3C0-00261834B5AF.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples_v3/patTuple_cfg-2A4B3C43-C575-E211-8960-90E6BA0D09AD.root'
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

#from UWAnalysis.Configuration.tools.CutSequenceProducer import *
#
#analysisConfigurator = CutSequenceProducer(initialCounter = 'initialEvents',
#                                  pyModuleName = __name__,
#                                  pyNameSpace = locals())
#process.selectionSequence = analysisConfigurator.returnSequence()
#


process.load("UWAnalysis.Configuration.countEvents_cff")
process.eventSelection = cms.Path(process.selectionSequence) 

from UWAnalysis.Configuration.tools.ntupleToolsPTwbbClean import *
#
#addEventTreeData(process,'muonEventTree',
#      'smearedGoodMuons',
#      'smearedQCDMuons',
#      srcGMu='smearedGoodMuons',
#      srcVMu='smearedVetoMuons',
#      srcQMu='smearedQCDMuons',
#      srcAMu='smearedAllMuons',
#      srcGEle='smearedGoodElectrons',
#      srcVEle='smearedVetoElectrons',
#      srcQEle='smearedQCDElectrons',
#      srcAEle='smearedAllElectrons',
#      srcGJet='smearedGoodJets',
#      srcFJet='smearedFwdJets',
#      srcAJet='smearedAllJets',
#      srcCJet='smearedCleanJets'
#   )

addEventTreeData(process,'muonEventTree',
      'goodMuons',
      'qcdMuons',
      srcGMu='goodMuons',
      srcVMu='vetoMuons',
      srcQMu='qcdMuons',
      srcAMu='allMuons',
      srcGEle='goodElectrons',
      srcVEle='vetoElectrons',
      srcQEle='qcdElectrons',
      srcAEle='allElectrons',
      srcGJet='goodJets',
      srcFJet='smearedFwdJets',
      srcAJet='allJets',
      srcCJet='smearedCleanJets'
   )
addEventSummary(process,True)
process.TFileService.fileName = cms.string('Data_Mu_VVC.root')

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/data.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
