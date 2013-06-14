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

leaf=[]
leaf.append('met')
leaf.append('meta')
leaf.append('metjesMpt')
leaf.append('metjesPpt')
leaf.append('metonept')

iso=[]
iso.append('2')
#iso.append('3')
#iso.append('4')

rangg=[]
rangg.append('20')
#rangg.append('30')
#rangg.append('40')
rangg.append('200')

path = '../MetLook/'
leef = 'met'
lumi, steps, xmin, xmax, xtitle, xunits = hr.ranger(leef)
lumiTitle = '#int L dt = %.1f fb^{-1}' %(lumi/1000.)
xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.001f' %((xmax-xmin)/(steps))
title = xtitle+' Data v MC'

jNr = 2
bNr = 0

#canvas attributes
canx = 1200
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

for s in iso:
 for r in rangg:
  c = TCanvas('c','Canvas Named c',canx,cany)
  
  metFile=TFile(path+'met'+str(jNr)+'j'+str(bNr)+'bIso'+s+'rescaled_0_'+r+'.root')
  metAFile=TFile(path+'meta'+str(jNr)+'j'+str(bNr)+'bIso'+s+'rescaled_0_'+r+'.root')
  metMFile=TFile(path+'metjesMpt'+str(jNr)+'j'+str(bNr)+'bIso'+s+'rescaled_0_'+r+'.root')
  metPFile=TFile(path+'metjesPpt'+str(jNr)+'j'+str(bNr)+'bIso'+s+'rescaled_0_'+r+'.root')
  metOFile=TFile(path+'metonept'+str(jNr)+'j'+str(bNr)+'bIso'+s+'rescaled_0_'+r+'.root')

  hhh = metFile.Get('hh')
  hhA = metAFile.Get('hh')
  hhM = metMFile.Get('hh')
  hhP = metPFile.Get('hh')
  hhO = metOFile.Get('hh')

  hhh.SetLineColor(q)
  hhh.SetLineWidth(2)
  hhA.SetLineColor(z)
  hhA.SetLineWidth(2)
  hhM.SetLineColor(d)
  hhM.SetLineWidth(2)
  hhP.SetLineColor(ttb)
  hhP.SetLineWidth(2)
  hhO.SetLineColor(wc)
  hhO.SetLineWidth(2)

  c.cd()
  hhh.Draw()
  hhh.SetTitle('')
  hhh.GetXaxis().SetTitle(xlabel)
  hhh.GetYaxis().SetTitleOffset(1.5)
  hhh.GetYaxis().SetTitle(ylabel)
  hhA.Draw('same')
  hhM.Draw('same')
  hhP.Draw('same')
  hhO.Draw('same')

  leg=TLegend(0.4,0.4,0.9,0.8)
  leg.AddEntry(hhh,'Calibrated MET')
  leg.AddEntry(hhA,'Uncalibrated MET')
  leg.AddEntry(hhM,'Jet Scale -')
  leg.AddEntry(hhP,'Jet Scale +')
  leg.AddEntry(hhO,'Type 1 Correct (jets only)')
  leg.SetFillColor(0)
  leg.SetBorderSize(0)
  leg.Draw('sames')
 
  tex.DrawLatex(0,1,'MET Comparison')
  tex.SetTextSize(0.04)
  tex.DrawLatex(0.5,0.4,str(jNr)+' Jets')
  tex.DrawLatex(0.5,0.35,str(bNr)+' bTags')
#  tex.DrawLatex(0.5,0.3,'No QCD')
#  tex.DrawLatex(0.5,0.3,'QCD Iso > 0.'+str(s))
#  tex.DrawLatex(0.5,0.25,'QCD Fit MT 0-'+str(r))
  tex.SetTextSize(0.07)
  c.Print(path+'metComp'+str(jNr)+'j'+str(bNr)+'bIso'+s+'0_'+r+'.png')
