#!/usr/bin/env python
'''
Makes nice plots from histograms made using makeHistos.py
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TLegend,TCanvas,TFile,TLatex,gROOT,gStyle
import histoRange as hr

leaf='mt'

lumi, steps, xmin, xmax, xtitle, xunits = hr.ranger(leaf)
lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)
xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.001f' %((xmax-xmin)/(steps))
title = xtitle+' Data v MC'

filename = []
filename.append('../scratch/aamt2j0bIso2r_0_20.root')
#canvas attributes
canx = 1300
cany = 900

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
#color scheme
d = 1
q = ROOT.EColor.kRed+1
z = ROOT.EColor.kOrange-3
d = ROOT.EColor.kYellow-3
tt = ROOT.EColor.kGreen+1
ts = ROOT.EColor.kGreen-5
ttw = ROOT.EColor.kGreen+3 
ttb = ROOT.EColor.kGreen-9
wtau = ROOT.EColor.kAzure-7
wbx = ROOT.EColor.kCyan
wbb = 51#ROOT.EColor.kCyan
wcc = ROOT.EColor.kAzure+2
wc = ROOT.EColor.kBlue+1
wl = ROOT.EColor.kAzure+10

for i in filename:
 c = TCanvas('c','Canvas Named c',canx,cany) 
 theFile = TFile(i)
 
 dataih = theFile.Get('dataih')
 dataih.Sumw2()
 dataih.SetMarkerStyle(22)
 dataih.SetMarkerSize(1.2)
 dmax = dataih.GetMaximum()
 
 qh = theFile.Get('qh')
 qh.SetFillColor(q)
 zih = theFile.Get('zih')
 zih.SetFillColor(z)
 dih = theFile.Get('dih')
 dih.SetFillColor(d)
 ttih = theFile.Get('ttih')
 ttih.SetFillColor(tt)
 tsih = theFile.Get('tsih')
 tsih.SetFillColor(ts)
 ttwih = theFile.Get('ttwih')
 ttwih.SetFillColor(ttw)
 ttbih = theFile.Get('ttbih')
 ttbih.SetFillColor(ttb)
 wtih = theFile.Get('wtih')
 wtih.SetFillColor(wtau)
 wbih = theFile.Get('wbih')
 wbih.SetFillColor(wbx)
 wbbih = theFile.Get('wbbih')
 wbbih.SetFillColor(wbb)
 wccih = theFile.Get('wccih')
 wccih.SetFillColor(wcc)
 wcih = theFile.Get('wcih')
 wcih.SetFillColor(wc)
 wlih = theFile.Get('wlih')
 wlih.SetFillColor(wl)
 
 hs = THStack('hs','')
 hs.SetTitle('')
 hs.Add(qh)
 hs.Add(zih)
 hs.Add(dih)
 hs.Add(ttih)
 hs.Add(tsih)
 hs.Add(ttwih)
 hs.Add(ttbih)
 hs.Add(wtih)
 hs.Add(wbih)
 hs.Add(wbbih)
 hs.Add(wccih)
 hs.Add(wcih)
 hs.Add(wlih)
 hs.Draw()
 hs.GetXaxis().SetTitle(xlabel)
 hs.GetYaxis().SetTitleOffset(1.5)
 hs.GetYaxis().SetTitle(ylabel)
 hsmax = hs.GetMaximum()
 
 leg=TLegend(0.7,0.4,0.9,0.8)
 leg.AddEntry(dataih,'data')
 leg.AddEntry(wlih,'W(#mu#nu)+light')
 leg.AddEntry(wcih,'W(#mu#nu)+c')
 leg.AddEntry(wccih,'W(#mu#nu)+cc')
 leg.AddEntry(wbbih,'W(#mu#nu)+bb')
 leg.AddEntry(wbih,'W(#mu#nu)+bx')
 leg.AddEntry(wtih,'W(#tau#nu)')
 leg.AddEntry(ttbih,'t#bar{t}')
 leg.AddEntry(ttwih,'t_tW')
 leg.AddEntry(tsih,'t_s')
 leg.AddEntry(ttih,'t_t')
 leg.AddEntry(dih,'WW,WZ')
 leg.AddEntry(zih,'Drell-Yan')
 leg.AddEntry(qh,'QCD')
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 
 c.cd()
 if dmax>hsmax:
  hs.SetMaximum(1.2*dmax)
 else:
  hs.SetMaximum(1.2*hsmax)
 hs.Draw()
 dataih.Draw('sames')
 leg.Draw('sames')
 tex.DrawLatex(0,1,title)
 tex.SetTextSize(0.03)
 tex.SetTextAlign(33)
 tex.DrawLatex(0.87,0.87,lumiTitle)
 c.Update()
 c.Print('../scratch/testplot.png')
