import FWCore.ParameterSet.Config as cms
import sys
from FWCore.ParameterSet.VarParsing import VarParsing

sys.setrecursionlimit(10000)

process = cms.Process("ANALYSIS")

process.load('Configuration/StandardSequences/FrontierConditions_GlobalTag_cff')
process.GlobalTag.globaltag = 'START53_V27::All' # for global tag with re-reco data

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

process.source = cms.Source("PoolSource",
 fileNames = cms.untracked.vstring(
#"file:///afs/hep.wisc.edu/cms/tperry/FSAv2_CMSSW_5_3_14/src/FinalStateAnalysis/PatTools/test/SKIMTEST_W2Jet_p2-64628488-9FE4-E211-96FF-0026189438D5.root"
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1Jet_p1_s-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-00035FC4-C903-E211-BB66-003048D477C2.root",
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-002D70FC-7F84-E211-A7E6-782BCB6E0938.root" # "source"

#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-84403EFB-54CE-E111-BF8A-001E673969FF.root" # "source"
#"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-00065798-2704-E211-B308-0025901D4C44.root" # "source"
#"root://cmsxrootd.hep.wisc.edu//hdfs/store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-4C1B8B0D-4603-E211-8B77-002590200B60.root" # "source"
"root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2Jet_p2_l-skimpattuple_cfg/skimpattuple_cfg-patTuple_cfg-004CD553-7BE4-E211-ADFB-0026189438A9.root"

# synch files
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-02CCD580-BA87-E211-93B5-842B2B185476.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-00277FF2-7B84-E211-9475-782BCB27B958.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-5ACBC7A4-7D84-E211-A0B6-782BCB27B958.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-AED5F4C3-6E84-E211-B83B-0002C90EEE6E.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-002D70FC-7F84-E211-A7E6-782BCB6E0938.root", 
#"root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1/patTuple_cfg-5ADB775B-A284-E211-B0A2-90B11C18B19E.root", 
 ),
 inputCommands=cms.untracked.vstring(
  'keep *',
  'drop *_finalState*_*_*',
  'drop *_patFinalStateEvent*_*_*'
 )
)

process.load("FWCore.MessageLogger.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 100

# RECO LEVEL
process.load("PhysicsTools.PatAlgos.patSequences_cff")
from UWAnalysis.Configuration.tools.analysisToolsPT import *

defaultReconstructionPT(process,
 'HLT',
 ['HLT_IsoMu24_eta2p1_v','HLT_Ele27_WP80'],
 itsMC=True,itsData=False,lhep_="externalLHEProducer")

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

process.load("UWAnalysis.Configuration.countSmearEvents_cff")
process.eventSelection = cms.Path(process.selectionSequence) ##changing to multiples see below

# createSystematics in analysisToolsPT
process.selectionSequenceMuonUp    = createSystematics(process,process.selectionSequence,'MuonUp'  ,1.01, 1.0, 1.0, 0, 1.0)
process.selectionSequenceMuonDown  = createSystematics(process,process.selectionSequence,'MuonDown',0.99, 1.0, 1.0, 0, 1.0)
process.selectionSequenceElectronUp    = createSystematics(process,process.selectionSequence,'ElectronUp'  ,1.0, 1.01, 1.0, 0, 1.0)
process.selectionSequenceElectronDown  = createSystematics(process,process.selectionSequence,'ElectronDown',1.0, 0.99, 1.0, 0, 1.0)
process.selectionSequenceJetUp     = createSystematics(process,process.selectionSequence,'JetUp'   ,1.00, 1.0, 1.0, 1, 1.0)
process.selectionSequenceJetDown   = createSystematics(process,process.selectionSequence,'JetDown' ,1.00, 1.0, 1.0,-1, 1.0)

process.eventSelectionMuonUp    =  cms.Path(process.selectionSequenceMuonUp)
process.eventSelectionMuonDown  =  cms.Path(process.selectionSequenceMuonDown)
process.eventSelectionJetUp     =  cms.Path(process.selectionSequenceJetUp)
process.eventSelectionJetDown   =  cms.Path(process.selectionSequenceJetDown)

# GEN LEVEL
options = VarParsing ('analysis')
options.outputFile = "2.root"
options.register(
    'CrossSection',
#    12234.4*3*0.05626,
        46.3*3,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "CrossSection")

options.register(
    'selectNUP',
    -1, 
    VarParsing.multiplicity.singleton,
    VarParsing.varType.int,
    "selectNUP")

options.parseArguments()

from RecoJets.JetProducers.GenJetParameters_cfi import *
from RecoJets.JetProducers.AnomalousCellParameters_cfi import *

process.load("RecoJets.Configuration.GenJetParticles_cff")
process.load("RecoJets.JetProducers.ak5GenJets_cfi")

process.genParticlesNoNeutrinos = cms.EDProducer("GenParticlePruner",
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
        "drop  *", # this is the default
        "keep status = 1 ",
        "drop abs(pdgId) = 12", "drop abs(pdgId) = 14", "drop abs(pdgId) = 16" 
    )   
)

