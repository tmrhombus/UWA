
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
          edm::Handle<pat::JetCollection> l123Jets);
    private:
	edm::InputTag srcMET_;
        edm::InputTag srcJ123_;
};

PATMETTypeOne::PATMETTypeOne(
        const edm::ParameterSet& pset):
     srcMET_(pset.getParameter<edm::InputTag>("srcMET")),
     srcJ123_(pset.getParameter<edm::InputTag>("srcJ123"))
            {
        produces<pat::METCollection>();
    }

void PATMETTypeOne::produce(edm::Event& iEvent, const edm::EventSetup& es) {

    using namespace edm;
    using namespace reco;

    // get the collections and define the new output MET
    std::auto_ptr<pat::METCollection> outMET(new pat::METCollection);

    edm::Handle<pat::JetCollection> jetsL123;
    iEvent.getByLabel(srcJ123_,jetsL123);

    edm::Handle<pat::METCollection> inMET;

    math::PtEtaPhiMLorentzVector correction;
    math::PtEtaPhiMLorentzVector inP4;
    math::PtEtaPhiMLorentzVector outP4;

    if(iEvent.getByLabel(srcMET_,inMET)){
     pat::MET met=inMET->at(0);
     pat::MET newmet=inMET->at(0);

     correction = findCorrection(jetsL123);
     inP4 = met.p4();
     outP4 = inP4 + correction;
     newmet.setP4(outP4);
//     std::cout<<"MET In   pt "<<inP4.pt()      <<" eta "<<inP4.eta()<<" phi "<<inP4.phi()<<std::endl;
//     std::cout<<"MET Corr pt "<<correction.pt()<<" eta "<<correction.eta()<<" phi "<<correction.phi()<<std::endl;
//     std::cout<<"MET Out  pt "<<outP4.pt()     <<" eta "<<outP4.eta()<<" phi "<<outP4.phi()<<std::endl;
//     std::cout<<"MET New  pt "<<newmet.pt()    <<" eta "<<newmet.eta()<<" phi "<<newmet.phi()<<std::endl;
//     std::cout<<std::endl;
//     std::cout<<"MET In   px "<<inP4.px()      <<" py "<<inP4.py()<<" pz "<<inP4.pz()<<std::endl;
//     std::cout<<"MET Corr px "<<correction.px()<<" py "<<correction.py()<<" pz "<<correction.pz()<<std::endl;
//     std::cout<<"MET Out  px "<<outP4.px()     <<" py "<<outP4.py()<<" pz "<<outP4.pz()<<std::endl;
//     std::cout<<"MET New  px "<<newmet.px()    <<" py "<<newmet.py()<<" pz "<<newmet.pz()<<std::endl;
//     std::cout<<std::endl;

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
math::PtEtaPhiMLorentzVector PATMETTypeOne::findCorrection(edm::Handle<pat::JetCollection> l123Jets)
{
 math::PtEtaPhiMLorentzVector corr;
 for(unsigned int i=0;i!=l123Jets->size();++i){
  pat::Jet jet123 = l123Jets->at(i);
  corr += jet123.correctedP4("L1FastJet") - jet123.p4();
//  std::cout<<"L1   px "<<jet123.correctedP4("L1FastJet").px()
//               <<" py "<<jet123.correctedP4("L1FastJet").px()
//               <<" pz "<<jet123.correctedP4("L1FastJet").px()<<std::endl;
//  std::cout<<"L123 px "<<jet123.p4().px()
//               <<" py "<<jet123.p4().px()
//               <<" pz "<<jet123.p4().px()<<std::endl<<std::endl;
 }
 return corr;
}




#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PATMETTypeOne);
