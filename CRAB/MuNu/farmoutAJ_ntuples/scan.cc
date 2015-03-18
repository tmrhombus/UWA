
// Mu
TString columns = "HLT_IsoMu24_eta2p1_v_fired:nrGoodMu:nrVetoMu:nrVetoEle:nrGoodJets:nrFwdJets:mt_goodMuon:goodJ1_CSV:goodJ2_CSV"; 
// Ele
//TString columns = "EVENT:goodEle_pt_vec:goodEle_eta_vec:goodEle_phi_vec";
TString columns = "HLT_Ele27_WP80_fired:nrGoodEle:goodEle_Iso03_vec[0]:nrVetoEle:nrVetoMu:nrGoodJets:nrFwdJets:mt_goodElectron:goodJ1_CSV:goodJ2_CSV";


// Wbb Mu
TString cuts = "(HLT_IsoMu24_eta2p1_v_fired && nrGoodMu==1 && nrVetoMu<=1 && nrVetoEle==0 && nrGoodJets==2 && nrFwdJets==0)"; 
// Wbb Ele
TString cuts = "(HLT_Ele27_WP80_fired && nrGoodEle==1 && goodEle_Iso03_vec[0]<0.10 && nrVetoEle<=1 && nrVetoMu==0 && nrGoodJets==2 && nrFwdJets==0)"; 
// no cut
TString cuts = ""; 

TTree* tree0 = _file0.Get("muEleEventTree/eventTree");

((TTreePlayer*)(tree0->GetPlayer()))->SetScanRedirect(true);
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Wbb4F_skimmed_wjj_mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Wbb4F_skimmed_wjj_ele.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Wbb4F_isItFull_wjj_mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Wbb4F_isItFull_wjj_ele.txt");

((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("New_Mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("New_Ele.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Old_Mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Old_Ele.txt");

tree0->Scan(columns,cuts,"colsize=10");


