#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/Utilities/interface/Exception.h"
#include "FWCore/ServiceRegistry/interface/Service.h"

// system include files
#include <memory>
#include <algorithm>
#include <TLorentzVector.h>

// user include files

#include "DataFormats/PatCandidates/interface/MET.h"
#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "DataFormats/Math/interface/deltaR.h"

class PATMETCorrector : public edm::EDProducer {
    public:

        PATMETCorrector(const edm::ParameterSet& pset);
        virtual ~PATMETCorrector(){}
        void produce(edm::Event& iEvent, const edm::EventSetup& es);
        pat::Jet jetMatchL1(pat::Jet jetL123, edm::Handle<pat::JetCollection> jetsL1);
	math::PtEtaPhiMLorentzVector findCorrectionType1(
          edm::Handle<pat::JetCollection> jets, bool isMC);
        math::PtEtaPhiMLorentzVector findCorrectionXY(int nrVtx, bool isMC);
        math::PtEtaPhiMLorentzVector antiCorrectionType1(
          edm::Handle<pat::JetCollection> jets);
    private:
	edm::InputTag srcMET_;
        edm::InputTag srcJ123_;
        edm::InputTag srcVert_;
        bool mc_;
};

PATMETCorrector::PATMETCorrector(
        const edm::ParameterSet& pset):
     srcMET_(pset.getParameter<edm::InputTag>("srcMET")),
     srcJ123_(pset.getParameter<edm::InputTag>("srcJ123")),
     srcVert_(pset.getParameter<edm::InputTag>("srcVert")),
     mc_(pset.getParameter<bool>("mc"))
     {
      produces<pat::METCollection>();
     }

void PATMETCorrector::produce(edm::Event& iEvent, const edm::EventSetup& es) {

    using namespace edm;
    using namespace reco;

    // get the collections and define the new output MET
    std::auto_ptr<pat::METCollection> outMET(new pat::METCollection);

    edm::Handle<pat::JetCollection> jets;
    iEvent.getByLabel(srcJ123_,jets);

    edm::Handle<reco::VertexCollection> vertices;
    iEvent.getByLabel(srcVert_, vertices);
    int Nvtx = vertices->size();

    edm::Handle<pat::METCollection> inMET;

    math::PtEtaPhiMLorentzVector correctionType1;
    math::PtEtaPhiMLorentzVector correctionXY;
    math::PtEtaPhiMLorentzVector inP4;
    math::PtEtaPhiMLorentzVector outP4;
    math::PtEtaPhiMLorentzVector antiType1;

    if(iEvent.getByLabel(srcMET_,inMET)){
     pat::MET met=inMET->at(0);
     pat::MET newmet=inMET->at(0);

     correctionType1 = findCorrectionType1(jets, mc_);
     antiType1 = antiCorrectionType1(jets);
     correctionXY = findCorrectionXY(Nvtx, mc_);
     if(mc_){
      inP4 = met.p4();
      outP4 = inP4 - correctionXY;
     }
     if(!mc_){
      //inP4 = met.p4();
      //inP4 = met.userCand("type0rtT1Txy")->p4();
      //inP4 = met.userCand("type0pcT1Txy")->p4();
      inP4 = met.userCand("type1")->p4();
      //inP4 = met.userCand("raw")->p4();
      outP4 = inP4 - correctionXY;
     }
     newmet.setP4(outP4);
     outMET->push_back(newmet);
    }
    iEvent.put(outMET);
}

   // matches jets with L1 correction to jets with L123 corrections