process.neutrinos = cms.EDProducer("GenParticlePruner",
    src = cms.InputTag("genParticles"),
    select = cms.vstring(
        "drop  *", # this is the default
        "keep abs(pdgId) = 12 & status =1 ", "keep abs(pdgId) = 14 & status =  1", "keep abs(pdgId) = 16 & status = 1"
    )
)

process.GenJetParameters.src=cms.InputTag("genParticlesNoNeutrinos")

process.ak5GenJetsNoNu = cms.EDProducer(
     "FastjetJetProducer",
     GenJetParameters,
     AnomalousCellParameters,
     jetAlgorithm = cms.string("AntiKt"),
     rParam       = cms.double(0.5)
     )

process.partonJetsSeq=cms.Sequence(process.genParticlesNoNeutrinos*process.ak5GenJetsNoNu*process.neutrinos)

process.LHEFilter = cms.EDFilter("GenFilterLHE",
        PartonMultiplicity=cms.untracked.int32(0),
        PartonMultiplicityMAX=cms.untracked.int32(20),
)

# Produce PDF weights (maximum is 3)
process.pdfWeights = cms.EDProducer("PdfWeightProducer",
      # Fix MADGRAPH if buggy (this PDF set will also appear on output, 
      # so only two more PDF sets can be added in PdfSetNames if not "")
      FixMADGRAPH = cms.untracked.int32(3),
      GenTag = cms.untracked.InputTag("genParticles"),
      PdfInfoTag = cms.untracked.InputTag("generator"),
      PdfSetNames = cms.untracked.vstring(
             "CT10.LHgrid",
#             "MSTW2008nlo68cl.LHgrid",
#             "cteq66.LHgrid",
             "MSTW2008nnlo68cl.LHgrid",
             "cteq6ll.LHpdf" ,
      )
)

process.bhadrons = cms.EDProducer('MCBHadronProducer',
                                  quarkId = cms.uint32(5)
                                  )

process.btaggedGenJets= cms.EDProducer('GENJetBtagger',
                                src=cms.InputTag("ak5GenJetsNoNu"),
                                srcSIMB=cms.InputTag("bhadrons")
)

process.cleanGenJets= cms.EDProducer('GenJetCleaner',
                                src=cms.InputTag("btaggedGenJets"),
                                srcDressedLepton=cms.InputTag("dressedLeptons"),
                                onlyGoodLeptons=cms.bool(True)
)

process.dressedLeptons = cms.EDProducer("DressedGenLeptonsProducer",
                                src= cms.InputTag("genParticles"),
#                                genPDGID= cms.untracked.int32(0), # 0 --> muons and electrons,  13 --> muons  11--> electrons
#                                genSTATUS= cms.untracked.int32(1)
                                 minPT = cms.untracked.double(0),
                                 maxETA = cms.untracked.double(10),
)


process.cleanGenJetsAndrea= cms.EDProducer('GenJetCleaner',
                                src=cms.InputTag("btaggedGenJets"),
                                srcDressedLepton=cms.InputTag("dressedLeptons"),
                                onlyGoodLeptons=cms.bool(False),
                                excludeTaus=cms.untracked.bool(True)
)


