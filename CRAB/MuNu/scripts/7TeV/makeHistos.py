#!/usr/bin/env python
'''
Makes a root file containing histograms for later plotting
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *

import cuts as ct
import histoRange as hr
import aHisto as h

import scaleqcd as qs


# Available Leaves: mt, met, ptMu, massDiNoBJets, massDiJets, ptDiJets, isoMuPFIsoRho, etaMu'
leaf = 'mt'
lumi = 4895.
lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)
isNr = 4
jNr = 2
bNr = 0
I = 0
F = 200

qcdFromData = False 
qcdFromMC = False
qcdFromDsubMC=True

qcdRescale = False
tRescale = False
ttRescale = False
vRescale = False
dRescale = False

qcdScale = 1
dScale = 1
qcdScale = 1
tScale = 1
vScale = 1
ttScale = 1

#dScale = 1.00323
#qcdScale = 0.313351
#tScale = 1.00342
#vScale = 1.11233
#ttScale = 1.00986

if qcdRescale:
  qcdScale = qs.scaleMe(isNr,jNr,bNr,I,F,qcdFromData,qcdFromMC,qcdFromDsubMC)

fitrange = '_'+str(I)+'_'+str(F)
re = 'unscaled'
if qcdRescale:
 re = 'rescaled'
path = '../ForAN/QCD'
extraName = str(jNr)+'j'+str(bNr)+'bIso'+str(isNr)+re+fitrange
lumi, steps, xmin, xmax, xtitle, xunits = hr.ranger(leaf)

theCut = ''
if bNr==0:
 TD = 'wtPU*wtEffIsotComb*'+str(lumi)
 btag = 'Skim'
### C2
if bNr==1:
 TD = 'CSVM1Jet*wtPU*wtEffIsotComb*'+str(lumi)
 btag = 'SomeBtag'
 ### C1 or C3
if bNr==2:
 TD = 'CSVM2Jets*wtPU*wtEffIsotComb*'+str(lumi)
# btag = 'TwoBtag'
 btag = 'Skim'

if jNr==2:
 jtag = 'Skim'
if jNr==3:
 jtag = '3jets'
if jNr==4:
 jtag = '4jets'

Iso='isoMuPF<0.12'
NonIso = 'isoMuPF>=0.'+str(isNr)
Wtau = '(abs(genWLeptonID)!=13)'
Wbx = '(genWBs==1&&abs(genWLeptonID)==13)'
Wbb = '(genWBs>1&&abs(genWLeptonID)==13)'
Wcc='(genWBs<1&&(foundC>0&&foundCbar>0)&&(abs(foundC-foundCbar)%2==0&&abs(genWLeptonID)==13))'
Wc='(genWBs<1&&(foundC>0||foundCbar>0)&&(abs(foundC-foundCbar)%2!=0)&&abs(genWLeptonID)==13)'
Wl = '(genWBs<1&&foundC<=0&&foundCbar<=0&&abs(genWLeptonID)==13)'

#Available cuts: Skim, NoMuMu, JetEta, MT, OneMuNuCand, JetPt20, JetPt30, JetPt40, 4jets30, IsDiBJet, IsDiNoBJet
nrcuts =3
cut1 = 'Skim'
cut2 = jtag
cut3 = btag
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

for i in range(nrcuts):
  theCut += '&&'+ct.cuts[CutList[i]] 

CutsMCi = '('+TD+'*('+Iso+theCut+'))'
CutsDatai = '('+Iso+theCut+')'
CutsWtaui =  '('+TD+'*('+Wtau+'&&'+Iso+theCut+'))'
CutsWbxi = '('+TD+'*('+Wbx+'&&'+Iso+theCut+'))'
CutsWbbi = '('+TD+'*('+Wbb+'&&'+Iso+theCut+'))'
CutsWcci =  '('+TD+'*('+Wcc+'&&'+Iso+theCut+'))'
CutsWci =  '('+TD+'*('+Wc+'&&'+Iso+theCut+'))'
CutsWli = '('+TD+'*('+Wl+'&&'+Iso+theCut+'))'

CutsMCn = '('+TD+'*('+NonIso+theCut+'))'
CutsDatan = '('+NonIso+theCut+')'

datafilename = '../data/MuonData_2011_WBB_VT02.root'
ttfilename = '../data/Singletop_t_VT02.root'
tsfilename = '../data/Singletop_s_VT02.root'
ttwfilename = '../data/Singletop_tW_VT02.root'
stfilename = '../data/Singletop_VT02.root'
ttbfilename = '../data/TTBAR_VT02.root'
dfilename = '../data/Dibosons_VT02.root'
wfilename = '../data/W_VT03.root'
zfilename = '../data/DYall_VT02.root'
#qfilename = '../data/QCDMu_V13.root'

datafile = TFile(datafilename)
ttfile = TFile(ttfilename)
tsfile = TFile(tsfilename)
ttwfile = TFile(ttwfilename)
ttbfile = TFile(ttbfilename)
stfile = TFile(stfilename)
dfile = TFile(dfilename)
wfile = TFile(wfilename)
zfile = TFile(zfilename)
#qfile = TFile(qfilename)

outFile=gROOT.FindObject(path+leaf+extraName+'.root')
if outFile : outFile.Close()
outFile = TFile(path+leaf+extraName+'.root','RECREATE','Demo ROOT file')

eventTreeLocation = 'muNuJetJetEventTree/eventTree'

dataTree = datafile.Get(eventTreeLocation)
ttTree = ttfile.Get(eventTreeLocation)
tsTree = tsfile.Get(eventTreeLocation)
stTree = stfile.Get(eventTreeLocation)
ttwTree = ttwfile.Get(eventTreeLocation)
ttbTree = ttbfile.Get(eventTreeLocation)
dTree = dfile.Get(eventTreeLocation)
wTree = wfile.Get(eventTreeLocation)
zTree = zfile.Get(eventTreeLocation)
#qTree = qfile.Get(eventTreeLocation)

log = open(path+leaf+extraName+'.log','w')

print('----------------')
print('     --'+leaf+'--')
print(extraName)
print('----------------')

###
datanh,datanhSize,datanhSizePart = h.gram(dataTree,leaf,xmin,xmax,steps,CutsDatan,I,F)
print('data nonIso')
datanh.SetName('datanh')
print('  '+str(datanhSize))
print('  '+str(datanhSizePart))
###

if qcdFromData or qcdFromMC or qcdFromDsubMC:
 if qcdFromData:
  print('qcd from data')
  dataTree.Draw(leaf+'>>qh',CutsDatan,'')
     
 elif qcdFromMC:
  print('qcd from mc')
  qTree.Draw(leaf+'>>qh',CutsMCi,'')
 
 elif qcdFromDsubMC:
  print('qcd from data sub mc')
  ###
  print('  z nonIso')
  znh,znhSize,znhSizePart = h.gram(zTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  znh.SetName('znh')
  print('    '+str(znhSize))
  print('    '+str(znhSizePart))
  ###
  print('  d nonIso')
  dnh,dnhSize,dnhSizePart = h.gram(dTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  dnh.SetName('dnh')
  print('    '+str(dnhSize))
  print('    '+str(dnhSizePart))
  ###
  print('  singletop nonIso')
  stnh,stnhSize,stnhSizePart = h.gram(stTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  stnh.SetName('stnh')
  print('    '+str(stnhSize))
  print('    '+str(stnhSizePart))
  ###
  print('  ttbar nonIso')
  ttbnh,ttbnhSize,ttbnhSizePart = h.gram(ttbTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  ttbnh.SetName('ttbnh')
  print('    '+str(ttbnhSize))
  print('    '+str(ttbnhSizePart))
  ###
  print('  w nonIso')
  wnh,wnhSize,wnhSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  wnh.SetName('wnh')
  print('    '+str(wnhSize))
  print('    '+str(wnhSizePart))

  qh = datanh.Clone()
  qh.SetName('qh')
  qh.Add(znh,-1)
  qh.Add(dnh,-1)
  qh.Add(stnh,-1)
  qh.Add(ttbnh,-1)
  qh.Add(wnh,-1)

 print('qcd')
 qh.SetTitle('')
 bminq = qh.GetXaxis().FindBin(xmin)
 bmaxq = qh.GetXaxis().FindBin(xmax)
 bIq = qh.GetXaxis().FindBin(I)
 bFq = qh.GetXaxis().FindBin(F)
 qhSizePart = qh.Integral(bIq,bFq)
 qh.Scale(qcdScale)
 qhSize = qh.Integral(bminq,bmaxq)
 print('  '+str(qhSize))
 print('  '+str(qhSizePart))
 
else:
 print('no qcd?')
 qhSize = 0
 qhSizePart = 0
 qh = 0
 ### not sure if this is handled correctly

###
print("data Iso") 
dataih,dataihSize,dataihSizePart = h.gram(dataTree,leaf,xmin,xmax,steps,CutsDatai,I,F)
dataih.SetName('dataih')
print('  '+str(dataihSize))
print('  '+str(dataihSizePart))
dimax = dataih.GetMaximum()
###
print("z Iso")
zih,zihSize,zihSizePart = h.gram(zTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
zih.SetName('zih')
zih.Scale(vScale)
print('  '+str(zihSize))
print('  '+str(zihSizePart))
###
print("d Iso")
dih,dihSize,dihSizePart = h.gram(dTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
dih.SetName('dih')
dih.Scale(dScale)
print('  '+str(dihSize))
print('  '+str(dihSizePart))
###
print('tt Iso')
ttih,ttihSize,ttihSizePart = h.gram(ttTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
ttih.SetName('ttih')
ttih.Scale(tScale)
print('  '+str(ttihSize))
print('  '+str(ttihSizePart))
###
print('ts Iso')
tsih,tsihSize,tsihSizePart = h.gram(tsTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
tsih.SetName('tsih')
tsih.Scale(tScale)
print('  '+str(tsihSize))
print('  '+str(tsihSizePart))
###
print('ttw Iso')
ttwih,ttwihSize,ttwihSizePart = h.gram(ttwTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
ttwih.SetName('ttwih')
ttwih.Scale(tScale)
print('  '+str(ttwihSize))
print('  '+str(ttwihSizePart))
###
print('ttb Iso')
ttbih,ttbihSize,ttbihSizePart = h.gram(ttbTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
ttbih.SetName('ttbih')
ttbih.Scale(ttScale)
print('  '+str(ttbihSize))
print('  '+str(ttbihSizePart))
###
print('wtau Iso')
wtih,wtihSize,wtihSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsWtaui,I,F)
wtih.SetName('wtih')
wtih.Scale(vScale)
print('  '+str(wtihSize))
print('  '+str(wtihSizePart))
###
print('wbx Iso')
wbih,wbihSize,wbihSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsWbxi,I,F)
wbih.SetName('wbih')
wbih.Scale(vScale)
print('  '+str(wbihSize))
print('  '+str(wbihSizePart))
###
print('wbb Iso')
wbbih,wbbihSize,wbbihSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsWbbi,I,F)
wbbih.SetName('wbbih')
wbbih.Scale(vScale)
print('  '+str(wbbihSize))
print('  '+str(wbbihSizePart))
###
print('wcc Iso')
wccih,wccihSize,wccihSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsWcci,I,F)
wccih.SetName('wccih')
wccih.Scale(vScale)
print('  '+str(wccihSize))
print('  '+str(wccihSizePart))
###
print('wc Iso')
wcih,wcihSize,wcihSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsWci,I,F)
wcih.SetName('wcih')
wcih.Scale(vScale)
print('  '+str(wcihSize))
print('  '+str(wcihSizePart))
###
print('wl Iso')
wlih,wlihSize,wlihSizePart = h.gram(wTree,leaf,xmin,xmax,steps,CutsWli,I,F)
wlih.SetName('wlih')
wlih.Scale(vScale)
print('  '+str(wlihSize))
print('  '+str(wlihSizePart))

hh = TH1F('hh','hh',steps,xmin,xmax)
hh.Add(qh)
hh.Add(zih)
hh.Add(dih)
hh.Add(ttih)
hh.Add(tsih)
hh.Add(ttwih)
hh.Add(ttbih)
hh.Add(wtih)
hh.Add(wbih)
hh.Add(wbbih)
hh.Add(wccih)
hh.Add(wcih)
hh.Add(wlih)
hh.Draw()

outFile.Write()
print('')
print('Your File is here: '+path+leaf+extraName+'.root')
print('')

log.write('------------------------------------------------\n')
log.write('No QCD or Data  \n')
log.write('QCD from Data:    '+str(qcdFromData)+'\n')
log.write('QCD from MC:      '+str(qcdFromMC)+'\n')
log.write('QCD from Data-MC: '+str(qcdFromDsubMC)+'\n\n')
log.write('Non Isolated\n')
log.write('---------------------------\n')
log.write(' Cuts MC:  '+str(CutsMCn)+'\n\n')
log.write(' Cuts Data: '+str(CutsDatan)+'\n\n')
log.write('Isolated\n')
log.write('---------------------------\n')
log.write(' Cuts MC:  '+str(CutsMCi)+'\n\n')
log.write(' Cuts Data: '+str(CutsDatai)+'\n\n')
log.write(' Cuts Wtau: '+str(CutsWtaui)+'\n\n')
log.write(' Cuts Wbx: '+str(CutsWbxi)+'\n\n')
log.write(' Cuts Wbb: '+str(CutsWbbi)+'\n\n')
log.write(' Cuts Wcc: '+str(CutsWcci)+'\n\n')
log.write(' Cuts Wc: '+str(CutsWci)+'\n\n')
log.write(' Cuts Wl: '+str(CutsWli)+'\n\n')
log.write('Anti-Isolated Sizes\n')
log.write('---------------------------\n')
log.write(' W Size:---------'+str(wnhSize)+'\n')
log.write(' tt Size:--------'+str(ttbnhSize)+'\n')
log.write(' singletop Size:-'+str(stnhSize)+'\n')
log.write(' WW,WZ Size:-----'+str(dnhSize)+'\n')
log.write(' Drell-Yan Size:-'+str(znhSize)+'\n')
log.write(' QCD Size:-------'+str(qhSize)+'\n')
log.write(' Data Size:      '+str(datanhSize)+'\n')
log.write('---------------------------\n')
log.write('Anti-Isolated Sizes from '+str(I)+' to '+str(F)+'\n')
log.write('---------------------------\n')
log.write(' W Size:---------'+str(wnhSizePart)+'\n')
log.write(' tt Size:--------'+str(ttbnhSizePart)+'\n')
log.write(' singletop Size:-'+str(stnhSizePart)+'\n')
log.write(' WW,WZ Size:-----'+str(dnhSizePart)+'\n')
log.write(' Drell-Yan Size:-'+str(znhSizePart)+'\n')
log.write(' QCD Size:-------'+str(qhSizePart)+'\n')
log.write(' Data Size:      '+str(datanhSizePart)+'\n')
log.write('---------------------------------------------\n')
log.write('QCD Scale:   '+str(qcdScale)+'\n')
log.write('W,Z Scale:   '+str(vScale)+'\n')
log.write('t Scale:     '+str(tScale)+'\n')
log.write('tt Scale:    '+str(ttScale)+'\n')
log.write('Dibo Scale:  '+str(dScale)+'\n')
log.write('---------------------------------------------\n')
log.write('Isolated Sizes from '+str(I)+' to '+str(F)+'\n')
log.write('---------------------------\n')
log.write('W+light:--------'+str(wlihSizePart)+'\n')
log.write('W+c:------------'+str(wcihSizePart)+'\n')
log.write('W+cc:-----------'+str(wccihSizePart)+'\n')
log.write('W+bb:-----------'+str(wbbihSizePart)+'\n')
log.write('W+bx:-----------'+str(wbihSizePart)+'\n')
log.write('W+tau:----------'+str(wtihSizePart)+'\n')
log.write('tt Size:--------'+str(ttbihSizePart)+'\n')
log.write('t_tW Size:------'+str(ttwihSizePart)+'\n')
log.write('t_s Size:-------'+str(tsihSizePart)+'\n')
log.write('t_t Size:-------'+str(ttihSizePart)+'\n')
log.write('WW,WZ Size:-----'+str(dihSizePart)+'\n')
log.write('Drell-Yan Size:-'+str(zihSizePart)+'\n')
log.write('MC Size (no QCD):   '+str(zihSizePart+dihSizePart+ttihSizePart+tsihSizePart+ttwihSizePart+ttbihSizePart+wtihSizePart+wbihSizePart+wbbihSizePart+wccihSizePart+wcihSizePart+wlihSizePart)+'\n')
log.write('MC Size (with QCD):   '+str(zihSizePart+dihSizePart+ttihSizePart+tsihSizePart+ttwihSizePart+ttbihSizePart+wtihSizePart+wbihSizePart+wbbihSizePart+wccihSizePart+wcihSizePart+wlihSizePart+qhSizePart)+'\n')
log.write('Data Size:          '+str(dataihSizePart)+'\n')
log.write('---------------------------------------------\n')
log.write('Isolated Sizes\n')
log.write('---------------------------\n')
log.write('W+light:--------'+str(wlihSize)+'\n')
log.write('W+c:------------'+str(wcihSize)+'\n')
log.write('W+cc:-----------'+str(wccihSize)+'\n')
log.write('W+bb:-----------'+str(wbbihSize)+'\n')
log.write('W+bx:-----------'+str(wbihSize)+'\n')
log.write('W+tau:----------'+str(wtihSize)+'\n')
log.write('tt Size:--------'+str(ttbihSize)+'\n')
log.write('t_tW Size:------'+str(ttwihSize)+'\n')
log.write('t_s Size:-------'+str(tsihSize)+'\n')
log.write('t_t Size:-------'+str(ttihSize)+'\n')
log.write('WW,WZ Size:-----'+str(dihSize)+'\n')
log.write('Drell-Yan Size:-'+str(zihSize)+'\n')
log.write('MC Size (no QCD):   '+str(zihSize+dihSize+ttihSize+tsihSize+ttwihSize+ttbihSize+wtihSize+wbihSize+wbbihSize+wccihSize+wcihSize+wlihSize)+'\n')
log.write('MC Size (with QCD): '+str(zihSize+dihSize+qhSize+ttihSize+tsihSize+ttwihSize+ttbihSize+wtihSize+wbihSize+wbbihSize+wccihSize+wcihSize+wlihSize)+'\n')
log.write('Data Size:          '+str(dataihSize)+'\n')
log.write('---------------------------\n')
log.write('---------------------------------------------\n')

log.close()

