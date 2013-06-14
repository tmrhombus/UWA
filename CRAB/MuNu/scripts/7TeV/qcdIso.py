#!/usr/bin/env python
'''
Plots a variety of leafs with progressing cuts
and a graph to show the cuts effects.
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *

import cuts as ct
import histoRangeQCD as hr

# Drawing Options
tex=ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)

gStyle.SetOptStat('')
gStyle.SetStatY(0.9)
gStyle.SetStatX(0.9)
gStyle.SetStatW(0.2)
gStyle.SetStatH(0.2)
gStyle.SetStatColor(0)

gROOT.SetStyle('Plain')

#canvas attributes
canx = 950
cany = 900

# Available Leaves: mt, met, ptMu, massDiNoBJets, massDiJets, ptDiJets, isoMuPFIsoRho, etaMu'
leaf = 'isoMuPF'
xtitle = 'Isolation'
xunits = 'GeV'
lumi = 4895.
lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)

extraName = ''
steps, xmin, xmax = hr.ranger(leaf)

#Available cuts: Skim, NoMuMu, JetEta, MT, OneMuNuCand, JetPt20, JetPt30, JetPt40, 4jets30, IsDiBJet, IsDiNoBJet
nrcuts =1
cut1 = 'Skim'
cut2 = 'MT'
cut3 = 'C1'
cut4 = 'NoEle'
cut5 = ''
cut6 = ''
cut7 = ''
cut8 = ''
cut9 = ''

CutList = []
CutList.append(cut1)
CutList.append(cut2)
CutList.append(cut3)
CutList.append(cut4)
CutList.append(cut5)
CutList.append(cut6)
CutList.append(cut7)
CutList.append(cut8)

theCut = ''
TD = 'PU3D*wtEffIsotComb*'+str(lumi)
Iso='isoMuPF<0.12'
NonIso = 'isoMuPF>=0.2'


for i in range(nrcuts):
  theCut += '&&'+ct.cuts[CutList[i]] 

datafilename = '../data/MuonData_2011_WBB_COMMON_V12.root'
qfilename = '../data/QCDMu_V12.root'

datafile = TFile(datafilename)
qfile = TFile(qfilename)

eventTreeLocation = 'muNuJetJetEventTree/eventTree'

dataTree = datafile.Get(eventTreeLocation)
qTree = qfile.Get(eventTreeLocation)

gStyle.SetOptStat('')

mch = TH1F('mch','mch',steps,xmin,xmax)
datah = TH1F('datah','datah',steps,xmin,xmax)

c = TCanvas('c','Canvas Named c',canx,cany)
#c.SetLogy()

####
print("data") 
dataTree.Draw(leaf+'>>datah','1<2'+theCut,'')
datah.SetTitle('')
datah.SetLineWidth(3)
datah.SetLineColor(ROOT.EColor.kGreen)
bmindata = datah.GetXaxis().FindBin(xmin)
bmaxdata = datah.GetXaxis().FindBin(xmax)
dataSize = datah.Integral(bmindata,bmaxdata)
datah.Scale(1/dataSize)
datamax=datah.GetMaximum()
print(datamax)
###
print("mc") 
qTree.Draw(leaf+'>>mch','1<2'+theCut,'sames')
mch.SetTitle('')
mch.SetLineWidth(3)
mch.SetLineColor(ROOT.EColor.kAzure)
bminmc=mch.GetXaxis().FindBin(xmin)
bmaxmc=mch.GetXaxis().FindBin(xmax)
mcSize=mch.Integral(bminmc,bmaxmc)
mch.Scale(1/mcSize)
mcmax = mch.GetMaximum()
print(mcmax)
###
print('--------')
if (datamax>mcmax):
	datah.GetYaxis().SetRangeUser(0,1.2*datamax)
elif(mcmax>datamax):
	datah.GetYaxis().SetRangeUser(0,1.2*mcmax)

datah.Draw()
datah.GetXaxis().SetTitle(xtitle)
mch.Draw('sames')

leg=TLegend(0.4,0.4,0.9,0.85)
leg.AddEntry(mch,'MC')
leg.AddEntry(datah,'Data')
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.Draw('sames')

la = TLine(0.12,0,0.12,1)
la.SetLineColor(13)
la.SetLineWidth(2)
la.Draw()
lb = TLine(0.2,0,0.2,1)
lb.SetLineColor(13)
lb.SetLineWidth(2)
lb.Draw()

mtTitle = xtitle+' QCD Shapes'
tex.DrawLatex(0,1,mtTitle)


c.cd()

c.Update()
c.Print('../plots/QCDshape'+leaf+extraName+'.png')
c.Close()