process.Filter=cms.Sequence(process.partonJetsSeq*process.dressedLeptons*process.bhadrons*process.btaggedGenJets*process.cleanGenJets*process.cleanGenJetsAndrea*process.LHEFilter)#*process.pdfWeights)
process.eventSelectionMC = cms.Path(process.Filter) ##changing to multiples see below

process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")
process.printTree = cms.EDAnalyzer("ParticleListDrawer",
  maxEventsToPrint = cms.untracked.int32(1),
  printVertex = cms.untracked.bool(False),
  src = cms.InputTag("genParticles")
)

#process.list=cms.Path(process.printTree)



process.crossSectionJet25Lepton30=cms.EDFilter("GenStudy",
      DressedLepton=cms.untracked.InputTag("dressedLeptons"),
      Jets=cms.untracked.InputTag("cleanGenJets"),
      SIMB=cms.untracked.InputTag("bhadrons"),
      Neutrinos=cms.untracked.InputTag("neutrinos"),
      filterByNUP=cms.untracked.int32(options.selectNUP),
      selLeptonPDGID=cms.untracked.int32(13),
      ptCutJetis=cms.untracked.double(25),
      ptCutLepton=cms.untracked.double(30),
      inputCrossSection=cms.untracked.double(options.CrossSection)
)

process.crossSectionJet25Lepton30Andrea=cms.EDFilter("GenStudyAndrea",
      DressedLepton=cms.untracked.InputTag("dressedLeptons"),
      Jets=cms.untracked.InputTag("cleanGenJets"),
      SIMB=cms.untracked.InputTag("bhadrons"),
      Neutrinos=cms.untracked.InputTag("neutrinos"),
      filterByNUP=cms.untracked.int32(options.selectNUP),
      selLeptonPDGID=cms.untracked.int32(13),
      ptCutJetis=cms.untracked.double(25),
      ptCutLepton=cms.untracked.double(30),
      inputCrossSection=cms.untracked.double(options.CrossSection)
)

process.eventSelectionMC = cms.Path(process.Filter*process.crossSectionJet25Lepton30Andrea)



