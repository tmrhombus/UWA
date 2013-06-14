#include "TCanvas.h"

void effHist(){
Int_t NBINS = 15;
Float_t etaBins[16] = {-2.4, -2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.4};

TH1F *hd = new TH1F("hd","histogram",NBINS,etaBins);
TH1F *hmc = new TH1F("hmc","histogram",NBINS,etaBins);
TCanvas *c1 = new TCanvas("c1","Histogram Drawing Options",200,10,700,900);
TCanvas *c2 = new TCanvas("c2","Histogram Drawing Options",200,10,700,900);

outFile = new TFile("../data/eff_mu.root","RECREATE");

c1->cd();
hd->Fill(-2.4+.1,0.582);
hd->Fill(-2.1+.1,0.881);
hd->Fill(-1.6+.1,0.844);
hd->Fill(-1.2+.1,0.831);
hd->Fill(-0.9+.1,0.875);
hd->Fill(-0.6+.1,0.904);
hd->Fill(-0.3+.05,0.857);
hd->Fill(-0.2+.1,0.904);
hd->Fill(0.2+0.05,0.859);
hd->Fill(0.3+.1,0.904);
hd->Fill(0.6+.1,0.877);
hd->Fill(0.9+.1,0.828);
hd->Fill(1.2+.1,0.828);
hd->Fill(1.6+.1,0.818);
hd->Fill(2.1+.1,0.589);
hd->Draw();
c1->Update();

c2->cd();
hmc->Fill(-2.4+.1,0.456);
hmc->Fill(-2.1+.1,0.784);
hmc->Fill(-1.6+.1,0.800);
hmc->Fill(-1.2+.1,0.843);
hmc->Fill(-0.9+.1,0.886);
hmc->Fill(-0.6+.1,0.919);
hmc->Fill(-0.3+.05,0.893);
hmc->Fill(-0.2+.1,0.921);
hmc->Fill(0.2+0.05,0.892);
hmc->Fill(0.3+.1,0.918);
hmc->Fill(0.6+.1,0.883);
hmc->Fill(0.9+.1,0.847);
hmc->Fill(1.2+.1,0.796);
hmc->Fill(1.6+.1,0.770);
hmc->Fill(2.1+.1,0.443);
hmc->Draw();
c2->Update();

outFile->cd();

hd->Write();
hmc->Write();
}