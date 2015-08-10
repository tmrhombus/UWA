#define Q_class_cxx
#include "Q_class.h"
#include <TH2.h>
#include <TStyle.h>
#include <TCanvas.h>
#include <math.h>
#include <fstream>

void Q_class::Loop()
{
   if (fChain == 0) return;

   Long64_t nentries = fChain->GetEntriesFast();

   Long64_t nbytes = 0, nb = 0;
   double nrEEvents;
   double nrMEvents;
   nrEEvents = 0;
   nrMEvents = 0;

   Bool_t oneGoodMuon;
   Bool_t oneGoodElectron;
   Bool_t min2goodJs;
   Bool_t exactly2goodJs;
   Bool_t exactly2goodBJs;

   Int_t nbrGoodMu, nbrVetoMu, nbrQCDMu;
   Int_t nbrGoodEle, nbrVetoEle, nbrQCDEle;


   for (Long64_t jentry=0; jentry<nentries;jentry++) {
      Long64_t ientry = LoadTree(jentry);
      if (ientry < 0) break;
      nb = fChain->GetEntry(jentry);   nbytes += nb;


  nbrGoodMu = 0;  
  nbrGoodMu = std::count_if(
   goodMu_pt_vec->begin(),goodMu_pt_vec->end(), 
   std::bind2nd(std::greater_equal<Float_t>(),30));
  nbrVetoMu=0;
  if(vetoMu_pt>10){nbrVetoMu=1;}
  nbrQCDMu=0;
  if(qcdMu_pt>30){nbrQCDMu=1;}

  nbrGoodEle = 0;  
  nbrGoodEle = std::count_if(
   goodEle_pt_vec->begin(),goodEle_pt_vec->end(), 
   std::bind2nd(std::greater_equal<double>(),30.));
  nbrVetoEle=0;
  if(vetoEle_pt>10){nbrVetoEle=1;}
  nbrQCDEle=0;
  if(qcdEle_pt>30){nbrQCDEle=1;}
  oneGoodMuon = 
    HLT_IsoMu24_eta2p1_v_fired 
    && nbrGoodMu==1 && nbrVetoMu<=1 && nbrVetoEle==0;

  oneGoodElectron =
   HLT_Ele27_WP80_fired
   && nbrGoodEle==1 && nbrVetoEle<=1 && nbrVetoMu==0;

  exactly2goodJs = 
   goodJ1_pt>25 && goodJ2_pt>25 && fwdJ1_pt<25 && goodJ3_pt<25;

  exactly2goodBJs = //1;
   exactly2goodJs
   && goodJ1_CSV>0.898 && goodJ2_CSV>0.898;

   if (oneGoodElectron && exactly2goodBJs){
    std::cout<<"Found Electron Event: "<<EVENT<<std::endl;
    nrEEvents+=1;
   }   
   if (oneGoodMuon && exactly2goodBJs){
    std::cout<<"Found Muon Event: "<<EVENT<<std::endl;
    nrMEvents+=1;
   }   
   std::cout<<"  Event: "<<EVENT<<std::endl;
   std::cout<<"  nbrGoodEle: "<<nbrGoodEle<<std::endl;
   //std::cout<<"  goodEle_pt_vec->at(0): "<<goodEle_pt_vec->at(0)<<std::endl;
   std::cout<<"  goodJ1_pt: "<<goodJ1_pt<<std::endl;
   std::cout<<"  goodJ2_pt: "<<goodJ2_pt<<std::endl;
   }   
  std::cout<<"Total Electron Events: "<<nrEEvents<<std::endl;
  std::cout<<"Total Muon Events: "<<nrMEvents<<std::endl;
}
