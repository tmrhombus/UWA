//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Mon Jul  1 06:21:56 2013 by ROOT version 5.32/00
// from TTree eventTree/
// found on file: MuNuPAT-patTuple_cfg-620C9593-F8DC-E111-B81B-003048FFCBB0.root
//////////////////////////////////////////////////////////

#ifndef Event_h
#define Event_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include <vector>

// Fixed size dimensions of array or collections stored in the TTree if any.

class Event {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain
   TTree *tree;
   // Declaration of leaf types
   UInt_t          EVENT;
   UInt_t          RUN;
   UInt_t          LUMI;
   Float_t         hadMassZ;
   Float_t         DiSVMass;
   Float_t         DiSVPt;
   Float_t         J1Dmass;
   Float_t         J1D0mass;
   Float_t         J1DR;
   Float_t         J1Mu1Boost;
   Float_t         J1Mu1dxy;
   Float_t         J1SVeta;
   Float_t         J1SVM;
   Float_t         J1SVphi;
   Float_t         J1SVpt;
   Float_t         J1TRKdxy;
   Float_t         J1TRKdz;
   Float_t         J1nTracks;
   Float_t         J1Track1Pt;
   Float_t         J1Track2Pt;
   Float_t         J1Track3Pt;
   Float_t         J2Dmass;
   Float_t         J2D0mass;
   Float_t         J2DR;
   Float_t         J2Mu2Boost;
   Float_t         J2Mu1dxy;
   Float_t         J2SVeta;
   Float_t         J2SVM;
   Float_t         J2SVphi;
   Float_t         J2SVpt;
   Float_t         J2TRKdxy;
   Float_t         J2TRKdz;
   Float_t         J2nTracks;
   Float_t         J2Track1Pt;
   Float_t         J2Track2Pt;
   Float_t         J2Track3Pt;
   Int_t           vertices;
   Int_t           nBCand;
   Int_t           ncCands;
   Int_t           ncbarCands;
   Int_t           nElectrons;
   Int_t           genWs;
   Int_t           genBs;
   Int_t           genCs;
   Int_t           genDs;
   Int_t           genSs;
   Int_t           genUs;
   Float_t         l1DXY;
   Float_t         HMass1;
   Float_t         HMass2;
   Float_t         DiMuonMass;
   Float_t         l1PFIsoDB;
   Float_t         l2PFIsoDB;
   Float_t         l1StdRelIso;
   Float_t         l2StdRelIso;
   Float_t         l1eta;
   Float_t         l1phi;
   Float_t         l1pt;
   Float_t         l2eta;
   Float_t         l2phi;
   Float_t         l2pt;
   Float_t         J3CSVbtag;
   Float_t         EffWEIGHTCSVL;
   Float_t         EffWEIGHTCSVL2;
   Float_t         EffWEIGHTCSVM;
   Float_t         EffWEIGHTCSVM2;
   Float_t         EffWEIGHTCSVT;
   Float_t         EffWEIGHTCSVT2;
   Float_t         met;
   Float_t         muonCharge;
   Float_t         corMET;
   Float_t         MtCal;
   Float_t         muNuDPhi;
   Float_t         dz;
   Float_t         EffWEIGHTpt;
   Float_t         EffWEIGHTeta;
   Float_t         muonEta;
   Float_t         J1massBpm3;
   Float_t         J1massBpm3_charge;
   Float_t         J1massBpmE;
   Float_t         J1massBpm;
   Float_t         J1massBpm2;
   Float_t         J1ChargeMulti;
   Float_t         J1massD03;
   Float_t         J1massD0;
   Float_t         J1massDpm;
   Float_t         J1ElectronEnergy;
   Float_t         J1ElectronEnergyFrac;
   Float_t         J1EleMulti;
   Float_t         J1FlightDist;
   Float_t         J1errorFlightDist;
   Float_t         J1CSVMVAbtag;
   Float_t         J1CSVbtag;
   Float_t         J1Charge;
   Float_t         J1nCharges;
   Float_t         highestJetEta;
   Float_t         J1JetParton;
   Float_t         J1Mass;
   Float_t         highestJetPhi;
   Float_t         highestJetPt;
   Float_t         J1SSVHEbtag;
   Float_t         J1SVMass;
   Float_t         J1SVMassNegb;
   Float_t         J1SVMassb;
   Float_t         J1TCHEbtag;
   Float_t         J1TCHPbtag;
   Float_t         J1MuonEnergy;
   Float_t         J1MuEnergyFrac;
   Float_t         J1MuonMulti;
   Float_t         J1nTracksSSV;
   Float_t         J1nTracksSSVneg;
   Float_t         J1PhotonEnergy;
   Float_t         J1PhotonEnergyFrac;
   Float_t         J1PhotonMulti;
   Float_t         ht;
   Float_t         J1JetShape;
   Float_t         J1muon1pt;
   Float_t         J1Mu1ZMass;
   Float_t         J1muon2pt;
   Float_t         J2JetShape;
   Float_t         J2muon1pt;
   Float_t         J2Mu1ZMass;
   Float_t         J2muon2pt;
   Float_t         mJJ;
   Float_t         mJ3J4;
   Float_t         ptJJ;
   Int_t           nJetsPt20;
   Int_t           nJetsPt24;
   Int_t           nJetsPt25;
   Int_t           nJetsPt26;
   Int_t           nJetsPt30;
   Int_t           nJetsPt40;
   Int_t           LHEProduct;
   Float_t         MET;
   Float_t         Mt;
   Float_t         muNuRelPFIso;
   Float_t         PFIsoRho;
   Float_t         PFIsoVeto;
   Float_t         muonPhi;
   Float_t         WPt;
   Float_t         muNuRecoil;
   Float_t         lPFIsoDB;
   Float_t         muNuRelStdIso03;
   Float_t         EffWEIGHTSSVHEM;
   Float_t         EffWEIGHTSSVHEM2;
   Float_t         J2massBpm3;
   Float_t         J2massBpm3_charge;
   Float_t         J2massBpmE;
   Float_t         J2massBpm;
   Float_t         J2massBpm2;
   Float_t         J2ChargeMulti;
   Float_t         J2massD03;
   Float_t         J2massD0;
   Float_t         J2massDpm;
   Float_t         J2ElectronEnergy;
   Float_t         J2ElectronEnergyFrac;
   Float_t         J2EleMulti;
   Float_t         J2FlightDist;
   Float_t         J2errorFlightDist;
   Float_t         J2CSVMVAbtag;
   Float_t         J2CSVbtag;
   Float_t         J2Charge;
   Float_t         J2nCharges;
   Float_t         secondJetEta;
   Float_t         J2JetParton;
   Float_t         J2Mass;
   Float_t         secondJetPhi;
   Float_t         secondJetPt;
   Float_t         J2SSVHEbtag;
   Float_t         J2SVMass;
   Float_t         J2SVMassNegb;
   Float_t         J2SVMassb;
   Float_t         J2TCHEbtag;
   Float_t         J2TCHPbtag;
   Float_t         J2MuonEnergy;
   Float_t         J2MuEnergyFrac;
   Float_t         J2MuonMulti;
   Float_t         J2nTracksSSV;
   Float_t         J2nTracksSSVneg;
   Float_t         J2PhotonEnergy;
   Float_t         J2PhotonEnergyFrac;
   Float_t         J2PhotonMulti;
   Int_t           NWCands;
   Float_t         J3ChargeMulti;
   Float_t         J3ElectronEnergy;
   Float_t         J3ElectronEnergyFrac;
   Float_t         J3EleMulti;
   Float_t         J3Charge;
   Float_t         J3nCharges;
   Float_t         thirdJetEta;
   Float_t         J3JetParton;
   Float_t         J3Mass;
   Float_t         thirdJetPhi;
   Float_t         thirdJetPt;
   Float_t         J3TCHEbtag;
   Float_t         J3MuonEnergy;
   Float_t         J3MuEnergyFrac;
   Float_t         J3MuonMulti;
   Float_t         J3PhotonEnergy;
   Float_t         J3PhotonEnergyFrac;
   Float_t         J3PhotonMulti;
   Float_t         J1top;
   Float_t         leptonjj;
   Float_t         metjj;
   Int_t           nMuons;
   Float_t         muonPt;
   Float_t         nJets24to5;
   Float_t         nJets24Pt20;
   Float_t         nJets24Pt25;
   Float_t         nJets24Pt30;
   Float_t         puBXminus;
   Float_t         puTruth;
   Float_t         puBX0;
   Float_t         puBXplus;
   Int_t           nbHadrons;
   Int_t           HLT_IsoMu24_eta2p1_v_wasRun;
   Int_t           HLT_IsoMu24_eta2p1_v_fired;
   Int_t           HLT_IsoMu24_eta2p1_v_prescale;
   Int_t           HLT_IsoMu24_eta2p1_v_error;
   Int_t           HLT_Mu40_eta2p1_v_wasRun;
   Int_t           HLT_Mu40_eta2p1_v_fired;
   Int_t           HLT_Mu40_eta2p1_v_prescale;
   Int_t           HLT_Mu40_eta2p1_v_error;
   Int_t           HLT_Any;
   Float_t 	   weightFactor;	

