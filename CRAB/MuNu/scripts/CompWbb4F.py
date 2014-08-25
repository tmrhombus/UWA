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

file_wbb4f_filename = '../plots/19aout_W4F2_wbb.root' 
file_wbb4f = TFile(file_wbb4f_filename)

path = '../plots/19aout_4Fcomp'

leafs = [
#'J1_pt',
#'J2_pt',
#'muon_pt',
#'met_pt',
'mt'
]

"../plots/PS5_1aout_2j2525_2bt_J1_pt.root",
"../plots/PS5_1aout_2j2525_2bt_J2_pt.root",
"../plots/PS5_1aout_2j2525_2bt_muon_pt.root",
"../plots/PS5_1aout_2j2525_2bt_met_pt.root",
"../plots/PS5_1aout_2j2525_2bt_mt.root"
files = [
#TFile("../plots/PS5_1aout_2j2525_2bt_J1_pt.root"),
#TFile("../plots/PS5_1aout_2j2525_2bt_J2_pt.root"),
#TFile("../plots/PS5_1aout_2j2525_2bt_muon_pt.root"),
#TFile("../plots/PS5_1aout_2j2525_2bt_met_pt.root"),
TFile("../plots/PS5_19aout_2j2525_2bt_mt.root ")
]

can = TCanvas('can','can',800,800)
for file5f,leaf in zip(files,leafs):
 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

 wbb_n_plot = file5f.Get("wbbnih")
 wbb_n_plot.SetName("wbb_n_plot")
 wbb_n_plot.SetLineColor(ROOT.EColor.kGreen-6)
 wbb_n_plot.SetLineStyle(3)
 wbb_n_plot.SetLineWidth(1)
 wbb_1_plot = file5f.Get("wbb1ih")
 wbb_1_plot.SetName("wbb_1_plot")
 wbb_n_plot.SetLineColor(ROOT.EColor.kYellow-6)
 wbb_n_plot.SetLineStyle(3)
 wbb_n_plot.SetLineWidth(1)
 wbb_2_plot = file5f.Get("wbb2ih")
 wbb_2_plot.SetName("wbb_2_plot")
 wbb_2_plot.SetLineColor(ROOT.EColor.kRed-6)
 wbb_2_plot.SetLineStyle(3)
 wbb_2_plot.SetLineWidth(1)
 wbb_3_plot = file5f.Get("wbb3ih")
 wbb_3_plot.SetName("wbb_3_plot")
 wbb_3_plot.SetLineColor(ROOT.EColor.kCyan-6)
 wbb_3_plot.SetLineStyle(3)
 wbb_3_plot.SetLineWidth(1)
 wbb_4_plot = file5f.Get("wbb4ih")
 wbb_4_plot.SetName("wbb_4_plot")
 wbb_4_plot.SetLineColor(ROOT.EColor.kMagenta-6)
 wbb_4_plot.SetLineStyle(3)
 wbb_4_plot.SetLineWidth(1)

 wbb_5f_plot = wbb_n_plot.Clone()
 wbb_5f_plot.SetName("wbb_5f_plot")
 wbb_5f_plot.Add(wbb_1_plot)
 wbb_5f_plot.Add(wbb_2_plot)
 wbb_5f_plot.Add(wbb_3_plot)
 wbb_5f_plot.Add(wbb_4_plot)
 wbb_5f_plot.SetLineWidth(3)
 wbb_5f_plot.SetLineColor(ROOT.EColor.kBlue)
 wbb_5f_plot.SetLineStyle(1)

 wbb_4f_plot = file_wbb4f.Get(leaf)
 wbb_4f_plot.SetName("wbb_4f_plot")
 wbb_4f_plot.SetLineColor(ROOT.EColor.kRed)
 wbb_4f_plot.SetLineWidth(2)
 wbb_4f_plot.SetLineStyle(1)
 
 leg=TLegend(0.5,0.5,0.9,0.7)
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 leg.AddEntry(wbb_4f_plot,'4 Flavor')
 leg.AddEntry(wbb_5f_plot,'5 Flavor')

 can.cd()
 #hnwr.SetMaximum(0.07)
 wbb_5f_plot.SetTitle(leaf)
 wbb_5f_plot.Draw('hist')
 wbb_4f_plot.Draw('hist,sames')
 #leg.Draw('sames')
 #gStyle.SetOptStat(1122)

 can.Update()
 print('you just read '+leaf)
 #print('Nr. Events:  %s'%(hnwr.Integral()))
 #print('Nr. Events:  %s'%(hnwr.Integral(-10,1000)))
 #print('Nr. Entries: %s'%(hnwr.GetEntries()))
# save = raw_input ('Press Enter to Continue (type save to save)\n')
# if save == 'save':
 can.Print(path+'_'+leaf+'.png') 
