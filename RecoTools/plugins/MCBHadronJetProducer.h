// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/Math/interface/Vector3D.h"
#include "DataFormats/PatCandidates/interface/Jet.h"
#include "DataFormats/JetReco/interface/PFJet.h"

#include "DataFormats/ParticleFlowCandidate/interface/PFCandidate.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "DataFormats/Math/interface/angle.h"

// Math
#include "Math/GenVector/VectorUtil.h"

//#include "AnalysisDataFormats/BAnalysis/interface/SimBHadron.h"
//#include "AnalysisDataFormats/BAnalysis/interface/SimSecondaryVertex.h"

#include "ZSV/BAnalysis/interface/SimBHadron.h"
#include "ZSV/BAnalysis/interface/SimSecondaryVertex.h"

//
// class declaration
//

class MCBHadronJetProducer : public edm::EDProducer {

  typedef std::set<int>::const_iterator intsetit;
  typedef SimBHadronCollection::iterator SBHit;
  typedef std::set<const reco::Candidate *>::iterator candsetit; 


  public: 
  
   explicit MCBHadronJetProducer(const edm::ParameterSet& iConfig):
     src_(iConfig.getParameter<edm::InputTag>("src"))
     { 
       produces<pat::JetCollection>(); 
       produces<SimBHadronCollection>(); 

     }     
  


  ~MCBHadronJetProducer() 
     { 

    // do anything here that needs to be done at desctruction time  
    // (e.g. close files, deallocate resources etc.)  

     } 
 private: 


  // ------------ method called to produce the data  ------------  
  virtual void produce(edm::Event& iEvent, const edm::EventSetup& iSetup) 
  {
    noEvent++;  
    //std::cout << "MCB Hadron Proucer " << std::endl;  
    using namespace edm;  
    using namespace reco;  
    std::auto_ptr<pat::JetCollection> jets(new pat::JetCollection);  
    std::auto_ptr<GenParticleCollection> genBs (new GenParticleCollection);
    std::auto_ptr<GenParticleCollection> genCs (new GenParticleCollection);
    Handle<pat::JetCollection > cands;  
    
    //output collection  
    SimBHadronCollection * output = new SimBHadronCollection();  
    SimBHadronCollection * output2 = new SimBHadronCollection();  


   /////////////////////////////////////////////  
    //--------------GenParticles  
    Handle<GenParticleCollection> GPCollection;  
    if(iEvent.getByLabel("genParticles", GPCollection)){  
      const GenParticleCollection & gpc = *(GPCollection.product());  
      //      
      //printf("gets here3\n");
      for(unsigned int i=0; i<gpc.size(); i++){  
	int pdgid = gpc[i].pdgId();  
	int pdid = abs(pdgid);  
	if(((pdid/100)==5 || (pdid/1000)==5) && ((pdid%10)==1 || (pdid%10)==2 )) {  

	  if((*output).size()>0) removeMothers(gpc[i], *output);
	  
	  SimBHadron sbh(gpc[i]); 
	  sbh.decPosition.SetXYZ((*gpc[i].daughter(0)).vx(),(*gpc[i].daughter(0)).vy(),(*gpc[i].daughter(0)).vz());

	  //printf("decay position x %f PDGID: %i\n",(*gpc[i].daughter(0)).vx(),(*gpc[i].daughter(0)).pdgId());
	  genBs->push_back(gpc[i]);
	  setMoDauQuantities(gpc[i], sbh);
	  output->push_back(sbh);
	}


	if(pdid==411||pdid==421||pdid==431||pdid==413) {  
	  if((*output2).size()>0) removeMothers(gpc[i], *output2);
	  SimBHadron sbh2(gpc[i]); 
  	  //printf("decay position x %f PDGID: %i\n",(*gpc[i].daughter(0)).vx(),(*gpc[i].daughter(0)).pdgId());
	  genCs->push_back(gpc[i]);
	  setMoDauQuantities(gpc[i], sbh2);
	  output2->push_back(sbh2);

	}


      }
    }
 
    if(iEvent.getByLabel(src_,cands)) {
      for(unsigned int  i=0;i!=cands->size();++i){
	//printf("Gets Here1.0\n");
	pat::Jet jet = cands->at(i);
	int nMb05 = 0;
	int nMb1 = 0;
	int nMc05 = 0;
	int nMc1 = 0;
	for(unsigned int k=0; k!=genBs->size();k++){
	  //printf("gen pt %f pdgID: %i\n",genBs->at(k).pt(),genBs->at(k).pdgId());
	  if(ROOT::Math::VectorUtil::DeltaR(jet.p4(),genBs->at(k).p4())<0.5){
	    nMb05 += 1;
	    //printf("nMb: %i--------jetpt: %f eta: %f  idloose: %f fullidloose: %i\n",nMb,jet.pt(),jet.eta(),jet.userFloat("idLoose"),jet.userInt("fullIdLoose"));
	    //abs(eta)<5.0&&userFloat("idLoose")>0&&pt>10&&userInt("fullIdLoose")>0
	  }
	  if(ROOT::Math::VectorUtil::DeltaR(jet.p4(),genBs->at(k).p4())<1){
	    nMb1 += 1;
	    //printf("nMb: %i--------jetpt: %f eta: %f  idloose: %f fullidloose: %i\n",nMb,jet.pt(),jet.eta(),jet.userFloat("idLoose"),jet.userInt("fullIdLoose"));
	    //abs(eta)<5.0&&userFloat("idLoose")>0&&pt>10&&userInt("fullIdLoose")>0
	  }
	}
	for(unsigned int k=0; k!=genCs->size();k++){
	  //printf("gen pt %f pdgID: %i\n",genBs->at(k).pt(),genBs->at(k).pdgId());
	  if(ROOT::Math::VectorUtil::DeltaR(jet.p4(),genCs->at(k).p4())<0.5){
	    nMc05 += 1;
	    //printf("nMb: %i--------jetpt: %f eta: %f  idloose: %f fullidloose: %i\n",nMb,jet.pt(),jet.eta(),jet.userFloat("idLoose"),jet.userInt("fullIdLoose"));
	    //abs(eta)<5.0&&userFloat("idLoose")>0&&pt>10&&userInt("fullIdLoose")>0
	  }
	  if(ROOT::Math::VectorUtil::DeltaR(jet.p4(),genCs->at(k).p4())<1){
	    nMc1 += 1;
	    //printf("nMb: %i--------jetpt: %f eta: %f  idloose: %f fullidloose: %i\n",nMb,jet.pt(),jet.eta(),jet.userFloat("idLoose"),jet.userInt("fullIdLoose"));
	    //abs(eta)<5.0&&userFloat("idLoose")>0&&pt>10&&userInt("fullIdLoose")>0
	  }
	}
	jet.addUserFloat("nMatchedc05",nMc05);
	jet.addUserFloat("nMatchedc1",nMc1);

	jet.addUserFloat("nMatchedb05",nMb05);
	jet.addUserFloat("nMatchedb1",nMb1);

	jets->push_back(jet);
      }
      
    }
    
    //std::cout << "number of b " << output->size() << std::endl;
    std::auto_ptr<SimBHadronCollection> pOut(output);
    iEvent.put(jets);
    iEvent.put(pOut);
  }
  
   
     void removeMothers(const reco::Candidate &gp, SimBHadronCollection &out){
       for(SBHit it = out.begin(); it != out.end(); it++){
	 if(gp.p4()==(*it).p4()) {
	   //int t3 = (*it).pdgId();
	   SBHit temp = it;
	   out.erase(temp);
	   it--;
	   //std::cout << "removed " << t3 << " B hadron from output\n";
	 }
       }
       if(gp.status() != 3){
	 for(unsigned int m=0; m<gp.numberOfMothers(); m++) {
	   removeMothers((*gp.mother(m)), out);
	 }
       }
     }
     
