//////////////////////////////////////////////////////////
// This class has been automatically generated on
// Fri Jul 17 12:50:22 2015 by ROOT version 5.34/00
// from TTree eventTree/
// found on file: MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root
//////////////////////////////////////////////////////////

#ifndef findMTresolution_h
#define findMTresolution_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>

// Header file for the classes stored in the TTree if any.
#include <vector>
#include <vector>
#include <algorithm> 

#include <TH1.h>
#include <TLorentzVector.h>

// Fixed size dimensions of array or collections stored in the TTree if any.

class findMTresolution {
public :
   TTree  *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t   fCurrent; //!current Tree number in a TChain

   Int_t nbrGoodMu;
   Int_t nbrVetoMu;
   Int_t nbrGoodEle;
   Int_t nbrVetoEle;

   Bool_t oneGoodMuon;
   Bool_t oneGoodElectron;
   Bool_t min2goodJs;
   Bool_t exactly2goodJs;
   Bool_t exactly2goodBJs;

   Bool_t pass_wbb_mu_good;
   Bool_t pass_wbb_ele_good;

   Float_t SF_top2BJs;

   Float_t SF_wjj_mu_good_IDIsoHLT;
   Float_t SF_wjj_ele_good_IDIsoHLT;
   Float_t weight_wbb_mu_good;
   Float_t dphiMu;
   Float_t mt_genMuon;
   Float_t res_Muon;
   Float_t weight_wbb_ele_good;
   Float_t dphiEle;
   Float_t mt_genEle;
   Float_t res_Ele;

   TH1F hists_mt_reco_mu[1];
   TH1F hists_mt_gen_mu[1];
   TH1F hists_mt_res_mu[1];
   TH1F hists_mt_reco_ele[1];
   TH1F hists_mt_gen_ele[1];
   TH1F hists_mt_res_ele[1];

   Float_t genMatchedLep_pt;
   Float_t genMatchedLep_eta;
   Float_t genMatchedLep_phi;

   Float_t drBestMatch;
   Float_t dR;
   Float_t dP;
   Float_t dE;

   TLorentzVector gen_met_fv;
   TLorentzVector gen_met_tempfv;

   // Declaration of leaf types
   UInt_t          EVENT;
   UInt_t          RUN;
   UInt_t          LUMI;
   Float_t         GBWeight;
   vector<double>  *GEN_dressedLeptonPDGID;
   vector<double>  *GEN_dressedLeptonETA;
   vector<double>  *GEN_dressedLeptonMotherPDGID;
   vector<double>  *GEN_dressedLeptonOriginalPT;
   vector<double>  *GEN_dressedLeptonPHI;
   vector<double>  *GEN_dressedLeptonPT;
   Int_t           GEN_dressedLeptonSIZE;
   vector<double>  *GEN_dressedLeptonType;
   vector<double>  *GEN_jetAngleBs;
   vector<double>  *GEN_jetEta;
   vector<double>  *GEN_jetEtaLeadB;
   vector<double>  *GEN_jetEtaSecondB;
   vector<double>  *GEN_jetBsMatches;
   vector<double>  *GEN_jetPhi;
   vector<double>  *GEN_jetPt;
   vector<double>  *GEN_jetPtDRHadron;
   vector<double>  *GEN_jetPtLeadB;
   vector<double>  *GEN_jetPtSecondB;
   vector<double>  *GEN_jetPhiLeadB;
   vector<double>  *GEN_jetPhiSecondB;
   vector<double>  *GEN_neutrinoETA;
   vector<double>  *GEN_neutrinoPDGID;
   vector<double>  *GEN_neutrinoPHI;
   vector<double>  *GEN_neutrinoPT;
   Float_t         J1_eta_gen_NoNu;
   Float_t         J1_phi_gen_NoNu;
   Float_t         J1_pt_gen_NoNu;
   Float_t         J2_eta_gen_NoNu;
   Float_t         J2_phi_gen_NoNu;
   Float_t         J2_pt_gen_NoNu;
   Float_t         J3_eta_gen_NoNu;
   Float_t         J3_phi_gen_NoNu;
   Float_t         J3_pt_gen_NoNu;
   Float_t         J4_eta_gen_NoNu;
   Float_t         J4_phi_gen_NoNu;
   Float_t         J4_pt_gen_NoNu;
   vector<double>  *SF_goodEle_IDIso;
   vector<double>  *SF_goodEle_IDIsoHLT;
   vector<double>  *SF_goodEle_IDIsoHLT_errDn;
   vector<double>  *SF_goodEle_IDIsoHLT_errUp;
   vector<double>  *SF_goodEle_IDIso_errDn;
   vector<double>  *SF_goodEle_IDIso_errUp;
   vector<double>  *SF_goodMu_IDIso;
   vector<double>  *SF_goodMu_IDIsoHLT;
   vector<double>  *SF_goodMu_IDIsoHLT_errDn;
   vector<double>  *SF_goodMu_IDIsoHLT_errUp;
   vector<double>  *SF_goodMu_IDIso_errDn;
   vector<double>  *SF_goodMu_IDIso_errUp;
   Float_t         SF_lumiWeightPU;
   Float_t         SF_qcdEle_IDIso;
   Float_t         SF_qcdEle_IDIsoHLT;
   Float_t         SF_qcdEle_IDIsoHLT_errDn;
   Float_t         SF_qcdEle_IDIsoHLT_errUp;
   Float_t         SF_qcdEle_IDIso_errDn;
   Float_t         SF_qcdEle_IDIso_errUp;
   Float_t         SF_qcdMu_IDIso;
   Float_t         SF_qcdMu_IDIsoHLT;
   Float_t         SF_qcdMu_IDIsoHLT_errDn;
   Float_t         SF_qcdMu_IDIsoHLT_errUp;
   Float_t         SF_qcdMu_IDIso_errDn;
   Float_t         SF_qcdMu_IDIso_errUp;
   Float_t         bCandidate1Eta;
   Float_t         bCandidate1Phi;
   Float_t         bCandidate1Pt;
   Float_t         bCandidate2Eta;
   Float_t         bCandidate2Phi;
   Float_t         bCandidate2Pt;
   Float_t         bCandidateBC1MASS;
   Float_t         bCandidateBC1nTracks;
   Float_t         bCandidateBC2MASS;
   Float_t         bCandidateBC2nTracks;
   Float_t         bCandidateBCDeltaR;
   Float_t         bCandidateBCEnergySum;
   Float_t         bCandidateBCGenEnergySum;
   Float_t         bCandidateBDeltaPHI;
   Float_t         bCandidateDeltaPhi;
   Float_t         bCandidateDeltaR;
   Float_t         bCandidateJet1BC1ETA;
   Float_t         bCandidateJet1BC1PHI;
   Float_t         bCandidateJet1BC1PT;
   Float_t         bCandidateJet1BC2ETA;
   Float_t         bCandidateJet1BC2PHI;
   Float_t         bCandidateJet1BC2PT;
   Float_t         bCandidateJet2BC1ETA;
   Float_t         bCandidateJet2BC1PHI;
   Float_t         bCandidateJet2BC1PT;
   Float_t         bCandidateJet2BC2ETA;
   Float_t         bCandidateJet2BC2PHI;
   Float_t         bCandidateJet2BC2PT;
   Float_t         bCandidateJet3BC1ETA;
   Float_t         bCandidateJet3BC1PHI;
   Float_t         bCandidateJet3BC1PT;
   Float_t         bCandidateJet3BC2ETA;
   Float_t         bCandidateJet3BC2PHI;
   Float_t         bCandidateJet3BC2PT;
   Float_t         bCandidateJet4BC1ETA;
   Float_t         bCandidateJet4BC1PHI;
   Float_t         bCandidateJet4BC1PT;
   Float_t         bCandidateJet4BC2ETA;
   Float_t         bCandidateJet4BC2PHI;
   Float_t         bCandidateJet4BC2PT;
   Float_t         bCandidatenBC;
   Float_t         bCandidatenJetAssociatedToBC;
   Float_t         bCandidatenJetAssociatedToBC1;
   Float_t         bCandidatenJetAssociatedToBC2;
   vector<double>  *bHadronsEta;
   vector<double>  *bHadronsID;
   vector<double>  *bHadronsPhi;
   vector<double>  *bHadronsPt;
   Float_t         fwdJ1_CSV;
   Float_t         fwdJ1_CSVreweight;
   Float_t         fwdJ1_SF_CSVL;
   Float_t         fwdJ1_SF_CSVL_errDn;
   Float_t         fwdJ1_SF_CSVL_errUp;
   Float_t         fwdJ1_SF_CSVM;
   Float_t         fwdJ1_SF_CSVM_errDn;
   Float_t         fwdJ1_SF_CSVM_errUp;
   Float_t         fwdJ1_SF_CSVT;
   Float_t         fwdJ1_SF_CSVT_errDn;
   Float_t         fwdJ1_SF_CSVT_errUp;
   Float_t         fwdJ1_eta;
   Float_t         fwdJ1_mass;
   Float_t         fwdJ1_partonFlavour;
   Float_t         fwdJ1_phi;
   Float_t         fwdJ1_pt;
   Float_t         fwdJ1_pt_resUp;
   Float_t         fwdJ2_CSV;
   Float_t         fwdJ2_CSVreweight;
   Float_t         fwdJ2_SF_CSVL;
   Float_t         fwdJ2_SF_CSVL_errDn;
   Float_t         fwdJ2_SF_CSVL_errUp;
   Float_t         fwdJ2_SF_CSVM;
   Float_t         fwdJ2_SF_CSVM_errDn;
   Float_t         fwdJ2_SF_CSVM_errUp;
   Float_t         fwdJ2_SF_CSVT;
   Float_t         fwdJ2_SF_CSVT_errDn;
   Float_t         fwdJ2_SF_CSVT_errUp;
   Float_t         fwdJ2_eta;
   Float_t         fwdJ2_mass;
   Float_t         fwdJ2_partonFlavour;
   Float_t         fwdJ2_phi;
   Float_t         fwdJ2_pt;
   Float_t         fwdJ2_pt_resUp;
   Int_t           genBs;
   Int_t           genCs;
   Int_t           genDs;
   Float_t         genWLeptonID;
   Float_t         genLeptonPT;
   Float_t         genLeptonETA;
   Float_t         genLeptonPHI;
   Float_t         genWBs;
   Float_t         genWCs;
   Float_t         genWGs;
   Float_t         genWBbar;
   Float_t         genWB;
   Float_t         genWBbar_st3;
   Float_t         genWCbar_st3;
   Float_t         genWB_st3;
   Float_t         genWC_st3;
   Float_t         genWGs_st3;
   Float_t         genWBbar_AfterW;
   Float_t         genWCbar_AfterW;
   Float_t         genWB_AfterW;
   Float_t         genWC_AfterW;
   Float_t         genWGs_AfterW;
   Float_t         infoNUP;
   Float_t         foundB;
   Float_t         foundBbar;
   Float_t         foundC;
   Float_t         foundCbar;
   Float_t         gluonPythiaForB;
   Float_t         gluonPythiaForC;
   Float_t         gluonMadgraphForB;
   Float_t         gluonMadgraphForC;
   vector<double>  *BCandsPt;
   vector<double>  *BCandsPhi;
   vector<double>  *BCandsEta;
   vector<int>     *BCandsPDGID;
   vector<int>     *BCandsStatus;
   vector<int>     *BCandsMothers;
   vector<double>  *CCandsPt;
   vector<double>  *CCandsPhi;
   vector<double>  *CCandsEta;
   vector<int>     *CCandsPDGID;
   vector<int>     *CCandsStatus;
   vector<int>     *CCandsMothers;
   Int_t           genSs;
   Int_t           genTbars;
   Int_t           genTs;
   Int_t           genUs;
   Int_t           genWs;
   vector<double>  *goodEle_Iso03_vec;
   vector<double>  *goodEle_Iso04_vec;
   vector<double>  *goodEle_charge_vec;
   vector<double>  *goodEle_eta_vec;
   vector<double>  *goodEle_mass_vec;
   vector<double>  *goodEle_phi_vec;
   vector<double>  *goodEle_pt_vec;
   Float_t         goodJ1_CSV;
   Float_t         goodJ1_CSVreweight;
   Float_t         goodJ1_SF_CSVL;
   Float_t         goodJ1_SF_CSVL_errDn;
   Float_t         goodJ1_SF_CSVL_errUp;
   Float_t         goodJ1_SF_CSVM;
   Float_t         goodJ1_SF_CSVM_errDn;
   Float_t         goodJ1_SF_CSVM_errUp;
   Float_t         goodJ1_SF_CSVT;
   Float_t         goodJ1_SF_CSVT_errDn;
   Float_t         goodJ1_SF_CSVT_errUp;
   Float_t         goodJ1_eta;
   Float_t         goodJ1_mass;
   Float_t         goodJ1_mass_SV_corrected;
   Float_t         goodJ1_mass_SV_unweighted;
   Float_t         goodJ1_mass_SV_weighted;
   Float_t         goodJ1_partonFlavour;
   Float_t         goodJ1_phi;
   Float_t         goodJ1_pt;
   Float_t         goodJ1_pt_SV_unweighted;
   Float_t         goodJ1_pt_SV_weighted;
   Float_t         goodJ1_pt_resDown;
   Float_t         goodJ1_pt_resUp;
   Float_t         goodJ1_shift_pt;
   Float_t         goodJ1_shift_pt_Dn;
   Float_t         goodJ1_shift_pt_Up;
   Float_t         goodJ1_total_shift_pt;
   Float_t         goodJ1_total_shift_pt_Dn;
   Float_t         goodJ1_total_shift_pt_Up;
   Float_t         goodJ2_CSV;
   Float_t         goodJ2_CSVreweight;
   Float_t         goodJ2_SF_CSVL;
   Float_t         goodJ2_SF_CSVL_errDn;
   Float_t         goodJ2_SF_CSVL_errUp;
   Float_t         goodJ2_SF_CSVM;
   Float_t         goodJ2_SF_CSVM_errDn;
   Float_t         goodJ2_SF_CSVM_errUp;
   Float_t         goodJ2_SF_CSVT;
   Float_t         goodJ2_SF_CSVT_errDn;
   Float_t         goodJ2_SF_CSVT_errUp;
   Float_t         goodJ2_eta;
   Float_t         goodJ2_mass;
   Float_t         goodJ2_mass_SV_corrected;
   Float_t         goodJ2_mass_SV_unweighted;
   Float_t         goodJ2_mass_SV_weighted;
   Float_t         goodJ2_partonFlavour;
   Float_t         goodJ2_phi;
   Float_t         goodJ2_pt;
   Float_t         goodJ2_pt_SV_unweighted;
   Float_t         goodJ2_pt_SV_weighted;
   Float_t         goodJ2_pt_resDown;
   Float_t         goodJ2_pt_resUp;
   Float_t         goodJ2_shift_pt;
   Float_t         goodJ2_shift_pt_Dn;
   Float_t         goodJ2_shift_pt_Up;
   Float_t         goodJ2_total_shift_pt;
   Float_t         goodJ2_total_shift_pt_Dn;
   Float_t         goodJ2_total_shift_pt_Up;
   Float_t         goodJ3_CSV;
   Float_t         goodJ3_CSVreweight;
   Float_t         goodJ3_SF_CSVL;
   Float_t         goodJ3_SF_CSVL_errDn;
   Float_t         goodJ3_SF_CSVL_errUp;
   Float_t         goodJ3_SF_CSVM;
   Float_t         goodJ3_SF_CSVM_errDn;
   Float_t         goodJ3_SF_CSVM_errUp;
   Float_t         goodJ3_SF_CSVT;
   Float_t         goodJ3_SF_CSVT_errDn;
   Float_t         goodJ3_SF_CSVT_errUp;
   Float_t         goodJ3_eta;
   Float_t         goodJ3_mass;
   Float_t         goodJ3_mass_SV_corrected;
   Float_t         goodJ3_mass_SV_unweighted;
   Float_t         goodJ3_mass_SV_weighted;
   Float_t         goodJ3_partonFlavour;
   Float_t         goodJ3_phi;
   Float_t         goodJ3_pt;
   Float_t         goodJ3_pt_SV_unweighted;
   Float_t         goodJ3_pt_SV_weighted;
   Float_t         goodJ3_pt_resDown;
   Float_t         goodJ3_pt_resUp;
   Float_t         goodJ4_CSV;
   Float_t         goodJ4_CSVreweight;
   Float_t         goodJ4_SF_CSVL;
   Float_t         goodJ4_SF_CSVL_errDn;
   Float_t         goodJ4_SF_CSVL_errUp;
   Float_t         goodJ4_SF_CSVM;
   Float_t         goodJ4_SF_CSVM_errDn;
   Float_t         goodJ4_SF_CSVM_errUp;
   Float_t         goodJ4_SF_CSVT;
   Float_t         goodJ4_SF_CSVT_errDn;
   Float_t         goodJ4_SF_CSVT_errUp;
   Float_t         goodJ4_eta;
   Float_t         goodJ4_mass;
   Float_t         goodJ4_partonFlavour;
   Float_t         goodJ4_phi;
   Float_t         goodJ4_pt;
   Float_t         goodJ4_pt_resDown;
   Float_t         goodJ4_pt_resUp;
   vector<double>  *goodMu_charge_vec;
   vector<double>  *goodMu_eta_vec;
   vector<double>  *goodMu_mass_vec;
   vector<double>  *goodMu_phi_vec;
   vector<double>  *goodMu_pt_vec;
   Float_t         met_eesDn_phi;
   Float_t         met_eesDn_pt;
   Float_t         met_eesUp_phi;
   Float_t         met_eesUp_pt;
   Float_t         met_jesDn_phi;
   Float_t         met_jesDn_pt;
   Float_t         met_jesUp_phi;
   Float_t         met_jesUp_pt;
   Float_t         met_phi;
   Float_t         met_pt;
   Float_t         met_uesDn_phi;
   Float_t         met_uesDn_pt;
   Float_t         met_uesUp_phi;
   Float_t         met_uesUp_pt;
   Float_t         mt_goodElectron;
   Float_t         mt_goodElectron_eesDn;
   Float_t         mt_goodElectron_eesUp;
   Float_t         mt_goodElectron_jesDn;
   Float_t         mt_goodElectron_jesUp;
   Float_t         mt_goodElectron_uesDn;
   Float_t         mt_goodElectron_uesUp;
   Float_t         mt_goodMuon;
   Float_t         mt_goodMuon_eesDn;
   Float_t         mt_goodMuon_eesUp;
   Float_t         mt_goodMuon_jesDn;
   Float_t         mt_goodMuon_jesUp;
   Float_t         mt_goodMuon_uesDn;
   Float_t         mt_goodMuon_uesUp;
   Float_t         mt_qcdElectron;
   Float_t         mt_qcdElectron_eesDn;
   Float_t         mt_qcdElectron_eesUp;
   Float_t         mt_qcdElectron_jesDn;
   Float_t         mt_qcdElectron_jesUp;
   Float_t         mt_qcdElectron_uesDn;
   Float_t         mt_qcdElectron_uesUp;
   Float_t         mt_qcdMuon;
   Float_t         mt_qcdMuon_eesDn;
   Float_t         mt_qcdMuon_eesUp;
   Float_t         mt_qcdMuon_jesDn;
   Float_t         mt_qcdMuon_jesUp;
   Float_t         mt_qcdMuon_uesDn;
   Float_t         mt_qcdMuon_uesUp;
   Int_t           LHEProduct;
   Int_t           nbHadrons;
   Int_t           nrAllEle;
   Int_t           nrAllJets;
   Int_t           nrAllMu;
   Int_t           nrCleanJets;
   Int_t           nrFwdJets;
   Int_t           nrGoodEle;
   Int_t           nrGoodJets;
   Int_t           nrGoodMu;
   Int_t           nrQCDEle;
   Int_t           nrQCDMu;
   Int_t           nrVetoEle;
   Int_t           nrVetoMu;
   Float_t         puBXminus;
   Float_t         puTruth;
   Float_t         puBX0;
   Float_t         puBXplus;
   vector<double>  *qcdEle_charge_vec;
   vector<double>  *qcdEle_eta_vec;
   vector<double>  *qcdEle_phi_vec;
   vector<double>  *qcdEle_pt_vec;
   vector<double>  *qcdMu_charge_vec;
   vector<double>  *qcdMu_eta_vec;
   vector<double>  *qcdMu_phi_vec;
   vector<double>  *qcdMu_pt_vec;
   Float_t         weightTop;
   Float_t         topPt;
   Float_t         antitopPt;
   Int_t           HLT_IsoMu24_eta2p1_v_wasRun;
   Int_t           HLT_IsoMu24_eta2p1_v_fired;
   Int_t           HLT_IsoMu24_eta2p1_v_prescale;
   Int_t           HLT_IsoMu24_eta2p1_v_error;
   Int_t           HLT_Ele27_WP80_wasRun;
   Int_t           HLT_Ele27_WP80_fired;
   Int_t           HLT_Ele27_WP80_prescale;
   Int_t           HLT_Ele27_WP80_error;
   Int_t           HLT_Any;
   Int_t           vertices;
   vector<double>  *vetoEle_charge_vec;
   vector<double>  *vetoEle_eta_vec;
   vector<double>  *vetoEle_phi_vec;
   vector<double>  *vetoEle_pt_vec;
   vector<double>  *vetoMu_charge_vec;
   vector<double>  *vetoMu_eta_vec;
   vector<double>  *vetoMu_phi_vec;
   vector<double>  *vetoMu_pt_vec;