   // List of branches
   TBranch        *b_EVENT;   //!
   TBranch        *b_RUN;   //!
   TBranch        *b_LUMI;   //!
   TBranch        *b_hadMassZ;   //!
   TBranch        *b_DiSVMass;   //!
   TBranch        *b_DiSVPt;   //!
   TBranch        *b_J1Dmass;   //!
   TBranch        *b_J1D0mass;   //!
   TBranch        *b_J1DR;   //!
   TBranch        *b_J1Mu1Boost;   //!
   TBranch        *b_J1Mu1dxy;   //!
   TBranch        *b_J1SVeta;   //!
   TBranch        *b_J1SVM;   //!
   TBranch        *b_J1SVphi;   //!
   TBranch        *b_J1SVpt;   //!
   TBranch        *b_J1TRKdxy;   //!
   TBranch        *b_J1TRKdz;   //!
   TBranch        *b_J1nTracks;   //!
   TBranch        *b_J1Track1Pt;   //!
   TBranch        *b_J1Track2Pt;   //!
   TBranch        *b_J1Track3Pt;   //!
   TBranch        *b_J2Dmass;   //!
   TBranch        *b_J2D0mass;   //!
   TBranch        *b_J2DR;   //!
   TBranch        *b_J2Mu2Boost;   //!
   TBranch        *b_J2Mu1dxy;   //!
   TBranch        *b_J2SVeta;   //!
   TBranch        *b_J2SVM;   //!
   TBranch        *b_J2SVphi;   //!
   TBranch        *b_J2SVpt;   //!
   TBranch        *b_J2TRKdxy;   //!
   TBranch        *b_J2TRKdz;   //!
   TBranch        *b_J2nTracks;   //!
   TBranch        *b_J2Track1Pt;   //!
   TBranch        *b_J2Track2Pt;   //!
   TBranch        *b_J2Track3Pt;   //!
   TBranch        *b_vertices;   //!
//   TBranch        *b_bCandidateEta;   //!
//   TBranch        *b_bCandidatePt;   //!
//   TBranch        *b_bCandidatePhi;   //!
//   TBranch        *b_nBCand;   //!
   TBranch        *b_ncCands;   //!
   TBranch        *b_ncbarCands;   //!
   TBranch        *b_nElectrons;   //!
   TBranch        *b_genWs;   //!
   TBranch        *b_genBs;   //!
   TBranch        *b_genCs;   //!
   TBranch        *b_genDs;   //!
   TBranch        *b_genSs;   //!
   TBranch        *b_genUs;   //!
   TBranch        *b_l1DXY;   //!
   TBranch        *b_HMass1;   //!
   TBranch        *b_HMass2;   //!
   TBranch        *b_DiMuonMass;   //!
   TBranch        *b_l1PFIsoDB;   //!
   TBranch        *b_l2PFIsoDB;   //!
   TBranch        *b_l1StdRelIso;   //!
   TBranch        *b_l2StdRelIso;   //!
   TBranch        *b_l1eta;   //!
   TBranch        *b_l1phi;   //!
   TBranch        *b_l1pt;   //!
   TBranch        *b_l2eta;   //!
   TBranch        *b_l2phi;   //!
   TBranch        *b_l2pt;   //!
   TBranch        *b_J3CSVbtag;   //!
   TBranch        *b_EffWEIGHTCSVL;   //!
   TBranch        *b_EffWEIGHTCSVL2;   //!
   TBranch        *b_EffWEIGHTCSVM;   //!
   TBranch        *b_EffWEIGHTCSVM2;   //!
   TBranch        *b_EffWEIGHTCSVT;   //!
   TBranch        *b_EffWEIGHTCSVT2;   //!
   TBranch        *b_met;   //!
   TBranch        *b_muonCharge;   //!
   TBranch        *b_corMET;   //!
   TBranch        *b_MtCal;   //!
   TBranch        *b_muNuDPhi;   //!
   TBranch        *b_dz;   //!
   TBranch        *b_EffWEIGHTpt;   //!
   TBranch        *b_EffWEIGHTeta;   //!
   TBranch        *b_muonEta;   //!
   TBranch        *b_J1massBpm3;   //!
   TBranch        *b_J1massBpm3_charge;   //!
   TBranch        *b_J1massBpmE;   //!
   TBranch        *b_J1massBpm;   //!
   TBranch        *b_J1massBpm2;   //!
   TBranch        *b_J1ChargeMulti;   //!
   TBranch        *b_J1massD03;   //!
   TBranch        *b_J1massD0;   //!
   TBranch        *b_J1massDpm;   //!
   TBranch        *b_J1ElectronEnergy;   //!
   TBranch        *b_J1ElectronEnergyFrac;   //!
   TBranch        *b_J1EleMulti;   //!
   TBranch        *b_J1FlightDist;   //!
   TBranch        *b_J1errorFlightDist;   //!
   TBranch        *b_J1CSVMVAbtag;   //!
   TBranch        *b_J1CSVbtag;   //!
   TBranch        *b_J1Charge;   //!
   TBranch        *b_J1nCharges;   //!
   TBranch        *b_highestJetEta;   //!
   TBranch        *b_J1JetParton;   //!
   TBranch        *b_J1Mass;   //!
   TBranch        *b_highestJetPhi;   //!
   TBranch        *b_highestJetPt;   //!
   TBranch        *b_J1SSVHEbtag;   //!
   TBranch        *b_J1SVMass;   //!
   TBranch        *b_J1SVMassNegb;   //!
   TBranch        *b_J1SVMassb;   //!
   TBranch        *b_J1TCHEbtag;   //!
   TBranch        *b_J1TCHPbtag;   //!
   TBranch        *b_J1MuonEnergy;   //!
   TBranch        *b_J1MuEnergyFrac;   //!
   TBranch        *b_J1MuonMulti;   //!
   TBranch        *b_J1nTracksSSV;   //!
   TBranch        *b_J1nTracksSSVneg;   //!
   TBranch        *b_J1PhotonEnergy;   //!
   TBranch        *b_J1PhotonEnergyFrac;   //!
   TBranch        *b_J1PhotonMulti;   //!
   TBranch        *b_ht;   //!
   TBranch        *b_J1JetShape;   //!
   TBranch        *b_J1muon1pt;   //!
   TBranch        *b_J1Mu1ZMass;   //!
   TBranch        *b_J1muon2pt;   //!
   TBranch        *b_J2JetShape;   //!
   TBranch        *b_J2muon1pt;   //!
   TBranch        *b_J2Mu1ZMass;   //!
   TBranch        *b_J2muon2pt;   //!
   TBranch        *b_mJJ;   //!
   TBranch        *b_mJ3J4;   //!
   TBranch        *b_ptJJ;   //!
   TBranch        *b_nJetsPt20;   //!
   TBranch        *b_nJetsPt24;   //!
   TBranch        *b_nJetsPt25;   //!
   TBranch        *b_nJetsPt26;   //!
   TBranch        *b_nJetsPt30;   //!
   TBranch        *b_nJetsPt40;   //!
   TBranch        *b_LHEProduct;   //!
   TBranch        *b_MET;   //!
   TBranch        *b_Mt;   //!
   TBranch        *b_muNuRelPFIso;   //!
   TBranch        *b_PFIsoRho;   //!
   TBranch        *b_PFIsoVeto;   //!
   TBranch        *b_muonPhi;   //!
   TBranch        *b_WPt;   //!
   TBranch        *b_muNuRecoil;   //!
   TBranch        *b_lPFIsoDB;   //!
   TBranch        *b_muNuRelStdIso03;   //!
   TBranch        *b_EffWEIGHTSSVHEM;   //!
   TBranch        *b_EffWEIGHTSSVHEM2;   //!
   TBranch        *b_J2massBpm3;   //!
   TBranch        *b_J2massBpm3_charge;   //!
   TBranch        *b_J2massBpmE;   //!
   TBranch        *b_J2massBpm;   //!
   TBranch        *b_J2massBpm2;   //!
   TBranch        *b_J2ChargeMulti;   //!
   TBranch        *b_J2massD03;   //!
   TBranch        *b_J2massD0;   //!
   TBranch        *b_J2massDpm;   //!
   TBranch        *b_J2ElectronEnergy;   //!
   TBranch        *b_J2ElectronEnergyFrac;   //!
   TBranch        *b_J2EleMulti;   //!
   TBranch        *b_J2FlightDist;   //!
   TBranch        *b_J2errorFlightDist;   //!
   TBranch        *b_J2CSVMVAbtag;   //!
   TBranch        *b_J2CSVbtag;   //!
   TBranch        *b_J2Charge;   //!
   TBranch        *b_J2nCharges;   //!
   TBranch        *b_secondJetEta;   //!
   TBranch        *b_J2JetParton;   //!
   TBranch        *b_J2Mass;   //!
   TBranch        *b_secondJetPhi;   //!
   TBranch        *b_secondJetPt;   //!
   TBranch        *b_J2SSVHEbtag;   //!
   TBranch        *b_J2SVMass;   //!
   TBranch        *b_J2SVMassNegb;   //!
   TBranch        *b_J2SVMassb;   //!
   TBranch        *b_J2TCHEbtag;   //!
   TBranch        *b_J2TCHPbtag;   //!
   TBranch        *b_J2MuonEnergy;   //!
   TBranch        *b_J2MuEnergyFrac;   //!
   TBranch        *b_J2MuonMulti;   //!
   TBranch        *b_J2nTracksSSV;   //!
   TBranch        *b_J2nTracksSSVneg;   //!
   TBranch        *b_J2PhotonEnergy;   //!
   TBranch        *b_J2PhotonEnergyFrac;   //!
   TBranch        *b_J2PhotonMulti;   //!
   TBranch        *b_NWCands;   //!
   TBranch        *b_J3ChargeMulti;   //!
   TBranch        *b_J3ElectronEnergy;   //!
   TBranch        *b_J3ElectronEnergyFrac;   //!
   TBranch        *b_J3EleMulti;   //!
   TBranch        *b_J3Charge;   //!
   TBranch        *b_J3nCharges;   //!
   TBranch        *b_thirdJetEta;   //!
   TBranch        *b_J3JetParton;   //!
   TBranch        *b_J3Mass;   //!
   TBranch        *b_thirdJetPhi;   //!
   TBranch        *b_thirdJetPt;   //!
   TBranch        *b_J3TCHEbtag;   //!
   TBranch        *b_J3MuonEnergy;   //!
   TBranch        *b_J3MuEnergyFrac;   //!
   TBranch        *b_J3MuonMulti;   //!
   TBranch        *b_J3PhotonEnergy;   //!
   TBranch        *b_J3PhotonEnergyFrac;   //!
   TBranch        *b_J3PhotonMulti;   //!
   TBranch        *b_J1top;   //!
   TBranch        *b_leptonjj;   //!
   TBranch        *b_metjj;   //!
   TBranch        *b_nMuons;   //!
   TBranch        *b_muonPt;   //!
   TBranch        *b_nJets24to5;   //!
   TBranch        *b_nJets24Pt20;   //!
   TBranch        *b_nJets24Pt25;   //!
   TBranch        *b_nJets24Pt30;   //!
   TBranch        *b_puBXminus;   //!
   TBranch        *b_puTruth;   //!
   TBranch        *b_puBX0;   //!
   TBranch        *b_puBXplus;   //!
   TBranch        *b_bHadronsEta;   //!
   TBranch        *b_bHadronsPt;   //!
   TBranch        *b_bHadronsPhi;   //!
   TBranch        *b_nbHadrons;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_wasRun;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_fired;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_prescale;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_error;   //!
   TBranch        *b_HLT_Mu40_eta2p1_v_wasRun;   //!
   TBranch        *b_HLT_Mu40_eta2p1_v_fired;   //!
   TBranch        *b_HLT_Mu40_eta2p1_v_prescale;   //!
   TBranch        *b_HLT_Mu40_eta2p1_v_error;   //!
   TBranch        *b_HLT_Any;   //!
   TBranch        *b_weightFactor;
   Int_t NEvent;

