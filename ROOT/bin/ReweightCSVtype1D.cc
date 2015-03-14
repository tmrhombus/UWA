#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "PhysicsTools/Utilities/interface/Lumi3DReWeighting.h"
#include "PhysicsTools/Utilities/interface/LumiReWeighting.h"
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TH1D.h"
#include "TString.h"
#include "TMath.h"
#include "boost/filesystem.hpp"
#include <cstdlib>

// system include files
#include <memory>
#include <algorithm>
#include <TLorentzVector.h>
#include <string> 

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "DataFormats/PatCandidates/interface/Jet.h"

#include "Math/GenVector/VectorUtil.h"

#include "DataFormats/JetReco/interface/GenJet.h"
#include "DataFormats/JetReco/interface/GenJetCollection.h"
#include "DataFormats/Math/interface/deltaR.h"

void AddReweightBranches(
    TDirectory *dir, 
    optutl::CommandLineParser parser, 
    TString postfix, 
    TH1D* h_wgt_b[9][6],
    TH1D* h_wgt_c[5][6],
    TH1D* h_wgt_l[9][4][3] );

Float_t CalculateReweight(
    Float_t pt, 
    Float_t eta, 
    Float_t csv, 
    Int_t flavor,
    TH1D* h_wgt_b[9][6],
    TH1D* h_wgt_c[5][6],
    TH1D* h_wgt_l[9][4][3] );

int main (int argc, char* argv[]){
 optutl::CommandLineParser parser ("Does Type 1D CSV Reweighting");
 parser.addOption("filename",optutl::CommandLineParser::kString,"Name of File to be Reweighted","myfile");
 parser.addOption("postfix",optutl::CommandLineParser::kString,"Name of branch to be added","mybranch");
 parser.parseArguments (argc, argv);

    /* Fill vectors of histograms (systematics) */
    TString base = std::getenv("CMSSW_BASE");
    TString n_CSVwgt_HF = "/src/UWAnalysis/Configuration/data/csv_rwt_hf.root";
    TString n_CSVwgt_LF = "/src/UWAnalysis/Configuration/data/csv_rwt_lf.root";
    TFile *f_CSVwgt_HF = new TFile ( base + n_CSVwgt_HF );
    TFile *f_CSVwgt_LF = new TFile ( base + n_CSVwgt_LF );

    TH1D* h_wgt_b[9][6];
    TH1D* h_wgt_c[5][6];
    TH1D* h_wgt_l[9][4][3];

    for( int iSys=0; iSys<9; iSys++ ){
      std::string syst_csv_suffix_hf = "final";
      std::string syst_csv_suffix_c = "final";
      std::string syst_csv_suffix_lf = "final";

      switch( iSys ){
      case 0:  // this is the nominal case
        break;
      case 1:  // JESUp
        syst_csv_suffix_hf = "final_JESUp";
        syst_csv_suffix_lf = "final_JESUp";
        syst_csv_suffix_c  = "final_cErr1Up";
        break;
      case 2:  // JESDown
        syst_csv_suffix_hf = "final_JESDown";
        syst_csv_suffix_lf = "final_JESDown";
        syst_csv_suffix_c  = "final_cErr1Down";
        break;
      case 3:  // purity up
        syst_csv_suffix_hf = "final_LFUp";
        syst_csv_suffix_lf = "final_HFUp";
        syst_csv_suffix_c  = "final_cErr2Up";
        break;
      case 4:  // purity down
        syst_csv_suffix_hf = "final_LFDown";
        syst_csv_suffix_lf = "final_HFDown";
        syst_csv_suffix_c  = "final_cErr2Down";
        break;
      case 5:  // stats1 up
        syst_csv_suffix_hf = "final_Stats1Up";
        syst_csv_suffix_lf = "final_Stats1Up";
        break;
      case 6:  // stats1 down
        syst_csv_suffix_hf = "final_Stats1Down";
        syst_csv_suffix_lf = "final_Stats1Down";
        break;
      case 7:  // stats2 up
        syst_csv_suffix_hf = "final_Stats2Up";
        syst_csv_suffix_lf = "final_Stats2Up";
        break;
      case 8:  // stats2 down
        syst_csv_suffix_hf = "final_Stats2Down";
        syst_csv_suffix_lf = "final_Stats2Down";
        break;
      }

      std::string plot;
      for( int iPt=0; iPt<6; iPt++ ) {
       plot ="csv_ratio_Pt"+std::to_string(iPt)+"_Eta0_"+syst_csv_suffix_hf;
       h_wgt_b[iSys][iPt] = (TH1D*)f_CSVwgt_HF->Get( (TString)plot );
      }

      if( iSys<5 ){
        for( int iPt=0; iPt<6; iPt++ ) {
          plot = "c_csv_ratio_Pt"+std::to_string(iPt)+"_Eta0_"+syst_csv_suffix_c;
          h_wgt_c[iSys][iPt] = (TH1D*)f_CSVwgt_HF->Get( (TString)plot );
        }
      }

      for( int iPt=0; iPt<4; iPt++ ){
        for( int iEta=0; iEta<3; iEta++ ) {
          plot = "csv_ratio_Pt"+std::to_string(iPt)+"_Eta"+std::to_string(iEta)+"_"+syst_csv_suffix_lf;
          h_wgt_l[iSys][iPt][iEta] = (TH1D*)f_CSVwgt_LF->Get( (TString)plot );
        }
      }
    }

   TString filename = parser.stringValue("filename");
   TString postfix = parser.stringValue("postfix");
   std::cout<<filename<<std::endl;
   std::cout<<postfix<<std::endl;

   TFile *thefile = new TFile(filename,"UPDATE");

   AddReweightBranches(thefile,parser,postfix,h_wgt_b,h_wgt_c,h_wgt_l);

   thefile->Close();
}


