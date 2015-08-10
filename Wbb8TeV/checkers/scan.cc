// Mu
TString columns = "EVENT:HLT_IsoMu24_eta2p1_v_fired:nrGoodMu:nrVetoMu:nrVetoEle:nrGoodJets:nrFwdJets:mt_goodMuon:goodJ1_CSV:goodJ2_CSV"; 
// Ele
//TString columns = "EVENT:goodEle_pt_vec:goodEle_eta_vec:goodEle_phi_vec";
TString columns = "EVENT:HLT_Ele27_WP80_fired:nrGoodEle:goodEle_Iso03_vec[0]:nrVetoEle:nrVetoMu:nrGoodJets:nrFwdJets:mt_goodElectron:goodJ1_CSV:goodJ2_CSV";


// Wbb Mu
TString cuts = "(HLT_IsoMu24_eta2p1_v_fired && nrGoodMu==1 && nrVetoMu<=1 && nrVetoEle==0 && nrGoodJets==2 && nrFwdJets==0)"; 
// Wbb Ele
TString cuts = "(HLT_Ele27_WP80_fired && nrGoodEle==1 && goodEle_Iso03_vec[0]<0.10 && nrVetoEle<=1 && nrVetoMu==0 && nrGoodJets==2 && nrFwdJets==0)"; 
// no cut
TString cuts = ""; 

TTree* tree0 = _file0.Get("muEleEventTree/eventTree");
TTree* tree0 = _file0.Get("muonEventTree/eventTree");
TTree* tree0 = _file0.Get("electronEventTree/eventTree");

((TTreePlayer*)(tree0->GetPlayer()))->SetScanRedirect(true);

((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("NeuYear_W1Jet_Mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Earth2_WJets_Ele.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("CestPi_WJets_Mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("CestPi_WJets_Ele.txt");

tree0->Scan(columns,cuts,"colsize=10");




// Jet Energy Corrections
_file0->cd();

muEleEventTree->cd();
muEleEventTreeJetUp->cd();
muEleEventTreeJetDown->cd();

eventTree->Scan("EVENT:goodJ1_pt:goodJ1_eta:goodJ2_pt:goodJ2_eta:met_pt:met_jesUp_pt:met_jesDn_pt","goodJ1_pt>25 && goodJ1_pt<35")
eventTree->Scan("EVENT:goodJ1_pt:goodJ1_eta:goodJ2_pt:goodJ2_eta:met_pt:met_jesUp_pt:met_jesDn_pt","goodJ1_pt>45 && goodJ1_pt<55")
eventTree->Scan("EVENT:goodJ1_pt:goodJ1_eta:goodJ2_pt:goodJ2_eta:met_pt:met_jesUp_pt:met_jesDn_pt","goodJ1_pt>95 && goodJ1_pt<105")



((TTreePlayer*)(tree0->GetPlayer()))->SetScanRedirect(true);

((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("CestPi_DataAMu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("CestPi_DataAEle.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Old_Mu.txt");
((TTreePlayer*)(tree0->GetPlayer()))->SetScanFileName("Old_Ele.txt");

tree0->Scan(columns,cuts,"colsize=10");
