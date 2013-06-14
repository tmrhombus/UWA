# CUTS
massTrans = 50.

cuts={}
#for TTbar
#cuts['Skim']="((HLT_IsoMu24_eta2p1_v_fired||HLT_IsoMu24_v_fired)&&muMuCands==0&&muNuCands>=1&&abs(etaMu)<2.1&&jet1pt>25&&jet2pt>25&&massDiJets!=0&&abs(jet1eta)<2.4&&abs(jet2eta)<2.4&&nJets20>=2&&mtW>0&&ptMu>30)"
#cuts['Skim']="((HLT_IsoMu24_eta2p1_v_fired||HLT_IsoMu24_v_fired)&&muNuCands>=1&&abs(etaMu)<2.1&&jet1pt>25&&jet2pt>25&&massDiJets!=0&&abs(jet1eta)>2.8&&abs(jet2eta)>2.8&&nJets20>=2&&mt>0&&ptMu>30)"
cuts['Skim']="((HLT_IsoMu24_eta2p1_v_fired||HLT_IsoMu24_v_fired)&&muNuCands>=1&&abs(etaMu)<2.1&&jet1pt>25&&jet2pt>25&&massDiJets!=0&&nJets20>=2&&mt>0&&ptMu>30)"
cuts['C1']='(jet1Bpt>1&&jet2Bpt>1&&jet1NoBpt>1&&jet2NoBpt>1&&nJets30 >= 4&&vetoPatElectrons==0)'
cuts['C2']='(nJets30>=3&&((jet1BTag_CSV>0.679)||(jet2BTag_CSV>0.679))&&vetoPatElectrons==0)'
cuts['notC2']='(nJets30<3&&((jet1BTag_CSV>0.679)||(jet2BTag_CSV>0.679))&&vetoPatElectrons==0)'
cuts['C3']='(nJets30>=3&&((jet1BTag_CSV>0.679)&&(jet2BTag_CSV>0.679))&&vetoPatElectrons==0)'
cuts['notC3']='(nJets30<3&&((jet1BTag_CSV>0.679)&&(jet2BTag_CSV>0.679))&&vetoPatElectrons==0)'
cuts['OneEle']='(vetoPatElectrons==1)'
cuts['OneEleB']='(vetoPatElectrons==1&&((jet1BTag_CSV>0.679)||(jet2BTag_CSV>0.679)))'
cuts['OneEleBB']='(vetoPatElectrons==1&&((jet1BTag_CSV>0.679)&&(jet2BTag_CSV>0.679)))'
cuts['3jets']='(nJets30>=3)'
cuts['4jets']='(nJets30>=4)'
cuts['IsDiBJet']='(jet1Bpt>1&&jet2Bpt>1)'
cuts['IsDiNoBJet']='(jet1NoBpt>1&&jet2NoBpt>1)'
cuts['MT']='(mt>'+str(massTrans)+')'
cuts['aDiMuon']='(massDiMuon>0)'
cuts['sTop']='((jet1BTag_CSV>0.679&&jet2eta>2.4)||(jet2BTag_CSV>0.679&&jet1eta>2.4))'
cuts['non']='((HLT_IsoMu24_eta2p1_v_fired||HLT_IsoMu24_v_fired))'

cuts['NoEle']='vetoPatElectrons==0'
cuts['NoMuMu']='(muMuCands==0)'
cuts['JetEta']='(abs(jet1eta)<2.1&&abs(jet2eta)<2.1)'
cuts['OneMuNu']='(muNuCands>=1)'
cuts['JetPt25']='(jet1pt>25&&jet2pt>25)'
cuts['JetPt30']='(jet1pt>30&&jet2pt>30)'
cuts['JetPt40']='(jet1pt>40&&jet2pt>40)'
cuts['4jets30']='(nJets30 == 4)'

cuts['notIsDiNoBJet']='(!(jet1NoBpt>1&&jet2NoBpt>1))'
cuts['MuPt']='(ptMu>30)'
cuts['NoTT']='(!((jet1Bpt>1&&jet2Bpt>1)&&(jet1NoBpt>1&&jet2NoBpt>1)))'
cuts['notC1']='(!(jet1Bpt>1&&jet2Bpt>1&&jet1NoBpt>1&&jet2NoBpt>1&&nJets30 == 4))'
cuts['notC3']='(nJets40<3)'
cuts['OneBtag']='(((jet1BTag_CSV>0.898)||(jet2BTag_CSV>0.898))&&!(jet1BTag_CSV>0.898&&jet2BTag_CSV>0.898))'
cuts['SomeBtag']='((jet1BTag_CSV>0.679)||(jet2BTag_CSV>0.679))'
cuts['TwoBtag']='(jet1BTag_CSV>0.679&&jet2BTag_CSV>0.679)'
#one b-tag, one very forward jet
cuts['JetKin']='((jet1BTag_CSV>0.898&&jet2eta>2.8)||(jet2BTag_CSV>0.898&&jet1eta>2.8))'

