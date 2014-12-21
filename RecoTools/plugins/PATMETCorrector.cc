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

    // get the collections and define the new output MET
    std::auto_ptr<pat::METCollection> outMET(new pat::METCollection);

    edm::Handle<pat::METCollection> inMET;

    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsRaw;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metType1;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metT0pcT1Txy;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsFullJESUp;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsFullJESDown;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsFullUESUp;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsFullUESDown;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsEESUp;
    edm::Handle<std::vector<reco::LeafCandidate>> handleLeafCand_metsEESDown;

    iEvent.getByLabel("systematicsMET", "metsRaw",  handleLeafCand_metsRaw);
    iEvent.getByLabel("systematicsMET", "metType1", handleLeafCand_metType1);
    iEvent.getByLabel("systematicsMET", "metT0pcT1Txy",  handleLeafCand_metT0pcT1Txy);
    iEvent.getByLabel("systematicsMET", "metsFullJESUp",   handleLeafCand_metsFullJESUp);
    iEvent.getByLabel("systematicsMET", "metsFullJESDown", handleLeafCand_metsFullJESDown);
    iEvent.getByLabel("systematicsMET", "metsFullUESUp",   handleLeafCand_metsFullUESUp);
    iEvent.getByLabel("systematicsMET", "metsFullUESDown", handleLeafCand_metsFullUESDown);
    iEvent.getByLabel("systematicsMET", "metsEESUp",   handleLeafCand_metsEESUp);
    iEvent.getByLabel("systematicsMET", "metsEESDown", handleLeafCand_metsEESDown);

    //std::cout<<"RecoTools/plugins/PATMETCorrector.cc: "<<handleLeafCand_metsRaw.product()->front().pt()<<std::endl;

    math::PtEtaPhiMLorentzVector rawP4(
     handleLeafCand_metsRaw.product()->front().pt(),
     handleLeafCand_metsRaw.product()->front().eta(),
     handleLeafCand_metsRaw.product()->front().phi(),
     handleLeafCand_metsRaw.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector type1P4(
     handleLeafCand_metType1.product()->front().pt(),
     handleLeafCand_metType1.product()->front().eta(),
     handleLeafCand_metType1.product()->front().phi(),
     handleLeafCand_metType1.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector T0pcT1TxyP4(
     handleLeafCand_metT0pcT1Txy.product()->front().pt(),
     handleLeafCand_metT0pcT1Txy.product()->front().eta(),
     handleLeafCand_metT0pcT1Txy.product()->front().phi(),
     handleLeafCand_metT0pcT1Txy.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector eesUpP4(
     handleLeafCand_metsEESUp.product()->front().pt(),
     handleLeafCand_metsEESUp.product()->front().eta(),
     handleLeafCand_metsEESUp.product()->front().phi(),
     handleLeafCand_metsEESUp.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector eesDnP4(
     handleLeafCand_metsEESDown.product()->front().pt(),
     handleLeafCand_metsEESDown.product()->front().eta(),
     handleLeafCand_metsEESDown.product()->front().phi(),
     handleLeafCand_metsEESDown.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector jesUpP4(
     handleLeafCand_metsFullJESUp.product()->front().pt(),
     handleLeafCand_metsFullJESUp.product()->front().eta(),
     handleLeafCand_metsFullJESUp.product()->front().phi(),
     handleLeafCand_metsFullJESUp.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector jesDnP4(
     handleLeafCand_metsFullJESDown.product()->front().pt(),
     handleLeafCand_metsFullJESDown.product()->front().eta(),
     handleLeafCand_metsFullJESDown.product()->front().phi(),
     handleLeafCand_metsFullJESDown.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector uesUpP4(
     handleLeafCand_metsFullUESUp.product()->front().pt(),
     handleLeafCand_metsFullUESUp.product()->front().eta(),
     handleLeafCand_metsFullUESUp.product()->front().phi(),
     handleLeafCand_metsFullUESUp.product()->front().mass()
    );

    math::PtEtaPhiMLorentzVector uesDnP4(
     handleLeafCand_metsFullUESDown.product()->front().pt(),
     handleLeafCand_metsFullUESDown.product()->front().eta(),
     handleLeafCand_metsFullUESDown.product()->front().phi(),
     handleLeafCand_metsFullUESDown.product()->front().mass()
    );
    
    if(iEvent.getByLabel(srcMET_,inMET)){
     pat::MET newmet=inMET->at(0);

     newmet.setP4(rawP4);
     newmet.addUserFloat("eesUp_pt",eesUpP4.pt());
     newmet.addUserFloat("eesUp_eta",eesUpP4.eta());
     newmet.addUserFloat("uesUp_pt",uesUpP4.pt());
     newmet.addUserFloat("uesUp_eta",uesUpP4.eta());
     newmet.addUserFloat("jesUp_pt",jesUpP4.pt());
     newmet.addUserFloat("jesUp_eta",jesUpP4.eta());
     newmet.addUserFloat("eesDn_pt",eesDnP4.pt());
     newmet.addUserFloat("eesDn_eta",eesDnP4.eta());
     newmet.addUserFloat("uesDn_pt",uesDnP4.pt());
     newmet.addUserFloat("uesDn_eta",uesDnP4.eta());
     newmet.addUserFloat("jesDn_pt",jesDnP4.pt());
     newmet.addUserFloat("jesDn_eta",jesDnP4.eta());
     //std::cout<<eesUpP4<<std::endl;
     outMET->push_back(newmet);
    }
    iEvent.put(outMET);
}


// obsolete functions 
   // matches jets with L1 correction to jets with L123 corrections
pat::Jet PATMETCorrector::jetMatchL1(pat::Jet jetL123, edm::Handle<pat::JetCollection> jetsL1){
 pat::Jet retVal;
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
