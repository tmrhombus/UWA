#!/usr/bin/env python
'''
Plots your leaf with way many hidden options.
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F,TPad,TLine
from ROOT import TLatex
from ROOT import gROOT,gStyle
#from ROOT import *

import cuts as ct
import histoRange as hr
import qcdScales as qs

# Available Leaves: mt, met, ptMu, massDiNoBJets, massDiJets, ptDiJets, isoMuPFIsoRho, etaMu'
leaf = 'mt'
lumi = 4895.
lumiTitle = '#int L dt = %.1f pb^{-1}' %(lumi/1000.)
isNr = 2
jNr = 2
bNr = 0
I = 0
F = 20

qcdFromData = False 
qcdFromMC = False
qcdFromDsubMC=True
qcdRescale = True
extraEffects = True

fitrange = '_'+str(I)+'_'+str(F)
re = 'unscaled'
if qcdRescale:
 re = 'r'
path = '../scratch/'
extraName = str(jNr)+'j'+str(bNr)+'bIso'+str(isNr)+re+fitrange

print('----------------')
print('     --'+leaf+'--')
print(extraName)
print('----------------')
lumi, steps, xmin, xmax, xtitle, xunits = hr.ranger(leaf)

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

#color scheme
d = 1
q = ROOT.EColor.kRed+1
z = ROOT.EColor.kOrange-3
d = ROOT.EColor.kYellow-3
tt = ROOT.EColor.kGreen+1
ts = ROOT.EColor.kGreen-5
ttw = ROOT.EColor.kGreen+3 
ttb = ROOT.EColor.kGreen-9
wtau = ROOT.EColor.kAzure-7
wbx = ROOT.EColor.kCyan
wbb = 51#ROOT.EColor.kCyan
wcc = ROOT.EColor.kAzure+2
wc = ROOT.EColor.kBlue+1
wl = ROOT.EColor.kAzure+10

#canvas attributes
canx = 570
cany = 900

datafilename = '../data/MuonData_2011_WBB_COMMON_V12.root'
ttfilename = '../data/Singletop_t_V13.root'
tsfilename = '../data/Singletop_s_V13.root'
ttwfilename = '../data/Singletop_tW_V13.root'
stfilename = '../data/Singletop_V13.root'
ttbfilename = '../data/TTBAR_V13.root'
dfilename = '../data/Dibosons_V13.root'
wfilename = '../data/W_V13.root'
zfilename = '../data/DYall_V13.root'
qfilename = '../data/QCDMu_V13.root'

datafile = TFile(datafilename)
ttfile = TFile(ttfilename)
tsfile = TFile(tsfilename)
ttwfile = TFile(ttwfilename)
ttbfile = TFile(ttbfilename)
stfile = TFile(stfilename)
dfile = TFile(dfilename)
wfile = TFile(wfilename)
zfile = TFile(zfilename)
qfile = TFile(qfilename)

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
qTree = qfile.Get(eventTreeLocation)

gStyle.SetOptStat('')
hs = THStack('hs','')
hs.SetTitle('')

dataih = TH1F('dataih','dataih',steps,xmin,xmax)
datanh = TH1F('datanh','datanh',steps,xmin,xmax)
datar = TH1F('datar','datar',steps,xmin,xmax)
dataih.Sumw2()
dataih.SetMarkerStyle(22)
dataih.SetMarkerSize(1.5)
datar.Sumw2()
datar.SetMarkerStyle(22)
datar.SetMarkerSize(1.5)

zih = TH1F('zih','zih',steps,xmin,xmax)
dih = TH1F('dih','dih',steps,xmin,xmax)
ttih = TH1F('ttih','ttih',steps,xmin,xmax)
tsih = TH1F('tsih','tsih',steps,xmin,xmax)
ttwih = TH1F('ttwih','ttwih',steps,xmin,xmax)
ttbih = TH1F('ttbih','ttbih',steps,xmin,xmax)
wtih = TH1F('wtih','wtih',steps,xmin,xmax)
wbih = TH1F('wbih','wbih',steps,xmin,xmax)
wbbih = TH1F('wbbih','wbbih',steps,xmin,xmax)
wccih = TH1F('wccih','wccih',steps,xmin,xmax)
wcih = TH1F('wcih','wcih',steps,xmin,xmax)
wlih = TH1F('wlih','wlih',steps,xmin,xmax)
hh = TH1F('hh','hh',steps,xmin,xmax)

znh = TH1F('znh','znh',steps,xmin,xmax)
dnh = TH1F('dnh','dnh',steps,xmin,xmax)
stnh = TH1F('stnh','stnh',steps,xmin,xmax)
ttbnh = TH1F('ttbnh','ttbnh',steps,xmin,xmax)
wnh = TH1F('wnh','wnh',steps,xmin,xmax)
qh = TH1F('qh','qh',steps,xmin,xmax)

log = open(path+leaf+extraName+'Ratio.log','w')

c = TCanvas('c','Canvas Named c',canx,cany)
c.cd()
p1=TPad('p1','p1',0,0.3,1,1)
p1.SetBottomMargin(0)
p1.Draw()
p1.cd()
#p1.SetLogy()

###
print('data nonIso')
dataTree.Draw(leaf+'>>datanh',CutsDatan,'')
datanh.SetTitle('')
bmindatan = datanh.GetXaxis().FindBin(xmin)
bmaxdatan = datanh.GetXaxis().FindBin(xmax)
bIdata = datanh.GetXaxis().FindBin(I)
bFdata = datanh.GetXaxis().FindBin(F)
datanhSize = datanh.Integral(bmindatan,bmaxdatan)
datahSizePart = datanh.Integral(bIdata,bFdata)
print('  '+str(datanhSize))
print('  '+str(datahSizePart))
###
qcdScale = 1
if qcdRescale:
  qcdScale = qs.scaleMe(isNr,jNr,bNr,I,F,qcdFromData,qcdFromMC,qcdFromDsubMC)

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
  zTree.Draw(leaf+'>>znh',CutsMCn,'')
  znh.SetTitle('')
  znh.SetFillColor(z)
  bminzn = znh.GetXaxis().FindBin(xmin)
  bmaxzn = znh.GetXaxis().FindBin(xmax)
  znhSize = znh.Integral(bminzn,bmaxzn)
  bminznA = znh.GetXaxis().FindBin(I)
  bmaxznA = znh.GetXaxis().FindBin(F)
  znhSizeA = znh.Integral(bminznA,bmaxznA)
  print('    '+str(znhSize))
  print('    '+str(znhSizeA))
  ###
  print('  d nonIso')
  dTree.Draw(leaf+'>>dnh',CutsMCn,'')
  dnh.SetTitle('')
  dnh.SetFillColor(d)
  bmindn = dnh.GetXaxis().FindBin(xmin)
  bmaxdn = dnh.GetXaxis().FindBin(xmax)
  dnhSize = dnh.Integral(bmindn,bmaxdn)
  bmindnA = dnh.GetXaxis().FindBin(I)
  bmaxdnA = dnh.GetXaxis().FindBin(F)
  dnhSizeA = dnh.Integral(bmindnA,bmaxdnA)
  print('    '+str(dnhSize))
  print('    '+str(dnhSizeA))
  ###
  print('  singletop nonIso')
  stTree.Draw(leaf+'>>stnh',CutsMCn,'')
  stnh.SetTitle('')
  stnh.SetFillColor(tt)
  bminstn = stnh.GetXaxis().FindBin(xmin)
  bmaxstn = stnh.GetXaxis().FindBin(xmax)
  stnhSize = stnh.Integral(bminstn,bmaxstn)
  bmintnA = stnh.GetXaxis().FindBin(I)
  bmaxtnA = stnh.GetXaxis().FindBin(F)
  stnhSizeA = stnh.Integral(bmintnA,bmaxtnA)
  print('    '+str(stnhSize))
  print('    '+str(stnhSizeA))
  ###
  print('  ttbar nonIso')
  ttbTree.Draw(leaf+'>>ttbnh',CutsMCn,'')
  ttbnh.SetTitle('')
  ttbnh.SetFillColor(ttb)
  bminttbn = ttbnh.GetXaxis().FindBin(xmin)
  bmaxttbn = ttbnh.GetXaxis().FindBin(xmax)
  ttbnhSize = ttbnh.Integral(bminttbn,bmaxttbn)
  bminttnA = ttbnh.GetXaxis().FindBin(I)
  bmaxttnA = ttbnh.GetXaxis().FindBin(F)
  ttbnhSizeA = ttbnh.Integral(bminttnA,bmaxttnA)
  print('    '+str(ttbnhSize))
  print('    '+str(ttbnhSizeA))
  ###
  print('  w nonIso')
  wTree.Draw(leaf+'>>wnh',CutsMCn,'')
  wnh.SetTitle('')
  wnh.SetFillColor(wtau)
  bminwn = wnh.GetXaxis().FindBin(xmin)
  bmaxwn = wnh.GetXaxis().FindBin(xmax)
  wnhSize = wnh.Integral(bminwn,bmaxwn)
  bminwnA = wnh.GetXaxis().FindBin(I)
  bmaxwnA = wnh.GetXaxis().FindBin(F)
  wnhSizeA = wnh.Integral(bminwnA,bmaxwnA)
  print('    '+str(wnhSize))
  print('    '+str(wnhSizeA))
 

  qh = datanh.Clone()
  qh.SetName('qh')
  qh.Add(znh,-1)
  qh.Add(dnh,-1)
  qh.Add(stnh,-1)
  qh.Add(ttbnh,-1)
  qh.Add(wnh,-1)

 print('qcd')
 qh.SetTitle('')
 qh.SetFillColor(q)
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
dataTree.Draw(leaf+'>>dataih',CutsDatai,'')
dataih.SetTitle('')
bmindatai = dataih.GetXaxis().FindBin(xmin)
bmaxdatai = dataih.GetXaxis().FindBin(xmax)
dataihSize = dataih.Integral(bmindatai,bmaxdatai)
bIdi = dataih.GetXaxis().FindBin(I)
bFdi = dataih.GetXaxis().FindBin(F)
dataihSizePart = dataih.Integral(bIdi,bFdi)
print('  '+str(dataihSize))
print('  '+str(dataihSizePart))
dimax = dataih.GetMaximum()
###
print("z Iso")
zTree.Draw(leaf+'>>zih',CutsMCi,'')
zih.SetTitle('')
zih.SetFillColor(z)
bminzi = zih.GetXaxis().FindBin(xmin)
bmaxzi = zih.GetXaxis().FindBin(xmax)
zihSize = zih.Integral(bminzi,bmaxzi)
bminziA = zih.GetXaxis().FindBin(I)
bmaxziA = zih.GetXaxis().FindBin(F)
zihSizeA = zih.Integral(bminziA,bmaxziA)
print('  '+str(zihSize))
print('  '+str(zihSizeA))
###
print("d Iso")
dTree.Draw(leaf+'>>dih',CutsMCi,'')
dih.SetTitle('')
dih.SetFillColor(d)
bmindi = dih.GetXaxis().FindBin(xmin)
bmaxdi = dih.GetXaxis().FindBin(xmax)
dihSize = dih.Integral(bmindi,bmaxdi)
bmindiA = dih.GetXaxis().FindBin(I)
bmaxdiA = dih.GetXaxis().FindBin(F)
dihSizeA = dih.Integral(bmindiA,bmaxdiA)
print('  '+str(dihSize))
print('  '+str(dihSizeA))
###
print('tt Iso')
ttTree.Draw(leaf+'>>ttih',CutsMCi,'')
ttih.SetTitle('')
ttih.SetFillColor(tt)
bmintti = ttih.GetXaxis().FindBin(xmin)
bmaxtti = ttih.GetXaxis().FindBin(xmax)
ttihSize = ttih.Integral(bmintti,bmaxtti)
bminttiA = ttih.GetXaxis().FindBin(I)
bmaxttiA = ttih.GetXaxis().FindBin(F)
ttihSizeA = ttih.Integral(bminttiA,bmaxttiA)
print('  '+str(ttihSize))
print('  '+str(ttihSizeA))
###
print('ts Iso')
tsTree.Draw(leaf+'>>tsih',CutsMCi,'')
tsih.SetTitle('')
tsih.SetFillColor(ts)
bmintsi = tsih.GetXaxis().FindBin(xmin)
bmaxtsi = tsih.GetXaxis().FindBin(xmax)
tsihSize = tsih.Integral(bmintsi,bmaxtsi)
bmintsiA = tsih.GetXaxis().FindBin(I)
bmaxtsiA = tsih.GetXaxis().FindBin(F)
tsihSizeA = tsih.Integral(bmintsiA,bmaxtsiA)
print('  '+str(tsihSize))
print('  '+str(tsihSizeA))
###
print('ttw Iso')
ttwTree.Draw(leaf+'>>ttwih',CutsMCi,'')
ttwih.SetTitle('')
ttwih.SetFillColor(ttw)
bminttwi = ttwih.GetXaxis().FindBin(xmin)
bmaxttwi = ttwih.GetXaxis().FindBin(xmax)
ttwihSize = ttwih.Integral(bminttwi,bmaxttwi)
bminttwiA = ttwih.GetXaxis().FindBin(I)
bmaxttwiA = ttwih.GetXaxis().FindBin(F)
ttwihSizeA = ttwih.Integral(bminttwiA,bmaxttwiA)
print('  '+str(ttwihSize))
print('  '+str(ttwihSizeA))
###
print('ttb Iso')
ttbTree.Draw(leaf+'>>ttbih',CutsMCi,'')
ttbih.SetTitle('')
ttbih.SetFillColor(ttb)
bminttbi = ttbih.GetXaxis().FindBin(xmin)
bmaxttbi = ttbih.GetXaxis().FindBin(xmax)
ttbihSize = ttbih.Integral(bminttbi,bmaxttbi)
bminttbiA = ttbih.GetXaxis().FindBin(I)
bmaxttbiA = ttbih.GetXaxis().FindBin(F)
ttbihSizeA = ttbih.Integral(bminttbiA,bmaxttbiA)
print('  '+str(ttbihSize))
print('  '+str(ttbihSizeA))
###
print('wtau Iso')
wTree.Draw(leaf+'>>wtih',CutsWtaui,'')
wtih.SetTitle('')
wtih.SetFillColor(wtau)
bminwti = wtih.GetXaxis().FindBin(xmin)
bmaxwti = wtih.GetXaxis().FindBin(xmax)
wtihSize = wtih.Integral(bminwti,bmaxwti)
bminwtiA = wtih.GetXaxis().FindBin(I)
bmaxwtiA = wtih.GetXaxis().FindBin(F)
wtihSizeA = wtih.Integral(bminwtiA,bmaxwtiA)
print('  '+str(wtihSize))
print('  '+str(wtihSizeA))
###
print('wbx Iso')
wTree.Draw(leaf+'>>wbih',CutsWbxi,'')
wbih.SetTitle('')
wbih.SetFillColor(wbx)
bminwbi = wbih.GetXaxis().FindBin(xmin)
bmaxwbi = wbih.GetXaxis().FindBin(xmax)
wbihSize = wbih.Integral(bminwbi,bmaxwbi)
bminwbiA = wbih.GetXaxis().FindBin(I)
bmaxwbiA = wbih.GetXaxis().FindBin(F)
wbihSizeA = wbih.Integral(bminwbiA,bmaxwbiA)
print('  '+str(wbihSize))
print('  '+str(wbihSizeA))
###
print('wbb Iso')
wTree.Draw(leaf+'>>wbbih',CutsWbbi,'')
wbbih.SetTitle('')
wbbih.SetFillColor(wbb)
bminwbbi = wbbih.GetXaxis().FindBin(xmin)
bmaxwbbi = wbbih.GetXaxis().FindBin(xmax)
wbbihSize = wbbih.Integral(bminwbbi,bmaxwbbi)
bminwbbiA = wbbih.GetXaxis().FindBin(I)
bmaxwbbiA = wbbih.GetXaxis().FindBin(F)
wbbihSizeA = wbbih.Integral(bminwbbiA,bmaxwbbiA)
print('  '+str(wbbihSize))
print('  '+str(wbbihSizeA))
###
print('wcc Iso')
wTree.Draw(leaf+'>>wccih',CutsWcci,'')
wccih.SetTitle('')
wccih.SetFillColor(wcc)
bminwcci = wccih.GetXaxis().FindBin(xmin)
bmaxwcci = wccih.GetXaxis().FindBin(xmax)
wccihSize = wccih.Integral(bminwcci,bmaxwcci)
bminwcciA = wccih.GetXaxis().FindBin(I)
bmaxwcciA = wccih.GetXaxis().FindBin(F)
wccihSizeA = wccih.Integral(bminwcciA,bmaxwcciA)
print('  '+str(wccihSize))
print('  '+str(wccihSizeA))
###
print('wc Iso')
wTree.Draw(leaf+'>>wcih',CutsWci,'')
wcih.SetTitle('')
wcih.SetFillColor(wc)
bminwci = wcih.GetXaxis().FindBin(xmin)
bmaxwci = wcih.GetXaxis().FindBin(xmax)
wcihSize = wcih.Integral(bminwci,bmaxwci)
bminwciA = wcih.GetXaxis().FindBin(I)
bmaxwciA = wcih.GetXaxis().FindBin(F)
wcihSizeA = wcih.Integral(bminwciA,bmaxwciA)
print('  '+str(wcihSize))
print('  '+str(wcihSizeA))
###
print('wl Iso')
wTree.Draw(leaf+'>>wlih',CutsWli,'')
wlih.SetTitle('')
wlih.SetFillColor(wl)
bminwli = wlih.GetXaxis().FindBin(xmin)
bmaxwli = wlih.GetXaxis().FindBin(xmax)
wlihSize = wlih.Integral(bminwli,bmaxwli)
bminwliA = wlih.GetXaxis().FindBin(I)
bmaxwliA = wlih.GetXaxis().FindBin(F)
wlihSizeA = wlih.Integral(bminwliA,bmaxwliA)
print('  '+str(wlihSize))
print('  '+str(wlihSizeA))

hs.Add(qh)
hs.Add(zih)
hs.Add(dih)
hs.Add(ttih)
hs.Add(tsih)
hs.Add(ttwih)
hs.Add(ttbih)
hs.Add(wtih)
hs.Add(wbih)
hs.Add(wbbih)
hs.Add(wccih)
hs.Add(wcih)
hs.Add(wlih)

leg=TLegend(0.7,0.4,0.9,0.8)
leg.AddEntry(dataih,'data')
leg.AddEntry(wlih,'W(#mu#nu)+light')
leg.AddEntry(wcih,'W(#mu#nu)+c')
leg.AddEntry(wccih,'W(#mu#nu)+cc')
leg.AddEntry(wbbih,'W(#mu#nu)+bb')
leg.AddEntry(wbih,'W(#mu#nu)+bx')
leg.AddEntry(wtih,'W(#tau#nu)')
leg.AddEntry(ttbih,'t#bar{t}')
leg.AddEntry(ttwih,'t_tW')
leg.AddEntry(tsih,'t_s')
leg.AddEntry(ttih,'t_t')
leg.AddEntry(dih,'WW,WZ')
leg.AddEntry(zih,'Drell-Yan')
leg.AddEntry(qh,'QCD')
leg.SetFillColor(0)
leg.SetBorderSize(0)
leg.Draw()

mtTitle = xtitle+' Data v MC'
hs.Draw()
hsmax = hs.GetMaximum()
if (dimax>hsmax):
 hs.SetMaximum(1.2*dimax)
elif(hsmax>=dimax):
 hs.SetMaximum(1.2*hsmax)
if leaf == ('jet1BTag_CSV') or ('jet2BTag_CSV'):
  if (dimax>hsmax):
   hs.SetMaximum(dimax)
  elif(hsmax>=dimax):
   hs.SetMaximum(hsmax)
print(dimax)
print(hsmax)
hs.GetXaxis().SetTitle(xtitle+' ['+xunits+']')
if extraEffects:
 if leaf=="mt":
  hs.GetXaxis().SetRangeUser(0,20)
 if leaf=="massDiNoBJets":
  hs.GetXaxis().SetRangeUser(30,200)
# if leaf=="met":
#  hs.GetXaxis().SetRangeUser(10,140)
 if leaf=="isoMuPF":
  hs.GetYaxis().SetRangeUser(0.5,dmax)

hs.Draw()
dataih.Draw('e1p,sames')
leg.Draw('sames')
tex.DrawLatex(0,1,mtTitle)
tex.SetTextSize(0.03)
tex.SetTextAlign(33)
tex.DrawLatex(0.87,0.87,lumiTitle)
tex.DrawLatex(0,0.9,'Events/ %.001f' %((xmax-xmin)/(steps)))

if extraEffects:
 if leaf == 'massDiNoBJets':
   l = TLine(80.4,0,80.4,hsmax)
   l.SetLineColor(99)
   l.Draw()
 if (leaf == 'jet1BTag_CSV') or (leaf == 'jet2BTag_CSV'):
   a1 = TArrow(0.244,dimax,0.244,0)
   a1.SetLineWidth(3)
   a1.Draw()
   a2 = TArrow(0.679,dimax,0.679,0)
   a2.SetLineWidth(3)
   a2.Draw()
   a3 = TArrow(0.898,dimax,0.898,0)
   a3.SetLineWidth(3)
   a3.Draw()
 if (leaf == 'isoMuPF'):
   a1 = TArrow(0.12,dimax,0.12,0)
   a1.SetLineColor(7)
   a1.SetLineWidth(3)
   a1.Draw()
   a2 = TArrow(0.2,dimax,0.2,0)
   a2.SetLineColor(7)
   a2.SetLineWidth(3)
   a2.Draw()

c.cd()
p2=TPad('p2','p2',0,0,1,0.2)
p2.SetTopMargin(0)
p2.Draw()
p2.cd()

hh.Add(zih)
hh.Add(dih)
hh.Add(qh)
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
datar = dataih.Clone()
datar.SetName('datar')
datar.GetYaxis().SetRangeUser(0.5,1.5) 
datar.Divide(hh)
datar.Draw('ep')
if extraEffects:
 if leaf=="mt":
  datar.GetXaxis().SetRangeUser(0,20)
  lb=TLine(0,1,20,1)
  lb.SetLineStyle(3)
  lb.Draw()
 if leaf=='massDiNoBJets':
  datar.GetXaxis().SetRangeUser(30,200)
  lb=TLine(30,1,200,1)
  lb.SetLineStyle(3)
  lb.Draw()
# elif leaf=="met":
#  datar.GetXaxis().SetRangeUser(10,140)
#  lb=TLine(10,1,140,1)
#  lb.SetLineStyle(3)
#  lb.Draw()
 else:
  lb=TLine(xmin,1,xmax,1)
  lb.SetLineStyle(3)
  lb.Draw()
datar.GetYaxis().SetLabelSize(0.12)

c.Print(path+leaf+extraName+'Ratio.png')
print('Here is your file sir or madam:   '+path+leaf+extraName+'Ratio.png')
print('  ')
outFile.Write()
c.Close()

log.write('Made plot '+path+leaf+extraName+'Ratio.png\n')
log.write('---------------------------------------------\n')
log.write('QCD from Data:    '+str(qcdFromData)+'\n')
log.write('QCD from MC:      '+str(qcdFromMC)+'\n')
log.write('QCD from Data-MC: '+str(qcdFromDsubMC)+'\n\n')
log.write('Non Isolated\n')
log.write('------------\n')
log.write(' Cuts MC:  '+str(CutsMCn)+'\n\n')
log.write(' Cuts Data: '+str(CutsDatan)+'\n\n')
log.write('Isolated\n')
log.write('------------\n')
log.write(' Cuts MC:  '+str(CutsMCi)+'\n\n')
log.write(' Cuts Data: '+str(CutsDatai)+'\n\n')
log.write(' Cuts Wtau: '+str(CutsWtaui)+'\n\n')
log.write(' Cuts Wbx: '+str(CutsWbxi)+'\n\n')
log.write(' Cuts Wbb: '+str(CutsWbbi)+'\n\n')
log.write(' Cuts Wcc: '+str(CutsWcci)+'\n\n')
log.write(' Cuts Wc: '+str(CutsWci)+'\n\n')
log.write(' Cuts Wl: '+str(CutsWli)+'\n\n')
log.write('Anti-Isolated Sizes\n')
log.write('--------------------\n')
log.write('W Size:---------'+str(wnhSize)+'\n')
log.write('tt Size:--------'+str(ttbnhSize)+'\n')
log.write('singletop Size:-'+str(stnhSize)+'\n')
log.write('WW,WZ Size:-----'+str(dnhSize)+'\n')
log.write('Drell-Yan Size:-'+str(znhSize)+'\n')
log.write('QCD Size:-------'+str(qhSize)+'\n')
log.write('Data Size:      '+str(datanhSize)+'\n')
log.write('--------------------\n')
log.write('QCD Scale:-'+str(qcdScale)+'\n')
log.write('--------------------\n')
log.write('Isolated Sizes\n')
log.write('--------------------\n')
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
log.write('---------------------------------------------\n')
log.write('---------------------------------------------\n')

log.close()

