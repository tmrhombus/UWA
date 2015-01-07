/**
* @file PATmuonSFer.cc
* @author T.M.Perry
*/

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Utilities/interface/InputTag.h"

#include "Math/GenVector/VectorUtil.h"

#include "DataFormats/PatCandidates/interface/Muon.h"
#include "UWAnalysis/RecoTools/interface/table.h"

//#include "TFile.h"
//#include "TGraphAsymmErrors.h"
/**
* @class PATmuonSFer
* @brief embeds trigger/id scalefactors as userFloats
*/
class PATmuonSFer : public edm::EDProducer
{

    public:
        PATmuonSFer(const edm::ParameterSet& pset);
        virtual ~PATmuonSFer () {}
        void produce( edm::Event& iEvent, const edm::EventSetup& es );

    private:
        typedef reco::Candidate::LorentzVector FourVec;
        edm::InputTag src_;
};



PATmuonSFer::PATmuonSFer( const edm::ParameterSet& pset)
{
    src_ = pset.getParameter<edm::InputTag>("src");
    produces<pat::MuonCollection>();
}

void PATmuonSFer::produce( edm::Event& iEvent, const edm::EventSetup& es )
{

    table* SFtable_Iso;
    table* SFtable_ID;
    table* SFtable_HLT;
    std::string base = std::getenv("CMSSW_BASE");
    SFtable_Iso = new table(base+"/src/UWAnalysis/RecoTools/data/SF_muon_Iso.txt");
    SFtable_ID = new table(base+"/src/UWAnalysis/RecoTools/data/SF_muon_ID.txt");
    SFtable_HLT = new table(base+"/src/UWAnalysis/RecoTools/data/SF_muon_HLT.txt");

/*
    // Muon ID Eficiency   DATA_over_MC_Tight_eta_pt20-500  for each eta, mult by a factor
    edm::FileInPath fileID("UWAnalysis/Configuration/data/MuonEfficiencies_Run2012ReReco_53X.root");
    // Muon ISO Efficiency  DATA_over_MC_combRelIsoPF04dBeta<012_Tight_eta_pt20-500
    edm::FileInPath fileIS("UWAnalysis/Configuration/data/MuonEfficiencies_ISO_Run_2012ReReco_53X.root");
    // Muon Trigger Efficiency  IsoMu24_eta2p1_DATA_over_MC_TightID_ETA_pt25-500_2012ABCD
    edm::FileInPath fileTR("UWAnalysis/Configuration/data/SingleMuonTriggerEfficiencies_eta2p1_Run2012ABCD_v5trees.root");
    
    TFile *fID = new TFile(fileID.fullPath().c_str());
    TFile *fIS = new TFile(fileIS.fullPath().c_str());
    TFile *fTR = new TFile(fileTR.fullPath().c_str());
    
    TGraphAsymmErrors *gID = (TGraphAsymmErrors*)fID->Get("DATA_over_MC_Tight_eta_pt20-500");
    TGraphAsymmErrors *gIS = (TGraphAsymmErrors*)fIS->Get("DATA_over_MC_combRelIsoPF04dBeta<012_Tight_eta_pt20-500");
    TGraphAsymmErrors *gTR = (TGraphAsymmErrors*)fTR->Get("IsoMu24_eta2p1_DATA_over_MC_TightID_ETA_pt25-500_2012ABCD");

    //compositePtrCandidate.setEffWEIGHTeta_ID(weight_etaID);
    //compositePtrCandidate.setEffWEIGHTeta_IS(weight_etaIS);
    //compositePtrCandidate.setEffWEIGHTeta_TR(weight_etaTR);
*/

    std::auto_ptr<pat::MuonCollection> out( new pat::MuonCollection);
    edm::Handle<pat::MuonCollection> muons;
    if(iEvent.getByLabel(src_,muons))
      for(unsigned int i=0;i<muons->size();++i) {
        float SF_Iso = 1.;
        float SF_Iso_errUp = 0.;
        float SF_Iso_errDn = 0.;
        float SF_ID = 1.;
        float SF_ID_errUp = 0.;
        float SF_ID_errDn = 0.;
        float SF_HLT = 1.;
        float SF_HLT_errUp = 0.;
        float SF_HLT_errDn = 0.;
        float SF_total = 1.;
        float SF_total_errUp = 0.;
        float SF_total_errDn = 0.;
        pat::Muon muon = muons->at(i);

        float muon_pt  = muon.pt();
        float muon_eta = muon.eta();

/*
        SF_Iso = (float) gIS->Eval(muon_eta);
        SF_Iso_errUp = (float) gIS->Eval(muon_eta);
        SF_Iso_errDn = (float) gIS->Eval(muon_eta);
        SF_ID = (float) gID->Eval(muon_eta);
        SF_HLT = (float) gTR->Eval(muon_eta);
*/    

        SF_Iso = SFtable_Iso->Val(muon_pt,muon_eta);
        SF_Iso_errUp = SFtable_Iso->ErrUp(muon_pt,muon_eta);
        SF_Iso_errDn = SFtable_Iso->ErrDn(muon_pt,muon_eta);

        SF_ID = SFtable_ID->Val(muon_pt,muon_eta);
        SF_ID_errUp = SFtable_ID->ErrUp(muon_pt,muon_eta);
        SF_ID_errDn = SFtable_ID->ErrDn(muon_pt,muon_eta);

        SF_HLT = SFtable_HLT->Val(muon_pt,muon_eta);
        SF_HLT_errUp = SFtable_HLT->ErrUp(muon_pt,muon_eta);
        SF_HLT_errDn = SFtable_HLT->ErrDn(muon_pt,muon_eta);


        SF_total = SF_Iso * SF_ID * SF_HLT;
        SF_total_errUp = sqrt( pow(SF_Iso_errUp,2) + pow(SF_ID_errUp,2) + pow(SF_HLT_errUp,2) );
        SF_total_errDn = sqrt( pow(SF_Iso_errDn,2) + pow(SF_ID_errDn,2) + pow(SF_HLT_errDn,2) );

        //std::cout<<"RecoTools/plugins/PATmuonSFer.cc "
        //<<muon_pt<<" "<<muon_eta<<"\n "<<
        //"Iso: "<<SF_Iso<<"+"<<SF_Iso_errUp<<"-"<<SF_Iso_errDn<<"\n "<<
        //"ID: "<<SF_ID<<"+"<<SF_ID_errUp<<"-"<<SF_ID_errDn<<"\n "<<
        //"HLT:   "<<SF_HLT<<"+"<<SF_HLT_errUp<<"-"<<SF_HLT_errDn<<std::endl;

        muon.addUserFloat("SF_Iso",SF_Iso);
        muon.addUserFloat("SF_Iso_errUp",SF_Iso_errUp);
        muon.addUserFloat("SF_Iso_errDn",SF_Iso_errDn);
        muon.addUserFloat("SF_ID",SF_ID);
        muon.addUserFloat("SF_ID_errUp",SF_ID_errUp);
        muon.addUserFloat("SF_ID_errDn",SF_ID_errDn);
        muon.addUserFloat("SF_HLT",SF_HLT);
        muon.addUserFloat("SF_HLT_errUp",SF_HLT_errUp);
        muon.addUserFloat("SF_HLT_errDn",SF_HLT_errDn);
        muon.addUserFloat("SF_total",SF_total);
        muon.addUserFloat("SF_total_errUp",SF_total + SF_total_errUp);
        muon.addUserFloat("SF_total_errDn",SF_total - SF_total_errDn);
        out->push_back(muon);
    }

    iEvent.put( out );
    delete SFtable_Iso;
    delete SFtable_ID;
    delete SFtable_HLT;

    //delete fID;
    //delete fIS;
    //delete fTR;
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(PATmuonSFer);
