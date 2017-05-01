
void printSyst(){


fa = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_EES_h_Wbb4F_ttme.root");
fb = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_EMu_h_Wbb4F_ttme.root");
fc = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_JES_h_Wbb4F_ttme.root");
fd = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_MES_h_Wbb4F_ttme.root");
fe = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_UES_h_Wbb4F_ttme.root");
ff = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgCSVsf_h_Wbb4F_ttme.root");
fg = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgDY_h_Wbb4F_ttme.root");
fh = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgGJ_h_Wbb4F_ttme.root");
fi = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgJESsf_h_Wbb4F_ttme.root");
fj = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgQCDele_h_Wbb4F_ttme.root");
fk = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgQCDmu_h_Wbb4F_ttme.root");
fl = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgTTbar_h_Wbb4F_ttme.root");
fm = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgT_h_Wbb4F_ttme.root");
fn = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgVV_h_Wbb4F_ttme.root");
fo = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgWcc_h_Wbb4F_ttme.root");
fp = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_bgWl_h_Wbb4F_ttme.root");
fq = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_full_h_Wbb4F_ttme.root");
fr = new TFile("/afs/cern.ch/user/t/tmperry/WbbFits_slc6_481_CMSSW_7_1_5/src/HiggsAnalysis/CombinedLimit/test/Wbb8TeV/Interlochen/Plots_liszt/Step3_Wbb/mlfit_Step3_Wbb_stats_h_Wbb4F_ttme.root");


fa->cd();
fit_s->Print();

fb->cd();
fit_s->Print();

fc->cd();
fit_s->Print();

fd->cd();
fit_s->Print();

fe->cd();
fit_s->Print();

ff->cd();
fit_s->Print();

fg->cd();
fit_s->Print();

fh->cd();
fit_s->Print();

fi->cd();
fit_s->Print();

fj->cd();
fit_s->Print();

fk->cd();
fit_s->Print();

fl->cd();
fit_s->Print();

fm->cd();
fit_s->Print();

fn->cd();
fit_s->Print();

fo->cd();
fit_s->Print();

fp->cd();
fit_s->Print();

fq->cd();
fit_s->Print();

fr->cd();
fit_s->Print();

}
