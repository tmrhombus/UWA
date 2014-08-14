import FWCore.ParameterSet.Config as cms

#Import tool that creates the cut sequence
from UWAnalysis.Configuration.tools.CutSequenceProducer import *

analysisConfigurator = CutSequenceProducer(initialCounter = 'initialEvents',
                                  pyModuleName = __name__,
                                  pyNameSpace = locals())

#analysisConfigurator.addSmearing('patOverloadedTaus','cleanPatMuons','cleanPatElectrons','cleanPatJets','patType1CorrectedPFMet')
#analysisConfigurator.addSmearing('patOverloadedTaus','cleanPatMuons','cleanPatElectrons','cleanPatJets','metTypeOne')
#analysisConfigurator.addSmearing('patOverloadedTaus','rochCorMuons','cleanPatElectrons','cleanPatJets','metTypeOne')
# in use
#analysisConfigurator.addSmearing('patOverloadedTaus','selectedPatMuons','selectedPatElectrons','cleanPatJets','metTypeOne')
# try new met
#analysisConfigurator.addSmearing('patOverloadedTaus','selectedPatMuons','selectedPatElectrons','cleanPatJets','pfMetT1')
analysisConfigurator.addSmearing('patOverloadedTaus','selectedPatMuons','selectedPatElectrons','cleanPatJets','patType1CorrectedPFMet')

DiMuonPreSel='leg1.isGlobalMuon && leg1.isTrackerMuon && leg2.isGlobalMuon && leg2.isTrackerMuon && leg1.pt()>20 && leg2.pt()>20 && leg1.charge * leg2.charge<0'
DiMuonPreSel2='(leg1.isolationR03().sumPt+leg1.isolationR03().emEt+leg1.isolationR03().hadEt)/leg1.pt()<0.15 '
DiMuonPreSel3='(leg2.isolationR03().sumPt+leg2.isolationR03().emEt+leg2.isolationR03().hadEt)/leg2.pt()<0.15 '

#Make Di Muons to VETO DY
analysisConfigurator.addDiCandidateModule('diMuons','PATMuPairProducer', 'smearedMuons','smearedMuons','smearedMET','smearedJets',0,9999,text = '',leadingObjectsOnly = True,dR = 0.15,recoMode = "")
analysisConfigurator.addSelector('diMuonsSel','PATMuPairSelector',DiMuonPreSel+'&&'+DiMuonPreSel2+'&&'+DiMuonPreSel3,'diMuonSel',0,999)
analysisConfigurator.addSorter('diMuonsSorted','PATMuPairSorter')

##Make Electrons+MET cleanPatJets
#analysisConfigurator.addCandidateMETModule('weCands','PATElectronNuPairProducer','smearedElectrons','smearedMET','smearedJets',0,9999,'weCandidate',genParticles='genDaughters')
#analysisConfigurator.addSelector('weCandsKin','PATElectronNuPairSelector','','weCandsKin',0,999)
##analysisConfigurator.addSelector('weCandsKin','PATElectronNuPairSelector','lepton.pt()>27 && abs(lepton.eta()) < 1.5','weCandsKin',0,999)
#analysisConfigurator.addSelector('weCandsJets','PATElectronNuPairSelector','','weCandsSel',0,999)

#Make Muons+MET cleanPatJets
analysisConfigurator.addCandidateMETModule('wCands','PATMuonNuPairProducer','smearedMuons','smearedMET','smearedJets',0,9999,'AtLeastOneWCandidate',genParticles="genDaughters")

analysisConfigurator.addSelector('wCandsKIN','PATMuonNuPairSelector','lepton.pt()>25 && abs(lepton.eta())<2.1' ,'wCandsKIN',1)
#analysisConfigurator.addSelector('wCandsKIN','PATMuonNuPairSelector','lepton.pt()>25 && abs(lepton.eta())<2.1 && lepton.userInt("tightID")==1' ,'wCandsKIN',1)
analysisConfigurator.addSelector('wCandsJets','PATMuonNuPairSelector','','wCandsSel',1)

selectionSequence = analysisConfigurator.returnSequence()
