import FWCore.ParameterSet.Config as cms



#Import tool that creates the cut sequence
from UWAnalysis.Configuration.tools.CutSequenceProducer import *


analysisConfigurator = CutSequenceProducer(initialCounter  = 'initialEvents',
                                  pyModuleName = __name__,
                                  pyNameSpace  = locals())

#analysisConfigurator.addSmearing('patOverloadedTaus','cleanPatMuons','cleanPatElectrons','cleanPatJets','systematicsMET')

analysisConfigurator.addDiCandidateModule('BASECandidates','PATMuPairProducer', 'cleanPatMuons','cleanPatMuons','systematicsMET','patOverloadedJets',0,9999,text = '',leadingObjectsOnly = False,dR = 0.15,recoMode = "")
analysisConfigurator.addSorter('BASECandidatesSorted','PATMuPairSorter')
analysisConfigurator.addSelector('BASECandidatesID','PATMuPairSelector','leg1.userFloat("isWWMuon")&&leg2.userFloat("isWWMuon")&&leg1.pt()>15&&leg2.pt()>15&&abs(leg1.eta)<2.5&&abs(leg2.eta)<2.5','ZMuMuID')

analysisConfigurator.addDiCandidateModule('zJJCandidates','PATJetPairProducer', 'patOverloadedJets','patOverloadedJets','patMETs','patOverloadedJets',0,9999,text = '',leadingObjectsOnly = False,dR = 0.15,recoMode = "")
analysisConfigurator.addSorter('zJJCandidatesSorted','PATJetPairSorter')
analysisConfigurator.addSelector('zJJCandidatesID','PATJetPairSelector','leg1.pt()>25&&leg2.pt()>25&&abs(leg1.eta)<3&&abs(leg2.eta)<3','ZJJID') 

analysisConfigurator.addDiCandidateModule('zBASEJJ','PATMuMuJJQuadProducer','BASECandidatesID','zJJCandidatesID','patMETs','patOverloadedJets',1,9999,text='MuMuJJAtLeastOneZZ',leadingObjectsOnly = False,dR = 0.5,recoMode ="",genParticles='genDaughters')

analysisConfigurator.addCrossCleanerModule('BASEJJCleanedCands','PATMuMuJJQuadCrossCleaner',1,9999,text='MMJJAtLeastOneZZCleanedCandidate',dR = 0.5)  


selectionSequence =analysisConfigurator.returnSequence()