   // List of branches
   TBranch        *b_EVENT;   //!
   TBranch        *b_RUN;   //!
   TBranch        *b_LUMI;   //!
   TBranch        *b_GBWeight;   //!
   TBranch        *b_GEN_dressedLeptonPDGID;   //!
   TBranch        *b_GEN_dressedLeptonETA;   //!
   TBranch        *b_GEN_dressedLeptonMotherPDGID;   //!
   TBranch        *b_GEN_dressedLeptonOriginalPT;   //!
   TBranch        *b_GEN_dressedLeptonPHI;   //!
   TBranch        *b_GEN_dressedLeptonPT;   //!
   TBranch        *b_GEN_dressedLeptonSIZE;   //!
   TBranch        *b_GEN_dressedLeptonType;   //!
   TBranch        *b_GEN_jetAngleBs;   //!
   TBranch        *b_GEN_jetEta;   //!
   TBranch        *b_GEN_jetEtaLeadB;   //!
   TBranch        *b_GEN_jetEtaSecondB;   //!
   TBranch        *b_GEN_jetBsMatches;   //!
   TBranch        *b_GEN_jetPhi;   //!
   TBranch        *b_GEN_jetPt;   //!
   TBranch        *b_GEN_jetPtDRHadron;   //!
   TBranch        *b_GEN_jetPtLeadB;   //!
   TBranch        *b_GEN_jetPtSecondB;   //!
   TBranch        *b_GEN_jetPhiLeadB;   //!
   TBranch        *b_GEN_jetPhiSecondB;   //!
   TBranch        *b_GEN_neutrinoETA;   //!
   TBranch        *b_GEN_neutrinoPDGID;   //!
   TBranch        *b_GEN_neutrinoPHI;   //!
   TBranch        *b_GEN_neutrinoPT;   //!
   TBranch        *b_J1_eta_gen_NoNu;   //!
   TBranch        *b_J1_phi_gen_NoNu;   //!
   TBranch        *b_J1_pt_gen_NoNu;   //!
   TBranch        *b_J2_eta_gen_NoNu;   //!
   TBranch        *b_J2_phi_gen_NoNu;   //!
   TBranch        *b_J2_pt_gen_NoNu;   //!
   TBranch        *b_J3_eta_gen_NoNu;   //!
   TBranch        *b_J3_phi_gen_NoNu;   //!
   TBranch        *b_J3_pt_gen_NoNu;   //!
   TBranch        *b_J4_eta_gen_NoNu;   //!
   TBranch        *b_J4_phi_gen_NoNu;   //!
   TBranch        *b_J4_pt_gen_NoNu;   //!
   TBranch        *b_SF_goodEle_IDIso;   //!
   TBranch        *b_SF_goodEle_IDIsoHLT;   //!
   TBranch        *b_SF_goodEle_IDIsoHLT_errDn;   //!
   TBranch        *b_SF_goodEle_IDIsoHLT_errUp;   //!
   TBranch        *b_SF_goodEle_IDIso_errDn;   //!
   TBranch        *b_SF_goodEle_IDIso_errUp;   //!
   TBranch        *b_SF_goodMu_IDIso;   //!
   TBranch        *b_SF_goodMu_IDIsoHLT;   //!
   TBranch        *b_SF_goodMu_IDIsoHLT_errDn;   //!
   TBranch        *b_SF_goodMu_IDIsoHLT_errUp;   //!
   TBranch        *b_SF_goodMu_IDIso_errDn;   //!
   TBranch        *b_SF_goodMu_IDIso_errUp;   //!
   TBranch        *b_SF_lumiWeightPU;   //!
   TBranch        *b_SF_qcdEle_IDIso;   //!
   TBranch        *b_SF_qcdEle_IDIsoHLT;   //!
   TBranch        *b_SF_qcdEle_IDIsoHLT_errDn;   //!
   TBranch        *b_SF_qcdEle_IDIsoHLT_errUp;   //!
   TBranch        *b_SF_qcdEle_IDIso_errDn;   //!
   TBranch        *b_SF_qcdEle_IDIso_errUp;   //!
   TBranch        *b_SF_qcdMu_IDIso;   //!
   TBranch        *b_SF_qcdMu_IDIsoHLT;   //!
   TBranch        *b_SF_qcdMu_IDIsoHLT_errDn;   //!
   TBranch        *b_SF_qcdMu_IDIsoHLT_errUp;   //!
   TBranch        *b_SF_qcdMu_IDIso_errDn;   //!
   TBranch        *b_SF_qcdMu_IDIso_errUp;   //!
   TBranch        *b_bCandidate1Eta;   //!
   TBranch        *b_bCandidate1Phi;   //!
   TBranch        *b_bCandidate1Pt;   //!
   TBranch        *b_bCandidate2Eta;   //!
   TBranch        *b_bCandidate2Phi;   //!
   TBranch        *b_bCandidate2Pt;   //!
   TBranch        *b_bCandidateBC1MASS;   //!
   TBranch        *b_bCandidateBC1nTracks;   //!
   TBranch        *b_bCandidateBC2MASS;   //!
   TBranch        *b_bCandidateBC2nTracks;   //!
   TBranch        *b_bCandidateBCDeltaR;   //!
   TBranch        *b_bCandidateBCEnergySum;   //!
   TBranch        *b_bCandidateBCGenEnergySum;   //!
   TBranch        *b_bCandidateBDeltaPHI;   //!
   TBranch        *b_bCandidateDeltaPhi;   //!
   TBranch        *b_bCandidateDeltaR;   //!
   TBranch        *b_bCandidateJet1BC1ETA;   //!
   TBranch        *b_bCandidateJet1BC1PHI;   //!
   TBranch        *b_bCandidateJet1BC1PT;   //!
   TBranch        *b_bCandidateJet1BC2ETA;   //!
   TBranch        *b_bCandidateJet1BC2PHI;   //!
   TBranch        *b_bCandidateJet1BC2PT;   //!
   TBranch        *b_bCandidateJet2BC1ETA;   //!
   TBranch        *b_bCandidateJet2BC1PHI;   //!
   TBranch        *b_bCandidateJet2BC1PT;   //!
   TBranch        *b_bCandidateJet2BC2ETA;   //!
   TBranch        *b_bCandidateJet2BC2PHI;   //!
   TBranch        *b_bCandidateJet2BC2PT;   //!
   TBranch        *b_bCandidateJet3BC1ETA;   //!
   TBranch        *b_bCandidateJet3BC1PHI;   //!
   TBranch        *b_bCandidateJet3BC1PT;   //!
   TBranch        *b_bCandidateJet3BC2ETA;   //!
   TBranch        *b_bCandidateJet3BC2PHI;   //!
   TBranch        *b_bCandidateJet3BC2PT;   //!
   TBranch        *b_bCandidateJet4BC1ETA;   //!
   TBranch        *b_bCandidateJet4BC1PHI;   //!
   TBranch        *b_bCandidateJet4BC1PT;   //!
   TBranch        *b_bCandidateJet4BC2ETA;   //!
   TBranch        *b_bCandidateJet4BC2PHI;   //!
   TBranch        *b_bCandidateJet4BC2PT;   //!
   TBranch        *b_bCandidatenBC;   //!
   TBranch        *b_bCandidatenJetAssociatedToBC;   //!
   TBranch        *b_bCandidatenJetAssociatedToBC1;   //!
   TBranch        *b_bCandidatenJetAssociatedToBC2;   //!
   TBranch        *b_bHadronsEta;   //!
   TBranch        *b_bHadronsID;   //!
   TBranch        *b_bHadronsPhi;   //!
   TBranch        *b_bHadronsPt;   //!
   TBranch        *b_fwdJ1_CSV;   //!
   TBranch        *b_fwdJ1_CSVreweight;   //!
   TBranch        *b_fwdJ1_SF_CSVL;   //!
   TBranch        *b_fwdJ1_SF_CSVL_errDn;   //!
   TBranch        *b_fwdJ1_SF_CSVL_errUp;   //!
   TBranch        *b_fwdJ1_SF_CSVM;   //!
   TBranch        *b_fwdJ1_SF_CSVM_errDn;   //!
   TBranch        *b_fwdJ1_SF_CSVM_errUp;   //!
   TBranch        *b_fwdJ1_SF_CSVT;   //!
   TBranch        *b_fwdJ1_SF_CSVT_errDn;   //!
   TBranch        *b_fwdJ1_SF_CSVT_errUp;   //!
   TBranch        *b_fwdJ1_eta;   //!
   TBranch        *b_fwdJ1_mass;   //!
   TBranch        *b_fwdJ1_partonFlavour;   //!
   TBranch        *b_fwdJ1_phi;   //!
   TBranch        *b_fwdJ1_pt;   //!
   TBranch        *b_fwdJ1_pt_resUp;   //!
   TBranch        *b_fwdJ2_CSV;   //!
   TBranch        *b_fwdJ2_CSVreweight;   //!
   TBranch        *b_fwdJ2_SF_CSVL;   //!
   TBranch        *b_fwdJ2_SF_CSVL_errDn;   //!
   TBranch        *b_fwdJ2_SF_CSVL_errUp;   //!
   TBranch        *b_fwdJ2_SF_CSVM;   //!
   TBranch        *b_fwdJ2_SF_CSVM_errDn;   //!
   TBranch        *b_fwdJ2_SF_CSVM_errUp;   //!
   TBranch        *b_fwdJ2_SF_CSVT;   //!
   TBranch        *b_fwdJ2_SF_CSVT_errDn;   //!
   TBranch        *b_fwdJ2_SF_CSVT_errUp;   //!
   TBranch        *b_fwdJ2_eta;   //!
   TBranch        *b_fwdJ2_mass;   //!
   TBranch        *b_fwdJ2_partonFlavour;   //!
   TBranch        *b_fwdJ2_phi;   //!
   TBranch        *b_fwdJ2_pt;   //!
   TBranch        *b_fwdJ2_pt_resUp;   //!
   TBranch        *b_genBs;   //!
   TBranch        *b_genCs;   //!
   TBranch        *b_genDs;   //!
   TBranch        *b_genWLeptonID;   //!
   TBranch        *b_genLeptonPT;   //!
   TBranch        *b_genLeptonETA;   //!
   TBranch        *b_genLeptonPHI;   //!
   TBranch        *b_genWBs;   //!
   TBranch        *b_genWCs;   //!
   TBranch        *b_genWGs;   //!
   TBranch        *b_genWBbar;   //!
   TBranch        *b_genWB;   //!
   TBranch        *b_genWBbar_st3;   //!
   TBranch        *b_genWCbar_st3;   //!
   TBranch        *b_genWB_st3;   //!
   TBranch        *b_genWC_st3;   //!
   TBranch        *b_genWGs_st3;   //!
   TBranch        *b_genWBbar_AfterW;   //!
   TBranch        *b_genWCbar_AfterW;   //!
   TBranch        *b_genWB_AfterW;   //!
   TBranch        *b_genWC_AfterW;   //!
   TBranch        *b_genWGs_AfterW;   //!
   TBranch        *b_infoNUP;   //!
   TBranch        *b_foundB;   //!
   TBranch        *b_foundBbar;   //!
   TBranch        *b_foundC;   //!
   TBranch        *b_foundCbar;   //!
   TBranch        *b_gluonPythiaForB;   //!
   TBranch        *b_gluonPythiaForC;   //!
   TBranch        *b_gluonMadgraphForB;   //!
   TBranch        *b_gluonMadgraphForC;   //!
   TBranch        *b_BCandsPt;   //!
   TBranch        *b_BCandsPhi;   //!
   TBranch        *b_BCandsEta;   //!
   TBranch        *b_BCandsPDGID;   //!
   TBranch        *b_BCandsStatus;   //!
   TBranch        *b_BCandsMothers;   //!
   TBranch        *b_CCandsPt;   //!
   TBranch        *b_CCandsPhi;   //!
   TBranch        *b_CCandsEta;   //!
   TBranch        *b_CCandsPDGID;   //!
   TBranch        *b_CCandsStatus;   //!
   TBranch        *b_CCandsMothers;   //!
   TBranch        *b_genSs;   //!
   TBranch        *b_genTbars;   //!
   TBranch        *b_genTs;   //!
   TBranch        *b_genUs;   //!
   TBranch        *b_genWs;   //!
   TBranch        *b_goodEle_Iso03_vec;   //!
   TBranch        *b_goodEle_Iso04_vec;   //!
   TBranch        *b_goodEle_charge_vec;   //!
   TBranch        *b_goodEle_eta_vec;   //!
   TBranch        *b_goodEle_mass_vec;   //!
   TBranch        *b_goodEle_phi_vec;   //!
   TBranch        *b_goodEle_pt_vec;   //!
   TBranch        *b_goodJ1_CSV;   //!
   TBranch        *b_goodJ1_CSVreweight;   //!
   TBranch        *b_goodJ1_SF_CSVL;   //!
   TBranch        *b_goodJ1_SF_CSVL_errDn;   //!
   TBranch        *b_goodJ1_SF_CSVL_errUp;   //!
   TBranch        *b_goodJ1_SF_CSVM;   //!
   TBranch        *b_goodJ1_SF_CSVM_errDn;   //!
   TBranch        *b_goodJ1_SF_CSVM_errUp;   //!
   TBranch        *b_goodJ1_SF_CSVT;   //!
   TBranch        *b_goodJ1_SF_CSVT_errDn;   //!
   TBranch        *b_goodJ1_SF_CSVT_errUp;   //!
   TBranch        *b_goodJ1_eta;   //!
   TBranch        *b_goodJ1_mass;   //!
   TBranch        *b_goodJ1_mass_SV_corrected;   //!
   TBranch        *b_goodJ1_mass_SV_unweighted;   //!
   TBranch        *b_goodJ1_mass_SV_weighted;   //!
   TBranch        *b_goodJ1_partonFlavour;   //!
   TBranch        *b_goodJ1_phi;   //!
   TBranch        *b_goodJ1_pt;   //!
   TBranch        *b_goodJ1_pt_SV_unweighted;   //!
   TBranch        *b_goodJ1_pt_SV_weighted;   //!
   TBranch        *b_goodJ1_pt_resDown;   //!
   TBranch        *b_goodJ1_pt_resUp;   //!
   TBranch        *b_goodJ1_shift_pt;   //!
   TBranch        *b_goodJ1_shift_pt_Dn;   //!
   TBranch        *b_goodJ1_shift_pt_Up;   //!
   TBranch        *b_goodJ1_total_shift_pt;   //!
   TBranch        *b_goodJ1_total_shift_pt_Dn;   //!
   TBranch        *b_goodJ1_total_shift_pt_Up;   //!
   TBranch        *b_goodJ2_CSV;   //!
   TBranch        *b_goodJ2_CSVreweight;   //!
   TBranch        *b_goodJ2_SF_CSVL;   //!
   TBranch        *b_goodJ2_SF_CSVL_errDn;   //!
   TBranch        *b_goodJ2_SF_CSVL_errUp;   //!
   TBranch        *b_goodJ2_SF_CSVM;   //!
   TBranch        *b_goodJ2_SF_CSVM_errDn;   //!
   TBranch        *b_goodJ2_SF_CSVM_errUp;   //!
   TBranch        *b_goodJ2_SF_CSVT;   //!
   TBranch        *b_goodJ2_SF_CSVT_errDn;   //!
   TBranch        *b_goodJ2_SF_CSVT_errUp;   //!
   TBranch        *b_goodJ2_eta;   //!
   TBranch        *b_goodJ2_mass;   //!
   TBranch        *b_goodJ2_mass_SV_corrected;   //!
   TBranch        *b_goodJ2_mass_SV_unweighted;   //!
   TBranch        *b_goodJ2_mass_SV_weighted;   //!
   TBranch        *b_goodJ2_partonFlavour;   //!
   TBranch        *b_goodJ2_phi;   //!
   TBranch        *b_goodJ2_pt;   //!
   TBranch        *b_goodJ2_pt_SV_unweighted;   //!
   TBranch        *b_goodJ2_pt_SV_weighted;   //!
   TBranch        *b_goodJ2_pt_resDown;   //!
   TBranch        *b_goodJ2_pt_resUp;   //!
   TBranch        *b_goodJ2_shift_pt;   //!
   TBranch        *b_goodJ2_shift_pt_Dn;   //!
   TBranch        *b_goodJ2_shift_pt_Up;   //!
   TBranch        *b_goodJ2_total_shift_pt;   //!
   TBranch        *b_goodJ2_total_shift_pt_Dn;   //!
   TBranch        *b_goodJ2_total_shift_pt_Up;   //!
   TBranch        *b_goodJ3_CSV;   //!
   TBranch        *b_goodJ3_CSVreweight;   //!
   TBranch        *b_goodJ3_SF_CSVL;   //!
   TBranch        *b_goodJ3_SF_CSVL_errDn;   //!
   TBranch        *b_goodJ3_SF_CSVL_errUp;   //!
   TBranch        *b_goodJ3_SF_CSVM;   //!
   TBranch        *b_goodJ3_SF_CSVM_errDn;   //!
   TBranch        *b_goodJ3_SF_CSVM_errUp;   //!
   TBranch        *b_goodJ3_SF_CSVT;   //!
   TBranch        *b_goodJ3_SF_CSVT_errDn;   //!
   TBranch        *b_goodJ3_SF_CSVT_errUp;   //!
   TBranch        *b_goodJ3_eta;   //!
   TBranch        *b_goodJ3_mass;   //!
   TBranch        *b_goodJ3_mass_SV_corrected;   //!
   TBranch        *b_goodJ3_mass_SV_unweighted;   //!
   TBranch        *b_goodJ3_mass_SV_weighted;   //!
   TBranch        *b_goodJ3_partonFlavour;   //!
   TBranch        *b_goodJ3_phi;   //!
   TBranch        *b_goodJ3_pt;   //!
   TBranch        *b_goodJ3_pt_SV_unweighted;   //!
   TBranch        *b_goodJ3_pt_SV_weighted;   //!
   TBranch        *b_goodJ3_pt_resDown;   //!
   TBranch        *b_goodJ3_pt_resUp;   //!
   TBranch        *b_goodJ4_CSV;   //!
   TBranch        *b_goodJ4_CSVreweight;   //!
   TBranch        *b_goodJ4_SF_CSVL;   //!
   TBranch        *b_goodJ4_SF_CSVL_errDn;   //!
   TBranch        *b_goodJ4_SF_CSVL_errUp;   //!
   TBranch        *b_goodJ4_SF_CSVM;   //!
   TBranch        *b_goodJ4_SF_CSVM_errDn;   //!
   TBranch        *b_goodJ4_SF_CSVM_errUp;   //!
   TBranch        *b_goodJ4_SF_CSVT;   //!
   TBranch        *b_goodJ4_SF_CSVT_errDn;   //!
   TBranch        *b_goodJ4_SF_CSVT_errUp;   //!
   TBranch        *b_goodJ4_eta;   //!
   TBranch        *b_goodJ4_mass;   //!
   TBranch        *b_goodJ4_partonFlavour;   //!
   TBranch        *b_goodJ4_phi;   //!
   TBranch        *b_goodJ4_pt;   //!
   TBranch        *b_goodJ4_pt_resDown;   //!
   TBranch        *b_goodJ4_pt_resUp;   //!
   TBranch        *b_goodMu_charge_vec;   //!
   TBranch        *b_goodMu_eta_vec;   //!
   TBranch        *b_goodMu_mass_vec;   //!
   TBranch        *b_goodMu_phi_vec;   //!
   TBranch        *b_goodMu_pt_vec;   //!
   TBranch        *b_met_eesDn_phi;   //!
   TBranch        *b_met_eesDn_pt;   //!
   TBranch        *b_met_eesUp_phi;   //!
   TBranch        *b_met_eesUp_pt;   //!
   TBranch        *b_met_jesDn_phi;   //!
   TBranch        *b_met_jesDn_pt;   //!
   TBranch        *b_met_jesUp_phi;   //!
   TBranch        *b_met_jesUp_pt;   //!
   TBranch        *b_met_phi;   //!
   TBranch        *b_met_pt;   //!
   TBranch        *b_met_uesDn_phi;   //!
   TBranch        *b_met_uesDn_pt;   //!
   TBranch        *b_met_uesUp_phi;   //!
   TBranch        *b_met_uesUp_pt;   //!
   TBranch        *b_mt_goodElectron;   //!
   TBranch        *b_mt_goodElectron_eesDn;   //!
   TBranch        *b_mt_goodElectron_eesUp;   //!
   TBranch        *b_mt_goodElectron_jesDn;   //!
   TBranch        *b_mt_goodElectron_jesUp;   //!
   TBranch        *b_mt_goodElectron_uesDn;   //!
   TBranch        *b_mt_goodElectron_uesUp;   //!
   TBranch        *b_mt_goodMuon;   //!
   TBranch        *b_mt_goodMuon_eesDn;   //!
   TBranch        *b_mt_goodMuon_eesUp;   //!
   TBranch        *b_mt_goodMuon_jesDn;   //!
   TBranch        *b_mt_goodMuon_jesUp;   //!
   TBranch        *b_mt_goodMuon_uesDn;   //!
   TBranch        *b_mt_goodMuon_uesUp;   //!
   TBranch        *b_mt_qcdElectron;   //!
   TBranch        *b_mt_qcdElectron_eesDn;   //!
   TBranch        *b_mt_qcdElectron_eesUp;   //!
   TBranch        *b_mt_qcdElectron_jesDn;   //!
   TBranch        *b_mt_qcdElectron_jesUp;   //!
   TBranch        *b_mt_qcdElectron_uesDn;   //!
   TBranch        *b_mt_qcdElectron_uesUp;   //!
   TBranch        *b_mt_qcdMuon;   //!
   TBranch        *b_mt_qcdMuon_eesDn;   //!
   TBranch        *b_mt_qcdMuon_eesUp;   //!
   TBranch        *b_mt_qcdMuon_jesDn;   //!
   TBranch        *b_mt_qcdMuon_jesUp;   //!
   TBranch        *b_mt_qcdMuon_uesDn;   //!
   TBranch        *b_mt_qcdMuon_uesUp;   //!
   TBranch        *b_LHEProduct;   //!
   TBranch        *b_nbHadrons;   //!
   TBranch        *b_nrAllEle;   //!
   TBranch        *b_nrAllJets;   //!
   TBranch        *b_nrAllMu;   //!
   TBranch        *b_nrCleanJets;   //!
   TBranch        *b_nrFwdJets;   //!
   TBranch        *b_nrGoodEle;   //!
   TBranch        *b_nrGoodJets;   //!
   TBranch        *b_nrGoodMu;   //!
   TBranch        *b_nrQCDEle;   //!
   TBranch        *b_nrQCDMu;   //!
   TBranch        *b_nrVetoEle;   //!
   TBranch        *b_nrVetoMu;   //!
   TBranch        *b_puBXminus;   //!
   TBranch        *b_puTruth;   //!
   TBranch        *b_puBX0;   //!
   TBranch        *b_puBXplus;   //!
   TBranch        *b_qcdEle_charge_vec;   //!
   TBranch        *b_qcdEle_eta_vec;   //!
   TBranch        *b_qcdEle_phi_vec;   //!
   TBranch        *b_qcdEle_pt_vec;   //!
   TBranch        *b_qcdMu_charge_vec;   //!
   TBranch        *b_qcdMu_eta_vec;   //!
   TBranch        *b_qcdMu_phi_vec;   //!
   TBranch        *b_qcdMu_pt_vec;   //!
   TBranch        *b_weightTop;   //!
   TBranch        *b_topPt;   //!
   TBranch        *b_antitopPt;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_wasRun;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_fired;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_prescale;   //!
   TBranch        *b_HLT_IsoMu24_eta2p1_v_error;   //!
   TBranch        *b_HLT_Ele27_WP80_wasRun;   //!
   TBranch        *b_HLT_Ele27_WP80_fired;   //!
   TBranch        *b_HLT_Ele27_WP80_prescale;   //!
   TBranch        *b_HLT_Ele27_WP80_error;   //!
   TBranch        *b_HLT_Any;   //!
   TBranch        *b_vertices;   //!
   TBranch        *b_vetoEle_charge_vec;   //!
   TBranch        *b_vetoEle_eta_vec;   //!
   TBranch        *b_vetoEle_phi_vec;   //!
   TBranch        *b_vetoEle_pt_vec;   //!
   TBranch        *b_vetoMu_charge_vec;   //!
   TBranch        *b_vetoMu_eta_vec;   //!
   TBranch        *b_vetoMu_phi_vec;   //!
   TBranch        *b_vetoMu_pt_vec;   //!

