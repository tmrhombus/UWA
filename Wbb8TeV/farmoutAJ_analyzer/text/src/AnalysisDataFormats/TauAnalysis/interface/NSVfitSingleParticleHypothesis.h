#ifndef AnalysisDataFormats_TauAnalysis_NSVfitSingleParticleHypothesis_h
#define AnalysisDataFormats_TauAnalysis_NSVfitSingleParticleHypothesis_h

#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "DataFormats/Common/interface/Ptr.h"

#include "AnalysisDataFormats/TauAnalysis/interface/NSVfitSingleParticleHypothesisBase.h"

#include <string>

class NSVfitResonanceHypothesis;

class NSVfitSingleParticleHypothesis : public NSVfitSingleParticleHypothesisBase
{
 public:

  NSVfitSingleParticleHypothesis() 
    : mother_(NULL)
  {}
  NSVfitSingleParticleHypothesis(const std::string& name, int barcode)
    : NSVfitSingleParticleHypothesisBase(name, barcode),
      mother_(NULL)
  {}
  NSVfitSingleParticleHypothesis(const edm::Ptr<reco::Candidate>& particle, const std::string& name, int barcode)
    : NSVfitSingleParticleHypothesisBase(particle, name, barcode),
      mother_(NULL),
      p4_(particle->p4())
  {
    //std::cout << "<NSVfitSingleParticleHypothesis::NSVfitSingleParticleHypothesis>:" << std::endl;
    //std::cout << " constructor(const edm::Ptr<reco::Candidate>&, std::string, int)" << std::endl;
  }
  NSVfitSingleParticleHypothesis(const NSVfitSingleParticleHypothesis& bluePrint)
    : NSVfitSingleParticleHypothesisBase(bluePrint),
      mother_(bluePrint.mother_),
      p4_(bluePrint.p4_),
      p4_fitted_(bluePrint.p4_fitted_),
      dp4_(bluePrint.dp4_)
  {}

  NSVfitSingleParticleHypothesis& operator=(const NSVfitSingleParticleHypothesis& bluePrint)  
  {  
    NSVfitSingleParticleHypothesisBase::operator=(bluePrint);
    mother_ = bluePrint.mother_;
    p4_ = bluePrint.p4_;
    p4_fitted_ = bluePrint.p4_fitted_;
    dp4_ = bluePrint.dp4_;
    return (*this);
  }

  ~NSVfitSingleParticleHypothesis() {}

  const NSVfitResonanceHypothesis* mother() const { return mother_; }
  void setMother(const NSVfitResonanceHypothesis* mother) 
  {
    mother_ = mother;
  }

  /// momentum of particle before fit, after fit
  /// and difference in momentum (after - before) fit
  const reco::Candidate::LorentzVector& p4() const { return p4_; }
  const reco::Candidate::LorentzVector& p4_fitted() const { return p4_fitted_; }
  const reco::Candidate::LorentzVector& dp4_fitted() const { return dp4_; }

  void print(std::ostream& stream) const
  {
    stream << "<NSVfitSingleParticleHypothesis::print>:" << std::endl;
    stream << " name = " << name_ << std::endl;
    stream << " barcode = " << barcode_ << std::endl;
    stream << " particle(id:key) = " << particle_.id() << ":" << particle_.key() << std::endl;
    stream << " p4: Pt = " << p4_.pt() << ","
	   << " eta = " << p4_.eta() << ", phi = " << p4_.phi() << std::endl;
    stream << " p4_fitted: Pt = " << p4_fitted().pt() << ","
	   << " eta = " << p4_fitted().eta() << ", phi = " << p4_fitted().phi() << std::endl;
    stream << "(x = " << (p4_.energy()/p4_fitted().energy()) << ")" << std::endl;
  }

  friend class NSVfitAlgorithmByLikelihoodMaximization;
  template<typename T1, typename T2> friend class CompositePtrCandidateT1T2MEt;

 protected:

  /// pointer to resonance hypothesis object
  const NSVfitResonanceHypothesis* mother_;

  /// momentum of particle before fit, after fit
  /// and difference (after - before) fit
  reco::Candidate::LorentzVector p4_;
  reco::Candidate::LorentzVector p4_fitted_;
  reco::Candidate::LorentzVector dp4_;  
};

#endif
