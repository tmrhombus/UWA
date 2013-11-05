// system include files
#include <memory>
#include <algorithm>
#include <TLorentzVector.h>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/Utilities/interface/Exception.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

class PATMETTypeOne : public edm::EDProducer {
   public:
    explicit PATMETTypeOne(const edm::ParameterSet& iConfig):
     srcMET_(iConfig.getParameter<edm::InputTag>("srcMET")),
     srcJ1_(iConfig.getParameter<edm::InputTag>("srcJ1")),
     srcJ123_(iConfig.getParameter<edm::InputTag>("srcJ123"))
     {
      produces<pat::MET>
     }
    ~PATMETTypeOne();

   private:
   // matches jets with L1 correction to jets with L123 corrections
   pat::Jet jetMatchL1(pat::Jet jetL123, edm::Handle<pat::JetCollection> jetsL1){
    const pat::Jet* retVal = 0;
    double PT=-20;
    double dRbestMatch = 0.5;
    for ( pat::JetCollection::const_iterator jetL1 = jetsL1->begin();
      jetL1 != jetsL1->end(); ++jetL1 ) {
        double dR = deltaR(jetL123.p4(), jetL1->p4());
        if ( dR < dRbestMatch ) {
        retVal = &(*jetL1);
        dRbestMatch = dR;
      }
    }
    return retVal;
   }

   // https://twiki.cern.ch/twiki/bin/view/CMS/METType1Type2Formulae
   mathPtEtaPhiMLorentzVector findCorrection(
    edm::Handle<pat::JetCollection> l123Jets,
    edm::Handle<pat::JetCollection> l1Jets )
   {
    mathPtEtaPhiMLorentzVector corr; 
    for(unsigned int i=0;i!=l123Jets->size();++i){
     pat::Jet jet123 = l123Jets->at(i);
     pat::Jet jet1 = jetMatchL1(jet123, l1Jets); // should check that this is unique
     corr += jet1.p4() - jet123.p4();
    }
   return corr;
   }  

   virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
   {
    using namespace edm;
    using namespace reco;
  
    // get the collections and define the new output MET
    std::auto_ptr<pat::METCollection> newMET(new pat::METCollection);
    edm::Handle<pat::JetCollection> jetsL1;
    iEvent.getByLabel(srcJ1_,jetsL1);
    edm::Handle<pat::JetCollection> jetsL123;
    iEvent.getByLabel(srcJ123,jetsL123);
    edm::Handle<pat::METCollection> inMET;

    math::PtEtaPhiMLorentzVector correction;
    math::PtEtaPhiMLorentzVector inP4;
    math::PtEtaPhiMLorentzVector outP4;
 
    if(iEvent.getByLabel(srcMET_,inMET)){
     correction = findCorrection(jetsL123,jetsL1);
     inP4 = inMET.p4(); 
     outp4 = inP4 + correction;
     newMET = inMET.clone();
     newMET.setP4(outp4);
    
     iEvent.put(newMET);
    }
   }

      // ----------member data ---------------------------

      edm::InputTag srcMET_;       //input Collection
      edm::InputTag srcJ1_;        //input Collection
      edm::InputTag srcJ123_;      //input Collection
 };
