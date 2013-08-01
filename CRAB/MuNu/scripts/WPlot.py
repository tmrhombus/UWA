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
wl = 0
#wl = ROOT.EColor.kAzure+10
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

extraName = ''

leafa = 'Mt'
leafb = 'MtCal'

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leafa)

xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.0001f' %(float((xmax-xmin))/(steps))
title = xtitle #+' Data v MC'

c = TCanvas('c','Canvas Named c',canx,cany)
theFileA = TFile('../plots/'+leafa+extraName+'.root')
theFileB = TFile('../plots/'+leafb+extraName+'.root')


### W 
print("W + Beautiful")
wbbnihA = theFileA.Get('wbbnih')
bmin = wbbnihA.GetXaxis().FindBin(xmin)
bmax = wbbnihA.GetXaxis().FindBin(xmax)
wbbnihA.SetFillColor(wl)
wbbnihASize = wbbnihA.Integral(bmin,bmax)
#wbbnihA.Scale(1/wbbnihASize)
###
wbb1ihA = theFileA.Get('wbb1ih')
wbb1ihA.SetFillColor(wc)
wbb1ihASize = wbb1ihA.Integral(bmin,bmax)
###
wbb2ihA = theFileA.Get('wbb2ih')
wbb2ihA.SetFillColor(wcc)
wbb2ihASize = wbb2ihA.Integral(bmin,bmax)
###
wbb3ihA = theFileA.Get('wbb3ih')
wbb3ihA.SetFillColor(wbb)
wbb3ihASize = wbb3ihA.Integral(bmin,bmax)
###
wbb4ihA = theFileA.Get('wbb4ih')
wbb4ihA.SetFillColor(tt)
wbb4ihASize = wbb4ihA.Integral(bmin,bmax)
###  
totSizeA = wbbnihASize + wbb1ihASize + wbb2ihASize + wbb3ihASize + wbb4ihASize 
#wbbnihA.Scale(1/totSizeA)
#wbb1ihA.Scale(1/totSizeA)
#wbb2ihA.Scale(1/totSizeA)
#wbb3ihA.Scale(1/totSizeA)
#wbb4ihA.Scale(1/totSizeA)

#hsA = THStack('hsA','')
#hsA.SetTitle('')
#hsA.Add(wbbnihA)
#hsA.Add(wbb1ihA)
#hsA.Add(wbb2ihA)
#hsA.Add(wbb3ihA)
#hsA.Add(wbb4ihA)

#hsA.Draw()
#hsA.GetXaxis().SetTitle(xlabel)
#hsA.GetXaxis().SetRangeUser(xmin,xmax)
#hsA.GetYaxis().SetTitleOffset(1.5)
#hsA.GetYaxis().SetTitle(ylabel)
#
#legA=TLegend(0.68,0.2,0.9,0.8)
#legA.SetFillColor(0)
#
#legA.AddEntry(wbbnihA,'W+n Jets','f')
#legA.AddEntry(wbb1ihA,'W+1 Jet','f')
#legA.AddEntry(wbb2ihA,'W+2 Jets','f')
#legA.AddEntry(wbb3ihA,'W+3 Jets','f')
#legA.AddEntry(wbb4ihA,'W+4 Jets','f')
#
#hsA.SetMaximum(0.6)
#c.cd()
#hsA.Draw()

histA = TH1F('histA','histA',steps,xmin,xmax)
histA = wbbnihA.Clone()
histA.Add(wbb1ihA)
histA.Add(wbb2ihA)
histA.Add(wbb3ihA)
histA.Add(wbb4ihA)
histA.Draw()
maxA = histA.GetMaximum()
histA.SetFillColor(0)
histA.SetLineColor(8)

print("W + Beautiful")
wbbnihB = theFileB.Get('wbbnih')
bmin = wbbnihB.GetXaxis().FindBin(xmin)
bmax = wbbnihB.GetXaxis().FindBin(xmax)
wbbnihB.SetFillColor(wl)
wbbnihBSize = wbbnihB.Integral(bmin,bmax)
#wbbnihB.Scale(1/wbbnihBSize)
###
wbb1ihB = theFileB.Get('wbb1ih')
wbb1ihB.SetFillColor(wc)
wbb1ihBSize = wbb1ihB.Integral(bmin,bmax)
###
wbb2ihB = theFileB.Get('wbb2ih')
wbb2ihB.SetFillColor(wcc)
wbb2ihBSize = wbb2ihB.Integral(bmin,bmax)
###
wbb3ihB = theFileB.Get('wbb3ih')
wbb3ihB.SetFillColor(wbb)
wbb3ihBSize = wbb3ihB.Integral(bmin,bmax)
###
wbb4ihB = theFileB.Get('wbb4ih')
wbb4ihB.SetFillColor(tt)
wbb4ihBSize = wbb4ihB.Integral(bmin,bmax)
###  
totSizeB = wbbnihBSize + wbb1ihBSize + wbb2ihBSize + wbb3ihBSize + wbb4ihBSize 
#wbbnihB.Scale(1/totSizeB)
#wbb1ihB.Scale(1/totSizeB)
#wbb2ihB.Scale(1/totSizeB)
#wbb3ihB.Scale(1/totSizeB)
#wbb4ihB.Scale(1/totSizeB)

#hsB = THStack('hsB','')
#hsB.SetTitle('')
#hsB.Add(wbbnihB)
#hsB.Add(wbb1ihB)
#hsB.Add(wbb2ihB)
#hsB.Add(wbb3ihB)
#hsB.Add(wbb4ihB)

#hsB.Draw()
#hsB.GetXaxis().SetTitle(xlabel)
#hsB.GetXaxis().SetRangeUser(xmin,xmax)
#hsB.GetYaxis().SetTitleOffset(1.5)
#hsB.GetYaxis().SetTitle(ylabel)
#
#legB=TLegend(0.68,0.2,0.9,0.8)
#legB.SetFillColor(0)
#
#legB.AddEntry(wbbnihB,'W+n Jets','f')
#legB.AddEntry(wbb1ihB,'W+1 Jet','f')
#legB.AddEntry(wbb2ihB,'W+2 Jets','f')
#legB.BddEntry(wbb3ihA,'W+3 Jets','f')
#legB.AddEntry(wbb4ihB,'W+4 Jets','f')
#
#hsB.SetMaximum(0.6)
#c.cd()
#hsB.Draw()

histB = TH1F('histB','histB',steps,xmin,xmax)
histB = wbbnihB.Clone()
histB.Add(wbb1ihB)
histB.Add(wbb2ihB)
histB.Add(wbb3ihB)
histB.Add(wbb4ihB)
histB.Draw()
maxB = histB.GetMaximum()
histB.SetFillColor(0)
histB.SetLineColor(9)

leg = TLegend(0.68,0.2,0.9,0.8)
leg.SetFillColor(0)
leg.AddEntry(histA,leafa)
leg.AddEntry(histB,leafb) 

histA.SetMaximum(1.1*max(maxA,maxB))
histA.Draw()
histB.Draw('sames')
leg.Draw('sames')
cpr.prelim_noLumi()
tex.SetTextAlign(11)#left, bottom
tex.DrawLatex(0.17,0.9,title)
c.Update()
save2 = raw_input ('Press Enter to Continue (type save to save)\n')
if save2 == 'save':
 c.Print('../plots/CompMet'+extraName+'.png')
print('')
c.Close()
