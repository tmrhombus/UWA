#!/usr/bin/env python
'''
Makes cut effect plot from .root file made by EffectCutsHisto.py
Author: T.M.Perry UW
'''
print('importing')
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
import histoRange as hr
import cmsPrelim as cpr
print('all modules imported')
#canvas attributes
canx = 800 # for one plot on page
#canx = 550 # for two plots on page with text
#canx = 600 # for two plots on page just title
#canx = 500 # for three plots on page with text
#canx = 400 # for three plots on page with just title

cany = 900

#color scheme
d = 1

q =   ROOT.EColor.kRed+1
z =   ROOT.EColor.kOrange-3
d =   ROOT.EColor.kYellow-3
tt =  ROOT.EColor.kGreen+1
ts =  ROOT.EColor.kGreen-5
ttw = ROOT.EColor.kGreen+3 
ttb = ROOT.EColor.kGreen-9
wl =  ROOT.EColor.kAzure+10
wc =  ROOT.EColor.kBlue+1
wcc = ROOT.EColor.kAzure+2
wbb = 51#ROOT.EColor.kCyan

#7 TeV color scheme
#q =   ROOT.EColor.kGreen-3   
#z =   ROOT.EColor.kRed+2     
#d =   ROOT.EColor.kRed+3     
#tt =  ROOT.EColor.kOrange+7  
#ts =  ROOT.EColor.kOrange+6  
#ttw = ROOT.EColor.kOrange+5  
#ttb = ROOT.EColor.kOrange-2  
#wl =  ROOT.EColor.kAzure+1   
#wc =  ROOT.EColor.kMagenta-4 
#wcc = ROOT.EColor.kViolet-6  
#wbb = ROOT.EColor.kBlue-10   

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')

drawQCD = True
drawData = True
saveAsk = True

path = '../plots/EffectCuts'
extraName = '_tp2'
leaf = 'muonCharge'
steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
setLogY=True
nrplots = 4

xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events'
title = xtitle #+' Data v MC'
yrange = 0.2

filename = path+extraName+'_'+leaf+'.root'
theFile = TFile(filename)

can = TCanvas('can','Canvas Named can',canx,cany)
pad1 = TPad('pad1','pad1',0,0.3,1,1)
pad1.SetLogy(setLogY)
pad1.SetBottomMargin(0.08)
pad1.Draw()
pad1.cd()

print("getting histograms")

datac = theFile.Get('datac')
datac.SetTitle('')
datac.SetMarkerStyle(22)
qc      = theFile.Get('qc')
zc      = theFile.Get('zc')
wwc     = theFile.Get('wwc')
wzc     = theFile.Get('wzc')
zzc     = theFile.Get('zzc')
t_tc    = theFile.Get('t_tc')
tb_tc   = theFile.Get('tb_tc')
t_sc    = theFile.Get('t_sc')
tb_sc   = theFile.Get('tb_sc')
t_twc   = theFile.Get('t_twc')
tb_twc  = theFile.Get('tb_twc')
ttbc    = theFile.Get('ttbc')
wbbc    = theFile.Get('wbbc')
wccc    = theFile.Get('wccc')
wcc     = theFile.Get('wcc')
wlc     = theFile.Get('wlc')
print("all histograms loaded")

dc = wwc.Clone()
dc.SetName('dc')
dc.Add(wzc)
dc.Add(zzc)

sttc = t_tc.Clone()
sttc.SetName('sttc')
sttc.Add(tb_tc)

stsc = t_sc.Clone()
stsc.SetName('stsc')
stsc.Add(tb_sc)

sttwc = t_twc.Clone()
sttwc.SetName('sttwc')
sttwc.Add(tb_twc)

hc = THStack('hc','')
hc.SetTitle('')
if drawQCD:
 hc.Add(qc)
hc.Add(zc)
hc.Add(dc)
hc.Add(sttc)
hc.Add(stsc)
hc.Add(sttwc)
hc.Add(ttbc)
hc.Add(wbbc)
hc.Add(wccc)
hc.Add(wcc)
hc.Add(wlc)

hc.Draw('hist')
hc.GetXaxis().SetTitle(xlabel)
hc.GetXaxis().SetRangeUser(0,nrplots)
hc.GetYaxis().SetTitleOffset(1.5)
hc.GetYaxis().SetTitle(ylabel)
hsmax = hc.GetMaximum()

leg=TLegend(0.68,0.2,0.9,0.8)
if drawData:
 leg.AddEntry(datac,'data')
leg.AddEntry(wlc,'W(#mu#nu)+light','f')
leg.AddEntry(wcc,'W(#mu#nu)+c','f')
leg.AddEntry(wccc,'W(#mu#nu)+c#bar{c}','f')
leg.AddEntry(wbbc,'W(#mu#nu)+b#bar{b}','f')
leg.AddEntry(ttbc,'t#bar{t}','f')
leg.AddEntry(sttwc,'t_tW','f')
leg.AddEntry(stsc,'t_s','f')
leg.AddEntry(sttc,'t_t','f')
leg.AddEntry(dc,'WW,WZ,ZZ','f')
leg.AddEntry(zc,'Drell-Yan','f')
if drawQCD:
 leg.AddEntry(qc,'QCD','f')
leg.SetFillColor(0)
leg.SetBorderSize(0)

theMax = hsmax 

if drawData:
 theMax = max(1,hsmax) 
hc.SetMaximum(1.2*theMax)
can.cd()
pad1.cd()
hc.Draw("hist")
if drawData:
 datac.Draw('sames, E1')
leg.Draw('sames')
cpr.prelim_alt(19429.)
tex.SetTextAlign(11)#left, bottom
tex.DrawLatex(0.17,0.9,title)

can.cd()
pad2 = TPad('pad2','pad2',0,0,1,0.3)
pad2.SetTopMargin(0.1)
pad2.Draw()
pad2.cd()

if drawQCD:
 hhc = qc.Clone()
 hhc.SetName('hhc')
 hhc.Add(zc)
else:
 hhc = zc.Clone()
 hhc.SetName('hhc')
hhc.Add(dc)
hhc.Add(sttc)
hhc.Add(stsc)
hhc.Add(sttwc)
hhc.Add(ttbc)
hhc.Add(wbbc)
hhc.Add(wccc)
hhc.Add(wcc)
hhc.Add(wlc)
hhc.Sumw2()

if drawData:
 datarc = datac.Clone()
else:
 datarc = hhc.Clone()
datarc.SetName('datarc')
datarc.GetYaxis().SetRangeUser(1.-yrange,1.+yrange) 
datarc.GetYaxis().SetLabelSize(0.11)
datarc.Divide(hhc)
datarc.Draw('ep')

l = TLine(0,1,nrplots,1)
l.SetLineStyle(3)
l.Draw()
can.Update()
if saveAsk:
 save = raw_input ('Press Enter to Continue (type save to save)\n')
 if save == 'save':
  can.Print(path+extraName+'_'+leaf+'_Effects.png')
else:
  can.Print(path+extraName+'_'+leaf+'_Effects.png')
