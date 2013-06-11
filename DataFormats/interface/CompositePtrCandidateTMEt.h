#ifndef __UWAnalysis_DataFormats_CompositeRefCandidateTMEt_h__
#define __UWAnalysis_DataFormats_CompositeRefCandidateTMEt_h__

/** \class CompositeRefCandidateTMEt
 *
 * Combination of visible tau decay products with missing transverse momentum 
 * (representing the undetected momentum carried away 
 *  the neutrino produced in a W --> tau nu decay and the neutrinos produced in the tau decay)
 * 
 * \authors Christian Veelken
 *
 * \version $Revision: 1.4 $
 *
 * $Id: CompositePtrCandidateTMEt.h,v 1.4 2012/07/01 17:02:13 ojalvo Exp $
 *
 */

#include "DataFormats/Candidate/interface/CandidateFwd.h" 
#include "DataFormats/Candidate/interface/Candidate.h" 
#include "DataFormats/Candidate/interface/LeafCandidate.h" 
#include "DataFormats/Common/interface/Ptr.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

template<typename T>

class CompositePtrCandidateTMEt : public reco::LeafCandidate 
{
  typedef edm::Ptr<T> TPtr;
  typedef edm::Ptr<pat::MET> METPtr;
  typedef edm::Ptr<pat::Jet> JetPtr;
  typedef std::vector<edm::Ptr<pat::Jet> > JetPtrVector;

 public:

  /// default constructor
  CompositePtrCandidateTMEt() {}

  /// constructor with MEt
  CompositePtrCandidateTMEt(const TPtr visDecayProducts, METPtr met)
    : visDecayProducts_(visDecayProducts), met_(met) {recoilDPhi_=0;}

  /// destructor
  ~CompositePtrCandidateTMEt() {}

  /// access to daughter particles
  const TPtr lepton() const { return visDecayProducts_; }

  const int genPdg() const {return pdg_; }

  /// access to gen. mother particles
  /// (undecayed tau leptons)
  const reco::Candidate::LorentzVector& p4Leptongen() const { return p4Leptongen_; }
  
  /// access to visible gen. daughter particles
  /// (electrons, muons, kaons, charged and neutral pions produced in tau decay)
  const reco::Candidate::LorentzVector& p4VisLeptongen() const { return p4VisLeptongen_; }

  /// access to missing transverse momentum
  const METPtr met() const { return met_; }

  /// get transverse mass of visible decay products + missing transverse momentum
  double massZ() const { return massZ_; }
  double mt() const { return mt_; }
  double mJJ() const {return mjj_;}
  double ptJJ() const {return ptjj_;}
  double mJJ2() const {return mjj2_;}

  void setJJVariables(double mjj,double ptjj,double mjj2) {
    mjj_ = mjj;
    mjj2_ = mjj2;
    ptjj_ = ptjj;
  }

  double genMt() const { return genMt_; }
  double corMt() const { return corMt_; }

  /// build transverse momentum 
  double pt() const { return pt_; }
  double px() const { return px_; }
  double py() const { return py_; }

  double corPt() const { return corPt_; }
  double corPx() const { return corPx_; }
  double corPy() const { return corPy_; }

  double trueMet() const {return trueMet_;}
  double trueMetPhi() const {return trueMetPhi_;}
  double trueMEx() const {return trueMEx_;}
  double trueMEy() const {return trueMEy_;}
  double trueMEz() const {return trueMEz_;}
  reco::Candidate::LorentzVector calibratedMET() const {return calibratedMET_;}
  /// get acoplanarity angle (angle in transverse plane) between visible decay products 
  /// and missing transverse momentum 
  double dPhi() const { return dPhi_; } 
  const reco::Candidate::LorentzVector recoil() const {return recoil_;}
  double recoilDPhi() const {return recoilDPhi_;}

  // rebuild neutrino pz, assuming this is a W:
  // This has yet to be tested (and the definition of the neutrino pz revised)
  double metPz() const {return metPz_;}
  double metPzB() const {return metPzB_;}
  bool isPzSolutionComplex() const { return isPzSolutionComplex_;}
  math::XYZTLorentzVector WP4()  const {return WP4_;}

  ///Jet variables
  const JetPtrVector jets() const {return jets_;}
  const JetPtrVector jets5() const {return jets5_;}
  int nJets() const {return jets_.size();}
  int nJets24to5() const {return jets5_.size();}

