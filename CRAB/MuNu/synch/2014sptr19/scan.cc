TString columns = "EVENT:muon_pt_vec[0]:muon_pt_vec[1]:muon_eta:muNuRelPFIsoDB_A_vec[0]:muNuRelPFIsoDB_A_vec[1]:nrMu:nrMuLoose:nrEle";
TString columns = "EVENT:J1_pt:J1_eta:J1_CSVbtag:J2_pt:J2_eta:J2_CSVbtag:J3_pt:J3_eta:J3_CSVbtag";
TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT";

TString cuts = "";
TString cuts = "J2_pt<25."
TString cuts = "nrMuLoose>1 || nrEle>0"
TString cuts = "J3_pt>25 && J3_eta<2.4"

TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");

((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C0_tt_mets_xyp.txt"); 

New_Tree->Scan(columns,cuts,"colsize=10")

# full selection different events
TString cuts = "EVENT==66899251||EVENT==3196962||EVENT==65011275||EVENT==5521111||EVENT==76947283"

TString cuts = "EVENT==1428572535||EVENT==1428687615||EVENT==1428656551||EVENT==1428716439"


TString cuts = "((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired)&&((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (mt_new>45)))";

TString columns = "EVENT:met_pt:met_phi:mt_new";
TString columns = "EVENT:J1_pt_L1:J1_pt_L2:J1_pt_L3:J1_pt";
TTree* New_Tree = _file0.Get("muNuEventTree/eventTree");
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("tt_jet_corr.txt");
New_Tree->Scan(columns,cuts,"colsize=10")