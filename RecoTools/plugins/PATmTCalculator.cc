// WARNING  never finished writing this
// doesn't check for existance of muon/met and crashes

// system include files
#include <memory>
#include <algorithm>
#include <TLorentzVector.h>
#include <math.h> //fabs

// user include files
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/PatCandidates/interface/Muon.h"

class PATmTCalculator : public edm::EDProducer {
    public:

        PATmTCalculator(const edm::ParameterSet& pset);
        virtual ~PATmTCalculator(){}
        void produce(edm::Event& iEvent, const edm::EventSetup& es);
    private:
	edm::InputTag srcMET_;
        edm::InputTag srcMuon_;
};

PATmTCalculator::PATmTCalculator(
        const edm::ParameterSet& pset):
     srcMET_(pset.getParameter<edm::InputTag>("srcMET")),
     srcMuon_(pset.getParameter<edm::InputTag>("srcMuon"))
            {
        produces<pat::MuonCollection>();
    }

void PATmTCalculator::produce(edm::Event& iEvent, const edm::EventSetup& es) {

    using namespace edm;
    using namespace reco;
    double pi,pt_muon,pt_met,phi_muon,phi_met,dphi,mt = -1.;

    // get the collections
    edm::Handle<pat::MuonCollection> inMuon ;
    edm::Handle<pat::METCollection> inMET ;
    if(iEvent.getByLabel(srcMuon_,inMuon)){
     if(iEvent.getByLabel(srcMET_,inMET)){

      pat::MET met=inMET->at(0);
      pat::Muon muon=inMuon->at(0);
      pi = acos(-1.);
      pt_muon = muon.pt();
      pt_met = met.pt();
      phi_muon = muon.phi();
      phi_met = met.phi();
      dphi = fabs(phi_muon - phi_met);
      if (dphi > pi){dphi = 2*pi - dphi;} 
      mt = sqrt(2*pt_muon*pt_met*(1. - cos(dphi)));
    //outMET->push_back(newmet);
     }   
    }
    //iEvent.put(outMET);
   std::cout<<pi<<std::endl;
   std::cout<<"muon"<<std::endl<<" "<<pt_muon<<" "<<phi_muon<<std::endl;
   std::cout<<"met"<<std::endl<<" "<<pt_met<<" "<<phi_met<<std::endl;
   std::cout<<"dphi = "<<dphi<<" mt = "<<mt<<std::endl;

}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PATmTCalculator);
