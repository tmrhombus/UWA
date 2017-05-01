
void fittedYieldCalc(){

f = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_full_h_Wbb4F_ttme.root");


f->cd();
shapes_prefit->cd();
Muo->cd();

printf("Muon Prefit\n");
printf(" Wbb         %7.1f \n", h_Wbb4F->Integral() );
printf(" Wcc         %7.1f \n", h_Wcc->Integral() );
printf(" Wl          %7.1f \n", h_Wl->Integral() );
printf(" TTbar       %7.1f \n", h_TTbar->Integral() );
printf(" Single Top  %7.1f \n", h_T->Integral() );
printf(" Drell-Yan   %7.1f \n", h_DYan->Integral() );
printf(" Diboson     %7.1f \n", h_VV->Integral() );
printf(" Photon+Jets %7.1f \n", h_GJ->Integral() );
printf(" QCD         %7.1f \n", h_qcd_mu->Integral() );


f->cd();
shapes_fit_s->cd();
Muo->cd();

printf("Muon Fitted\n");
printf(" Wbb         %7.1f \n", h_Wbb4F->Integral() );
printf(" Wcc         %7.1f \n", h_Wcc->Integral() );
printf(" Wl          %7.1f \n", h_Wl->Integral() );
printf(" TTbar       %7.1f \n", h_TTbar->Integral() );
printf(" Single Top  %7.1f \n", h_T->Integral() );
printf(" Drell-Yan   %7.1f \n", h_DYan->Integral() );
printf(" Diboson     %7.1f \n", h_VV->Integral() );
printf(" Photon+Jets %7.1f \n", h_GJ->Integral() );
printf(" QCD         %7.1f \n", h_qcd_mu->Integral() );


f->cd();
shapes_prefit->cd();
Ele->cd();

printf("Electron Prefit\n");
printf(" Wbb         %7.1f \n", h_Wbb4F->Integral() );
printf(" Wcc         %7.1f \n", h_Wcc->Integral() );
printf(" Wl          %7.1f \n", h_Wl->Integral() );
printf(" TTbar       %7.1f \n", h_TTbar->Integral() );
printf(" Single Top  %7.1f \n", h_T->Integral() );
printf(" Drell-Yan   %7.1f \n", h_DYan->Integral() );
printf(" Diboson     %7.1f \n", h_VV->Integral() );
printf(" Photon+Jets %7.1f \n", h_GJ->Integral() );
printf(" QCD         %7.1f \n", h_qcd_ele->Integral() );


f->cd();
shapes_fit_s->cd();
Ele->cd();

printf("Electron Fitted\n");
printf(" Wbb         %7.1f \n", h_Wbb4F->Integral() );
printf(" Wcc         %7.1f \n", h_Wcc->Integral() );
printf(" Wl          %7.1f \n", h_Wl->Integral() );
printf(" TTbar       %7.1f \n", h_TTbar->Integral() );
printf(" Single Top  %7.1f \n", h_T->Integral() );
printf(" Drell-Yan   %7.1f \n", h_DYan->Integral() );
printf(" Diboson     %7.1f \n", h_VV->Integral() );
printf(" Photon+Jets %7.1f \n", h_GJ->Integral() );
printf(" QCD         %7.1f \n", h_qcd_ele->Integral() );

}
