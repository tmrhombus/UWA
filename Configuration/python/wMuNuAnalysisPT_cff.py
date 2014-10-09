import FWCore.ParameterSet.Config as cms

#Import tool that creates the cut sequence
from UWAnalysis.Configuration.tools.CutSequenceProducer import *

analysisConfigurator = CutSequenceProducer(initialCounter = 'initialEvents',
                                  pyModuleName = __name__,
                                  pyNameSpace = locals())

## in use
analysisConfigurator.addSmearing('patOverloadedTaus','selectedPatMuons','selectedPatElectrons','cleanPatJets','metCorrected')

DiMuonPreSel='leg1.isGlobalMuon && leg1.isTrackerMuon && leg2.isGlobalMuon && leg2.isTrackerMuon && leg1.pt()>20 && leg2.pt()>20 && leg1.charge * leg2.charge<0'
DiMuonPreSel2='(leg1.isolationR03().sumPt+leg1.isolationR03().emEt+leg1.isolationR03().hadEt)/leg1.pt()<0.15 '
DiMuonPreSel3='(leg2.isolationR03().sumPt+leg2.isolationR03().emEt+leg2.isolationR03().hadEt)/leg2.pt()<0.15 '

#Make Di Muons to VETO DY
analysisConfigurator.addDiCandidateModule('diMuons','PATMuPairProducer', 'smearedMuons','smearedMuons','smearedMET','smearedJets',0,9999,text = '',leadingObjectsOnly = True,dR = 0.15,recoMode = "")
analysisConfigurator.addSelector('diMuonsSel','PATMuPairSelector',DiMuonPreSel+'&&'+DiMuonPreSel2+'&&'+DiMuonPreSel3,'diMuonSel',0,999)
analysisConfigurator.addSorter('diMuonsSorted','PATMuPairSorter')

#Make Muons+MET cleanPatJets
analysisConfigurator.addCandidateMETModule('wCands','PATMuonNuPairProducer','smearedMuons','smearedMET','smearedJets',0,9999,'AtLeastOneWCandidate',genParticles="genDaughters")

analysisConfigurator.addSelector('wCandsKIN','PATMuonNuPairSelector','lepton.pt()>25 && abs(lepton.eta())<2.1' ,'wCandsKIN',0)
analysisConfigurator.addSelector('wCandsJets','PATMuonNuPairSelector','','wCandsSel',0)

selectionSequence = analysisConfigurator.returnSequence()
