// -*- C++ -*-
//
// Package:    PATMuonTrackVetoSelector
// Class:      PATMuonTrackVetoSelector
// 
/**\class PATMuonTrackVetoSelector PATMuonTrackVetoSelector.cc UWAnalysis/PATMuonTrackVetoSelector/src/PATMuonTrackVetoSelector.cc

 Description: <one line class summary>

 Implementation:
     <Notes on implementation>
*/
//
// Original Author:  Isobel Ojalvo
//         Created:  Sun Jan 31 15:04:57 CST 2010
// $Id: PATJetOverloader.h,v 1.1 2011/06/18 00:41:29 bachtis Exp $
//
//
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

class PATJetOverloader : public edm::EDProducer {
   public:
  
  

  explicit PATJetOverloader(const edm::ParameterSet& iConfig):
    src_(iConfig.getParameter<edm::InputTag>("src")),
    leptons_(iConfig.getParameter<edm::InputTag>("leptons")),
    vertex_(iConfig.getParameter<edm::InputTag>("vertices"))
  {
    produces<pat::JetCollection>();
  }
  
  ~PATJetOverloader() {}
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
    //reco::btau::trackSip2dSigAboveCharm;

    //std::cout<<"Running PATJetOverloader, vertexes T/F: "<<verticesExist<<std::endl;
    //printf("Gets Here1\n");
    if(verticesExist)
      verticesExist*=(vertices->size()>0)&&(vertices->at(0).isValid());


