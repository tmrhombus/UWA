TString columns = "EVENT:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";
TString columns = "EVENT:J1_pt:J1_eta:J1_CSVbtag:J2_pt:J2_eta:J2_CSVbtag:J3_pt:J3_eta:J3_CSVbtag:J4_pt:J4_eta:J4_CSVbtag";
TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT";

TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");

((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C1_data_synch01_2014ocbr23_m12e10_smrGenNu_clnMu.txt"); 

New_Tree->Scan(columns,cuts,"colsize=10")

# full selection different events

TString cuts = "((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired)&&((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (mt_new>45)))";

TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT:J1_pt_L1:J1_pt_L2:J1_pt_L3:J1_pt";


TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C0_tt_synch_2014ocbr03_jets.txt");
New_Tree->Scan(columns,cuts,"colsize=10")


TString columns = "EVENT:met_pt:met_phi:mt_new";
TString cuts = "";
TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");
New_Tree->Scan(columns,cuts,"colsize=10")

TString cuts = "EVENT==3196962";


TString columns = "EVENT:J1_pt:J1_eta:J2_pt:J2_eta:J3_pt:J3_eta:J4_pt:J4_eta:J5_pt:J5_eta:J6_pt:J6_eta";
TString columns = "EVENT:J1_pt_gen:J1_eta_gen:J2_pt_gen:J2_eta_gen:J3_pt_gen:J3_eta_gen:J4_pt_gen:J4_eta_gen";
TString columns = "EVENT:J1_pt_gen_Nu:J1_eta_gen_Nu:J2_pt_gen_Nu:J2_eta_gen_Nu:J3_pt_gen_Nu:J3_eta_gen_Nu:J4_pt_gen_Nu:J4_eta_gen_Nu";
TString columns = "EVENT:J1_pt_gen_NoNu:J1_eta_gen_NoNu:J2_pt_gen_NoNu:J2_eta_gen_NoNu:J3_pt_gen_NoNu:J3_eta_gen_NoNu:J4_pt_gen_NoNu:J4_eta_gen_NoNu";
TString columns = "EVENT:J1_pt_L1:J1_eta_L1:J2_pt_L1:J2_eta_L1:J3_pt_L1:J3_eta_L1:J4_pt_L1:J4_eta_L1";
TString columns = "EVENT:J1_pt_L2:J1_eta_L2:J2_pt_L2:J2_eta_L2:J3_pt_L2:J3_eta_L2:J4_pt_L2:J4_eta_L2";
TString columns = "EVENT:J1_pt_L3:J1_eta_L3:J2_pt_L3:J2_eta_L3:J3_pt_L3:J3_eta_L3:J4_pt_L3:J4_eta_L3";
TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";

TString columns ="EVENT:RUN:J1_pt:J2_pt:J3_pt:muon_pt_vec[0]:muon_pt_vec[1]:met_pt:mt_new";
TString cuts = "";
TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");
New_Tree->Scan(columns,cuts,"colsize=10")



TString cuts = "EVENT==80374889||EVENT==22132746||EVENT==87455977||EVENT==3198161||EVENT==75782615||EVENT==14715485||EVENT==79333016||EVENT==24563282||EVENT==45726591||EVENT==4022494||EVENT==68490946||EVENT==80813409||EVENT==66857629||EVENT==14719218";
TString cuts = "EVENT==4022494||EVENT==73082312||EVENT==66857629||EVENT==9190295";

