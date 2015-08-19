#ifndef histoFillerTTbarProgression_h
#define histoFillerTTbarProgression_h

#include <TROOT.h>
#include <TChain.h>
#include <TFile.h>
#include <TH2.h>
#include <iostream>
#include <exception>
#include <cmath>
#include <TLorentzVector.h>

// classes stored in the TTree
#include <vector>

class histoFillerTTbarProgression {
public :
   TTree          *fChain;   //!pointer to the analyzed TTree or TChain
   Int_t           fCurrent; //!current Tree number in a TChain

   // Histograms
   std::vector<TString> PSpace;  // 14 ttme0b, ttme1bta, ttme1btb, ttme2bt, ttme1bma, ttme1bmb, ttme2bm, ttme0bJv, ttme1btaJv, ttme1btbJv, ttme2btJv, ttme1bmaJv, ttme1bmbJv, ttme2bmJv,

   std::vector<TString> EMu;     // 2
   std::vector<TString> QCD;     // 1
   std::vector<TString> Syst;    // 1
   std::vector<TString> WFlav;   // 5
   TH1F hists_met[14][2][1][1][5];
   TH1F hists_met_phi[14][2][1][1][5];
   TH1F hists_mt[14][2][1][1][5];
   TH1F hists_goodLep_pt[14][2][1][1][5];
   TH1F hists_goodJ1_pt[14][2][1][1][5];
   TH1F hists_goodJ2_pt[14][2][1][1][5];
   TH1F hists_goodJ1J2_dR[14][2][1][1][5];
   TH1F hists_goodJ1J2_mass[14][2][1][1][5];
   TH1F hists_goodJ1J2_pt[14][2][1][1][5];
   TH1F hists_goodJ1_CSV[14][2][1][1][5];
   TH1F hists_goodJ1_mass_SV_unweighted[14][2][1][1][5];
   TH1F hists_goodJ1_mass_SV_corrected[14][2][1][1][5];
   TH1F hists_goodJ1_mass_SV_weighted[14][2][1][1][5];
   TH1F hists_goodJ2_CSV[14][2][1][1][5]; 
   TH1F hists_goodJ3J4_mass[14][2][1][1][5]; 
   TH1F hists_vertices[14][2][1][1][5]; 

   Int_t nbrGoodMu ;
   Int_t nbrVetoMu ;
   Int_t nbrQCDMu ;
   Int_t nbrGoodEle ;
   Int_t nbrVetoEle ;
   Int_t nbrQCDEle ;

   // For Cuts
   Bool_t twoGoodLMuE;
   Bool_t twoGoodLEMu;
   Bool_t twoQCDLMuE;
   Bool_t twoQCDLEMu;

   Bool_t min2goodJs;
   Bool_t vetoJ3;
   Bool_t btag0J;
   Bool_t btag1Jta;
   Bool_t btag1Jtb;
   Bool_t btag2Jt;
   Bool_t btag1Jma;
   Bool_t btag1Jmb;
   Bool_t btag2Jm;

   // W splitting
   Bool_t twoCs;
   Bool_t someCs;
   Bool_t someBs;
   Bool_t isWl;
   Bool_t isWc;
   Bool_t isWcc;
   Bool_t isWbb;

   // btag scale factors
   Float_t SF_1bta;
   Float_t SF_1btb;
   Float_t SF_2bt;
   Float_t SF_1bma;
   Float_t SF_1bmb;
   Float_t SF_2bm;

   // histogram variables
   Float_t mt_ele_qcd;
   Float_t mt_ele_qcd_uesUp;
   Float_t mt_ele_qcd_uesDown;
   Float_t lep_ele_qcd_pt;
   Float_t lep_ele_qcd_eta;
   Float_t lep_ele_qcd_phi;
   Float_t mt_mu_good;
   Float_t mt_mu_good_uesUp;
   Float_t mt_mu_good_uesDown;
   Float_t lep_mu_good_pt;
   Float_t lep_mu_good_eta;
   Float_t lep_mu_good_phi;
   Float_t mt_mu_qcd;
   Float_t mt_mu_qcd_uesUp;
   Float_t mt_mu_qcd_uesDown;
   Float_t lep_mu_qcd_pt;
   Float_t lep_mu_qcd_eta;
   Float_t lep_mu_qcd_phi;
   Float_t mt_ele_good;
   Float_t mt_ele_good_uesUp;
   Float_t mt_ele_good_uesDown;
   Float_t lep_ele_good_pt;
   Float_t lep_ele_good_eta;
   Float_t lep_ele_good_phi;
   Float_t MET_pt;
   Float_t MET_phi;
   Float_t MET_pt_uesUp;
   Float_t MET_pt_uesDown;
   Float_t MET_phi_uesUp;
   Float_t MET_phi_uesDown;
   
   // DiJets
   TLorentzVector fourVec_J1;
   TLorentzVector fourVec_J2;
   TLorentzVector fourVec_J1J2;
   TLorentzVector fourVec_J3;
   TLorentzVector fourVec_J4;
   TLorentzVector fourVec_J3J4;
   double goodJ1J2_pt;
   double goodJ1J2_eta;
   double goodJ1J2_phi;
   double goodJ1J2_mass;
   double goodJ3J4_pt;
   double goodJ3J4_eta;
   double goodJ3J4_phi;
   double goodJ3J4_mass;
   Float_t goodJ1J2_dR;
   Float_t dphiJJ;
   Float_t detaJJ;
   Float_t dphiJ1Met;