    if(iEvent.getByLabel(src_,cands)) 
      for(unsigned int  l=0;l!=cands->size();++l){

	//printf("Gets Here1.0\n");
	pat::Jet jet = cands->at(l);
	//float trackSIP =jet.get(trackSip2dValAboveCharm);
	//bool taginfosize = jet.hasTagInfo("vertexMass");
	//bool taginfosize = jet.tagInfo().hasTracks();
	//if(taginfosize)
	//{printf("Has Tracks!!\n");}
	//printf("tag info size %i \n",taginfosize);
	//const reco::SecondaryVertexTagInfo* secInfo = jet.tagInfoSecondaryVertex("secondaryVertex");
	//if(jet.bDiscriminator("combinedSecondaryVertexBJetTags").isNonnull())
	//printf("CSV : %f\n",jet.bDiscriminator("combinedSecondaryVertexBJetTags"));
	/*




	*/
	//reco::TaggingVariable(reco::btau::vertexMass,31);

	//if(vertexmass!=31)

	//const reco::BaseTagInfo* stuff = jet.tagInfo(trackSip2dValAboveCharm);
	//float n = stuff->TaggingVariableName{trackSip2dValAboveCharm};
	//using namespace reco::btag;
	//float size = jet.tagInfo(stuff);
	//enum TaggingVariableName trackSim2dValAboveCharm;
	//float stuf = get(stuff);
	//printf("Gets to PatJetOverloader\n");
	if(jet.hasTagInfo("trackIP"))printf("has Track IP TagInfo\n");

	//if(jet.hasTagInfo("secondaryVertex"))printf("has SV TagInfo\n");
	/*
	if(jet.hasTagInfo("secondaryVertex")){
	  // printf("HasTagInfo\n");
	  float vertexmass = jet.tagInfoSecondaryVertex("secondaryVertex")->taggingVariables().get(reco::btau::vertexMass);
	  //float vertexmass = jet.tagInfoTrackIP("trackIP")->taggingVariables().get(reco::btau::vertexMass);
	  printf("vertexMass:%f-------------------------------------------------------\n",vertexmass);
	}
	*/
	float pt=0.0;
	float sumPt=0.0;
	float sumPt2=0.0;
	float maxpt=0.0;
	float nTrack = 0.0;
	reco::PFCandidatePtr highptpfcand;
	reco::PFCandidatePtr pfcand;
	reco::PFCandidatePtr pfcandMuon1;
	reco::PFCandidatePtr pfcandMuon2;
	bool charged = false;
	bool muon1found;
	bool muon2found;
	float muonpt1 = 0;
	float muonpt2 = 0;
	float maxPFdist = 0;
	float Mu1ZMasstemp=0;
	float Mu1ZMass =0;
	float Mu2ZMasstemp=0;
	float Mu2ZMass =0;
	int pdgid = 0;
	float dxy =0;
	float dz = 0;

	std::vector<reco::PFCandidatePtr> chargedParticles;
	std::vector<reco::PFCandidatePtr> muons;
	std::vector<reco::PFCandidatePtr> elecs;
	int t = 0; ///number of charged particles
	for(unsigned int j=0;j<jet.getPFConstituents().size();++j) {
	  pt = jet.getPFConstituents().at(j)->pt();
	  pdgid = jet.getPFConstituents().at(j)->pdgId();

	  if(ROOT::Math::VectorUtil::DeltaR(jet.p4(),jet.getPFConstituents().at(j)->p4())>maxPFdist){
	    maxPFdist = ROOT::Math::VectorUtil::DeltaR(jet.p4(),jet.getPFConstituents().at(j)->p4());
	  }

	  pfcand = jet.getPFConstituents().at(j);
	  sumPt+=pt;
	  sumPt2+=pt*pt;
	  if(pt>maxpt){
	    maxpt = pt;
	    if(jet.getPFConstituents().at(j)->charge()!=0){
	      highptpfcand = jet.getPFConstituents().at(j);
	      charged = true;
	    }
	  }
	if(abs(pfcand->pdgId())==211&&pfcand->pt()>1){
	  t = t+1;
	  chargedParticles.push_back(pfcand);
	  
	}
	
	/*
	if(abs(pfcand->pdgId())==13){
	  muons.push_back(pfcand);
	}

	if(abs(pfcand->pdgId())==11&&pfcand->pt()>1){
	  elecs.push_back(pfcand);
	}
	*/

	if(pfcand->trackRef().isNonnull())
	  nTrack +=1;
	  
	  if(abs(pfcand->pdgId())==13){
	    if(pfcand->pt()>muonpt1){
	      if(pfcandMuon1.isNonnull())
		pfcandMuon2 = pfcandMuon1;

	      muon1found = true;
	      pfcandMuon1 = jet.getPFConstituents().at(j);
	      muonpt1 = pfcandMuon1->pt();

	      if(pfcandMuon2.isNonnull())
		muonpt2 = pfcandMuon2->pt();
	      muon2found = true;
	    }
	    else if(pfcand->pt()>muonpt2&&pfcand->pt()<muonpt1){
	      pfcandMuon2 = jet.getPFConstituents().at(j);
	      muonpt2 = pfcandMuon2->pt();
	    }
	  }
	}
	/*
	////adding D meson Code Here--> Take Vector of particles and loop
	double massD0 = 0;
	math::PtEtaPhiMLorentzVector D0;
	if(jet.pt()>20&&chargedParticles.size()>1)
	  for(unsigned int k = 0; k<chargedParticles.size()-1;k++)
	    for(unsigned int j = k+1; j<chargedParticles.size();j++)
	      if(chargedParticles.at(k)->charge()+chargedParticles.at(j)->charge()==0){
		//printf("chargedparticles size %i\n",(int)chargedParticles.size());
		math::PtEtaPhiMLorentzVector kaon(chargedParticles.at(k)->pt(),
						  chargedParticles.at(k)->eta(),
						  chargedParticles.at(k)->phi(),
						  0.494);
		math::PtEtaPhiMLorentzVector pion(chargedParticles.at(j)->pt(),
						  chargedParticles.at(j)->eta(),
						  chargedParticles.at(j)->phi(),
						  0.140);
		
		if(chargedParticles.at(k)->charge()>0){
		  pion =math::PtEtaPhiMLorentzVector(chargedParticles.at(k)->pt(),
						     chargedParticles.at(k)->eta(),
						     chargedParticles.at(k)->phi(),
						     0.140);
		  kaon =math::PtEtaPhiMLorentzVector(chargedParticles.at(j)->pt(),
						     chargedParticles.at(j)->eta(),
						     chargedParticles.at(j)->phi(),
						     0.494);
		}
		D0 = pion+kaon;
		double mass = (pion+kaon).M();

		if(fabs(mass-1.864)<fabs(massD0-1.864)){
		  massD0 = mass;
		}
	      }
	jet.addUserFloat("massD0",massD0);
	*/
	//////////////costructing Dpm
	/*
	double massDp = 0;
	math::PtEtaPhiMLorentzVector Dp;
	if(jet.pt()>20&&chargedParticles.size()>1)
	  for(unsigned int k = 0; k<chargedParticles.size()-1;k++)
	    for(unsigned int j = k+1; j<chargedParticles.size();j++)
	      if(chargedParticles.at(k)->charge()+chargedParticles.at(j)->charge()==0){
		//printf("chargedparticles size %i\n",(int)chargedParticles.size());
		math::PtEtaPhiMLorentzVector kaon(chargedParticles.at(k)->pt(),
						  chargedParticles.at(k)->eta(),
						  chargedParticles.at(k)->phi(),
						  0.494);
		math::PtEtaPhiMLorentzVector pion(chargedParticles.at(j)->pt(),
						  chargedParticles.at(j)->eta(),
						  chargedParticles.at(j)->phi(),
						  0.140);
		
		if(chargedParticles.at(k)->charge()>0){
		  pion =math::PtEtaPhiMLorentzVector(chargedParticles.at(k)->pt(),
						     chargedParticles.at(k)->eta(),
						     chargedParticles.at(k)->phi(),
						     0.140);
		  kaon =math::PtEtaPhiMLorentzVector(chargedParticles.at(j)->pt(),
						     chargedParticles.at(j)->eta(),
						     chargedParticles.at(j)->phi(),
						     0.494);
		}
		D0 = pion+kaon;
		double mass = (pion+kaon).M();

		if(fabs(mass-1.864)<fabs(massD0-1.864)){
		  massD0 = mass;
		}
	      }
	printf("Gets Here5\n");	
	jet.addUserFloat("massD0",massD0);
	*/
	///////////finish constructing Dpm
	/*
	double massBpm = 0;
	if(jet.pt()>20&&chargedParticles.size()>1&&muons.size()>0)
	  for(unsigned int k = 0; k<muons.size();k++){

	    math::PtEtaPhiMLorentzVector muon(chargedParticles.at(k)->pt(),
					      chargedParticles.at(k)->eta(),
					      chargedParticles.at(k)->phi(),
					      0.105);
	    double mass = (D0+muon).M();

	    if(fabs(mass-5.279)<fabs(massBpm-5.279))
	      massBpm = mass;
	  }

	jet.addUserFloat("massBpm",massBpm);

	double massBpmElecs = 0;
	if(jet.pt()>20&&chargedParticles.size()>1&&elecs.size()>0)
	  for(unsigned int k = 0; k<elecs.size();k++){

	    math::PtEtaPhiMLorentzVector elec(chargedParticles.at(k)->pt(),
					       chargedParticles.at(k)->eta(),
					       chargedParticles.at(k)->phi(),
					       0.000511);
	    double mass = (D0+elec).M();

	    if(fabs(mass-5.279)<fabs(massBpmElecs-5.279))
	      massBpmElecs = mass;
	  }

	jet.addUserFloat("massBpmElecs",massBpmElecs);
	*/
	if(iEvent.getByLabel(leptons_,leptons)){
	  for(unsigned int k =0; k!=leptons->size();k++){

	    if(pfcandMuon1.isNonnull()){
	      Mu1ZMasstemp=(pfcandMuon1->p4()+leptons->at(k).p4()).M();
	      if(Mu1ZMasstemp>Mu1ZMass)
		Mu1ZMass = Mu1ZMasstemp;
	    }
	    
	    if(pfcandMuon2.isNonnull()){
	      Mu1ZMasstemp=(pfcandMuon2->p4()+leptons->at(k).p4()).M();
	      if(Mu2ZMasstemp>Mu2ZMass)
		Mu2ZMass = Mu2ZMasstemp;
	    }
	  }
	}

	if(pfcandMuon1.isNonnull()){
	  //printf("Gets to boost\n");
	  TLorentzVector muVec(pfcandMuon1->p4().px(),pfcandMuon1->p4().py(),pfcandMuon1->p4().pz(),pfcandMuon1->energy());
	  //printf("muVecPt %f\n",muVec.Pt());
	  TLorentzVector jet2(jet.px(),jet.py(),jet.pz());
	  double jetpx=-jet.px();
	  double jetpy=-jet.py();
	  double jetpz=-jet.pz();
	  //printf("jetpx: %f jetpy: %f jetpz: %f\n",jetpx,jetpy,jetpz);
	  muVec.Boost(-jet2.BoostVector());
	  //printf("after muVecPt %f\n",muVec.Px());
	  jet.addUserFloat("Mu1Boost",muVec.Pt());
	}

	if(pfcandMuon2.isNonnull()){
	  TLorentzVector muVec(pfcandMuon2->p4().px(),pfcandMuon2->p4().py(),pfcandMuon2->p4().pz(),pfcandMuon2->energy());
	  muVec.Boost(-jet.px(),-jet.py(),-jet.pz());
	  jet.addUserFloat("Mu2Boost",muVec.P());
	}

	/*	
	if(pfcandMuon1->trackRef().isNonnull()&&pfcandMuon2->trackRef().isNonnull()){
	  if(pfcandMuon1->trackRef()->pt()<pfcandMuon2->trackRef()->pt()){
	    reco::PFCandidatePtr pfcandMuon1dupe = pfcandMuon1;
	    pfcandMuon1 = pfcandMuon2;
	    pfcandMuon2 = pfcandMuon1dupe;
	  }
	}
	*/
	//printf("Gets Here3\n");	
	  if(verticesExist&&maxpt>0&&charged) {
	    if(highptpfcand->trackRef().isNonnull()){
	      dxy = highptpfcand->trackRef()->dxy(vertices->at(0).position());
	      jet.addUserFloat("dxy",dxy);
	      dz = highptpfcand->trackRef()->dz(vertices->at(0).position());
	      jet.addUserFloat("dz",dz);
	    }
	    dxy = 0;
	    dz = 0;
	    //printf("Gets Here41\n");
	    if(pfcandMuon1.isNonnull())
	      if(pfcandMuon1->trackRef().isNonnull()&&verticesExist&&muon1found)
		if(pfcandMuon1->charge()!=0){
		  //printf("Gets Here43\n");
		  dxy = pfcandMuon1->trackRef()->dxy(vertices->at(0).position());

		  jet.addUserFloat("dxyMu1",dxy);

		  dz = pfcandMuon1->trackRef()->dz(vertices->at(0).position());
		  jet.addUserFloat("dzMu1",dz);
		}

	    dxy = 0;
	    dz = 0;
	    if(pfcandMuon2.isNonnull())
	      if(pfcandMuon2->trackRef().isNonnull()&&verticesExist&&muon2found&&pfcandMuon2->pt()>0)
		if(pfcandMuon2->charge()!=0){
		  dxy = pfcandMuon2->trackRef()->dxy(vertices->at(0).position());
		  jet.addUserFloat("dxyMu2",dxy);
		  dz = pfcandMuon2->trackRef()->dz(vertices->at(0).position());
		  jet.addUserFloat("dzMu2",dz);
	     }
	  }
        double mass_PV = -777; 
        double pt_PV = -777; 
        double eta_PV = -777; 
        double phi_PV = -777; 
        mass_PV = vertices->at(0).p4().M();
        pt_PV = vertices->at(0).p4().Pt();
        eta_PV = vertices->at(0).p4().Eta();
        phi_PV = vertices->at(0).p4().Phi();
        //std::cout<<"PV "<<mass_PV<<" "<<pt_PV<<" "<<eta_PV<<" "<<phi_PV<<std::endl;
	jet.addUserFloat("muon1ZMass",Mu1ZMass);
	jet.addUserFloat("muon2ZMass",Mu2ZMass);
	jet.addUserFloat("muon1pt",muonpt1);
	jet.addUserFloat("muon2pt",muonpt2);
	jet.addUserFloat("nTracks",nTrack);
	jet.addUserFloat("DR",maxPFdist);
	jet.addUserFloat("ptRMS",sqrt(sumPt2/(sumPt*sumPt)));
        jet.addUserFloat("mass_PV",mass_PV); 
        jet.addUserFloat("pt_PV",pt_PV); 
        jet.addUserFloat("eta_PV",eta_PV); 
        jet.addUserFloat("phi_PV",phi_PV); 
	jets->push_back(jet);
      }
    iEvent.put(jets);
  } 
  
      // ----------member data ---------------------------
  edm::InputTag src_;
  edm::InputTag leptons_;
  edm::InputTag vertex_;
};

