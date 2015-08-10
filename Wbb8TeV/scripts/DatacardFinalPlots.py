#!/usr/bin/env python
'''
Makes shape and pre/post fit plots of .root files used in fitting
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
import histoRange as hr
import cmsPrelim as cpr
#import TheParameters as p
import scaleFactors as sf
 
# get parameters to run on
Signal = True
TT_m   = False
Rescale = True

Stack  = False
Shape  = True
errorBand = False
if Stack: kind = '_stack'
if Shape: kind = '_shape'
ratioRange = 0.3
rebin = 1
drawZ = False
drawW = False
lumi = 19742. #SV_3
types=['','_TTUp','_TTDown','_muonUp','_muonDown','_jetUp','_jetDown','_jetUCEUp','_jetUCEDown']

path = '../plots/Renamed_Datacard_'
if Signal: 
 leaf = 'J1_pt'
 name = path+'2j2525_2bt_'+leaf
if TT_m:
 leaf = 'mJ3J4'
 name = path+'4j2525_2bt_'+leaf

#canvas attributes
#canx = 800 # for one plot on page
#canx = 550 # for two plots on page with text
canx = 800 # for two plots on page just title
#canx = 500 # for three plots on page with text
#canx = 400 # for three plots on page with just title

cany = 900

#color scheme
d   = 1
q   = ROOT.EColor.kRed+1
z   = ROOT.EColor.kOrange-3
d   = ROOT.EColor.kYellow-3
tt  = ROOT.EColor.kGreen+1
ts  = ROOT.EColor.kGreen-5
ttw = ROOT.EColor.kGreen+3 
ttb = ROOT.EColor.kGreen-9
wl  = ROOT.EColor.kAzure+10
wc  = ROOT.EColor.kBlue+1
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

sf_Signal_QCD, sf_Signal_Drell, sf_Signal_T, sf_Signal_TTbar, sf_Signal_Tbar, sf_Signal_VV, sf_Signal_Wbb, sf_Signal_Wcc, sf_Signal_tW, sf_TTbar_QCD, sf_TTbar_T, sf_TTbar_TTbar, sf_TTbar_Tbar, sf_TTbar_Wbb, sf_TTbar_tW = sf.actor(Rescale)

sf_QCD    = 1.
sf_Wbb    = 1. 
sf_Tbar   = 1. 
sf_tW     = 1. 
sf_TTbar  = 1. 
sf_Drell  = 1. 
sf_Wcc    = 1. 
sf_T      = 1. 
sf_VV     = 1. 
sf_Wl     = 1.
sf_Wc     = 1.
if Signal and Rescale:
 sf_QCD    = sf_Signal_QCD
 sf_Wbb    = sf_Signal_Wbb   
 sf_Tbar   = sf_Signal_Tbar  
 sf_tW     = sf_Signal_tW    
 sf_TTbar  = sf_Signal_TTbar   
 sf_Drell  = sf_Signal_Drell
 sf_Wcc    = sf_Signal_Wcc   
 sf_T      = sf_Signal_T     
 sf_VV     = sf_Signal_VV    
if TT_m and Rescale:
 sf_QCD    = sf_TTbar_QCD
 sf_Wbb    = sf_TTbar_Wbb  
 sf_Tbar   = sf_TTbar_Tbar 
 sf_tW     = sf_TTbar_tW   
 sf_TTbar  = sf_TTbar_TTbar  
 sf_T      = sf_TTbar_T    

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

log = open(name+'.log','a')
log.write('\n\nOn Plotting SF QCD: '+str(sf_QCD)+'\n') 
log.write('On Plotting SF Drell: '+str(sf_Drell)+'\n')
log.write('On Plotting SF Top: '+str(sf_T)+'\n')
log.write('On Plotting SF tBar: '+str(sf_Tbar)+'\n')
log.write('On Plotting SF tW: '+str(sf_tW)+'\n')
log.write('On Plotting SF TTbar: '+str(sf_TTbar)+'\n')
log.write('On Plotting SF Wbb: '+str(sf_Wbb)+'\n')
log.write('On Plotting SF Wcc: '+str(sf_Wcc)+'\n')
log.write('On Plotting SF Diboson: '+str(sf_VV)+'\n')
log.write('Canvas X: '+str(canx)+'\n')
log.write('Canvas Y: '+str(cany)+'\n')
log.write('----------------------------------------\n')
log.write('----------------------------------------\n')
log.close()

theFile = TFile(name+'.root')

for xn in types:
 
 c = TCanvas('c','Canvas Named c',canx,cany)
 p1 = TPad('p1','p1',0,0.3,1,1)
 p1.SetBottomMargin(0.08)
 p1.Draw()
 p1.cd()
 p1.SetLogy(setLogY)
 
 dataih = theFile.Get('data_obs')
 dataih.Rebin(rebin)
 dataih.SetMarkerStyle(22)
 dataih.SetMarkerSize(1.2)
 dmax = dataih.GetMaximum()
 
 #### QCD
 qh = theFile.Get('QCD'+xn)
 qh.SetFillColor(q)
 qh.Rebin(rebin)
 qh.Scale(sf_QCD)
 qh.Draw()
 ### Drell
 zih = theFile.Get('Drell'+xn)
 zih.SetFillColor(z)
 zih.Rebin(rebin)
 zih.Scale(sf_Drell)
 zih.Draw()
 ### Diboson
 vvih = theFile.Get('VV'+xn)
 vvih.SetFillColor(d)
 vvih.Rebin(rebin)
 vvih.Scale(sf_VV)
 vvih.Draw()
 ### Single Top
 # t
 tih = theFile.Get('T'+xn)
 tih.SetFillColor(ts)
 tih.Rebin(rebin)
 tih.Scale(sf_T)
 tih.Draw()
 # tbar
 tbih = theFile.Get('Tbar'+xn)
 tbih.SetFillColor(tt)
 tbih.Rebin(rebin)
 tbih.Scale(sf_Tbar)
 tbih.Draw()
 # t tW
 t_twih = theFile.Get('tW'+xn)
 t_twih.SetFillColor(ttw)
 t_twih.Rebin(rebin)
 t_twih.Scale(sf_tW)
 t_twih.Draw()
 ### TTbar
 ttbih = theFile.Get('TTbar'+xn)
 ttbih.SetFillColor(ttb)
 ttbih.Rebin(rebin)
 ttbih.Scale(sf_TTbar)
 ttbih.Draw()
 
# bmin = ttbih.GetXaxis().FindBin(xmin)
# bmax = ttbih.GetXaxis().FindBin(xmax)
# print(ttbih.Integral(bmin,bmax))
# ### W + Light
# print("W + Light")
# wlih = theFile.Get('wlih'+xn)
# wlih.SetFillColor(wl)
# wlih.Rebin(rebin)
# wlih.Scale(sf_Wl)
# print(wlih.Integral(bmin,bmax))
# ### W + Charm
# print("W + Charm")
# wcih = theFile.Get('wcih'+xn)
# wcih.SetFillColor(wc)
# wcih.Rebin(rebin)
# wcih.Scale(sf_Wc)
# print(wcih.Integral(bmin,bmax))
 ### W + Charming
# print("W + Charming")
 wccih = theFile.Get('Wcc'+xn)
 wccih.SetFillColor(wcc)
 wccih.Rebin(rebin)
 wccih.Scale(sf_Wcc)
 #print(wccih.Integral(bmin,bmax))
 ### W + Beautiful
# print("W + Beautiful")
 wbbih = theFile.Get('Wbb'+xn)
 wbbih.SetFillColor(wbb)
 wbbih.Rebin(rebin)
 wbbih.Scale(sf_Wbb)
 #print(wbbih.Integral(bmin,bmax))
 
 if xunits is not None:
  xlabel = xtitle+' ['+xunits+']'
 else:
  xlabel = xtitle
 ylabel = 'Events/ %.0001f' %(float((xmax-xmin))/(qh.GetNbinsX()))
 title = xtitle+xn #+' Data v MC'

 if Stack:
  hs = THStack('hs','')
  hs.SetTitle('')
  hs.Add(qh)
  hs.Add(zih)
  hs.Add(vvih)
  hs.Add(tih)
  hs.Add(tbih)
  hs.Add(t_twih)
  hs.Add(ttbih)
  #hs.Add(wlih)
  #hs.Add(wcih)
  hs.Add(wccih)
  hs.Add(wbbih)

  hs.Draw()
  hs.GetXaxis().SetTitle(xlabel)
  hs.GetXaxis().SetRangeUser(xmin,xmax)
  hs.GetYaxis().SetTitleOffset(1.5)
  hs.GetYaxis().SetTitle(ylabel)
  hsmax = hs.GetMaximum()
  theMax = max(dmax,hsmax) 
  hs.SetMaximum(1.2*theMax)
 
 hh = TH1F('hh','hh',qh.GetNbinsX(),xmin,xmax)
 hh.Add(qh)
 hh.Add(zih)
 hh.Add(vvih)
 hh.Add(tih)
 hh.Add(tbih)
 hh.Add(t_twih)
 hh.Add(ttbih)
 hh.Add(wbbih)
 hh.Add(wccih)
# hh.Add(wcih)
# hh.Add(wlih)
 if errorBand:
  hherr = hh.Clone()
  hherr.SetName('hherr')
  hherr.SetFillColor(ROOT.EColor.kBlue-6)
  hherr.SetFillStyle(3001)
 
 leg=TLegend(0.68,0.2,0.9,0.8)
 leg.AddEntry(dataih,'data')
 leg.AddEntry(wbbih,'W(#mu#nu)+b#bar{b}','f')
 leg.AddEntry(wccih,'W(#mu#nu)+c#bar{c}','f')
 #leg.AddEntry(wcih,'W(#mu#nu)+c','f')
 #leg.AddEntry(wlih,'W(#mu#nu)+light','f')
 leg.AddEntry(ttbih,'t#bar{t}','f')
 leg.AddEntry(t_twih,'t_tW','f')
 leg.AddEntry(tbih,'#bar{t}','f')
 leg.AddEntry(tih,'t','f')
 leg.AddEntry(vvih,'WW,WZ,ZZ','f')
 leg.AddEntry(zih,'Drell-Yan','f')
 leg.AddEntry(qh,'QCD','f')
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 
 c.cd()
 p1.cd()

 if Stack: hs.Draw('hist')
 if Shape:
  linestyle = 1
  linewidth = 2
  qh.SetMaximum(1.2*dmax)
  qh.Draw('hist')
  zih.Draw('sames,hist')
  vvih.Draw('sames,hist')
  tih.Draw('sames,hist')
  tbih.Draw('sames,hist')
  t_twih.Draw('sames,hist')
  ttbih.Draw('sames,hist')
  wbbih.Draw('sames,hist')
  wccih.Draw('sames,hist')
  qh.SetLineStyle(linestyle)
  qh.SetLineWidth(linewidth)
  qh.SetLineColor(q)
  qh.SetFillStyle(0)
  zih.SetLineStyle(linestyle)
  zih.SetLineWidth(linewidth)
  zih.SetLineColor(z)
  zih.SetFillStyle(0)
  vvih.SetLineStyle(linestyle)
  vvih.SetLineWidth(linewidth)
  vvih.SetLineColor(d)
  vvih.SetFillStyle(0)
  tih.SetLineStyle(linestyle)
  tih.SetLineWidth(linewidth)
  tih.SetLineColor(ts)
  tih.SetFillStyle(0)
  tbih.SetLineStyle(linestyle)
  tbih.SetLineWidth(linewidth)
  tbih.SetLineColor(tt)
  tbih.SetFillStyle(0)
  t_twih.SetLineStyle(linestyle)
  t_twih.SetLineWidth(linewidth)
  t_twih.SetLineColor(ttw)
  t_twih.SetFillStyle(0)
  ttbih.SetLineStyle(linestyle)
  ttbih.SetLineWidth(linewidth)
  ttbih.SetLineColor(ttb)
  ttbih.SetFillStyle(0)
  wccih.SetLineStyle(linestyle)
  wccih.SetLineWidth(linewidth)
  wccih.SetLineColor(wcc)
  wccih.SetFillStyle(0)
  wbbih.SetLineStyle(linestyle)
  wbbih.SetLineWidth(linewidth)
  wbbih.SetLineColor(wbb)
  wbbih.SetFillStyle(0)
 if errorBand:
  hherr.Draw('sames,E2')
 #hs.GetXaxis().SetRangeUser(70,110)
 dataih.Draw('sames,E1')
 leg.Draw('sames')
 cpr.prelim_alt(lumi)
 tex.SetTextAlign(11)#left, bottom
 tex.DrawLatex(0.17,0.9,title)
 ## Draw Z Line
 if drawZ == True:
  zline = TLine(91.188,0,91.188,1.1*dmax)
  zline.SetLineWidth(2)
  zline.SetLineStyle(2)
  zline.Draw()
 ## Draw W Line
 if drawW == True:
  wline = TLine(80.385,0,80.385,1.1*dmax)
  wline.SetLineStyle(2)
  wline.SetLineWidth(2)
  wline.Draw()
 c.Update()
 ####
 c.cd()
 p2 = TPad('p2','p2',0,0,1,0.3)
 p2.SetTopMargin(0.1)
 p2.Draw()
 p2.cd()
 
 datar = TH1F('datar','datar',qh.GetNbinsX(),xmin,xmax)
 datar = dataih.Clone()
 datar.SetName('datar')
 if errorBand:
  hNOerr = TH1F('hNOerr','hNOerr',qh.GetNbinsX(),xmin,xmax)
  for j in range(steps+1):
   hNOerr.SetBinContent(j,hherr.GetBinContent(j))
   hNOerr.SetBinError(j,0)
  hrerr = hherr.Clone()
  hrerr.SetName("hrerr")
  hrerr.Divide(hNOerr)
 
 datar.GetYaxis().SetRangeUser(1.-ratioRange,1.+ratioRange) 
 datar.GetYaxis().SetLabelSize(0.11)
 datar.Divide(hh)
 datar.Draw('ep')
 if errorBand: hrerr.Draw('sames,E2')
 #datar.GetXaxis().SetRangeUser(70,110)
 
 l = TLine(xmin,1,xmax,1)
 l.SetLineStyle(3)
 l.Draw()
 c.Update()
 print('you just read '+leaf+xn)
 save2 = raw_input ('Press Enter to Continue (type save to save)\n')
 if save2 == 'save':
  c.Print(name+xn+kind+'.png')
  #c.Print(path+i+'_unscaled.png')
 print('')
 c.Close()
