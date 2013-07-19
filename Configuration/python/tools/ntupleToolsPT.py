import FWCore.ParameterSet.Config as cms

from UWAnalysis.Configuration.tools.analysisToolsPT import TriggerPaths


def addBASEEventTree(process,name,src = 'BASEJJCleanedCands', srcLL = 'zJJCandidatesID'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              coreCollections = cms.VInputTag(
                                   cms.InputTag(src)
                              ),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag("patTrigger"),
                                  paths = cms.vstring(TriggerPaths)
                                  ),

                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src = cms.InputTag("addPileupInfo"),
                                  tag = cms.string("pu"),
                                  ),
                                  
                              pt1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pt1"),
                                  method = cms.string("leg1.pt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              pt2 = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("pt2"),
                                    method = cms.string("leg2.pt"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              charge1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge1"),
                                  method = cms.string("leg1.charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              charge2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge2"),
                                  method = cms.string("leg2.charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              pt = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("pt"),
                                    method = cms.string("pt"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              eta = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("eta"),
                                    method = cms.string("eta"),
                                    leadingOnly=cms.untracked.bool(True)

                              ),
                              muTauEta1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("eta1"),
                                  method = cms.string("leg1.eta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauEta2 = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("eta2"),
                                    method = cms.string("leg2.eta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPhi1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("phi1"),
                                  method = cms.string("leg1.phi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPhi2 = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("phi2"),
                                    method = cms.string("leg2.phi"),
                                  leadingOnly=cms.untracked.bool(True)
                              )
   )

   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)


def addMuNuEventTreePtDat(process,name,src = 'wCandsJets',srcZ = 'diMuonsSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              coreCollections = cms.VInputTag(
                                   cms.InputTag(src)
                              ),
                              PVs = cms.PSet(
                                    pluginType = cms.string("VertexSizeFiller"),
                                    src = cms.InputTag("primaryVertexFilter"),
                                    tag = cms.string("vertices")
                              ),
                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src = cms.InputTag("addPileupInfo"),
                                  tag = cms.string("pu"),
                                  ),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag("patTrigger"),
                                  paths = cms.vstring(TriggerPaths)
                              ),
                               DiJetSVSVMass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("DiSVMass"),
                                  method = cms.string('SV1SV2M')
                              ),
                               DiJetSVSVPt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("DiSVPt"),
                                  method = cms.string('SV1SV2Pt')
                              ),
                               J1SV_M = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVM"),
                                  method = cms.string('userFloat("SV_M")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1SV_Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVpt"),
                                  method = cms.string('userFloat("SV_pt")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1SV_Eta = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVeta"),
                                  method = cms.string('userFloat("SV_eta")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1SV_Phi = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVphi"),
                                  method = cms.string('userFloat("SV_phi")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J2SV_M = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVM"),
                                  method = cms.string('userFloat("SV_M")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2SV_Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVpt"),
                                  method = cms.string('userFloat("SV_pt")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2SV_Eta = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVeta"),
                                  method = cms.string('userFloat("SV_eta")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2SV_Phi = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVphi"),
                                  method = cms.string('userFloat("SV_phi")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J1Mu1boost = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Mu1Boost"),
                                  method = cms.string('userFloat("Mu1Boost")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2Mu1boost = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Mu1Boost"),
                                  method = cms.string('userFloat("Mu1Boost")'),
                                  rank = cms.untracked.double(1)
                             ),
                               muNuFirstBpmElecstrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpmE"),
                                   method = cms.string('userFloat("massBpmElecs")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpmElecstrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpmE"),
                                   method = cms.string('userFloat("massBpmElecs")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpm3 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm3"),
                                   method = cms.string('userFloat("sec_massBpm")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpm3 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm3"),
                                   method = cms.string('userFloat("sec_massBpm")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpm3charge = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm3_charge"),
                                   method = cms.string('userFloat("sec_massBpm_charge")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpm3charge = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm3_charge"),
                                   method = cms.string('userFloat("sec_massBpm_charge")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstD03 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massD03"),
                                   method = cms.string('userFloat("sec_massD0")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondD03 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massD03"),
                                   method = cms.string('userFloat("sec_massD0")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpmtrue2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm2"),
                                   method = cms.string('userFloat("massBpm2")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpmtrue2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm2"),
                                   method = cms.string('userFloat("massBpm2")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstDpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massDpm"),
                                   method = cms.string('userFloat("massDpm")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondDpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massDpm"),
                                   method = cms.string('userFloat("massDpm")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm"),
                                   method = cms.string('userFloat("massBpm")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm"),
                                   method = cms.string('userFloat("massBpm")'),
                                   rank = cms.untracked.double(1)
                               ),
                              cSIZE2= cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("cbarCands"),
                                  tag = cms.string("ncbarCands"),
                                  ),
                              cSIZE = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("cCands"),
                                  tag = cms.string("ncCands"),
                                  ),
                              muNuSize = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("NWCands")
                                  ),
                              muSize = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("selectedPatMuons"),
                                  tag = cms.string("nMuons")
                                  ),
                              eleSize = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("selectedPatElectrons"),
                                  tag = cms.string("nElectrons")
                                  ),
                               nJets24to5 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24to5"), #nJets24to5
                                   method = cms.string("nJets24to5")
                               ),
                               nJets24to5pt20 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24Pt20"),
                                   method = cms.string("nJets24Pt20")
                               ),
                               nJets24to5pt25 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24Pt25"),
                                   method = cms.string("nJets24Pt25")
                               ),
                               nJets24to5pt30 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24Pt30"),
                                   method = cms.string("nJets24Pt30")
                               ),
                               muNuFirstD0true = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massD0"),
                                   method = cms.string('userFloat("massD0")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondD0true = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massD0"),
                                   method = cms.string('userFloat("massD0")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstFD = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1FlightDist"),
                                   method = cms.string('userFloat("flightDistance")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondFD = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2FlightDist"),
                                   method = cms.string('userFloat("flightDistance")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstFDer = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1errorFlightDist"),
                                   method = cms.string('userFloat("errorFlightDistance")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondFDer = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2errorFlightDist"),
                                   method = cms.string('userFloat("errorFlightDistance")'),
                                   rank = cms.untracked.double(1)
                               ),
                               J1ntracks = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1nTracks"),
                                  method = cms.string('userFloat("nTracks")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2ntracks = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2nTracks"),
                                  method = cms.string('userFloat("nTracks")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1track1Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Track1Pt"),
                                  method = cms.string('(userFloat("SSV_track1_px")^2+userFloat("SSV_track1_py")^2+userFloat("SSV_track1_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1track2Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Track2Pt"),
                                  method = cms.string('(userFloat("SSV_track2_px")^2+userFloat("SSV_track2_py")^2+userFloat("SSV_track2_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1track3Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Track3Pt"),
                                  method = cms.string('(userFloat("SSV_track3_px")^2+userFloat("SSV_track3_py")^2+userFloat("SSV_track3_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(0)
                              ),
                               J2track1Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Track1Pt"),
                                  method = cms.string('(userFloat("SSV_track1_px")^2+userFloat("SSV_track1_py")^2+userFloat("SSV_track1_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2track2Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Track2Pt"),
                                  method = cms.string('(userFloat("SSV_track2_px")^2+userFloat("SSV_track2_py")^2+userFloat("SSV_track2_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2track3Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Track3Pt"),
                                  method = cms.string('(userFloat("SSV_track3_px")^2+userFloat("SSV_track3_py")^2+userFloat("SSV_track3_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(1)
                              ),
                               muNuDZ = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dz"),
                                  method = cms.string('abs(lepton.userFloat("dz"))'),
                                  Leadingonly=cms.untracked.bool(True)
                               ),
                              muNuJ1DR = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1DR"),
                                  method = cms.string('userFloat("DR")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuJ2DR = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2DR"),
                                  method = cms.string('userFloat("DR")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuJ1Shape = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1JetShape"),
                                  method = cms.string('userFloat("ptRMS")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuJ2Shape = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2JetShape"),
                                  method = cms.string('userFloat("ptRMS")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J1TRKdxy = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TRKdxy"),
                                  method = cms.string('userFloat("dxy")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2TRKdxy = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TRKdxy"),
                                  method = cms.string('userFloat("dxy")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1TRKdz = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TRKdz"),
                                  method = cms.string('userFloat("dz")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2TRKdz = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TRKdz"),
                                  method = cms.string('userFloat("dz")'),
                                  rank = cms.untracked.double(1)
                             ),
                               genWs = cms.PSet(
                                     pluginType = cms.string("CollectionSizeFiller"),
                                     src = cms.InputTag("genWs"),
                                     tag = cms.string("genWs"),
                               ),
                              muNuHT = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("ht"),
                                  method = cms.string("ht"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                               muNuFirstJetFlavor = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1JetParton"),
                                   method = cms.string('partonFlavour()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstNTrackSSV = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1nTracksSSV"),
                                   method = cms.string('userFloat("nTracksSSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondNTrackSSV = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2nTracksSSV"),
                                   method = cms.string('userFloat("nTracksSSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstJetSVMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1SVMass"),
                                   method = cms.string('userFloat("massSSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetSVMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2SVMass"),
                                   method = cms.string('userFloat("massSSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstJetSVMassb = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1SVMassb"),
                                   method = cms.string('userFloat("mass_SSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetSVMassb = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2SVMassb"),
                                   method = cms.string('userFloat("mass_SSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstMuonMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1MuonMulti"),
                                   method = cms.string('muonMultiplicity()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondMuonMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2MuonMulti"),
                                   method = cms.string('muonMultiplicity()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdMuonMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3MuonMulti"),
                                   method = cms.string('muonMultiplicity()'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuFirstChargeMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1ChargeMulti"),
                                  method = cms.string('chargedMultiplicity()'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuSecondChargeMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2ChargeMulti"),
                                  method = cms.string('chargedMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuFirstElectronMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1EleMulti"),
                                  method = cms.string('electronMultiplicity()'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuSecondElectronMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2EleMulti"),
                                  method = cms.string('electronMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuFirstPhotonMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1PhotonMulti"),
                                  method = cms.string('photonMultiplicity()'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuSecondPhotonMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2PhotonMulti"),
                                  method = cms.string('photonMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetFlavor = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2JetParton"),
                                  method = cms.string('partonFlavour()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuThirdJetFlavor = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3JetParton"),
                                  method = cms.string('partonFlavour()'),
                                  rank = cms.untracked.double(2)
                              ),
                              genbb = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genbbCands"),
                                  tag = cms.string("genBs"),
                              ),
                              gencc = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genccCands"),
                                  tag = cms.string("genCs"),
                              ),
                              gendd = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genddCands"),
                                  tag = cms.string("genDs"),
                              ),
                              genuu = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genuuCands"),
                                  tag = cms.string("genUs"),
                              ),
                              genss = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genSSCands"),
                                  tag = cms.string("genSs"),
                              ),
                              muNuJJ = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mJJ"),
                                  method = cms.string("mJJ"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                              muNuJJ2 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mJ3J4"),
                                  method = cms.string("mJJ2"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("ptJJ"),
                                   method = cms.string("ptJJ"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muonPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonPt"),
                                   method = cms.string("lepton().pt")
                               ),##
                               WPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("WPt"),
                                   method = cms.string("corPt()")
                               ),
                               muNuCalMET = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("met"),
                                   method = cms.string("calibratedMET.pt()"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuMET = cms.PSet(
                                     pluginType = cms.string("PATMuonNuPairFiller"),
                                     src = cms.InputTag(src),
                                     tag = cms.string("MET"),
                                     method = cms.string("met().pt")
                               ),
                               muNuCorMET = cms.PSet(
                                     pluginType = cms.string("PATMuonNuPairFiller"),
                                     src = cms.InputTag(src),
                                     tag = cms.string("corMET"),
                                     method = cms.string("trueMet")
                               ),
                               muNuEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonEta"),
                                   method = cms.string("lepton.eta")
                               ),
                               muNuPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonPhi"),
                                   method = cms.string("lepton.phi")
                               ),
                               muNuCharge = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonCharge"),
                                   method = cms.string("lepton.charge()")
                               ),
                               muNuMT = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("Mt"),
                                   method = cms.string("mt")
                               ),
                               muNuCorMT = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("MtCal"),
                                   method = cms.string("corMt()")
                               ),
                               muMuMass = cms.PSet(
                                   pluginType = cms.string("PATMuPairFiller"),
                                   src = cms.InputTag(srcZ),
                                   tag = cms.string("DiMuonMass"),
                                   method = cms.string("mass")
                               ),###
                              muMuleg1pt = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1pt"),
                                  method = cms.string('leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg1eta = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1eta"),
                                  method = cms.string('leg1.eta()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg1phi = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1phi"),
                                  method = cms.string('leg1.phi()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg2pt = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2pt"),
                                  method = cms.string('leg2.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg2eta = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2eta"),
                                  method = cms.string('leg2.eta()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg2phi = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2phi"),
                                  method = cms.string('leg2.phi()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelStdIsoLeg1 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1StdRelIso"),
                                  method = cms.string('(leg1.isolationR03.sumPt+leg1.isolationR03.emEt+leg1.isolationR03.hadEt)/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelPFIsoDBLeg1 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1PFIsoDB"),
                                  method = cms.string('(leg1.userIso(0)+max(leg1.photonIso()+leg1.neutralHadronIso()-0.5*leg1.puChargedHadronIso,0.0))/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelStdIsoLeg2 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2StdRelIso"),
                                  method = cms.string('(leg2.isolationR03.sumPt+leg2.isolationR03.emEt+leg2.isolationR03.hadEt)/leg2.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelPFIsoDBLeg2 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2PFIsoDB"),
                                  method = cms.string('(leg2.userIso(0)+max(leg2.photonIso()+leg2.neutralHadronIso()-0.5*leg2.puChargedHadronIso,0.0))/leg2.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                               muMuHMass = cms.PSet(
                                   pluginType = cms.string("PATMuPairFiller"),
                                   src = cms.InputTag(srcZ),
                                   tag = cms.string("HMass1"),
                                   method = cms.string("p4Higgs.M()")
                               ),
                               muMuHMassSV = cms.PSet(
                                   pluginType = cms.string("PATMuPairFiller"),
                                   src = cms.InputTag(srcZ),
                                   tag = cms.string("HMass2"),
                                   method = cms.string("p4HiggsSV.M()")
                               ),
                               muNumetjj = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("metjj"),
                                   method = cms.string("metjj")
                               ),
                               muNuleptonjj = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("leptonjj"),
                                   method = cms.string("leptonjj")
                               ),
                               muNuDPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuDPhi"),
                                   method = cms.string("dPhi")
                               ),
                               muNuRecoil = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuRecoil"),
                                   method = cms.string("recoil().pt()")
                               ),
                               muNuMuRelPFIso = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuRelPFIso"),
                                   method = cms.string('(lepton.chargedHadronIso()+lepton.photonIso()+lepton.neutralHadronIso())/lepton.pt()')
                               ),
                               muNuMuRelPFIsoVeto = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("PFIsoVeto"),
                                   method = cms.string('lepton.userIso(0)')
                               ),
                               muNuMuRelPFIsoRho = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("PFIsoRho"),
                                   method = cms.string('lepton.userFloat("rho")')
                               ),
                               muNuRelStdIso03 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuRelStdIso03"),
                                   method = cms.string('(lepton.isolationR03.sumPt+lepton.isolationR03.emEt+lepton.isolationR03.hadEt)/lepton.pt()')
                               ),
                              muNuRelPFIsoDB = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lPFIsoDB"),
                                  method = cms.string('(lepton.userIso(0)+max(lepton.photonIso()+lepton.neutralHadronIso()-0.5*lepton.puChargedHadronIso,0.0))/lepton.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muNuJ1mu1Mass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Mu1ZMass"),
                                  method = cms.string('userFloat("muon1ZMass")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ2mu1Mass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Mu1ZMass"),
                                  method = cms.string('userFloat("muon1ZMass")'),
                                  rank = cms.untracked.double(1)
                                  ),
                              muNuJ1mu1 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1muon1pt"),
                                  method = cms.string('userFloat("muon1pt")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ1mu2 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1muon2pt"),
                                  method = cms.string('userFloat("muon2pt")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ2mu1 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2muon1pt"),
                                  method = cms.string('userFloat("muon1pt")'),
                                  rank = cms.untracked.double(1)
                                  ),
                              muNuJ2mu2 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2muon2pt"),
                                  method = cms.string('userFloat("muon2pt")'),
                                  rank = cms.untracked.double(1)
                                  ),
                               muNuJetsPt30 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt30"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt25 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt25"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>25&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt26 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt26"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>26&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt24 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt24"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>24&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt40 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt40"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>40&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt20 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt20"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>20&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuFirstJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("highestJetPt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("secondJetPt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("thirdJetPt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuFirstJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("highestJetEta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("secondJetEta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("thirdJetEta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuFirstJetPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("highestJetPhi"),
                                   method = cms.string('phi()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("secondJetPhi"),
                                   method = cms.string('phi()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdJetPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("thirdJetPhi"),
                                   method = cms.string('phi()'),
                                   rank = cms.untracked.double(2)
                               ),
                                muNuFirstJetChargedMultiplicity = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1nCharges"),
                                   method = cms.string('chargedHadronMultiplicity()'),
                                   rank = cms.untracked.double(0)
                               ),
                              muNuFirstJetTCHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TCHEbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighEffBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetTCHPbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TCHPbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighPurBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetSSVHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SSVHEbtag"),
                                  method = cms.string('bDiscriminator("simpleSecondaryVertexHighEffBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetCSVbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1CSVbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetCSVMVAbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1CSVMVAbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexMVABJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetCharge = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Charge"),
                                  method = cms.string('jetCharge'),
                                  rank = cms.untracked.double(0)
                              ),
                               muNuFirstJetMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1Mass"),
                                   method = cms.string('mass'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstPhotonEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1PhotonEnergy"),
                                   method = cms.string('photonEnergy'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstPhotonEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1PhotonEnergyFrac"),
                                   method = cms.string('photonEnergyFraction'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstElectronEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1ElectronEnergy"),
                                   method = cms.string('electronEnergy'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstElectronEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1ElectronEnergyFrac"),
                                   method = cms.string('chargedEmEnergyFraction'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstMuEnergy = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J1MuonEnergy"),
                                    method = cms.string('chargedMuEnergy'),
                                    rank = cms.untracked.double(0)
                                ),
                                muNuFirstMuEnergyFrac = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J1MuEnergyFrac"),
                                    method = cms.string('muonEnergyFraction'),
                                    rank = cms.untracked.double(0)
                                ),
                              muNuSecondJetChargedMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2nCharges"),
                                  method = cms.string('chargedHadronMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetTCHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TCHEbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighEffBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetTCHPbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TCHPbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighPurBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetSSVHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SSVHEbtag"),
                                  method = cms.string('bDiscriminator("simpleSecondaryVertexHighEffBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetCSVbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2CSVbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetCSVMVAbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2CSVMVAbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexMVABJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),#####
                              muNuSecondJetCharge = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Charge"),
                                  method = cms.string('jetCharge'),
                                  rank = cms.untracked.double(1)
                              ),
                               muNuSecondJetMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2Mass"),
                                   method = cms.string('mass'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondPhotonEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2PhotonEnergy"),
                                   method = cms.string('photonEnergy'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondPhotonEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2PhotonEnergyFrac"),
                                   method = cms.string('photonEnergyFraction'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondElectronEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2ElectronEnergy"),
                                   method = cms.string('electronEnergy'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondElectronEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2ElectronEnergyFrac"),
                                   method = cms.string('chargedEmEnergyFraction'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondMuEnergy = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J2MuonEnergy"),
                                    method = cms.string('chargedMuEnergy'),
                                    rank = cms.untracked.double(1)
                                ),
                                muNuSecondMuEnergyFrac = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J2MuEnergyFrac"),
                                    method = cms.string('muonEnergyFraction'),
                                    rank = cms.untracked.double(1)
                                ),

                               muNuThirdJetChargedMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3nCharges"),
                                  method = cms.string('chargedHadronMultiplicity()'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuThirdJetTCHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3TCHEbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighEffBJetTags")'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuThirdJetCharge = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3Charge"),
                                  method = cms.string('jetCharge'),
                                  rank = cms.untracked.double(2)
                              ),
                               muNuThirdJetMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3Mass"),
                                   method = cms.string('mass'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdPhotonEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3PhotonEnergy"),
                                   method = cms.string('photonEnergy'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdPhotonEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3PhotonEnergyFrac"),
                                   method = cms.string('photonEnergyFraction'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdElectronEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3ElectronEnergy"),
                                   method = cms.string('electronEnergy'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdElectronEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3ElectronEnergyFrac"),
                                   method = cms.string('chargedEmEnergyFraction'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdMuEnergy = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J3MuonEnergy"),
                                    method = cms.string('chargedMuEnergy'),
                                    rank = cms.untracked.double(2)
                                ),
                                muNuThirdMuEnergyFrac = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J3MuEnergyFrac"),
                                    method = cms.string('muonEnergyFraction'),
                                    rank = cms.untracked.double(2)
                                ),
                               mu1DXY = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("l1DXY"),
                                   method = cms.string('lepton.userFloat("ipDXY")'),
                                   leadingOnly=cms.untracked.bool(True)
                                   ),###################FOR BTAGGING CORRECTIONS ##CSVbtag value
                               muNu3rdJetCSVbtag = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3CSVbtag"),
                                   method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNu4thJetCSVbtag = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J4CSVbtag"),
                                   method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                   rank = cms.untracked.double(3)
                               ),
                              muNu4thJetFlavor = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J4JetParton"),
                                   method = cms.string('partonFlavour()'),
                                   rank = cms.untracked.double(3)
                               ),
                              muNu4thJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J4Pt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(3)
                               ),
                              muNu4thJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J4Eta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(3)
                               )


   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)

def addMuNuEventTreePt(process,name,src = 'wCandsJets',srcZ = 'diMuonsSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              coreCollections = cms.VInputTag(
                                   cms.InputTag(src)
                              ),
                              PVs = cms.PSet(
                                    pluginType = cms.string("VertexSizeFiller"),
                                    src = cms.InputTag("primaryVertexFilter"),
                                    tag = cms.string("vertices")
                              ),
                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src = cms.InputTag("addPileupInfo"),
                                  tag = cms.string("pu"),
                                  ),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag("patTrigger"),
                                  paths = cms.vstring(TriggerPaths)
                              ),
                              muNuLHEProduct = cms.PSet(
                                  pluginType = cms.string("LHEProductFiller"),
                                  src = cms.InputTag("source"),
                                  tag = cms.string("LHEProduct"),
                              ),
                              simBHadronsSIZE = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("bhadrons"),
                                  tag = cms.string("nbHadrons"),
                                  ),
                               DiJetSVSVMass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("DiSVMass"),
                                  method = cms.string('SV1SV2M')
                              ),
                               DiJetSVSVPt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("DiSVPt"),
                                  method = cms.string('SV1SV2Pt')
                              ),
                               J1SV_M = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVM"),
                                  method = cms.string('userFloat("SV_M")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1SV_Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVpt"),
                                  method = cms.string('userFloat("SV_pt")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1SV_Eta = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVeta"),
                                  method = cms.string('userFloat("SV_eta")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1SV_Phi = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SVphi"),
                                  method = cms.string('userFloat("SV_phi")'),
                                  rank = cms.untracked.double(0)
                              ),
                               J2SV_M = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVM"),
                                  method = cms.string('userFloat("SV_M")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2SV_Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVpt"),
                                  method = cms.string('userFloat("SV_pt")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2SV_Eta = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVeta"),
                                  method = cms.string('userFloat("SV_eta")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2SV_Phi = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SVphi"),
                                  method = cms.string('userFloat("SV_phi")'),
                                  rank = cms.untracked.double(1)
                              ),
                               DiJetHadZMass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("hadMassZ"),
                                  method = cms.string('massZ')
                              ),
                               muNuFirstBpm3charge = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm3_charge"),
                                   method = cms.string('userFloat("sec_massBpm_charge")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpm3charge = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm3_charge"),
                                   method = cms.string('userFloat("sec_massBpm_charge")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpm3 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm3"),
                                   method = cms.string('userFloat("sec_massBpm")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpm3 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm3"),
                                   method = cms.string('userFloat("sec_massBpm")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstD03 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massD03"),
                                   method = cms.string('userFloat("sec_massD0")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondD03 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massD03"),
                                   method = cms.string('userFloat("sec_massD0")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstD0true = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massD0"),
                                   method = cms.string('userFloat("massD0")'),
                                   rank = cms.untracked.double(0)
                              ),
                               muNuSecondD0true = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massD0"),
                                   method = cms.string('userFloat("massD0")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstDpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massDpm"),
                                   method = cms.string('userFloat("massDpm")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondDpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massDpm"),
                                   method = cms.string('userFloat("massDpm")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpmtrue2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm2"),
                                   method = cms.string('userFloat("massBpm2")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpmtrue2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm2"),
                                   method = cms.string('userFloat("massBpm2")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpmElecstrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpmE"),
                                   method = cms.string('userFloat("massBpmElecs")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpmElecstrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpmE"),
                                   method = cms.string('userFloat("massBpmElecs")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstBpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1massBpm"),
                                   method = cms.string('userFloat("massBpm")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondBpmtrue = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2massBpm"),
                                   method = cms.string('userFloat("massBpm")'),
                                   rank = cms.untracked.double(1)
                               ),
                               simBHadronsPT1 = cms.PSet(
                                   pluginType = cms.string("SimBHadronsFiller"),
                                   src = cms.InputTag('bhadrons'),
                                   tag = cms.string('bHadronsPt'),
                                   method = cms.string("pt()"),
                                   leadingOnly=cms.untracked.bool(False)
                                   ),
                               simBHadronsEta1 = cms.PSet(
                                   pluginType = cms.string("SimBHadronsFiller"),
                                   src = cms.InputTag('bhadrons'),
                                   tag = cms.string('bHadronsEta'),
                                   method = cms.string("eta()"),
                                   leadingOnly=cms.untracked.bool(False)
                                   ),
                               simBHadronsPhi1 = cms.PSet(
                                   pluginType = cms.string("SimBHadronsFiller"),
                                   src = cms.InputTag('bhadrons'),
                                   tag = cms.string('bHadronsPhi'),
                                   method = cms.string("phi()"),
                                   leadingOnly=cms.untracked.bool(False)
                                   ),
                              cSIZE2= cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("cbarCands"),
                                  tag = cms.string("ncbarCands"),
                                  ),
                              cSIZE = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("cCands"),
                                  tag = cms.string("ncCands"),
                                  ),
                               nJets24to5 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24to5"),
                                   method = cms.string("nJets24to5")
                               ),
                               nJets24to5pt20 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24Pt20"),
                                   method = cms.string("nJets24Pt20")
                               ),
                               nJets24to5pt25 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24Pt25"),
                                   method = cms.string("nJets24Pt25")
                               ),
                               nJets24to5pt30 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJets24Pt30"),
                                   method = cms.string("nJets24Pt30")
                               ),
                              muNuSize = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("NWCands")
                                  ),
                              muSize = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("selectedPatMuons"),
                                  tag = cms.string("nMuons")
                                  ),
                              eleSize = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("selectedPatElectrons"),
                                  tag = cms.string("nElectrons")
                                  ),
                               muNuDZ = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dz"),
                                  method = cms.string('abs(lepton.userFloat("dz"))'),
                                  Leadingonly=cms.untracked.bool(True)
                               ),
                              muNuTop = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1top"),
                                  method = cms.string('userFloat("top")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuJ1mu1Mass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Mu1ZMass"),
                                  method = cms.string('userFloat("muon1ZMass")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ2mu1Mass = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Mu1ZMass"),
                                  method = cms.string('userFloat("muon1ZMass")'),
                                  rank = cms.untracked.double(1)
                                  ),
                              muNuJ1mu1 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1muon1pt"),
                                  method = cms.string('userFloat("muon1pt")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ1mu2 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1muon2pt"),
                                  method = cms.string('userFloat("muon2pt")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ2mu1 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2muon1pt"),
                                  method = cms.string('userFloat("muon1pt")'),
                                  rank = cms.untracked.double(1)
                                  ),
                              muNuJ2mu2 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2muon2pt"),
                                  method = cms.string('userFloat("muon2pt")'),
                                  rank = cms.untracked.double(1)
                                  ),
                              muNuJ1DR = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1DR"),
                                  method = cms.string('userFloat("DR")'),
                                  rank = cms.untracked.double(0)
                                  ),
                              muNuJ2DR = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2DR"),
                                  method = cms.string('userFloat("DR")'),
                                  rank = cms.untracked.double(1)
                                  ),
                              muNuJ1Shape = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1JetShape"),
                                  method = cms.string('userFloat("ptRMS")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuJ2Shape = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2JetShape"),
                                  method = cms.string('userFloat("ptRMS")'),
                                  rank = cms.untracked.double(1)
                              ),
                               J1MuTRKdxy = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Mu1dxy"),
                                  method = cms.string('userFloat("dxyMu1")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2MuTRKdxy = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Mu1dxy"),
                                  method = cms.string('userFloat("dxyMu1")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1DR = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1DR"),
                                  method = cms.string('userFloat("DR")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2DR = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2DR"),
                                  method = cms.string('userFloat("DR")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1ntracks = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1nTracks"),
                                  method = cms.string('userFloat("nTracks")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2ntracks = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2nTracks"),
                                  method = cms.string('userFloat("nTracks")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1Mu1boost = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Mu1Boost"),
                                  method = cms.string('userFloat("Mu1Boost")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2Mu1boost = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Mu2Boost"),
                                  method = cms.string('userFloat("Mu2Boost")'),
                                  rank = cms.untracked.double(1)
                             ),####
                               J1TRKdxy = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TRKdxy"),
                                  method = cms.string('userFloat("dxy")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2TRKdxy = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TRKdxy"),
                                  method = cms.string('userFloat("dxy")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1TRKdz = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TRKdz"),
                                  method = cms.string('userFloat("dz")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2TRKdz = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TRKdz"),
                                  method = cms.string('userFloat("dz")'),
                                  rank = cms.untracked.double(1)
                             ),
                               genWs = cms.PSet(
                                     pluginType = cms.string("CollectionSizeFiller"),
                                     src = cms.InputTag("genWs"),
                                     tag = cms.string("genWs"),
                               ),
                              muNuHT = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("ht"),
                                  method = cms.string("ht"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                               muNuFirstJetFlavor = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1JetParton"),
                                   method = cms.string('partonFlavour()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstFD = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1FlightDist"),
                                   method = cms.string('userFloat("flightDistance")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondFD = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2FlightDist"),
                                   method = cms.string('userFloat("flightDistance")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstFDer = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1errorFlightDist"),
                                   method = cms.string('userFloat("errorFlightDistance")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondFDer = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2errorFlightDist"),
                                   method = cms.string('userFloat("errorFlightDistance")'),
                                   rank = cms.untracked.double(1)
                               ),
                               J1D0 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1D0mass"),
                                  method = cms.string('userFloat("massD0_SSV")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2D0 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2D0mass"),
                                  method = cms.string('userFloat("massD0_SSV")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1D = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Dmass"),
                                  method = cms.string('userFloat("massD_SSV")'),
                                  rank = cms.untracked.double(0)
                              ),
                              J2D = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Dmass"),
                                  method = cms.string('userFloat("massD_SSV")'),
                                  rank = cms.untracked.double(1)
                             ),
                               J1track1Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Track1Pt"),
                                  method = cms.string('(userFloat("SSV_track1_px")^2+userFloat("SSV_track1_py")^2+userFloat("SSV_track1_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1track2Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Track2Pt"),
                                  method = cms.string('(userFloat("SSV_track2_px")^2+userFloat("SSV_track2_py")^2+userFloat("SSV_track2_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(0)
                              ),
                               J1track3Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Track3Pt"),
                                  method = cms.string('(userFloat("SSV_track3_px")^2+userFloat("SSV_track3_py")^2+userFloat("SSV_track3_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(0)
                              ),
                               J2track1Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Track1Pt"),
                                  method = cms.string('(userFloat("SSV_track1_px")^2+userFloat("SSV_track1_py")^2+userFloat("SSV_track1_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2track2Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Track2Pt"),
                                  method = cms.string('(userFloat("SSV_track2_px")^2+userFloat("SSV_track2_py")^2+userFloat("SSV_track2_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(1)
                              ),
                               J2track3Pt = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Track3Pt"),
                                  method = cms.string('(userFloat("SSV_track3_px")^2+userFloat("SSV_track3_py")^2+userFloat("SSV_track3_pz")^2)^(1/2)'),
                                  rank = cms.untracked.double(1)
                              ),
                               muNuFirstNTrackSSV = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1nTracksSSV"),
                                   method = cms.string('userFloat("nTracksSSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondNTrackSSV = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2nTracksSSV"),
                                   method = cms.string('userFloat("nTracksSSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstNTrackSSVneg = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1nTracksSSVneg"),
                                   method = cms.string('userFloat("nTracksNEGSSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondNTrackSSVneg = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2nTracksSSVneg"),
                                   method = cms.string('userFloat("nTracksNEGSSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstJetSVMassNegb = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1SVMassNegb"),
                                   method = cms.string('userFloat("mass_SSVNEG")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetSVMassNegb = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2SVMassNegb"),
                                   method = cms.string('userFloat("mass_SSVNEG")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstJetSVMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1SVMass"),
                                   method = cms.string('userFloat("massSSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetSVMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2SVMass"),
                                   method = cms.string('userFloat("massSSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstJetSVMassb = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1SVMassb"),
                                   method = cms.string('userFloat("mass_SSV")'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetSVMassb = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2SVMassb"),
                                   method = cms.string('userFloat("mass_SSV")'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuFirstMuonMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1MuonMulti"),
                                   method = cms.string('muonMultiplicity()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondMuonMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2MuonMulti"),
                                   method = cms.string('muonMultiplicity()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdMuonMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3MuonMulti"),
                                   method = cms.string('muonMultiplicity()'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuFirstChargeMulti = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1ChargeMulti"),
                                  method = cms.string('chargedMultiplicity()'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuSecondChargeMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2ChargeMulti"),
                                  method = cms.string('chargedMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuThirdChargeMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3ChargeMulti"),
                                  method = cms.string('chargedMultiplicity()'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuFirstElectronMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1EleMulti"),
                                  method = cms.string('electronMultiplicity()'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuSecondElectronMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2EleMulti"),
                                  method = cms.string('electronMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuThirdElectronMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3EleMulti"),
                                  method = cms.string('electronMultiplicity()'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuFirstPhotonMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1PhotonMulti"),
                                  method = cms.string('photonMultiplicity()'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuSecondPhotonMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2PhotonMulti"),
                                  method = cms.string('photonMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuThirdPhotonMulti = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3PhotonMulti"),
                                  method = cms.string('photonMultiplicity()'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuSecondJetFlavor = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2JetParton"),
                                  method = cms.string('partonFlavour()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuThirdJetFlavor = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3JetParton"),
                                  method = cms.string('partonFlavour()'),
                                  rank = cms.untracked.double(2)
                              ),
                              genbb = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genbbCands"),
                                  tag = cms.string("genBs"),
                              ),
                              gencc = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genccCands"),
                                  tag = cms.string("genCs"),
                              ),
                              gendd = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genddCands"),
                                  tag = cms.string("genDs"),
                              ),
                              genuu = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genuuCands"),
                                  tag = cms.string("genUs"),
                              ),
                              genss = cms.PSet(
                                  pluginType = cms.string("CollectionSizeFiller"),
                                  src = cms.InputTag("genSSCands"),
                                  tag = cms.string("genSs"),
                              ),
                              muNuJJ = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mJJ"),
                                  method = cms.string("mJJ"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                              muNuJJ2 = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mJ3J4"),
                                  method = cms.string("mJJ2"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJJPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("ptJJ"),
                                   method = cms.string("ptJJ"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuCSVL1 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTCSVL"),
                                   method = cms.string("SFCSVL1"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuCSVL2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTCSVL2"),
                                   method = cms.string("SFCSVL2"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuCSVM1 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTCSVM"),
                                   method = cms.string("SFCSVM1"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuCSVM2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTCSVM2"),
                                   method = cms.string("SFCSVM2"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuCSVT1 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTCSVT"),
                                   method = cms.string("SFCSVT1"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuCSVT2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTCSVT2"),
                                   method = cms.string("SFCSVT2"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuSSVHE1 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTSSVHEM"),
                                   method = cms.string("SFSSVHE1"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuSSVHE2 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("EffWEIGHTSSVHEM2"),
                                   method = cms.string("SFSSVHE2"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
# muNuEffTrig = cms.PSet(
# pluginType = cms.string("PATMuonNuPairFiller"),
# src = cms.InputTag(src),
# tag = cms.string("EffWEIGHTeta"),
# method = cms.string("EffWEIGHTeta"),
# leadingOnly=cms.untracked.bool(True)
# ),
                               muNuEffTrig_IS = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("weightEtaMuonIso"),
                                   method = cms.string("EffWEIGHTeta_IS"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuEffTrig_ID = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("weightEtaMuonID"),
                                   method = cms.string("EffWEIGHTeta_ID"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuEffTrig_TR = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("weightEtaMuonTrig"),
                                   method = cms.string("EffWEIGHTeta_TR"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
# muNuEffPt = cms.PSet(
# pluginType = cms.string("PATMuonNuPairFiller"),
# src = cms.InputTag(src),
# tag = cms.string("EffWEIGHTpt"),
# method = cms.string("EffWEIGHTpt"),
# leadingOnly=cms.untracked.bool(True)
# ),
                               muonPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonPt"),
                                   method = cms.string("lepton().pt")
                               ),##
                               muNuPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("WPt"),
                                   method = cms.string("corPt()")
                               ),
                               muNuCalMET = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("met"),
                                   method = cms.string("calibratedMET.pt()"),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuMET = cms.PSet(
                                     pluginType = cms.string("PATMuonNuPairFiller"),
                                     src = cms.InputTag(src),
                                     tag = cms.string("MET"),
                                     method = cms.string("met().pt")
                               ),
                               muNuCorMET = cms.PSet(
                                     pluginType = cms.string("PATMuonNuPairFiller"),
                                     src = cms.InputTag(src),
                                     tag = cms.string("corMET"),
                                     method = cms.string("trueMet")
                               ),
                               muNuEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonEta"),
                                   method = cms.string("lepton.eta")
                               ),
                               muNuPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonPhi"),
                                   method = cms.string("lepton.phi")
                               ),
                               muNuCharge = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muonCharge"),
                                   method = cms.string("lepton.charge()")
                               ),
                               muNuMT = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("Mt"),
                                   method = cms.string("mt")
                               ),
                               muNuCorMT = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("MtCal"),
                                   method = cms.string("corMt()")
                               ),
                               muMuMass = cms.PSet(
                                   pluginType = cms.string("PATMuPairFiller"),
                                   src = cms.InputTag(srcZ),
                                   tag = cms.string("DiMuonMass"),
                                   method = cms.string("mass")
                               ),###
                              muMuleg1pt = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1pt"),
                                  method = cms.string('leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg1eta = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1eta"),
                                  method = cms.string('leg1.eta()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg1phi = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1phi"),
                                  method = cms.string('leg1.phi()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg2pt = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2pt"),
                                  method = cms.string('leg2.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg2eta = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2eta"),
                                  method = cms.string('leg2.eta()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuleg2phi = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2phi"),
                                  method = cms.string('leg2.phi()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelStdIsoLeg1 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1StdRelIso"),
                                  method = cms.string('(leg1.isolationR03.sumPt+leg1.isolationR03.emEt+leg1.isolationR03.hadEt)/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelPFIsoDBLeg1 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1PFIsoDB"),
                                  method = cms.string('(leg1.userIso(0)+max(leg1.photonIso()+leg1.neutralHadronIso()-0.5*leg1.puChargedHadronIso,0.0))/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelStdIsoLeg2 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2StdRelIso"),
                                  method = cms.string('(leg2.isolationR03.sumPt+leg2.isolationR03.emEt+leg2.isolationR03.hadEt)/leg2.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuRelPFIsoDBLeg2 = cms.PSet(
                                  pluginType = cms.string("PATMuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l2PFIsoDB"),
                                  method = cms.string('(leg2.userIso(0)+max(leg2.photonIso()+leg2.neutralHadronIso()-0.5*leg2.puChargedHadronIso,0.0))/leg2.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                               muMuHMass = cms.PSet(
                                   pluginType = cms.string("PATMuPairFiller"),
                                   src = cms.InputTag(srcZ),
                                   tag = cms.string("HMass1"),
                                   method = cms.string("p4Higgs.M()")
                               ),
                               muMuHMassSV = cms.PSet(
                                   pluginType = cms.string("PATMuPairFiller"),
                                   src = cms.InputTag(srcZ),
                                   tag = cms.string("HMass2"),
                                   method = cms.string("p4HiggsSV.M()")
                               ),
                               muNumetjj = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("metjj"),
                                   method = cms.string("metjj")
                               ),
                               muNuleptonjj = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("leptonjj"),
                                   method = cms.string("leptonjj")
                               ),
                               muNuDPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuDPhi"),
                                   method = cms.string("dPhi")
                               ),
                               muNuRecoil = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuRecoil"),
                                   method = cms.string("recoil().pt()")
                               ),
                               muNuMuRelPFIso = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuRelPFIso"),
                                   method = cms.string('(lepton.chargedHadronIso()+lepton.photonIso()+lepton.neutralHadronIso())/lepton.pt()')
                               ),
                               muNuMuRelPFIsoVeto = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("PFIsoVeto"),
                                   method = cms.string('lepton.userIso(0)')
                               ),
                               muNuMuRelPFIsoRho = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("PFIsoRho"),
                                   method = cms.string('lepton.userFloat("rho")')
                               ),
                               muNuRelStdIso03 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("muNuRelStdIso03"),
                                   method = cms.string('(lepton.isolationR03.sumPt+lepton.isolationR03.emEt+lepton.isolationR03.hadEt)/lepton.pt()')
                               ),
                              muNuRelPFIsoDB = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lPFIsoDB"),
                                  method = cms.string('(lepton.userIso(0)+max(lepton.photonIso()+lepton.neutralHadronIso()-0.5*lepton.puChargedHadronIso,0.0))/lepton.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                               muNuJetsPt30 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt30"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt25 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt25"),
                                   method = cms.string('userInt("fullIdLoose")>0&&userFloat("idLoose")&&pt()>25&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt26 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt26"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>26&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt24 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt24"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>24&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt40 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt40"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>40&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuJetsPt20 = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairJetCountFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("nJetsPt20"),
                                   method = cms.string('userInt("fullIdLoose")>0&&pt()>20&&abs(eta())<2.4'),
                                   leadingOnly=cms.untracked.bool(True)
                               ),
                               muNuFirstJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("highestJetPt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("secondJetPt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdJetPt = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("thirdJetPt"),
                                   method = cms.string('pt()'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuFirstJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("highestJetEta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("secondJetEta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdJetEta = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("thirdJetEta"),
                                   method = cms.string('eta()'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuFirstJetPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("highestJetPhi"),
                                   method = cms.string('phi()'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuSecondJetPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("secondJetPhi"),
                                   method = cms.string('phi()'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuThirdJetPhi = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("thirdJetPhi"),
                                   method = cms.string('phi()'),
                                   rank = cms.untracked.double(2)
                               ),
                                muNuFirstJetChargedMultiplicity = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1nCharges"),
                                   method = cms.string('chargedHadronMultiplicity()'),
                                   rank = cms.untracked.double(0)
                               ),
                              muNuFirstJetTCHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TCHEbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighEffBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetTCHPbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1TCHPbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighPurBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetSSVHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1SSVHEbtag"),
                                  method = cms.string('bDiscriminator("simpleSecondaryVertexHighEffBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetCSVbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1CSVbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetCSVMVAbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1CSVMVAbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexMVABJetTags")'),
                                  rank = cms.untracked.double(0)
                              ),
                              muNuFirstJetCharge = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J1Charge"),
                                  method = cms.string('jetCharge'),
                                  rank = cms.untracked.double(0)
                              ),
                               muNuFirstJetMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1Mass"),
                                   method = cms.string('mass'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstPhotonEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1PhotonEnergy"),
                                   method = cms.string('photonEnergy'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstPhotonEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1PhotonEnergyFrac"),
                                   method = cms.string('photonEnergyFraction'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstElectronEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1ElectronEnergy"),
                                   method = cms.string('electronEnergy'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstElectronEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J1ElectronEnergyFrac"),
                                   method = cms.string('chargedEmEnergyFraction'),
                                   rank = cms.untracked.double(0)
                               ),
                               muNuFirstMuEnergy = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J1MuonEnergy"),
                                    method = cms.string('chargedMuEnergy'),
                                    rank = cms.untracked.double(0)
                                ),
                                muNuFirstMuEnergyFrac = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J1MuEnergyFrac"),
                                    method = cms.string('muonEnergyFraction'),
                                    rank = cms.untracked.double(0)
                                ),
                              muNuSecondJetChargedMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2nCharges"),
                                  method = cms.string('chargedHadronMultiplicity()'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetTCHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TCHEbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighEffBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetTCHPbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2TCHPbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighPurBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetSSVHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2SSVHEbtag"),
                                  method = cms.string('bDiscriminator("simpleSecondaryVertexHighEffBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetCSVbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2CSVbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),
                              muNuSecondJetCSVMVAbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2CSVMVAbtag"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexMVABJetTags")'),
                                  rank = cms.untracked.double(1)
                              ),#####
                              muNuSecondJetCharge = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J2Charge"),
                                  method = cms.string('jetCharge'),
                                  rank = cms.untracked.double(1)
                              ),
                               muNuSecondJetMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2Mass"),
                                   method = cms.string('mass'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondPhotonEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2PhotonEnergy"),
                                   method = cms.string('photonEnergy'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondPhotonEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2PhotonEnergyFrac"),
                                   method = cms.string('photonEnergyFraction'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondElectronEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2ElectronEnergy"),
                                   method = cms.string('electronEnergy'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondElectronEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J2ElectronEnergyFrac"),
                                   method = cms.string('chargedEmEnergyFraction'),
                                   rank = cms.untracked.double(1)
                               ),
                               muNuSecondMuEnergy = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J2MuonEnergy"),
                                    method = cms.string('chargedMuEnergy'),
                                    rank = cms.untracked.double(1)
                                ),
                                muNuSecondMuEnergyFrac = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J2MuEnergyFrac"),
                                    method = cms.string('muonEnergyFraction'),
                                    rank = cms.untracked.double(1)
                                ),

                               muNuThirdJetChargedMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3nCharges"),
                                  method = cms.string('chargedHadronMultiplicity()'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuThirdJetTCHEbtag = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3TCHEbtag"),
                                  method = cms.string('bDiscriminator("trackCountingHighEffBJetTags")'),
                                  rank = cms.untracked.double(2)
                              ),
                              muNuThirdJetCharge = cms.PSet(
                                  pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("J3Charge"),
                                  method = cms.string('jetCharge'),
                                  rank = cms.untracked.double(2)
                              ),
                               muNuThirdJetMass = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3Mass"),
                                   method = cms.string('mass'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdPhotonEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3PhotonEnergy"),
                                   method = cms.string('photonEnergy'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdPhotonEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3PhotonEnergyFrac"),
                                   method = cms.string('photonEnergyFraction'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdElectronEnergy = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3ElectronEnergy"),
                                   method = cms.string('electronEnergy'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdElectronEnergyFrac = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3ElectronEnergyFrac"),
                                   method = cms.string('chargedEmEnergyFraction'),
                                   rank = cms.untracked.double(2)
                               ),
                               muNuThirdMuEnergy = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J3MuonEnergy"),
                                    method = cms.string('chargedMuEnergy'),
                                    rank = cms.untracked.double(2)
                                ),
                                muNuThirdMuEnergyFrac = cms.PSet(
                                    pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("J3MuEnergyFrac"),
                                    method = cms.string('muonEnergyFraction'),
                                    rank = cms.untracked.double(2)
                                ),
                               mu1DXY = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("l1DXY"),
                                   method = cms.string('lepton.userFloat("ipDXY")'),
                                   leadingOnly=cms.untracked.bool(True)
                                   ),###################FOR BTAGGING CORRECTIONS ##CSVbtag value
                               muNu3rdJetCSVbtag = cms.PSet(
                                   pluginType = cms.string("PATMuonNuPairPtJetVarFiller"),
                                   src = cms.InputTag(src),
                                   tag = cms.string("J3CSVbtag"),
                                   method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")'),
                                   rank = cms.untracked.double(2)
                               )


   )
   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)





def addMuTauEventTree(process,name,src = 'diTausSorted', srcLL = 'diMuonsSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              coreCollections = cms.VInputTag(
                                   cms.InputTag(src)
                              ),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag("patTrigger"),
                                  paths = cms.vstring(TriggerPaths)
                                  ),

                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src = cms.InputTag("addPileupInfo"),
                                  tag = cms.string("pu"),
                                  ),
                                  
                              pt1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pt1"),
                                  method = cms.string("leg1.pt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              pt2 = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("pt2"),
                                    method = cms.string("leg2.pt"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              charge1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge1"),
                                  method = cms.string("leg1.charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              charge2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge2"),
                                  method = cms.string("leg2.charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              pt = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("pt"),
                                    method = cms.string("pt"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              eta = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("eta"),
                                    method = cms.string("eta"),
                                    leadingOnly=cms.untracked.bool(True)

                              ),
                              muTauEta1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("eta1"),
                                  method = cms.string("leg1.eta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauEta2 = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("eta2"),
                                    method = cms.string("leg2.eta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPhi1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("phi1"),
                                  method = cms.string("leg1.phi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPhi2 = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("phi2"),
                                    method = cms.string("leg2.phi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDZ = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("dz"),
                                    method = cms.string('abs(leg1.userFloat("vz")-leg2.userFloat("vz"))'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMudZ = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("l1dz"),
                                    method = cms.string('abs(leg1.userFloat("dz"))'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauTaudZ = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("l2dz"),
                                    method = cms.string('abs(leg2.userFloat("dz"))'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMuvZ = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("l1Vz"),
                                    method = cms.string('leg1.userFloat("vz")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauTauvZ = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("l2Vz"),
                                    method = cms.string('leg2.userFloat("vz")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauEleDXY = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1Dxy"),
                                  method = cms.string('leg1.userFloat("ipDXY")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauRho = cms.PSet(
                                  pluginType = cms.string("EventWeightFiller"),
                                  src = cms.InputTag("kt6PFJetsForRhoComputationVoronoi","rho"),
                                  tag = cms.string("Rho")
                              ),

# muTauDCA = cms.PSet(
# pluginType = cms.string("PATMuTauPairFiller"),
# src = cms.InputTag(src),
# tag = cms.string("dca"),
# method = cms.string("dca"),
# leadingOnly=cms.untracked.bool(True)
# ),
# muTauDist = cms.PSet(
# pluginType = cms.string("PATMuTauPairFiller"),
# src = cms.InputTag(src),
# tag = cms.string("xPointDist"),
# method = cms.string("crossingPointDistance"),
# leadingOnly=cms.untracked.bool(True)
# ),
                              projMET = cms.PSet(
                                    pluginType = cms.string("PATMuTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("projMET"),
                                    method = cms.string("projMET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauCharge = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge"),
                                  method = cms.string("charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mass"),
                                  method = cms.string("mass"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauSVMass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("svMass"),
                                  method = cms.string("svMass"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMT1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mt1"),
                                  method = cms.string("mt1MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMT = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mt"),
                                  method = cms.string("mt12MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMT2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mt2"),
                                  method = cms.string("mt2MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMET = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("met"),
                                  method = cms.string("calibratedMET.pt()"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDPhi = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dPhi"),
                                  method = cms.string("dPhi12"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDR = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dR"),
                                  method = cms.string("dR12"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDPhi1MET = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dPhi1MET"),
                                  method = cms.string("dPhi1MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDPhi2MET = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dPhi2MET"),
                                  method = cms.string("dPhi2MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauHT = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("ht"),
                                  method = cms.string("ht"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJJ = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mJJ"),
                                  method = cms.string("mJJ"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJJPt = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("ptJJ"),
                                  method = cms.string("ptJJ"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFDEta = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDEta"),
                                  method = cms.string("vbfDEta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFPt1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfPt1"),
                                  method = cms.string("vbfPt1"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFPt2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfPt2"),
                                  method = cms.string("vbfPt2"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFEta1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfEta1"),
                                  method = cms.string("vbfEta1"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFEta2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfEta2"),
                                  method = cms.string("vbfEta2"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFMass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfMass"),
                                  method = cms.string("vbfMass"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFMVA = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfMVA"),
                                  method = cms.string("vbfMVA"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFDPhi = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDPhi"),
                                  method = cms.string("vbfDPhi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFDiJetPt = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDiJetPt"),
                                  method = cms.string("vbfDiJetPt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFDiTauPt = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDiTauPt"),
                                  method = cms.string("vbfDiTauPt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFDPhiHJ = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDPhiHJ"),
                                  method = cms.string("vbfDPhiHJ"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFC1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfC1"),
                                  method = cms.string("vbfC1"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVBFC2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfC2"),
                                  method = cms.string("vbfC2"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muMuVBFJets20 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfNJetsGap20"),
                                  method = cms.string("vbfNJetsGap20"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              muMuVBFJets30 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfNJetsGap30"),
                                  method = cms.string("vbfNJetsGap30"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              muTauWWID = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lWWId"),
                                  method = cms.string('leg1.userInt("WWID2011")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPFID = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lPFId"),
                                  method = cms.string('leg1.pfCandidateRef().isNonnull()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMVAID = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lMVAId"),
                                  method = cms.string('leg1.userFloat("idmva")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMVAIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lMVAIso"),
                                  method = cms.string('leg1.userFloat("isomva")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauRingMVAIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lRingMVAIso"),
                                  method = cms.string('leg1.userFloat("isoringsradmva")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauRelStdIso03 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lStdRelIso"),
                                  method = cms.string('(leg1.isolationR03.sumPt+leg1.isolationR03.emEt+leg1.isolationR03.hadEt)/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauRelPFIsoDB = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lPFIsoDB"),
                                  method = cms.string('(leg1.userIso(0)+max(leg1.photonIso()+leg1.neutralHadronIso()-0.5*leg1.puChargedHadronIso,0.0))/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDecayMode = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauDecayMode"),
                                  method = cms.string('leg2.decayMode()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMuTriggerMatch = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lTrigger"),
                                  method = cms.string('leg1.userFloat("hltOverlapFilterIsoMu18LooseIsoPFTau20")+leg1.userFloat("hltOverlapFilterIsoMu17LooseIsoPFTau20")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauTauTriggerMatch = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauTrigger"),
                                  method = cms.string('leg2.userFloat("hltOverlapFilterIsoMu18LooseIsoPFTau20")+leg2.userFloat("hltOverlapFilterIsoMu17LooseIsoPFTau20")'),
                                  #+leg2.userFloat("hltOverlapFilterIsoMu15IsoPFTau15")+
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPzeta = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pZeta"),
                                  method = cms.string('pZeta-1.5*pZetaVis'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPZ = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pZ"),
                                  method = cms.string('pZeta'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauPZV = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pZV"),
                                  method = cms.string('pZetaVis'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauHadMass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMass"),
                                  method = cms.string('leg2.mass()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauDecayFound = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauDecayFound"),
                                  method = cms.string('leg2.tauID("decayModeFinding")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVLooseIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauVLooseIso"),
                                  method = cms.string('leg2.tauID("byVLooseIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauLooseIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLooseIso"),
                                  method = cms.string('leg2.tauID("byLooseIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauLooseIsoMVA = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLooseMVAIso"),
                                  method = cms.string('leg2.tauID("byLooseIsolationMVA")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauRAWMVAIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMVAIso"),
                                  method = cms.string('leg2.tauID("byIsolationMVAraw")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMedIsoMVA = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMedMVAIso"),
                                  method = cms.string('leg2.tauID("byMediumIsolationMVA")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMediumIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMediumIso"),
                                  method = cms.string('leg2.tauID("byMediumIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauTightIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),

                                  tag = cms.string("tauTightIso"),
                                  method = cms.string('leg2.tauID("byTightIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauLooseDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLooseIsoDBPt"),
                                  method = cms.string('leg2.tauID("byLooseCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauVLooseDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauVLooseIsoDBPt"),
                                  method = cms.string('leg2.tauID("byVLooseCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauMediumDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMediumIsoDBPt"),
                                  method = cms.string('leg2.tauID("byMediumCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauTightDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauTightIsoDBPt"),
                                  method = cms.string('leg2.tauID("byTightCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauElectronTightMVA = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauElectronMVAPass"),
                                  method = cms.string('leg2.tauID("againstElectronTightMVA2")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauElectronVLMVA2Pass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauElectronVLooseMVA"),
                                  method = cms.string('leg2.tauID("againstElectronVLooseMVA2")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauH = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauH"),
                                  method = cms.string('leg2.leadPFChargedHadrCand().hcalEnergy()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauE = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauE"),
                                  method = cms.string('leg2.leadPFChargedHadrCand().ecalEnergy()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauP = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauP"),
                                  method = cms.string('leg2.leadPFChargedHadrCand().p()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsBTagCSVLPt20 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsBTagCSVLPt20"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>=0.244&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsBTagCSVMPt20 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsBTagCSVMPt20"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>=0.679&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsBTagCSVTPt20 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsBTagCSVTPt20"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>=0.898&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt30 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsPt30"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt30Tag = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt30"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt30TagMatch = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt30Matched"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta)<2.4&&abs(partonFlavour)==5'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt30TagNoMatch = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt30NotMatched"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta)<2.4&&abs(partonFlavour)!=5'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt20 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsPt20"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>20'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt20Tag = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt20"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt20TagMatch = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt20Matched"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>20&&abs(eta)<2.4&&abs(partonFlavour)==5'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauJetsPt20TagNoMatch = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt20NotMatched"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>20&&abs(eta)<2.4&&abs(partonFlavour)!=5'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauGenPt1 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genPt1"),
                                  method = cms.string('p4VisLeg1gen().pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauGenPt2 = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genPt2"),
                                  method = cms.string('p4VisLeg2gen().pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauGenVisMass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genVisMass"),
                                  method = cms.string('p4VisGen().M()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauGenMass = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genFullMass"),
                                  method = cms.string('p4gen().M()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauFirstJetPt = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetPt"),
                                  method = cms.string('pt()'),
                              ),
                              muTauFirstJetEta = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetEta"),
                                  method = cms.string('eta()'),
                              ),
                              muTauFirstJetID = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetID"),
                                  method = cms.string("userFloat('fullDiscriminant')"),
                              ),
                              muTauFirstJetFlavour = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetFlavour"),
                                  method = cms.string('partonFlavour()'),
                              ),
                              muTauFirstJetShape = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetShape"),
                                  method = cms.string('userFloat("ptRMS")'),
                              ),
                              muTauFirstJetChMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetNCharged"),
                                  method = cms.string('chargedMultiplicity()'),
                              ),
                              muTauFirstJetNeutMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetNNeutral"),
                                  method = cms.string('photonMultiplicity()+neutralHadronMultiplicity()'),
                              ),
                              PVs = cms.PSet(
                                    pluginType = cms.string("VertexSizeFiller"),
                                    src = cms.InputTag("primaryVertexFilter"),
                                    tag = cms.string("vertices")
                              ),
                              mumuSize = cms.PSet(
                                    pluginType = cms.string("CollectionSizeFiller"),
                                    src = cms.InputTag(srcLL),
                                    tag = cms.string("diLeptons"),
                              ),
                              genTaus = cms.PSet(
                                    pluginType = cms.string("CollectionSizeFiller"),
                                    src = cms.InputTag("genTauCands"),
                                    tag = cms.string("genTaus"),
                              ),
                              higgsPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src = cms.InputTag("genDaughters"),
                                  tag = cms.string("higgsPt"),
                                  method = cms.string('pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              muTauSize = cms.PSet(
                                    pluginType = cms.string("CollectionSizeFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("nCands"),
                              ),
                              muTauEmbedWeight = cms.PSet(
                                    pluginType = cms.string("EventWeightFiller"),
                                    src = cms.InputTag("generator","weight"),
                                    tag = cms.string("embeddedWeight"),
                              ),
                              muTauEmbedPt = cms.PSet(
                                    pluginType = cms.string("PATGenParticleFiller"),
                                    src = cms.InputTag("genDaughters"),
                                    tag = cms.string("embeddedPt"),
                                    method = cms.string("pt"),
                                    leadingOnly=cms.untracked.bool(False)

                              ),
                              muTauEmbedEta = cms.PSet(
                                    pluginType = cms.string("PATGenParticleFiller"),
                                    src = cms.InputTag("genDaughters"),
                                    tag = cms.string("embeddedEta"),
                                    method = cms.string("eta"),
                                    leadingOnly=cms.untracked.bool(False)
                              ),
                              muTauMVANoTrig = cms.PSet(
                                  pluginType = cms.string("PATMuTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lIDMVANonTrig"),
                                  method = cms.string('leg1.userFloat("mvaNonTrigV0")'),
                                  leadingOnly=cms.untracked.bool(True)
                              )
   )

   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)



#Tree for e+tau + MET final state
def addEleTauEventTree(process,name,src='eleTausSorted',srcLL='osDiElectrons',srcLT='eleTracksSorted',srcLG='eleGSFTracksSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              coreCollections = cms.VInputTag(
                                   cms.InputTag(src)
                              ),
                              trigger = cms.PSet(
                                  pluginType = cms.string("TriggerFiller"),
                                  src = cms.InputTag("patTrigger"),
                                  paths = cms.vstring(
                                      TriggerPaths
                                  )
                              ),
                              eleTauSize = cms.PSet(
                                    pluginType = cms.string("CollectionSizeFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("nCands"),
                              ),
                              pu = cms.PSet(
                                  pluginType = cms.string("PUFiller"),
                                  src = cms.InputTag("addPileupInfo"),
                                  tag = cms.string("pu"),
                              ),
                              eleTauRho = cms.PSet(
                                  pluginType = cms.string("EventWeightFiller"),
                                  src = cms.InputTag("kt6PFJetsForRhoComputationVoronoi","rho"),
                                  tag = cms.string("Rho")
                              ),
genTaus = cms.PSet(
                                    pluginType = cms.string("CollectionSizeFiller"),
                                    src = cms.InputTag("genTauCands"),
                                    tag = cms.string("genTaus"),
                              ),
                              eleTauPt1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pt1"),
                                  method = cms.string("leg1.pt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPdg1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pdg1"),
                                  method = cms.string("genPdg1()"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPdg2 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pdg2"),
                                  method = cms.string("genPdg2()"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPt2 = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("pt2"),
                                    method = cms.string("leg2.pt"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPt = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("pt"),
                                    method = cms.string("pt"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauEta1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("eta1"),
                                  method = cms.string("leg1.eta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauWW = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lWWID"),
                                  method = cms.string('leg1.userFloat("WWID")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauWWMVA = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lWWIDMVA"),
                                  method = cms.string('leg1.userFloat("MITID")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMVATrig = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lIDMVATrig"),
                                  method = cms.string('leg1.electronID("mvaTrigV0")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMVANoTrig = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lIDMVANonTrig"),
                                  method = cms.string('leg1.electronID("mvaNonTrigV0")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMVAIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lRingMVAIso"),
                                  method = cms.string('leg1.userFloat("isomva")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauEleTriggerMatch = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lTrigger"),
                                  method = cms.string('leg1.userFloat("hltOverlapFilterIsoEle20LooseIsoPFTau20")+leg1.userFloat("hltOverlapFilterIsoEle20WP90LooseIsoPFTau20")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTautauTriggerMatch = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauTrigger"),
                                  method = cms.string('leg2.userFloat("hltOverlapFilterIsoEle20LooseIsoPFTau20")+leg2.userFloat("hltOverlapFilterIsoEle20WP90LooseIsoPFTau20")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauEta2 = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("eta2"),
                                    method = cms.string("leg2.eta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauEleDXY = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("l1Dxy"),
                                  method = cms.string('leg1.userFloat("ipDXY")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPhi1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("phi1"),
                                  method = cms.string("leg1.phi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPhi2 = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("phi2"),
                                    method = cms.string("leg2.phi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauDZ = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dz"),
                                  method = cms.string('abs(leg1.userFloat("vz")-leg2.userFloat("vz"))'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauEledZ = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("l1dz"),
                                    method = cms.string('leg1.userFloat("dz")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauTaudZ = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("l2dz"),
                                    method = cms.string('leg2.userFloat("dz")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
# eleTauDCA = cms.PSet(
# pluginType = cms.string("PATEleTauPairFiller"),
# src = cms.InputTag(src),
# tag = cms.string("dca"),
# method = cms.string("dca"),
# leadingOnly=cms.untracked.bool(True)
# ),
# eleTauDist = cms.PSet(
# pluginType = cms.string("PATEleTauPairFiller"),
# src = cms.InputTag(src),
# tag = cms.string("xPointDist"),
# method = cms.string("dca"),
# leadingOnly=cms.untracked.bool(True)
# ),
                              eleTauEta = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("eta"),
                                    method = cms.string("eta"),
                                    leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauRelIso03B = cms.PSet(
                                    pluginType = cms.string("PATEleTauPairFiller"),
                                    src = cms.InputTag(src),
                                    tag = cms.string("lStandardRelIso"),
                                    method = cms.string("leg1.isEB()*((leg1.dr03TkSumPt()+max(leg1.dr03EcalRecHitSumEt()-1.0,0.0)+leg1.dr03HcalTowerSumEt())/leg1.pt())+leg1.isEE()*((leg1.dr03TkSumPt()+leg1.dr03EcalRecHitSumEt()+leg1.dr03HcalTowerSumEt())/leg1.pt())"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauCharge = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge"),
                                  method = cms.string("charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTaucharge1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge1"),
                                  method = cms.string("leg1.charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTaucharge2 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("charge2"),
                                  method = cms.string("leg2.charge"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mass"),
                                  method = cms.string("mass"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauSVMass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("svMass"),
                                  method = cms.string("svMass"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMT1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mt1"),
                                  method = cms.string("mt1MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMT2 = cms.PSet(
                                  pluginType =cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag =cms.string("mt2"),
                                  method =cms.string("mt2MET"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMET = cms.PSet(
                                  pluginType= cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag =cms.string("met"),
                                  method =cms.string("met.pt()"),
                                  leadingOnly=cms.untracked.bool(True)
                                  ),
                              eleTauDPhi = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag =cms.string("dPhi"),
                                  method =cms.string("dPhi12"),
                                  leadingOnly=cms.untracked.bool(True)
                                  ),
                              eleTauDPhi1MET = cms.PSet(
                                  pluginType =cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag =cms.string("dPhi1MET"),
                                  method =cms.string("dPhi1MET"),
                                  leadingOnly=cms.untracked.bool(True)
                                  ),
                              eleTauDPhi2MET = cms.PSet(
                                  pluginType =cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("dPhi2MET"),
                                  method = cms.string("dPhi2MET"),
                                  leadingOnly=cms.untracked.bool(True)
                                  ),
                              eleTauHT = cms.PSet(
                                  pluginType =cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("ht"),
                                  method =cms.string("ht"),
                                  leadingOnly=cms.untracked.bool(True)
                                  ),
                              eleTauPFRelIsoMVA = cms.PSet(
                                  pluginType =cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lPfRelIso"),
                                  method =cms.string('leg1.userFloat("isomva")'),
                                  leadingOnly=cms.untracked.bool(True)
                                  ),
                              eleTauRelPFIsoDB = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("lPFIsoDB"),
                                  method = cms.string('(leg1.userIso(0)+max(leg1.userIso(1)+leg1.neutralHadronIso()-0.5*leg1.userIso(2),0.0))/leg1.pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauProngs = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauProngs"),
                                  method = cms.string('leg2.signalPFChargedHadrCands.size()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauElectronDecision = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauTightElectronVeto"),
                                  method = cms.string('leg2.tauID("againstElectronTight")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauElectronMVAPass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauElectronMVAPass"),
                                  method = cms.string('leg2.tauID("againstElectronMVA")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauElectronMed = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauElectronMedPass"),
                                  method = cms.string('leg2.tauID("againstElectronMedium")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauElectronTightMVAPass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauElectronTightMVAPass"),
                                  method = cms.string('leg2.tauID("againstElectronTightMVA2")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPzeta = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pZeta"),
                                  method = cms.string('pZeta-1.5*pZetaVis'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPZ = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pZ"),
                                  method = cms.string('pZeta'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPZV = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("pZV"),
                                  method = cms.string('pZetaVis'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauProjMET = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("projMET"),
                                  method = cms.string('projMET'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauHadMass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMass"),
                                  method = cms.string('leg2.mass()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauDecayMode = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMode"),
                                  method = cms.string('leg2.decayMode()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauE = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauE"),
                                  method = cms.string('leg2.leadPFCand().ecalEnergy()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauH = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauH"),
                                  method = cms.string('leg2.leadPFCand().hcalEnergy()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauLC = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLCharge"),
                                  method = cms.string('leg2.leadPFCand().charge()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauPT = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauPT"),
                                  method = cms.string('leg2.leadPFCand().pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauCMVA = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauCMVA"),
                                  method = cms.string('leg2.leadPFChargedHadrCand().mva_e_pi()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauGammas = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauGammas"),
                                  method = cms.string('leg2.signalPFGammaCands.size()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVLooseIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauVLooseIso"),
                                  method = cms.string('leg2.tauID("byVLooseIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauLooseIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLooseIso"),
                                  method = cms.string('leg2.tauID("byLooseIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMediumIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMediumIso"),
                                  method = cms.string('leg2.tauID("byMediumIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauTightIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauTightIso"),
                                  method = cms.string('leg2.tauID("byTightIsolation")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauLooseIsoMVA = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLooseMVAIso"),
                                  method = cms.string('leg2.tauID("byLooseIsolationMVA")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauRAWMVAIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMVAIso"),
                                  method = cms.string('leg2.tauID("byIsolationMVAraw")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMedIsoMVA = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMedMVAIso"),
                                  method = cms.string('leg2.tauID("byMediumIsolationMVA")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauLooseDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauLooseIsoDBPt"),
                                  method = cms.string('leg2.tauID("byLooseCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVLooseDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauVLooseIsoDBPt"),
                                  method = cms.string('leg2.tauID("byVLooseCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauMediumDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauMediumIsoDBPt"),
                                  method = cms.string('leg2.tauID("byMediumCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauTightDBPtIso = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("tauTightIsoDBPt"),
                                  method = cms.string('leg2.tauID("byTightCombinedIsolationDeltaBetaCorr")'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJetsBTagCSVLPt20 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsBTagCSVLPt20"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>=0.244&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJetsBTagCSVMPt20 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsBTagCSVMPt20"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>=0.679&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJetsBTagCSVTPt20 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsBTagCSVTPt20"),
                                  method = cms.string('bDiscriminator("combinedSecondaryVertexBJetTags")>=0.898&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJets30 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsPt30"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJets30Tag = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt30"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJets30TagMatch = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt30Matched"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta)<2.4&&abs(partonFlavour)==5'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJets30TagNoMatch = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt30NotMatched"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>30&&abs(eta)<2.4&&abs(partonFlavour)!=5'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJJ = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("mJJ"),
                                  method = cms.string("mJJ"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJJPt = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("ptJJ"),
                                  method = cms.string("ptJJ"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),

                              eleTauJets20 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsPt20"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>20'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJets20Tag = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nTaggableJetsPt20"),
                                  method = cms.string('userInt("fullIdLoose")>0&&pt()>20&&abs(eta)<2.4'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFDEta = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDEta"),
                                  method = cms.string("vbfDEta"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFMass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfMass"),
                                  method = cms.string("vbfMass"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFMVA = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfMVA"),
                                  method = cms.string("vbfMVA"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFDPhi = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDPhi"),
                                  method = cms.string("vbfDPhi"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFDiTauPt = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDiTauPt"),
                                  method = cms.string("vbfDiTauPt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFDiJetPt = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDiJetPt"),
                                  method = cms.string("vbfDiJetPt"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFDPhiHJ = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfDPhiHJ"),
                                  method = cms.string("vbfDPhiHJ"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFC1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfC1"),
                                  method = cms.string("vbfC1"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFC2 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfC2"),
                                  method = cms.string("vbfC2"),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauVBFPt1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfPt1"),
                                  method = cms.string("vbfPt1"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              eleTauVBFPt2 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfPt2"),
                                  method = cms.string("vbfPt2"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              eleTauVBFEta1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfEta1"),
                                  method = cms.string("vbfEta1"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              eleTauVBFEta2 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfEta2"),
                                  method = cms.string("vbfEta2"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),

                              eleTauVBFJets20 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfNJetsGap20"),
                                  method = cms.string("vbfNJetsGap20"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              eleTauVBFJets30 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("vbfNJetsGap30"),
                                  method = cms.string("vbfNJetsGap30"),
                                  leadingOnly=cms.untracked.bool(True)
                               ),
                              eleTauJetsPt30 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsPt30"),
                                  method = cms.string('pt()>30'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauJetsPt20 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairJetCountFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("nJetsPt20"),
                                  method = cms.string('pt()>20'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauGenPt1 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genPt1"),
                                  method = cms.string('p4VisLeg1gen().pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauGenPt2 = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genPt2"),
                                  method = cms.string('p4VisLeg2gen().pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauGenVisMass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genVisMass"),
                                  method = cms.string('p4VisGen().M()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauGenMass = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("genMass"),
                                  method = cms.string('p4gen().M()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauFirstJetPt = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetPt"),
                                  method = cms.string('pt()'),
                              ),
                              eleTauFirstJetEta = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetEta"),
                                  method = cms.string('eta()'),
                              ),
                              eleTauFirstJetID = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetID"),
                                  method = cms.string("userFloat('fullDiscriminant')"),
                              ),
                              eleTauFirstJetFlavour = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetFlavour"),
                                  method = cms.string('partonFlavour()'),
                              ),
                              eleTauFirstJetShape = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetShape"),
                                  method = cms.string('userFloat("ptRMS")'),
                              ),
                              eleTauFirstJetChMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetNCharged"),
                                  method = cms.string('chargedMultiplicity()'),
                              ),
                              eleTauFirstJetNeutMultiplicity = cms.PSet(
                                  pluginType = cms.string("PATEleTauPairHighestPtJetVarFiller"),
                                  src = cms.InputTag(src),
                                  tag = cms.string("highestJetNNeutral"),
                                  method = cms.string('photonMultiplicity()+neutralHadronMultiplicity()'),
                              ),
                              PVs = cms.PSet(
                                    pluginType = cms.string("VertexSizeFiller"),
                                    src = cms.InputTag("primaryVertexFilter"),
                                    tag = cms.string("vertices")
                              ),
                              eleeleSize = cms.PSet(
                                    pluginType = cms.string("CollectionSizeFiller"),
                                    src = cms.InputTag(srcLL),
                                    tag = cms.string("diLeptons"),

                              ),
                              eleTauEmbedWeight = cms.PSet(
                                    pluginType = cms.string("EventWeightFiller"),
                                    src = cms.InputTag("generator","weight"),
                                    tag = cms.string("embeddedWeight"),
                              ),
                              higgsPt = cms.PSet(
                                  pluginType = cms.string("PATGenParticleFiller"),
                                  src = cms.InputTag("genDaughters"),
                                  tag = cms.string("higgsPt"),
                                  method = cms.string('pt()'),
                                  leadingOnly=cms.untracked.bool(True)
                              ),
                              eleTauEmbedPt = cms.PSet(
                                    pluginType = cms.string("PATGenParticleFiller"),
                                    src = cms.InputTag("genDaughters"),
                                    tag = cms.string("embeddedPt"),
                                    method = cms.string("pt"),
                                    leadingOnly=cms.untracked.bool(False)

                              ),
                              eleTauEmbedEta = cms.PSet(
                                    pluginType = cms.string("PATGenParticleFiller"),
                                    src = cms.InputTag("genDaughters"),
                                    tag = cms.string("embeddedEta"),
                                    method = cms.string("eta"),
                                    leadingOnly=cms.untracked.bool(False)
                              )
   )



   setattr(process, name, eventTree)
   p = cms.Path(getattr(process,name))
   setattr(process, name+'Path', p)
