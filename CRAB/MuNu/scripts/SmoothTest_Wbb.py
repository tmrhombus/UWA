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

w1_filename = '../data/post_synch_v0/W1Jet.root'
w2_filename = '../data/post_synch_v0/W2Jet.root'
w3_filename = '../data/post_synch_v0/W3Jet.root'
w4_filename = '../data/post_synch_v0/W4Jet.root'
wn_filename = '../data/post_synch_v0/WJets.root'

w1_file  = TFile( w1_filename )
w2_file  = TFile( w2_filename )
w3_file  = TFile( w3_filename )
w4_file  = TFile( w4_filename )
wn_file  = TFile( wn_filename )
eventTreeLocation = 'muNuEventTree/eventTree'
w1_tree  =  w1_file.Get(eventTreeLocation) 
w2_tree  =  w2_file.Get(eventTreeLocation) 
w3_tree  =  w3_file.Get(eventTreeLocation) 
w4_tree  =  w4_file.Get(eventTreeLocation) 
wn_tree  =  wn_file.Get(eventTreeLocation) 

leafs = [
'J1_pt',
'mt',
'nJetsPt25',
'met_pt',
'muon_pt',
'vertices',
]

cut_standard = '(((weightFactor * 19751.0 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVT_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVT_SFl)))) * ((muNuRelPFIsoDB_A<0.12) && ((abs(muon_eta)<2.1 && muon_pt>30 && HLT_IsoMu24_eta2p1_v_fired) && (nrMu==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && (mt>45))))'

cut_modified = '(((weightFactor * 19751.0 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVM_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVM_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFl)))) * ((muNuRelPFIsoDB_A<0.12) && ((abs(muon_eta)<2.1 && muon_pt>30 && HLT_IsoMu24_eta2p1_v_fired) && (nrMu==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.679) && (J2_CSVbtag>0.679) && (mt>45))))'   # 2 medium btags

#cut_modified = ' (((weightFactor * 19751.0 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVL_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVL_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVL_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVL_SFl)))) * ((muNuRelPFIsoDB_A<0.12) && ((abs(muon_eta)<2.1 && muon_pt>30 && HLT_IsoMu24_eta2p1_v_fired) && (nrMu==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.244) && (J2_CSVbtag>0.244) && (mt>45))))'  # 2 light btags


I = -1
F = -1
path = '../plots/SmoothTest_Wbb_'
can = TCanvas('can','can',800,900)
for leaf in leafs:
 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

 h1std,h1stdSize,h1stdSizePart,h1stdEvents = h.gram(w1_tree,leaf,xmin,xmax,steps,cut_standard,I,F)
 h1std.SetName("h1std")
 h2std,h2stdSize,h2stdSizePart,h2stdEvents = h.gram(w2_tree,leaf,xmin,xmax,steps,cut_standard,I,F)
 h2std.SetName("h2std")
 h3std,h3stdSize,h3stdSizePart,h3stdEvents = h.gram(w3_tree,leaf,xmin,xmax,steps,cut_standard,I,F)
 h3std.SetName("h3std")
 h4std,h4stdSize,h4stdSizePart,h4stdEvents = h.gram(w4_tree,leaf,xmin,xmax,steps,cut_standard,I,F)
 h4std.SetName("h4std")
 hnstd,hnstdSize,hnstdSizePart,hnstdEvents = h.gram(wn_tree,leaf,xmin,xmax,steps,cut_standard,I,F)
 hnstd.SetName("hnstd")
 
 hstd = TH1F("hstd","hstd",steps,xmin,xmax)
 hstd.Add(h1std)
 hstd.Add(h2std)
 hstd.Add(h3std)
 hstd.Add(h4std)
 hstd.Add(hnstd)
 hstd.Sumw2()
 hstd_err = hstd.Clone()
 hstd_err.SetName("hstd_err")

 hstd.Scale(1./hstd.Integral())
 stdMax = hstd.GetMaximum()
 hstd.SetLineColor(ROOT.EColor.kGreen+3)
 hstd.SetLineWidth(4)

 h1mod,h1modSize,h1modSizePart,h1modEvents = h.gram(w1_tree,leaf,xmin,xmax,steps,cut_modified,I,F)
 h1mod.SetName("h1mod")
 h2mod,h2modSize,h2modSizePart,h2modEvents = h.gram(w2_tree,leaf,xmin,xmax,steps,cut_modified,I,F)
 h2mod.SetName("h2mod")
 h3mod,h3modSize,h3modSizePart,h3modEvents = h.gram(w3_tree,leaf,xmin,xmax,steps,cut_modified,I,F)
 h3mod.SetName("h3mod")
 h4mod,h4modSize,h4modSizePart,h4modEvents = h.gram(w4_tree,leaf,xmin,xmax,steps,cut_modified,I,F)
 h4mod.SetName("h4mod")
 hnmod,hnmodSize,hnmodSizePart,hnmodEvents = h.gram(wn_tree,leaf,xmin,xmax,steps,cut_modified,I,F)
 hnmod.SetName("hnmod")
 
 hmod = TH1F("hmod","hmod",steps,xmin,xmax)
 hmod.Add(h1mod)
 hmod.Add(h2mod)
 hmod.Add(h3mod)
 hmod.Add(h4mod)
 hmod.Add(hnmod)
 hmod.Sumw2()
 hmod_err = hmod.Clone()
 hmod_err.SetName("hmod_err")

 hmod.Scale(1./hmod.Integral())
 modMax = hmod.GetMaximum()
 hmod.SetLineColor(ROOT.EColor.kRed)
 hmod.SetLineWidth(4)



 leg=TLegend(0.5,0.5,0.9,0.8)
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 leg.AddEntry(hstd,'Standard, 2CSV Tight')
 leg.AddEntry(hmod,'Modified, 2CSV Medium')

 can.cd()
 hstd.SetMaximum(1.1*max(stdMax,modMax))
 hstd.SetTitle(leaf)
 hstd.Draw('hist')
 hmod.Draw('sames,hist')
 leg.Draw('sames')

 can.Update()
 print('you just read '+leaf)
# save = raw_input ('Press Enter to Continue (type save to save)\n')
# if save == 'save':
 can.Print(path+leaf+'.png') 