   Event( TString filename );
   virtual ~Event();
   virtual Int_t    Cut(Long64_t entry);
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop();
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);

   virtual Float_t  StringToFloat(TString VarString);
};

#endif

#ifdef Event_cxx

Event::Event( TString filename )
{

  tree = 0;
  
  if (tree == 0) {
    TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject(filename);
      if (!f) {
         f = new TFile(filename);
      }
      tree = (TTree*)gDirectory->Get("muNuEventTree/eventTree");
//	cout<<"The number of events is ";
 //  	TH1F *eventNumber=(TH1F*)f->Get("summary/results");
//	cout<<eventNumber->GetBinContent(1)<<endl;
   }
   Init(tree);
}

Event::~Event()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t Event::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t Event::LoadTree(Long64_t entry)
{
// Set the environment to read one entry
   if (!fChain) return -5;
   Long64_t centry = fChain->LoadTree(entry);
   if (centry < 0) return centry;
   if (fChain->GetTreeNumber() != fCurrent) {
      fCurrent = fChain->GetTreeNumber();
      Notify();
   }
   return centry;
}

void Event::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).

   // Set object pointer
//   bCandidateEta = 0;
//   bCandidatePt = 0;
//   bCandidatePhi = 0;
//   bHadronsEta = 0;
//   bHadronsPt = 0;
//   bHadronsPhi = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);



   fChain->SetBranchAddress("EVENT", &EVENT, &b_EVENT);
   fChain->SetBranchAddress("RUN", &RUN, &b_RUN);
   fChain->SetBranchAddress("LUMI", &LUMI, &b_LUMI);
   fChain->SetBranchAddress("hadMassZ", &hadMassZ, &b_hadMassZ);
   fChain->SetBranchAddress("DiSVMass", &DiSVMass, &b_DiSVMass);
   fChain->SetBranchAddress("DiSVPt", &DiSVPt, &b_DiSVPt);
   fChain->SetBranchAddress("J1Dmass", &J1Dmass, &b_J1Dmass);
   fChain->SetBranchAddress("J1D0mass", &J1D0mass, &b_J1D0mass);
   fChain->SetBranchAddress("J1DR", &J1DR, &b_J1DR);
   fChain->SetBranchAddress("J1Mu1Boost", &J1Mu1Boost, &b_J1Mu1Boost);
   fChain->SetBranchAddress("J1Mu1dxy", &J1Mu1dxy, &b_J1Mu1dxy);
   fChain->SetBranchAddress("J1SVeta", &J1SVeta, &b_J1SVeta);
   fChain->SetBranchAddress("J1SVM", &J1SVM, &b_J1SVM);
   fChain->SetBranchAddress("J1SVphi", &J1SVphi, &b_J1SVphi);
   fChain->SetBranchAddress("J1SVpt", &J1SVpt, &b_J1SVpt);
   fChain->SetBranchAddress("J1TRKdxy", &J1TRKdxy, &b_J1TRKdxy);
   fChain->SetBranchAddress("J1TRKdz", &J1TRKdz, &b_J1TRKdz);
   fChain->SetBranchAddress("J1nTracks", &J1nTracks, &b_J1nTracks);
   fChain->SetBranchAddress("J1Track1Pt", &J1Track1Pt, &b_J1Track1Pt);
   fChain->SetBranchAddress("J1Track2Pt", &J1Track2Pt, &b_J1Track2Pt);
   fChain->SetBranchAddress("J1Track3Pt", &J1Track3Pt, &b_J1Track3Pt);
   fChain->SetBranchAddress("J2Dmass", &J2Dmass, &b_J2Dmass);
   fChain->SetBranchAddress("J2D0mass", &J2D0mass, &b_J2D0mass);
   fChain->SetBranchAddress("J2DR", &J2DR, &b_J2DR);
   fChain->SetBranchAddress("J2Mu2Boost", &J2Mu2Boost, &b_J2Mu2Boost);
   fChain->SetBranchAddress("J2Mu1dxy", &J2Mu1dxy, &b_J2Mu1dxy);
   fChain->SetBranchAddress("J2SVeta", &J2SVeta, &b_J2SVeta);
   fChain->SetBranchAddress("J2SVM", &J2SVM, &b_J2SVM);
   fChain->SetBranchAddress("J2SVphi", &J2SVphi, &b_J2SVphi);
   fChain->SetBranchAddress("J2SVpt", &J2SVpt, &b_J2SVpt);
   fChain->SetBranchAddress("J2TRKdxy", &J2TRKdxy, &b_J2TRKdxy);
   fChain->SetBranchAddress("J2TRKdz", &J2TRKdz, &b_J2TRKdz);
   fChain->SetBranchAddress("J2nTracks", &J2nTracks, &b_J2nTracks);
   fChain->SetBranchAddress("J2Track1Pt", &J2Track1Pt, &b_J2Track1Pt);
   fChain->SetBranchAddress("J2Track2Pt", &J2Track2Pt, &b_J2Track2Pt);
   fChain->SetBranchAddress("J2Track3Pt", &J2Track3Pt, &b_J2Track3Pt);
   fChain->SetBranchAddress("vertices", &vertices, &b_vertices);
