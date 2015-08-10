#!/usr/bin/env python
'''
Compares the shapes of variables from two data.root files
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle

import aHisto as h #function to make histograms
import histoRange as hr #manages range, lables for plots
 # newnew_v_newold
data_filename_nwr = '../data/partialData/Data_1_newGTreJet.root' 
data_filename_new = '../data/partialData/Data_1_new_new.root' 
data_filename_old = '../data/partialData/Data_1_old_new.root'

## # newnew_v_oldold
#data_filename_nwr = '../data/partialData/Data_newGTreJet.root'
#data_filename_new = '../data/v6/Data.root' 
#data_filename_old = '../data/v5/wMuNuData.root'

data_file_nwr  = TFile( data_filename_nwr )
data_file_new  = TFile( data_filename_new )
data_file_old  = TFile( data_filename_old )
eventTreeLocation = 'muNuEventTree/eventTree'
data_tree_nwr  =  data_file_nwr.Get(eventTreeLocation) 
data_tree_new  =  data_file_new.Get(eventTreeLocation) 
data_tree_old  =  data_file_old.Get(eventTreeLocation) 

leafs = [
#'highestJetPt',
'secondJetPt',
'thirdJetPt',
'Mt',
'nJetsPt25',
'MET',
'muonPt',
'muonEta',
'muonPhi',
'muonCharge',
'mJJ',
'vertices',
'mJ3J4',
]

cut = '(2>1)'

# 2j0b 
#cut = '((lPFIsoDB<0.12)&&(((HLT_IsoMu24_eta2p1_v_fired)&&(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)&&(abs(dz)<0.5&&abs(l1DXY)<0.02)&&(Mt>45)&&(nJets24Pt25==0))&&((highestJetPt >25 && secondJetPt>25 && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4) && nJetsPt25>=2)))'

# ttbar 1e1m
#cut = '((lPFIsoDB<0.12)&&(((HLT_IsoMu24_eta2p1_v_fired)&&(DiMuonMass<=60 && nElectrons==1 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)&&(abs(dz)<0.5&&abs(l1DXY)<0.02)&&(Mt>45))&&((((highestJetPt >25 && secondJetPt>25 && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4)&& thirdJetPt  > 25 && abs(thirdJetEta) <  2.4)&& mJ3J4 > 0) && nJetsPt25>=4)))'

# ttbar 4j2b
#cut = '((lPFIsoDB<0.12)&&((((HLT_IsoMu24_eta2p1_v_fired)&&(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)&&(abs(dz)<0.5&&abs(l1DXY)<0.02)&&(Mt>45)&&(nJets24Pt25==0)))&&((((highestJetPt >25 && secondJetPt>25 && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4)&& thirdJetPt >25 && abs(thirdJetEta)<2.4)&& mJ3J4 > 0) && nJetsPt25==4))&&((J1CSVbtag>0.898)&&(J2CSVbtag>0.898)))'#

# tomislav
cut = '((lPFIsoDB<0.12)&&(((HLT_IsoMu24_eta2p1_v_fired)&&(DiMuonMass<=60 && nElectrons==0 && nMuons==1 && abs(muonEta)<2.1 && muonPt>25)&&(abs(dz)<0.5&&abs(l1DXY)<0.02)&&(Mt>50)&&(MET>30))&&((highestJetPt >25 && secondJetPt>25 && abs(highestJetEta)<2.4 && abs(secondJetEta)<2.4) && nJetsPt25>=2)))'

I = -1
F = -1
#path = '../plots/newnew_v_newold/ttbar/datacomp_'
#path = '../plots/newnew_v_oldold/ttbar/datacomp_'
path = '../plots/triple/tomislav/XXX_datacomp_'
can = TCanvas('can','can',800,900)
for leaf in leafs:
 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

 hnwr,hnwrSize,hnwrSizePart,hnwrEvents = h.gram(data_tree_nwr,leaf,xmin,xmax,steps,cut,I,F)
 hnwr.SetName("hnwr")
 hnwr.Scale(1./hnwr.Integral())
 nwrMax = hnwr.GetMaximum()
 hnwr.SetLineColor(ROOT.EColor.kGreen+3)
 hnwr.SetLineWidth(4)

 hnew,hnewSize,hnewSizePart,hnewEvents = h.gram(data_tree_new,leaf,xmin,xmax,steps,cut,I,F)
 hnew.SetName("hnew")
 hnew.Scale(1./hnew.Integral())
 newMax = hnew.GetMaximum()
 hnew.SetLineColor(9)
 hnew.SetLineWidth(3)

 hold,holdSize,holdSizePart,holdEvents = h.gram(data_tree_old,leaf,xmin,xmax,steps,cut,I,F)
 hold.SetName("hold")
 hold.Scale(1./hold.Integral())
 oldMax = hold.GetMaximum()
 hold.SetLineColor(46)
 hold.SetLineWidth(2)
 hold.SetTitle(leaf)

 leg=TLegend(0.5,0.5,0.9,0.8)
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 leg.AddEntry(hold,'Old GT, Old Data')
 leg.AddEntry(hnew,'New GT, New Data')
 leg.AddEntry(hnwr,'New GT, RerunJets, New Data')
 #leg.AddEntry(hold,'Old Data')
 #leg.AddEntry(hnew,'New Data')
 #leg.AddEntry(hold,'Old Algo')
 #leg.AddEntry(hnew,'New Algo')

 can.cd()
 hnwr.SetMaximum(1.1*max(newMax,oldMax))
 hnwr.SetTitle(leaf)
 hnwr.Draw('hist')
 hnew.Draw('sames,hist')
 hold.Draw('sames,hist')
 leg.Draw('sames')

 can.Update()
 print('you just read '+leaf)
# save = raw_input ('Press Enter to Continue (type save to save)\n')
# if save == 'save':
 can.Print(path+leaf+'.png') 
