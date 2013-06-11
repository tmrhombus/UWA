#include "PhysicsTools/FWLite/interface/CommandLineParser.h" 
#include "TFile.h"
#include "TROOT.h"
#include "TKey.h"
#include "TTree.h"
#include "TH1F.h"
#include "TF1.h"
#include <math.h> 
#include "TMath.h" 
#include <limits>
#include "RooHist.h"
#include "TPaletteAxis.h"
#include "TCanvas.h"

// RooHist *stuff = _file0->Get("MC_combRelPFISO20_2011B_pt__abseta>1.2")



void readdir(TDirectory *dir,TFile * fc, TFile * ft,optutl::CommandLineParser parser); 


int main (int argc, char* argv[]) 
{
   optutl::CommandLineParser parser ("Sets Event Weights in the ntuple");
   //parser.addOption("outputFile",optutl::CommandLineParser::kString,"File","corrections.root");
   //parser.addOption("eta",optutl::CommandLineParser::kString,"eta variable","eta1");
   parser.addOption("EffFile",optutl::CommandLineParser::kString,"Efficiencies File","~/UWCode2012/CMSSW_5_2_5/src/UWAnalysis/ROOT/bin/MuonEfficiencies_11June2012_52X.root");
   parser.addOption("TrigEffFile",optutl::CommandLineParser::kString,"Trig Efficiency File","~/eff_mu.root");
   parser.addOption("brancheta",optutl::CommandLineParser::kString,"Tag and Probe Weight","effWEIGHTeta");
   parser.addOption("branchpt",optutl::CommandLineParser::kString,"Tag and Probe Weight","effWEIGHTpt");

   parser.addOption("typept",optutl::CommandLineParser::kInteger,"Typept",0);
   parser.addOption("typeeta",optutl::CommandLineParser::kInteger,"Typeeta",2);
   parser.parseArguments (argc, argv);
   
   TFile *f = new TFile(parser.stringValue("outputFile").c_str(),"UPDATE");
   printf("Now weighting: %s\n",parser.stringValue("outputFile").c_str());
   TFile *fc = new TFile(parser.stringValue("EffFile").c_str());

   TCanvas *mydummycanvas = new TCanvas();      
   TFile *ft = new TFile(parser.stringValue("TrigEffFile").c_str());
   //int topType = parser.integerValue("typeTop");

   readdir(f,fc,ft,parser);



   f->Close();
   fc->Close();
   ft->Close();
} 


void readdir(TDirectory *dir,TFile* fc, TFile* ft,optutl::CommandLineParser parser) 
{

  //read directory

  TDirectory *dirsav = gDirectory;
 
  TIter next(dir->GetListOfKeys());

  TKey *key;

  while((key = (TKey*)next())){
    printf("Found key=%s \n",key->GetName());

    TString string = (TString) key->GetName();
    if(string == "summary")
      return;

    TObject *obj = key->ReadObj();
    if(obj->IsA()->InheritsFrom(TDirectory::Class())){
      dir->cd(key->GetName());
      TDirectory *subdir = gDirectory;
      readdir(subdir,fc,ft,parser);
      dirsav->cd();
    }
    else if(obj->IsA()->InheritsFrom(TTree::Class())){
      TTree *t = (TTree*)obj;

      //get muon pt,eta
      float pt;
      float eta;

      float weightpt = 1.0;
      float weighteta = 1.0;
      
      int typeeta = 0;
      int typept = 0;
      t->SetBranchAddress("muonPt",&pt);
      t->SetBranchAddress("muonEta",&eta);
    
      //get branch and add in value
      TBranch *newBranchPt = t->Branch(parser.stringValue("branchpt").c_str(),&weightpt,(parser.stringValue("branchpt")+"/F").c_str());
      TBranch *typeBranchPt = t->Branch("TYPE",&typept,"TYPE/I");

      TBranch *newBranchEta = t->Branch(parser.stringValue("brancheta").c_str(),&weighteta,(parser.stringValue("brancheta")+"/F").c_str());
      TBranch *typeBranchEta = t->Branch("TYPE",&typeeta,"TYPE/I");

      ///////
      //ID/Trigger
      RooHist *ptMCB_2012 = (RooHist*)fc->Get("MC_IsoMu24_eta2p1_TightIso_pt_abseta<1.2");
      RooHist *ptMCE_2012 = (RooHist*)fc->Get("MC_IsoMu24_eta2p1_TightIso_pt_abseta>1.2");

      RooHist *ptDataB_2012 = (RooHist*)fc->Get("DATA_IsoMu24_eta2p1_TightIso_pt_abseta<1.2");
      RooHist *ptDataE_2012 = (RooHist*)fc->Get("DATA_IsoMu24_eta2p1_TightIso_pt_abseta>1.2");

      //
      printf("Found tree -> weighting\n");

      printf("Entries %i \n",(int)t->GetEntries());

      for(Int_t i=0;i<t->GetEntries();++i)
	{
	  t->GetEntry(i);
	  weightpt=0.0;
	  if(fabs(eta)<1.2)//abs eta less than 1.2
	    {
	      weightpt= (float) ptDataB_2012->Eval(pt)/(ptMCB_2012->Eval(pt));
	      //printf("Gets Here1\n");
	    }
	  else if(fabs(eta)>=1.2)//abs eta greater than = 1.2
	    {

	      weightpt = (float) ptDataE_2012->Eval(pt)/(ptMCE_2012->Eval(pt));

	    }
	}
	  newBranchPt->Fill();
	  typeBranchPt->Fill();
	  //printf("Gets Here4\n");
	  
	  RooHist *etaData_2012 = (RooHist*)fc->Get("DATA_IsoMu24_eta2p1_TightIso_eta_pt26-100");
	  RooHist *etaMC_2012 = (RooHist*)fc->Get("MC_IsoMu24_eta2p1_TightIso_eta_pt26-100");


      for(Int_t i=0;i<t->GetEntries();++i)
	{
	  //printf("Gets Here1\n");
	  t->GetEntry(i);
	  weighteta = 0.0;
	  if(pt>26)//abs eta less than 1.2
	    {
	      //printf("Gets Here2\n");
	      weighteta = etaData_2012->Eval(eta)/etaMC_2012->Eval(eta);
	      //printf("Gets Here2.1\n");
	      
	    }

	  //newBranchTrigEta->Fill();
	  newBranchEta->Fill();
	  typeBranchEta->Fill();
	}



      t->Write("",TObject::kOverwrite);

    }
    else{
    printf("Gets Here 1\n");
    return;     
    }
  }

} 
