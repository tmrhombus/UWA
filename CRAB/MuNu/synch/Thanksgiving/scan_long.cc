TString columns = "EVENT:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";
TString columns = "EVENT:electron_pt_vec[0]:electron_pt_vec[1]:eleNuRelPFIsoDB_A_vec[0]:nrMu:nrMuLoose:nrEle:nrEleLoose";
TString columns = "EVENT:J1_pt:J1_eta:J1_CSVbtag:J2_pt:J2_eta:J2_CSVbtag:J3_pt:J3_eta:J3_CSVbtag:J4_pt:J4_eta:J4_CSVbtag";
TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT";

TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");

((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C1_data_synch01_2014ocbr23_m12e10_smrGenNu_clnMu.txt"); 

((TTreePlayer*)(muNuEventTree_eventTree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(muNuEventTree_eventTree->GetPlayer()))->SetScanFileName("TTbar_full_wbbSelection.txt"); 
muNuEventTree_eventTree->Scan(columns,cuts,"colsize=10")



New_Tree->Scan(columns,cuts,"colsize=10")

# full selection different events

TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C0_tt_synch_2014ocbr03_jets.txt");
New_Tree->Scan(columns,cuts,"colsize=10")


TString columns = "EVENT:met_pt:met_phi:mt_new";
TString cuts = "";
TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");
New_Tree->Scan(columns,cuts,"colsize=10")


TString columns = "EVENT:J1_pt:J1_eta:J2_pt:J2_eta:J3_pt:J3_eta:J4_pt:J4_eta:J5_pt:J5_eta:J6_pt:J6_eta";
TString columns = "EVENT:J1_pt_gen:J1_eta_gen:J2_pt_gen:J2_eta_gen:J3_pt_gen:J3_eta_gen:J4_pt_gen:J4_eta_gen";
TString columns = "EVENT:J1_pt_gen_Nu:J1_eta_gen_Nu:J2_pt_gen_Nu:J2_eta_gen_Nu:J3_pt_gen_Nu:J3_eta_gen_Nu:J4_pt_gen_Nu:J4_eta_gen_Nu";
TString columns = "EVENT:J1_pt_gen_NoNu:J1_eta_gen_NoNu:J2_pt_gen_NoNu:J2_eta_gen_NoNu:J3_pt_gen_NoNu:J3_eta_gen_NoNu:J4_pt_gen_NoNu:J4_eta_gen_NoNu";
TString columns = "EVENT:J1_pt_L1:J1_eta_L1:J2_pt_L1:J2_eta_L1:J3_pt_L1:J3_eta_L1:J4_pt_L1:J4_eta_L1";
TString columns = "EVENT:J1_pt_L2:J1_eta_L2:J2_pt_L2:J2_eta_L2:J3_pt_L2:J3_eta_L2:J4_pt_L2:J4_eta_L2";
TString columns = "EVENT:J1_pt_L3:J1_eta_L3:J2_pt_L3:J2_eta_L3:J3_pt_L3:J3_eta_L3:J4_pt_L3:J4_eta_L3";
TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT:HLT_IsoMu24_eta2p1_v_fired:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";


TString columns ="EVENT:RUN:J1_pt:J2_pt:J3_pt:muon_pt:nrMu:nrMuLoose:nrEle:nrEleLoose:met_pt:mt_new";
TString columns ="EVENT:HLT_IsoMu24_eta2p1_v_fired:muon_eta:muon_pt:nrMuLoose:nrEle";
TString columns = "EVENT:RUN:weightEtaMuonID:weightEtaMuonIso:weightEtaMuonTrig:QweightFactor:J1_pt:J2_pt:J1_partonFlavour:J2_partonFlavour:J1_CSVT_SFb:J1_CSVT_SFl:J2_CSVT_SFb:J2_CSVT_SFl"
TString columns ="EVENT:J1_pt:J1_eta:J1_idLooseJet:J2_pt:J2_eta:J2_idLooseJet:J3_pt:J3_eta:J3_idLooseJet:J4_pt:J4_eta:J5_pt:J5_eta";


TString cuts = "EVENT==80366642||EVENT==66899251||EVENT==22130994||EVENT==76947963||EVENT==1577878||EVENT==65011275||EVENT==75776112||EVENT==88787016||EVENT==70329960||EVENT==79328732||EVENT==63257513||EVENT==6473783||EVENT==76947283||EVENT==3196962||EVENT==15853413||EVENT==75782215"

TString cuts = "";
New_Tree->Scan(columns,cuts,"colsize=10")

TString cuts = "EVENT==3196808||EVENT==3196817||EVENT==3196833||EVENT==3196839||EVENT==3196840"
TString cuts = "EVENT==15626033||EVENT==15626060||EVENT==15626076||EVENT==15626086||EVENT==15626099";




TString columns = "EVENT:electron_pt_vec[0]:electron_eta_vec[0]:electron_phi_vec[0]:electron_pt_vec[1]:nrMu:nrMuLoose:nrEle:nrEleLoose";
TString cuts = "EVENT==15626033||EVENT==15626060||EVENT==15626076||EVENT==15626086||EVENT==15626099";
TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");

New_Tree->Scan(columns,cuts,"colsize=10")