  double SV1SV2M() const {return SV1SV2M_;} /// set invariant mass of the 2 vertices
  double SV1SV2Pt() const {return SV1SV2Pt_;} /// set invariant pt of the 2 vertices
  double ht() const {return ht_;}
  double nJets24Pt20() const {return nJets24Pt20_;}
  double nJets24Pt25() const {return nJets24Pt25_;}
  double nJets24Pt30() const {return nJets24Pt30_;}
  double SFCSVL1() const {return SFCSVL1_;}
  double SFCSVL2() const {return SFCSVL2_;}
  double SFCSVM1() const {return SFCSVM1_;}
  double SFCSVM2() const {return SFCSVM2_;}
  double SFCSVT1() const {return SFCSVT1_;}
  double SFCSVT2() const {return SFCSVT2_;}
  double SFSSVHE1() const {return SFSSVHE1_;}
  double SFSSVHE2() const {return SFSSVHE2_;}
  double SFCSVL1T() const {return SFCSVL1T_;}
  double SFCSVL2T() const {return SFCSVL2T_;}
  double SFCSVM1T() const {return SFCSVM1T_;}
  double SFCSVM2T() const {return SFCSVM2T_;}
  double SFCSVT1T() const {return SFCSVT1T_;}
  double SFCSVT2T() const {return SFCSVT2T_;}
  double SFSSVHE1T() const {return SFSSVHE1T_;}
  double SFSSVHE2T() const {return SFSSVHE2T_;}
  double EffWEIGHTpt() const {return EffWEIGHTpt_;}
  double EffWEIGHTeta() const {return EffWEIGHTeta_; }
  double metjj() const {return metjj_;}
  double leptonjj() const {return leptonjj_;}

  const JetPtr jet(int i) const {return jets_.at(i);}

  /// clone  object
  CompositePtrCandidateTMEt<T>* clone() const { return new CompositePtrCandidateTMEt<T>(*this); }

 private:

  void setSSVar(double metjj, double leptonjj){
    metjj_=metjj;
    leptonjj_=leptonjj;
  }
  
  void setJetValues(const JetPtrVector& jets,int njetsgt24,double ht) {
    jets_ = jets;
    njetsgt24_ = njetsgt24;
    ht_   = ht;
  }
  /*
  void setJetValues(const JetPtrVector& jets,const JetPtrVector& jets5,double ht) {
    jets_ = jets;
    jets5_ = jets5;
    ht_   = ht;
  }
  */
  void setJetValuesNonTracker(int nJets24Pt20, int nJets24Pt25, int nJets24Pt30) {
    nJets24Pt20_ = nJets24Pt20;
    nJets24Pt25_ = nJets24Pt25;
    nJets24Pt30_ = nJets24Pt30;
  }

  /// allow only CompositePtrCandidateTMEtAlgorithm to change values of data-members
  template<typename T_type> friend class CompositePtrCandidateTMEtAlgorithm; 

  void setP4Leptongen(const reco::Candidate::LorentzVector& p4) { p4Leptongen_ = p4; }
  void setP4VisLeptongen(const reco::Candidate::LorentzVector& p4) { p4VisLeptongen_ = p4; }


  /// set transverse mass of visible decay products + missing transverse momentum
  void setSFCSVL1(double SFCSVL1) { SFCSVL1_ = SFCSVL1; }
  void setSFCSVL2(double SFCSVL2) { SFCSVL2_ = SFCSVL2; }
  void setSFCSVM1(double SFCSVM1) { SFCSVM1_ = SFCSVM1; }
  void setSFCSVM2(double SFCSVM2) { SFCSVM2_ = SFCSVM2; }
  void setSFCSVT1(double SFCSVT1) { SFCSVT1_ = SFCSVT1; }
  void setSFCSVT2(double SFCSVT2) { SFCSVT2_ = SFCSVT2; }
  void setSFSSVHE1(double SFSSVHE1) { SFSSVHE1_ = SFSSVHE1; }
  void setSFSSVHE2(double SFSSVHE2) { SFSSVHE2_ = SFSSVHE2; }
  void setSFCSVL1T(double SFCSVL1T) { SFCSVL1T_ = SFCSVL1T; }
  void setSFCSVL2T(double SFCSVL2T) { SFCSVL2T_ = SFCSVL2T; }
  void setSFCSVM1T(double SFCSVM1T) { SFCSVM1T_ = SFCSVM1T; }
  void setSFCSVM2T(double SFCSVM2T) { SFCSVM2T_ = SFCSVM2T; }
  void setSFCSVT1T(double SFCSVT1T) { SFCSVT1T_ = SFCSVT1T; }
  void setSFCSVT2T(double SFCSVT2T) { SFCSVT2T_ = SFCSVT2T; }
  void setSFSSVHE1T(double SFSSVHE1T) { SFSSVHE1T_ = SFSSVHE1T; }
  void setSFSSVHE2T(double SFSSVHE2T) { SFSSVHE2T_ = SFSSVHE2T; }
  void setEffWEIGHTpt(double EffWEIGHTpt) { EffWEIGHTpt_ = EffWEIGHTpt; }
  void setEffWEIGHTeta(double EffWEIGHTeta) { EffWEIGHTeta_ = EffWEIGHTeta; }
  void setMassZ(double massZ) { massZ_ = massZ; }
  void setMt(double mt) { mt_ = mt; }
  void setPx(double px) { px_ = px; }
  void setPy(double py) { py_ = py; }
  void setPt(double pt) { pt_ = pt; }
  void setSV1SV2M(double SV1SV2M) { SV1SV2M_ = SV1SV2M; }
  void setSV1SV2Pt(double SV1SV2Pt) { SV1SV2Pt_ = SV1SV2Pt; }

