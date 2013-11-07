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
import TheParameters as p
import scaleFactors as sf
 
# qcd scale factor is applied in DatacardHisto.py
#sf_qcd = 1.9191895562 # PU_fullIdTight
sf_qcd = 2.19849549176/2.05901169 # PU_idTight
#sf_qcd = 2.20315337368 # PU_idLoose

sf_Signal_Wbb,sf_Signal_Wcc,sf_Signal_TTbar,sf_Signal_Tbar,sf_Signal_T,sf_Signal_tW,sf_Signal_Drell,sf_Signal_VV,sf_TTbar_Wbb,sf_TTbar_Tbar,sf_TTbar_tW,sf_TTbar_TTbar,sf_TTbar_T = sf.actor()

ratioRange = 0.3
rebin = 1
errorBand = False
#canvas attributes
#canx = 800 # for one plot on page
#canx = 550 # for two plots on page with text
canx = 800 # for two plots on page just title
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

# get parameters to run on
lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,eventTreeLocation,extraCut = p.arams() 

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
if Signal:
 print("youre at line 82")
 sf_Wbb    = sf_Signal_Wbb   
 sf_Tbar   = sf_Signal_Tbar  
 sf_tW     = sf_Signal_tW    
 sf_TTbar  = sf_Signal_TTbar   
 sf_Drell  = sf_Signal_Drell
 sf_Wcc    = sf_Signal_Wcc   
 sf_T      = sf_Signal_T     
 sf_VV     = sf_Signal_VV    
if TT_m or TT_me:
 print("youre at line 92")
 sf_Wbb    = sf_TTbar_Wbb  
 sf_Tbar   = sf_TTbar_Tbar 
 sf_tW     = sf_TTbar_tW   
 sf_TTbar  = sf_TTbar_TTbar  
 sf_T      = sf_TTbar_T    

