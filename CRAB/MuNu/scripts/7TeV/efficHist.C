/* #include "Riostream.h"						     */
void efficHist() {
 ifstream in;
 in.open("../data/efficData.dat");
 
 Float_t x,y,z;
 Float_t p,q,r;
 Int_t nlines = 0;
 Int_t mlines = 0;
 Int_t NBINS = 15;
 Float_t etaBins[16] = {-2.4, -2.1, -1.6, -1.2, -0.9, -0.6, -0.3, -0.2, 0.2, 0.3, 0.6, 0.9, 1.2, 1.6, 2.1, 2.4};
 
 TFile *f = new TFile("../data/eff_mu.root","RECREATE");
 TH1F *hd = new TH1F("hd","hd",NBINS,etaBins);
 TH1F *hde = new TH1F("hde","hde",NBINS,etaBins);
 TH1F *hmc = new TH1F("hmc","hmc",NBINS,etaBins);
 TH1F *hmce = new TH1F("hmce","hmce",NBINS,etaBins);

 TNtuple *dataleaf = new TNtuple("dataleaf","data from file","x:y:z");
 TNtuple *mcleaf = new TNtuple("mcleaf","mc from file","p:q:r");

 while (1) {
    in >> x >> y >> z;
    if (!in.good()) break;
    if (nlines < 5) printf("x=%8f, y=%8f, z=%8f\n",x,y,z);
    hd->Fill(x+0.05,y);
    hde->Fill(x+0.05,z);
    dataleaf->Fill(x,y,z);
    nlines++;
 }
 printf(" found %d points\n",nlines);

 in.close();
 
 in.open("../data/efficData.dat");
 while (1) {
	 in >> p >> q >> r;
	 if (!in.good()) break;
	 if (mlines < 5) printf("p=%8f, q=%8f, r=%8f\n",p,q,r);
	 hmc->Fill(p+0.05,q);
	 hmce->Fill(p+0.05,r);
	 mcleaf->Fill(p,q,r);
	 mlines++;
 }

 in.close();
 f->Write();
}