/*   fChain->SetBranchAddress("bCandidateEta", &bCandidateEta, &b_bCandidateEta);
   fChain->SetBranchAddress("bCandidatePt", &bCandidatePt, &b_bCandidatePt);
   fChain->SetBranchAddress("bCandidatePhi", &bCandidatePhi, &b_bCandidatePhi);
   fChain->SetBranchAddress("nBCand", &nBCand, &b_nBCand);
*/   fChain->SetBranchAddress("ncCands", &ncCands, &b_ncCands);
   fChain->SetBranchAddress("ncbarCands", &ncbarCands, &b_ncbarCands);
   fChain->SetBranchAddress("nElectrons", &nElectrons, &b_nElectrons);
   fChain->SetBranchAddress("genWs", &genWs, &b_genWs);
   fChain->SetBranchAddress("genBs", &genBs, &b_genBs);
   fChain->SetBranchAddress("genCs", &genCs, &b_genCs);
   fChain->SetBranchAddress("genDs", &genDs, &b_genDs);
   fChain->SetBranchAddress("genSs", &genSs, &b_genSs);
   fChain->SetBranchAddress("genUs", &genUs, &b_genUs);
   fChain->SetBranchAddress("l1DXY", &l1DXY, &b_l1DXY);
   fChain->SetBranchAddress("HMass1", &HMass1, &b_HMass1);
   fChain->SetBranchAddress("HMass2", &HMass2, &b_HMass2);
   fChain->SetBranchAddress("DiMuonMass", &DiMuonMass, &b_DiMuonMass);
   fChain->SetBranchAddress("l1PFIsoDB", &l1PFIsoDB, &b_l1PFIsoDB);
   fChain->SetBranchAddress("l2PFIsoDB", &l2PFIsoDB, &b_l2PFIsoDB);
   fChain->SetBranchAddress("l1StdRelIso", &l1StdRelIso, &b_l1StdRelIso);
   fChain->SetBranchAddress("l2StdRelIso", &l2StdRelIso, &b_l2StdRelIso);
   fChain->SetBranchAddress("l1eta", &l1eta, &b_l1eta);
   fChain->SetBranchAddress("l1phi", &l1phi, &b_l1phi);
   fChain->SetBranchAddress("l1pt", &l1pt, &b_l1pt);
   fChain->SetBranchAddress("l2eta", &l2eta, &b_l2eta);
   fChain->SetBranchAddress("l2phi", &l2phi, &b_l2phi);
   fChain->SetBranchAddress("l2pt", &l2pt, &b_l2pt);
   fChain->SetBranchAddress("J3CSVbtag", &J3CSVbtag, &b_J3CSVbtag);
   fChain->SetBranchAddress("EffWEIGHTCSVL", &EffWEIGHTCSVL, &b_EffWEIGHTCSVL);
   fChain->SetBranchAddress("EffWEIGHTCSVL2", &EffWEIGHTCSVL2, &b_EffWEIGHTCSVL2);
   fChain->SetBranchAddress("EffWEIGHTCSVM", &EffWEIGHTCSVM, &b_EffWEIGHTCSVM);
   fChain->SetBranchAddress("EffWEIGHTCSVM2", &EffWEIGHTCSVM2, &b_EffWEIGHTCSVM2);
   fChain->SetBranchAddress("EffWEIGHTCSVT", &EffWEIGHTCSVT, &b_EffWEIGHTCSVT);
   fChain->SetBranchAddress("EffWEIGHTCSVT2", &EffWEIGHTCSVT2, &b_EffWEIGHTCSVT2);
   fChain->SetBranchAddress("met", &met, &b_met);
   fChain->SetBranchAddress("muonCharge", &muonCharge, &b_muonCharge);
   fChain->SetBranchAddress("corMET", &corMET, &b_corMET);
   fChain->SetBranchAddress("MtCal", &MtCal, &b_MtCal);
   fChain->SetBranchAddress("muNuDPhi", &muNuDPhi, &b_muNuDPhi);
   fChain->SetBranchAddress("dz", &dz, &b_dz);
   fChain->SetBranchAddress("EffWEIGHTpt", &EffWEIGHTpt, &b_EffWEIGHTpt);
   fChain->SetBranchAddress("EffWEIGHTeta", &EffWEIGHTeta, &b_EffWEIGHTeta);
   fChain->SetBranchAddress("muonEta", &muonEta, &b_muonEta);
   fChain->SetBranchAddress("J1massBpm3", &J1massBpm3, &b_J1massBpm3);
   fChain->SetBranchAddress("J1massBpm3_charge", &J1massBpm3_charge, &b_J1massBpm3_charge);
   fChain->SetBranchAddress("J1massBpmE", &J1massBpmE, &b_J1massBpmE);
   fChain->SetBranchAddress("J1massBpm", &J1massBpm, &b_J1massBpm);
   fChain->SetBranchAddress("J1massBpm2", &J1massBpm2, &b_J1massBpm2);
   fChain->SetBranchAddress("J1ChargeMulti", &J1ChargeMulti, &b_J1ChargeMulti);
   fChain->SetBranchAddress("J1massD03", &J1massD03, &b_J1massD03);
   fChain->SetBranchAddress("J1massD0", &J1massD0, &b_J1massD0);
   fChain->SetBranchAddress("J1massDpm", &J1massDpm, &b_J1massDpm);
   fChain->SetBranchAddress("J1ElectronEnergy", &J1ElectronEnergy, &b_J1ElectronEnergy);
   fChain->SetBranchAddress("J1ElectronEnergyFrac", &J1ElectronEnergyFrac, &b_J1ElectronEnergyFrac);
   fChain->SetBranchAddress("J1EleMulti", &J1EleMulti, &b_J1EleMulti);
   fChain->SetBranchAddress("J1FlightDist", &J1FlightDist, &b_J1FlightDist);
   fChain->SetBranchAddress("J1errorFlightDist", &J1errorFlightDist, &b_J1errorFlightDist);
   fChain->SetBranchAddress("J1CSVMVAbtag", &J1CSVMVAbtag, &b_J1CSVMVAbtag);
   fChain->SetBranchAddress("J1CSVbtag", &J1CSVbtag, &b_J1CSVbtag);
   fChain->SetBranchAddress("J1Charge", &J1Charge, &b_J1Charge);
   fChain->SetBranchAddress("J1nCharges", &J1nCharges, &b_J1nCharges);
   fChain->SetBranchAddress("highestJetEta", &highestJetEta, &b_highestJetEta);
   fChain->SetBranchAddress("J1JetParton", &J1JetParton, &b_J1JetParton);
   fChain->SetBranchAddress("J1Mass", &J1Mass, &b_J1Mass);
   fChain->SetBranchAddress("highestJetPhi", &highestJetPhi, &b_highestJetPhi);
   fChain->SetBranchAddress("highestJetPt", &highestJetPt, &b_highestJetPt);
   fChain->SetBranchAddress("J1SSVHEbtag", &J1SSVHEbtag, &b_J1SSVHEbtag);
   fChain->SetBranchAddress("J1SVMass", &J1SVMass, &b_J1SVMass);
   fChain->SetBranchAddress("J1SVMassNegb", &J1SVMassNegb, &b_J1SVMassNegb);
   fChain->SetBranchAddress("J1SVMassb", &J1SVMassb, &b_J1SVMassb);
   fChain->SetBranchAddress("J1TCHEbtag", &J1TCHEbtag, &b_J1TCHEbtag);
   fChain->SetBranchAddress("J1TCHPbtag", &J1TCHPbtag, &b_J1TCHPbtag);
   fChain->SetBranchAddress("J1MuonEnergy", &J1MuonEnergy, &b_J1MuonEnergy);
   fChain->SetBranchAddress("J1MuEnergyFrac", &J1MuEnergyFrac, &b_J1MuEnergyFrac);
   fChain->SetBranchAddress("J1MuonMulti", &J1MuonMulti, &b_J1MuonMulti);
   fChain->SetBranchAddress("J1nTracksSSV", &J1nTracksSSV, &b_J1nTracksSSV);
   fChain->SetBranchAddress("J1nTracksSSVneg", &J1nTracksSSVneg, &b_J1nTracksSSVneg);
   fChain->SetBranchAddress("J1PhotonEnergy", &J1PhotonEnergy, &b_J1PhotonEnergy);
   fChain->SetBranchAddress("J1PhotonEnergyFrac", &J1PhotonEnergyFrac, &b_J1PhotonEnergyFrac);
   fChain->SetBranchAddress("J1PhotonMulti", &J1PhotonMulti, &b_J1PhotonMulti);
   fChain->SetBranchAddress("ht", &ht, &b_ht);
   fChain->SetBranchAddress("J1JetShape", &J1JetShape, &b_J1JetShape);
   fChain->SetBranchAddress("J1muon1pt", &J1muon1pt, &b_J1muon1pt);
   fChain->SetBranchAddress("J1Mu1ZMass", &J1Mu1ZMass, &b_J1Mu1ZMass);
   fChain->SetBranchAddress("J1muon2pt", &J1muon2pt, &b_J1muon2pt);
   fChain->SetBranchAddress("J2JetShape", &J2JetShape, &b_J2JetShape);
   fChain->SetBranchAddress("J2muon1pt", &J2muon1pt, &b_J2muon1pt);
   fChain->SetBranchAddress("J2Mu1ZMass", &J2Mu1ZMass, &b_J2Mu1ZMass);
   fChain->SetBranchAddress("J2muon2pt", &J2muon2pt, &b_J2muon2pt);