  void setCalibratedMET(const reco::Candidate::LorentzVector& met) { calibratedMET_ = met; }
  void setCorMt(double corMt) { corMt_ = corMt; }
  void setCorPx(double corPx) { corPx_ = corPx; }
  void setCorPy(double corPy) { corPy_ = corPy; }
  void setCorPt(double corPt) { corPt_ = corPt; }

  void setTrueMet(double trueMet){trueMet_=trueMet;}
  void setTrueMetPhi(double trueMetPhi){trueMetPhi_=trueMetPhi;}
  void setTrueMEy(double trueMEy){trueMEy_=trueMEy;}
  void setTrueMEx(double trueMEx){trueMEx_=trueMEx;}
  void setTrueMEz(double trueMEz){trueMEz_=trueMEz;}

  void setGenMt(double genMt) {genMt_ = genMt; }

  void setPdg(int pdg) {pdg_ = pdg;}

  /// set acoplanarity angle (angle in transverse plane) between visible decay products 
  /// and missing transverse momentum
  void setDPhi(double dPhi) { dPhi_ = dPhi; }
  
  void setRecoil(const reco::Candidate::LorentzVector& recoil) {recoil_ = recoil; }
  void setRecoilDPhi(double dPhi) {recoilDPhi_ = dPhi;}


  
  // rebuild neutrino pz (with a different name just in case), assuming this is a W:
  void setMetPz(double metPz) {metPz=metPz_;}
  void setMetPzB(double metPzB) {metPzB=metPzB_;}
  void setIsComplex(double isPzSolutionComplex){isPzSolutionComplex=isPzSolutionComplex_;}
  void setWP4 ( math::XYZTLorentzVector WP4) {WP4=WP4_;} 

  /// references/pointers to decay products and missing transverse momentum
  reco::Candidate::LorentzVector recoil_;
  double recoilDPhi_;

  TPtr visDecayProducts_;
  METPtr met_;
  /// transverse mass of visible decay products + missing transverse momentum
  double SFCSVL1_;
  double SFCSVL2_;
  double SFCSVM1_;
  double SFCSVM2_;
  double SFCSVT1_;
  double SFCSVT2_;
  double SFSSVHE1_;
  double SFSSVHE2_;
  double SFCSVL1T_;
  double SFCSVL2T_;
  double SFCSVM1T_;
  double SFCSVM2T_;
  double SFCSVT1T_;
  double SFCSVT2T_;
  double SFSSVHE1T_;
  double SFSSVHE2T_;
  double massZ_;
  double mt_;
  double corMt_;
  double SV1SV2M_;
  double SV1SV2Pt_;
  /// W momentum:
  double px_;
  double py_;
  double pt_;
  double corPx_;
  double corPy_;
  double corPt_;

  double EffWEIGHTeta_;
  double EffWEIGHTpt_;

  reco::Candidate::LorentzVector calibratedMET_;

  /// acoplanarity angle (angle in transverse plane) between visible decay products
  /// and missing transverse momentum
  double dPhi_;

  // pz of the neutrino (once the candidate is assumed to be a W boson)
  double metPz_;
  double metPzB_;
  double isPzSolutionComplex_;
  math::XYZTLorentzVector WP4_;

  JetPtrVector jets_;
  JetPtrVector jets5_;
  int njetsgt24_;
  int nJets24Pt20_;
  int nJets24Pt25_;
  int nJets24Pt30_;

  double ht_;
  //setSSVar
  double metjj_,leptonjj_;

  //JJ variables
  double mjj_,ptjj_,mjj2_;

  /// gen. four-momenta
  reco::Candidate::LorentzVector p4Leptongen_;
  reco::Candidate::LorentzVector p4VisLeptongen_;

  int pdg_;

  //true Met
  double trueMet_;
  double trueMetPhi_;
  double trueMEy_;
  double trueMEx_;
  double trueMEz_;
  double genMt_;

};

#include "DataFormats/PatCandidates/interface/Tau.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "DataFormats/PatCandidates/interface/Electron.h"

typedef CompositePtrCandidateTMEt<pat::Tau> PATTauNuPair;
typedef CompositePtrCandidateTMEt<pat::Muon> PATMuonNuPair;
typedef CompositePtrCandidateTMEt<pat::Electron> PATElectronNuPair;
typedef CompositePtrCandidateTMEt<reco::Candidate> PATCandNuPair;

#endif
