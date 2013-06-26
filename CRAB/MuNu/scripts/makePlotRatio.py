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

lumi = 13498. #luminosity 
path = '../plots/'
tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')

jNr = 2
bNr = 0
 
# scale factors : sf_qcd = 1 + (data-allMC)/qcd in 0<Mt<20
sf_qcd = 1+(486395.0-(70228.7539062+3820.58770752+261.598018646+3045.22140503+3501.15155029+40844.8603516+30151.6518555+3103.32769775+65838.4931641+52626.2958984+39184.6586914+41183.0043945))/(41183.0043945) # Mt > 0. && 0.98 eff correction
# sf_qcd   = 1+(486395.0-(71661.6357422+3898.57788086+266.936691284+3107.36975098+3572.60089111+41678.2138672+30766.9594727+3166.66146851+67181.9228516+53699.9023438+39984.6865234+41038.4926758))/(41038.4926758) # Mt > 0. no eff correction

sf_drell = 1.# 3503.71 / 3.02386400000000000e+07
sf_st    = 1.# 22.2    / 9.91118000000000000e+05
sf_ttbar = 1.# 225.    / 6.88773100000000000e+06
sf_wjets = 1.# 37509.  / 5.31329400000000000e+07
sf_vv    = 1.
 
#canvas attributes
canx = 700
cany = 900

#color scheme
d = 1
q = ROOT.EColor.kRed+1
z = ROOT.EColor.kOrange-3
d = ROOT.EColor.kYellow-3
tt = ROOT.EColor.kGreen+1
ts = ROOT.EColor.kGreen-5
ttw = ROOT.EColor.kGreen+3 
ttb = ROOT.EColor.kGreen-9
wl = ROOT.EColor.kAzure+10
wc = ROOT.EColor.kBlue+1
wcc = ROOT.EColor.kAzure+2
wbb = 51#ROOT.EColor.kCyan
 
#leafs = ['LHEProduct']
#leafs = ['muonPt','MET','vertices','muonPhi','WPt','DiMuonMass','mjj','mJ3J4','ptJJ','met','MtCal','muonEta','ht','highestJetEta','secondJetEta','thirdJetEta','highestJetPhi','secondJetPhi','thirdJetPhi','highestJetPt','secondJetPt','thirdJetPt']
#leafs=['Mt']
#leafs=['vertices']
#leafs = ['muonPt','MET','vertices','muonPhi','WPt','DiMuonMass','mJ3J4','ptJJ','met','MtCal','muonEta','ht','highestJetEta','secondJetEta','thirdJetEta','highestJetPhi','secondJetPhi','thirdJetPhi','highestJetPt','secondJetPt','thirdJetPt']
leafs = ['muonPt','MET','J1CSVbtag','J2CSVbtag','vertices','muonPhi','J1DR','J2DR']