//   fChain->SetBranchAddress("mJJ", &mJJ, &b_mJJ);
   fChain->SetBranchAddress("mJJ", &mJJ, &b_mJJ);
   fChain->SetBranchAddress("mJ3J4", &mJ3J4, &b_mJ3J4);
   fChain->SetBranchAddress("ptJJ", &ptJJ, &b_ptJJ);
   fChain->SetBranchAddress("nJetsPt20", &nJetsPt20, &b_nJetsPt20);
   fChain->SetBranchAddress("nJetsPt24", &nJetsPt24, &b_nJetsPt24);
   fChain->SetBranchAddress("nJetsPt25", &nJetsPt25, &b_nJetsPt25);
   fChain->SetBranchAddress("nJetsPt26", &nJetsPt26, &b_nJetsPt26);
   fChain->SetBranchAddress("nJetsPt30", &nJetsPt30, &b_nJetsPt30);
   fChain->SetBranchAddress("nJetsPt40", &nJetsPt40, &b_nJetsPt40);
   fChain->SetBranchAddress("LHEProduct", &LHEProduct, &b_LHEProduct);
   fChain->SetBranchAddress("MET", &MET, &b_MET);
   fChain->SetBranchAddress("Mt", &Mt, &b_Mt);
   fChain->SetBranchAddress("muNuRelPFIso", &muNuRelPFIso, &b_muNuRelPFIso);
   fChain->SetBranchAddress("PFIsoRho", &PFIsoRho, &b_PFIsoRho);
   fChain->SetBranchAddress("PFIsoVeto", &PFIsoVeto, &b_PFIsoVeto);
   fChain->SetBranchAddress("muonPhi", &muonPhi, &b_muonPhi);
   fChain->SetBranchAddress("WPt", &WPt, &b_WPt);
   fChain->SetBranchAddress("muNuRecoil", &muNuRecoil, &b_muNuRecoil);
   fChain->SetBranchAddress("lPFIsoDB", &lPFIsoDB, &b_lPFIsoDB);
   fChain->SetBranchAddress("muNuRelStdIso03", &muNuRelStdIso03, &b_muNuRelStdIso03);
   fChain->SetBranchAddress("EffWEIGHTSSVHEM", &EffWEIGHTSSVHEM, &b_EffWEIGHTSSVHEM);
   fChain->SetBranchAddress("EffWEIGHTSSVHEM2", &EffWEIGHTSSVHEM2, &b_EffWEIGHTSSVHEM2);
   fChain->SetBranchAddress("J2massBpm3", &J2massBpm3, &b_J2massBpm3);
   fChain->SetBranchAddress("J2massBpm3_charge", &J2massBpm3_charge, &b_J2massBpm3_charge);
   fChain->SetBranchAddress("J2massBpmE", &J2massBpmE, &b_J2massBpmE);
   fChain->SetBranchAddress("J2massBpm", &J2massBpm, &b_J2massBpm);
   fChain->SetBranchAddress("J2massBpm2", &J2massBpm2, &b_J2massBpm2);
   fChain->SetBranchAddress("J2ChargeMulti", &J2ChargeMulti, &b_J2ChargeMulti);
   fChain->SetBranchAddress("J2massD03", &J2massD03, &b_J2massD03);
   fChain->SetBranchAddress("J2massD0", &J2massD0, &b_J2massD0);
   fChain->SetBranchAddress("J2massDpm", &J2massDpm, &b_J2massDpm);
   fChain->SetBranchAddress("J2ElectronEnergy", &J2ElectronEnergy, &b_J2ElectronEnergy);
   fChain->SetBranchAddress("J2ElectronEnergyFrac", &J2ElectronEnergyFrac, &b_J2ElectronEnergyFrac);
   fChain->SetBranchAddress("J2EleMulti", &J2EleMulti, &b_J2EleMulti);
   fChain->SetBranchAddress("J2FlightDist", &J2FlightDist, &b_J2FlightDist);
   fChain->SetBranchAddress("J2errorFlightDist", &J2errorFlightDist, &b_J2errorFlightDist);
   fChain->SetBranchAddress("J2CSVMVAbtag", &J2CSVMVAbtag, &b_J2CSVMVAbtag);
   fChain->SetBranchAddress("J2CSVbtag", &J2CSVbtag, &b_J2CSVbtag);
   fChain->SetBranchAddress("J2Charge", &J2Charge, &b_J2Charge);
   fChain->SetBranchAddress("J2nCharges", &J2nCharges, &b_J2nCharges);
   fChain->SetBranchAddress("secondJetEta", &secondJetEta, &b_secondJetEta);
   fChain->SetBranchAddress("J2JetParton", &J2JetParton, &b_J2JetParton);
   fChain->SetBranchAddress("J2Mass", &J2Mass, &b_J2Mass);
   fChain->SetBranchAddress("secondJetPhi", &secondJetPhi, &b_secondJetPhi);
   fChain->SetBranchAddress("secondJetPt", &secondJetPt, &b_secondJetPt);
   fChain->SetBranchAddress("J2SSVHEbtag", &J2SSVHEbtag, &b_J2SSVHEbtag);
   fChain->SetBranchAddress("J2SVMass", &J2SVMass, &b_J2SVMass);
   fChain->SetBranchAddress("J2SVMassNegb", &J2SVMassNegb, &b_J2SVMassNegb);
   fChain->SetBranchAddress("J2SVMassb", &J2SVMassb, &b_J2SVMassb);
   fChain->SetBranchAddress("J2TCHEbtag", &J2TCHEbtag, &b_J2TCHEbtag);
   fChain->SetBranchAddress("J2TCHPbtag", &J2TCHPbtag, &b_J2TCHPbtag);
   fChain->SetBranchAddress("J2MuonEnergy", &J2MuonEnergy, &b_J2MuonEnergy);
   fChain->SetBranchAddress("J2MuEnergyFrac", &J2MuEnergyFrac, &b_J2MuEnergyFrac);
   fChain->SetBranchAddress("J2MuonMulti", &J2MuonMulti, &b_J2MuonMulti);
   fChain->SetBranchAddress("J2nTracksSSV", &J2nTracksSSV, &b_J2nTracksSSV);
   fChain->SetBranchAddress("J2nTracksSSVneg", &J2nTracksSSVneg, &b_J2nTracksSSVneg);
   fChain->SetBranchAddress("J2PhotonEnergy", &J2PhotonEnergy, &b_J2PhotonEnergy);
   fChain->SetBranchAddress("J2PhotonEnergyFrac", &J2PhotonEnergyFrac, &b_J2PhotonEnergyFrac);
   fChain->SetBranchAddress("J2PhotonMulti", &J2PhotonMulti, &b_J2PhotonMulti);
   fChain->SetBranchAddress("NWCands", &NWCands, &b_NWCands);
   fChain->SetBranchAddress("J3ChargeMulti", &J3ChargeMulti, &b_J3ChargeMulti);
   fChain->SetBranchAddress("J3ElectronEnergy", &J3ElectronEnergy, &b_J3ElectronEnergy);
   fChain->SetBranchAddress("J3ElectronEnergyFrac", &J3ElectronEnergyFrac, &b_J3ElectronEnergyFrac);
   fChain->SetBranchAddress("J3EleMulti", &J3EleMulti, &b_J3EleMulti);
   fChain->SetBranchAddress("J3Charge", &J3Charge, &b_J3Charge);
   fChain->SetBranchAddress("J3nCharges", &J3nCharges, &b_J3nCharges);
   fChain->SetBranchAddress("thirdJetEta", &thirdJetEta, &b_thirdJetEta);
   fChain->SetBranchAddress("J3JetParton", &J3JetParton, &b_J3JetParton);
   fChain->SetBranchAddress("J3Mass", &J3Mass, &b_J3Mass);
   fChain->SetBranchAddress("thirdJetPhi", &thirdJetPhi, &b_thirdJetPhi);
   fChain->SetBranchAddress("thirdJetPt", &thirdJetPt, &b_thirdJetPt);
   fChain->SetBranchAddress("J3TCHEbtag", &J3TCHEbtag, &b_J3TCHEbtag);
   fChain->SetBranchAddress("J3MuonEnergy", &J3MuonEnergy, &b_J3MuonEnergy);
   fChain->SetBranchAddress("J3MuEnergyFrac", &J3MuEnergyFrac, &b_J3MuEnergyFrac);
   fChain->SetBranchAddress("J3MuonMulti", &J3MuonMulti, &b_J3MuonMulti);
   fChain->SetBranchAddress("J3PhotonEnergy", &J3PhotonEnergy, &b_J3PhotonEnergy);
   fChain->SetBranchAddress("J3PhotonEnergyFrac", &J3PhotonEnergyFrac, &b_J3PhotonEnergyFrac);
   fChain->SetBranchAddress("J3PhotonMulti", &J3PhotonMulti, &b_J3PhotonMulti);
   fChain->SetBranchAddress("J1top", &J1top, &b_J1top);
   fChain->SetBranchAddress("leptonjj", &leptonjj, &b_leptonjj);
   fChain->SetBranchAddress("metjj", &metjj, &b_metjj);
   fChain->SetBranchAddress("nMuons", &nMuons, &b_nMuons);
   fChain->SetBranchAddress("muonPt", &muonPt, &b_muonPt);
   fChain->SetBranchAddress("nJets24to5", &nJets24to5, &b_nJets24to5);
   fChain->SetBranchAddress("nJets24Pt20", &nJets24Pt20, &b_nJets24Pt20);
   fChain->SetBranchAddress("nJets24Pt25", &nJets24Pt25, &b_nJets24Pt25);
   fChain->SetBranchAddress("nJets24Pt30", &nJets24Pt30, &b_nJets24Pt30);
   fChain->SetBranchAddress("puBXminus", &puBXminus, &b_puBXminus);
   fChain->SetBranchAddress("puTruth", &puTruth, &b_puTruth);
   fChain->SetBranchAddress("puBX0", &puBX0, &b_puBX0);
   fChain->SetBranchAddress("puBXplus", &puBXplus, &b_puBXplus);