     void setMoDauQuantities(reco::GenParticle gp, SimBHadron &bh){
       //This function is buggy, it make a mess on single top
       
       bh.quarkstatus = -1;
       bh.brotherstatus = -1;
       
       std::set<const reco::Candidate *> bquarks; 
       findbquarks(gp, bquarks);
       int id2 = gp.pdgId(); 
       bool bmes = false; 
       if(id2/1000==0) bmes = true;
       if(bquarks.size()>1){
	 for(candsetit it = bquarks.begin(); it !=bquarks.end(); it++){
	   int id1 = (*it)->pdgId();
	   //same sign 
	   if(id1/abs(id1)==id2/abs(id2)){
	     if(bmes){
	   //remove
	       candsetit temp = it;
	       it--;
	       bquarks.erase(temp);
	     }
	   }
	   else{
	     if(!bmes){
	       //remove
	       candsetit temp = it;
	       it--;
	       bquarks.erase(temp);
	     }
	   }
	 }
       }
       if(bquarks.size()!=1) {
	 std::cout << "MORE THAN ONE B/BBAR!!!\n";
       }
       else{
	 candsetit it = bquarks.begin();
	 bh.quarkstatus = (*it)->status(); 
	 for(unsigned int m=0; m<(*it)->numberOfMothers(); m++){
	   bh.motherids.push_back((*it)->mother(m)->pdgId());
	   //printf("Mother ID: %i\n",(*it)->mother(m)->pdgId());
	   
	 }
	 if((*it)->numberOfMothers()>0){
	   for(unsigned int d=0; d<((*it)->mother())->numberOfDaughters(); d++){
	     int id1 = ((*it)->mother())->daughter(d)->pdgId();
	     if(abs(id1)==5 && ((*it)->mother())->daughter(d)->p4() != (*it)->p4()){
	       if(id1!=(*it)->pdgId()) bh.brotherstatus = ((*it)->mother())->daughter(d)->status();
	     }
	   }
	 }
       }
       
       
     }


     void findbquarks(const reco::Candidate &gp, std::set<const reco::Candidate *> &set){
       for(unsigned int m=0; m<gp.numberOfMothers(); m++){
	 if(abs((*gp.mother(m)).pdgId())==5) {
	   //const reco::Candidate *temp = gp.mother(m);
	   bool hasbmother = false;
	   for(unsigned int m1=0; m1<(*gp.mother(m)).numberOfMothers(); m1++){
	     if(abs((*(*gp.mother(m)).mother(m1)).pdgId())==5) hasbmother = true;
	   }
	   if(!hasbmother) set.insert(gp.mother(m));
	 }
	 if((*gp.mother(m)).status()!=3 || (*gp.mother(m)).pdgId()!=2212) findbquarks((*gp.mother(m)), set);
       }
     } 
 

 private:
 int noEvent;
 edm::InputTag src_;
};
