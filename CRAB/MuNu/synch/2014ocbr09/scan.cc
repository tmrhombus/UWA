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
((TTreePlayer*)(New_Tree->GetPlayer()))->SetScanFileName("C0_tt_leps.txt"); 

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


TString cuts = "EVENT==80813416||EVENT==80376971||EVENT==52245065||EVENT==15862805||EVENT==72590275||EVENT==65472216||EVENT==75776815||EVENT==57675310||EVENT==3199316||EVENT==75785603||EVENT==80374650||EVENT==65031536||EVENT==65032098||EVENT==22131586||EVENT==80373609||EVENT==24860133||EVENT==73100821||EVENT==70330402||EVENT==80374972||EVENT==79329211||EVENT==45733963||EVENT==80366793||EVENT==80366795||EVENT==80365326||EVENT==68490349||EVENT==3197155||EVENT==55344777||EVENT==66900773||EVENT==22130095||EVENT==22131361||EVENT==66905002||EVENT==1578175||EVENT==68490649||EVENT==80813580||EVENT==75777038||EVENT==65037821||EVENT==79335538||EVENT==24860056||EVENT==24571591||EVENT==4022494||EVENT==66857629||EVENT==80374101||EVENT==24858777||EVENT==75784274||EVENT==88786430||EVENT==52247237||EVENT==22131817||EVENT==79325495||EVENT==3198161||EVENT==80373609||EVENT==4022494||EVENT==52248070||EVENT==66902586||EVENT==79333016||EVENT==80813409||EVENT==88783739||EVENT==14719218";

