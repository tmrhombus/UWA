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

#Start the Plotting Program
leaf = 'Mt'

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
I = xmin
F = xmax

path = '../plots/TTbarError'
extraName=''
fileName = path+extraName+'_'+leaf
theFile = TFile(fileName+'.root')

xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.0001f' %(float((xmax-xmin))/(steps))
title = xtitle #+' Data v MC'

c = TCanvas('c','Canvas Named c',canx,cany)

print("TTbar")
httbar = theFile.Get('httbar')
bminA = httbar.GetXaxis().FindBin(xmin)
bmaxA = httbar.GetXaxis().FindBin(xmax)
httbar.SetLineWidth(3)
httbar.SetLineColor(28)
httbarSize = httbar.Integral(bminA,bmaxA)
print(httbarSize)
###
print("TTbar Up")
httbarUp = theFile.Get('httbarUp')
httbarUpSize = httbarUp.Integral(bminA,bmaxA)
httbarUp.SetLineWidth(2)
httbarUp.SetLineStyle(2)
httbarUp.SetLineColor(9)
print(httbarUpSize)
###
print("TTbar Down")
httbarDown = theFile.Get('httbarDown')
httbarDownSize = httbarDown.Integral(bminA,bmaxA)
httbarDown.SetLineWidth(2)
httbarDown.SetLineStyle(2)
httbarDown.SetLineColor(8)
print(httbarDownSize)

leg = TLegend(0.68,0.2,0.9,0.8)
leg.SetFillColor(0)
leg.AddEntry(httbar,'t#bar{t}')
leg.AddEntry(httbarUp,'t#bar{t}+#epsilon')
leg.AddEntry(httbarDown,'t#bar{t}-#epsilon')

httbar.SetMaximum(1.1*httbar.GetMaximum())
httbar.Draw('hist')
httbarUp.Draw('sames,hist')
httbarDown.Draw('sames,hist')
leg.Draw('sames')
cpr.prelim_noLumi()
tex.SetTextAlign(11)#left, bottom
tex.DrawLatex(0.17,0.9,title)
c.Update()
save2 = raw_input ('Press Enter to Continue (type save to save)\n')
if save2 == 'save':
 c.Print(fileName+'.png')
print('')
c.Close()
