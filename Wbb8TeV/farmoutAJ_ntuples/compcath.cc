

TString columns1 = "EVENT:GEN_dressedLeptonPDGID:GEN_dressedLeptonOriginalPT:GEN_dressedLeptonPT:GEN_jetEtaLeadB:GEN_jetPt"
TString columns2 = "EVENT:SF_goodEle_IDIso:SF_goodEle_IDIsoHLT:SF_goodMu_IDIso:SF_goodMu_IDIsoHLT:SF_lumiWeightPU"
TString columns3 = "EVENT:allEle_pt_vec:allEle_eta_vec:goodEle_pt_vec:goodEle_eta_vec:goodEle_mass_vec"
TString columns4 = "EVENT:allMu_pt_vec:allMu_eta_vec:goodMu_pt_vec:goodMu_eta_vec:goodMu_mass_vec"
TString columns5 = "EVENT:allJ1_pt:allJ2_eta:fwdJ1_pt:goodJ1_CSV:goodJ1_pt:goodJ1_phi:met_pt:met_phi:mt_goodElectron:mt_goodMuon"
TString columns6 = "EVENT:nbHadrons:nrAllEle:nrAllJets:nrAllMu:nrGoodEle:nrGoodJets:nrGoodMu:vertices:HLT_Ele27_WP80_fired:HLT_Ele27_WP80_fired"

TTree* C_Tree = _file0.Get("muEleEventTree/eventTree");
TTree* T_Tree = _file1.Get("muEleEventTree/eventTree");

TString cuts = ""; 

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanRedirect(true);

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanFileName("C_1.txt");
C_Tree->Scan(columns1,cuts,"colsize=10");
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanFileName("T_1.txt");
T_Tree->Scan(columns1,cuts,"colsize=10");

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanFileName("C_2.txt");
C_Tree->Scan(columns2,cuts,"colsize=10");
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanFileName("T_2.txt");
T_Tree->Scan(columns2,cuts,"colsize=10");

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanFileName("C_3.txt");
C_Tree->Scan(columns3,cuts,"colsize=10");
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanFileName("T_3.txt");
T_Tree->Scan(columns3,cuts,"colsize=10");

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanFileName("C_4.txt");
C_Tree->Scan(columns4,cuts,"colsize=10");
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanFileName("T_4.txt");
T_Tree->Scan(columns4,cuts,"colsize=10");

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanFileName("C_5.txt");
C_Tree->Scan(columns5,cuts,"colsize=10");
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanFileName("T_5.txt");
T_Tree->Scan(columns5,cuts,"colsize=10");

((TTreePlayer*)(C_Tree->GetPlayer()))->SetScanFileName("C_6.txt");
C_Tree->Scan(columns6,cuts,"colsize=10");
((TTreePlayer*)(T_Tree->GetPlayer()))->SetScanFileName("T_6.txt");
T_Tree->Scan(columns6,cuts,"colsize=10");