   // Id/Iso/HLT (EMu) Scale Factors
   Float_t SF_ttme_mu_good_IDIsoHLT  ; 
   Float_t SF_ttme_ele_good_IDIsoHLT ; 

   // Weights
   Float_t weight_ttme0b_mu_good   ;
   Float_t weight_ttme1bta_mu_good ;
   Float_t weight_ttme1btb_mu_good ;
   Float_t weight_ttme2bt_mu_good  ;
   Float_t weight_ttme1bma_mu_good ;
   Float_t weight_ttme1bmb_mu_good ;
   Float_t weight_ttme2bm_mu_good  ;

   Float_t weight_ttme0b_ele_good  ;
   Float_t weight_ttme1bta_ele_good;
   Float_t weight_ttme1btb_ele_good;
   Float_t weight_ttme2bt_ele_good ;
   Float_t weight_ttme1bma_ele_good;
   Float_t weight_ttme1bmb_ele_good;
   Float_t weight_ttme2bm_ele_good ;

   // Declaration of leaf types
   UInt_t          EVENT;
   UInt_t          RUN;
   UInt_t          LUMI;
   Float_t         GBWeight;
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
   vector<double>  *bHadronsPhi;
   vector<double>  *bHadronsPt;
   Float_t         fwdJ1_CSV;
   Float_t         fwdJ1_CSVreweight;
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
   Float_t         fwdJ2_CSV;
   Float_t         fwdJ2_CSVreweight;
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
   Int_t           genBs;
   Int_t           genCs;
   Int_t           genDs;
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
   Float_t         goodJ2_CSV;
   Float_t         goodJ2_CSVreweight;
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
   Float_t         goodJ3_CSV;
   Float_t         goodJ3_CSVreweight;
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
   Float_t         goodJ4_CSV;
   Float_t         goodJ4_CSVreweight;
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
   TBranch        *b_bHadronsPhi;   //!
   TBranch        *b_bHadronsPt;   //!
   TBranch        *b_fwdJ1_CSV;   //!
   TBranch        *b_fwdJ1_CSVreweight;   //!
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
   TBranch        *b_fwdJ2_CSV;   //!
   TBranch        *b_fwdJ2_CSVreweight;   //!
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
   TBranch        *b_genBs;   //!
   TBranch        *b_genCs;   //!
   TBranch        *b_genDs;   //!
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
   TBranch        *b_goodJ2_CSV;   //!
   TBranch        *b_goodJ2_CSVreweight;   //!
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
   TBranch        *b_goodJ3_CSV;   //!
   TBranch        *b_goodJ3_CSVreweight;   //!
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
   TBranch        *b_goodJ4_CSV;   //!
   TBranch        *b_goodJ4_CSVreweight;   //!
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

   histoFillerTTbarProgression(TTree *tree=0, Bool_t isMC=kTRUE);
   virtual ~histoFillerTTbarProgression();
   virtual Int_t    GetEntry(Long64_t entry);
   virtual Long64_t LoadTree(Long64_t entry);
   virtual void     Init(TTree *tree, Bool_t isMC);
   virtual void     Loop(
                     TString outfileName, TString shift, 
                     Bool_t isMC, Bool_t isW,
                     UInt_t lumi_mu, UInt_t lumi_ele, 
                     UInt_t nrEvents, Float_t crossSec
                    );
   virtual Bool_t   Notify();
   virtual double   dPhi(double phi1, double phi2);
   virtual double   dEta(double eta1, double eta2);
   virtual Bool_t   FillHistograms(int i, int j, int k, int l, int m,
                     double metval, double metphival,
                     double mt, double lep_pt, double weight );
   virtual Bool_t   WriteHistograms(int i, int j, int k, int l, int m);
   virtual Bool_t   DeleteHistograms(int i, int j, int k, int l, int m);
   virtual Bool_t   writeHistWriter( int pspace_nr=3, int syst_nr=0, Bool_t isW=kFALSE );
   virtual Bool_t   fillHistWriter(
                     Bool_t pass_mu_good=kFALSE, Bool_t pass_mu_qcd=kFALSE, Bool_t pass_ele_good=kFALSE, Bool_t pass_ele_qcd=kFALSE,
                     int pspace_nr=3, int syst_nr=0,
                     Float_t met_pt_val=0., Float_t met_phi_val=0.,
                     Float_t mt_mu_good_val=0., Float_t mt_mu_qcd_val=0., Float_t mt_ele_good_val=0., Float_t mt_ele_qcd_val=0.,
                     // weights
                     Float_t weight_mu_good_val=1., Float_t weight_mu_qcd_val=1., Float_t weight_ele_good_val=1., Float_t weight_ele_qcd_val=1.
                    );
   virtual void     Show(Long64_t entry = -1);
};

#endif

#ifdef histoFillerTTbarProgression_cxx
histoFillerTTbarProgression::histoFillerTTbarProgression(TTree *tree, Bool_t isMC) : fChain(0) 
{
//// if parameter tree is not specified (or zero), connect the file
//// used to generate this class and read the Tree.
//   if (tree == 0) {
//      TFile *f = (TFile*)gROOT->GetListOfFiles()->FindObject("/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root");
//      if (!f || !f->IsOpen()) {
//         f = new TFile("/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root");
//      }
//      TDirectory * dir = (TDirectory*)f->Get("/hdfs/store/user/tperry/Schweincomp/Schweincomp_Wbb4F-MuEle-PATMCs/MuEle-PATMCs-patTuple_cfg-0003D872-C40E-E211-8C51-003048673FE6.root:/muEleEventTree");
//      dir->GetObject("eventTree",tree);
//   }
//   Init(tree, isMC);
}