/*   fChain->SetBranchAddress("bHadronsEta", &bHadronsEta, &b_bHadronsEta);
   fChain->SetBranchAddress("bHadronsPt", &bHadronsPt, &b_bHadronsPt);
   fChain->SetBranchAddress("bHadronsPhi", &bHadronsPhi, &b_bHadronsPhi);
*/  fChain->SetBranchAddress("nbHadrons", &nbHadrons, &b_nbHadrons);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_wasRun", &HLT_IsoMu24_eta2p1_v_wasRun, &b_HLT_IsoMu24_eta2p1_v_wasRun);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_fired", &HLT_IsoMu24_eta2p1_v_fired, &b_HLT_IsoMu24_eta2p1_v_fired);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_prescale", &HLT_IsoMu24_eta2p1_v_prescale, &b_HLT_IsoMu24_eta2p1_v_prescale);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_error", &HLT_IsoMu24_eta2p1_v_error, &b_HLT_IsoMu24_eta2p1_v_error);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_wasRun", &HLT_Mu40_eta2p1_v_wasRun, &b_HLT_Mu40_eta2p1_v_wasRun);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_fired", &HLT_Mu40_eta2p1_v_fired, &b_HLT_Mu40_eta2p1_v_fired);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_prescale", &HLT_Mu40_eta2p1_v_prescale, &b_HLT_Mu40_eta2p1_v_prescale);
   fChain->SetBranchAddress("HLT_Mu40_eta2p1_v_error", &HLT_Mu40_eta2p1_v_error, &b_HLT_Mu40_eta2p1_v_error);
   fChain->SetBranchAddress("HLT_Any", &HLT_Any, &b_HLT_Any);
   fChain->SetBranchAddress("weightFactor", &weightFactor, &b_weightFactor);
   Notify();
}


