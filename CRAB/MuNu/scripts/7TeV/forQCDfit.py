#!/usr/bin/env python
'''
Makes a .root file with histograms ready for use by fitWjets.c
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad, TLine
from ROOT import TLatex
from ROOT import gROOT,gStyle

import cuts as ct
import histoRange as hr

# Available Leaves: mt, met, ptMu, massDiJets, ptDiJets, isoMuPFIsoRho, etaMu, massDiNoBJets, massDiBJets
leaf = 'mt'
lumi = 4895

lumi,steps,xmin,xmax,xtitle,xunits = hr.ranger(leaf)
print(steps)
#xmin = 0.
#xmax = 200.
#steps = int(xmax-xmin)
#steps = 20

isNr = 2
jNr = 2
bNr = 0

qcdFromData = False
qcdFromMC = False
qcdFromDsubMC = True

Iso='isoMuPF<0.12'
NonIso = 'isoMuPF>=0.'+str(isNr)

if bNr==0:### Skim or whatever
 TD = 'wtPU3D*wtEffIsotComb*'+str(lumi)
 bCut = 'Skim'
elif bNr==1:### C2
 TD = 'CSVM1Jet*wtPU3D*wtEffIsotComb*'+str(lumi)
 bCut = 'SomeBtag'
elif bNr==2:### C1 or C3
 TD = 'CSVM2Jets*wtPU3D*wtEffIsotComb*'+str(lumi)
 bCut = 'TwoBtag'
else:
 print('You want how many bs?')

if jNr==2:
 jCut = 'Skim'
elif jNr==3:
 jCut = '3jets'
elif jNr==4:
 jCut = '4jets'
else:
 print('You want how many jets?')

theCut = '&&'+ct.cuts['Skim']+'&&'+ct.cuts[bCut]+'&&'+ct.cuts[jCut]

datafilename = '../data/MuonData_2011_WBB_COMMON_V12.root'
qfilename = '../data/QCDMu_V13.root'
tfilename = '../data/Singletop_V13.root'
ttfilename = '../data/TTBAR_V13.root'
dfilename = '../data/Dibosons_V13.root'
wfilename = '../data/W_V13.root'
zfilename = '../data/DYall_V13.root'

datafile = TFile(datafilename)
qfile = TFile(qfilename)
tfile = TFile(tfilename)
ttfile = TFile(ttfilename)
dfile = TFile(dfilename)
wfile = TFile(wfilename)
zfile = TFile(zfilename)

path = '../scratch/'
outfilename = 'forQCD'+str(jNr)+'j'+str(bNr)+'bIso'+str(isNr)+'_'+str(int(xmin))+'_'+str(int(xmax))

outFile=gROOT.FindObject(path+outfilename+'.root')
if outFile : outFile.Close()
outFile = TFile(path+outfilename+'.root','RECREATE','Demo ROOT file')

eventTreeLocation = 'muNuJetJetEventTree/eventTree'

dataTree = datafile.Get(eventTreeLocation)
qTree = qfile.Get(eventTreeLocation)
tTree = tfile.Get(eventTreeLocation)
dTree = dfile.Get(eventTreeLocation)
ttTree = ttfile.Get(eventTreeLocation)
wTree = wfile.Get(eventTreeLocation)
zTree = zfile.Get(eventTreeLocation)

datah = TH1F('datah','datah',steps,xmin,xmax)
datah.Sumw2()
qh = TH1F('qh','qh',steps,xmin,xmax)
th = TH1F('th','th',steps,xmin,xmax)
tth = TH1F('tth','tth',steps,xmin,xmax)
dh = TH1F('dh','dh',steps,xmin,xmax)
wh = TH1F('wh','wh',steps,xmin,xmax)
zh = TH1F('zh','zh',steps,xmin,xmax)
hh = TH1F('hh','hh',steps,xmin,xmax)

tnh = TH1F('tnh','tnh',steps,xmin,xmax)
ttnh = TH1F('ttnh','ttnh',steps,xmin,xmax)
dnh = TH1F('dnh','dnh',steps,xmin,xmax)
wnh = TH1F('wnh','wnh',steps,xmin,xmax)
znh = TH1F('znh','znh',steps,xmin,xmax)

datahSize=-1
qhSize=-1
thSize=-1
tthSize=-1
dhSize=-1
whSize=-1
zhSize=-1
tnhSize=-1
ttnhSize=-1
dnhSize=-1
wnhSize=-1
znhSize=-1

CutsMC = '('+TD+'*('+Iso+theCut+'))'
CutsMCn = '('+TD+'*('+NonIso+theCut+'))'
CutsData = '('+Iso+theCut+')'
CutsDatan = '('+NonIso+theCut+')'

#canvas attributes
canx = 600
cany = 700
c1 = TCanvas('c1','Canvas Named c1',canx,cany)
c2 = TCanvas('c2','Canvas Named c2',canx,cany)
c3 = TCanvas('c3','Canvas Named c3',canx,cany)
c4 = TCanvas('c4','Canvas Named c4',canx,cany)
c5 = TCanvas('c5','Canvas Named c5',canx,cany)
c6 = TCanvas('c6','Canvas Named c6',canx,cany)
c7 = TCanvas('c7','Canvas Named c7',canx,cany)
c8 = TCanvas('c8','Canvas Named c8',canx,cany)

c1.cd()
print('')
print("data")
dataTree.Draw(leaf+'>>datah',CutsData,'')
bmindata = datah.GetXaxis().FindBin(xmin)
bmaxdata = datah.GetXaxis().FindBin(xmax)
datahSize = datah.Integral(bmindata,bmaxdata)
print(datahSize)
print('')
datah.Draw()
c1.Update()

if qcdFromData:
 # QCD from data
 c2.cd()
 print("qcd from data")
 dataTree.Draw(leaf+'>>qh',CutsDatan,'')
 bminq = qh.GetXaxis().FindBin(xmin)
 bmaxq = qh.GetXaxis().FindBin(xmax)
 qhSize = qh.Integral(bminq,bmaxq)
 print(qhSize)
 print('')
 qh.Draw()
 c2.Update()

if qcdFromMC:
 ### QCD from mc 
 c2.cd()
 print("qcd from MC")
 qTree.Draw(leaf+'>>qh',CutsMC,'')
 bminq = qh.GetXaxis().FindBin(xmin)
 bmaxq = qh.GetXaxis().FindBin(xmax)
 qhSize = qh.Integral(bminq,bmaxq)
 print(qhSize)
 print('')
 qh.Draw()
 c2.Update()

if qcdFromDsubMC:
 ### QCD from data - mc 
 c2.cd()
 print("qcd from Data-MC")
 
 tTree.Draw(leaf+'>>tnh',CutsMCn,'')
 bmintn = tnh.GetXaxis().FindBin(xmin)
 bmaxtn = tnh.GetXaxis().FindBin(xmax)
 tnhSize = tnh.Integral(bmintn,bmaxtn)
 print('    t:  '+str(tnhSize))
 #
 ttTree.Draw(leaf+'>>ttnh',CutsMCn,'')
 bminttn = ttnh.GetXaxis().FindBin(xmin)
 bmaxttn = ttnh.GetXaxis().FindBin(xmax)
 ttnhSize = ttnh.Integral(bminttn,bmaxttn)
 print('    tt: '+str(ttnhSize))
 #
 dTree.Draw(leaf+'>>dnh',CutsMCn,'')
 bmindn = dnh.GetXaxis().FindBin(xmin)
 bmaxdn = dnh.GetXaxis().FindBin(xmax)
 dnhSize = dnh.Integral(bmindn,bmaxdn)
 print('    d:  '+str(dnhSize))
 #
 wTree.Draw(leaf+'>>wnh',CutsMCn,'')
 bminwn = wnh.GetXaxis().FindBin(xmin)
 bmaxwn = wnh.GetXaxis().FindBin(xmax)
 wnhSize = wnh.Integral(bminwn,bmaxwn)
 print('    w:  '+str(wnhSize))
 #
 zTree.Draw(leaf+'>>znh',CutsMCn,'')
 bminzn = znh.GetXaxis().FindBin(xmin)
 bmaxzn = znh.GetXaxis().FindBin(xmax)
 znhSize = znh.Integral(bminzn,bmaxzn)
 print('    z:  '+str(znhSize))

 dataTree.Draw(leaf+'>>qh',CutsDatan,'')
 qh.Add(tnh,-1)
 qh.Add(ttnh,-1)
 qh.Add(dnh,-1)
 qh.Add(wnh,-1)
 qh.Add(znh,-1)
 bminq = qh.GetXaxis().FindBin(xmin)
 bmaxq = qh.GetXaxis().FindBin(xmax)
 qhSize = qh.Integral(bminq,bmaxq)
 print(qhSize)
 print('')
 qh.Draw()
 c2.Update()

c3.cd()
print('single top')
tTree.Draw(leaf+'>>th',CutsMC,'')
bmint = th.GetXaxis().FindBin(xmin)
bmaxt = th.GetXaxis().FindBin(xmax)
thSize = th.Integral(bmint,bmaxt)
print(thSize)
print('')
th.Draw()
c3.Update()
#
c4.cd()
print('ttbar')
ttTree.Draw(leaf+'>>tth',CutsMC,'')
bmintt = tth.GetXaxis().FindBin(xmin)
bmaxtt = tth.GetXaxis().FindBin(xmax)
tthSize = tth.Integral(bmintt,bmaxtt)
print(tthSize)
print('')
tth.Draw()
c4.Update()
#
c5.cd()
print('diboson')
dTree.Draw(leaf+'>>dh',CutsMC,'')
bmind = dh.GetXaxis().FindBin(xmin)
bmaxd = dh.GetXaxis().FindBin(xmax)
dhSize = dh.Integral(bmind,bmaxd)
print(dhSize)
print('')
dh.Draw()
c5.Update()
#
c6.cd()
print('w')
wTree.Draw(leaf+'>>wh',CutsMC,'')
bminw = wh.GetXaxis().FindBin(xmin)
bmaxw = wh.GetXaxis().FindBin(xmax)
whSize = wh.Integral(bminw,bmaxw)
print(whSize)
print('')
wh.Draw()
c6.Update()
#
c7.cd()
print('z')
zTree.Draw(leaf+'>>zh',CutsMC,'')
bminz = zh.GetXaxis().FindBin(xmin)
bmaxz = zh.GetXaxis().FindBin(xmax)
zhSize = zh.Integral(bminz,bmaxz)
print(zhSize)
print('')
zh.Draw()
c7.Update()

print('xmin  '+str(xmin))
print('xmax  '+str(xmax))

c8.cd()
hh.Add(qh)
hh.Add(th)
hh.Add(tth)
hh.Add(dh)
hh.Add(wh)
hh.Add(zh)
hh.SetLineColor(51)
datah.SetMinimum(0)
datah.Draw()
qh.SetLineColor(1)
th.SetLineColor(2)
tth.SetLineColor(3)
dh.SetLineColor(4)
wh.SetLineColor(5)
zh.SetLineColor(6)
hh.Draw('sames')
qh.Draw('sames')
th.Draw('sames')
tth.Draw('sames')
dh.Draw('sames')
wh.Draw('sames')
zh.Draw('sames')

leg=TLegend(0.1,0.4,0.4,0.8)
leg.AddEntry(datah,'data')
leg.AddEntry(hh,'total MC')
leg.AddEntry(wh,'W')
leg.AddEntry(tth,'t#bar{t}')
leg.AddEntry(th,'t')
leg.AddEntry(qh,'QCD')
leg.AddEntry(dh,'WW,WZ')
leg.AddEntry(zh,'Drell-Yan')
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.Draw('sames')

c8.Print(path+outfilename+'.png')
outFile.Write()

log = open(path+outfilename+'.log','w')
log.write('------------------------\n')
log.write('--'+leaf+'----\n')
log.write('------------------------\n')
log.write('------------------------\n')
log.write('datafile:  '+datafilename+'\n')
log.write('qcd file:  '+qfilename+'\n')
log.write('single t:  '+tfilename+'\n')
log.write('ttbar:     '+ttfilename+'\n')
log.write('diboson:   '+dfilename+'\n')
log.write('w file:    '+wfilename+'\n')
log.write('z file:    '+zfilename+'\n')
log.write('------------------------\n')
log.write('------------------------\n')
log.write('Cuts MC:  '+CutsMC+'\n\n')
log.write('Cuts Data:  '+CutsData+'\n\n')
log.write('Cuts Datan: '+CutsDatan+'\n\n')
log.write('QCD from Data: '+str(qcdFromData)+'\n')
log.write('QCD from MC:   '+str(qcdFromMC)+'\n')
log.write('Min Bin:  '+str(xmin)+'\n')
log.write('Max Bin:  '+str(xmax)+'\n')
log.write('------------------------\n')
log.write('data:---------'+str(datahSize)+'\n')
log.write('mc (w/ qcd):--'+str(qhSize+thSize+tthSize+dhSize+whSize+zhSize)+'\n')
log.write('qcd:----------'+str(qhSize)+'\n')
log.write('t:------------'+str(thSize)+'\n')
log.write('tt:-----------'+str(tthSize)+'\n')
log.write('dibosons:-----'+str(dhSize)+'\n')
log.write('w:------------'+str(whSize)+'\n')
log.write('drell-yan:----'+str(zhSize)+'\n')
log.write('------------------------\n')
log.write('mc NonIso (w/ qcd): '+str(qhSize+tnhSize+ttnhSize+dnhSize+wnhSize+znhSize)+'\n')
log.write('t NonIso:---------'+str(tnhSize)+'\n')
log.write('tt NonIso:--------'+str(ttnhSize)+'\n')
log.write('dibosons NonIso:--'+str(dnhSize)+'\n')
log.write('w NonIso:---------'+str(wnhSize)+'\n')
log.write('drell-yan NonIso:-'+str(znhSize)+'\n')
log.write('------------------------\n')
