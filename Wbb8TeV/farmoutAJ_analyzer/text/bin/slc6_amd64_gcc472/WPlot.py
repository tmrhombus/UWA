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

extraName = ''

leafa = 'Mt'
leafb = 'MtCal'

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leafa)
I = xmin
F = xmax

xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.0001f' %(float((xmax-xmin))/(steps))
title = xtitle #+' Data v MC'

c = TCanvas('c','Canvas Named c',canx,cany)
theFileA = TFile('../plots/'+leafa+extraName+'.root')
theFileB = TFile('../plots/'+leafb+extraName+'.root')

print("W + Beautiful")
hnA = theFileA.Get('hn')
hnA.SetName('hnA')
bminA = hnA.GetXaxis().FindBin(xmin)
bmaxA = hnA.GetXaxis().FindBin(xmax)
hnA.SetFillColor(wl)
hnASize = hnA.Integral(bminA,bmaxA)
print(hnASize)
###
h1A = theFileA.Get('h1')
h1A.SetName('h1A') 
h1A.SetFillColor(wc)
h1ASize = h1A.Integral(bminA,bmaxA)
print(h1ASize)
###
h2A = theFileA.Get('h2')
h2A.SetName('h2A') 
h2A.SetFillColor(wcc)
h2ASize = h2A.Integral(bminA,bmaxA)
print(h2ASize)
###
h3A = theFileA.Get('h3')
h3A.SetName('h3A') 
h3A.SetFillColor(wbb)
h3ASize = h3A.Integral(bminA,bmaxA)
print(h3ASize)
###
h4A = theFileA.Get('h4')
h4A.SetName('h4A') 
h4A.SetFillColor(tt)
h4ASize = h4A.Integral(bminA,bmaxA)
print(h4ASize)
###  

histA = TH1F('histA','histA',steps,xmin,xmax)
histA = hnA.Clone()
histA.SetName('histA')
histA.Add(h1A)
histA.Add(h2A)
histA.Add(h3A)
histA.Add(h4A)
histA.Draw()
maxA = histA.GetMaximum()
histA.SetFillColor(0)
histA.SetLineColor(8)
histA.SetLineWidth(3)
histA.SetLineStyle(1)

print("W + Beautiful")
hnB = theFileB.Get('hn')
hnB.SetName('hnB')
bminB = hnB.GetXaxis().FindBin(xmin)
bmaxB = hnB.GetXaxis().FindBin(xmax)
hnB.SetFillColor(wl)
hnBSize = hnB.Integral(bminB,bmaxB)
print(hnBSize)
###
h1B = theFileB.Get('h1')
h1B.SetName('h1B') 
h1B.SetFillColor(wc)
h1BSize = h1B.Integral(bminB,bmaxB)
print(h1BSize)
###
h2B = theFileB.Get('h2')
h2B.SetName('h2B') 
h2B.SetFillColor(wcc)
h2BSize = h2B.Integral(bminB,bmaxB)
print(h2BSize)
###
h3B = theFileB.Get('h3')
h3B.SetName('h3B') 
h3B.SetFillColor(wbb)
h3BSize = h3B.Integral(bminB,bmaxB)
print(h3BSize)
###
h4B = theFileB.Get('h4')
h4B.SetName('h4B') 
h4B.SetFillColor(tt)
h4BSize = h4B.Integral(bminB,bmaxB)
print(h4BSize)
###  

histB = TH1F('histB','histB',steps,xmin,xmax)
histB = hnB.Clone()
histB.SetName('histB')
histB.Add(h1B)
histB.Add(h2B)
histB.Add(h3B)
histB.Add(h4B)
histB.Draw()
maxB = histB.GetMaximum()
histB.SetFillColor(0)
histB.SetLineColor(9)
histB.SetLineWidth(2)
histB.SetLineStyle(3)

leg = TLegend(0.68,0.2,0.9,0.8)
leg.SetFillColor(0)
leg.AddEntry(histA,leafa)
leg.AddEntry(histB,leafb) 

histA.SetMaximum(1.1*max(maxA,maxB))
histA.Draw()
histB.Draw('sames')
#wbbnihB.Draw()
#wbbnihA.Draw('sames')
leg.Draw('sames')
cpr.prelim_noLumi()
tex.SetTextAlign(11)#left, bottom
tex.DrawLatex(0.17,0.9,title)
c.Update()
save2 = raw_input ('Press Enter to Continue (type save to save)\n')
if save2 == 'save':
 c.Print('../plots/'+leafa+'_'+leafb+'_comp'+extraName+'.png')
print('')
c.Close()