void AddReweightBranches(
    TDirectory *dir, 
    optutl::CommandLineParser parser, 
    TString postfix, 
    TH1D* h_wgt_b[9][6],
    TH1D* h_wgt_c[5][6],
    TH1D* h_wgt_l[9][4][3] ){

 TDirectory *dirsav = gDirectory;
 TIter next(dir->GetListOfKeys());
 TKey *key;

 while ((key = (TKey*)next())) {
  TString keyname = (TString) key->GetName();
  std::cout<<"Found key = "<<keyname<<std::endl;
  if ( !keyname.Contains("Tree") ) continue;

  TObject *obj = key->ReadObj();
  // if in a directory, recursively call function
  if (obj->IsA()->InheritsFrom(TDirectory::Class())) {
   dir->cd(keyname);
   TDirectory *subdir = gDirectory;
   AddReweightBranches(subdir,parser,postfix,h_wgt_b,h_wgt_c,h_wgt_l);
   dirsav->cd();
  }
  // if at a tree, do the weighting
  else if(obj->IsA()->InheritsFrom(TTree::Class())) {
   std::cout<<"We Found A Tree"<<std::endl;

   TTree *thetree = (TTree*)obj;

   // todo overwrite branch
   // https://root.cern.ch/phpBB3/viewtopic.php?f=3&t=6853
   // TBranch *delbranch = thetree->GetBranch(gJ1bname);
   // thetree->GetListOfBranches()->Remove(delbranch);

   // goodJ1
   Float_t goodJ1_pt = -15.;
   Float_t goodJ1_eta = -15.; 
   Float_t goodJ1_CSV = -15;
   Int_t goodJ1_partonFlavour = -15;
   Float_t gJ1rwtval = 1.;
   TString gJ1bname = "goodJ1_CSVrwt"+postfix ;
   TBranch *gJ1branch = thetree->Branch(gJ1bname,&gJ1rwtval,gJ1bname+"/F");
   thetree->SetBranchAddress("goodJ1_pt",&goodJ1_pt);
   thetree->SetBranchAddress("goodJ1_eta",&goodJ1_eta);
   thetree->SetBranchAddress("goodJ1_CSV",&goodJ1_CSV);
   thetree->SetBranchAddress("goodJ1_partonFlavour",&goodJ1_partonFlavour);

   // goodJ2
   Float_t goodJ2_pt = -15.;
   Float_t goodJ2_eta = -15.; 
   Float_t goodJ2_CSV = -15;
   Int_t goodJ2_partonFlavour = -15;
   Float_t gJ2rwtval = 1.;
   TString gJ2bname = "goodJ2_CSVrwt"+postfix ;
   TBranch *gJ2branch = thetree->Branch(gJ2bname,&gJ2rwtval,gJ2bname+"/F");
   thetree->SetBranchAddress("goodJ2_pt",&goodJ2_pt);
   thetree->SetBranchAddress("goodJ2_eta",&goodJ2_eta);
   thetree->SetBranchAddress("goodJ2_CSV",&goodJ2_CSV);
   thetree->SetBranchAddress("goodJ2_partonFlavour",&goodJ2_partonFlavour);

   // goodJ3
   Float_t goodJ3_pt = -15.;
   Float_t goodJ3_eta = -15.; 
   Float_t goodJ3_CSV = -15;
   Int_t goodJ3_partonFlavour = -15;
   Float_t gJ3rwtval = 1.;
   TString gJ3bname = "goodJ3_CSVrwt"+postfix ;
   TBranch *gJ3branch = thetree->Branch(gJ3bname,&gJ3rwtval,gJ3bname+"/F");
   thetree->SetBranchAddress("goodJ3_pt",&goodJ3_pt);
   thetree->SetBranchAddress("goodJ3_eta",&goodJ3_eta);
   thetree->SetBranchAddress("goodJ3_CSV",&goodJ3_CSV);
   thetree->SetBranchAddress("goodJ3_partonFlavour",&goodJ3_partonFlavour);

   // goodJ4
   Float_t goodJ4_pt = -15.;
   Float_t goodJ4_eta = -15.; 
   Float_t goodJ4_CSV = -15;
   Int_t goodJ4_partonFlavour = -15;
   Float_t gJ4rwtval = 1.;
   TString gJ4bname = "goodJ4_CSVrwt"+postfix ;
   TBranch *gJ4branch = thetree->Branch(gJ4bname,&gJ4rwtval,gJ4bname+"/F");
   thetree->SetBranchAddress("goodJ4_pt",&goodJ4_pt);
   thetree->SetBranchAddress("goodJ4_eta",&goodJ4_eta);
   thetree->SetBranchAddress("goodJ4_CSV",&goodJ4_CSV);
   thetree->SetBranchAddress("goodJ4_partonFlavour",&goodJ4_partonFlavour);

   // fwdJ1
   Float_t fwdJ1_pt = -15.;
   Float_t fwdJ1_eta = -15.; 
   Float_t fwdJ1_CSV = -15;
   Int_t fwdJ1_partonFlavour = -15;
   Float_t fJ1rwtval = 1.;
   TString fJ1bname = "fwdJ1_CSVrwt"+postfix ;
   TBranch *fJ1branch = thetree->Branch(fJ1bname,&fJ1rwtval,fJ1bname+"/F");
   thetree->SetBranchAddress("fwdJ1_pt",&fwdJ1_pt);
   thetree->SetBranchAddress("fwdJ1_eta",&fwdJ1_eta);
   thetree->SetBranchAddress("fwdJ1_CSV",&fwdJ1_CSV);
   thetree->SetBranchAddress("fwdJ1_partonFlavour",&fwdJ1_partonFlavour);

   // fwdJ2
   Float_t fwdJ2_pt = -15.;
   Float_t fwdJ2_eta = -15.; 
   Float_t fwdJ2_CSV = -15;
   Int_t fwdJ2_partonFlavour = -15;
   Float_t fJ2rwtval = 1.;
   TString fJ2bname = "fwdJ2_CSVrwt"+postfix ;
   TBranch *fJ2branch = thetree->Branch(fJ2bname,&fJ2rwtval,fJ2bname+"/F");
   thetree->SetBranchAddress("fwdJ2_pt",&fwdJ2_pt);
   thetree->SetBranchAddress("fwdJ2_eta",&fwdJ2_eta);
   thetree->SetBranchAddress("fwdJ2_CSV",&fwdJ2_CSV);
   thetree->SetBranchAddress("fwdJ2_partonFlavour",&fwdJ2_partonFlavour);

   // Loop through events, Fill branch and (over)write to tree
   for(Int_t i=0;i<thetree->GetEntries();++i){
    thetree->GetEntry(i);

    // goodJ1
    gJ1rwtval = CalculateReweight(
     goodJ1_pt,  TMath::Abs(goodJ1_eta),
     goodJ1_CSV, TMath::Abs(goodJ1_partonFlavour),
     h_wgt_b, h_wgt_c, h_wgt_l );
    gJ1branch->Fill();
    // goodJ2
    gJ2rwtval = CalculateReweight(
     goodJ2_pt,  TMath::Abs(goodJ2_eta),
     goodJ2_CSV, TMath::Abs(goodJ2_partonFlavour),
     h_wgt_b, h_wgt_c, h_wgt_l );
    gJ2branch->Fill();
    // goodJ3
    gJ3rwtval = CalculateReweight(
     goodJ3_pt,  TMath::Abs(goodJ3_eta),
     goodJ3_CSV, TMath::Abs(goodJ3_partonFlavour),
     h_wgt_b, h_wgt_c, h_wgt_l );
    gJ3branch->Fill();
    // goodJ4
    gJ4rwtval = CalculateReweight(
     goodJ4_pt,  TMath::Abs(goodJ4_eta),
     goodJ4_CSV, TMath::Abs(goodJ4_partonFlavour),
     h_wgt_b, h_wgt_c, h_wgt_l );
    gJ4branch->Fill();
    // fwdJ1
    fJ1rwtval = CalculateReweight(
     fwdJ1_pt,  TMath::Abs(fwdJ1_eta),
     fwdJ1_CSV, TMath::Abs(fwdJ1_partonFlavour),
     h_wgt_b, h_wgt_c, h_wgt_l );
    fJ1branch->Fill();
    // fwdJ2
    fJ2rwtval = CalculateReweight(
     fwdJ2_pt,  TMath::Abs(fwdJ2_eta),
     fwdJ2_CSV, TMath::Abs(fwdJ2_partonFlavour),
     h_wgt_b, h_wgt_c, h_wgt_l );
    fJ2branch->Fill();

   }
   thetree->Write("",TObject::kOverwrite);
   return;
  }
 }
}

