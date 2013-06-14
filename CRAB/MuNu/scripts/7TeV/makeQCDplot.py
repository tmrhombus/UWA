#!/usr/bin/env python
'''
Makes nice plots with ratio from histograms made using makeHistos.py
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
import histoRange as hr

leaf='mt'

lumi, steps, xmin, xmax, xtitle, xunits = hr.ranger(leaf)
lumiTitle = '#int L dt = %.1f fb^{-1}' %(lumi/1000.)
#xlabel = xtitle+' ['+xunits+']'
xlabel = 'Transverse Mass ['+xunits+']'
ylabel = 'Events/ %.001f' %((xmax-xmin)/(steps))
title = xtitle#+' Data v MC'
path = '../ForAN/'

jNr = 2
bNr = 0

name = []
name.append('QCDmt2j0bIso2unscaled_0_200')
name.append('QCDmt2j0bIso3unscaled_0_200')
name.append('QCDmt2j0bIso4unscaled_0_200')
#name.append('mt2j2bIso2unscaled_0_200')
#name.append('massDiMuon'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_20')
#name.append('massDiMuon'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_200')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_40')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_70')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_200')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_20')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_30')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_40')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_200')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_20')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_30')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_40')
#name.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_200')

#canvas attributes
canx = 775
cany = 900

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)

gStyle.SetOptStat('')
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

for i in name:
 c = TCanvas('c','Canvas Named c',canx,cany)
# p1 = TPad('p1','p1',0,0.3,1,1)
# p1.SetBottomMargin(0)
# p1.Draw()
# p1.cd()
 #p1.SetLogy()
 theFile = TFile(path+i+'.root')
 
 rebin = 1
 
 datanh = theFile.Get('datanh')
 datanh.Rebin(rebin)
 datanh.Sumw2()
 datanh.SetMarkerStyle(22)
 datanh.SetMarkerSize(1.2)
 dmax = datanh.GetMaximum()
 
 qh = theFile.Get('qh')
# qh.SetFillColor(q)
 qh.SetLineStyle(3)
 qh.SetLineWidth(3)
 qh.Rebin(rebin)

 znh = theFile.Get('znh')
 znh.SetFillColor(z)
 znh.Rebin(rebin)
 dnh = theFile.Get('dnh')
 dnh.SetFillColor(d)
 dnh.Rebin(rebin)
 stnh = theFile.Get('stnh')
 stnh.SetFillColor(tt)
 stnh.Rebin(rebin)
# tsnh = theFile.Get('tsnh')
# tsnh.SetFillColor(ts)
# tsnh.Rebin(rebin)
# ttwnh = theFile.Get('ttwnh')
# ttwnh.SetFillColor(ttw)
# ttwnh.Rebin(rebin)
 ttbnh = theFile.Get('ttbnh')
 ttbnh.SetFillColor(ttb)
 ttbnh.Rebin(rebin)
 wnh = theFile.Get('wnh')
 wnh.SetFillColor(wtau)
 wnh.Rebin(rebin)
# wtnh = theFile.Get('wtnh')
# wtnh.SetFillColor(wtau)
# wtnh.Rebin(rebin)
# wbnh = theFile.Get('wbnh')
# wbnh.SetFillColor(wbx)
# wbnh.Rebin(rebin)
# wbbnh = theFile.Get('wbbnh')
# wbbnh.SetFillColor(wbb)
# wbbnh.Rebin(rebin)
# wccnh = theFile.Get('wccnh')
# wccnh.SetFillColor(wcc)
# wccnh.Rebin(rebin)
# wcnh = theFile.Get('wcnh')
# wcnh.SetFillColor(wc)
# wcnh.Rebin(rebin)
# wlnh = theFile.Get('wlnh')
# wlnh.SetFillColor(wl)
# wlnh.Rebin(rebin)
 
 hs = THStack('hs','')
 hs.SetTitle('')
# hs.Add(qh)
 hs.Add(znh)
 hs.Add(dnh)
 hs.Add(stnh)
# hs.Add(tsnh)
# hs.Add(ttwnh)
 hs.Add(ttbnh)
 hs.Add(wnh)
# hs.Add(wtnh)
# hs.Add(wbnh)
# hs.Add(wbbnh)
# hs.Add(wccnh)
# hs.Add(wcnh)
# hs.Add(wlnh)
 hs.Draw()
 hs.GetXaxis().SetTitle(xlabel)
# hs.GetXaxis().SetRangeUser(50,140)
 hs.GetYaxis().SetTitleOffset(1.5)
 hs.GetYaxis().SetTitle(ylabel)
 hsmax = hs.GetMaximum()
 
 leg=TLegend(0.68,0.2,0.9,0.8)
 leg.AddEntry(datanh,'data')
# leg.AddEntry(wlnh,'W(#mu#nu)+light')
# leg.AddEntry(wcnh,'W(#mu#nu)+c')
# leg.AddEntry(wccnh,'W(#mu#nu)+cc')
# leg.AddEntry(wbbnh,'W(#mu#nu)+bb')
# leg.AddEntry(wbnh,'W(#mu#nu)+bx')
# leg.AddEntry(wtnh,'W(#tau#nu)')
 leg.AddEntry(wnh,'W')
 leg.AddEntry(ttbnh,'t#bar{t}')
# leg.AddEntry(ttwnh,'t_tW')
# leg.AddEntry(tsnh,'t_s')
# leg.AddEntry(ttnh,'t_t')
 leg.AddEntry(stnh,'Single Top')
 leg.AddEntry(dnh,'WW,WZ')
 leg.AddEntry(znh,'Drell-Yan')
 leg.AddEntry(qh,'Template')
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 
 if dmax>hsmax:
  hs.SetMaximum(1.2*dmax)
 else:
  hs.SetMaximum(1.2*hsmax)
# hs.SetMaximum(4000)
 hs.Draw()
 datanh.Draw('sames')
 qh.Draw('sames')
 leg.Draw('sames')
 tex.DrawLatex(0,1,'Transverse Mass')
 tex.DrawLatex(0,1,title)
 tex.DrawLatex(0.15,0.88,str(jNr)+' Jets')
 tex.DrawLatex(0.15,0.8,str(bNr)+' bTags')
# tex.SetTextSize(0.06)
# tex.DrawLatex(0.26,0.88,'2 Jets')
# tex.DrawLatex(0.31,0.82,'one w/ b')
# tex.DrawLatex(0.31,0.76,'other w/ #eta > 2.8')
 tex.SetTextSize(0.03)
 tex.SetTextAlign(33)
 tex.DrawLatex(0.87,0.87,lumiTitle)
 tex.SetTextSize(0.07)
 tex.SetTextAlign(13)
 
 c.Update()
 c.Print(path+i+'.png')
 c.Close()
