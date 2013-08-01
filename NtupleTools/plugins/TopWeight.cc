// system include files
#include <memory>

// user include files
#include "DataFormats/Candidate/interface/Candidate.h"
#include <TTree.h>
#include "UWAnalysis/NtupleTools/interface/NtupleFillerBase.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

// Stuff for gen level ID (based on a W analysis...)

class TopWeight : public NtupleFillerBase {
 public:

    TopWeight(){
    }

    TopWeight(const edm::ParameterSet& iConfig, TTree* t):
    CorFactorA_(iConfig.getUntrackedParameter<double>("A",0.156)),
    CorFactorB_(iConfig.getUntrackedParameter<double>("B",-0.00137)),
    src_(iConfig.getParameter<edm::InputTag>("src"))
        {
            weightTop=1; topPt=-1; antitopPt=-1;

            t->Branch("weightTop",&weightTop,"weightTop/F");
            t->Branch("topPt",&topPt,"topPt/F");
            t->Branch("antitopPt",&antitopPt,"antitopPt/F");
        }

    ~TopWeight()
        {

        }

    double scaleFactor(double toppt);
    void fill(const edm::Event& iEvent,const edm::EventSetup& iSetup);

 protected:
    double CorFactorA_;
    double CorFactorB_;
    edm::InputTag src_;

    float weightTop;
    float topPt;
    float antitopPt;

};

double TopWeight::scaleFactor(double toppt){
        if (toppt<0) return 1;
        double corPt=CorFactorA_+toppt*CorFactorB_;
        corPt=exp(corPt);
        return corPt;
}

void TopWeight::fill(const edm::Event& iEvent,const edm::EventSetup& iSetup){

  weightTop=1; topPt=-1; antitopPt=-1;

  edm::Handle< std::vector<reco::GenParticle> >pGenPart;
  if(iEvent.getByLabel(src_, pGenPart)){
          for( size_t i = 0; i < pGenPart->size(); ++ i ) {
                const reco::GenParticle& genpart = (*pGenPart)[i];

                if(abs(genpart.pdgId())!=6 || genpart.status()!=3) continue;
                if (genpart.pdgId()==6) {topPt=genpart.pt();}
                if (genpart.pdgId()==-6) {antitopPt=genpart.pt();}
          }
          if (topPt>0 && antitopPt>0){
                double SF_Top=scaleFactor(topPt);
                double SF_AntiTop=scaleFactor(antitopPt);
                weightTop=sqrt(SF_Top*SF_AntiTop);
          }
  }
}
#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_EDM_PLUGIN(NtupleFillerFactory, TopWeight, "TopWeight");