from UWAnalysis.Configuration.tools.ntupleToolsPTwbbClean import *
addEventTreeMC(process,'muEleEventTree',
      srcGMu='smearedGoodMuons',
      srcVMu='smearedVetoMuons',
      srcQMu='smearedQCDMuons',
      srcAMu='smearedAllMuons',
      srcGEle='smearedGoodElectrons',
      srcVEle='smearedVetoElectrons',
      srcQEle='smearedQCDElectrons',
      srcAEle='smearedAllElectrons',
      srcGJet='smearedGoodJets',
      srcFJet='smearedFwdJets',
      srcAJet='smearedAllJets',
      srcCJet='smearedCleanJets',
      lhep="externalLHEProducer",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

addEventSummary(process,True)

addEventTreeMC(process,'muEleEventTreeJetUp',
      srcGMu='smearedGoodMuonsJetUp',
      srcVMu='smearedVetoMuonsJetUp',
      srcQMu='smearedQCDMuonsJetUp',
      srcAMu='smearedAllMuonsJetUp',
      srcGEle='smearedGoodElectronsJetUp',
      srcVEle='smearedVetoElectronsJetUp',
      srcQEle='smearedQCDElectronsJetUp',
      srcAEle='smearedAllElectronsJetUp',
      srcGJet='smearedGoodJetsJetUp',
      srcFJet='smearedFwdJetsJetUp',
      srcAJet='smearedAllJetsJetUp',
      srcCJet='smearedCleanJetsJetUp',
      lhep="externalLHEProducer",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

addEventTreeMC(process,'muEleEventTreeJetDown',
      srcGMu='smearedGoodMuonsJetDown',
      srcVMu='smearedVetoMuonsJetDown',
      srcQMu='smearedQCDMuonsJetDown',
      srcAMu='smearedAllMuonsJetDown',
      srcGEle='smearedGoodElectronsJetDown',
      srcVEle='smearedVetoElectronsJetDown',
      srcQEle='smearedQCDElectronsJetDown',
      srcAEle='smearedAllElectronsJetDown',
      srcGJet='smearedGoodJetsJetDown',
      srcFJet='smearedFwdJetsJetDown',
      srcAJet='smearedAllJetsJetDown',
      srcCJet='smearedCleanJetsJetDown',
      lhep="externalLHEProducer",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

addEventTreeMC(process,'muEleEventTreeMuonUp',
      srcGMu='smearedGoodMuonsMuonUp',
      srcVMu='smearedVetoMuonsMuonUp',
      srcQMu='smearedQCDMuonsMuonUp',
      srcAMu='smearedAllMuonsMuonUp',
      srcGEle='smearedGoodElectronsMuonUp',
      srcVEle='smearedVetoElectronsMuonUp',
      srcQEle='smearedQCDElectronsMuonUp',
      srcAEle='smearedAllElectronsMuonUp',
      srcGJet='smearedGoodJetsMuonUp',
      srcFJet='smearedFwdJetsMuonUp',
      srcAJet='smearedAllJetsMuonUp',
      srcCJet='smearedCleanJetsMuonUp',
      lhep="externalLHEProducer",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

addEventTreeMC(process,'muEleEventTreeMuonDown',
      srcGMu='smearedGoodMuonsMuonDown',
      srcVMu='smearedVetoMuonsMuonDown',
      srcQMu='smearedQCDMuonsMuonDown',
      srcAMu='smearedAllMuonsMuonDown',
      srcGEle='smearedGoodElectronsMuonDown',
      srcVEle='smearedVetoElectronsMuonDown',
      srcQEle='smearedQCDElectronsMuonDown',
      srcAEle='smearedAllElectronsMuonDown',
      srcGJet='smearedGoodJetsMuonDown',
      srcFJet='smearedFwdJetsMuonDown',
      srcAJet='smearedAllJetsMuonDown',
      srcCJet='smearedCleanJetsMuonDown',
      lhep="externalLHEProducer",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

addEventTreeMC(process,'muEleEventTreeElectronUp',
      srcGMu='smearedGoodMuonsElectronUp',
      srcVMu='smearedVetoMuonsElectronUp',
      srcQMu='smearedQCDMuonsElectronUp',
      srcAMu='smearedAllMuonsElectronUp',
      srcGEle='smearedGoodElectronsElectronUp',
      srcVEle='smearedVetoElectronsElectronUp',
      srcQEle='smearedQCDElectronsElectronUp',
      srcAEle='smearedAllElectronsElectronUp',
      srcGJet='smearedGoodJetsElectronUp',
      srcFJet='smearedFwdJetsElectronUp',
      srcAJet='smearedAllJetsElectronUp',
      srcCJet='smearedCleanJetsElectronUp',
      lhep="source",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

addEventTreeMC(process,'muEleEventTreeElectronDown',
      srcGMu='smearedGoodMuonsElectronDown',
      srcVMu='smearedVetoMuonsElectronDown',
      srcQMu='smearedQCDMuonsElectronDown',
      srcAMu='smearedAllMuonsElectronDown',
      srcGEle='smearedGoodElectronsElectronDown',
      srcVEle='smearedVetoElectronsElectronDown',
      srcQEle='smearedQCDElectronsElectronDown',
      srcAEle='smearedAllElectronsElectronDown',
      srcGJet='smearedGoodJetsElectronDown',
      srcFJet='smearedFwdJetsElectronDown',
      srcAJet='smearedAllJetsElectronDown',
      srcCJet='smearedCleanJetsElectronDown',
      lhep="source",
      srcGenParticles="genParticles",
      srcGenLep="dressedLeptons",
      srcTaggedGenJets="btaggedGenJets"
      )

process.TFileService.fileName = cms.string('BastilleTest_l.root') 

## makes EDM output of all collections
#process.out = cms.OutputModule("PoolOutputModule",
# fileName = cms.untracked.string('/scratch/tperry/analysis.root'),
# outputCommands = cms.untracked.vstring(
#                       'keep *'),
# )
#process.e = cms.EndPath(process.out)
#
#Pax = open("myConfig.py","w")
#Pax.write(process.dumpPython())