pat::Jet PATMETCorrector::jetMatchL1(pat::Jet jetL123, edm::Handle<pat::JetCollection> jetsL1){
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
math::PtEtaPhiMLorentzVector PATMETCorrector::antiCorrectionType1(edm::Handle<pat::JetCollection> jets)
{
 math::PtEtaPhiMLorentzVector corr;
 math::PtEtaPhiMLorentzVector JCor;
 math::PtEtaPhiMLorentzVector JUnc;
 for(unsigned int i=0;i!=jets->size();++i){
  pat::Jet jet = jets->at(i);
  JUnc += jet.correctedP4("L3Absolute");
  JCor += jet.correctedP4("L1FastJet");
 // if (jet.pt() > 10.)
 // {
 //   std::cout<<"L1: "<<std::endl;
 //   std::cout<<" pt: "<<jet.correctedP4("L1FastJet").pt()<<
 //              " eta: "<<jet.correctedP4("L1FastJet").eta()<<
 //              " phi: "<<jet.correctedP4("L1FastJet").phi()<<std::endl;

 //   std::cout<<"L3: "<<std::endl;
 //   std::cout<<" pt: "<<jet.correctedP4("L3Absolute").pt()<<
 //              " eta: "<<jet.correctedP4("L3Absolute").eta()<<
 //              " phi: "<<jet.correctedP4("L3Absolute").phi()<<std::endl;

 //   //std::cout<<"L1:  "<<jet.correctedP4("L1FastJet")<<std::endl;
 //   //std::cout<<"L2:  "<<jet.correctedP4("L2Relative")<<std::endl;
 //   //std::cout<<"L3:  "<<jet.correctedP4("L3Absolute")<<std::endl;
 //   //std::cout<<"L23: "<<jet.correctedP4("L2L3Residual")<<std::endl<<std::endl;

 //   //corr += jet.correctedP4("L1FastJet") - jet.correctedP4("L2L3Residual");
 //   corr += jet.correctedP4("L3Absolute") - jet.correctedP4("L1FastJet");
 //   //corr += jet.correctedP4("L1FastJet") - jet.correctedP4("L3Absolute");

 //   //else{corr += jet.correctedP4("L1FastJet") - jet.correctedP4("L2L3Residual");}
 //  //corr += jet.correctedP4("L1FastJet") - jet.p4();
 // }
 }
 corr = JUnc - JCor;
 return corr;
}
// https://twiki.cern.ch/twiki/bin/view/CMS/METTypeOneType2Formulae
math::PtEtaPhiMLorentzVector PATMETCorrector::findCorrectionType1(edm::Handle<pat::JetCollection> jets, bool isMC)
{
 math::PtEtaPhiMLorentzVector corr;
 //std::cout<<corr.pt()<<" "<<corr.eta()<<" "<<corr.phi()<<std::endl;
 for(unsigned int i=0;i!=jets->size();++i){
  pat::Jet jet = jets->at(i);
  if (jet.pt() > 10.)
  {
    if(isMC){corr += jet.correctedP4("L1FastJet") - jet.correctedP4("L3Absolute");}
    else{corr += jet.correctedP4("L1FastJet") - jet.correctedP4("L2L3Residual");}
   //corr += jet.correctedP4("L1FastJet") - jet.p4();
  }
 }
 return corr;
}

// xy corrections from JetMETCorrections/Type1MET/python/pfMETsysShiftCorrections_cfi.py
// https://github.com/cms-sw/cmssw/blob/CMSSW_5_3_14_patch1/JetMETCorrections/Type1MET/python/pfMETsysShiftCorrections_cfi.py
math::PtEtaPhiMLorentzVector PATMETCorrector::findCorrectionXY(int nrVtx, bool isMC)
{
 //math::XYZTLorentzVector corrXYZ;
 //math::PtEtaPhiMLorentzVector corr;
 if(isMC){
  math::XYZTLorentzVector corrXYZ(1.62861e-01 - 2.38517e-02*nrVtx,3.60860e-01 - 1.30335e-01*nrVtx,0,0);
  math::PtEtaPhiMLorentzVector corr(corrXYZ.pt(),corrXYZ.eta(),corrXYZ.phi(),corrXYZ.M());
  return corr;
 }
 else{
  math::XYZTLorentzVector corrXYZ(4.83642e-02 + 2.48870e-01*nrVtx,-1.50135e-01 - 8.27917e-02*nrVtx,0,0);
  math::PtEtaPhiMLorentzVector corr(corrXYZ.pt(),corrXYZ.eta(),corrXYZ.phi(),corrXYZ.M());
  return corr;
 }
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PATMETCorrector);
