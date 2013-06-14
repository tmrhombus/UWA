#!/usr/bin/env python
'''
Plots a comparison between PU reweighting and not applying it
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad, TLine
from ROOT import TLatex
from ROOT import gROOT,gStyle

import cuts as ct
import histoRange as hr

# Available Leaves: mt, met, ptMu, massDiJets, ptDiJets, isoMuPFIsoRho, etaMu, massDiNoBJets, massDiBJets
leaf = 'jet1BTag_SSVMass'
lumi = 4895
steps, xmin, xmax,xtitle,xunits = hr.ranger(leaf)

lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)
extraName='BTagC2'

#canvas attributes
canx = 600
cany = 700

gROOT.SetStyle('Plain')
gStyle.SetOptStat('mr')
tex=ROOT.TLatex()
tex.SetTextAlign(13)
tex.SetNDC(True)

tfilename = '../data/Singletop_V12no.root'
ttfilename = '../data/TTBAR_V12no.root'
dfilename = '../data/Dibosons_V12no.root'
wfilename = '../data/W_V12no.root'
zfilename = '../data/DYall_V12no.root'

tfilename3d = '../data/Singletop_V123d.root'
ttfilename3d = '../data/TTBAR_V123d.root'
dfilename3d = '../data/Dibosons_V123d.root'
wfilename3d = '../data/W_V123d.root'
zfilename3d = '../data/DYall_V123d.root'

tfilenamev = '../data/Singletop_V12.root'
ttfilenamev = '../data/TTBAR_V12.root'
dfilenamev = '../data/Dibosons_V12.root'
wfilenamev = '../data/W_V12.root'
zfilenamev = '../data/DYall_V12.root'

tfile = TFile(tfilename)
ttfile = TFile(ttfilename)
dfile = TFile(dfilename)
wfile = TFile(wfilename)
zfile = TFile(zfilename)

tfile3d = TFile(tfilename3d)
ttfile3d = TFile(ttfilename3d)
dfile3d = TFile(dfilename3d)
wfile3d = TFile(wfilename3d)
zfile3d = TFile(zfilename3d)

tfilev = TFile(tfilenamev)
ttfilev = TFile(ttfilenamev)
dfilev = TFile(dfilenamev)
wfilev = TFile(wfilenamev)
zfilev = TFile(zfilenamev)

eventTreeLocation = 'muNuJetJetEventTree/eventTree'

tTree = tfile.Get(eventTreeLocation)
dTree = dfile.Get(eventTreeLocation)
ttTree = ttfile.Get(eventTreeLocation)
wTree = wfile.Get(eventTreeLocation)
zTree = zfile.Get(eventTreeLocation)

tTree3d = tfile3d.Get(eventTreeLocation)
dTree3d = dfile3d.Get(eventTreeLocation)
ttTree3d = ttfile3d.Get(eventTreeLocation)
wTree3d = wfile3d.Get(eventTreeLocation)
zTree3d = zfile3d.Get(eventTreeLocation)

tTreev = tfilev.Get(eventTreeLocation)
dTreev = dfilev.Get(eventTreeLocation)
ttTreev = ttfilev.Get(eventTreeLocation)
wTreev = wfilev.Get(eventTreeLocation)
zTreev = zfilev.Get(eventTreeLocation)

th = TH1F('th','th',steps,xmin,xmax)
tth = TH1F('tth','tth',steps,xmin,xmax)
dh = TH1F('dh','dh',steps,xmin,xmax)
wh = TH1F('wh','wh',steps,xmin,xmax)
zh = TH1F('zh','zh',steps,xmin,xmax)
allh = TH1F('allh','allh',steps,xmin,xmax)

th3d = TH1F('th3d','th3d',steps,xmin,xmax)
tth3d = TH1F('tth3d','tth3d',steps,xmin,xmax)
dh3d = TH1F('dh3d','dh3d',steps,xmin,xmax)
wh3d = TH1F('wh3d','wh3d',steps,xmin,xmax)
zh3d = TH1F('zh3d','zh3d',steps,xmin,xmax)
allh3d = TH1F('allh3d','allh3d',steps,xmin,xmax)

thv = TH1F('thv','thv',steps,xmin,xmax)
tthv = TH1F('tthv','tthv',steps,xmin,xmax)
dhv = TH1F('dhv','dhv',steps,xmin,xmax)
whv = TH1F('whv','whv',steps,xmin,xmax)
zhv = TH1F('zhv','zhv',steps,xmin,xmax)
allhv = TH1F('allhv','allhv',steps,xmin,xmax)

a = ROOT.EColor.kCyan-7
t = ROOT.EColor.kRed-4
tt = ROOT.EColor.kPink-4 
d = ROOT.EColor.kGreen
w = ROOT.EColor.kAzure+8
z = ROOT.EColor.kGreen-3

c1 = TCanvas('c1','Canvas Named c1',canx,cany)
c2 = TCanvas('c2','Canvas Named c2',canx,cany)
c3 = TCanvas('c3','Canvas Named c3',canx,cany)
c4 = TCanvas('c4','Canvas Named c4',canx,cany)
c5 = TCanvas('c5','Canvas Named c5',canx,cany)
c6 = TCanvas('c6','Canvas Named c6',canx,cany)

#TD = 'wtPU3D*'+str(lumi)
#TD = 'CSVM2Jets*wtPU3D*wtEffIsotComb*'+str(lumi)
TD = 'CSVM1Jet*wtPU3D*wtEffIsotComb*'+str(lumi)
D = str(lumi)
Iso = 'isoMuPF<0.12'
JetsB = 'genWBs>0'
JetsNoB = 'genWBs==0'

theCut = '&&'+ct.cuts['Skim']+'&&'+ct.cuts['MT']+'&&'+ct.cuts['C2']
CutsMC = '('+TD+'*('+Iso+theCut+'))'
CutsM = '('+D+'*('+Iso+theCut+'))'

lab = 'no PU info'
lab3d = '3D Weight'
labv = 'Nr. Vertices'

#
c1.cd()
tTree.Draw(leaf+'>>th',CutsMC,'')
tTree3d.Draw(leaf+'>>th3d',CutsMC,'')
tTreev.Draw(leaf+'>>thv',CutsMC,'')
th.SetLineWidth(3)
th.SetLineColor(d)
th3d.SetLineWidth(3)
th3d.SetLineColor(w)
thv.SetLineWidth(3)
thv.SetLineColor(t)
th3d.SetTitle('')
th3d.Draw()
thv.Draw('sames')
th.Draw('sames')

legt=TLegend(0.5,0.6,0.9,0.8)
legt.AddEntry(th,lab)
legt.AddEntry(th3d,lab3d)
legt.AddEntry(thv,labv)
legt.SetFillColor(0)
legt.SetBorderSize(0)
legt.Draw('sames')

c1.Update()
c1.Print('../plots/PU/top_'+leaf+extraName+'.png')
##
c2.cd()
ttTree.Draw(leaf+'>>tth',CutsMC,'')
ttTree3d.Draw(leaf+'>>tth3d',CutsMC,'')
ttTreev.Draw(leaf+'>>tthv',CutsMC,'')
tth.SetLineWidth(3)
tth.SetLineColor(d)
tth3d.SetLineWidth(3)
tth3d.SetLineColor(w)
tthv.SetLineWidth(3)
tthv.SetLineColor(t)
tth3d.SetTitle('')
tth3d.Draw()
tthv.Draw('sames')
tth.Draw('sames')

legtt=TLegend(0.5,0.6,0.9,0.8)
legtt.AddEntry(tth,lab)
legtt.AddEntry(tth3d,lab3d)
legtt.AddEntry(tthv,labv)
legtt.SetFillColor(0)
legtt.SetBorderSize(0)
legtt.Draw('sames')

c2.Update()
c2.Print('../plots/PU/tt_'+leaf+extraName+'.png')
##
c3.cd()
dTree.Draw(leaf+'>>th',CutsMC,'')
dTree3d.Draw(leaf+'>>th3d',CutsMC,'')
dTreev.Draw(leaf+'>>thv',CutsMC,'')
dh.SetLineWidth(3)
dh.SetLineColor(d)
dh3d.SetLineWidth(3)
dh3d.SetLineColor(w)
dhv.SetLineWidth(3)
dhv.SetLineColor(t)
dh3d.SetTitle('')
dh3d.Draw()
dhv.Draw('sames')
dh.Draw('sames')

legd=TLegend(0.5,0.6,0.9,0.8)
legd.AddEntry(dh,lab)
legd.AddEntry(dh3d,lab3d)
legd.AddEntry(dhv,labv)
legd.SetFillColor(0)
legd.SetBorderSize(0)
legd.Draw('sames')

c3.Update()
c3.Print('../plots/PU/dibos_'+leaf+extraName+'.png')
##
c4.cd()
wTree.Draw(leaf+'>>wh',CutsMC,'')
wTree3d.Draw(leaf+'>>wh3d',CutsMC,'')
wTreev.Draw(leaf+'>>whv',CutsMC,'')
wh.SetLineWidth(3)
wh.SetLineColor(d)
wh3d.SetLineWidth(3)
wh3d.SetLineColor(w)
whv.SetLineWidth(3)
whv.SetLineColor(t)
wh3d.Draw()
whv.Draw('sames')
wh.Draw('sames')

legw=TLegend(0.5,0.6,0.9,0.8)
legw.AddEntry(wh,lab)
legw.AddEntry(wh3d,lab3d)
legw.AddEntry(whv,labv)
legw.SetFillColor(0)
legw.SetBorderSize(0)
legw.Draw('sames')

c4.Update()
c4.Print('../plots/PU/w_'+leaf+extraName+'.png')
##
c5.cd()
zTree.Draw(leaf+'>>zh',CutsMC,'')
zTree3d.Draw(leaf+'>>zh3d',CutsMC,'')
zTreev.Draw(leaf+'>>zhv',CutsMC,'')
zh.SetLineWidth(3)
zh.SetLineColor(d)
zh3d.SetLineWidth(3)
zh3d.SetLineColor(w)
zhv.SetLineWidth(3)
zhv.SetLineColor(t)
zh3d.Draw()
zhv.Draw('sames')
zh.Draw('sames')

legz=TLegend(0.5,0.6,0.9,0.8)
legz.AddEntry(zh,lab)
legz.AddEntry(zh3d,lab3d)
legz.AddEntry(zhv,labv)
legz.SetFillColor(0)
legz.SetBorderSize(0)
legz.Draw('sames')

c5.Update()
c5.Print('../plots/PU/z_'+leaf+extraName+'.png')
##
c6.cd()
allh.Add(th)
allh.Add(tth)
allh.Add(dh)
allh.Add(wh)
allh.Add(zh)


allh3d.Add(th3d)
allh3d.Add(tth3d)
allh3d.Add(dh3d)
allh3d.Add(wh3d)
allh3d.Add(zh3d)
allh3d.SetTitle('')

allhv.Add(thv)
allhv.Add(tthv)
allhv.Add(dhv)
allhv.Add(whv)
allhv.Add(zhv)

allh.SetLineWidth(3)
allh.SetLineColor(d)
allh3d.SetLineWidth(3)
allh3d.SetLineColor(w)
allhv.SetLineWidth(3)
allhv.SetLineColor(t)
#
allh3d.Draw()
tdSize=allh3d.Integral()
c6.Update()
s1=allh3d.GetListOfFunctions().FindObject("stats")
s1.SetX1NDC(0.6)
s1.SetY1NDC(0.8)
s1.SetX2NDC(0.9)
s1.SetY2NDC(0.9)
#
allhv.Draw('sames')
vSize=allhv.Integral()
c6.Update()
s2=allhv.GetListOfFunctions().FindObject("stats")
s2.SetX1NDC(0.6)
s2.SetY1NDC(0.7)
s2.SetX2NDC(0.9)
s2.SetY2NDC(0.8)
#
allh.Draw('sames')
Size=allh.Integral()
c6.Update()
s3=allh.GetListOfFunctions().FindObject("stats")
s3.SetX1NDC(0.6)
s3.SetY1NDC(0.6)
s3.SetX2NDC(0.9)
s3.SetY2NDC(0.7)

leg=TLegend(0.6,0.3,0.9,0.6)
leg.AddEntry(allh3d,lab3d)
leg.AddEntry(allhv,labv)
leg.AddEntry(allh,lab)
leg.SetFillColor(0)
#leg.SetBorderSize(0)
leg.Draw('sames')

mtTitle = xtitle+' Correction Comparison'
allh3d.GetXaxis().SetTitle(xtitle+' ['+xunits+']')
allh3d.GetYaxis().SetTitle('Events')
tex.DrawLatex(0,1,mtTitle)

print('3D Size:     '+str(tdSize))
print('Vert Size:   '+str(vSize))
print('No PU Size:  '+str(Size))
c6.Update()
c6.Print('../plots/PU/ALL_'+leaf+extraName+'.png')
