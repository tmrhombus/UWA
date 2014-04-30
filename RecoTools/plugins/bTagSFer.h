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

class bTagSFer : public edm::EDProducer {
   public:

  explicit bTagSFer(const edm::ParameterSet& iConfig):
    src_(iConfig.getParameter<edm::InputTag>("src")),
    leptons_(iConfig.getParameter<edm::InputTag>("leptons")),
    vertex_(iConfig.getParameter<edm::InputTag>("vertices"))
  {
    produces<pat::JetCollection>();
  }

  ~bTagSFer() {}
   private:

  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup)
  {
    using namespace edm;
    using namespace reco;
    std::auto_ptr<pat::JetCollection> jets(new pat::JetCollection);
    Handle<pat::JetCollection > cands;
    Handle<pat::MuonCollection > leptons;
    Handle<reco::VertexCollection> vertices;
    bool verticesExist = iEvent.getByLabel(vertex_,vertices);

    //std::cout<<"Running bTagSFer, vertexes T/F: "<<verticesExist<<std::endl;
    if(verticesExist)
      verticesExist*=(vertices->size()>0)&&(vertices->at(0).isValid());


    if(iEvent.getByLabel(src_,cands))
      for(unsigned int  l=0;l!=cands->size();++l){

        pat::Jet jet = cands->at(l);
        float jet_pt  = jet.pt();
        float jet_eta = fabs(jet.eta());
        float CSVT_SFb, CSVM_SFb, CSVL_SFb;
        float CSVT_errorb, CSVM_errorb, CSVL_errorb;
        CSVT_errorb = 0;
        CSVM_errorb = 0;
        CSVL_errorb = 0;
        std::vector<int> ptmax;
        std::vector<float> CSVT_errorsb, CSVM_errorsb, CSVL_errorsb;

        // pT-Dependant bTag Scale Factors for real b's
        // https://twiki.cern.ch/twiki/pub/CMS/BtagPOG/SFb-pt_WITHttbar_payload_EPS13.txt
        ptmax = {30, 40, 50, 60, 70, 80, 100, 120, 160, 210, 260, 320, 400, 500, 600, 800};
        CSVT_errorsb = {0.0515703, 0.0264008, 0.0272757, 0.0275565, 0.0248745, 0.0218456, 0.0253845, 0.0239588, 0.0271791, 0.0273912, 0.0379822, 0.0411624, 0.0786307, 0.0866832, 0.0942053, 0.102403, 0.204806 };
        CSVM_errorsb = {0.0415707, 0.0204209, 0.0223227, 0.0206655, 0.0199325, 0.0174121, 0.0202332, 0.0182446, 0.0159777, 0.0218531, 0.0204688, 0.0265191, 0.0313175, 0.0415417, 0.0740446, 0.0596716, 0.1193432 };
        CSVL_errorsb = {0.033299, 0.0146768, 0.013803, 0.0170145, 0.0166976, 0.0137879, 0.0149072, 0.0153068, 0.0133077, 0.0123737, 0.0157152, 0.0175161, 0.0209241, 0.0278605, 0.0346928, 0.0350099, 0.0700198 };

        // calculate SF
        for(unsigned int i=0; i<ptmax.size(); ++i){
         if(jet_pt < ptmax[i]){
          CSVT_errorb = CSVT_errorsb[i];
          CSVM_errorb = CSVM_errorsb[i];
          CSVL_errorb = CSVL_errorsb[i];
          break;
         }
         else{
          CSVT_errorb = CSVT_errorsb[ptmax.size()+1];
          CSVM_errorb = CSVM_errorsb[ptmax.size()+1];
          CSVL_errorb = CSVL_errorsb[ptmax.size()+1];
         }
        }
        jet.addUserFloat("CSVT_errorb",CSVT_errorb);
        jet.addUserFloat("CSVM_errorb",CSVM_errorb);
        jet.addUserFloat("CSVL_errorb",CSVL_errorb);

        CSVT_SFb = (0.927563+(1.55479e-05*jet_pt))+(-1.90666e-07*(jet_pt*jet_pt));
        CSVM_SFb = (0.938887+(0.00017124*jet_pt))+(-2.76366e-07*(jet_pt*jet_pt));
        CSVL_SFb = 0.997942*((1.+(0.00923753*jet_pt))/(1.+(0.0096119*jet_pt))); 
        jet.addUserFloat("CSVT_SFb",CSVT_SFb);
        jet.addUserFloat("CSVM_SFb",CSVM_SFb);
        jet.addUserFloat("CSVL_SFb",CSVL_SFb);
 
       // pT/eta-Dependant bTag Scale Factors for 
       // https://twiki.cern.ch/twiki/pub/CMS/BtagPOG/SFlightFuncs_EPS2013.C 
        float CSVT_SFl, CSVM_SFl, CSVL_SFl;
         CSVT_SFl = 0;
         CSVM_SFl = 0;
         CSVL_SFl = 0;
        float CSVT_SFl_down, CSVM_SFl_down, CSVL_SFl_down;
         CSVT_SFl_down = 0;
         CSVM_SFl_down = 0;
         CSVL_SFl_down = 0;
        float CSVT_SFl_up, CSVM_SFl_up, CSVL_SFl_up;
         CSVT_SFl_up = 0;
         CSVM_SFl_up = 0;
         CSVL_SFl_up = 0;
       if(jet_eta <= 0.5){
        //CSVL Mean eta 0-0.5
        CSVL_SFl = ((1.01177+(0.0023066*jet_pt))+(-4.56052e-06*(jet_pt*jet_pt)))+(2.57917e-09*(jet_pt*(jet_pt*jet_pt)));
        CSVL_SFl_down = ((0.977761+(0.00170704*jet_pt))+(-3.2197e-06*(jet_pt*jet_pt)))+(1.78139e-09*(jet_pt*(jet_pt*jet_pt)));
        CSVL_SFl_up = ((1.04582+(0.00290226*jet_pt))+(-5.89124e-06*(jet_pt*jet_pt)))+(3.37128e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta > 0.5 && jet_eta <= 1.0){
       //CSVL Mean eta 0.5-1
       CSVL_SFl = ((0.975966+(0.00196354*jet_pt))+(-3.83768e-06*(jet_pt*jet_pt)))+(2.17466e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVL_SFl_down = ((0.945135+(0.00146006*jet_pt))+(-2.70048e-06*(jet_pt*jet_pt)))+(1.4883e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVL_SFl_up = ((1.00683+(0.00246404*jet_pt))+(-4.96729e-06*(jet_pt*jet_pt)))+(2.85697e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta > 1.0 && jet_eta <= 1.5){
       //CSVL Mean eta 1-1.5
       CSVL_SFl = ((0.93821+(0.00180935*jet_pt))+(-3.86937e-06*(jet_pt*jet_pt)))+(2.43222e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVL_SFl_down = ((0.911657+(0.00142008*jet_pt))+(-2.87569e-06*(jet_pt*jet_pt)))+(1.76619e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVL_SFl_up = ((0.964787+(0.00219574*jet_pt))+(-4.85552e-06*(jet_pt*jet_pt)))+(3.09457e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta > 1.5 && jet_eta <= 2.4){
       //CSVL Mean eta 1.5-2.4
       CSVL_SFl = ((1.00022+(0.0010998*jet_pt))+(-3.10672e-06*(jet_pt*jet_pt)))+(2.35006e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVL_SFl_down = ((0.970045+(0.000862284*jet_pt))+(-2.31714e-06*(jet_pt*jet_pt)))+(1.68866e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVL_SFl_up = ((1.03039+(0.0013358*jet_pt))+(-3.89284e-06*(jet_pt*jet_pt)))+(3.01155e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta <= 0.8){
       //CSVM Mean eta 0-0.8
       CSVM_SFl = ((1.07541+(0.00231827*jet_pt))+(-4.74249e-06*(jet_pt*jet_pt)))+(2.70862e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVM_SFl_down = ((0.964527+(0.00149055*jet_pt))+(-2.78338e-06*(jet_pt*jet_pt)))+(1.51771e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVM_SFl_up = ((1.18638+(0.00314148*jet_pt))+(-6.68993e-06*(jet_pt*jet_pt)))+(3.89288e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta > 0.8 && jet_eta <= 1.6){
       //CSVM Mean 0.8-1.6
       CSVM_SFl = ((1.05613+(0.00114031*jet_pt))+(-2.56066e-06*(jet_pt*jet_pt)))+(1.67792e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVM_SFl_down = ((0.946051+(0.000759584*jet_pt))+(-1.52491e-06*(jet_pt*jet_pt)))+(9.65822e-10*(jet_pt*(jet_pt*jet_pt)));
       CSVM_SFl_up = ((1.16624+(0.00151884*jet_pt))+(-3.59041e-06*(jet_pt*jet_pt)))+(2.38681e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta > 1.6 && jet_eta <= 2.4){
       //CSVM Mean eta 1.6-2.4
       CSVM_SFl = ((1.05625+(0.000487231*jet_pt))+(-2.22792e-06*(jet_pt*jet_pt)))+(1.70262e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVM_SFl_down = ((0.956736+(0.000280197*jet_pt))+(-1.42739e-06*(jet_pt*jet_pt)))+(1.0085e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVM_SFl_up = ((1.15575+(0.000693344*jet_pt))+(-3.02661e-06*(jet_pt*jet_pt)))+(2.39752e-09*(jet_pt*(jet_pt*jet_pt)));
       }
       if(jet_eta <= 2.4){
       //CSVT Mean eta 0-2.4
       CSVT_SFl = ((1.00462+(0.00325971*jet_pt))+(-7.79184e-06*(jet_pt*jet_pt)))+(5.22506e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVT_SFl_down = ((0.845757+(0.00186422*jet_pt))+(-4.6133e-06*(jet_pt*jet_pt)))+(3.21723e-09*(jet_pt*(jet_pt*jet_pt)));
       CSVT_SFl_up = ((1.16361+(0.00464695*jet_pt))+(-1.09467e-05*(jet_pt*jet_pt)))+(7.21896e-09*(jet_pt*(jet_pt*jet_pt)));
       }

      jet.addUserFloat("CSVT_SFl",CSVT_SFl);
      jet.addUserFloat("CSVM_SFl",CSVM_SFl);
      jet.addUserFloat("CSVL_SFl",CSVL_SFl);
      jet.addUserFloat("CSVT_SFl_down",CSVT_SFl_down);
      jet.addUserFloat("CSVM_SFl_down",CSVM_SFl_down);
      jet.addUserFloat("CSVL_SFl_down",CSVL_SFl_down);
      jet.addUserFloat("CSVT_SFl_up",CSVT_SFl_up);
      jet.addUserFloat("CSVM_SFl_up",CSVM_SFl_up);
      jet.addUserFloat("CSVL_SFl_up",CSVL_SFl_up);

       jets->push_back(jet);
      }
     iEvent.put(jets);
    }
   //------------- member data ----------------
   edm::InputTag src_;
   edm::InputTag leptons_;
   edm::InputTag vertex_;
   };
