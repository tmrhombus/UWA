# CUTS
massTrans = 50.
cuts={}
#trigger = '(HLT_IsoMu24_eta2p1_v_fired||HLT_Mu40eta2p1_v_fired)'
trigger = '(HLT_IsoMu24_eta2p1_v_fired)'
muon_selection = '(nMuons==1&&abs(muonEta)<2.1&&muonPt>25)'
vertex = '(abs(dz)<0.5&&abs(l1DXY)<0.02)'
jets = '(highestJetPt>30 && secondJetPt>30 && nJetsPt25>=2 && abs(highestJetEta)<2.5 && abs(secondJetEta)<2.5)'

def cutmaker(iv,aiv):
 cuts['Skim']='('+trigger+'&&'+muon_selection+'&&'+vertex+'&&'+jets+')'
 cuts['Iso']='(lPFIsoDB<'+str(iv)+')'
 cuts['NonIso'] ='(lPFIsoDB>='+str(aiv)+')'
 
 cuts['OneBtag']='(((jet1BTag_CSV>0.898)||(jet2BTag_CSV>0.898))&&!(jet1BTag_CSV>0.898&&jet2BTag_CSV>0.898))'
 cuts['SomeBtag']='((jet1BTag_CSV>0.679)||(jet2BTag_CSV>0.679))'
 cuts['TwoBtag']='(jet1BTag_CSV>0.679&&jet2BTag_CSV>0.679)'
 return cuts
