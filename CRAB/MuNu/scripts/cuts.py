# CUTS
massTrans = 50.

cuts={}

trigger = '(HLT_IsoMu24_eta2p1_v_fired||HLT_Mu40eta2p1_v_fired)'
muon_selection = '(nMuons==1&&abs(muonEta)<2.1&&muonPt>25)'
vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'

cuts['Skim']='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+'(jet2pt>25&&massDiJets!=0&&nJets20>=2&&mt>0&&ptMu>30)'
cuts['OneBtag']='(((jet1BTag_CSV>0.898)||(jet2BTag_CSV>0.898))&&!(jet1BTag_CSV>0.898&&jet2BTag_CSV>0.898))'
cuts['SomeBtag']='((jet1BTag_CSV>0.679)||(jet2BTag_CSV>0.679))'
cuts['TwoBtag']='(jet1BTag_CSV>0.679&&jet2BTag_CSV>0.679)'

