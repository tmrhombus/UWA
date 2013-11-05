
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDProducer.h"

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
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "DataFormats/Math/interface/deltaR.h"



#include "DataFormats/PatCandidates/interface/MET.h"

class PATMETTypeOne : public edm::EDProducer {
    public:

        PATMETTypeOne(const edm::ParameterSet& pset);
        virtual ~PATMETTypeOne(){}
        void produce(edm::Event& iEvent, const edm::EventSetup& es);
        pat::Jet jetMatchL1(pat::Jet jetL123, edm::Handle<pat::JetCollection> jetsL1);
	math::PtEtaPhiMLorentzVector findCorrection(
    edm::Handle<pat::JetCollection> l123Jets,
    edm::Handle<pat::JetCollection> l1Jets );
	
    private:
	edm::InputTag srcMET_;
	edm::InputTag srcJ1_;
        edm::InputTag srcJ123_;
};

PATMETTypeOne::PATMETTypeOne(
        const edm::ParameterSet& pset):
     srcMET_(pset.getParameter<edm::InputTag>("srcMET")),
     srcJ1_(pset.getParameter<edm::InputTag>("srcJ1")),
     srcJ123_(pset.getParameter<edm::InputTag>("srcJ123"))
            {
        produces<pat::METCollection>();
    }

void PATMETTypeOne::produce(edm::Event& iEvent, const edm::EventSetup& es) {

   using namespace edm;
    using namespace reco;

    // get the collections and define the new output MET
    std::auto_ptr<pat::METCollection> outMET(new pat::METCollection);
    edm::Handle<pat::JetCollection> jetsL1;
    iEvent.getByLabel(srcJ1_,jetsL1);
    edm::Handle<pat::JetCollection> jetsL123;
    iEvent.getByLabel(srcJ123_,jetsL123);
    edm::Handle<pat::METCollection> inMET;

    math::PtEtaPhiMLorentzVector correction;
    math::PtEtaPhiMLorentzVector inP4;
    math::PtEtaPhiMLorentzVector outP4;

    if(iEvent.getByLabel(srcMET_,inMET)){
     pat::MET met=inMET->at(0);
     pat::MET newmet=inMET->at(0);

     correction = findCorrection(jetsL123,jetsL1);
     inP4 = met.p4();
     outP4 = inP4 + correction;
     newmet.setP4(outP4);

     outMET->push_back(newmet);
    }

     iEvent.put(outMET);


}

   // matches jets with L1 correction to jets with L123 corrections
pat::Jet PATMETTypeOne::jetMatchL1(pat::Jet jetL123, edm::Handle<pat::JetCollection> jetsL1){
 pat::Jet retVal;
 //const pat::Jet* retVal = 0;
 //double PT=-20;
 double dRbestMatch = 0.5;
   for (unsigned int i=0; i<jetsL1->size(); i++){
   pat::Jet  jetL1=jetsL1->at(i);
     double dR = deltaR(jetL123.p4(), jetL1.p4());
     if ( dR < dRbestMatch ) {
     retVal = jetL1;
     dRbestMatch = dR;
   }
 }
 return retVal;
}

// https://twiki.cern.ch/twiki/bin/view/CMS/METTypeOneType2Formulae
math::PtEtaPhiMLorentzVector PATMETTypeOne::findCorrection(
 edm::Handle<pat::JetCollection> l123Jets,
 edm::Handle<pat::JetCollection> l1Jets )
{
 math::PtEtaPhiMLorentzVector corr;
 for(unsigned int i=0;i!=l123Jets->size();++i){
  pat::Jet jet123 = l123Jets->at(i);
  pat::Jet jet1 = jetMatchL1(jet123, l1Jets); // should check that this is unique
  corr += jet1.p4() - jet123.p4();
 }
return corr;
}




#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PATMETTypeOne);
