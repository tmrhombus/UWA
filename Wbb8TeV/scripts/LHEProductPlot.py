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
import cmsPrelim as cpr
import parameters as p
 
#canvas attributes
canx = 800 # for one plot on page
#canx = 550 # for two plots on page with text
#canx = 600 # for two plots on page just title
#canx = 500 # for three plots on page with text
#canx = 400 # for three plots on page with just title

cany = 900

#color scheme
tt = ROOT.EColor.kAzure+1
wl = ROOT.EColor.kAzure+10
wc = ROOT.EColor.kBlue+1
wcc = ROOT.EColor.kAzure+2
wbb = 51#ROOT.EColor.kCyan

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')

# get parameters to run on
I = 4
F = 10

extraName = '_scaled'

leaf = 'LHEProduct'

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.0001f' %(float((xmax-xmin))/(steps))
title = xtitle #+' Data v MC'

c = TCanvas('c','Canvas Named c',canx,cany)
theFile = TFile('../plots/LHEProduct'+extraName+'.root')


### W 
print("W + Beautiful")
wbbnih = theFile.Get('wbbnih')
bmin = wbbnih.GetXaxis().FindBin(xmin)
bmax = wbbnih.GetXaxis().FindBin(xmax)
wbbnih.SetFillColor(wl)
wbbnihSize = wbbnih.Integral(bmin,bmax)
#wbbnih.Scale(1/wbbnihSize)
###
wbb1ih = theFile.Get('wbb1ih')
wbb1ih.SetFillColor(wc)
wbb1ihSize = wbb1ih.Integral(bmin,bmax)
###
wbb2ih = theFile.Get('wbb2ih')
wbb2ih.SetFillColor(wcc)
wbb2ihSize = wbb2ih.Integral(bmin,bmax)
###
wbb3ih = theFile.Get('wbb3ih')
wbb3ih.SetFillColor(wbb)
wbb3ihSize = wbb3ih.Integral(bmin,bmax)
###
wbb4ih = theFile.Get('wbb4ih')
wbb4ih.SetFillColor(tt)
wbb4ihSize = wbb4ih.Integral(bmin,bmax)
###  
totSize = wbbnihSize + wbb1ihSize + wbb2ihSize + wbb3ihSize + wbb4ihSize 
wbbnih.Scale(1/totSize)
wbb1ih.Scale(1/totSize)
wbb2ih.Scale(1/totSize)
wbb3ih.Scale(1/totSize)
wbb4ih.Scale(1/totSize)

hs = THStack('hs','')
hs.SetTitle('')
hs.Add(wbbnih)
hs.Add(wbb1ih)
hs.Add(wbb2ih)
hs.Add(wbb3ih)
hs.Add(wbb4ih)

hs.Draw()
hs.GetXaxis().SetTitle(xlabel)
hs.GetXaxis().SetRangeUser(xmin,xmax)
hs.GetYaxis().SetTitleOffset(1.5)
hs.GetYaxis().SetTitle(ylabel)

leg=TLegend(0.68,0.2,0.9,0.8)
leg.SetFillColor(0)

leg.AddEntry(wbbnih,'W+n Jets','f')
leg.AddEntry(wbb1ih,'W+1 Jet','f')
leg.AddEntry(wbb2ih,'W+2 Jets','f')
leg.AddEntry(wbb3ih,'W+3 Jets','f')
leg.AddEntry(wbb4ih,'W+4 Jets','f')

hs.SetMaximum(0.6)
c.cd()
hs.Draw()
leg.Draw('sames')
cpr.prelim_noLumi()
tex.SetTextAlign(11)#left, bottom
tex.DrawLatex(0.17,0.9,title)
c.Update()
print('you are on '+leaf)
save2 = raw_input ('Press Enter to Continue (type save to save)\n')
if save2 == 'save':
 c.Print('../plots/LHEProduct'+extraName+'.png')
print('')
c.Close()
