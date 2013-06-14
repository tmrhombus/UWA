#!/usr/bin/env python
'''
Makes a 2-D histogram of leaves x and y
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *

import cuts as ct
import histoRange as hr

# Available Leaves: mt, met, ptMu, massDiNoBJets, massDiJets, ptDiJets, isoMuPFIsoRho, etaMu'
leafy = 'mt'
leafx = 'isoMuPF'
#xtitle = 'Transverse Mass'
#xunits = 'GeV'
lumi = 4895.
lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)

extraName = ''
#steps, xmin, xmax, xtitle, xunits = hr.ranger(leaf)

#Available cuts: Skim, NoMuMu, JetEta, MT, OneMuNuCand, JetPt20, JetPt30, JetPt40, 4jets30, IsDiBJet, IsDiNoBJet
nrcuts =1
cut1 = 'Skim'
cut2 = '4jets'
cut3 = 'TwoBtag'
cut4 = 'MT'
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
TD = 'wtPU3D*wtEffIsotComb*'+str(lumi)
### C1 or C3
#TD = 'CSVM2Jets*wtPU3D*wtEffIsotComb*'+str(lumi)
### C2
#TD = 'CSVM1Jet*wtPU3D*wtEffIsotComb*'+str(lumi)
Iso='isoMuPF<0.12'
NonIso = 'isoMuPF>=0.2'

for i in range(nrcuts):
  theCut += '&&'+ct.cuts[CutList[i]] 

#CutsMC = '('+TD+'*('+Iso+theCut+'))'
#CutsData = '('+Iso+theCut+')'
#CutsQCD = '('+NonIso+theCut+')'
#CutsWtau =  '('+TD+'*('+Wtau+'&&'+Iso+theCut+'))'
#CutsWbx = '('+TD+'*('+Wbx+'&&'+Iso+theCut+'))'
#CutsWbb = '('+TD+'*('+Wbb+'&&'+Iso+theCut+'))'
#CutsWc =  '('+TD+'*('+Wc+'&&'+Iso+theCut+'))'
#CutsWl = '('+TD+'*('+Wl+'&&'+Iso+theCut+'))'

blank = '1<2'
CutsMC = '('+TD+'*('+blank+theCut+'))'
CutsData = '('+blank+theCut+')'
CutsQCD = '('+blank+theCut+')'
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
canx = 650
cany = 900

datafilename = '../data/MuonData_2011_WBB_COMMON_V12.root'
ttfilename = '../data/TTBAR_V12.root'
qfilename = '../data/QCDMu_V12.root'

datafile = TFile(datafilename)
ttfile = TFile(ttfilename)
qfile = TFile(qfilename)

#outFile=gROOT.FindObject('../data/'+leaf+extraName+'.root')
#if outFile : outFile.Close()
#outFile = TFile('../data/'+leaf+extraName+'.root','RECREATE','Demo ROOT file')

eventTreeLocation = 'muNuJetJetEventTree/eventTree'

dataTree = datafile.Get(eventTreeLocation)
ttTree = ttfile.Get(eventTreeLocation)
qTree = qfile.Get(eventTreeLocation)

gStyle.SetOptStat('')

stepsy = 50
ymin = 0
ymax = 200
stepsx = 50
xmin = 0.4
xmax = 0.5

qh = TH2F('qh','qh',stepsx,xmin,xmax,stepsy,ymin,ymax)
tth = TH2F('tth','tth',stepsx,xmin,xmax,stepsy,ymin,ymax)
dh = TH2F('dh','dh',stepsx,xmin,xmax,stepsy,ymin,ymax)

c1 = TCanvas('c1','Canvas Named c1',canx,cany)
c2 = TCanvas('c2','Canvas Named c2',canx,cany)
c3 = TCanvas('c3','Canvas Named c3',canx,cany)

c1.cd()

###
print("data") 
dataTree.Draw(leafy+':'+leafx+'>>dh',CutsData,'colz')
c1.Print('../plots/2dDatac.png')
dh.SetTitle('')
####
c2.cd()
print("tt")
ttTree.Draw(leafy+':'+leafx+'>>tth',CutsMC,'colz')
tth.SetTitle('')
c2.Print('../plots/2dttc.png')
###
c3.cd()
print('qcd')
qTree.Draw(leafy+':'+leafx+'>>qh',CutsMC,'colz')
qh.SetTitle('')
c3.Print('../plots/2dQCDc.png')
