#include "TFile.h"
#include "TTree.h"
#include "TBranch.h"
#include "TH1F.h"

const Int_t kMaxfParticles = 1293;

void AnalyzeTree()
{
   // Variables used to store the data
   Int_t     totalSize = 0;         // Sum of data size (in bytes) of all events
   Int_t     eventSize = 0;         // Size of the current event
   TH1F      *hJ1pT;                // X position of the particles

   // List of branches
   TBranch  *highestJetPtBranch;
   TBranch  *highestJetEtaBranch;
   TBranch  *secondJetPtBranch;

   // Declaration of leaf types
   Double_t     highestJetPt;
   Double_t     highestJetEta;
   Double_t     secondJetPt;

   // open the file
   TFile *f = TFile::Open("../data/v0/TTbar.root");
   if (f == 0) {
      // if we cannot open the file, print an error message and return immediatly
      printf("Error: cannot open ../data/v0/TTbar.root!\n");
      return;
   }
   // get a pointer to the tree
   TTree *tree = (TTree *)f->Get("muNuEventTree/eventTree");
   // To use SetBranchAddress() with simple types (e.g. double, int)
   // instead of objects (e.g. std::vector<Particle>).
   tree->SetMakeClass(1);

   // Connect the branches with their member variables.
   tree->SetBranchAddress("highestJetPt", &highestJetPt, &highestJetPtBranch);
   tree->SetBranchAddress("highestJetEta", &highestJetEta, &highestJetEtaBranch);
   tree->SetBranchAddress("secondJetPt", &secondJetPt, &secondJetPtBranch);

   // create the TH1F histogram
   hJ1pT = new TH1F("hJ1pT", "highest Jet pT", 100, 0, 200);
   // enable bin errors:
   hJ1pT->Sumw2();

   Long64_t nentries = tree->GetEntries();
   for (Long64_t i=0;i<nentries;i++) {
      // We only need the number of particles...
      highestJetPtBranch->GetEntry(i);
      std::cout<<highestJetPtBranch->GetBinContent(i)<<std::endl;
      // ... and their position in X...
      highestJetEtaBranch->GetEntry(i);
      // ... and their momentum
      secondJetPtBranch->GetEntry(i);
      // *** 2. *** Do the actual analysis
      hJ1pT->Fill(highestJetPtBranch->GetEntry(i));
//      for (int iParticle = 0; iParticle < nParticles; ++iParticle) {
//            hJ1pT->Fill();
//      }
   }
   // Fit the histogram:
//   hPosX->Fit("pol2");
   // and draw it:
   hJ1pT->Draw();
}
