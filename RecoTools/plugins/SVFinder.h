/*
Calculates bTag scale factors and makes userFloats
Authors: T.M.Perry, M.Cepeda
*/

#include "PhysicsTools/JetMCUtils/interface/JetMCTag.h"

// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/TauReco/interface/PFTau.h"
#include "DataFormats/MuonReco/interface/MuonSelectors.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJet.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "Math/GenVector/VectorUtil.h"
//
// class decleration
#include <boost/foreach.hpp>
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/angle.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/BTauReco/interface/TrackIPTagInfo.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackBase.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "Math/GenVector/VectorUtil.h"
#include "DataFormats/PatCandidates/interface/Muon.h"
#include "TLorentzVector.h"
#include "DataFormats/BTauReco/interface/TaggingVariable.h"

class SVFinder : public edm::EDProducer {
   public:

  explicit SVFinder(const edm::ParameterSet& iConfig):
    src_(iConfig.getParameter<edm::InputTag>("src")),
    leptons_(iConfig.getParameter<edm::InputTag>("leptons")),
    vertex_(iConfig.getParameter<edm::InputTag>("vertices"))
  {
    produces<pat::JetCollection>();
  }

  ~SVFinder() {}
   private:

  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
  {
    using namespace edm;
    using namespace reco;
    std::auto_ptr<pat::JetCollection> jets(new pat::JetCollection);
    Handle<pat::JetCollection > cands;
    Handle<pat::MuonCollection > leptons; ///adding muons! :D
    Handle<reco::VertexCollection> vertices;
    bool verticesExist = iEvent.getByLabel(vertex_,vertices);

    std::cout<<"Running SVFinder, vertexes T/F: "<<verticesExist<<std::endl;
    if(verticesExist)
      verticesExist*=(vertices->size()>0)&&(vertices->at(0).isValid());


    if(iEvent.getByLabel(src_,cands))
      for(unsigned int  l=0;l!=cands->size();++l){

        pat::Jet jet = cands->at(l);
        float jet_pt = jet.pt();
        float CSVT_SF, CSVM_SF, CSVL_SF;
        float CSVT_error, CSVM_error, CSVL_error;
        std::vector<int> ptmax;
        std::vector<float> CSVT_errors, CSVM_errors, CSVL_errors;

        // pT-Dependant bTag Scale Factors
        ptmax = {30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800};
        CSVT_errors = {0.0515703, 0.0264008, 0.0272757, 0.0275565, 0.0248745, 0.0218456, 0.0253845, 0.0239588, 0.0271791, 0.0273912, 0.0379822, 0.0411624, 0.0786307, 0.0866832, 0.0942053, 0.102403 };
        CSVM_errors = {0.0415707, 0.0204209, 0.0223227, 0.0206655, 0.0199325, 0.0174121, 0.0202332, 0.0182446, 0.0159777, 0.0218531, 0.0204688, 0.0265191, 0.0313175, 0.0415417, 0.0740446, 0.0596716 };
        CSVL_errors = {0.033299, 0.0146768, 0.013803, 0.0170145, 0.0166976, 0.0137879, 0.0149072, 0.0153068, 0.0133077, 0.0123737, 0.0157152, 0.0175161, 0.0209241, 0.0278605, 0.0346928, 0.0350099 };

        // calculate SF
        for(unsigned int i=0; i<ptmax.size(); ++i){
         if(jet_pt < ptmax[i]){
          CSVT_error = CSVT_errors[i];
          CSVM_error = CSVM_errors[i];
          CSVL_error = CSVL_errors[i];
          break;
         }
        }
        jet.addUserFloat("CSVT_error",CSVT_error);
        jet.addUserFloat("CSVM_error",CSVM_error);
        jet.addUserFloat("CSVL_error",CSVL_error);

        CSVT_SF = (0.927563+(1.55479e-05*jet_pt))+(-1.90666e-07*(jet_pt*jet_pt));
        CSVM_SF = (0.938887+(0.00017124*jet_pt))+(-2.76366e-07*(jet_pt*jet_pt));
        CSVL_SF = 0.997942*((1.+(0.00923753*jet_pt))/(1.+(0.0096119*jet_pt))); 
        jet.addUserFloat("CSVT_SF",CSVT_SF);
        jet.addUserFloat("CSVM_SF",CSVM_SF);
        jet.addUserFloat("CSVL_SF",CSVL_SF);

       jets->push_back(jet);
      }
     iEvent.put(jets);
    }
   //------------- member data ----------------
   edm::InputTag src_;
   edm::InputTag leptons_;
   edm::InputTag vertex_;
   };