histoFillerTTbarProgression::~histoFillerTTbarProgression()
{
   if (!fChain) return;
   delete fChain->GetCurrentFile();
   //  std::cout<<"We're actually deleting"<<std::endl;
}

Int_t histoFillerTTbarProgression::GetEntry(Long64_t entry)
{
// Read contents of entry.
   if (!fChain) return 0;
   return fChain->GetEntry(entry);
}
Long64_t histoFillerTTbarProgression::LoadTree(Long64_t entry)
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

void histoFillerTTbarProgression::Init(TTree *tree, Bool_t isMC)
{
   PSpace.clear();
   EMu.clear();
   QCD.clear();
   Syst.clear();
   WFlav.clear();

   PSpace.push_back("ttme0b");
   PSpace.push_back("ttme1bta");
   PSpace.push_back("ttme1btb");
   PSpace.push_back("ttme2bt");
   PSpace.push_back("ttme1bma");
   PSpace.push_back("ttme1bmb");
   PSpace.push_back("ttme2bm");
   PSpace.push_back("ttme0bJv");
   PSpace.push_back("ttme1btaJv");
   PSpace.push_back("ttme1btbJv");
   PSpace.push_back("ttme2btJv");
   PSpace.push_back("ttme1bmaJv");
   PSpace.push_back("ttme1bmbJv");
   PSpace.push_back("ttme2bmJv");
   EMu.push_back("mu");
   EMu.push_back("ele");
   QCD.push_back("good");
   Syst.push_back("");
   //Syst.push_back("_SFs");
   //Syst.push_back("_CSVUp");
   //Syst.push_back("_CSVDown");
   //Syst.push_back("_EMuUp");
   //Syst.push_back("_EMuDown");
   //Syst.push_back("_UESUp");
   //Syst.push_back("_UESDown");
   WFlav.push_back("");
   WFlav.push_back("_Wl");
   WFlav.push_back("_Wc");
   WFlav.push_back("_Wcc");
   WFlav.push_back("_Wbb");

   for(unsigned int i=0; i<PSpace.size(); ++i){
    for(unsigned int j=0; j<EMu.size(); ++j){
      //unsigned int j=0; unsigned int k=0; unsigned int l=0; unsigned int m=0;
     for(unsigned int k=0; k<QCD.size(); ++k){
      for(unsigned int l=0; l<Syst.size(); ++l){
       for(unsigned int m=0; m<WFlav.size(); ++m){

        TString histoname_met = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_met"+Syst[l]+WFlav[m];
        TString histoname_met_phi = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_met_phi"+Syst[l]+WFlav[m];
        TString histoname_mt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_mt"+Syst[l]+WFlav[m];
        TString histoname_goodLep_pt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodLep_pt"+Syst[l]+WFlav[m];
        TString histoname_goodMu_pt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodMu_pt"+Syst[l]+WFlav[m];
        TString histoname_goodEle_pt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodEle_pt"+Syst[l]+WFlav[m];
        TString histoname_goodJ1_pt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1_pt"+Syst[l]+WFlav[m];
        TString histoname_goodJ2_pt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ2_pt"+Syst[l]+WFlav[m];
        TString histoname_goodJ1J2_dR = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1J2_dR"+Syst[l]+WFlav[m];
        TString histoname_goodJ1J2_mass = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1J2_mass"+Syst[l]+WFlav[m];
        TString histoname_goodJ1J2_pt = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1J2_pt"+Syst[l]+WFlav[m];
        TString histoname_goodJ3J4_mass = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ3J4_mass"+Syst[l]+WFlav[m];
        TString histoname_goodJ1_CSV = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1_CSV"+Syst[l]+WFlav[m];
        TString histoname_goodJ2_CSV = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ2_CSV"+Syst[l]+WFlav[m];
        TString histoname_goodJ1_mass_SV_unweighted = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1_mass_SV_unweighted"+Syst[l]+WFlav[m];
        TString histoname_goodJ1_mass_SV_corrected = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1_mass_SV_corrected"+Syst[l]+WFlav[m];
        TString histoname_goodJ1_mass_SV_weighted = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_goodJ1_mass_SV_weighted"+Syst[l]+WFlav[m];
        TString histoname_vertices = "h_"+PSpace[i]+"_"+EMu[j]+"_"+QCD[k]+"_vertices"+Syst[l]+WFlav[m];

        //std::cout<<histoname<<std::endl;
        hists_met[i][j][k][l][m].Clear();
        hists_met[i][j][k][l][m] = TH1F(histoname_met, "MET", 40, 0., 200.);
        hists_met[i][j][k][l][m].Sumw2();                                               

        hists_met_phi[i][j][k][l][m].Clear();
        hists_met_phi[i][j][k][l][m] = TH1F(histoname_met_phi, "MET Phi", 35, -3.4033, 5.7594);
        hists_met_phi[i][j][k][l][m].Sumw2();                                               

        hists_mt[i][j][k][l][m].Clear();
        hists_mt[i][j][k][l][m] = TH1F(histoname_mt, "Transverse Mass", 40, 0., 200.);
        hists_mt[i][j][k][l][m].Sumw2();                                               

        hists_goodLep_pt[i][j][k][l][m].Clear();
        hists_goodLep_pt[i][j][k][l][m] = TH1F(histoname_goodLep_pt, "Leading Lepton pT", 40, 0., 200.);
        hists_goodLep_pt[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1_pt[i][j][k][l][m].Clear();
        hists_goodJ1_pt[i][j][k][l][m] = TH1F(histoname_goodJ1_pt, "Leading Jet pT", 12, 25., 205.);
        hists_goodJ1_pt[i][j][k][l][m].Sumw2();                                               

        hists_goodJ2_pt[i][j][k][l][m].Clear();
        hists_goodJ2_pt[i][j][k][l][m] = TH1F(histoname_goodJ2_pt, "Subleading Jet pT", 12, 25., 205.);
        hists_goodJ2_pt[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1J2_dR[i][j][k][l][m].Clear();
        hists_goodJ1J2_dR[i][j][k][l][m] = TH1F(histoname_goodJ1J2_dR, "dR(J1,J2)", 16, 0., 8.);
        hists_goodJ1J2_dR[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1J2_mass[i][j][k][l][m].Clear();
        hists_goodJ1J2_mass[i][j][k][l][m] = TH1F(histoname_goodJ1J2_mass, "mass(J1,J2)", 40, 0., 200.);
        hists_goodJ1J2_mass[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1J2_pt[i][j][k][l][m].Clear();
        hists_goodJ1J2_pt[i][j][k][l][m] = TH1F(histoname_goodJ1J2_pt, "pt(J1,J2)", 40, 0., 200.);
        hists_goodJ1J2_pt[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1_CSV[i][j][k][l][m].Clear();
        hists_goodJ1_CSV[i][j][k][l][m] = TH1F(histoname_goodJ1_CSV, "Leading Jet CSV", 40, 0., 1.);
        hists_goodJ1_CSV[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1_mass_SV_unweighted[i][j][k][l][m].Clear();
        hists_goodJ1_mass_SV_unweighted[i][j][k][l][m] = TH1F(histoname_goodJ1_mass_SV_unweighted, "Leading Jet mass_SV_unweighted", 32, 0., 8.);
        hists_goodJ1_mass_SV_unweighted[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1_mass_SV_corrected[i][j][k][l][m].Clear();
        hists_goodJ1_mass_SV_corrected[i][j][k][l][m] = TH1F(histoname_goodJ1_mass_SV_corrected, "Leading Jet mass_SV_corrected", 32, 0., 8.);
        hists_goodJ1_mass_SV_corrected[i][j][k][l][m].Sumw2();                                               

        hists_goodJ1_mass_SV_weighted[i][j][k][l][m].Clear();
        hists_goodJ1_mass_SV_weighted[i][j][k][l][m] = TH1F(histoname_goodJ1_mass_SV_weighted, "Leading Jet mass_SV_weighted", 32, 0., 8.);
        hists_goodJ1_mass_SV_weighted[i][j][k][l][m].Sumw2();                                               

        hists_goodJ2_CSV[i][j][k][l][m].Clear();
        hists_goodJ2_CSV[i][j][k][l][m] = TH1F(histoname_goodJ2_CSV, "SubLeading Jet CSV", 40, 0., 1.);
        hists_goodJ2_CSV[i][j][k][l][m].Sumw2();                                               

        hists_goodJ3J4_mass[i][j][k][l][m].Clear();
        hists_goodJ3J4_mass[i][j][k][l][m] = TH1F(histoname_goodJ3J4_mass, "mass(J3,J4)", 40, 0., 200.);
        hists_goodJ3J4_mass[i][j][k][l][m].Sumw2();                                               

        hists_vertices[i][j][k][l][m].Clear();
        hists_vertices[i][j][k][l][m] = TH1F(histoname_vertices, "Nr. Vertices", 60, 0., 60.);
        hists_vertices[i][j][k][l][m].Sumw2();                                               
        
       }
      }
     }
    }
   }

   // Set object pointer
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
   bHadronsPhi = 0; 
   bHadronsPt = 0; 
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
   qcdEle_charge_vec = 0; ////
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
   if( isMC ) {
    fChain->SetBranchAddress("GBWeight", &GBWeight, &b_GBWeight);
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
    fChain->SetBranchAddress("bHadronsEta", &bHadronsEta, &b_bHadronsEta);
    fChain->SetBranchAddress("bHadronsPhi", &bHadronsPhi, &b_bHadronsPhi);
    fChain->SetBranchAddress("bHadronsPt", &bHadronsPt, &b_bHadronsPt);
    fChain->SetBranchAddress("genBs", &genBs, &b_genBs);
    fChain->SetBranchAddress("genCs", &genCs, &b_genCs);
    fChain->SetBranchAddress("genDs", &genDs, &b_genDs);
    fChain->SetBranchAddress("genSs", &genSs, &b_genSs);
    fChain->SetBranchAddress("genTbars", &genTbars, &b_genTbars);
    fChain->SetBranchAddress("genTs", &genTs, &b_genTs);
    fChain->SetBranchAddress("genUs", &genUs, &b_genUs);
    fChain->SetBranchAddress("genWs", &genWs, &b_genWs);
    fChain->SetBranchAddress("met_eesDn_phi", &met_eesDn_phi, &b_met_eesDn_phi);
    fChain->SetBranchAddress("met_eesDn_pt", &met_eesDn_pt, &b_met_eesDn_pt);
    fChain->SetBranchAddress("met_eesUp_phi", &met_eesUp_phi, &b_met_eesUp_phi);
    fChain->SetBranchAddress("met_eesUp_pt", &met_eesUp_pt, &b_met_eesUp_pt);
    fChain->SetBranchAddress("met_jesDn_phi", &met_jesDn_phi, &b_met_jesDn_phi);
    fChain->SetBranchAddress("met_jesDn_pt", &met_jesDn_pt, &b_met_jesDn_pt);
    fChain->SetBranchAddress("met_jesUp_phi", &met_jesUp_phi, &b_met_jesUp_phi);
    fChain->SetBranchAddress("met_jesUp_pt", &met_jesUp_pt, &b_met_jesUp_pt);
    fChain->SetBranchAddress("met_uesDn_phi", &met_uesDn_phi, &b_met_uesDn_phi);
    fChain->SetBranchAddress("met_uesDn_pt", &met_uesDn_pt, &b_met_uesDn_pt);
    fChain->SetBranchAddress("met_uesUp_phi", &met_uesUp_phi, &b_met_uesUp_phi);
    fChain->SetBranchAddress("met_uesUp_pt", &met_uesUp_pt, &b_met_uesUp_pt);
    fChain->SetBranchAddress("mt_goodElectron_eesDn", &mt_goodElectron_eesDn, &b_mt_goodElectron_eesDn);
    fChain->SetBranchAddress("mt_goodElectron_eesUp", &mt_goodElectron_eesUp, &b_mt_goodElectron_eesUp);
    fChain->SetBranchAddress("mt_goodElectron_jesDn", &mt_goodElectron_jesDn, &b_mt_goodElectron_jesDn);
    fChain->SetBranchAddress("mt_goodElectron_jesUp", &mt_goodElectron_jesUp, &b_mt_goodElectron_jesUp);
    fChain->SetBranchAddress("mt_goodElectron_uesDn", &mt_goodElectron_uesDn, &b_mt_goodElectron_uesDn);
    fChain->SetBranchAddress("mt_goodElectron_uesUp", &mt_goodElectron_uesUp, &b_mt_goodElectron_uesUp);
    fChain->SetBranchAddress("mt_goodMuon_eesDn", &mt_goodMuon_eesDn, &b_mt_goodMuon_eesDn);
    fChain->SetBranchAddress("mt_goodMuon_eesUp", &mt_goodMuon_eesUp, &b_mt_goodMuon_eesUp);
    fChain->SetBranchAddress("mt_goodMuon_jesDn", &mt_goodMuon_jesDn, &b_mt_goodMuon_jesDn);
    fChain->SetBranchAddress("mt_goodMuon_jesUp", &mt_goodMuon_jesUp, &b_mt_goodMuon_jesUp);
    fChain->SetBranchAddress("mt_goodMuon_uesDn", &mt_goodMuon_uesDn, &b_mt_goodMuon_uesDn);
    fChain->SetBranchAddress("mt_goodMuon_uesUp", &mt_goodMuon_uesUp, &b_mt_goodMuon_uesUp);
    fChain->SetBranchAddress("mt_qcdElectron_eesDn", &mt_qcdElectron_eesDn, &b_mt_qcdElectron_eesDn);
    fChain->SetBranchAddress("mt_qcdElectron_eesUp", &mt_qcdElectron_eesUp, &b_mt_qcdElectron_eesUp);
    fChain->SetBranchAddress("mt_qcdElectron_jesDn", &mt_qcdElectron_jesDn, &b_mt_qcdElectron_jesDn);
    fChain->SetBranchAddress("mt_qcdElectron_jesUp", &mt_qcdElectron_jesUp, &b_mt_qcdElectron_jesUp);
    fChain->SetBranchAddress("mt_qcdElectron_uesDn", &mt_qcdElectron_uesDn, &b_mt_qcdElectron_uesDn);
    fChain->SetBranchAddress("mt_qcdElectron_uesUp", &mt_qcdElectron_uesUp, &b_mt_qcdElectron_uesUp);
    fChain->SetBranchAddress("mt_qcdMuon_eesDn", &mt_qcdMuon_eesDn, &b_mt_qcdMuon_eesDn);
    fChain->SetBranchAddress("mt_qcdMuon_eesUp", &mt_qcdMuon_eesUp, &b_mt_qcdMuon_eesUp);
    fChain->SetBranchAddress("mt_qcdMuon_jesDn", &mt_qcdMuon_jesDn, &b_mt_qcdMuon_jesDn);
    fChain->SetBranchAddress("mt_qcdMuon_jesUp", &mt_qcdMuon_jesUp, &b_mt_qcdMuon_jesUp);
    fChain->SetBranchAddress("mt_qcdMuon_uesDn", &mt_qcdMuon_uesDn, &b_mt_qcdMuon_uesDn);
    fChain->SetBranchAddress("mt_qcdMuon_uesUp", &mt_qcdMuon_uesUp, &b_mt_qcdMuon_uesUp);
    fChain->SetBranchAddress("LHEProduct", &LHEProduct, &b_LHEProduct);
    fChain->SetBranchAddress("nbHadrons", &nbHadrons, &b_nbHadrons);
    fChain->SetBranchAddress("weightTop", &weightTop, &b_weightTop);
    fChain->SetBranchAddress("topPt", &topPt, &b_topPt);
    fChain->SetBranchAddress("antitopPt", &antitopPt, &b_antitopPt);
   }
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
   fChain->SetBranchAddress("fwdJ1_CSV", &fwdJ1_CSV, &b_fwdJ1_CSV);
   fChain->SetBranchAddress("fwdJ1_CSVreweight", &fwdJ1_CSVreweight, &b_fwdJ1_CSVreweight);
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
   fChain->SetBranchAddress("fwdJ2_CSV", &fwdJ2_CSV, &b_fwdJ2_CSV);
   fChain->SetBranchAddress("fwdJ2_CSVreweight", &fwdJ2_CSVreweight, &b_fwdJ2_CSVreweight);
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
   fChain->SetBranchAddress("goodEle_Iso03_vec", &goodEle_Iso03_vec, &b_goodEle_Iso03_vec);
   fChain->SetBranchAddress("goodEle_Iso04_vec", &goodEle_Iso04_vec, &b_goodEle_Iso04_vec);
   fChain->SetBranchAddress("goodEle_charge_vec", &goodEle_charge_vec, &b_goodEle_charge_vec);
   fChain->SetBranchAddress("goodEle_eta_vec", &goodEle_eta_vec, &b_goodEle_eta_vec);
   fChain->SetBranchAddress("goodEle_mass_vec", &goodEle_mass_vec, &b_goodEle_mass_vec);
   fChain->SetBranchAddress("goodEle_phi_vec", &goodEle_phi_vec, &b_goodEle_phi_vec);
   fChain->SetBranchAddress("goodEle_pt_vec", &goodEle_pt_vec, &b_goodEle_pt_vec);
   fChain->SetBranchAddress("goodJ1_CSV", &goodJ1_CSV, &b_goodJ1_CSV);
   fChain->SetBranchAddress("goodJ1_CSVreweight", &goodJ1_CSVreweight, &b_goodJ1_CSVreweight);
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
   fChain->SetBranchAddress("goodJ2_CSV", &goodJ2_CSV, &b_goodJ2_CSV);
   fChain->SetBranchAddress("goodJ2_CSVreweight", &goodJ2_CSVreweight, &b_goodJ2_CSVreweight);
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
   fChain->SetBranchAddress("goodJ3_CSV", &goodJ3_CSV, &b_goodJ3_CSV);
   fChain->SetBranchAddress("goodJ3_CSVreweight", &goodJ3_CSVreweight, &b_goodJ3_CSVreweight);
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
   fChain->SetBranchAddress("goodJ4_CSV", &goodJ4_CSV, &b_goodJ4_CSV);
   fChain->SetBranchAddress("goodJ4_CSVreweight", &goodJ4_CSVreweight, &b_goodJ4_CSVreweight);
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
   fChain->SetBranchAddress("goodMu_charge_vec", &goodMu_charge_vec, &b_goodMu_charge_vec);
   fChain->SetBranchAddress("goodMu_eta_vec", &goodMu_eta_vec, &b_goodMu_eta_vec);
   fChain->SetBranchAddress("goodMu_mass_vec", &goodMu_mass_vec, &b_goodMu_mass_vec);
   fChain->SetBranchAddress("goodMu_phi_vec", &goodMu_phi_vec, &b_goodMu_phi_vec);
   fChain->SetBranchAddress("goodMu_pt_vec", &goodMu_pt_vec, &b_goodMu_pt_vec);
   fChain->SetBranchAddress("met_phi", &met_phi, &b_met_phi);
   fChain->SetBranchAddress("met_pt", &met_pt, &b_met_pt);
   fChain->SetBranchAddress("mt_goodElectron", &mt_goodElectron, &b_mt_goodElectron);
   fChain->SetBranchAddress("mt_goodMuon", &mt_goodMuon, &b_mt_goodMuon);
   fChain->SetBranchAddress("mt_qcdElectron", &mt_qcdElectron, &b_mt_qcdElectron);
   fChain->SetBranchAddress("mt_qcdMuon", &mt_qcdMuon, &b_mt_qcdMuon);
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

Bool_t histoFillerTTbarProgression::Notify()
{
   // The Notify() function is called when a new file is opened. This
   // can be either for a new TTree in a TChain or when when a new TTree
   // is started when using PROOF.
   return kTRUE;
}

void histoFillerTTbarProgression::Show(Long64_t entry)
{
// Print contents of entry.
// If entry is not specified, print current entry
   if (!fChain) return;
   fChain->Show(entry);
}

double histoFillerTTbarProgression::dPhi(double phi1, double phi2){
 double dphi;
 dphi = std::abs(phi1-phi2);
 if (dphi > 3.14159 ){ dphi = 6.2832 - dphi; }
 return dphi;
}

double histoFillerTTbarProgression::dEta(double eta1, double eta2){
 double deta;
 deta = std::abs(eta1-eta2);
 return deta;
}

Bool_t histoFillerTTbarProgression::FillHistograms(int i, int j, int k, int l, int m, double metval, double metphival, double mt, double lep_pt, double weight){
 hists_met[i][j][k][l][m].Fill(metval,weight);
 hists_met_phi[i][j][k][l][m].Fill(metphival,weight);
 hists_mt[i][j][k][l][m].Fill(mt,weight);
 hists_goodLep_pt[i][j][k][l][m].Fill(lep_pt,weight);
 hists_goodJ1_pt[i][j][k][l][m].Fill(goodJ1_pt,weight);
 hists_goodJ2_pt[i][j][k][l][m].Fill(goodJ2_pt,weight);
 hists_goodJ1J2_dR[i][j][k][l][m].Fill(goodJ1J2_dR,weight);
 hists_goodJ1J2_mass[i][j][k][l][m].Fill(goodJ1J2_mass,weight);
 hists_goodJ1J2_pt[i][j][k][l][m].Fill(goodJ1J2_pt,weight);
 hists_goodJ1_CSV[i][j][k][l][m].Fill(goodJ1_CSV,weight);
 hists_goodJ1_mass_SV_unweighted[i][j][k][l][m].Fill(goodJ1_mass_SV_unweighted,weight);
 hists_goodJ1_mass_SV_corrected[i][j][k][l][m].Fill(goodJ1_mass_SV_corrected,weight);
 hists_goodJ1_mass_SV_weighted[i][j][k][l][m].Fill(goodJ1_mass_SV_weighted,weight);
 hists_goodJ2_CSV[i][j][k][l][m].Fill(goodJ2_CSV,weight);
 hists_goodJ3J4_mass[i][j][k][l][m].Fill(goodJ3J4_mass,weight);
 hists_vertices[i][j][k][l][m].Fill(vertices,weight);
 return kTRUE;
}
Bool_t histoFillerTTbarProgression::WriteHistograms(int i, int j, int k, int l, int m){
 hists_met[i][j][k][l][m].Write();
 hists_met_phi[i][j][k][l][m].Write();
 hists_mt[i][j][k][l][m].Write();
 hists_goodLep_pt[i][j][k][l][m].Write();
 hists_goodJ1_pt[i][j][k][l][m].Write();
 hists_goodJ2_pt[i][j][k][l][m].Write();
 hists_goodJ1J2_dR[i][j][k][l][m].Write();
 hists_goodJ1J2_mass[i][j][k][l][m].Write();
 hists_goodJ1J2_pt[i][j][k][l][m].Write();
 hists_goodJ1_CSV[i][j][k][l][m].Write();
 hists_goodJ1_mass_SV_unweighted[i][j][k][l][m].Write();
 hists_goodJ1_mass_SV_corrected[i][j][k][l][m].Write();
 hists_goodJ1_mass_SV_weighted[i][j][k][l][m].Write();
 hists_goodJ2_CSV[i][j][k][l][m].Write();
 hists_goodJ3J4_mass[i][j][k][l][m].Write();
 hists_vertices[i][j][k][l][m].Write();
 return kTRUE;
}
Bool_t histoFillerTTbarProgression::DeleteHistograms(int i, int j, int k, int l, int m){
 hists_met[i][j][k][l][m].Delete();
 hists_met_phi[i][j][k][l][m].Delete();
 hists_mt[i][j][k][l][m].Delete();
 hists_goodLep_pt[i][j][k][l][m].Delete();
 hists_goodJ1_pt[i][j][k][l][m].Delete();
 hists_goodJ2_pt[i][j][k][l][m].Delete();
 hists_goodJ1J2_dR[i][j][k][l][m].Delete();
 hists_goodJ1J2_mass[i][j][k][l][m].Delete();
 hists_goodJ1J2_pt[i][j][k][l][m].Delete();
 hists_goodJ1_CSV[i][j][k][l][m].Delete();
 hists_goodJ1_mass_SV_unweighted[i][j][k][l][m].Delete();
 hists_goodJ1_mass_SV_corrected[i][j][k][l][m].Delete();
 hists_goodJ1_mass_SV_weighted[i][j][k][l][m].Delete();
 hists_goodJ2_CSV[i][j][k][l][m].Delete();
 hists_goodJ3J4_mass[i][j][k][l][m].Delete();
 hists_vertices[i][j][k][l][m].Delete();
 return kTRUE;
}

Bool_t histoFillerTTbarProgression::fillHistWriter(
  Bool_t pass_mu_good, Bool_t pass_mu_qcd, Bool_t pass_ele_good, Bool_t pass_ele_qcd,
  int pspace_nr, int syst_nr,
  // variables
  Float_t met_pt_val, Float_t met_phi_val,
  Float_t mt_mu_good_val, Float_t mt_mu_qcd_val, Float_t mt_ele_good_val, Float_t mt_ele_qcd_val,
  // weights
  Float_t weight_mu_good_val, Float_t weight_mu_qcd_val, Float_t weight_ele_good_val, Float_t weight_ele_qcd_val
)
{
 if( pass_mu_good )          { //std::cout<<"filling passed mu good for pspace "<<pspace_nr<<syst_nr<<std::endl;
  FillHistograms(pspace_nr,0,0,syst_nr,0,met_pt_val,met_phi_val,mt_mu_good_val,lep_mu_good_pt,weight_mu_good_val); } 
 if( pass_mu_good && isWl )  {
  FillHistograms(pspace_nr,0,0,syst_nr,1,met_pt_val,met_phi_val,mt_mu_good_val,lep_mu_good_pt,weight_mu_good_val); } 
 if( pass_mu_good && isWc )  {
  FillHistograms(pspace_nr,0,0,syst_nr,2,met_pt_val,met_phi_val,mt_mu_good_val,lep_mu_good_pt,weight_mu_good_val); } 
 if( pass_mu_good && isWcc ) {
  FillHistograms(pspace_nr,0,0,syst_nr,3,met_pt_val,met_phi_val,mt_mu_good_val,lep_mu_good_pt,weight_mu_good_val); } 
 if( pass_mu_good && isWbb ) {
  FillHistograms(pspace_nr,0,0,syst_nr,4,met_pt_val,met_phi_val,mt_mu_good_val,lep_mu_good_pt,weight_mu_good_val); } 
 if( pass_mu_qcd )           {
  FillHistograms(pspace_nr,0,1,syst_nr,0,met_pt_val,met_phi_val,mt_mu_qcd_val,lep_mu_qcd_pt,weight_mu_qcd_val); } 
 if( pass_mu_qcd && isWl )   {
  FillHistograms(pspace_nr,0,1,syst_nr,1,met_pt_val,met_phi_val,mt_mu_qcd_val,lep_mu_qcd_pt,weight_mu_qcd_val); } 
 if( pass_mu_qcd && isWc )   {
  FillHistograms(pspace_nr,0,1,syst_nr,2,met_pt_val,met_phi_val,mt_mu_qcd_val,lep_mu_qcd_pt,weight_mu_qcd_val); } 
 if( pass_mu_qcd && isWcc )  {
  FillHistograms(pspace_nr,0,1,syst_nr,3,met_pt_val,met_phi_val,mt_mu_qcd_val,lep_mu_qcd_pt,weight_mu_qcd_val); } 
 if( pass_mu_qcd && isWbb )  {
  FillHistograms(pspace_nr,0,1,syst_nr,4,met_pt_val,met_phi_val,mt_mu_qcd_val,lep_mu_qcd_pt,weight_mu_qcd_val); }    
 if( pass_ele_good )          { //std::cout<<"filling passed ele good for pspace "<<pspace_nr<<syst_nr<<std::endl;
  FillHistograms(pspace_nr,1,0,syst_nr,0,met_pt_val,met_phi_val,mt_ele_good_val,lep_ele_good_pt,weight_ele_good_val); }    
 if( pass_ele_good && isWl )  {
  FillHistograms(pspace_nr,1,0,syst_nr,1,met_pt_val,met_phi_val,mt_ele_good_val,lep_ele_good_pt,weight_ele_good_val); }    
 if( pass_ele_good && isWc )  {
  FillHistograms(pspace_nr,1,0,syst_nr,2,met_pt_val,met_phi_val,mt_ele_good_val,lep_ele_good_pt,weight_ele_good_val); }    
 if( pass_ele_good && isWcc ) {
  FillHistograms(pspace_nr,1,0,syst_nr,3,met_pt_val,met_phi_val,mt_ele_good_val,lep_ele_good_pt,weight_ele_good_val); }    
 if( pass_ele_good && isWbb ) {
  FillHistograms(pspace_nr,1,0,syst_nr,4,met_pt_val,met_phi_val,mt_ele_good_val,lep_ele_good_pt,weight_ele_good_val); }    
 if( pass_ele_qcd )           {
  FillHistograms(pspace_nr,1,1,syst_nr,0,met_pt_val,met_phi_val,mt_ele_qcd_val,lep_ele_qcd_pt,weight_ele_qcd_val); }      
 if( pass_ele_qcd && isWl )   {
  FillHistograms(pspace_nr,1,1,syst_nr,1,met_pt_val,met_phi_val,mt_ele_qcd_val,lep_ele_qcd_pt,weight_ele_qcd_val); }      
 if( pass_ele_qcd && isWc )   {
  FillHistograms(pspace_nr,1,1,syst_nr,2,met_pt_val,met_phi_val,mt_ele_qcd_val,lep_ele_qcd_pt,weight_ele_qcd_val); }      
 if( pass_ele_qcd && isWcc )  {
  FillHistograms(pspace_nr,1,1,syst_nr,3,met_pt_val,met_phi_val,mt_ele_qcd_val,lep_ele_qcd_pt,weight_ele_qcd_val); }      
 if( pass_ele_qcd && isWbb )  {
  FillHistograms(pspace_nr,1,1,syst_nr,4,met_pt_val,met_phi_val,mt_ele_qcd_val,lep_ele_qcd_pt,weight_ele_qcd_val); }      
 return kTRUE;
}

Bool_t histoFillerTTbarProgression::writeHistWriter( int pspace_nr, int syst_nr, Bool_t isW ){
 for(int qcd_nr=0; qcd_nr<1; ++qcd_nr){
  for(int emu_nr=0; emu_nr<2; ++emu_nr){
   if(isW){
    for(int wflav_nr=0; wflav_nr<5; ++wflav_nr){
     WriteHistograms(pspace_nr, emu_nr, qcd_nr, syst_nr, wflav_nr);
//     DeleteHistograms(pspace_nr, emu_nr, qcd_nr, syst_nr, wflav_nr);
    }
   }
   else{
    WriteHistograms(pspace_nr, emu_nr, qcd_nr, syst_nr, 0);
//    DeleteHistograms(pspace_nr, emu_nr, qcd_nr, syst_nr, 0);
   }
  }
 }
 return kTRUE;
}

#endif // #ifdef histoFillerTTbarProgression_cxx
