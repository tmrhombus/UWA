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

data_filename = '../data/post_synch_v0/Data_B.root' 

cut_type = 'wbb'
path = '../scripts/synch/Data_norm_%s'%(cut_type)

data_file  = TFile( data_filename)
eventTreeLocation = 'muNuEventTree/eventTree'
data_tree  =  data_file.Get(eventTreeLocation) 

out_file = gROOT.FindObject("%s.root"%(path))
if out_file: out_file.Close()
out_file = TFile("%s.root"%(path),"RECREATE","synching")

leafs = [
'J1_pt',
'J2_pt',
'muon_pt',
'met_pt',
'mt'
]

cut = '(2>1)'

if cut_type is 'wbb':
 cut='(((J1_idLooseJet)&&(J2_idLooseJet))&&(muNuRelPFIsoDB_A<0.12)&&(((((HLT_IsoMu24_eta2p1_v_fired)&&(nrEle==0 && nrMu==1 && abs(muon_eta)<2.1 && muon_pt>30)&&(nJets24Pt25==0))&&(2>1))&&((J1_CSVbtag>0.898)&&(J2_CSVbtag>0.898)))&&((J1_pt >25 && J2_pt>25 && abs(J1_eta)<2.4 && abs(J2_eta)<2.4)&& J3_pt<25)) && mt>45)'

if cut_type is 'tt_me':
 cut='(((J1_idLooseJet)&&(J2_idLooseJet))&&(muNuRelPFIsoDB_A<0.12)&&(((((HLT_IsoMu24_eta2p1_v_fired)&&(nrEle==1 && nrMu==1 && abs(muon_eta)<2.1 && muon_pt>30)&&(2>1)&&(mt>45))&&(2>1))&&(((J1_CSVbtag>0.898))))&&((J1_pt>25 && J2_pt>25 && abs(J1_eta)<2.4 && abs(J2_eta)<2.4) && J3_pt<25)) && mt>45)'

if cut_type is 'tt_m':
 cut='((((J1_idLooseJet)&&(J2_idLooseJet))&&(J3_idLooseJet))&&(muNuRelPFIsoDB_A<0.12)&&(((((HLT_IsoMu24_eta2p1_v_fired)&&(nrEle==0 && nrMu==1 && abs(muon_eta)<2.1 && muon_pt>30)&&(2>1)&&(mt>45))&&(2>1))&&((J1_CSVbtag>0.898)&&(J2_CSVbtag>0.898)))&&(((J1_pt >25 && J2_pt>25 && abs(J1_eta)<2.4 && abs(J2_eta)<2.4)&& J3_pt  > 25 && abs(J3_eta) <  2.4))))'

I = -1
F = -1
can = TCanvas('can','can',800,800)
for leaf in leafs:
 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

 hnwr,hnwrSize,hnwrSizePart,hnwrEvents = h.gram(data_tree,leaf,xmin,xmax,steps,cut,I,F)
 hnwr.SetName("hnwr")
 hnwr.Scale(1./hnwr.Integral())
 nwrMax = hnwr.GetMaximum()
 hnwr.SetLineColor(ROOT.EColor.kGreen+3)
 hnwr.SetLineWidth(3)

 leg=TLegend(0.5,0.5,0.9,0.7)
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 leg.AddEntry(hnwr,'Tom 2012B')

 can.cd()
 #hnwr.SetMaximum(0.07)
 hnwr.SetTitle(leaf)
 hnwr.Draw('hist')
 leg.Draw('sames')
 gStyle.SetOptStat(1122)

 can.Update()
 print('you just read '+leaf)
# save = raw_input ('Press Enter to Continue (type save to save)\n')
# if save == 'save':
 can.Print(path+'_'+leaf+'.png') 
 hnwr.SetName(leaf)
 out_file.Write()
 hnwr.Delete()
