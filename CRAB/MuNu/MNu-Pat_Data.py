import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(1000)
process = cms.Process("ANALYSIS")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'FT_53_V21_AN6::All' #new GT
#process.GlobalTag.globaltag = 'GR_P_V40_AN1::All' #old GT

process.maxEvents = cms.untracked.PSet(
 input = cms.untracked.int32(100)
)

process.load("UWAnalysis/Configuration/2012FullJSON")
process.source.fileNames= cms.untracked.vstring(
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012C-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-BE363131-F777-E211-B6FD-90E6BA0D0989.root'
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012D-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-5E518B22-6987-E211-957B-00259073E324.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012D-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-5A70F673-988A-E211-AA1D-20CF305B04ED.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012D-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-5439930D-2A87-E211-8605-20CF305616E1.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012D-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-52DC95E8-7585-E211-9677-00259073E3FE.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012D-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-50B04B10-F187-E211-9229-001EC9D282A8.root' #is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012D-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-4E2784EC-3186-E211-A4D4-00259073E47E.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012B-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-CA359D13-A971-E211-A636-20CF3019DF03.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012B-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-46137865-0481-E211-B996-00259073E524.root' # is ok
#'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012A-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-B2C4A0A7-C96F-E211-8D86-0017A477042C.root' #bad file
'root://cmsxrootd.hep.wisc.edu//store/user/tapas/SingleMu/Run2012B-22Jan2013-v1/AOD/2013-06-25-8TeV-53X-PatTuple_Master/patTuple_cfg-FE73DA29-2472-E211-81BC-00261834B586.root'
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

defaultReconstructionPT(process,'HLT',['HLT_IsoMu24_eta2p1_v'],
                        itsMC=False,itsData=True)
global metCalibration

process.metCalibration = cms.PSet(
 applyCalibration = cms.bool(True),
 calibrationScheme = cms.string("OneLeg"),
 responseU1   = cms.string("1.33223-0.917782*x"),
 responseU2   = cms.string("-0.013"),
 resolutionU1 = cms.string("11.1566+0.0654529*x+0.000124436*x*x"),
 resolutionU2 = cms.string("11.1235+0.0449872*x-6.39822e-5*x*x"),
 responseMCU1   = cms.string("1.26247-0.950094*x"),
 responseMCU2   = cms.string("-0.00544907"),
 resolutionMCU1 = cms.string("10.6449+0.0436475*x+3.07554e-5*x*x"),
 resolutionMCU2 = cms.string("10.5649+0.0225853*x-5.81371e-5*x*x")
)

process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.selectionSequence) 

from UWAnalysis.Configuration.tools.ntupleToolsPTwbb import *

addMuNuEventTreePtData(process,'muNuEventTree')
addEventSummary(process,True)
process.TFileService.fileName = cms.string('data.root')

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/data.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
