TString columns = "EVENT:J1_pt_gen:J1_eta_gen:J2_pt_gen:J2_eta_gen:J3_pt_gen:J3_eta_gen:J4_pt_gen:J4_eta_gen";
TString columns = "EVENT:J1_pt_gen_Nu:J1_eta_gen_Nu:J2_pt_gen_Nu:J2_eta_gen_Nu:J3_pt_gen_Nu:J3_eta_gen_Nu:J4_pt_gen_Nu:J4_eta_gen_Nu";
TString columns = "EVENT:J1_pt_L1:J1_eta_L1:J2_pt_L1:J2_eta_L1:J3_pt_L1:J3_eta_L1:J4_pt_L1:J4_eta_L1";
TString columns = "EVENT:J1_pt_L2:J1_eta_L2:J2_pt_L2:J2_eta_L2:J3_pt_L2:J3_eta_L2:J4_pt_L2:J4_eta_L2";
TString columns = "EVENT:J1_pt_L3:J1_eta_L3:J2_pt_L3:J2_eta_L3:J3_pt_L3:J3_eta_L3:J4_pt_L3:J4_eta_L3";
TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT:HLT_IsoMu24_eta2p1_v_fired:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";


TString columns ="EVENT:RUN:J1_pt:J2_pt:J3_pt:muon_pt:nrMu:nrMuLoose:nrEle:nrEleLoose:met_pt:mt_new";

TString columns ="EVENT:J1_pt:J1_eta:J1_idLooseJet:J2_pt:J2_eta:J2_idLooseJet:J3_pt:J3_eta:J3_idLooseJet:J4_pt:J4_eta:J5_pt:J5_eta";


TString columns = "EVENT";
TString columns = "EVENT:HLT_Ele27_WP80_fired:nrMu:nrMuLoose:nrGoodMu:nrVetoMu:nrQCDMu:nrEle:nrEleLoose:nrGoodEle:nrVetoEle:nrQCDEle";
TString columns = "EVENT:goodEle_pt_vec[0]:goodEle_eta_vec[0]:goodEle_phi_vec[0]";
TString columns = "EVENT:allEle_pt_vec[0]:allEle_eta_vec[0]:allEle_phi_vec[0]:met_pt:met_pt_Ind:mt_electron_vec[0]";
TString columns = "EVENT:allEle_pt_vec[0]:allEle_eta_vec[0]:allEle_phi_vec[0]:allEle_iso_vec[0]"
eString columns = "EVENT:allEle_pt_vec[1]:allEle_eta_vec[1]:allEle_phi_vec[1]:allEle_iso_vec[1]"
TString columns = "EVENT:goodEle_pt_vec[0]:goodEle_eta_vec[0]:goodEle_phi_vec[0]:goodEle_iso_vec[0]"
TString columns = "EVENT:allEle_dB_vec[0]:allEle_ecalE_vec[0]:allEle_escoP_vec[0]:allEle_pConvVto_vec[0]:allEle_trkNrH_vec[0]"
TString columns = "EVENT:allEle_scEta_vec[0]:allEle_dEscTratVtx_vec[0]:allEle_dPscTratVtx_vec[0]:allEle_sIeIe_vec[0]:allEle_hoEM_vec[0]"
TString columns = "EVENT:allMu_pt_vec[0]:allMu_eta_vec[0]:allMu_phi_vec[0]:allMu_Iso_vec[0]"
TString columns = "EVENT:goodMu_pt_vec[0]:goodMu_eta_vec[0]:goodMu_phi_vec[0]:goodMu_charge_vec[0]"

TTree* New_Tree = _file0.Get("muEleEventTree/eventTree");
TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");

columns = "EVENT:goodEle_Iso03_vec[0]:goodMu_charge_vec[0]:goodJ1_pt:goodJ1_CSV"
TString columns = "EVENT:HLT_Ele27_WP80_fired:nrMu:nrMuLoose:nrGoodMu:nrVetoMu:nrQCDMu:nrEle:nrEleLoose:nrGoodEle:nrVetoEle:nrQCDEle"

