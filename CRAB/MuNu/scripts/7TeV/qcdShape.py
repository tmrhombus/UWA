#!/usr/bin/env python
'''
Look at the (normalized) shapes of various QCD options
	Inverse Isolation from Data
	Isolation on QCD from MC
	Inverse Isolation on Data - MC
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
leaf = 'mt'
xtitle = 'Transverse Mass'
xunits = 'GeV'
lumi = 4895.
lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)

extraName = '3j1b'
path = '../QCDshapes/'
steps, xmin, xmax = hr.ranger(leaf)
steps = steps/5

jNr = 3
bNr = 1
#Available cuts: Skim, NoMuMu, JetEta, MT, OneMuNuCand, JetPt20, JetPt30, JetPt40, 4jets30, IsDiBJet, IsDiNoBJet

theCut = ''
if bNr==0:
 TD = 'wtPU3D*wtEffIsotComb*'+str(lumi)
 btag = 'Skim'
### C2
if bNr==1:
 TD = 'CSVM1Jet*wtPU3D*wtEffIsotComb*'+str(lumi)
 btag = 'SomeBtag'
 ### C1 or C3
if bNr==2:
 TD = 'CSVM2Jets*wtPU3D*wtEffIsotComb*'+str(lumi)
 btag = 'TwoBtag'

if jNr==2:
 jtag = 'Skim'
if jNr==3:
 jtag = '3jets'
if jNr==4:
 jtag = '4jets'

nrcuts =3
cut1 = 'Skim'
cut2 = btag
cut3 = jtag
cut4 = ''
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

Iso='isoMuPF<0.12'
NonIso2 = 'isoMuPF>=0.2'
NonIso3 = 'isoMuPF>=0.3'
NonIso4 = 'isoMuPF>=0.4'

for i in range(nrcuts):
  theCut += '&&'+ct.cuts[CutList[i]] 

CutsMCiso = '('+TD+'*('+Iso+theCut+'))'
CutsDATAiso = '('+Iso+theCut+')'

CutsMCniso2 = '('+TD+'*('+NonIso2+theCut+'))'
CutsMCniso3 = '('+TD+'*('+NonIso3+theCut+'))'
CutsMCniso4 = '('+TD+'*('+NonIso4+theCut+'))'
CutsDATAniso2 = '('+NonIso2+theCut+')'
CutsDATAniso3 = '('+NonIso3+theCut+')'
CutsDATAniso4 = '('+NonIso4+theCut+')'

datafilename = '../data/MuonData_2011_WBB_COMMON_V12.root'
qfilename = '../data/QCDMu_V13.root'
ttfilename = '../data/TTBAR_V13.root'
tfilename = '../data/Singletop_V13.root'
dfilename = '../data/Dibosons_V13.root'
wfilename = '../data/W_V13.root'
zfilename = '../data/DYall_V13.root'

datafile = TFile(datafilename)
qfile = TFile(qfilename)
ttfile = TFile(ttfilename)
tfile = TFile(tfilename)
dfile = TFile(dfilename)
wfile = TFile(wfilename)
zfile = TFile(zfilename)

eventTreeLocation = 'muNuJetJetEventTree/eventTree'

dataTree = datafile.Get(eventTreeLocation)
qTree = qfile.Get(eventTreeLocation)
ttTree = ttfile.Get(eventTreeLocation)
tTree = tfile.Get(eventTreeLocation)
dTree = dfile.Get(eventTreeLocation)
wTree = wfile.Get(eventTreeLocation)
zTree = zfile.Get(eventTreeLocation)

gStyle.SetOptStat('')

qmcIsoh = TH1F('qmcIsoh','qmcIsoh',steps,xmin,xmax)
dataIsoh = TH1F('dataIsoh','dataIsoh',steps,xmin,xmax)

qmcNIso2h = TH1F('qmcNIso2h','qmcNIsoh2',steps,xmin,xmax)
qmcNIso3h = TH1F('qmcNIso3h','qmcNIsoh3',steps,xmin,xmax)
qmcNIso4h = TH1F('qmcNIso4h','qmcNIsoh4',steps,xmin,xmax)

dataNIso2h = TH1F('dataNIso2h','dataNIso2h',steps,xmin,xmax)
dataNIso3h = TH1F('dataNIso3h','dataNIso3h',steps,xmin,xmax)
dataNIso4h = TH1F('dataNIso4h','dataNIso4h',steps,xmin,xmax)

zNIso2h = TH1F('zNIso2h','zNIso2h',steps,xmin,xmax)
zNIso3h = TH1F('zNIso3h','zNIso3h',steps,xmin,xmax)
zNIso4h = TH1F('zNIso4h','zNIso4h',steps,xmin,xmax)

wNIso2h = TH1F('wNIso2h','wNIso2h',steps,xmin,xmax)
wNIso3h = TH1F('wNIso3h','wNIso3h',steps,xmin,xmax)
wNIso4h = TH1F('wNIso4h','wNIso4h',steps,xmin,xmax)

dNIso2h = TH1F('dNIso2h','dNIso2h',steps,xmin,xmax)
dNIso3h = TH1F('dNIso3h','dNIso3h',steps,xmin,xmax)
dNIso4h = TH1F('dNIso4h','dNIso4h',steps,xmin,xmax)

tNIso2h = TH1F('tNIso2h','tNIso2h',steps,xmin,xmax)
tNIso3h = TH1F('tNIso3h','tNIso3h',steps,xmin,xmax)
tNIso4h = TH1F('tNIso4h','tNIso4h',steps,xmin,xmax)

ttNIso2h = TH1F('ttNIso2h','ttNIso2h',steps,xmin,xmax)
ttNIso3h = TH1F('ttNIso3h','ttNIso3h',steps,xmin,xmax)
ttNIso4h = TH1F('ttNIso4h','ttNIso4h',steps,xmin,xmax)

dataNIsoSub2h = TH1F('dataNIsoSub2h','dataNIsoSub2h',steps,xmin,xmax)
dataNIsoSub3h = TH1F('dataNIsoSub3h','dataNIsoSub3h',steps,xmin,xmax)
dataNIsoSub4h = TH1F('dataNIsoSub4h','dataNIsoSub4h',steps,xmin,xmax)

c = TCanvas('c','Canvas Named c',canx,cany)
#c.SetLogy()

## Isolated QCD(mc) and Data
print('qmcIso')
qTree.Draw(leaf+'>>qmcIsoh',CutsMCiso,'')
bminqI = qmcIsoh.GetXaxis().FindBin(xmin)
bmaxqI = qmcIsoh.GetXaxis().FindBin(xmax)
qIhSize = qmcIsoh.Integral(bminqI,bmaxqI)
qmcIsoh.Scale(1/qIhSize)

print('dataIso')
dataTree.Draw(leaf+'>>dataIsoh',CutsDATAiso,'')
bmindI = dataIsoh.GetXaxis().FindBin(xmin)
bmaxdI = dataIsoh.GetXaxis().FindBin(xmax)
dIhSize = dataIsoh.Integral(bmindI,bmaxdI)
dataIsoh.Scale(1/dIhSize)

## QCD Non Isolated

print('qmcNIso2')
qTree.Draw(leaf+'>>qmcNIso2h',CutsMCniso2,'')
bminqn2 = qmcNIso2h.GetXaxis().FindBin(xmin)
bmaxqn2 = qmcNIso2h.GetXaxis().FindBin(xmax)
qn2hSize = qmcNIso2h.Integral(bminqn2,bmaxqn2)
qmcNIso2h.Scale(1/qn2hSize)

print('qmcNIso3')
qTree.Draw(leaf+'>>qmcNIso3h',CutsMCniso3,'')
bminqn3 = qmcNIso3h.GetXaxis().FindBin(xmin)
bmaxqn3 = qmcNIso3h.GetXaxis().FindBin(xmax)
qn3hSize = qmcNIso3h.Integral(bminqn3,bmaxqn3)
qmcNIso3h.Scale(1/qn3hSize)

print('qmcNIso4')
qTree.Draw(leaf+'>>qmcNIso4h',CutsMCniso4,'')
bminqn4 = qmcNIso4h.GetXaxis().FindBin(xmin)
bmaxqn4 = qmcNIso4h.GetXaxis().FindBin(xmax)
qn4hSize = qmcNIso4h.Integral(bminqn4,bmaxqn4)
qmcNIso4h.Scale(1/qn4hSize)

## Data Non Isolated

print('dataNIso2')
dataTree.Draw(leaf+'>>dataNIso2h',CutsDATAniso2,'')
bmindn2 = dataNIso2h.GetXaxis().FindBin(xmin)
bmaxdn2 = dataNIso2h.GetXaxis().FindBin(xmax)
dn2hSize = dataNIso2h.Integral(bmindn2,bmaxdn2)
dataNIsoSub2h = dataNIso2h.Clone()
dataNIso2h.Scale(1/dn2hSize)

print('dataNIso3')
dataTree.Draw(leaf+'>>dataNIso3h',CutsDATAniso3,'')
bmindn3 = dataNIso3h.GetXaxis().FindBin(xmin)
bmaxdn3 = dataNIso3h.GetXaxis().FindBin(xmax)
dn3hSize = dataNIso3h.Integral(bmindn3,bmaxdn3)
dataNIsoSub3h = dataNIso3h.Clone()
dataNIso3h.Scale(1/dn3hSize)

print('dataNIso4')
dataTree.Draw(leaf+'>>dataNIso4h',CutsDATAniso4,'')
bmindn4 = dataNIso4h.GetXaxis().FindBin(xmin)
bmaxdn4 = dataNIso4h.GetXaxis().FindBin(xmax)
dn4hSize = dataNIso4h.Integral(bmindn4,bmaxdn4)
dataNIsoSub4h = dataNIso4h.Clone()
dataNIso4h.Scale(1/dn4hSize)

## Z Non Isolated

print('zNIso2')
zTree.Draw(leaf+'>>zNIso2h',CutsMCniso2,'')
#bminz2 = zNIso2h.GetXaxis().FindBin(xmin)
#bmaxz2 = zNIso2h.GetXaxis().FindBin(xmax)
#z2hSize = zNIso2h.Integral(bminz2,bmaxz2)
#zNIso2h.Scale(1/z2hSize)

print('zNIso3')
zTree.Draw(leaf+'>>zNIso3h',CutsMCniso3,'')
#bminz3 = zNIso3h.GetXaxis().FindBin(xmin)
#bmaxz3 = zNIso3h.GetXaxis().FindBin(xmax)
#z3hSize = zNIso3h.Integral(bminz3,bmaxz3)
#zNIso3h.Scale(1/z3hSize)

print('zNIso4')
zTree.Draw(leaf+'>>zNIso4h',CutsMCniso4,'')
#bminz4 = zNIso4h.GetXaxis().FindBin(xmin)
#bmaxz4 = zNIso4h.GetXaxis().FindBin(xmax)
#z4hSize = zNIso4h.Integral(bminz4,bmaxz4)
#zNIso4h.Scale(1/z4hSize)

## W Non Isolated

print('wNIso2')
wTree.Draw(leaf+'>>wNIso2h',CutsMCniso2,'')
#bminw2 = wNIso2h.GetXaxis().FindBin(xmin)
#bmaxw2 = wNIso2h.GetXaxis().FindBin(xmax)
#w2hSize = wNIso2h.Integral(bminw2,bmaxw2)
#wNIso2h.Scale(1/w2hSize)

print('wNIso3')
wTree.Draw(leaf+'>>wNIso3h',CutsMCniso3,'')
#bminw3 = wNIso3h.GetXaxis().FindBin(xmin)
#bmaxw3 = wNIso3h.GetXaxis().FindBin(xmax)
#w3hSize = wNIso3h.Integral(bminw3,bmaxw3)
#wNIso3h.Scale(1/w3hSize)

print('wNIso4')
wTree.Draw(leaf+'>>wNIso4h',CutsMCniso4,'')
#bminw4 = wNIso4h.GetXaxis().FindBin(xmin)
#bmaxw4 = wNIso4h.GetXaxis().FindBin(xmax)
#w4hSize = wNIso4h.Integral(bminw4,bmaxw4)
#wNIso4h.Scale(1/w4hSize)

## Diboson Non Isolated

print('dNIso2')
dTree.Draw(leaf+'>>dNIso2h',CutsMCniso2,'')
#bmind2 = dNIso2h.GetXaxis().FindBin(xmin)
#bmaxd2 = dNIso2h.GetXaxis().FindBin(xmax)
#d2hSize = dNIso2h.Integral(bmind2,bmaxd2)
#dNIso2h.Scale(1/d2hSize)

print('dNIso3')
dTree.Draw(leaf+'>>dNIso3h',CutsMCniso3,'')
#bmind3 = dNIso3h.GetXaxis().FindBin(xmin)
#bmaxd3 = dNIso3h.GetXaxis().FindBin(xmax)
#d3hSize = dNIso3h.Integral(bmind3,bmaxd3)
#dNIso3h.Scale(1/d3hSize)

print('dNIso4')
dTree.Draw(leaf+'>>dNIso4h',CutsMCniso4,'')
#bmind4 = dNIso4h.GetXaxis().FindBin(xmin)
#bmaxd4 = dNIso4h.GetXaxis().FindBin(xmax)
#d4hSize = dNIso4h.Integral(bmind4,bmaxd4)
#dNIso4h.Scale(1/d4hSize)

## Single Top Non Isolated

print('tNIso2')
tTree.Draw(leaf+'>>tNIso2h',CutsMCniso2,'')
#bmint2 = tNIso2h.GetXaxis().FindBin(xmin)
#bmaxt2 = tNIso2h.GetXaxis().FindBin(xmax)
#t2hSize = tNIso2h.Integral(bmint2,bmaxt2)
#tNIso2h.Scale(1/t2hSize)

print('tNIso3')
tTree.Draw(leaf+'>>tNIso3h',CutsMCniso3,'')
#bmint3 = tNIso3h.GetXaxis().FindBin(xmin)
#bmaxt3 = tNIso3h.GetXaxis().FindBin(xmax)
#t3hSize = tNIso3h.Integral(bmint3,bmaxt3)
#tNIso3h.Scale(1/t3hSize)

print('tNIso4')
tTree.Draw(leaf+'>>tNIso4h',CutsMCniso4,'')
#bmint4 = tNIso4h.GetXaxis().FindBin(xmin)
#bmaxt4 = tNIso4h.GetXaxis().FindBin(xmax)
#t4hSize = tNIso4h.Integral(bmint4,bmaxt4)
#tNIso4h.Scale(1/t4hSize)

## TTbar Non Isolated

print('ttNIso2')
ttTree.Draw(leaf+'>>ttNIso2h',CutsMCniso2,'')
#bmintt2 = ttNIso2h.GetXaxis().FindBin(xmin)
#bmaxtt2 = ttNIso2h.GetXaxis().FindBin(xmax)
#tt2hSize = ttNIso2h.Integral(bmintt2,bmaxtt2)
#ttNIso2h.Scale(1/tt2hSize)

print('ttNIso3')
ttTree.Draw(leaf+'>>ttNIso3h',CutsMCniso3,'')
#bmintt3 = ttNIso3h.GetXaxis().FindBin(xmin)
#bmaxtt3 = ttNIso3h.GetXaxis().FindBin(xmax)
#tt3hSize = ttNIso3h.Integral(bmintt3,bmaxtt3)
#ttNIso3h.Scale(1/tt3hSize)

print('tNIso4')
ttTree.Draw(leaf+'>>ttNIso4h',CutsMCniso4,'')
#bmintt4 = ttNIso4h.GetXaxis().FindBin(xmin)
#bmaxtt4 = ttNIso4h.GetXaxis().FindBin(xmax)
#tt4hSize = ttNIso4h.Integral(bmintt4,bmaxtt4)
#ttNIso4h.Scale(1/tt4hSize)

# Subtract the (Anti Isolated) MC from Data Histogram
dataNIsoSub2h.Add(zNIso2h,-1)
dataNIsoSub2h.Add(wNIso2h,-1)
dataNIsoSub2h.Add(dNIso2h,-1)
dataNIsoSub2h.Add(tNIso2h,-1)
dataNIsoSub2h.Add(ttNIso2h,-1)
bmindns2h = dataNIsoSub2h.GetXaxis().FindBin(xmin)
bmaxdns2h = dataNIsoSub2h.GetXaxis().FindBin(xmax)
dns2hSize = dataNIsoSub2h.Integral(bmindns2h,bmaxdns2h)
dataNIsoSub2h.Scale(1/dns2hSize)

dataNIsoSub3h.Add(zNIso3h,-1)
dataNIsoSub3h.Add(wNIso3h,-1)
dataNIsoSub3h.Add(dNIso3h,-1)
dataNIsoSub3h.Add(tNIso3h,-1)
dataNIsoSub3h.Add(ttNIso3h,-1)
bmindns3h = dataNIsoSub3h.GetXaxis().FindBin(xmin)
bmaxdns3h = dataNIsoSub3h.GetXaxis().FindBin(xmax)
dns3hSize = dataNIsoSub3h.Integral(bmindns3h,bmaxdns3h)
dataNIsoSub3h.Scale(1/dns3hSize)

dataNIsoSub4h.Add(zNIso4h,-1)
dataNIsoSub4h.Add(wNIso4h,-1)
dataNIsoSub4h.Add(dNIso4h,-1)
dataNIsoSub4h.Add(tNIso4h,-1)
dataNIsoSub4h.Add(ttNIso4h,-1)
bmindns4h = dataNIsoSub4h.GetXaxis().FindBin(xmin)
bmaxdns4h = dataNIsoSub4h.GetXaxis().FindBin(xmax)
dns4hSize = dataNIsoSub4h.Integral(bmindns4h,bmaxdns4h)
dataNIsoSub4h.Scale(1/dns4hSize)

qmcIsoh.SetLineWidth(3)
dataIsoh.SetLineWidth(3)
qmcNIso2h.SetLineWidth(3)
qmcNIso3h.SetLineWidth(3)
qmcNIso4h.SetLineWidth(3)
dataNIso2h.SetLineWidth(3)
dataNIso3h.SetLineWidth(3)
dataNIso4h.SetLineWidth(3)
dataNIsoSub2h.SetLineWidth(3)
dataNIsoSub3h.SetLineWidth(3)
dataNIsoSub4h.SetLineWidth(3)

qmcIsoh.SetLineColor(ROOT.EColor.kBlue)
dataIsoh.SetLineColor(ROOT.EColor.kCyan)
qmcNIso2h.SetLineColor(ROOT.EColor.kYellow+3)
qmcNIso3h.SetLineColor(ROOT.EColor.kYellow-3)
qmcNIso4h.SetLineColor(ROOT.EColor.kYellow-9)
dataNIso2h.SetLineColor(ROOT.EColor.kGreen+3)
dataNIso3h.SetLineColor(ROOT.EColor.kGreen-3)
dataNIso4h.SetLineColor(ROOT.EColor.kGreen-9)
dataNIsoSub2h.SetLineColor(ROOT.EColor.kMagenta+3)
dataNIsoSub3h.SetLineColor(ROOT.EColor.kMagenta-3)
dataNIsoSub4h.SetLineColor(ROOT.EColor.kMagenta-9)

theMax = max(
 qmcIsoh.GetMaximum(),
 dataIsoh.GetMaximum(),
 qmcNIso2h.GetMaximum(),
 qmcNIso3h.GetMaximum(),
 qmcNIso4h.GetMaximum(),
 dataNIso2h.GetMaximum(),
 dataNIso3h.GetMaximum(),
 dataNIso4h.GetMaximum(),
 dataNIsoSub2h.GetMaximum(),
 dataNIsoSub3h.GetMaximum(),
 dataNIsoSub4h.GetMaximum(),
)

qmcIsoh.SetMaximum(1.1*theMax)
qmcIsoh.SetTitle('')
qmcIsoh.GetXaxis().SetTitle(xtitle+' ['+xunits+']')

qmcIsoh.Draw()
dataIsoh.Draw('sames')
qmcNIso2h.Draw('sames')
qmcNIso3h.Draw('sames')
qmcNIso4h.Draw('sames')
dataNIso2h.Draw('sames')
dataNIso3h.Draw('sames')
dataNIso4h.Draw('sames')
dataNIsoSub2h.Draw('sames')
dataNIsoSub3h.Draw('sames')
dataNIsoSub4h.Draw('sames')

leg=TLegend(0.6,0.4,0.9,0.89)
leg.AddEntry(qmcIsoh,'QCD Iso < 0.12')
leg.AddEntry(dataIsoh,'Data Iso < 0.12')
leg.AddEntry(qmcNIso2h,'QCD Iso > 0.2')
leg.AddEntry(qmcNIso3h,'QCD Iso > 0.3')
leg.AddEntry(qmcNIso4h,'QCD Iso > 0.4')
leg.AddEntry(dataNIso2h,'Data Iso > 0.2')
leg.AddEntry(dataNIso3h,'Data Iso > 0.3')
leg.AddEntry(dataNIso4h,'Data Iso > 0.4')
leg.AddEntry(dataNIsoSub2h,'Data - MC Iso > 0.2')
leg.AddEntry(dataNIsoSub3h,'Data - MC Iso > 0.3')
leg.AddEntry(dataNIsoSub4h,'Data - MC Iso > 0.4')
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.Draw('sames')

mtTitle = xtitle+' QCD Shapes'
tex.DrawLatex(0,1,mtTitle)


c.cd()
#
c.Update()
c.Print(path+leaf+extraName+'.png')
print('Check it out: '+path+leaf+extraName+'.png')
c.Close()