   findMTresolution(TTree *tree=0);
   virtual ~findMTresolution();
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree);
   virtual void     Loop(TString outfileName);
   virtual Bool_t   Notify();
   virtual void     Show(Long64_t entry = -1);
   virtual void     matchGen(Float_t &genPt, Float_t &genEta, Float_t &genPhi,
                             Float_t recoEta, Float_t recoPhi, 
                             Bool_t isMu);
};

#endif

#ifdef findMTresolution_cxx
findMTresolution::findMTresolution(TTree *tree) : fChain(0) 
{
// if parameter tree is not specified (or zero), connect the file
// used to generate this class and read the Tree.
   if (tree == 0) {
      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/hdfs/store/user/tperry/Schweincomp_gen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root");
      if (!f || !f->IsOpen()) {
         f = new TFile("/hdfs/store/user/tperry/Schweincomp_gen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root");
      }
      TDirectory * dir = (TDirectory*)f->Get("/hdfs/store/user/tperry/Schweincomp_gen_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root:/muEleEventTree");
      dir->GetObject("eventTree",tree);

   }
   Init(tree);
}

findMTresolution::~findMTresolution()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
}

Int_t findMTresolution::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t findMTresolution::LoadTree(Long64_t entry)
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

void findMTresolution::Init(TTree *tree)
{
   // The Init() function is called when the selector needs to initialize
   // a new tree or chain. Typically here the branch addresses and branch
   // pointers of the tree will be set.
   // It is normally not necessary to make changes to the generated
   // code, but the routine can be extended by the user if needed.
   // Init() will be called many times when running on PROOF
   // (once per file to be processed).


   hists_mt_reco_mu[0].Clear();
   hists_mt_gen_mu[0].Clear();
   hists_mt_res_mu[0].Clear();
   hists_mt_reco_ele[0].Clear();
   hists_mt_gen_ele[0].Clear();
   hists_mt_res_ele[0].Clear();

   hists_mt_reco_mu[0] = TH1F("hists_mt_reco_mu", "mT reco mu", 200, 0., 200.);  
   hists_mt_gen_mu[0] = TH1F("hists_mt_gen_mu", "mT gen mu", 200, 0., 200.);  
   hists_mt_res_mu[0] = TH1F("hists_mt_res_mu", "mT res mu", 200, -3., 3.);  
   hists_mt_reco_ele[0] = TH1F("hists_mt_reco_ele", "mT reco ele", 200, 0., 200.);  
   hists_mt_gen_ele[0] = TH1F("hists_mt_gen_ele", "mT gen ele", 200, 0., 200.);  
   hists_mt_res_ele[0] = TH1F("hists_mt_res_ele", "mT res ele", 200, -3., 3.);  

   // Set object pointer
   GEN_dressedLeptonPDGID = 0;
   GEN_dressedLeptonETA = 0;
   GEN_dressedLeptonMotherPDGID = 0;
   GEN_dressedLeptonOriginalPT = 0;
   GEN_dressedLeptonPHI = 0;
   GEN_dressedLeptonPT = 0;
   GEN_dressedLeptonType = 0;
   GEN_jetAngleBs = 0;
   GEN_jetEta = 0;
   GEN_jetEtaLeadB = 0;
   GEN_jetEtaSecondB = 0;
   GEN_jetBsMatches = 0;
   GEN_jetPhi = 0;
   GEN_jetPt = 0;
   GEN_jetPtDRHadron = 0;
   GEN_jetPtLeadB = 0;
   GEN_jetPtSecondB = 0;
   GEN_jetPhiLeadB = 0;
   GEN_jetPhiSecondB = 0;
   GEN_neutrinoETA = 0;
   GEN_neutrinoPDGID = 0;
   GEN_neutrinoPHI = 0;
   GEN_neutrinoPT = 0;
   SF_goodEle_IDIso = 0;
   SF_goodEle_IDIsoHLT = 0;
   SF_goodEle_IDIsoHLT_errDn = 0;
   SF_goodEle_IDIsoHLT_errUp = 0;
   SF_goodEle_IDIso_errDn = 0;
   SF_goodEle_IDIso_errUp = 0;
   SF_goodMu_IDIso = 0;
   SF_goodMu_IDIsoHLT = 0;
   SF_goodMu_IDIsoHLT_errDn = 0;
   SF_goodMu_IDIsoHLT_errUp = 0;
   SF_goodMu_IDIso_errDn = 0;
   SF_goodMu_IDIso_errUp = 0;
   bHadronsEta = 0;
   bHadronsID = 0;
   bHadronsPhi = 0;
   bHadronsPt = 0;
   BCandsPt = 0;
   BCandsPhi = 0;
   BCandsEta = 0;
   BCandsPDGID = 0;
   BCandsStatus = 0;
   BCandsMothers = 0;
   CCandsPt = 0;
   CCandsPhi = 0;
   CCandsEta = 0;
   CCandsPDGID = 0;
   CCandsStatus = 0;
   CCandsMothers = 0;
   goodEle_Iso03_vec = 0;
   goodEle_Iso04_vec = 0;
   goodEle_charge_vec = 0;
   goodEle_eta_vec = 0;
   goodEle_mass_vec = 0;
   goodEle_phi_vec = 0;
   goodEle_pt_vec = 0;
   goodMu_charge_vec = 0;
   goodMu_eta_vec = 0;
   goodMu_mass_vec = 0;
   goodMu_phi_vec = 0;
   goodMu_pt_vec = 0;
   qcdEle_charge_vec = 0;
   qcdEle_eta_vec = 0;
   qcdEle_phi_vec = 0;
   qcdEle_pt_vec = 0;
   qcdMu_charge_vec = 0;
   qcdMu_eta_vec = 0;
   qcdMu_phi_vec = 0;
   qcdMu_pt_vec = 0;
   vetoEle_charge_vec = 0;
   vetoEle_eta_vec = 0;
   vetoEle_phi_vec = 0;
   vetoEle_pt_vec = 0;
   vetoMu_charge_vec = 0;
   vetoMu_eta_vec = 0;
   vetoMu_phi_vec = 0;
   vetoMu_pt_vec = 0;
   // Set branch addresses and branch pointers
   if (!tree) return;
   fChain = tree;
   fCurrent = -1;
   fChain->SetMakeClass(1);

   fChain->SetBranchAddress("EVENT", &EVENT, &b_EVENT);
   fChain->SetBranchAddress("RUN", &RUN, &b_RUN);
   fChain->SetBranchAddress("LUMI", &LUMI, &b_LUMI);
   fChain->SetBranchAddress("GBWeight", &GBWeight, &b_GBWeight);
   fChain->SetBranchAddress("GEN_dressedLeptonPDGID", &GEN_dressedLeptonPDGID, &b_GEN_dressedLeptonPDGID);
   fChain->SetBranchAddress("GEN_dressedLeptonETA", &GEN_dressedLeptonETA, &b_GEN_dressedLeptonETA);
   fChain->SetBranchAddress("GEN_dressedLeptonMotherPDGID", &GEN_dressedLeptonMotherPDGID, &b_GEN_dressedLeptonMotherPDGID);
   fChain->SetBranchAddress("GEN_dressedLeptonOriginalPT", &GEN_dressedLeptonOriginalPT, &b_GEN_dressedLeptonOriginalPT);
   fChain->SetBranchAddress("GEN_dressedLeptonPHI", &GEN_dressedLeptonPHI, &b_GEN_dressedLeptonPHI);
   fChain->SetBranchAddress("GEN_dressedLeptonPT", &GEN_dressedLeptonPT, &b_GEN_dressedLeptonPT);
   fChain->SetBranchAddress("GEN_dressedLeptonSIZE", &GEN_dressedLeptonSIZE, &b_GEN_dressedLeptonSIZE);
   fChain->SetBranchAddress("GEN_dressedLeptonType", &GEN_dressedLeptonType, &b_GEN_dressedLeptonType);
   fChain->SetBranchAddress("GEN_jetAngleBs", &GEN_jetAngleBs, &b_GEN_jetAngleBs);
   fChain->SetBranchAddress("GEN_jetEta", &GEN_jetEta, &b_GEN_jetEta);
   fChain->SetBranchAddress("GEN_jetEtaLeadB", &GEN_jetEtaLeadB, &b_GEN_jetEtaLeadB);
   fChain->SetBranchAddress("GEN_jetEtaSecondB", &GEN_jetEtaSecondB, &b_GEN_jetEtaSecondB);
   fChain->SetBranchAddress("GEN_jetBsMatches", &GEN_jetBsMatches, &b_GEN_jetBsMatches);
   fChain->SetBranchAddress("GEN_jetPhi", &GEN_jetPhi, &b_GEN_jetPhi);
   fChain->SetBranchAddress("GEN_jetPt", &GEN_jetPt, &b_GEN_jetPt);
   fChain->SetBranchAddress("GEN_jetPtDRHadron", &GEN_jetPtDRHadron, &b_GEN_jetPtDRHadron);
   fChain->SetBranchAddress("GEN_jetPtLeadB", &GEN_jetPtLeadB, &b_GEN_jetPtLeadB);
   fChain->SetBranchAddress("GEN_jetPtSecondB", &GEN_jetPtSecondB, &b_GEN_jetPtSecondB);
   fChain->SetBranchAddress("GEN_jetPhiLeadB", &GEN_jetPhiLeadB, &b_GEN_jetPhiLeadB);
   fChain->SetBranchAddress("GEN_jetPhiSecondB", &GEN_jetPhiSecondB, &b_GEN_jetPhiSecondB);
   fChain->SetBranchAddress("GEN_neutrinoETA", &GEN_neutrinoETA, &b_GEN_neutrinoETA);
   fChain->SetBranchAddress("GEN_neutrinoPDGID", &GEN_neutrinoPDGID, &b_GEN_neutrinoPDGID);
   fChain->SetBranchAddress("GEN_neutrinoPHI", &GEN_neutrinoPHI, &b_GEN_neutrinoPHI);
   fChain->SetBranchAddress("GEN_neutrinoPT", &GEN_neutrinoPT, &b_GEN_neutrinoPT);
   fChain->SetBranchAddress("J1_eta_gen_NoNu", &J1_eta_gen_NoNu, &b_J1_eta_gen_NoNu);
   fChain->SetBranchAddress("J1_phi_gen_NoNu", &J1_phi_gen_NoNu, &b_J1_phi_gen_NoNu);
   fChain->SetBranchAddress("J1_pt_gen_NoNu", &J1_pt_gen_NoNu, &b_J1_pt_gen_NoNu);
   fChain->SetBranchAddress("J2_eta_gen_NoNu", &J2_eta_gen_NoNu, &b_J2_eta_gen_NoNu);
   fChain->SetBranchAddress("J2_phi_gen_NoNu", &J2_phi_gen_NoNu, &b_J2_phi_gen_NoNu);
   fChain->SetBranchAddress("J2_pt_gen_NoNu", &J2_pt_gen_NoNu, &b_J2_pt_gen_NoNu);
   fChain->SetBranchAddress("J3_eta_gen_NoNu", &J3_eta_gen_NoNu, &b_J3_eta_gen_NoNu);
   fChain->SetBranchAddress("J3_phi_gen_NoNu", &J3_phi_gen_NoNu, &b_J3_phi_gen_NoNu);
   fChain->SetBranchAddress("J3_pt_gen_NoNu", &J3_pt_gen_NoNu, &b_J3_pt_gen_NoNu);
   fChain->SetBranchAddress("J4_eta_gen_NoNu", &J4_eta_gen_NoNu, &b_J4_eta_gen_NoNu);
   fChain->SetBranchAddress("J4_phi_gen_NoNu", &J4_phi_gen_NoNu, &b_J4_phi_gen_NoNu);
   fChain->SetBranchAddress("J4_pt_gen_NoNu", &J4_pt_gen_NoNu, &b_J4_pt_gen_NoNu);
   fChain->SetBranchAddress("SF_goodEle_IDIso", &SF_goodEle_IDIso, &b_SF_goodEle_IDIso);
   fChain->SetBranchAddress("SF_goodEle_IDIsoHLT", &SF_goodEle_IDIsoHLT, &b_SF_goodEle_IDIsoHLT);
   fChain->SetBranchAddress("SF_goodEle_IDIsoHLT_errDn", &SF_goodEle_IDIsoHLT_errDn, &b_SF_goodEle_IDIsoHLT_errDn);
   fChain->SetBranchAddress("SF_goodEle_IDIsoHLT_errUp", &SF_goodEle_IDIsoHLT_errUp, &b_SF_goodEle_IDIsoHLT_errUp);
   fChain->SetBranchAddress("SF_goodEle_IDIso_errDn", &SF_goodEle_IDIso_errDn, &b_SF_goodEle_IDIso_errDn);
   fChain->SetBranchAddress("SF_goodEle_IDIso_errUp", &SF_goodEle_IDIso_errUp, &b_SF_goodEle_IDIso_errUp);
   fChain->SetBranchAddress("SF_goodMu_IDIso", &SF_goodMu_IDIso, &b_SF_goodMu_IDIso);
   fChain->SetBranchAddress("SF_goodMu_IDIsoHLT", &SF_goodMu_IDIsoHLT, &b_SF_goodMu_IDIsoHLT);
   fChain->SetBranchAddress("SF_goodMu_IDIsoHLT_errDn", &SF_goodMu_IDIsoHLT_errDn, &b_SF_goodMu_IDIsoHLT_errDn);
   fChain->SetBranchAddress("SF_goodMu_IDIsoHLT_errUp", &SF_goodMu_IDIsoHLT_errUp, &b_SF_goodMu_IDIsoHLT_errUp);
   fChain->SetBranchAddress("SF_goodMu_IDIso_errDn", &SF_goodMu_IDIso_errDn, &b_SF_goodMu_IDIso_errDn);
   fChain->SetBranchAddress("SF_goodMu_IDIso_errUp", &SF_goodMu_IDIso_errUp, &b_SF_goodMu_IDIso_errUp);
   fChain->SetBranchAddress("SF_lumiWeightPU", &SF_lumiWeightPU, &b_SF_lumiWeightPU);
   fChain->SetBranchAddress("SF_qcdEle_IDIso", &SF_qcdEle_IDIso, &b_SF_qcdEle_IDIso);
   fChain->SetBranchAddress("SF_qcdEle_IDIsoHLT", &SF_qcdEle_IDIsoHLT, &b_SF_qcdEle_IDIsoHLT);
   fChain->SetBranchAddress("SF_qcdEle_IDIsoHLT_errDn", &SF_qcdEle_IDIsoHLT_errDn, &b_SF_qcdEle_IDIsoHLT_errDn);
   fChain->SetBranchAddress("SF_qcdEle_IDIsoHLT_errUp", &SF_qcdEle_IDIsoHLT_errUp, &b_SF_qcdEle_IDIsoHLT_errUp);
   fChain->SetBranchAddress("SF_qcdEle_IDIso_errDn", &SF_qcdEle_IDIso_errDn, &b_SF_qcdEle_IDIso_errDn);
   fChain->SetBranchAddress("SF_qcdEle_IDIso_errUp", &SF_qcdEle_IDIso_errUp, &b_SF_qcdEle_IDIso_errUp);
   fChain->SetBranchAddress("SF_qcdMu_IDIso", &SF_qcdMu_IDIso, &b_SF_qcdMu_IDIso);
   fChain->SetBranchAddress("SF_qcdMu_IDIsoHLT", &SF_qcdMu_IDIsoHLT, &b_SF_qcdMu_IDIsoHLT);
   fChain->SetBranchAddress("SF_qcdMu_IDIsoHLT_errDn", &SF_qcdMu_IDIsoHLT_errDn, &b_SF_qcdMu_IDIsoHLT_errDn);
   fChain->SetBranchAddress("SF_qcdMu_IDIsoHLT_errUp", &SF_qcdMu_IDIsoHLT_errUp, &b_SF_qcdMu_IDIsoHLT_errUp);
   fChain->SetBranchAddress("SF_qcdMu_IDIso_errDn", &SF_qcdMu_IDIso_errDn, &b_SF_qcdMu_IDIso_errDn);
   fChain->SetBranchAddress("SF_qcdMu_IDIso_errUp", &SF_qcdMu_IDIso_errUp, &b_SF_qcdMu_IDIso_errUp);
   fChain->SetBranchAddress("bCandidate1Eta", &bCandidate1Eta, &b_bCandidate1Eta);
   fChain->SetBranchAddress("bCandidate1Phi", &bCandidate1Phi, &b_bCandidate1Phi);
   fChain->SetBranchAddress("bCandidate1Pt", &bCandidate1Pt, &b_bCandidate1Pt);
   fChain->SetBranchAddress("bCandidate2Eta", &bCandidate2Eta, &b_bCandidate2Eta);
   fChain->SetBranchAddress("bCandidate2Phi", &bCandidate2Phi, &b_bCandidate2Phi);
   fChain->SetBranchAddress("bCandidate2Pt", &bCandidate2Pt, &b_bCandidate2Pt);
   fChain->SetBranchAddress("bCandidateBC1MASS", &bCandidateBC1MASS, &b_bCandidateBC1MASS);
   fChain->SetBranchAddress("bCandidateBC1nTracks", &bCandidateBC1nTracks, &b_bCandidateBC1nTracks);
   fChain->SetBranchAddress("bCandidateBC2MASS", &bCandidateBC2MASS, &b_bCandidateBC2MASS);
   fChain->SetBranchAddress("bCandidateBC2nTracks", &bCandidateBC2nTracks, &b_bCandidateBC2nTracks);
   fChain->SetBranchAddress("bCandidateBCDeltaR", &bCandidateBCDeltaR, &b_bCandidateBCDeltaR);
   fChain->SetBranchAddress("bCandidateBCEnergySum", &bCandidateBCEnergySum, &b_bCandidateBCEnergySum);
   fChain->SetBranchAddress("bCandidateBCGenEnergySum", &bCandidateBCGenEnergySum, &b_bCandidateBCGenEnergySum);
   fChain->SetBranchAddress("bCandidateBDeltaPHI", &bCandidateBDeltaPHI, &b_bCandidateBDeltaPHI);
   fChain->SetBranchAddress("bCandidateDeltaPhi", &bCandidateDeltaPhi, &b_bCandidateDeltaPhi);
   fChain->SetBranchAddress("bCandidateDeltaR", &bCandidateDeltaR, &b_bCandidateDeltaR);
   fChain->SetBranchAddress("bCandidateJet1BC1ETA", &bCandidateJet1BC1ETA, &b_bCandidateJet1BC1ETA);
   fChain->SetBranchAddress("bCandidateJet1BC1PHI", &bCandidateJet1BC1PHI, &b_bCandidateJet1BC1PHI);
   fChain->SetBranchAddress("bCandidateJet1BC1PT", &bCandidateJet1BC1PT, &b_bCandidateJet1BC1PT);
   fChain->SetBranchAddress("bCandidateJet1BC2ETA", &bCandidateJet1BC2ETA, &b_bCandidateJet1BC2ETA);
   fChain->SetBranchAddress("bCandidateJet1BC2PHI", &bCandidateJet1BC2PHI, &b_bCandidateJet1BC2PHI);
   fChain->SetBranchAddress("bCandidateJet1BC2PT", &bCandidateJet1BC2PT, &b_bCandidateJet1BC2PT);
   fChain->SetBranchAddress("bCandidateJet2BC1ETA", &bCandidateJet2BC1ETA, &b_bCandidateJet2BC1ETA);
   fChain->SetBranchAddress("bCandidateJet2BC1PHI", &bCandidateJet2BC1PHI, &b_bCandidateJet2BC1PHI);
   fChain->SetBranchAddress("bCandidateJet2BC1PT", &bCandidateJet2BC1PT, &b_bCandidateJet2BC1PT);
   fChain->SetBranchAddress("bCandidateJet2BC2ETA", &bCandidateJet2BC2ETA, &b_bCandidateJet2BC2ETA);
   fChain->SetBranchAddress("bCandidateJet2BC2PHI", &bCandidateJet2BC2PHI, &b_bCandidateJet2BC2PHI);
   fChain->SetBranchAddress("bCandidateJet2BC2PT", &bCandidateJet2BC2PT, &b_bCandidateJet2BC2PT);
   fChain->SetBranchAddress("bCandidateJet3BC1ETA", &bCandidateJet3BC1ETA, &b_bCandidateJet3BC1ETA);
   fChain->SetBranchAddress("bCandidateJet3BC1PHI", &bCandidateJet3BC1PHI, &b_bCandidateJet3BC1PHI);
   fChain->SetBranchAddress("bCandidateJet3BC1PT", &bCandidateJet3BC1PT, &b_bCandidateJet3BC1PT);
   fChain->SetBranchAddress("bCandidateJet3BC2ETA", &bCandidateJet3BC2ETA, &b_bCandidateJet3BC2ETA);
   fChain->SetBranchAddress("bCandidateJet3BC2PHI", &bCandidateJet3BC2PHI, &b_bCandidateJet3BC2PHI);
   fChain->SetBranchAddress("bCandidateJet3BC2PT", &bCandidateJet3BC2PT, &b_bCandidateJet3BC2PT);
   fChain->SetBranchAddress("bCandidateJet4BC1ETA", &bCandidateJet4BC1ETA, &b_bCandidateJet4BC1ETA);
   fChain->SetBranchAddress("bCandidateJet4BC1PHI", &bCandidateJet4BC1PHI, &b_bCandidateJet4BC1PHI);
   fChain->SetBranchAddress("bCandidateJet4BC1PT", &bCandidateJet4BC1PT, &b_bCandidateJet4BC1PT);
   fChain->SetBranchAddress("bCandidateJet4BC2ETA", &bCandidateJet4BC2ETA, &b_bCandidateJet4BC2ETA);
   fChain->SetBranchAddress("bCandidateJet4BC2PHI", &bCandidateJet4BC2PHI, &b_bCandidateJet4BC2PHI);
   fChain->SetBranchAddress("bCandidateJet4BC2PT", &bCandidateJet4BC2PT, &b_bCandidateJet4BC2PT);
   fChain->SetBranchAddress("bCandidatenBC", &bCandidatenBC, &b_bCandidatenBC);
   fChain->SetBranchAddress("bCandidatenJetAssociatedToBC", &bCandidatenJetAssociatedToBC, &b_bCandidatenJetAssociatedToBC);
   fChain->SetBranchAddress("bCandidatenJetAssociatedToBC1", &bCandidatenJetAssociatedToBC1, &b_bCandidatenJetAssociatedToBC1);
   fChain->SetBranchAddress("bCandidatenJetAssociatedToBC2", &bCandidatenJetAssociatedToBC2, &b_bCandidatenJetAssociatedToBC2);
   fChain->SetBranchAddress("bHadronsEta", &bHadronsEta, &b_bHadronsEta);
   fChain->SetBranchAddress("bHadronsID", &bHadronsID, &b_bHadronsID);
   fChain->SetBranchAddress("bHadronsPhi", &bHadronsPhi, &b_bHadronsPhi);
   fChain->SetBranchAddress("bHadronsPt", &bHadronsPt, &b_bHadronsPt);
   fChain->SetBranchAddress("fwdJ1_CSV", &fwdJ1_CSV, &b_fwdJ1_CSV);
   fChain->SetBranchAddress("fwdJ1_CSVreweight", &fwdJ1_CSVreweight, &b_fwdJ1_CSVreweight);
   fChain->SetBranchAddress("fwdJ1_SF_CSVL", &fwdJ1_SF_CSVL, &b_fwdJ1_SF_CSVL);
   fChain->SetBranchAddress("fwdJ1_SF_CSVL_errDn", &fwdJ1_SF_CSVL_errDn, &b_fwdJ1_SF_CSVL_errDn);
   fChain->SetBranchAddress("fwdJ1_SF_CSVL_errUp", &fwdJ1_SF_CSVL_errUp, &b_fwdJ1_SF_CSVL_errUp);
   fChain->SetBranchAddress("fwdJ1_SF_CSVM", &fwdJ1_SF_CSVM, &b_fwdJ1_SF_CSVM);
   fChain->SetBranchAddress("fwdJ1_SF_CSVM_errDn", &fwdJ1_SF_CSVM_errDn, &b_fwdJ1_SF_CSVM_errDn);
   fChain->SetBranchAddress("fwdJ1_SF_CSVM_errUp", &fwdJ1_SF_CSVM_errUp, &b_fwdJ1_SF_CSVM_errUp);
   fChain->SetBranchAddress("fwdJ1_SF_CSVT", &fwdJ1_SF_CSVT, &b_fwdJ1_SF_CSVT);
   fChain->SetBranchAddress("fwdJ1_SF_CSVT_errDn", &fwdJ1_SF_CSVT_errDn, &b_fwdJ1_SF_CSVT_errDn);
   fChain->SetBranchAddress("fwdJ1_SF_CSVT_errUp", &fwdJ1_SF_CSVT_errUp, &b_fwdJ1_SF_CSVT_errUp);
   fChain->SetBranchAddress("fwdJ1_eta", &fwdJ1_eta, &b_fwdJ1_eta);
   fChain->SetBranchAddress("fwdJ1_mass", &fwdJ1_mass, &b_fwdJ1_mass);
   fChain->SetBranchAddress("fwdJ1_partonFlavour", &fwdJ1_partonFlavour, &b_fwdJ1_partonFlavour);
   fChain->SetBranchAddress("fwdJ1_phi", &fwdJ1_phi, &b_fwdJ1_phi);
   fChain->SetBranchAddress("fwdJ1_pt", &fwdJ1_pt, &b_fwdJ1_pt);
   fChain->SetBranchAddress("fwdJ1_pt_resUp", &fwdJ1_pt_resUp, &b_fwdJ1_pt_resUp);
   fChain->SetBranchAddress("fwdJ2_CSV", &fwdJ2_CSV, &b_fwdJ2_CSV);
   fChain->SetBranchAddress("fwdJ2_CSVreweight", &fwdJ2_CSVreweight, &b_fwdJ2_CSVreweight);
   fChain->SetBranchAddress("fwdJ2_SF_CSVL", &fwdJ2_SF_CSVL, &b_fwdJ2_SF_CSVL);
   fChain->SetBranchAddress("fwdJ2_SF_CSVL_errDn", &fwdJ2_SF_CSVL_errDn, &b_fwdJ2_SF_CSVL_errDn);
   fChain->SetBranchAddress("fwdJ2_SF_CSVL_errUp", &fwdJ2_SF_CSVL_errUp, &b_fwdJ2_SF_CSVL_errUp);
   fChain->SetBranchAddress("fwdJ2_SF_CSVM", &fwdJ2_SF_CSVM, &b_fwdJ2_SF_CSVM);
   fChain->SetBranchAddress("fwdJ2_SF_CSVM_errDn", &fwdJ2_SF_CSVM_errDn, &b_fwdJ2_SF_CSVM_errDn);
   fChain->SetBranchAddress("fwdJ2_SF_CSVM_errUp", &fwdJ2_SF_CSVM_errUp, &b_fwdJ2_SF_CSVM_errUp);
   fChain->SetBranchAddress("fwdJ2_SF_CSVT", &fwdJ2_SF_CSVT, &b_fwdJ2_SF_CSVT);
   fChain->SetBranchAddress("fwdJ2_SF_CSVT_errDn", &fwdJ2_SF_CSVT_errDn, &b_fwdJ2_SF_CSVT_errDn);
   fChain->SetBranchAddress("fwdJ2_SF_CSVT_errUp", &fwdJ2_SF_CSVT_errUp, &b_fwdJ2_SF_CSVT_errUp);
   fChain->SetBranchAddress("fwdJ2_eta", &fwdJ2_eta, &b_fwdJ2_eta);
   fChain->SetBranchAddress("fwdJ2_mass", &fwdJ2_mass, &b_fwdJ2_mass);
   fChain->SetBranchAddress("fwdJ2_partonFlavour", &fwdJ2_partonFlavour, &b_fwdJ2_partonFlavour);
   fChain->SetBranchAddress("fwdJ2_phi", &fwdJ2_phi, &b_fwdJ2_phi);
   fChain->SetBranchAddress("fwdJ2_pt", &fwdJ2_pt, &b_fwdJ2_pt);
   fChain->SetBranchAddress("fwdJ2_pt_resUp", &fwdJ2_pt_resUp, &b_fwdJ2_pt_resUp);
   fChain->SetBranchAddress("genBs", &genBs, &b_genBs);
   fChain->SetBranchAddress("genCs", &genCs, &b_genCs);
   fChain->SetBranchAddress("genDs", &genDs, &b_genDs);
   fChain->SetBranchAddress("genWLeptonID", &genWLeptonID, &b_genWLeptonID);
   fChain->SetBranchAddress("genLeptonPT", &genLeptonPT, &b_genLeptonPT);
   fChain->SetBranchAddress("genLeptonETA", &genLeptonETA, &b_genLeptonETA);
   fChain->SetBranchAddress("genLeptonPHI", &genLeptonPHI, &b_genLeptonPHI);
   fChain->SetBranchAddress("genWBs", &genWBs, &b_genWBs);
   fChain->SetBranchAddress("genWCs", &genWCs, &b_genWCs);
   fChain->SetBranchAddress("genWGs", &genWGs, &b_genWGs);
   fChain->SetBranchAddress("genWBbar", &genWBbar, &b_genWBbar);
   fChain->SetBranchAddress("genWB", &genWB, &b_genWB);
   fChain->SetBranchAddress("genWBbar_st3", &genWBbar_st3, &b_genWBbar_st3);
   fChain->SetBranchAddress("genWCbar_st3", &genWCbar_st3, &b_genWCbar_st3);
   fChain->SetBranchAddress("genWB_st3", &genWB_st3, &b_genWB_st3);
   fChain->SetBranchAddress("genWC_st3", &genWC_st3, &b_genWC_st3);
   fChain->SetBranchAddress("genWGs_st3", &genWGs_st3, &b_genWGs_st3);
   fChain->SetBranchAddress("genWBbar_AfterW", &genWBbar_AfterW, &b_genWBbar_AfterW);
   fChain->SetBranchAddress("genWCbar_AfterW", &genWCbar_AfterW, &b_genWCbar_AfterW);
   fChain->SetBranchAddress("genWB_AfterW", &genWB_AfterW, &b_genWB_AfterW);
   fChain->SetBranchAddress("genWC_AfterW", &genWC_AfterW, &b_genWC_AfterW);
   fChain->SetBranchAddress("genWGs_AfterW", &genWGs_AfterW, &b_genWGs_AfterW);
   fChain->SetBranchAddress("infoNUP", &infoNUP, &b_infoNUP);
   fChain->SetBranchAddress("foundB", &foundB, &b_foundB);
   fChain->SetBranchAddress("foundBbar", &foundBbar, &b_foundBbar);
   fChain->SetBranchAddress("foundC", &foundC, &b_foundC);
   fChain->SetBranchAddress("foundCbar", &foundCbar, &b_foundCbar);
   fChain->SetBranchAddress("gluonPythiaForB", &gluonPythiaForB, &b_gluonPythiaForB);
   fChain->SetBranchAddress("gluonPythiaForC", &gluonPythiaForC, &b_gluonPythiaForC);
   fChain->SetBranchAddress("gluonMadgraphForB", &gluonMadgraphForB, &b_gluonMadgraphForB);
   fChain->SetBranchAddress("gluonMadgraphForC", &gluonMadgraphForC, &b_gluonMadgraphForC);
   fChain->SetBranchAddress("BCandsPt", &BCandsPt, &b_BCandsPt);
   fChain->SetBranchAddress("BCandsPhi", &BCandsPhi, &b_BCandsPhi);
   fChain->SetBranchAddress("BCandsEta", &BCandsEta, &b_BCandsEta);
   fChain->SetBranchAddress("BCandsPDGID", &BCandsPDGID, &b_BCandsPDGID);
   fChain->SetBranchAddress("BCandsStatus", &BCandsStatus, &b_BCandsStatus);
   fChain->SetBranchAddress("BCandsMothers", &BCandsMothers, &b_BCandsMothers);
   fChain->SetBranchAddress("CCandsPt", &CCandsPt, &b_CCandsPt);
   fChain->SetBranchAddress("CCandsPhi", &CCandsPhi, &b_CCandsPhi);
   fChain->SetBranchAddress("CCandsEta", &CCandsEta, &b_CCandsEta);
   fChain->SetBranchAddress("CCandsPDGID", &CCandsPDGID, &b_CCandsPDGID);
   fChain->SetBranchAddress("CCandsStatus", &CCandsStatus, &b_CCandsStatus);
   fChain->SetBranchAddress("CCandsMothers", &CCandsMothers, &b_CCandsMothers);
   fChain->SetBranchAddress("genSs", &genSs, &b_genSs);
   fChain->SetBranchAddress("genTbars", &genTbars, &b_genTbars);
   fChain->SetBranchAddress("genTs", &genTs, &b_genTs);
   fChain->SetBranchAddress("genUs", &genUs, &b_genUs);
   fChain->SetBranchAddress("genWs", &genWs, &b_genWs);
   fChain->SetBranchAddress("goodEle_Iso03_vec", &goodEle_Iso03_vec, &b_goodEle_Iso03_vec);
   fChain->SetBranchAddress("goodEle_Iso04_vec", &goodEle_Iso04_vec, &b_goodEle_Iso04_vec);
   fChain->SetBranchAddress("goodEle_charge_vec", &goodEle_charge_vec, &b_goodEle_charge_vec);
   fChain->SetBranchAddress("goodEle_eta_vec", &goodEle_eta_vec, &b_goodEle_eta_vec);
   fChain->SetBranchAddress("goodEle_mass_vec", &goodEle_mass_vec, &b_goodEle_mass_vec);
   fChain->SetBranchAddress("goodEle_phi_vec", &goodEle_phi_vec, &b_goodEle_phi_vec);
   fChain->SetBranchAddress("goodEle_pt_vec", &goodEle_pt_vec, &b_goodEle_pt_vec);
   fChain->SetBranchAddress("goodJ1_CSV", &goodJ1_CSV, &b_goodJ1_CSV);
   fChain->SetBranchAddress("goodJ1_CSVreweight", &goodJ1_CSVreweight, &b_goodJ1_CSVreweight);
   fChain->SetBranchAddress("goodJ1_SF_CSVL", &goodJ1_SF_CSVL, &b_goodJ1_SF_CSVL);
   fChain->SetBranchAddress("goodJ1_SF_CSVL_errDn", &goodJ1_SF_CSVL_errDn, &b_goodJ1_SF_CSVL_errDn);
   fChain->SetBranchAddress("goodJ1_SF_CSVL_errUp", &goodJ1_SF_CSVL_errUp, &b_goodJ1_SF_CSVL_errUp);
   fChain->SetBranchAddress("goodJ1_SF_CSVM", &goodJ1_SF_CSVM, &b_goodJ1_SF_CSVM);
   fChain->SetBranchAddress("goodJ1_SF_CSVM_errDn", &goodJ1_SF_CSVM_errDn, &b_goodJ1_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ1_SF_CSVM_errUp", &goodJ1_SF_CSVM_errUp, &b_goodJ1_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ1_SF_CSVT", &goodJ1_SF_CSVT, &b_goodJ1_SF_CSVT);
   fChain->SetBranchAddress("goodJ1_SF_CSVT_errDn", &goodJ1_SF_CSVT_errDn, &b_goodJ1_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ1_SF_CSVT_errUp", &goodJ1_SF_CSVT_errUp, &b_goodJ1_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ1_eta", &goodJ1_eta, &b_goodJ1_eta);
   fChain->SetBranchAddress("goodJ1_mass", &goodJ1_mass, &b_goodJ1_mass);
   fChain->SetBranchAddress("goodJ1_mass_SV_corrected", &goodJ1_mass_SV_corrected, &b_goodJ1_mass_SV_corrected);
   fChain->SetBranchAddress("goodJ1_mass_SV_unweighted", &goodJ1_mass_SV_unweighted, &b_goodJ1_mass_SV_unweighted);
   fChain->SetBranchAddress("goodJ1_mass_SV_weighted", &goodJ1_mass_SV_weighted, &b_goodJ1_mass_SV_weighted);
   fChain->SetBranchAddress("goodJ1_partonFlavour", &goodJ1_partonFlavour, &b_goodJ1_partonFlavour);
   fChain->SetBranchAddress("goodJ1_phi", &goodJ1_phi, &b_goodJ1_phi);
   fChain->SetBranchAddress("goodJ1_pt", &goodJ1_pt, &b_goodJ1_pt);
   fChain->SetBranchAddress("goodJ1_pt_SV_unweighted", &goodJ1_pt_SV_unweighted, &b_goodJ1_pt_SV_unweighted);
   fChain->SetBranchAddress("goodJ1_pt_SV_weighted", &goodJ1_pt_SV_weighted, &b_goodJ1_pt_SV_weighted);
   fChain->SetBranchAddress("goodJ1_pt_resDown", &goodJ1_pt_resDown, &b_goodJ1_pt_resDown);
   fChain->SetBranchAddress("goodJ1_pt_resUp", &goodJ1_pt_resUp, &b_goodJ1_pt_resUp);
   fChain->SetBranchAddress("goodJ1_shift_pt", &goodJ1_shift_pt, &b_goodJ1_shift_pt);
   fChain->SetBranchAddress("goodJ1_shift_pt_Dn", &goodJ1_shift_pt_Dn, &b_goodJ1_shift_pt_Dn);
   fChain->SetBranchAddress("goodJ1_shift_pt_Up", &goodJ1_shift_pt_Up, &b_goodJ1_shift_pt_Up);
   fChain->SetBranchAddress("goodJ1_total_shift_pt", &goodJ1_total_shift_pt, &b_goodJ1_total_shift_pt);
   fChain->SetBranchAddress("goodJ1_total_shift_pt_Dn", &goodJ1_total_shift_pt_Dn, &b_goodJ1_total_shift_pt_Dn);
   fChain->SetBranchAddress("goodJ1_total_shift_pt_Up", &goodJ1_total_shift_pt_Up, &b_goodJ1_total_shift_pt_Up);
   fChain->SetBranchAddress("goodJ2_CSV", &goodJ2_CSV, &b_goodJ2_CSV);
   fChain->SetBranchAddress("goodJ2_CSVreweight", &goodJ2_CSVreweight, &b_goodJ2_CSVreweight);
   fChain->SetBranchAddress("goodJ2_SF_CSVL", &goodJ2_SF_CSVL, &b_goodJ2_SF_CSVL);
   fChain->SetBranchAddress("goodJ2_SF_CSVL_errDn", &goodJ2_SF_CSVL_errDn, &b_goodJ2_SF_CSVL_errDn);
   fChain->SetBranchAddress("goodJ2_SF_CSVL_errUp", &goodJ2_SF_CSVL_errUp, &b_goodJ2_SF_CSVL_errUp);
   fChain->SetBranchAddress("goodJ2_SF_CSVM", &goodJ2_SF_CSVM, &b_goodJ2_SF_CSVM);
   fChain->SetBranchAddress("goodJ2_SF_CSVM_errDn", &goodJ2_SF_CSVM_errDn, &b_goodJ2_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ2_SF_CSVM_errUp", &goodJ2_SF_CSVM_errUp, &b_goodJ2_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ2_SF_CSVT", &goodJ2_SF_CSVT, &b_goodJ2_SF_CSVT);
   fChain->SetBranchAddress("goodJ2_SF_CSVT_errDn", &goodJ2_SF_CSVT_errDn, &b_goodJ2_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ2_SF_CSVT_errUp", &goodJ2_SF_CSVT_errUp, &b_goodJ2_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ2_eta", &goodJ2_eta, &b_goodJ2_eta);
   fChain->SetBranchAddress("goodJ2_mass", &goodJ2_mass, &b_goodJ2_mass);
   fChain->SetBranchAddress("goodJ2_mass_SV_corrected", &goodJ2_mass_SV_corrected, &b_goodJ2_mass_SV_corrected);
   fChain->SetBranchAddress("goodJ2_mass_SV_unweighted", &goodJ2_mass_SV_unweighted, &b_goodJ2_mass_SV_unweighted);
   fChain->SetBranchAddress("goodJ2_mass_SV_weighted", &goodJ2_mass_SV_weighted, &b_goodJ2_mass_SV_weighted);
   fChain->SetBranchAddress("goodJ2_partonFlavour", &goodJ2_partonFlavour, &b_goodJ2_partonFlavour);
   fChain->SetBranchAddress("goodJ2_phi", &goodJ2_phi, &b_goodJ2_phi);
   fChain->SetBranchAddress("goodJ2_pt", &goodJ2_pt, &b_goodJ2_pt);
   fChain->SetBranchAddress("goodJ2_pt_SV_unweighted", &goodJ2_pt_SV_unweighted, &b_goodJ2_pt_SV_unweighted);
   fChain->SetBranchAddress("goodJ2_pt_SV_weighted", &goodJ2_pt_SV_weighted, &b_goodJ2_pt_SV_weighted);
   fChain->SetBranchAddress("goodJ2_pt_resDown", &goodJ2_pt_resDown, &b_goodJ2_pt_resDown);
   fChain->SetBranchAddress("goodJ2_pt_resUp", &goodJ2_pt_resUp, &b_goodJ2_pt_resUp);
   fChain->SetBranchAddress("goodJ2_shift_pt", &goodJ2_shift_pt, &b_goodJ2_shift_pt);
   fChain->SetBranchAddress("goodJ2_shift_pt_Dn", &goodJ2_shift_pt_Dn, &b_goodJ2_shift_pt_Dn);
   fChain->SetBranchAddress("goodJ2_shift_pt_Up", &goodJ2_shift_pt_Up, &b_goodJ2_shift_pt_Up);
   fChain->SetBranchAddress("goodJ2_total_shift_pt", &goodJ2_total_shift_pt, &b_goodJ2_total_shift_pt);
   fChain->SetBranchAddress("goodJ2_total_shift_pt_Dn", &goodJ2_total_shift_pt_Dn, &b_goodJ2_total_shift_pt_Dn);
   fChain->SetBranchAddress("goodJ2_total_shift_pt_Up", &goodJ2_total_shift_pt_Up, &b_goodJ2_total_shift_pt_Up);
   fChain->SetBranchAddress("goodJ3_CSV", &goodJ3_CSV, &b_goodJ3_CSV);
   fChain->SetBranchAddress("goodJ3_CSVreweight", &goodJ3_CSVreweight, &b_goodJ3_CSVreweight);
   fChain->SetBranchAddress("goodJ3_SF_CSVL", &goodJ3_SF_CSVL, &b_goodJ3_SF_CSVL);
   fChain->SetBranchAddress("goodJ3_SF_CSVL_errDn", &goodJ3_SF_CSVL_errDn, &b_goodJ3_SF_CSVL_errDn);
   fChain->SetBranchAddress("goodJ3_SF_CSVL_errUp", &goodJ3_SF_CSVL_errUp, &b_goodJ3_SF_CSVL_errUp);
   fChain->SetBranchAddress("goodJ3_SF_CSVM", &goodJ3_SF_CSVM, &b_goodJ3_SF_CSVM);
   fChain->SetBranchAddress("goodJ3_SF_CSVM_errDn", &goodJ3_SF_CSVM_errDn, &b_goodJ3_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ3_SF_CSVM_errUp", &goodJ3_SF_CSVM_errUp, &b_goodJ3_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ3_SF_CSVT", &goodJ3_SF_CSVT, &b_goodJ3_SF_CSVT);
   fChain->SetBranchAddress("goodJ3_SF_CSVT_errDn", &goodJ3_SF_CSVT_errDn, &b_goodJ3_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ3_SF_CSVT_errUp", &goodJ3_SF_CSVT_errUp, &b_goodJ3_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ3_eta", &goodJ3_eta, &b_goodJ3_eta);
   fChain->SetBranchAddress("goodJ3_mass", &goodJ3_mass, &b_goodJ3_mass);
   fChain->SetBranchAddress("goodJ3_mass_SV_corrected", &goodJ3_mass_SV_corrected, &b_goodJ3_mass_SV_corrected);
   fChain->SetBranchAddress("goodJ3_mass_SV_unweighted", &goodJ3_mass_SV_unweighted, &b_goodJ3_mass_SV_unweighted);
   fChain->SetBranchAddress("goodJ3_mass_SV_weighted", &goodJ3_mass_SV_weighted, &b_goodJ3_mass_SV_weighted);
   fChain->SetBranchAddress("goodJ3_partonFlavour", &goodJ3_partonFlavour, &b_goodJ3_partonFlavour);
   fChain->SetBranchAddress("goodJ3_phi", &goodJ3_phi, &b_goodJ3_phi);
   fChain->SetBranchAddress("goodJ3_pt", &goodJ3_pt, &b_goodJ3_pt);
   fChain->SetBranchAddress("goodJ3_pt_SV_unweighted", &goodJ3_pt_SV_unweighted, &b_goodJ3_pt_SV_unweighted);
   fChain->SetBranchAddress("goodJ3_pt_SV_weighted", &goodJ3_pt_SV_weighted, &b_goodJ3_pt_SV_weighted);
   fChain->SetBranchAddress("goodJ3_pt_resDown", &goodJ3_pt_resDown, &b_goodJ3_pt_resDown);
   fChain->SetBranchAddress("goodJ3_pt_resUp", &goodJ3_pt_resUp, &b_goodJ3_pt_resUp);
   fChain->SetBranchAddress("goodJ4_CSV", &goodJ4_CSV, &b_goodJ4_CSV);
   fChain->SetBranchAddress("goodJ4_CSVreweight", &goodJ4_CSVreweight, &b_goodJ4_CSVreweight);
   fChain->SetBranchAddress("goodJ4_SF_CSVL", &goodJ4_SF_CSVL, &b_goodJ4_SF_CSVL);
   fChain->SetBranchAddress("goodJ4_SF_CSVL_errDn", &goodJ4_SF_CSVL_errDn, &b_goodJ4_SF_CSVL_errDn);
   fChain->SetBranchAddress("goodJ4_SF_CSVL_errUp", &goodJ4_SF_CSVL_errUp, &b_goodJ4_SF_CSVL_errUp);
   fChain->SetBranchAddress("goodJ4_SF_CSVM", &goodJ4_SF_CSVM, &b_goodJ4_SF_CSVM);
   fChain->SetBranchAddress("goodJ4_SF_CSVM_errDn", &goodJ4_SF_CSVM_errDn, &b_goodJ4_SF_CSVM_errDn);
   fChain->SetBranchAddress("goodJ4_SF_CSVM_errUp", &goodJ4_SF_CSVM_errUp, &b_goodJ4_SF_CSVM_errUp);
   fChain->SetBranchAddress("goodJ4_SF_CSVT", &goodJ4_SF_CSVT, &b_goodJ4_SF_CSVT);
   fChain->SetBranchAddress("goodJ4_SF_CSVT_errDn", &goodJ4_SF_CSVT_errDn, &b_goodJ4_SF_CSVT_errDn);
   fChain->SetBranchAddress("goodJ4_SF_CSVT_errUp", &goodJ4_SF_CSVT_errUp, &b_goodJ4_SF_CSVT_errUp);
   fChain->SetBranchAddress("goodJ4_eta", &goodJ4_eta, &b_goodJ4_eta);
   fChain->SetBranchAddress("goodJ4_mass", &goodJ4_mass, &b_goodJ4_mass);
   fChain->SetBranchAddress("goodJ4_partonFlavour", &goodJ4_partonFlavour, &b_goodJ4_partonFlavour);
   fChain->SetBranchAddress("goodJ4_phi", &goodJ4_phi, &b_goodJ4_phi);
   fChain->SetBranchAddress("goodJ4_pt", &goodJ4_pt, &b_goodJ4_pt);
   fChain->SetBranchAddress("goodJ4_pt_resDown", &goodJ4_pt_resDown, &b_goodJ4_pt_resDown);
   fChain->SetBranchAddress("goodJ4_pt_resUp", &goodJ4_pt_resUp, &b_goodJ4_pt_resUp);
   fChain->SetBranchAddress("goodMu_charge_vec", &goodMu_charge_vec, &b_goodMu_charge_vec);
   fChain->SetBranchAddress("goodMu_eta_vec", &goodMu_eta_vec, &b_goodMu_eta_vec);
   fChain->SetBranchAddress("goodMu_mass_vec", &goodMu_mass_vec, &b_goodMu_mass_vec);
   fChain->SetBranchAddress("goodMu_phi_vec", &goodMu_phi_vec, &b_goodMu_phi_vec);
   fChain->SetBranchAddress("goodMu_pt_vec", &goodMu_pt_vec, &b_goodMu_pt_vec);
   fChain->SetBranchAddress("met_eesDn_phi", &met_eesDn_phi, &b_met_eesDn_phi);
   fChain->SetBranchAddress("met_eesDn_pt", &met_eesDn_pt, &b_met_eesDn_pt);
   fChain->SetBranchAddress("met_eesUp_phi", &met_eesUp_phi, &b_met_eesUp_phi);
   fChain->SetBranchAddress("met_eesUp_pt", &met_eesUp_pt, &b_met_eesUp_pt);
   fChain->SetBranchAddress("met_jesDn_phi", &met_jesDn_phi, &b_met_jesDn_phi);
   fChain->SetBranchAddress("met_jesDn_pt", &met_jesDn_pt, &b_met_jesDn_pt);
   fChain->SetBranchAddress("met_jesUp_phi", &met_jesUp_phi, &b_met_jesUp_phi);
   fChain->SetBranchAddress("met_jesUp_pt", &met_jesUp_pt, &b_met_jesUp_pt);
   fChain->SetBranchAddress("met_phi", &met_phi, &b_met_phi);
   fChain->SetBranchAddress("met_pt", &met_pt, &b_met_pt);
   fChain->SetBranchAddress("met_uesDn_phi", &met_uesDn_phi, &b_met_uesDn_phi);
   fChain->SetBranchAddress("met_uesDn_pt", &met_uesDn_pt, &b_met_uesDn_pt);
   fChain->SetBranchAddress("met_uesUp_phi", &met_uesUp_phi, &b_met_uesUp_phi);
   fChain->SetBranchAddress("met_uesUp_pt", &met_uesUp_pt, &b_met_uesUp_pt);
   fChain->SetBranchAddress("mt_goodElectron", &mt_goodElectron, &b_mt_goodElectron);
   fChain->SetBranchAddress("mt_goodElectron_eesDn", &mt_goodElectron_eesDn, &b_mt_goodElectron_eesDn);
   fChain->SetBranchAddress("mt_goodElectron_eesUp", &mt_goodElectron_eesUp, &b_mt_goodElectron_eesUp);
   fChain->SetBranchAddress("mt_goodElectron_jesDn", &mt_goodElectron_jesDn, &b_mt_goodElectron_jesDn);
   fChain->SetBranchAddress("mt_goodElectron_jesUp", &mt_goodElectron_jesUp, &b_mt_goodElectron_jesUp);
   fChain->SetBranchAddress("mt_goodElectron_uesDn", &mt_goodElectron_uesDn, &b_mt_goodElectron_uesDn);
   fChain->SetBranchAddress("mt_goodElectron_uesUp", &mt_goodElectron_uesUp, &b_mt_goodElectron_uesUp);
   fChain->SetBranchAddress("mt_goodMuon", &mt_goodMuon, &b_mt_goodMuon);
   fChain->SetBranchAddress("mt_goodMuon_eesDn", &mt_goodMuon_eesDn, &b_mt_goodMuon_eesDn);
   fChain->SetBranchAddress("mt_goodMuon_eesUp", &mt_goodMuon_eesUp, &b_mt_goodMuon_eesUp);
   fChain->SetBranchAddress("mt_goodMuon_jesDn", &mt_goodMuon_jesDn, &b_mt_goodMuon_jesDn);
   fChain->SetBranchAddress("mt_goodMuon_jesUp", &mt_goodMuon_jesUp, &b_mt_goodMuon_jesUp);
   fChain->SetBranchAddress("mt_goodMuon_uesDn", &mt_goodMuon_uesDn, &b_mt_goodMuon_uesDn);
   fChain->SetBranchAddress("mt_goodMuon_uesUp", &mt_goodMuon_uesUp, &b_mt_goodMuon_uesUp);
   fChain->SetBranchAddress("mt_qcdElectron", &mt_qcdElectron, &b_mt_qcdElectron);
   fChain->SetBranchAddress("mt_qcdElectron_eesDn", &mt_qcdElectron_eesDn, &b_mt_qcdElectron_eesDn);
   fChain->SetBranchAddress("mt_qcdElectron_eesUp", &mt_qcdElectron_eesUp, &b_mt_qcdElectron_eesUp);
   fChain->SetBranchAddress("mt_qcdElectron_jesDn", &mt_qcdElectron_jesDn, &b_mt_qcdElectron_jesDn);
   fChain->SetBranchAddress("mt_qcdElectron_jesUp", &mt_qcdElectron_jesUp, &b_mt_qcdElectron_jesUp);
   fChain->SetBranchAddress("mt_qcdElectron_uesDn", &mt_qcdElectron_uesDn, &b_mt_qcdElectron_uesDn);
   fChain->SetBranchAddress("mt_qcdElectron_uesUp", &mt_qcdElectron_uesUp, &b_mt_qcdElectron_uesUp);
   fChain->SetBranchAddress("mt_qcdMuon", &mt_qcdMuon, &b_mt_qcdMuon);
   fChain->SetBranchAddress("mt_qcdMuon_eesDn", &mt_qcdMuon_eesDn, &b_mt_qcdMuon_eesDn);
   fChain->SetBranchAddress("mt_qcdMuon_eesUp", &mt_qcdMuon_eesUp, &b_mt_qcdMuon_eesUp);
   fChain->SetBranchAddress("mt_qcdMuon_jesDn", &mt_qcdMuon_jesDn, &b_mt_qcdMuon_jesDn);
   fChain->SetBranchAddress("mt_qcdMuon_jesUp", &mt_qcdMuon_jesUp, &b_mt_qcdMuon_jesUp);
   fChain->SetBranchAddress("mt_qcdMuon_uesDn", &mt_qcdMuon_uesDn, &b_mt_qcdMuon_uesDn);
   fChain->SetBranchAddress("mt_qcdMuon_uesUp", &mt_qcdMuon_uesUp, &b_mt_qcdMuon_uesUp);
   fChain->SetBranchAddress("LHEProduct", &LHEProduct, &b_LHEProduct);
   fChain->SetBranchAddress("nbHadrons", &nbHadrons, &b_nbHadrons);
   fChain->SetBranchAddress("nrAllEle", &nrAllEle, &b_nrAllEle);
   fChain->SetBranchAddress("nrAllJets", &nrAllJets, &b_nrAllJets);
   fChain->SetBranchAddress("nrAllMu", &nrAllMu, &b_nrAllMu);
   fChain->SetBranchAddress("nrCleanJets", &nrCleanJets, &b_nrCleanJets);
   fChain->SetBranchAddress("nrFwdJets", &nrFwdJets, &b_nrFwdJets);
   fChain->SetBranchAddress("nrGoodEle", &nrGoodEle, &b_nrGoodEle);
   fChain->SetBranchAddress("nrGoodJets", &nrGoodJets, &b_nrGoodJets);
   fChain->SetBranchAddress("nrGoodMu", &nrGoodMu, &b_nrGoodMu);
   fChain->SetBranchAddress("nrQCDEle", &nrQCDEle, &b_nrQCDEle);
   fChain->SetBranchAddress("nrQCDMu", &nrQCDMu, &b_nrQCDMu);
   fChain->SetBranchAddress("nrVetoEle", &nrVetoEle, &b_nrVetoEle);
   fChain->SetBranchAddress("nrVetoMu", &nrVetoMu, &b_nrVetoMu);
   fChain->SetBranchAddress("puBXminus", &puBXminus, &b_puBXminus);
   fChain->SetBranchAddress("puTruth", &puTruth, &b_puTruth);
   fChain->SetBranchAddress("puBX0", &puBX0, &b_puBX0);
   fChain->SetBranchAddress("puBXplus", &puBXplus, &b_puBXplus);
   fChain->SetBranchAddress("qcdEle_charge_vec", &qcdEle_charge_vec, &b_qcdEle_charge_vec);
   fChain->SetBranchAddress("qcdEle_eta_vec", &qcdEle_eta_vec, &b_qcdEle_eta_vec);
   fChain->SetBranchAddress("qcdEle_phi_vec", &qcdEle_phi_vec, &b_qcdEle_phi_vec);
   fChain->SetBranchAddress("qcdEle_pt_vec", &qcdEle_pt_vec, &b_qcdEle_pt_vec);
   fChain->SetBranchAddress("qcdMu_charge_vec", &qcdMu_charge_vec, &b_qcdMu_charge_vec);
   fChain->SetBranchAddress("qcdMu_eta_vec", &qcdMu_eta_vec, &b_qcdMu_eta_vec);
   fChain->SetBranchAddress("qcdMu_phi_vec", &qcdMu_phi_vec, &b_qcdMu_phi_vec);
   fChain->SetBranchAddress("qcdMu_pt_vec", &qcdMu_pt_vec, &b_qcdMu_pt_vec);
   fChain->SetBranchAddress("weightTop", &weightTop, &b_weightTop);
   fChain->SetBranchAddress("topPt", &topPt, &b_topPt);
   fChain->SetBranchAddress("antitopPt", &antitopPt, &b_antitopPt);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_wasRun", &HLT_IsoMu24_eta2p1_v_wasRun, &b_HLT_IsoMu24_eta2p1_v_wasRun);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_fired", &HLT_IsoMu24_eta2p1_v_fired, &b_HLT_IsoMu24_eta2p1_v_fired);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_prescale", &HLT_IsoMu24_eta2p1_v_prescale, &b_HLT_IsoMu24_eta2p1_v_prescale);
   fChain->SetBranchAddress("HLT_IsoMu24_eta2p1_v_error", &HLT_IsoMu24_eta2p1_v_error, &b_HLT_IsoMu24_eta2p1_v_error);
   fChain->SetBranchAddress("HLT_Ele27_WP80_wasRun", &HLT_Ele27_WP80_wasRun, &b_HLT_Ele27_WP80_wasRun);
   fChain->SetBranchAddress("HLT_Ele27_WP80_fired", &HLT_Ele27_WP80_fired, &b_HLT_Ele27_WP80_fired);
   fChain->SetBranchAddress("HLT_Ele27_WP80_prescale", &HLT_Ele27_WP80_prescale, &b_HLT_Ele27_WP80_prescale);
   fChain->SetBranchAddress("HLT_Ele27_WP80_error", &HLT_Ele27_WP80_error, &b_HLT_Ele27_WP80_error);
   fChain->SetBranchAddress("HLT_Any", &HLT_Any, &b_HLT_Any);
   fChain->SetBranchAddress("vertices", &vertices, &b_vertices);
   fChain->SetBranchAddress("vetoEle_charge_vec", &vetoEle_charge_vec, &b_vetoEle_charge_vec);
   fChain->SetBranchAddress("vetoEle_eta_vec", &vetoEle_eta_vec, &b_vetoEle_eta_vec);
   fChain->SetBranchAddress("vetoEle_phi_vec", &vetoEle_phi_vec, &b_vetoEle_phi_vec);
   fChain->SetBranchAddress("vetoEle_pt_vec", &vetoEle_pt_vec, &b_vetoEle_pt_vec);
   fChain->SetBranchAddress("vetoMu_charge_vec", &vetoMu_charge_vec, &b_vetoMu_charge_vec);
   fChain->SetBranchAddress("vetoMu_eta_vec", &vetoMu_eta_vec, &b_vetoMu_eta_vec);
   fChain->SetBranchAddress("vetoMu_phi_vec", &vetoMu_phi_vec, &b_vetoMu_phi_vec);
   fChain->SetBranchAddress("vetoMu_pt_vec", &vetoMu_pt_vec, &b_vetoMu_pt_vec);
   Notify();
}

Bool_t findMTresolution::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF. It is normally not necessary to make changes
   // to the generated code, but the routine can be extended by the
   // user if needed. The return value is currently not used.

   return kTRUE;
}

void findMTresolution::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}
#endif // #ifdef findMTresolution_cxx
