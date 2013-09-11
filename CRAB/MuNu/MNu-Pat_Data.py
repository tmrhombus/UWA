import FWCore.ParameterSet.Config as cms
import sys
sys.setrecursionlimit(1000)
process = cms.Process("ANALYSIS")
process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'FT_53_V21_AN6::All' #new GT
#process.GlobalTag.globaltag = 'GR_P_V40_AN1::All' #old GT

process.maxEvents = cms.untracked.PSet(
 input = cms.untracked.int32(1000)
)

process.load("UWAnalysis/Configuration/2012FullJSON")
process.source.fileNames= cms.untracked.vstring(
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

#defaultReconstructionPTDataABC(process,'HLT',['HLT_IsoMu24_eta2p1_v'
#                                      #'HLT_Mu40_eta2p1_v'
#                                       ])

defaultReconstructionPT(process,'HLT',['HLT_IsoMu24_eta2p1_v'],
                        itsMC=False,itsData=True)
global metCalibration

#process.metCalibration.applyCalibration = cms.bool(True)

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

#EventSelection

process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.selectionSequence) ##changing to multiples see below

#from UWAnalysis.Configuration.tools.ntupleToolsPT import *
from UWAnalysis.Configuration.tools.ntupleToolsPTwbb import *

addMuNuEventTreePtDat(process,'muNuEventTree')
addEventSummary(process,True)
process.TFileService.fileName = cms.string('data.root')
#addMuNuEventTreePtPlot(process,'muNuEventTreePlot')

#process.TFileService.fileName=cms.string("$outputFileName")
