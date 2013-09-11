/* ---------------------
File: PATMETRenamer

Our Patuples embed different MET flavours as userCands in the MET object.

This clashes with UWAnalysis. This small .cc will convert the MET et, phi, px, py of the userCand to the main collection.

Use with caution.
*/

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "DataFormats/PatCandidates/interface/MET.h"

class PATMETRenamer : public edm::EDProducer {
    public:

        PATMETRenamer(const edm::ParameterSet& pset);
        virtual ~PATMETRenamer(){}
        void produce(edm::Event& evt, const edm::EventSetup& es);
    private:
        edm::InputTag metSrc_;
	
};

PATMETRenamer::PATMETRenamer(
        const edm::ParameterSet& pset):
    metSrc_(pset.getParameter<edm::InputTag>("src"))
            {
        produces<pat::METCollection>();
    }

void PATMETRenamer::produce(edm::Event& evt, const edm::EventSetup& es) {
  edm::Handle<pat::METCollection> mets;
  evt.getByLabel(metSrc_, mets);

  std::auto_ptr<pat::METCollection> out(new pat::METCollection);
  out->reserve(mets->size());

  assert(mets->size() == 1);

  const pat::MET& inputMET = mets->at(0);
  pat::MET outputMET = inputMET;
  outputMET.setP4(inputMET.userCand("type1")->p4());

//  std::cout<<inputMET.pt()<<"   "<<inputMET.userCand("type1")->pt()<<"   "<<outputMET.pt()<<std::endl;
//  std::cout<<inputMET.px()<<"   "<<inputMET.userCand("type1")->px()<<"   "<<outputMET.px()<<std::endl;
//  std::cout<<inputMET.py()<<"   "<<inputMET.userCand("type1")->py()<<"   "<<outputMET.py()<<std::endl;
//  std::cout<<inputMET.phi()<<"   "<<inputMET.userCand("type1")->phi()<<"   "<<outputMET.phi()<<std::endl;

  out->push_back(outputMET);
  evt.put(out);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PATMETRenamer);
