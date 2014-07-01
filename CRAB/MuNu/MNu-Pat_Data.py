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
 #'root://cmsxrootd.hep.wisc.edu//store/user/mverzett/SingleMu/Run2012A-22Jan2013-v1/AOD/Spring2014PATTuples_v2/patTuple_cfg-589969E7-646F-E211-998B-1CC1DE1CEDB2.root'

# for synching
'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples/patTuple_cfg-000A8B8E-2875-E211-BC1E-00259073E3D6.root', 
'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples/patTuple_cfg-0012575F-4C75-E211-A333-00259073E4D6.root', 
'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples/patTuple_cfg-001833BF-0575-E211-B2C8-E0CB4E19F9AF.root', 
'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples/patTuple_cfg-001DD9EE-3975-E211-8FE1-90E6BA19A1FE.root', 
'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples/patTuple_cfg-002723BE-2575-E211-A28F-90E6BA19A231.root', 
'root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples/patTuple_cfg-0033FBE6-0E75-E211-91C6-00259073E4BE.root' 

#'file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/data.root'
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

process.findMuons = cms.EDFilter("PATMuonSelector",
                                           src = cms.InputTag("cleanPatMuons"),
                                           cut = cms.string('pt>25&&abs(eta)<2.1'),
                                           filter = cms.bool(False)
)

process.jetsFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("jetsETARED"),
                                minNumber = cms.uint32(1)
                             )

process.muonsFilter = cms.EDFilter("CandViewCountFilter",
                                src = cms.InputTag("findMuons"),
                                minNumber = cms.uint32(1)
                             )

process.jetsETARED = cms.EDProducer("PATJetCleaner",
   src = cms.InputTag("selectedPatJets"),
   preselection = cms.string('abs(eta)<3.&&pt>20&&userFloat("idLoose")>0'),
   checkOverlaps = cms.PSet(
       muons = cms.PSet(
        src = cms.InputTag("findMuons"),
        algorithm = cms.string("byDeltaR"),
        preselection = cms.string("pt>10&&isGlobalMuon&&isTrackerMuon&&(chargedHadronIso()+max(photonIso+neutralHadronIso(),0.0))/pt()<0.3"),
        deltaR = cms.double(0.5),
        checkRecoComponents = cms.bool(False),
        pairCut = cms.string(""),
        requireNoOverlaps = cms.bool(True),
       ),
       electrons = cms.PSet(
        src = cms.InputTag("cleanPatElectrons"),
        algorithm = cms.string("byDeltaR"),
        preselection = cms.string("pt>10&&(chargedHadronIso()+max(photonIso()+neutralHadronIso(),0.0))/pt()<0.3"),
        deltaR = cms.double(0.5),
        checkRecoComponents = cms.bool(False),
        pairCut = cms.string(""),
        requireNoOverlaps = cms.bool(True),
       ),
   ),
   finalCut = cms.string('')
)

process.preCleaning=cms.Sequence(process.findMuons*process.jetsETARED*process.jetsFilter*process.muonsFilter)

process.load("UWAnalysis.Configuration.wMuNuAnalysisPT_cff")
process.eventSelection = cms.Path(process.preCleaning*process.selectionSequence) 

from UWAnalysis.Configuration.tools.ntupleToolsPTwbb import *

addMuNuEventTreePtData(process,'muNuEventTree')
addEventSummary(process,True)
process.TFileService.fileName = cms.string('Data.root')

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/data.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