for leaf in leafs:

 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
 
 rebin = 1
 xlabel = xtitle+' ['+xunits+']'
 ylabel = 'Events/ %.001f' %(float((xmax-xmin))/(steps*rebin))
 title = xtitle #+' Data v MC'
 
 name = []
 name.append(leaf+str(jNr)+'j'+str(bNr)+'b')
 
 for i in name:
  c = TCanvas('c','Canvas Named c',canx,cany)
  p1 = TPad('p1','p1',0,0.3,1,1)
  p1.SetBottomMargin(0.08)
  p1.Draw()
  p1.cd()
  p1.SetLogy(setLogY)
  theFile = TFile(path+i+'.root')
  
  dataih = theFile.Get('dataih')
  dataih.Rebin(rebin)
  dataih.Sumw2()
  dataih.SetMarkerStyle(22)
  dataih.SetMarkerSize(1.2)
  dmax = dataih.GetMaximum()
  
  qh = theFile.Get('qh')
  qh.SetFillColor(q)
  qh.Rebin(rebin)
  qh.Scale(sf_qcd)
  qh.Draw()
  #raw_input("qcd")
  ###
  zih = theFile.Get('zih')
  zih.SetFillColor(z)
  zih.Rebin(rebin)
  zih.Scale(sf_drell)
  zih.Draw()
  #raw_input("drell")
  ###
  dih = theFile.Get('dih')
  dih.SetFillColor(d)
  dih.Rebin(rebin)
  dih.Scale(sf_vv)
  dih.Draw()
  #raw_input("diboson)
  ###
  stsih = theFile.Get('stsih')
  stsih.SetFillColor(ts)
  stsih.Rebin(rebin)
  stsih.Scale(sf_st)
  stsih.Draw()
  #raw_input("single top t")
  ###
  sttih = theFile.Get('sttih')
  sttih.SetFillColor(tt)
  sttih.Rebin(rebin)
  sttih.Scale(sf_st)
  sttih.Draw()
  #raw_input("single top s")
  ###
  sttwih = theFile.Get('sttwih')
  sttwih.SetFillColor(ttw)
  sttwih.Rebin(rebin)
  sttwih.Scale(sf_st)
  sttwih.Draw()
  #raw_input("single top tw")
  ###
  ttbih = theFile.Get('ttbih')
  ttbih.SetFillColor(ttb)
  ttbih.Rebin(rebin)
  ttbih.Scale(sf_ttbar)
  ttbih.Draw()
  #raw_input("ttbar")

  bmin = ttbih.GetXaxis().FindBin(xmin)
  bmax = ttbih.GetXaxis().FindBin(xmax)
 #### W + Light
  print("W + Light")
  wlnih = theFile.Get('wlnih')
  wlnih.SetFillColor(wl)
  wlnih.Rebin(rebin)
  print(wlnih.Integral(bmin,bmax))
  ###
  wl1ih = theFile.Get('wl1ih')
  wl1ih.SetFillColor(wl)
  wl1ih.Rebin(rebin)
  print(wl1ih.Integral(bmin,bmax))
  ###
  wl2ih = theFile.Get('wl2ih')
  wl2ih.SetFillColor(wl)
  wl2ih.Rebin(rebin)
  print(wl2ih.Integral(bmin,bmax))
  ###
  wl3ih = theFile.Get('wl3ih')
  wl3ih.SetFillColor(wl)
  wl3ih.Rebin(rebin)
  print(wl3ih.Integral(bmin,bmax))
  ###
  wl4ih = theFile.Get('wl4ih')
  wl4ih.SetFillColor(wl)
  wl4ih.Rebin(rebin)
  print(wl4ih.Integral(bmin,bmax))
  ### 
  wlih = wlnih.Clone()
  wlih.SetName('wlih')
  wlih.Add(wl1ih)
  wlih.Add(wl2ih)
  wlih.Add(wl3ih)
  wlih.Add(wl4ih)
  wlih.Draw()
  print(wlih.Integral(bmin,bmax))
 #### W + Charm
  print("W + Charm")
  wcnih = theFile.Get('wcnih')
  wcnih.SetFillColor(wc)
  wcnih.Rebin(rebin)
  print(wcnih.Integral(bmin,bmax))
  ###
  wc1ih = theFile.Get('wc1ih')
  wc1ih.SetFillColor(wc)
  wc1ih.Rebin(rebin)
  print(wc1ih.Integral(bmin,bmax))
  ###
  wc2ih = theFile.Get('wc2ih')
  wc2ih.SetFillColor(wc)
  wc2ih.Rebin(rebin)
  print(wc2ih.Integral(bmin,bmax))
  ###
  wc3ih = theFile.Get('wc3ih')
  wc3ih.SetFillColor(wc)
  wc3ih.Rebin(rebin)
  print(wc3ih.Integral(bmin,bmax))
  ###
  wc4ih = theFile.Get('wc4ih')
  wc4ih.SetFillColor(wc)
  wc4ih.Rebin(rebin)
  print(wc4ih.Integral(bmin,bmax))
  ###
  wcih = wcnih.Clone()
  wcih.SetName('wcih')
  wcih.Add(wc1ih)
  wcih.Add(wc2ih)
  wcih.Add(wc3ih)
  wcih.Add(wc4ih)
  wcih.Draw()
  print(wcih.Integral(bmin,bmax))
 #### W + Charming
  print("W + Charming")
  wccnih = theFile.Get('wccnih')
  wccnih.SetFillColor(wcc)
  wccnih.Rebin(rebin)
  print(wccnih.Integral(bmin,bmax))
  ###
  wcc1ih = theFile.Get('wcc1ih')
  wcc1ih.SetFillColor(wcc)
  wcc1ih.Rebin(rebin)
  print(wcc1ih.Integral(bmin,bmax))
  ###
  wcc2ih = theFile.Get('wcc2ih')
  wcc2ih.SetFillColor(wcc)
  wcc2ih.Rebin(rebin)
  print(wcc2ih.Integral(bmin,bmax))
  ###
  wcc3ih = theFile.Get('wcc3ih')
  wcc3ih.SetFillColor(wcc)
  wcc3ih.Rebin(rebin)
  print(wcc3ih.Integral(bmin,bmax))
  ###
  wcc4ih = theFile.Get('wcc4ih')
  wcc4ih.SetFillColor(wcc)
  wcc4ih.Rebin(rebin)
  print(wcc4ih.Integral(bmin,bmax))
  ###
  wccih = wccnih.Clone()
  wccih.SetName('wccih')
  wccih.Add(wcc1ih)
  wccih.Add(wcc2ih)
  wccih.Add(wcc3ih)
  wccih.Add(wcc4ih)
  wccih.Draw()
  print(wccih.Integral(bmin,bmax))
 #### W + Beautiful
  print("W + Beautiful")
  wbbnih = theFile.Get('wbbnih')
  wbbnih.SetFillColor(wbb)
  wbbnih.Rebin(rebin)
  print(wbbnih.Integral(bmin,bmax))
  ###
  wbb1ih = theFile.Get('wbb1ih')
  wbb1ih.SetFillColor(wbb)
  wbb1ih.Rebin(rebin)
  print(wbb1ih.Integral(bmin,bmax))
  ###
  wbb2ih = theFile.Get('wbb2ih')
  wbb2ih.SetFillColor(wbb)
  wbb2ih.Rebin(rebin)
  print(wbb2ih.Integral(bmin,bmax))
  ###
  wbb3ih = theFile.Get('wbb3ih')
  wbb3ih.SetFillColor(wbb)
  wbb3ih.Rebin(rebin)
  print(wbb3ih.Integral(bmin,bmax))
  ###
  wbb4ih = theFile.Get('wbb4ih')
  wbb4ih.SetFillColor(wbb)
  wbb4ih.Rebin(rebin)
  print(wbb4ih.Integral(bmin,bmax))
  ###  
  wbbih = wbbnih.Clone()
  wbbih.SetName('wbbih')
  wbbih.Add(wbb1ih)
  wbbih.Add(wbb2ih)
  wbbih.Add(wbb3ih)
  wbbih.Add(wbb4ih)
  wbbih.Draw()
  print(wbbih.Integral(bmin,bmax))
 
  hs = THStack('hs','')
  hs.SetTitle('')
  hs.Add(qh)
  hs.Add(zih)
  hs.Add(dih)
  hs.Add(sttih)
  hs.Add(stsih)
  hs.Add(sttwih)
  hs.Add(ttbih)
  hs.Add(wbbih)
  hs.Add(wccih)
  hs.Add(wcih)
  hs.Add(wlih)
 
  hs.Draw()
  hs.GetXaxis().SetTitle(xlabel)
 # hs.GetXaxis().SetRangeUser(50,140)
  hs.GetYaxis().SetTitleOffset(1.5)
  hs.GetYaxis().SetTitle(ylabel)
  hsmax = hs.GetMaximum()
  
  leg=TLegend(0.68,0.2,0.9,0.8)
  leg.AddEntry(dataih,'data')
 
  leg.AddEntry(wlih,'W(#mu#nu)+light','f')
  leg.AddEntry(wcih,'W(#mu#nu)+c','f')
  leg.AddEntry(wccih,'W(#mu#nu)+cc','f')
  leg.AddEntry(wbbih,'W(#mu#nu)+bb','f')
  leg.AddEntry(ttbih,'t#bar{t}','f')
  leg.AddEntry(sttwih,'t_tW','f')
  leg.AddEntry(stsih,'t_s','f')
  leg.AddEntry(sttih,'t_t','f')
  leg.AddEntry(dih,'WW,WZ,ZZ','f')
  leg.AddEntry(zih,'Drell-Yan','f')
  leg.AddEntry(qh,'QCD','f')
  leg.SetFillColor(0)
  leg.SetBorderSize(0)
 
  if dmax>hsmax:
   hs.SetMaximum(1.2*dmax)
  else:
   hs.SetMaximum(1.2*hsmax)
  c.cd()
  p1.cd()
  hs.Draw()
  dataih.Draw('sames')
  leg.Draw('sames')
  cpr.prelim(lumi)
  tex.SetTextAlign(11)#left, bottom
  tex.DrawLatex(0.17,0.9,title)
 
  c.Update()
 #####
  c.cd()
  p2 = TPad('p2','p2',0,0,1,0.3)
  p2.SetTopMargin(0.1)
  p2.Draw()
  p2.cd()
 
  datar = TH1F('datar','datar',steps,xmin,xmax)
  hh = TH1F('hh','hh',steps,xmin,xmax)
  hh.Rebin(rebin)
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
 #
  datar = dataih.Clone()
  datar.SetName('datar')
 # datar.GetXaxis().SetRangeUser(50,140)
  datar.GetYaxis().SetRangeUser(0.8,1.2) 
  datar.GetYaxis().SetLabelSize(0.11)
  datar.Divide(hh)
  datar.Draw('ep')
  
  if 1 > 2:
   print('something is wrong')
  else:
   l = TLine(xmin,1,xmax,1)
 #  l = TLine(50,1,140,1)
   l.SetLineStyle(3)
   l.Draw()
  c.Update()
  save2 = raw_input ('Press Enter to Continue (type save to save)\n')
  if save2 == 'save':
   c.Print(path+i+'.png')
#  c.Print(path+i+'.png')
  c.Close()
