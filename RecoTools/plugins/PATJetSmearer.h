// system include files
#include <memory>
#include <algorithm>
#include <TLorentzVector.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "Math/GenVector/VectorUtil.h"

#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"

class PATJetSmearer : public edm::EDProducer{
 public:

  explicit PATJetSmearer(const edm::ParameterSet& iConfig):
   src_(iConfig.getParameter<edm::InputTag>("src")),
   srcGenJet_(iConfig.getParameter<edm::InputTag>("genJet"))
//    recoJet_(iConfig.getParameter<edm::InputTag>("recoJet"))
  {
   produces<pat::JetCollection>();
  }
   ~PATJetSmearer() {}


 private:
  double genRecoMatch(pat::Jet recoJet, edm::Handle<reco::GenJetCollection> genJets){//, edm::Event* evt = 0){

//    assert(evt);
//    evt->getByLabel(srcGenJet_, genJets);
    const reco::GenJet* retVal = 0;
    double PT=-20;	

    double dRbestMatch = 0.5;
    //double dRbestMatch = dRmaxGenJetMatch_;
    for ( reco::GenJetCollection::const_iterator genJet = genJets->begin();
      genJet != genJets->end(); ++genJet ) {
        double dR = deltaR(recoJet.p4(), genJet->p4());
        if ( dR < dRbestMatch ) {
        retVal = &(*genJet);
        dRbestMatch = dR;
      }
    }
    if(retVal!=0) PT=retVal->pt();	
    return PT;
   }

  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
  {
   using namespace edm;
   using namespace reco;

//    // i will make these collections, but want them to start as clones of reco Jets
//   std::auto_ptr<pat::JetCollection> smeared(new pat::JetCollection);
//   std::auto_ptr<pat::JetCollection> smearedUp(new pat::JetCollection);
//   std::auto_ptr<pat::JetCollection> smearedDown(new pat::JetCollection);
   // or would it be better if i just make a smeared collection and have up/down uncertainties as userFloats
   std::auto_ptr<pat::JetCollection> smeared(new pat::JetCollection);
   //ROOT::Math::LorentzVector<ROOT::Math::T_double> p4(new ROOT::Math::LorentzVector);
   edm::Handle<pat::JetCollection> recoJets;
   edm::Handle<reco::GenJetCollection> genJets;
   iEvent.getByLabel(srcGenJet_, genJets);


   double etaRange[6] = {0.0, 0.5, 1.1, 1.7, 2.3, 5.0};
   double scale[5]   = {1.052, 1.057, 1.096, 1.134, 1.288};
   double stat[5]    = {0.012, 0.012, 0.017, 0.035, 0.127};
   double sysUp[5]   = {0.062, 0.056, 0.063, 0.087, 0.155};
   double sysDown[5] = {0.061, 0.055, 0.062, 0.085, 0.153};
   double errUp[5]   = {0.,0.,0.,0.,0.,};
   double errDown[5] = {0.,0.,0.,0.,0.,};
   double sf = 1.;
   double sfUp = 1.;
   double sfDown = 1.;

   for(unsigned int j=0;j<=4;++j){
    errUp[j] = std::sqrt(stat[j]*stat[j]+sysUp[j]*sysUp[j]);
    errDown[j] = std::sqrt(stat[j]*stat[j]+sysDown[j]*sysDown[j]);
//    std::cout<<"Stat: "<<stat[j]<<" SysUp: "<<sysUp[j]<<" ErrUp "<<errUp[j]<<std::endl;
//    std::cout<<"Stat: "<<stat[j]<<" SysDown: "<<sysDown[j]<<" ErrDown "<<errDown[j]<<std::endl;
   }

   if(iEvent.getByLabel(src_,recoJets)){
    for(unsigned int i=0;i!=recoJets->size();++i){
     pat::Jet jet = recoJets->at(i);

     double reco_pt = jet.pt();

	if(reco_pt<20) continue; 

     double reco_eta = fabs( jet.eta() );
     // matching using pointer back (may not be good for PU jets)
     double gen_pt = -10;
     bool matchedGenJet = jet.genJet();
     if(matchedGenJet) gen_pt = jet.genJet()->pt();

     std::cout<<matchedGenJet<<" match --> "<<gen_pt
     << " gen pT, "<<reco_pt<<" reco pT"<<std::endl;

     //matching by looping over genJets collections and going for dR
     double gen_pt_two = genRecoMatch(jet,genJets);

     std::cout<<"Other Gen pT "<<gen_pt_two<<std::endl;

     double ptSmeared = reco_pt;
     double ptSmearedUp = reco_pt;
     double ptSmearedDown = reco_pt;
     
     for(unsigned int j=0;j<=4;++j){
//      std::cout<<"Range: "<<etaRange[j]<<" to "<<etaRange[j+1]<<std::endl;
//      std::cout<<"Range: "<<etaRange[j]<<" to "<<etaRange[j+1]<<std::endl;
      if(reco_eta >= etaRange[j] && reco_eta < etaRange[j+1]){
       sf = scale[j];
       sfUp = scale[j]+errUp[j];
       sfDown = scale[j]+errDown[j];
//       sfUp = scale[j]+stat[j]+sysUp[j];
//       sfDown = scale[j]-stat[j]-sysDown[j];
//       std::cout<<"======="<<std::endl;
//       std::cout<<"eta: "<<reco_eta<<std::endl;
//       std::cout<<"Range: "<<etaRange[j]<<" to "<<etaRange[j+1]<<std::endl;
//       std::cout<<"======="<<std::endl;
      }
     }

     std::cout<<""<<std::endl;

     ptSmeared     = std::max(0., gen_pt + sf     * (reco_pt - gen_pt) );
     ptSmearedUp   = std::max(0., gen_pt + sfUp   * (reco_pt - gen_pt) );
     ptSmearedDown = std::max(0., gen_pt + sfDown * (reco_pt - gen_pt) );
 
     math::PtEtaPhiMLorentzVector p4(ptSmeared,jet.eta(),jet.phi(),jet.mass());
     //ROOT::Math::LorentzVector p4(ptSmeared,jet.eta(),jet.phi(),jet.mass());
     //TLorentzVector p4(ptSmeared,jet.eta(),jet.phi(),jet.mass());
     jet.setP4(p4);
     jet.addUserFloat("pt_gen",gen_pt);
     jet.addUserFloat("pt_uncorr",reco_pt);
     jet.addUserFloat("pt_smearedUp",ptSmearedUp);
     jet.addUserFloat("pt_smearedDown",ptSmearedDown);
     smeared->push_back(jet);
    }
   iEvent.put(smeared);
   }
  }
  // ----- member data -----
  edm::InputTag src_;
  edm::InputTag srcGenJet_;

};