TString columns = "HLT_Ele27_WP80_fired:nrGoodEle:goodEle_Iso03_vec[0]:nrVetoEle:nrVetoMu:nrGoodJets:nrFwdJets:mt_goodElectron:goodJ1_CSV:goodJ2_CSV:goodJ1_jProb:goodJ1_jBProb"
TString columns = "HLT_Ele27_WP80_fired:nrGoodEle:goodEle_Iso03_vec[0]:nrVetoEle:nrVetoMu:nrGoodJets:nrFwdJets:mt_goodElectron:goodJ1_CSV:goodJ2_CSV"
TString cuts = "";
TTree* tree0 = _file0.Get("electronEventTree/eventTree");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Ele_prova.txt");
tree0->Scan(columns,cuts,"colsize=10");

TTree* tree1 = _file1.Get("electronEventTree/eventTree");
((TTreePlayer*)(tree1->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(tree1->GetPlayer()))->SetScanFileName("Ele_Full.txt");
tree1->Scan(columns,cuts,"colsize=10");


((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("NY_All_electrons.txt");


New_Tree->Scan(columns,cuts,"colsize=10")



_file0->cd();
muNuEventTree->cd();
TString columns = "EVENT:allJ1_pt:allJ1_eta:allJ1_phi:allJ2_pt:allJ2_eta:allJ2_phi:allJ3_pt:allJ3_eta:allJ3_phi:allJ4_pt:allJ4_eta:allJ4_phi";
TString columns = "EVENT:goodJ1_pt:goodJ1_eta:goodJ1_phi:goodJ2_pt:goodJ2_eta:goodJ2_phi:goodJ3_pt:goodJ3_eta:goodJ3_phi:goodJ4_pt:goodJ4_eta:goodJ4_phi";
TString columns = "EVENT:J1_pt_gen_NoNu:J1_eta_gen_NoNu:J1_phi_gen_NoNu:J2_pt_gen_NoNu:J2_eta_gen_NoNu:J2_phi_gen_NoNu:J3_pt_gen_NoNu:J3_eta_gen_NoNu:J3_phi_gen_NoNu:J4_pt_gen_NoNu:J4_eta_gen_NoNu:J4_phi_gen_NoNu";

eventTree->Scan(columns,cuts,"colsize=10")

_file1->cd();
muNuEventTree->cd();

TTree* New_Tree = _file0.Get("muEleEventTree/eventTree");
// Cut 1
TString columns = "HLT_Ele27_WP80_fired:nrGoodEle:goodEle_Iso03_vec[0]:nrVetoEle:nrVetoMu:nrGoodJets:nrFwdJets";
TString columns = "EVENT:nrGoodEle:goodEle_pt_vec:nrAllEle:allEle_pt_vec:allEle_eta_vec:allEle_iso_vec:allEle_Iso03_vec:allEle_Iso04_vec"
TString columns = "EVENT:allEle_pt_vec:allEle_iso_vec:allEle_chIso_vec:allEle_nhIso_vec:allEle_phIso_vec:allEle_puIso_vec"
TString columns = "EVENT:allEle_pt_vec:allEle_Iso03_vec:allEle_Iso03xPT_vec:allEle_cHI03_vec:allEle_nHI03_vec:allEle_gI03_vec:allEle_pcHI03_vec"
TString columns = "EVENT:allEle_pt_vec:allEle_Iso04_vec:allEle_Iso04xPT_vec:allEle_cHI04_vec:allEle_nHI04_vec:allEle_gI04_vec:allEle_pcHI04_vec"

TString cuts = "EVENT==22134922||EVENT==45723622||EVENT==24858743||EVENT==63254235||EVENT==76947521||EVENT==16643504||EVENT==75774206||EVENT==6474255||EVENT==24561998||EVENT==80364915||EVENT==75775179||EVENT==22132393||EVENT==76947168||EVENT==63254787||EVENT==66903586||EVENT==24561900||EVENT==75786530||EVENT==15853635||EVENT==1580935||EVENT==24858091||EVENT==3197986||EVENT==66861167||EVENT==65469963||EVENT==87455940||EVENT==30792789||EVENT==22131089||EVENT==24565066"
New_Tree->Scan(columns,cuts,"colsize=9")