for leaf in leafs:

 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
 
 if xunits is not None:
  xlabel = xtitle+' ['+xunits+']'
 else:
  xlabel = xtitle
 ylabel = 'Events/ %.0001f' %(float((xmax-xmin)*rebin)/(steps))
 title = xtitle #+' Data v MC'
 
 name = []
 name.append(extraName+'_'+leaf)
 
 for i in name:

  log = open(path+i+'.log','a')
  log.write('\n\nOn Plotting SF QCD: '+str(sf_qcd)+'\n') 
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

  if eventTreeLocation == 'muNuEventTree/eventTree'        : xn = 'No'  
  if eventTreeLocation == 'muNuEventTreeMuonUp/eventTree'  : xn = 'Up'  
  if eventTreeLocation == 'muNuEventTreeMuonDown/eventTree': xn = 'Dn'  
  if eventTreeLocation == 'muNuEventTreeJetUp/eventTree'   : xn = 'JUp'  
  if eventTreeLocation == 'muNuEventTreeJetDown/eventTree' : xn = 'JDn'  
  if eventTreeLocation == 'muNuEventTreeUCEUp/eventTree'   : xn = 'UUp'
  if eventTreeLocation == 'muNuEventTreeUCEDown/eventTree' : xn = 'UDn'

  c = TCanvas('c','Canvas Named c',canx,cany)
  p1 = TPad('p1','p1',0,0.2,1,1)
  p1.SetBottomMargin(0.08)
  p1.Draw()
  p1.cd()
  p1.SetLogy(setLogY)
  theFile = TFile(path+i+'.root')
  
  if drawData:
   dataih = theFile.Get('dataih')
   dataih.Rebin(rebin)
   dataih.SetMarkerStyle(22)
   dataih.SetMarkerSize(1.2)
   dmax = dataih.GetMaximum()
  
  if drawQCD:
  #### QCD
   qh = theFile.Get('qh'+xn)
   qh.SetFillColor(q)
   qh.Rebin(rebin)
   qh.Scale(sf_qcd)
   qh.Draw()
 #### Drell
  zih = theFile.Get('zih'+xn)
  zih.SetFillColor(z)
  zih.Rebin(rebin)
  zih.Scale(sf_Drell)
  zih.Draw()
 #### Diboson
  vvih = theFile.Get('vvih'+xn)
  vvih.SetFillColor(d)
  vvih.Rebin(rebin)
  vvih.Scale(sf_VV)
  vvih.Draw()
 #### Single Top
  # t
  tih = theFile.Get('tih'+xn)
  tih.SetFillColor(ts)
  tih.Rebin(rebin)
  tih.Scale(sf_T)
  tih.Draw()
  # tbar
  tbih = theFile.Get('tbih'+xn)
  tbih.SetFillColor(tt)
  tbih.Rebin(rebin)
  tbih.Scale(sf_Tbar)
  tbih.Draw()
  # t tW
  t_twih = theFile.Get('t_twih'+xn)
  t_twih.SetFillColor(ttw)
  t_twih.Rebin(rebin)
  t_twih.Scale(sf_tW)
  t_twih.Draw()
 #### TTbar
  ttbih = theFile.Get('ttbih'+xn)
  ttbih.SetFillColor(ttb)
  ttbih.Rebin(rebin)
  ttbih.Scale(sf_TTbar)
  ttbih.Draw()

  bmin = ttbih.GetXaxis().FindBin(xmin)
  bmax = ttbih.GetXaxis().FindBin(xmax)
  print(ttbih.Integral(bmin,bmax))
 #### W + Light
  print("W + Light")
  wlih = theFile.Get('wlih'+xn)
  wlih.SetFillColor(wl)
  wlih.Rebin(rebin)
  wlih.Scale(sf_Wl)
  print(wlih.Integral(bmin,bmax))
 #### W + Charm
  print("W + Charm")
  wcih = theFile.Get('wcih'+xn)
  wcih.SetFillColor(wc)
  wcih.Rebin(rebin)
  wcih.Scale(sf_Wc)
  print(wcih.Integral(bmin,bmax))
 #### W + Charming
  print("W + Charming")
  wccih = theFile.Get('wccih'+xn)
  wccih.SetFillColor(wcc)
  wccih.Rebin(rebin)
  wccih.Scale(sf_Wcc)
  print(wccih.Integral(bmin,bmax))
 #### W + Beautiful
  print("W + Beautiful")
  wbbih = theFile.Get('wbbih'+xn)
  wbbih.SetFillColor(wbb)
  wbbih.Rebin(rebin)
  wbbih.Scale(sf_Wbb)
  print(wbbih.Integral(bmin,bmax))
 
  hs = THStack('hs','')
  hs.SetTitle('')
  if drawQCD:
   hs.Add(qh)
  hs.Add(zih)
  hs.Add(vvih)
  hs.Add(tih)
  hs.Add(tbih)
  hs.Add(t_twih)
  hs.Add(ttbih)
  hs.Add(wbbih)
  hs.Add(wccih)
  hs.Add(wcih)
  hs.Add(wlih)

  hh = TH1F('hh','hh',steps,xmin,xmax)
  if drawQCD:
   hh.Add(qh)
  hh.Add(zih)
  hh.Add(vvih)
  hh.Add(tih)
  hh.Add(tbih)
  hh.Add(t_twih)
  hh.Add(ttbih)
  hh.Add(wbbih)
  hh.Add(wccih)
  hh.Add(wcih)
  hh.Add(wlih)
  if errorBand:
   hherr = hh.Clone()
   hherr.SetName('hherr')
   hherr.SetFillColor(ROOT.EColor.kBlue-6)
   hherr.SetFillStyle(3001)
 
  hs.Draw()
  hs.GetXaxis().SetTitle(xlabel)
  hs.GetXaxis().SetRangeUser(xmin,xmax)