Float_t CalculateReweight(
    Float_t pt, 
    Float_t eta, 
    Float_t csv, 
    Int_t flavor,
    TH1D* h_wgt_b[9][6],
    TH1D* h_wgt_c[5][6],
    TH1D* h_wgt_l[9][4][3] ){

    Int_t iSysHF = 0;
//    switch(iSysType){
//    case sysType::JESup:           iSysHF=1; break;
//    case sysType::JESdown:         iSysHF=2; break;
//    case sysType::CSVLFup:         iSysHF=3; break;
//    case sysType::CSVLFdown:       iSysHF=4; break;
//    case sysType::CSVHFStats1up:   iSysHF=5; break;
//    case sysType::CSVHFStats1down: iSysHF=6; break;
//    case sysType::CSVHFStats2up:   iSysHF=7; break;
//    case sysType::CSVHFStats2down: iSysHF=8; break;
//    default : iSysHF = 0; break;
//    }

    Int_t iSysC = 0;
//    switch(iSysType){
//    case sysType::CSVCErr1up:   iSysC=1; break;
//    case sysType::CSVCErr1down: iSysC=2; break;
//    case sysType::CSVCErr2up:   iSysC=3; break;
//    case sysType::CSVCErr2down: iSysC=4; break;
//    default : iSysC = 0; break;
//    }

    Int_t iSysLF = 0;
//    switch(iSysType){
//    case sysType::JESup:           iSysLF=1; break;
//    case sysType::JESdown:         iSysLF=2; break;
//    case sysType::CSVHFup:         iSysLF=3; break;
//    case sysType::CSVHFdown:       iSysLF=4; break;
//    case sysType::CSVLFStats1up:   iSysLF=5; break;
//    case sysType::CSVLFStats1down: iSysLF=6; break;
//    case sysType::CSVLFStats2up:   iSysLF=7; break;
//    case sysType::CSVLFStats2down: iSysLF=8; break;
//    default : iSysLF = 0; break;
//    }

    Float_t rwtvalue = 1.;
    Float_t wgt_b = 1.; 
    Float_t wgt_c  = 1.; 
    Float_t wgt_l = 1.; 

    Int_t ipt = -1;
    Int_t ieta = -1; 
    if (pt<30) ipt = 0;
    else if (pt >=30 && pt<40) ipt = 1;
    else if (pt >=40 && pt<60) ipt = 2;
    else if (pt >=60 && pt<100) ipt = 3;
    else if (pt >=100 && pt<160) ipt = 4;
    else if (pt >=160 && pt<10000) ipt = 5;

    if (eta >=0 &&  eta<0.8) ieta = 0;
    else if ( eta>=0.8 && eta<1.6) ieta = 1;
    else if ( eta>=1.6) ieta = 2;
    //else if ( eta>=1.6 && eta<2.41) ieta = 2;

    if ( flavor == 5 ){
      Int_t useCSVBin = (csv>=0.) ? h_wgt_b[iSysHF][ipt]->FindBin(csv) : 1;
      Float_t iCSVWgtHF = h_wgt_b[iSysHF][ipt]->GetBinContent(useCSVBin);
      if( iCSVWgtHF!=0 ) wgt_b *= iCSVWgtHF;
    }   
    else if( flavor == 4 ){
      Int_t useCSVBin = (csv>=0.) ? h_wgt_c[iSysC][ipt]->FindBin(csv) : 1;
      Float_t iCSVWgtC = h_wgt_c[iSysC][ipt]->GetBinContent(useCSVBin);
      if( iCSVWgtC!=0 ) wgt_c *= iCSVWgtC;
    }   
    else {
      if (ipt >=3) ipt=3;       /// [>60] 
      Int_t useCSVBin = (csv>=0.) ? h_wgt_l[iSysLF][ipt][ieta]->FindBin(csv) : 1;
      Float_t iCSVWgtLF = h_wgt_l[iSysLF][ipt][ieta]->GetBinContent(useCSVBin);
      if( iCSVWgtLF!=0 ) wgt_l *= iCSVWgtLF;
    }   
  
    rwtvalue = wgt_b * wgt_c * wgt_l;
    //std::cout<<"CSV Weight "<<rwtvalue<<std::endl;
    // std::cout<<" wgt_b "<<wgt_b<<" wgt_c "<<wgt_c<<" wgt_l "<<wgt_l<<std::endl;  
    // std::cout<<"eta "<<eta<<" pt "<<pt<<" flavor "<<flavor<<" csv "<<csv<<std::endl;

 return rwtvalue;
}

