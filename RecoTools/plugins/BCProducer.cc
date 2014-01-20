#include <memory>

#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/ESHandle.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "DataFormats/GeometryVector/interface/GlobalVector.h"
#include "DataFormats/Candidate/interface/LeafCandidate.h"
#include "DataFormats/TrackReco/interface/Track.h"
#include "DataFormats/TrackReco/interface/TrackFwd.h"
#include "RecoBTag/SecondaryVertex/interface/SecondaryVertex.h"
#include "DataFormats/JetReco/interface/Jet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "UWAnalysis/DataFormats/interface/BCandFinalState.h"

#include <TLorentzVector.h>
class BCProducer : public edm::EDProducer {
   public:
      explicit BCProducer(const edm::ParameterSet&);
      ~BCProducer();

   private:
      virtual void beginJob();
      virtual void produce(edm::Event&, const edm::EventSetup&);
      virtual void endJob();
      GlobalVector flightDirection(reco::Vertex &, reco::Vertex &);
      void addTracks(std::set<reco::TrackRef> &, reco::Vertex &, double);	
      edm::InputTag vertexsrc_,offlinePrimaryVertices_,PFJet_;	
      BCandFinalState BCFS;
};

BCProducer::BCProducer(const edm::ParameterSet& iConfig):
  vertexsrc_(iConfig.getParameter<edm::InputTag>("src")),
  offlinePrimaryVertices_(iConfig.getParameter<edm::InputTag>("primaryVertices")),
  PFJet_(iConfig.getParameter<edm::InputTag>("jetSource"))
{
// produces<std::vector<reco::LeafCandidate> >();
produces<BCandFinalStateCollection>("BCandFinalState");
}


BCProducer::~BCProducer()
{}

