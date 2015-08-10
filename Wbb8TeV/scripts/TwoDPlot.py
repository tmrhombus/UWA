#!/usr/bin/env python
'''
Makes nice plots with ratio from histograms made using makeHistos.py
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import TH2F
from ROOT import gROOT,gStyle
import histoRange as hr
import cmsPrelim as cpr
import TheParameters as p
 
# scale factors : sf_qcd = 1 + (data-allMC)/qcd in 0<Mt<20
#sf_qcd = 1.9191895562 # PU_fullIdTight
#sf_qcd = 2.19849549176 # PU_idTight 
#sf_qcd = 2.20315337368 # PU_idLoose
#sf_qcd = 2.09269599272 # Jet idLoose + PUID_fullIdLoose
sf_qcd = 2.14867279181 # temp for 18pb moreSV_two

sf_Signal_Wbb    = 1. 
sf_Signal_Wcc    = 1. 
sf_Signal_TTbar  = 1. 
sf_Signal_Tbar   = 1. 
sf_Signal_T      = 1. 
sf_Signal_tW     = 1. 
sf_Signal_Drell  = 1. 
sf_Signal_VV     = 1. 
sf_TTbar_T       = 1. 
sf_TTbar_TTbar   = 1. 
sf_TTbar_tW      = 1. 
sf_TTbar_Wbb     = 1. 
sf_TTbar_Tbar    = 1. 

#sf_Signal_Wbb    = 1.71730791317
#sf_Signal_Wcc    = 0.998058823529
#sf_Signal_TTbar  = 0.926577903683
#sf_Signal_Tbar   = 0.891945409429
#sf_Signal_T      = 0.861381156317
#sf_Signal_tW     = 0.860732919255
#sf_Signal_Drell  = 0.928019480519
#sf_Signal_VV     = 0.899869888476
#
#sf_TTbar_Wbb     = 1.79024054983
#sf_TTbar_Tbar    = 1.03396588486
#sf_TTbar_tW      = 0.99043902439
#sf_TTbar_TTbar   = 1.06769847317
#sf_TTbar_T       = 1.00208835341

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
#cany = 600

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
leafs = [
 ['(J1_mass_SSV+J2_mass_SSV)','(J1_nTracksSSV+J2_nTracksSSV)'],
 ['J1_mass_SSV','J1_nTracksSSV'],
 ['J2_mass_SSV','J2_nTracksSSV'],
 ['(J1_mass_SSV_alt+J2_mass_SSV_alt)','(J1_nTracksSSV+J2_nTracksSSV)'],
 ['J1_mass_SSV_alt','J1_nTracksSSV'],
 ['J2_mass_SSV_alt','J2_nTracksSSV']
]
extraName+='2D'

sf_Wbb    = 1. 
sf_Tbar   = 1. 
sf_tW     = 1. 
sf_TTbar  = 1. 
sf_Drell  = 1. 
sf_Wcc    = 1. 
sf_T      = 1. 
sf_VV     = 1. 
sf_wl     = 1.
sf_wc     = 1.
if Signal:
 sf_Wbb    = sf_Signal_Wbb   
 sf_Tbar   = sf_Signal_Tbar  
 sf_tW     = sf_Signal_tW    
 sf_TTbar  = sf_Signal_TTbar   
 sf_Drell  = sf_Signal_Drell
 sf_Wcc    = sf_Signal_Wcc   
 sf_T      = sf_Signal_T     
 sf_VV     = sf_Signal_VV    
if TT_m or TT_me:
 sf_Wbb    = sf_TTbar_Wbb  
 sf_Tbar   = sf_TTbar_Tbar 
 sf_tW     = sf_TTbar_tW   
 sf_TTbar  = sf_TTbar_TTbar  
 sf_T      = sf_TTbar_T    

for leafPair in leafs:

 leafA = leafPair[0]
 leafB = leafPair[1]
 stepsA, minA, maxA, titleA, unitsA, setLogYA = hr.ranger(leafA)
 stepsB, minB, maxB, titleB, unitsB, setLogYB = hr.ranger(leafB)

 if unitsA is not None:
  labelA = titleA+' ['+unitsA+']'
 else:
  labelA = titleA
 if unitsB is not None:
  labelB = titleB+' ['+unitsB+']'
 else:
  labelB = titleB
 titleA = titleA #+' Data v MC'
 titleB = titleB #+' Data v MC'
 
 name = []
 name.append(extraName+'_'+leafA+'_'+leafB)
 
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

  canMC = TCanvas('canMC','Canvas Named c',canx,cany)
  canData = TCanvas('canData','Canvas Named d',canx,cany)
  #p1 = TPad('p1','p1',0,0.3,1,1)
  #p1 = TPad('p1','p1',0,0.2,1,1)
  #p1.SetBottomMargin(0.08)
  #p1.Draw()
  #p1.cd()
  #p1.SetLogy(setLogYA)
  theFile = TFile(path+i+'.root')
  
  if drawData:
   dataih = theFile.Get('dataih')
   #dataih.Rebin(rebin)
   dataih.SetMarkerStyle(22)
   dataih.SetMarkerSize(1.2)
   dmax = dataih.GetMaximum()
  
  if drawQCD:
  #### QCD
   qh = theFile.Get('qh')
   qh.SetFillColor(q)
   #qh.Rebin(rebin)
   qh.Scale(sf_qcd)
   qh.Draw()
 #### Drell
  zih = theFile.Get('zih')
  zih.SetFillColor(z)
  #zih.Rebin(rebin)
  zih.Scale(sf_Drell)
  zih.Draw()
 #### Diboson
  wwih = theFile.Get('wwih')
  wwih.SetFillColor(d)
  #wwih.Rebin(rebin)
  wwih.Scale(sf_VV)
  wwih.Draw()
  ###
  wzih = theFile.Get('wzih')
  wzih.SetFillColor(d)
  #wzih.Rebin(rebin)
  wzih.Scale(sf_VV)
  wzih.Draw()
  ###
  zzih = theFile.Get('zzih')
  zzih.SetFillColor(d)
  #zzih.Rebin(rebin)
  zzih.Scale(sf_VV)
  zzih.Draw()
  ####
  dih = wwih.Clone()
  dih.SetName('dih')
  dih.Add(wzih)
  dih.Add(zzih)
  dih.Draw()
 #### Single Top
  # s
  t_sih = theFile.Get('t_sih')
  t_sih.SetFillColor(ts)
  #t_sih.Rebin(rebin)
  t_sih.Scale(sf_T)
  t_sih.Draw()
  ###
  tb_sih = theFile.Get('tb_sih')
  tb_sih.SetFillColor(ts)
  #tb_sih.Rebin(rebin)
  tb_sih.Scale(sf_T)
  tb_sih.Draw()
  #### 
  stsih = t_sih.Clone()
  stsih.SetName('stsih')
  stsih.Add(tb_sih)
  stsih.Draw()
  ###
  # t
  t_tih = theFile.Get('t_tih')
  t_tih.SetFillColor(tt)
  #t_tih.Rebin(rebin)
  t_tih.Scale(sf_T)
  t_tih.Draw()
  ###
  tb_tih = theFile.Get('tb_tih')
  tb_tih.SetFillColor(tt)
  #tb_tih.Rebin(rebin)
  tb_tih.Scale(sf_T)
  tb_tih.Draw()
  #### 
  sttih = t_tih.Clone()
  sttih.SetName('sttih')
  sttih.Add(tb_tih)
  sttih.Draw()
  ###
  # tw
  t_twih = theFile.Get('t_twih')
  t_twih.SetFillColor(ttw)
  #t_twih.Rebin(rebin)
  t_twih.Scale(sf_tW)
  t_twih.Draw()
  ###
  tb_twih = theFile.Get('tb_twih')
  tb_twih.SetFillColor(ttw)
  #tb_twih.Rebin(rebin)
  tb_twih.Scale(sf_tW)
  tb_twih.Draw()
  #### 
  sttwih = t_twih.Clone()
  sttwih.SetName('sttwih')
  sttwih.Add(tb_twih)
  sttwih.Draw()
 #### TTbar
  tt_semiih = theFile.Get('tt_semiih')
  tt_semiih.SetFillColor(ttb)
  #tt_semiih.Rebin(rebin)
  tt_semiih.Scale(sf_TTbar)
  tt_semiih.Draw()
  ###
  tt_fullih = theFile.Get('tt_fullih')
  tt_fullih.SetFillColor(ttb)
  #tt_fullih.Rebin(rebin)
  tt_fullih.Scale(sf_TTbar)
  tt_fullih.Draw()
  ###
  ttbih = tt_semiih.Clone()
  ttbih.SetName('ttbih')
  ttbih.Add(tt_fullih)
  ttbih.Draw()

  #bmin = ttbih.GetXaxis().FindBin(xmin)
  #bmax = ttbih.GetXaxis().FindBin(xmax)
  #print(ttbih.Integral(bmin,bmax))
 #### W + Light
  print("W + Light")
  wlnih = theFile.Get('wlnih')
  wlnih.SetFillColor(wl)
  #wlnih.Rebin(rebin)
  #print(wlnih.Integral(bmin,bmax))
  ###
  wl1ih = theFile.Get('wl1ih')
  wl1ih.SetFillColor(wl)
  #wl1ih.Rebin(rebin)
  #print(wl1ih.Integral(bmin,bmax))
  ###
  wl2ih = theFile.Get('wl2ih')
  wl2ih.SetFillColor(wl)
  #wl2ih.Rebin(rebin)
  #print(wl2ih.Integral(bmin,bmax))
  ###
  wl3ih = theFile.Get('wl3ih')
  wl3ih.SetFillColor(wl)
  #wl3ih.Rebin(rebin)
  #print(wl3ih.Integral(bmin,bmax))
  ###
  wl4ih = theFile.Get('wl4ih')
  wl4ih.SetFillColor(wl)
  #wl4ih.Rebin(rebin)
  #print(wl4ih.Integral(bmin,bmax))
  ### 
  wlih = wlnih.Clone()
  wlih.SetName('wlih')
  wlih.Add(wl1ih)
  wlih.Add(wl2ih)
  wlih.Add(wl3ih)
  wlih.Add(wl4ih)
  wlih.Scale(sf_wl)
  wlih.Draw()
  #print(wlih.Integral(bmin,bmax))
 #### W + Charm
  print("W + Charm")
  wcnih = theFile.Get('wcnih')
  wcnih.SetFillColor(wc)
  #wcnih.Rebin(rebin)
  #print(wcnih.Integral(bmin,bmax))
  ###
  wc1ih = theFile.Get('wc1ih')
  wc1ih.SetFillColor(wc)
  #wc1ih.Rebin(rebin)
  #print(wc1ih.Integral(bmin,bmax))
  ###
  wc2ih = theFile.Get('wc2ih')
  wc2ih.SetFillColor(wc)
  #wc2ih.Rebin(rebin)
  #print(wc2ih.Integral(bmin,bmax))
  ###
  wc3ih = theFile.Get('wc3ih')
  wc3ih.SetFillColor(wc)
  #wc3ih.Rebin(rebin)
  #print(wc3ih.Integral(bmin,bmax))
  ###
  wc4ih = theFile.Get('wc4ih')
  wc4ih.SetFillColor(wc)
  #wc4ih.Rebin(rebin)
  #print(wc4ih.Integral(bmin,bmax))
  ###
  wcih = wcnih.Clone()
  wcih.SetName('wcih')
  wcih.Add(wc1ih)
  wcih.Add(wc2ih)
  wcih.Add(wc3ih)
  wcih.Add(wc4ih)
  wcih.Scale(sf_wc)
  wcih.Draw()
  #print(wcih.Integral(bmin,bmax))
 #### W + Charming
  print("W + Charming")
  wccnih = theFile.Get('wccnih')
  wccnih.SetFillColor(wcc)
  #wccnih.Rebin(rebin)
  #print(wccnih.Integral(bmin,bmax))
  ###
  wcc1ih = theFile.Get('wcc1ih')
  wcc1ih.SetFillColor(wcc)
  #wcc1ih.Rebin(rebin)
  #print(wcc1ih.Integral(bmin,bmax))
  ###
  wcc2ih = theFile.Get('wcc2ih')
  wcc2ih.SetFillColor(wcc)
  #wcc2ih.Rebin(rebin)
  #print(wcc2ih.Integral(bmin,bmax))
  ###
  wcc3ih = theFile.Get('wcc3ih')
  wcc3ih.SetFillColor(wcc)
  #wcc3ih.Rebin(rebin)
  #print(wcc3ih.Integral(bmin,bmax))
  ###
  wcc4ih = theFile.Get('wcc4ih')
  wcc4ih.SetFillColor(wcc)
  #wcc4ih.Rebin(rebin)
  #print(wcc4ih.Integral(bmin,bmax))
  ###
  wccih = wccnih.Clone()
  wccih.SetName('wccih')
  wccih.Add(wcc1ih)
  wccih.Add(wcc2ih)
  wccih.Add(wcc3ih)
  wccih.Add(wcc4ih)
  wccih.Scale(sf_Wcc)
  wccih.Draw()
  #print(wccih.Integral(bmin,bmax))
 #### W + Beautiful
  print("W + Beautiful")
  wbbnih = theFile.Get('wbbnih')
  wbbnih.SetFillColor(wbb)
  #wbbnih.Rebin(rebin)
  #print(wbbnih.Integral(bmin,bmax))
  ###
  wbb1ih = theFile.Get('wbb1ih')
  wbb1ih.SetFillColor(wbb)
  #wbb1ih.Rebin(rebin)
  #print(wbb1ih.Integral(bmin,bmax))
  ###
  wbb2ih = theFile.Get('wbb2ih')
  wbb2ih.SetFillColor(wbb)
  #wbb2ih.Rebin(rebin)
  #print(wbb2ih.Integral(bmin,bmax))
  ###
  wbb3ih = theFile.Get('wbb3ih')
  wbb3ih.SetFillColor(wbb)
  #wbb3ih.Rebin(rebin)
  #print(wbb3ih.Integral(bmin,bmax))
  ###
  wbb4ih = theFile.Get('wbb4ih')
  wbb4ih.SetFillColor(wbb)
  #wbb4ih.Rebin(rebin)
  #print(wbb4ih.Integral(bmin,bmax))
  ###  
  wbbih = wbbnih.Clone()
  wbbih.SetName('wbbih')
  wbbih.Add(wbb1ih)
  wbbih.Add(wbb2ih)
  wbbih.Add(wbb3ih)
  wbbih.Add(wbb4ih)
  wbbih.Scale(sf_Wbb)
  wbbih.Draw()
  #print(wbbih.Integral(bmin,bmax))
 
  hh = TH2F('hh','hh',stepsA,minA,maxA,stepsB,minB,maxB)
  if drawQCD:
   hh.Add(qh)
  hh.Add(zih)
  hh.Add(dih)
  hh.Add(sttih)
  hh.Add(stsih)
  hh.Add(sttwih)
  hh.Add(ttbih)
  hh.Add(wbbih)
  hh.Add(wccih)
  hh.Add(wcih)
  hh.Add(wlih)
 
  canData.cd()
  dataih.Draw('colz')
  dataih.SetTitle('')
  dataih.GetXaxis().SetTitle(labelA)
  dataih.GetYaxis().SetTitle(labelB)
  cpr.prelim_alt(lumi)
  tex.SetTextAlign(11)#left, bottom
  tex.SetTextSize(0.03)
  tex.DrawLatex(0.1,0.9,titleA+ ' vs '+titleB)
  canData.Update()

  save2 = raw_input ('Data: Press Enter to Continue (type save to save)\n')
  if save2 == 'save':
   canData.Print(path+i+'_MC.png')
  print('')
  canData.Close()

  canMC.cd()
  hh.Draw('colz')
  hh.SetTitle('')
  hh.GetXaxis().SetTitle(labelA)
  hh.GetYaxis().SetTitle(labelB)
  cpr.prelim_alt(lumi)
  tex.SetTextAlign(11)#left, bottom
  tex.SetTextSize(0.03)
  tex.DrawLatex(0.1,0.9,titleA+ ' vs '+titleB)
  canMC.Update()

  save3 = raw_input ('MC: Press Enter to Continue (type save to save)\n')
  if save3 == 'save':
   canMC.Print(path+i+'_Data.png')
  print('')
  canMC.Close()
