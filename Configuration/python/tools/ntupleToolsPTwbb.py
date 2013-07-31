#!/bin/env py
import FWCore.ParameterSet.Config as cms

from UWAnalysis.Configuration.tools.analysisToolsPT import TriggerPaths

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

def forDataAndMC():
                              PVs = cms.PSet(
                                    pluginType = cms.string("VertexSizeFiller"),
                                    src = cms.InputTag("primaryVertexFilter"),
                                    tag = cms.string("vertices")
                              )
                              return PVs

def addMuNuEventTreePt(process,name,src = 'wCandsJets',srcZ = 'diMuonsSorted'):
   process.TFileService = cms.Service("TFileService", fileName = cms.string("analysis.root") )
   eventTree = cms.EDAnalyzer('EventTreeMaker',
                              coreCollections = cms.VInputTag(
                                   cms.InputTag(src)
                              ),
#                              PVs = cms.PSet(
#                                    pluginType = cms.string("VertexSizeFiller"),
#                                    src = cms.InputTag("primaryVertexFilter"),
#                                    tag = cms.string("vertices")
#                              ),
                              forDataAndMC(),
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
                                  #src = cms.InputTag("externalLHEProducer"), #use this for running over new patuples
                                  src = cms.InputTag("source"),  #use this for the old patuples
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