#  if leaf=="Mt" and not Legacy:
#   hs.GetXaxis().SetRangeUser(50,140)
  hs.GetYaxis().SetTitleOffset(1.5)
  hs.GetYaxis().SetTitle(ylabel)
  hsmax = hs.GetMaximum()
  
  leg=TLegend(0.68,0.2,0.9,0.8)
  if drawData:
   leg.AddEntry(dataih,'data')
 
  leg.AddEntry(wlih,'W(#mu#nu)+light','f')
  leg.AddEntry(wcih,'W(#mu#nu)+c','f')
  leg.AddEntry(wccih,'W(#mu#nu)+c#bar{c}','f')
  leg.AddEntry(wbbih,'W(#mu#nu)+b#bar{b}','f')
  leg.AddEntry(ttbih,'t#bar{t}','f')
  leg.AddEntry(t_twih,'t_tW','f')
  leg.AddEntry(tbih,'#bar{t}','f')
  leg.AddEntry(tih,'t','f')
  leg.AddEntry(vvih,'WW,WZ,ZZ','f')
  leg.AddEntry(zih,'Drell-Yan','f')
  if drawQCD:
   leg.AddEntry(qh,'QCD','f')
  leg.SetFillColor(0)
  leg.SetBorderSize(0)
  
  theMax = hsmax 
  if drawData:
   theMax = max(dmax,hsmax) 
  hs.SetMaximum(1.2*theMax)
  c.cd()
  p1.cd()
  hs.Draw('hist')
  if errorBand:
   hherr.Draw('sames,E2')
  #hs.GetXaxis().SetRangeUser(70,110)
  if drawData:
   dataih.Draw('sames,E1')
  leg.Draw('sames')
  cpr.prelim_alt(lumi)
  tex.SetTextAlign(11)#left, bottom
  tex.DrawLatex(0.17,0.9,title)
  ## Draw Z Line
  if drawZ == True:
   zline = TLine(91.188,0,91.188,1.1*theMax)
   zline.SetLineWidth(2)
   zline.SetLineStyle(2)
   zline.Draw()
  ## Draw W Line
  if drawW == True:
   wline = TLine(80.385,0,80.385,1.1*theMax)
   wline.SetLineStyle(2)
   wline.SetLineWidth(2)
   wline.Draw()
  c.Update()
 #####
  c.cd()
  p2 = TPad('p2','p2',0,0,1,0.2)
  p2.SetTopMargin(0.1)
  p2.Draw()
  p2.cd()
 
  datar = TH1F('datar','datar',steps,xmin,xmax)
  if drawData:
   datar = dataih.Clone()
  else:
   datar = hh.Clone()
  datar.SetName('datar')
  if errorBand:
   hNOerr = TH1F('hNOerr','hNOerr',steps,xmin,xmax)
   for j in range(steps+1):
    hNOerr.SetBinContent(j,hherr.GetBinContent(j))
    hNOerr.SetBinError(j,0)
   hrerr = hherr.Clone()
   hrerr.SetName("hrerr")
   hrerr.Divide(hNOerr)

  if leaf =="Mt" and not noMT:
   datar.GetXaxis().SetRangeUser(50,140)
  datar.GetYaxis().SetRangeUser(1.-ratioRange,1.+ratioRange) 
  datar.GetYaxis().SetLabelSize(0.11)
  datar.Divide(hh)
  datar.Draw('ep')
  if errorBand: hrerr.Draw('sames,E2')
  #datar.GetXaxis().SetRangeUser(70,110)
  
  if leaf=="Mt" and not noMT:
   l = TLine(50,1,140,1)
   l.SetLineStyle(3)
   l.Draw()
  else:
   l = TLine(xmin,1,xmax,1)
   l.SetLineStyle(3)
   l.Draw()
  c.Update()
  print('you just read '+leaf)
  save2 = raw_input ('Press Enter to Continue (type save to save)\n')
  if save2 == 'save':
   c.Print(path+i+'.png')
   #c.Print(path+i+'_unscaled.png')
  print('')
  c.Close()