void BCProducer::produce(edm::Event& iEvent, const edm::EventSetup& iSetup) {
	BCFS.BC1PT(-777);
        BCFS.BC2PT(-777);
        BCFS.BC1ETA(-777);
        BCFS.BC2ETA(-777);
        BCFS.BC1PHI(-777);
        BCFS.BC2PHI(-777);
        BCFS.BC1nTracks(-777);
        BCFS.BC2nTracks(-777);
        BCFS.BCEnergySum(-777);
        BCFS.nJetAssociatedToBC1(-777);
        BCFS.nJetAssociatedToBC2(-777);
        BCFS.Jet1BC1PT(-777);
        BCFS.Jet2BC1PT(-777);
        BCFS.Jet3BC1PT(-777);
        BCFS.Jet4BC1PT(-777);
        BCFS.Jet1BC1ETA(-777);
        BCFS.Jet2BC1ETA(-777);
        BCFS.Jet3BC1ETA(-777);
        BCFS.Jet4BC1ETA(-777);
        BCFS.Jet1BC1PHI(-777);
        BCFS.Jet2BC1PHI(-777);
        BCFS.Jet3BC1PHI(-777);
        BCFS.Jet4BC1PHI(-777);
        BCFS.Jet1BC2PT(-777);
        BCFS.Jet2BC2PT(-777);
        BCFS.Jet3BC2PT(-777) ;
        BCFS.Jet4BC2PT(-777);
        BCFS.Jet1BC2ETA(-777);
        BCFS.Jet2BC2ETA(-777);
        BCFS.Jet3BC2ETA(-777);
        BCFS.Jet4BC2ETA(-777);
        BCFS.Jet1BC2PHI(-777);
        BCFS.Jet2BC2PHI(-777);
        BCFS.Jet3BC2PHI(-777);
        BCFS.Jet4BC2PHI(-777);
        BCFS.BCDeltaR(-777);
        BCFS.BDeltaPHI(-777);
	BCFS.BC1MASS(-777);
	BCFS.BC2MASS(-777);
	//std::cout<<"In BCProducer"<<std::endl;
	// std::vector<reco::LeafCandidate> *blc = new std::vector<reco::LeafCandidate>;
	
	std::auto_ptr<BCandFinalStateCollection> BCandFS(new BCandFinalStateCollection);
	
	//Getting the PV collection
	edm::Handle<reco::VertexCollection> primaryVertexCollection;
	iEvent.getByLabel(offlinePrimaryVertices_, primaryVertexCollection);
	const reco::VertexCollection pvc = *(primaryVertexCollection.product());
	
	//Getting the PFJetCollection
	edm::Handle<edm::View<reco::Jet> > inputJets;
	  iEvent.getByLabel(PFJet_, inputJets);	
	
	//Getting the Bcand collection (reco::Vertex)
	edm::Handle<std::vector<reco::Vertex> > SVC;
	iEvent.getByLabel(vertexsrc_, SVC);
	const std::vector<reco::Vertex> svc = *(SVC.product());
	//Define pv from the first PV (ordered by sum of track pt)
	reco::Vertex pv = pvc[0];
	//std::cout<<"PV x="<<pv.x()<<" y="<<pv.y()<<" z="<<pv.z()<<std::endl;
	std::vector<std::set<reco::TrackRef> > bCandtrackSets;
	float charge=0;	
	//std::cout<<"Running on SV, size="<<svc.size()<<std::endl;
	int nSV=0;
	int nJets=0;
	TLorentzVector TLV_jet[100];
	for(unsigned int j=0; j<100; j++){
	         TLV_jet[j].SetPxPyPzE(0,0,0,0);
       	}
	for(edm::View<reco::Jet>::const_iterator jet = inputJets->begin(); jet!=inputJets->end(); ++jet){
		if(jet->pt()>15){
                	TLV_jet[nJets].SetPtEtaPhiM(jet->pt(),jet->eta(),jet->phi(),jet->mass());
			nJets++;
		}
        }
	int index[nJets];
	for(int j=0; j<nJets; j++){index[j]=0;}	
		//Running on BCandidate collection to associate a LeafCandidate to each of them (actually building a new collection, 100% correlated with the BCandidate one).
	for(unsigned int i=0; i<svc.size(); i++){
		//std::cout<<"---> SV "<<i<<" x="<<svc[i].x()<<" y="<<svc[i].y()<<" z="<<svc[i].z()<<std::endl;
		math::XYZTLorentzVectorD bCandmom;
		bCandmom = svc[i].p4(0.13957,0.5);	
		reco::Vertex::Point p(svc[i].x(),svc[i].y(),svc[i].z());
		std::set<reco::TrackRef> bCandtracks;
		addTracks(bCandtracks, (reco::Vertex&) svc[i], 0.5);
		TLorentzVector SumFourVec;	
		for(std::set<reco::TrackRef>::const_iterator it=bCandtracks.begin(); it!=bCandtracks.end(); it++){
			charge += (*it)->charge();
			TLorentzVector FourVec;
			FourVec.SetPtEtaPhiM((*it)->pt(),(*it)->eta(),(*it)->phi(),0.135);
			SumFourVec+=FourVec;
		}
		reco::LeafCandidate lc(charge, bCandmom, p,0);
		float sumEnergy=0;
		int nJetAssociated=0;	
		if(nSV==0){
			BCFS.BC1nTracks(bCandtracks.size());
			BCFS.BC1MASS(SumFourVec.M());
                	BCFS.BC1PT(lc.pt());
                 	BCFS.BC1ETA(lc.eta());
                 	BCFS.BC1PHI(lc.phi());
			// Running jets to count the total energy associated to the first b-hadron
			for(int j=0; j<nJets; j++){
				if(index[j]==0){
                                	float dEtaBJ=fabs(TLV_jet[j].Eta()-lc.eta());
					float dPhiBJ=fabs(TLV_jet[j].Phi()-lc.phi())?fabs(TLV_jet[j].Phi()-lc.phi()):6.2831-fabs(TLV_jet[j].Phi()-lc.phi());
					float dRBJ=sqrt(pow(dEtaBJ,2)+pow(dPhiBJ,2));
	                                 if(dRBJ<0.5){
						sumEnergy+=TLV_jet[j].E();
						index[j]=1;
						if(nJetAssociated==0)BCFS.Jet1BC1PT(TLV_jet[j].Pt());BCFS.Jet1BC1ETA(TLV_jet[j].Eta());BCFS.Jet1BC1ETA(TLV_jet[j].Phi());
                                                if(nJetAssociated==1)BCFS.Jet2BC1PT(TLV_jet[j].Pt());BCFS.Jet2BC1ETA(TLV_jet[j].Eta());BCFS.Jet2BC1ETA(TLV_jet[j].Phi());
                                                if(nJetAssociated==2)BCFS.Jet3BC1PT(TLV_jet[j].Pt());BCFS.Jet3BC1ETA(TLV_jet[j].Eta());BCFS.Jet3BC1ETA(TLV_jet[j].Phi());
                                                if(nJetAssociated==3)BCFS.Jet4BC1PT(TLV_jet[j].Pt());BCFS.Jet4BC1ETA(TLV_jet[j].Eta());BCFS.Jet4BC1ETA(TLV_jet[j].Phi());

						nJetAssociated++;	
					}
				}
                        }
			BCFS.nJetAssociatedToBC1(nJetAssociated);
		}
		nJetAssociated=0;
		if(nSV==1){
			BCFS.BC2nTracks(bCandtracks.size());
			BCFS.BC2MASS(SumFourVec.M());
                        BCFS.BC2PT(lc.pt());
                        BCFS.BC2ETA(lc.eta());
                        BCFS.BC2PHI(lc.phi());
			BCFS.BCEnergySum();
			float dphi=fabs(BCFS.BC1PHI()-BCFS.BC2PHI())<3.14159?fabs(BCFS.BC1PHI()-BCFS.BC2PHI()):6.28318-fabs(BCFS.BC1PHI()-BCFS.BC2PHI());
			BCFS.BDeltaPHI(dphi);
			if(sqrt(pow(BCFS.BC1ETA()-BCFS.BC2ETA(),2)+pow(BCFS.BDeltaPHI(),2))>0.7102 && sqrt(pow(BCFS.BC1ETA()-BCFS.BC2ETA(),2)+pow(BCFS.BDeltaPHI(),2))<0.71032){
			//std::cout<<sqrt(pow(BCFS.BC1ETA()-BCFS.BC2ETA(),2)+pow(BCFS.BDeltaPHI(),2))<<" ************************************DOUBLECOUNTING****************"<<std::endl;
			}
                	BCFS.BCDeltaR(sqrt(pow(BCFS.BC1ETA()-BCFS.BC2ETA(),2)+pow(BCFS.BDeltaPHI(),2)));
			// Running jets to count the total energy associated to the second b-hadron
			for(int j=0; j<nJets; j++){
				if(index[j]==0){
                	  		float dEtaBJ=fabs(TLV_jet[j].Eta()-lc.eta());
                	  		float dPhiBJ=fabs(TLV_jet[j].Phi()-lc.phi())?fabs(TLV_jet[j].Phi()-lc.phi()):6.2831-fabs(TLV_jet[j].Phi()-lc.phi());
                	  		float dRBJ=sqrt(pow(dEtaBJ,2)+pow(dPhiBJ,2));
                	  		if(dRBJ<0.5){
						sumEnergy+=TLV_jet[j].E();
						index[j]=1;
						if(nJetAssociated==0)BCFS.Jet1BC2PT(TLV_jet[j].Pt());BCFS.Jet1BC2ETA(TLV_jet[j].Eta());BCFS.Jet1BC2ETA(TLV_jet[j].Phi());
                                                if(nJetAssociated==1)BCFS.Jet2BC2PT(TLV_jet[j].Pt());BCFS.Jet2BC2ETA(TLV_jet[j].Eta());BCFS.Jet2BC2ETA(TLV_jet[j].Phi());
                                                if(nJetAssociated==2)BCFS.Jet3BC2PT(TLV_jet[j].Pt());BCFS.Jet3BC2ETA(TLV_jet[j].Eta());BCFS.Jet3BC2ETA(TLV_jet[j].Phi());
                                                if(nJetAssociated==3)BCFS.Jet4BC2PT(TLV_jet[j].Pt());BCFS.Jet4BC2ETA(TLV_jet[j].Eta());BCFS.Jet4BC2ETA(TLV_jet[j].Phi());
						nJetAssociated++;
					}
				}
			}
			BCFS.nJetAssociatedToBC2(nJetAssociated);
                }
		BCFS.BCEnergySum(sumEnergy);
		nSV++;	
	}
	BCandFS->push_back(BCFS);	
	//std::cout<<"--->"<<sqrt(pow(BCFS.BC1ETA()-BCFS.BC2ETA(),2)+pow(BCFS.BDeltaPHI(),2))<<std::endl;	
      	std::auto_ptr<BCandFinalStateCollection > bfsColl(BCandFS);	
	iEvent.put(bfsColl,"BCandFinalState");	
}	

void BCProducer::addTracks(std::set<reco::TrackRef> &trackrefs, reco::Vertex &v, double weight){

  for(reco::Vertex::trackRef_iterator ti = v.tracks_begin(); ti!=v.tracks_end(); ti++){
    	if(v.trackWeight(*ti)>weight){
      		reco::TrackRef t = ti->castTo<reco::TrackRef>();
      		trackrefs.insert(t);
    	}

  }
}

GlobalVector BCProducer::flightDirection(reco::Vertex &pv, reco::Vertex &sv){
  GlobalVector res(sv.position().X() - pv.position().X(),sv.position().Y() - pv.position().Y(),sv.position().Z() - pv.position().Z());
  return res;
}

// ------------ method called once each job just before starting event loop ------------
void
BCProducer::beginJob()
{
 

}

// ------------ method called once each job just after ending the event loop ------------
void
BCProducer::endJob() {

}


DEFINE_FWK_MODULE(BCProducer);