Float_t Event::StringToFloat(const TString VarString)
{

  Float_t VarFloat = 0;

  if( VarString == "EVENT")VarFloat = EVENT;
  else if( VarString == "RUN")VarFloat = RUN;
  else if( VarString == "LUMI")VarFloat = LUMI;
  else if( VarString == "hadMassZ")VarFloat = hadMassZ;
  else if( VarString == "DiSVMass")VarFloat = DiSVMass;
  else if( VarString == "DiSVPt")VarFloat = DiSVPt  ;
  else if( VarString == "J1Dmass")VarFloat = J1Dmass;
  else if( VarString == "J1D0mass")VarFloat = J1D0mass;
  else if( VarString == "J1DR")VarFloat = J1DR;
  else if( VarString == "J1Mu1Boost")VarFloat = J1Mu1Boost;
  else if( VarString == "J1Mu1dxy")VarFloat = J1Mu1dxy ;
  else if( VarString == "J1SVeta")VarFloat = J1SVeta ;
  else if( VarString == "J1SVM")VarFloat = J1SVM ;
  else if( VarString == "J1SVphi")VarFloat = J1SVphi;
  else if( VarString == "J1SVpt")VarFloat = J1SVpt ;
  else if( VarString == "J1TRKdxy")VarFloat = J1TRKdxy;
  else if( VarString == "J1TRKdz")VarFloat = J1TRKdz;
  else if( VarString == "J1nTracks")VarFloat = J1nTracks;
  else if( VarString == "J1Track1Pt")VarFloat = J1Track1Pt;
  else if( VarString == "J1Track2Pt")VarFloat = J1Track2Pt ;
  else if( VarString == "J1Track3Pt")VarFloat = J1Track3Pt;
  else if( VarString == "J2Dmass")VarFloat = J2Dmass ;
  else if( VarString == "J2D0mass")VarFloat = J2D0mass ;
  else if( VarString == "J2DR")VarFloat = J2DR;
  else if( VarString == "J2Mu2Boost")VarFloat = J2Mu2Boost ;
  else if( VarString == "J2Mu1dxy")VarFloat = J2Mu1dxy;
  else if( VarString == "J2SVeta")VarFloat = J2SVeta;
  else if( VarString == "J2SVM")VarFloat = J2SVM ;
  else if( VarString == "J2SVphi")VarFloat = J2SVphi;
  else if( VarString == "J2SVpt")VarFloat = J2SVpt;
  else if( VarString == "J2TRKdxy")VarFloat = J2TRKdxy;
  else if( VarString == "J2TRKdz")VarFloat = J2TRKdz;
  else if( VarString == "J2nTracks")VarFloat = J2nTracks;
  else if( VarString == "J2Track1Pt")VarFloat = J2Track1Pt;
  else if( VarString == "J2Track2Pt")VarFloat = J2Track2Pt;
  else if( VarString == "J2Track3Pt")VarFloat = J2Track3Pt;
  else if( VarString =="vertices")VarFloat = vertices;
  else if( VarString =="nBCand")VarFloat = nBCand;
  else if( VarString =="ncCands")VarFloat = ncCands;
  else if( VarString =="ncbarCands")VarFloat = ncbarCands;
  else if( VarString =="nElectrons")VarFloat = nElectrons;
  else if( VarString =="genWs")VarFloat = genWs;
  else if( VarString =="genBs")VarFloat = genBs;
  else if( VarString =="genCs")VarFloat = genCs;
  else if( VarString =="genDs")VarFloat = genDs;
  else if( VarString =="genSs")VarFloat = genSs;
  else if( VarString =="genUs")VarFloat = genUs;
  else if( VarString == "l1DXY")VarFloat = l1DXY;
  else if( VarString == "HMass1")VarFloat = HMass1;
  else if( VarString == "HMass2")VarFloat = HMass2;
  else if( VarString == "DiMuonMass")VarFloat = DiMuonMass;
  else if( VarString == "l1PFIsoDB")VarFloat = l1PFIsoDB;
  else if( VarString == "l2PFIsoDB")VarFloat = l2PFIsoDB;
  else if( VarString == "l1StdRelIso")VarFloat = l1StdRelIso;
  else if( VarString == "l2StdRelIso")VarFloat = l2StdRelIso;
  else if( VarString == "l1eta")VarFloat = l1eta;
  else if( VarString == "l1phi")VarFloat = l1phi;
  else if( VarString == "l1pt")VarFloat = l1pt;
  else if( VarString == "l2eta")VarFloat = l2eta;
  else if( VarString == "l2phi")VarFloat = l2phi;
  else if( VarString == "l2pt")VarFloat = l2pt;
  else if( VarString == "J3CSVbtag")VarFloat = J3CSVbtag ;
  else if( VarString == "EffWEIGHTCSVL")VarFloat = EffWEIGHTCSVL;
  else if( VarString == "EffWEIGHTCSVL2")VarFloat = EffWEIGHTCSVL2;
  else if( VarString == "EffWEIGHTCSVM")VarFloat = EffWEIGHTCSVM;
  else if( VarString == "EffWEIGHTCSVM2")VarFloat = EffWEIGHTCSVM2;
  else if( VarString == "EffWEIGHTCSVT")VarFloat = EffWEIGHTCSVT;
  else if( VarString == "EffWEIGHTCSVT2")VarFloat = EffWEIGHTCSVT2;
  else if( VarString == "met")VarFloat = met;
  else if( VarString == "muonCharge")VarFloat = muonCharge ;
  else if( VarString == "corMET")VarFloat = corMET;
  else if( VarString == "MtCal")VarFloat = MtCal;
  else if( VarString == "muNuDPhi")VarFloat = muNuDPhi;
  else if( VarString == "dz")VarFloat = dz;
  else if( VarString == "EffWEIGHTpt")VarFloat = EffWEIGHTpt;
  else if( VarString == "EffWEIGHTeta")VarFloat = EffWEIGHTeta;
  else if( VarString == "muonEta")VarFloat = muonEta;
  else if( VarString == "J1massBpm3")VarFloat = J1massBpm3;
  else if( VarString == "J1massBpm3_charge")VarFloat = J1massBpm3_charge;
  else if( VarString == "J1massBpmE")VarFloat = J1massBpmE;
  else if( VarString == "J1massBpm")VarFloat = J1massBpm;
  else if( VarString == "J1massBpm2")VarFloat = J1massBpm2;
  else if( VarString == "J1ChargeMulti")VarFloat = J1ChargeMulti;
  else if( VarString == "J1massD03")VarFloat = J1massD03;
  else if( VarString == "J1massD0")VarFloat = J1massD0;
  else if( VarString == "J1massDpm")VarFloat = J1massDpm;
  else if( VarString == "J1ElectronEnergy")VarFloat = J1ElectronEnergy;
  else if( VarString == "J1ElectronEnergyFrac")VarFloat = J1ElectronEnergyFrac;
  else if( VarString == "J1EleMulti")VarFloat = J1EleMulti;
  else if( VarString == "J1FlightDist")VarFloat = J1FlightDist;
  else if( VarString == "J1errorFlightDist")VarFloat = J1errorFlightDist;
  else if( VarString == "J1CSVMVAbtag")VarFloat = J1CSVMVAbtag;
  else if( VarString == "J1CSVbtag")VarFloat = J1CSVbtag;
  else if( VarString == "J1Charge")VarFloat = J1Charge;
  else if( VarString == "J1nCharges")VarFloat = J1nCharges;
  else if( VarString == "highestJetEta")VarFloat = highestJetEta;
  else if( VarString == "J1JetParton")VarFloat = J1JetParton;
  else if( VarString == "J1Mass")VarFloat = J1Mass;
  else if( VarString == "highestJetPhi")VarFloat = highestJetPhi ;
  else if( VarString == "highestJetPt")VarFloat = highestJetPt;
  else if( VarString == "J1SSVHEbtag")VarFloat = J1SSVHEbtag;
  else if( VarString == "J1SVMass")VarFloat = J1SVMass;
  else if( VarString == "J1SVMassNegb")VarFloat = J1SVMassNegb;
  else if( VarString == "J1SVMassb")VarFloat = J1SVMassb;
  else if( VarString == "J1TCHEbtag")VarFloat = J1TCHEbtag;
  else if( VarString == "J1TCHPbtag")VarFloat = J1TCHPbtag;
  else if( VarString == "J1MuonEnergy")VarFloat = J1MuonEnergy;
  else if( VarString == "J1MuEnergyFrac")VarFloat = J1MuEnergyFrac;
  else if( VarString == "J1MuonMulti")VarFloat = J1MuonMulti;
  else if( VarString == "J1nTracksSSV")VarFloat = J1nTracksSSV;
  else if( VarString == "J1nTracksSSVneg")VarFloat = J1nTracksSSVneg;
  else if( VarString == "J1PhotonEnergy")VarFloat = J1PhotonEnergy;
  else if( VarString == "J1PhotonEnergyFrac")VarFloat = J1PhotonEnergyFrac;
  else if( VarString == "J1PhotonMulti")VarFloat = J1PhotonMulti;
  else if( VarString == "ht")VarFloat = ht;
  else if( VarString == "J1JetShape")VarFloat = J1JetShape;
  else if( VarString == "J1muon1pt")VarFloat = J1muon1pt;
  else if( VarString == "J1Mu1ZMass")VarFloat = J1Mu1ZMass;
  else if( VarString == "J1muon2pt")VarFloat = J1muon2pt;
  else if( VarString == "J2JetShape")VarFloat = J2JetShape;
  else if( VarString == "J2muon1pt")VarFloat = J2muon1pt;
  else if( VarString == "J2Mu1ZMass")VarFloat = J2Mu1ZMass;
  else if( VarString == "J2muon2pt")VarFloat = J2muon2pt;
  else if( VarString == "mJJ")VarFloat = mJJ;
  else if( VarString == "mJ3J4")VarFloat = mJ3J4;
  else if( VarString == "ptJJ")VarFloat = ptJJ;
  else if( VarString =="nJetsPt20")VarFloat = nJetsPt20;
  else if( VarString =="nJetsPt24")VarFloat = nJetsPt24;
  else if( VarString =="nJetsPt25")VarFloat = nJetsPt25;
  else if( VarString =="nJetsPt26")VarFloat = nJetsPt26;
  else if( VarString =="nJetsPt30")VarFloat = nJetsPt30;
  else if( VarString =="nJetsPt40")VarFloat = nJetsPt40;
  else if( VarString =="LHEProduct")VarFloat = LHEProduct;
  else if( VarString == "MET")VarFloat = MET;
  else if( VarString == "Mt")VarFloat = Mt;
  else if( VarString == "muNuRelPFIso")VarFloat = muNuRelPFIso;
  else if( VarString == "PFIsoRho")VarFloat = PFIsoRho;
  else if( VarString == "PFIsoVeto")VarFloat = PFIsoVeto;
  else if( VarString == "muonPhi")VarFloat = muonPhi;
  else if( VarString == "WPt")VarFloat = WPt;
  else if( VarString == "muNuRecoil")VarFloat = muNuRecoil;
  else if( VarString == "lPFIsoDB")VarFloat = lPFIsoDB;
  else if( VarString == "muNuRelStdIso03")VarFloat = muNuRelStdIso03;
  else if( VarString == "EffWEIGHTSSVHEM")VarFloat = EffWEIGHTSSVHEM;
  else if( VarString == "EffWEIGHTSSVHEM2")VarFloat = EffWEIGHTSSVHEM2;
  else if( VarString == "J2massBpm3")VarFloat = J2massBpm3;
  else if( VarString == "J2massBpm3_charge")VarFloat = J2massBpm3_charge;
  else if( VarString == "J2massBpmE")VarFloat = J2massBpmE;
  else if( VarString == "J2massBpm")VarFloat = J2massBpm;
  else if( VarString == "J2massBpm2")VarFloat = J2massBpm2;
  else if( VarString == "J2ChargeMulti")VarFloat = J2ChargeMulti;
  else if( VarString == "J2massD03")VarFloat = J2massD03;
  else if( VarString == "J2massD0")VarFloat = J2massD0;
  else if( VarString == "J2massDpm")VarFloat = J2massDpm;
  else if( VarString == "J2ElectronEnergy")VarFloat = J2ElectronEnergy;
  else if( VarString == "J2ElectronEnergyFrac")VarFloat = J2ElectronEnergyFrac;
  else if( VarString == "J2EleMulti")VarFloat = J2EleMulti;
  else if( VarString == "J2FlightDist")VarFloat = J2FlightDist;
  else if( VarString == "J2errorFlightDist")VarFloat = J2errorFlightDist;
  else if( VarString == "J2CSVMVAbtag")VarFloat = J2CSVMVAbtag;
  else if( VarString == "J2CSVbtag")VarFloat = J2CSVbtag;
  else if( VarString == "J2Charge")VarFloat = J2Charge;
  else if( VarString == "J2nCharges")VarFloat = J2nCharges;
  else if( VarString == "secondJetEta")VarFloat = secondJetEta;
  else if( VarString == "J2JetParton")VarFloat = J2JetParton;
  else if( VarString == "J2Mass")VarFloat = J2Mass;
  else if( VarString == "secondJetPhi")VarFloat = secondJetPhi ;
  else if( VarString == "secondJetPt")VarFloat = secondJetPt;
  else if( VarString == "J2SSVHEbtag")VarFloat = J2SSVHEbtag;
  else if( VarString == "J2SVMass")VarFloat = J2SVMass;
  else if( VarString == "J2SVMassNegb")VarFloat = J2SVMassNegb;
  else if( VarString == "J2SVMassb")VarFloat = J2SVMassb;
  else if( VarString == "J2TCHEbtag")VarFloat = J2TCHEbtag;
  else if( VarString == "J2TCHPbtag")VarFloat = J2TCHPbtag;
  else if( VarString == "J2MuonEnergy")VarFloat = J2MuonEnergy;
  else if( VarString == "J2MuEnergyFrac")VarFloat = J2MuEnergyFrac;
  else if( VarString == "J2MuonMulti")VarFloat = J2MuonMulti;
  else if( VarString == "J2nTracksSSV")VarFloat = J2nTracksSSV;
  else if( VarString == "J2nTracksSSVneg")VarFloat = J2nTracksSSVneg;
  else if( VarString == "J2PhotonEnergy")VarFloat = J2PhotonEnergy;
  else if( VarString == "J2PhotonEnergyFrac")VarFloat = J2PhotonEnergyFrac;
  else if( VarString == "J2PhotonMulti")VarFloat = J2PhotonMulti;
  else if( VarString =="NWCands")VarFloat = NWCands;
  else if( VarString == "J3ChargeMulti")VarFloat = J3ChargeMulti ;
  else if( VarString == "J3ElectronEnergy")VarFloat = J3ElectronEnergy;
  else if( VarString == "J3ElectronEnergyFrac")VarFloat = J3ElectronEnergyFrac;
  else if( VarString == "J3EleMulti")VarFloat = J3EleMulti;
  else if( VarString == "J3Charge")VarFloat = J3Charge;
  else if( VarString == "J3nCharges")VarFloat = J3nCharges;
  else if( VarString == "thirdJetEta")VarFloat = thirdJetEta;
  else if( VarString == "J3JetParton")VarFloat = J3JetParton;
  else if( VarString == "J3Mass")VarFloat = J3Mass;
  else if( VarString == "thirdJetPhi")VarFloat = thirdJetPhi;
  else if( VarString == "thirdJetPt")VarFloat = thirdJetPt;
  else if( VarString == "J3TCHEbtag")VarFloat = J3TCHEbtag;
  else if( VarString == "J3MuonEnergy")VarFloat = J3MuonEnergy;
  else if( VarString == "J3MuEnergyFrac")VarFloat = J3MuEnergyFrac;
  else if( VarString == "J3MuonMulti")VarFloat = J3MuonMulti;
  else if( VarString == "J3PhotonEnergy")VarFloat = J3PhotonEnergy;
  else if( VarString == "J3PhotonEnergyFrac")VarFloat = J3PhotonEnergyFrac;
  else if( VarString == "J3PhotonMulti")VarFloat = J3PhotonMulti;
  else if( VarString == "J1top")VarFloat = J1top;
  else if( VarString == "leptonjj")VarFloat = leptonjj;
  else if( VarString == "metjj")VarFloat = metjj;
  else if( VarString =="nMuons")VarFloat = nMuons;
  else if( VarString == "muonPt")VarFloat = muonPt;
  else if( VarString == "nJets24to5")VarFloat = nJets24to5;
  else if( VarString == "nJets24Pt20")VarFloat = nJets24Pt20;
  else if( VarString == "nJets24Pt25")VarFloat = nJets24Pt25;
  else if( VarString == "nJets24Pt30")VarFloat = nJets24Pt30;
  else if( VarString == "puBXminus")VarFloat = puBXminus;
  else if( VarString =="puTruth")VarFloat = puTruth;
  else if( VarString =="puBX0")VarFloat = puBX0;
  else if( VarString =="puBXplus")VarFloat = puBXplus;
  else if( VarString =="nbHadrons")VarFloat = nbHadrons;
  else if( VarString =="HLT_IsoMu24_eta2p1_v_wasRun")VarFloat = HLT_IsoMu24_eta2p1_v_wasRun;
  else if( VarString =="HLT_IsoMu24_eta2p1_v_fired")VarFloat = HLT_IsoMu24_eta2p1_v_fired;
  else if( VarString =="HLT_IsoMu24_eta2p1_v_prescale")VarFloat = HLT_IsoMu24_eta2p1_v_prescale;
  else if( VarString =="HLT_IsoMu24_eta2p1_v_error")VarFloat = HLT_IsoMu24_eta2p1_v_error;
  else if( VarString =="HLT_Mu40_eta2p1_v_wasRun")VarFloat = HLT_Mu40_eta2p1_v_wasRun;
  else if( VarString =="HLT_Mu40_eta2p1_v_fired")VarFloat = HLT_Mu40_eta2p1_v_fired;
  else if( VarString =="HLT_Mu40_eta2p1_v_prescale")VarFloat = HLT_Mu40_eta2p1_v_prescale;
  else if( VarString =="HLT_Mu40_eta2p1_v_error")VarFloat = HLT_Mu40_eta2p1_v_error;
  else if( VarString =="HLT_Any")VarFloat = HLT_Any;
  else if( VarString =="weightFactor")VarFloat = weightFactor;
  return VarFloat;
}



Bool_t Event::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void Event::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
Int_t Event::Cut(Long64_t entry)
{
// This function may be called from Loop.
// returns  1 if entry is accepted.
// returns -1 otherwise.
   return 1;
}
#endif // #ifdef Event_cxx
