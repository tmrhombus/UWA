#!/usr/bin/env python
'''
Plots a leaf with progressing cuts and a graph to show the cuts effects.
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad, TLine
from ROOT import TLatex
from ROOT import gROOT,gStyle

import aHisto as h #function to make histograms
import EffectCutsCuts as c #function to make vector of cut strings
import histoRange as hr
import cmsPrelim as cpr

leaf = 'muonCharge'
I=-1
F=-1
cuts,Wl,Wc,Wcc,Wbb,Iso,NonIso,weight = c.utList()
drawQCD = True
drawData = True
saveAsk = False

path='../plots/EffectCuts'
extraName = '_newT'
#nr < = 8
nrplots =4
steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
canx = 800
cany = 900
xlabel = xtitle+' ['+xunits+']'
ylabel = 'Events/ %.0001f' %(float((xmax-xmin))/(steps))
title = xtitle #+' Data v MC'

cut1 = 'SkimControl'
cut2 = 'noFJ'
cut3 = 'twoJetsE'
cut4 = 'twoTB'
cut5 = ''
cut6 = ''
cut7 = ''

CutList = []
CutList.append(cut1)
CutList.append(cut2)
CutList.append(cut3)
CutList.append(cut4)

data_filename  = '../data/v5/wMuNuData.root'
t_t_filename   = '../data/v1/T_t.root'
t_s_filename   = '../data/v0/T_s.root'
t_tw_filename  = '../data/v0/T_tW.root'
tb_t_filename  = '../data/v0/Tbar_t.root'
tb_s_filename  = '../data/v0/Tbar_s.root'
tb_tw_filename = '../data/v0/Tbar_tW.root'
ttb_filename   = '../data/v0/TTbar.root'
ww_filename    = '../data/v0/WW.root'
wz_filename    = '../data/v0/WZ.root'
zz_filename    = '../data/v0/ZZ.root'
wn_filename    = '../data/v0/WJets.root'
w1_filename    = '../data/v0/W1Jet.root'
w2_filename    = '../data/v0/W2Jet.root'
w3_filename    = '../data/v0/W3Jet.root'
w4_filename    = '../data/v0/W4Jet.root'
z_filename     = '../data/v0/Drell.root'

data_file  = TFile( data_filename )
t_t_file   = TFile( t_t_filename  )
t_s_file   = TFile( t_s_filename  )
t_tw_file  = TFile( t_tw_filename )
tb_t_file  = TFile( tb_t_filename )
tb_s_file  = TFile( tb_s_filename )
tb_tw_file = TFile( tb_tw_filename)
ttb_file   = TFile( ttb_filename  )
ww_file    = TFile( ww_filename   )
wz_file    = TFile( wz_filename   )
zz_file    = TFile( zz_filename   )
wn_file    = TFile( wn_filename   )
w1_file    = TFile( w1_filename   )
w2_file    = TFile( w2_filename   )
w3_file    = TFile( w3_filename   )
w4_file    = TFile( w4_filename   )
z_file     = TFile( z_filename    )

eventTreeLocation = 'muNuEventTree/eventTree'

data_tree  =  data_file.Get(eventTreeLocation) 
t_t_tree   =  t_t_file.Get(eventTreeLocation)
t_s_tree   =  t_s_file.Get(eventTreeLocation)
t_tw_tree  =  t_tw_file.Get(eventTreeLocation)
tb_t_tree  =  tb_t_file.Get(eventTreeLocation)
tb_s_tree  =  tb_s_file.Get(eventTreeLocation)
tb_tw_tree =  tb_tw_file.Get(eventTreeLocation)
ttb_tree   =  ttb_file.Get(eventTreeLocation)
ww_tree    =  ww_file.Get(eventTreeLocation)
wz_tree    =  wz_file.Get(eventTreeLocation)
zz_tree    =  zz_file.Get(eventTreeLocation)
wn_tree    =  wn_file.Get(eventTreeLocation)
w1_tree    =  w1_file.Get(eventTreeLocation)
w2_tree    =  w2_file.Get(eventTreeLocation)
w3_tree    =  w3_file.Get(eventTreeLocation)
w4_tree    =  w4_file.Get(eventTreeLocation)
z_tree     =  z_file.Get(eventTreeLocation)

qcdRescale = False
tRescale = False
ttRescale = False
vRescale = False
dRescale = False
sf_qcd = 1.
sf_drell = 1. # 3503.71 / 3.02386400000000000e+07
sf_st = 1. # 22.2    / 9.91118000000000000e+05
sf_ttbar = 1. # 225.    / 6.88773100000000000e+06
sf_wjets = 1. # 37509.  / 5.31329400000000000e+07
sf_vv = 1.

qColor =   ROOT.EColor.kRed+1
zColor =   ROOT.EColor.kOrange-3
dColor =   ROOT.EColor.kYellow-3
ttColor =  ROOT.EColor.kGreen+1
tsColor =  ROOT.EColor.kGreen-5
ttwColor = ROOT.EColor.kGreen+3 
ttbColor = ROOT.EColor.kGreen-9
wlColor =  ROOT.EColor.kAzure+10
wcColor =  ROOT.EColor.kBlue+1
wccColor = ROOT.EColor.kAzure+2
wbbColor = 51#ROOT.EColor.kCyan

#7 TeV color scheme
#qColor =   ROOT.EColor.kGreen-3   
#zColor =   ROOT.EColor.kRed+2     
#dColor =   ROOT.EColor.kRed+3     
#ttColor =  ROOT.EColor.kOrange+7  
#tsColor =  ROOT.EColor.kOrange+6  
#ttwColor = ROOT.EColor.kOrange+5  
#ttbColor = ROOT.EColor.kOrange-2  
#wlColor =  ROOT.EColor.kAzure+1   
#wcColor =  ROOT.EColor.kMagenta-4 
#wccColor = ROOT.EColor.kViolet-6  
#wbbColor = ROOT.EColor.kBlue-10   

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')

outFile=gROOT.FindObject(path+extraName+'_'+leaf+'.root')
if outFile : outFile.Close()
outFile = TFile(path+extraName+'_'+leaf+'.root','RECREATE','Demo ROOT file')

log = open(path+extraName+'_'+leaf+'.log','w')

datac = TH1F('datac','datac',nrplots,0,nrplots)
qc = TH1F('qc','qc',nrplots,0,nrplots)
t_tc = TH1F('t_tc','t_tc',nrplots,0,nrplots) 
tb_tc = TH1F('tb_tc','tb_tc',nrplots,0,nrplots) 
t_sc = TH1F('t_sc','t_sc',nrplots,0,nrplots) 
tb_sc = TH1F('tb_sc','tb_sc',nrplots,0,nrplots) 
t_twc = TH1F('t_twc','t_twc',nrplots,0,nrplots) 
tb_twc = TH1F('tb_twc','tb_twc',nrplots,0,nrplots) 
ttbc = TH1F('ttbc','ttbc',nrplots,0,nrplots) 
wwc = TH1F('wwc','wwc',nrplots,0,nrplots) 
wzc = TH1F('wzc','wzc',nrplots,0,nrplots) 
zzc = TH1F('zzc','zzc',nrplots,0,nrplots) 
wlc = TH1F('wac','wlc',nrplots,0,nrplots) 
wcc = TH1F('wc','wc',nrplots,0,nrplots) 
wccc = TH1F('wcc','wcc',nrplots,0,nrplots) 
wbbc = TH1F('wbc','wbc',nrplots,0,nrplots) 
zc = TH1F('zc','zc',nrplots,0,nrplots) 
hc = TH1F('hc','hc',nrplots,0,nrplots)

print('----------------------------')
print('      --'+leaf+'--')
print(extraName)
print('----------------------------')

theCut = ''
for i in range(nrplots):

 theCut += '&&'+cuts[CutList[i]] 

 CutsMCn = '('+weight+'*('+NonIso+theCut+'))'
 CutsDatan = '('+NonIso+theCut+')'
 CutsMCi = '('+weight+'*('+Iso+theCut+'))'
 CutsDatai = '('+Iso+theCut+')'
 CutsMCiwl = '('+weight+'*('+Wl+'&&'+Iso+theCut+'))'
 CutsMCiwbb = '('+weight+'*('+Wbb+'&&'+Iso+theCut+'))'
 CutsMCiwcc =  '('+weight+'*('+Wcc+'&&'+Iso+theCut+'))'
 CutsMCiwc =  '('+weight+'*('+Wc+'&&'+Iso+theCut+'))'

 if drawQCD:
  ###
  datanh,datanhSize,datanhSizePart,datanhEntries = h.gram(data_tree,leaf,xmin,xmax,steps,CutsDatan,I,F)
  print('For QCD Shape')
  print('data nonIso')
  datanh.SetName('datanh')
  print('  '+str(datanhSize))
  print('  '+str(datanhSizePart))
 ####  Drell
  print('  z nonIso')
  znh,znhSize,znhSizePart,znhEntries = h.gram(z_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  znh.SetName('znh')
  znh.Scale(sf_drell)
  print('    '+str(znhSize))
  print('    '+str(znhSizePart))
 ####  Dibosons
  print('  ww nonIso')
  wwnh,wwnhSize,wwnhSizePart,wwnhEntries = h.gram(ww_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  wwnh.SetName('wwnh')
  wwnh.Scale(sf_vv)
  print('    '+str(wwnhSize))
  print('    '+str(wwnhSizePart))
  ###
  print('  wz nonIso')
  wznh,wznhSize,wznhSizePart,wznhEntries = h.gram(wz_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  wznh.SetName('wznh')
  wznh.Scale(sf_vv)
  print('    '+str(wznhSize))
  print('    '+str(wznhSizePart))
  ###
  print('  ww nonIso')
  zznh,zznhSize,zznhSizePart,zznhEntries = h.gram(zz_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  zznh.SetName('zznh')
  zznh.Scale(sf_vv)
  print('    '+str(zznhSize))
  print('    '+str(zznhSizePart))
 ####  Single Top
  print('  t t nonIso')
  t_tnh,t_tnhSize,t_tnhSizePart,t_tnhEntries = h.gram(t_t_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  t_tnh.SetName('t_tnh')
  t_tnh.Scale(sf_st)
  print('    '+str(t_tnhSize))
  print('    '+str(t_tnhSizePart))
  ###
  print('  tb t nonIso')
  tb_tnh,tb_tnhSize,tb_tnhSizePart,tb_tnhEntries = h.gram(tb_t_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  tb_tnh.SetName('tb_tnh')
  tb_tnh.Scale(sf_st)
  print('    '+str(tb_tnhSize))
  print('    '+str(tb_tnhSizePart))
  ###
  print('  t s nonIso')
  t_snh,t_snhSize,t_snhSizePart,t_snhEntries = h.gram(t_s_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  t_snh.SetName('t_snh')
  t_snh.Scale(sf_st)
  print('    '+str(t_snhSize))
  print('    '+str(t_snhSizePart))
  ###
  print('  tb s nonIso')
  tb_snh,tb_snhSize,tb_snhSizePart,tb_snhEntries = h.gram(tb_s_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  tb_snh.SetName('tb_snh')
  tb_snh.Scale(sf_st)
  print('    '+str(tb_snhSize))
  print('    '+str(tb_snhSizePart))
  ###
  print('  t tw nonIso')
  t_twnh,t_twnhSize,t_twnhSizePart,t_twnhEntries = h.gram(t_tw_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  t_twnh.SetName('t_twnh')
  t_twnh.Scale(sf_st)
  print('    '+str(t_twnhSize))
  print('    '+str(t_twnhSizePart))
  ###
  print('  tb tw nonIso')
  tb_twnh,tb_twnhSize,tb_twnhSizePart,tb_twnhEntries = h.gram(tb_tw_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  tb_twnh.SetName('tb_twnh')
  tb_twnh.Scale(sf_st)
  print('    '+str(tb_twnhSize))
  print('    '+str(tb_twnhSizePart))
 ####  TTbar
  print('  ttbar nonIso')
  ttbnh,ttbnhSize,ttbnhSizePart,ttbnhEntries = h.gram(ttb_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  ttbnh.SetName('ttbnh')
  ttbnh.Scale(sf_ttbar)
  print('    '+str(ttbnhSize))
  print('    '+str(ttbnhSizePart))
 ####  W
  print('  wn nonIso')
  wnnh,wnnhSize,wnnhSizePart,wnhEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  wnnh.SetName('wnnh')
  wnnh.Scale(sf_wjets)
  print('    '+str(wnnhSize))
  print('    '+str(wnnhSizePart))
  print('  w1 nonIso')
  ###
  w1nh,w1nhSize,w1nhSizePart,w1nhEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  w1nh.SetName('w1nh')
  w1nh.Scale(sf_wjets)
  print('    '+str(w1nhSize))
  print('    '+str(w1nhSizePart))
  print('  w2 nonIso')
  ###
  w2nh,w2nhSize,w2nhSizePart,w2nhEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  w2nh.SetName('w2nh')
  w2nh.Scale(sf_wjets)
  print('    '+str(w2nhSize))
  print('    '+str(w2nhSizePart))
  print('  w3 nonIso')
  ###
  w3nh,w3nhSize,w3nhSizePart,w3nhEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  w3nh.SetName('w3nh')
  w3nh.Scale(sf_wjets)
  print('    '+str(w3nhSize))
  print('    '+str(w3nhSizePart))
  print('  w4 nonIso')
  ###
  w4nh,w4nhSize,w4nhSizePart,w4nhEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCn,I,F)
  w4nh.SetName('w4nh')
  w4nh.Scale(sf_wjets)
  print('    '+str(w4nhSize))
  print('    '+str(w4nhSizePart))
 #
  print('subtracting non-iso MC from Data ')
  qh = datanh.Clone()
  qh.SetName('qh')
  qh.Add(znh,-1)    #Drell
  qh.Add(t_tnh,-1)  #Single Top
  qh.Add(tb_tnh,-1)
  qh.Add(t_snh,-1)
  qh.Add(tb_snh,-1)
  qh.Add(t_twnh,-1)
  qh.Add(tb_twnh,-1)
  qh.Add(wwnh,-1)   #Diboson
  qh.Add(wznh,-1)
  qh.Add(zznh,-1)
  qh.Add(ttbnh,-1)  #TTbar
  qh.Add(wnnh,-1)   #W
  qh.Add(w1nh,-1)
  qh.Add(w2nh,-1)
  qh.Add(w3nh,-1)
  qh.Add(w4nh,-1)

  print('qcd')
  qh.SetTitle('')
  qh.SetFillColor(qColor)
  bminq = qh.GetXaxis().FindBin(xmin)
  bmaxq = qh.GetXaxis().FindBin(xmax)
  bIq = qh.GetXaxis().FindBin(I)
  bFq = qh.GetXaxis().FindBin(F)
  qhSizePart = qh.Integral(bIq,bFq)
  qh.Scale(sf_qcd)
  qhSize = qh.Integral(bminq,bmaxq)
  qhEntries = qh.GetEntries()
  print('  '+str(qhSize))
  print('  '+str(qhSizePart))
  
  qc.Fill(i,qhSize)
  qc.SetFillColor(qColor)
 ####################################
 if drawData:
  ### Data
  print('')
  print('Isolated Variables Now')
  print("data Iso") 
  dataih,dataihSize,dataihSizePart,dataihEntries = h.gram(data_tree,leaf,xmin,xmax,steps,CutsDatai,I,F)
  dataih.SetName('dataih')
  print('  '+str(dataihSize))
  print('  '+str(dataihSizePart))
  dimax = dataih.GetMaximum()
  datac.Fill(i,dataihSize)
#### Drell
 print("z Iso")
 zih,zihSize,zihSizePart,zihEntries = h.gram(z_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zih.SetName('zih')
 zih.Scale(sf_drell)
 zih.SetFillColor(zColor)
 print('  '+str(zihSize))
 print('  '+str(zihSizePart))
 zc.Fill(i,zihSize)
 zc.SetFillColor(zColor)
#### Diboson
 print("ww Iso")
 wwih,wwihSize,wwihSizePart,wwihEntries = h.gram(ww_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 wwih.SetName('wwih')
 wwih.Scale(sf_vv)
 wwih.SetFillColor(dColor)
 print('  '+str(wwihSize))
 print('  '+str(wwihSizePart))
 wwc.Fill(i,wwihSize)
 wwc.SetFillColor(dColor)
 ###
 print("wz Iso")
 wzih,wzihSize,wzihSizePart,wzihEntries = h.gram(wz_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 wzih.SetName('wzih')
 wzih.Scale(sf_vv)
 wzih.SetFillColor(dColor)
 print('  '+str(wzihSize))
 print('  '+str(wzihSizePart))
 wzc.Fill(i,wzihSize)
 wzc.SetFillColor(dColor)
 ###
 print("zz Iso")
 zzih,zzihSize,zzihSizePart,zzihEntries = h.gram(zz_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zzih.SetName('zzih')
 zzih.Scale(sf_vv)
 zzih.SetFillColor(dColor)
 print('  '+str(zzihSize))
 print('  '+str(zzihSizePart))
 zzc.Fill(i,zzihSize)
 zzc.SetFillColor(dColor)
#### Single Top
 print('t t Iso')
 t_tih,t_tihSize,t_tihSizePart,t_tihEntries = h.gram(t_t_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_tih.SetName('t_tih')
 t_tih.Scale(sf_st)
 t_tih.SetFillColor(ttColor)
 print('  '+str(t_tihSize))
 print('  '+str(t_tihSizePart))
 t_tc.Fill(i,t_tihSize)
 t_tc.SetFillColor(ttColor)
 ###
 print('tb t Iso')
 tb_tih,tb_tihSize,tb_tihSizePart,tb_tihEntries = h.gram(tb_t_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_tih.SetName('tb_tih')
 tb_tih.Scale(sf_st)
 tb_tih.SetFillColor(ttColor)
 print('  '+str(tb_tihSize))
 print('  '+str(tb_tihSizePart))
 tb_tc.Fill(i,tb_tihSize)
 tb_tc.SetFillColor(ttColor)
 ###
 print('t s Iso')
 t_sih,t_sihSize,t_sihSizePart,t_sihEntries = h.gram(t_s_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_sih.SetName('t_sih')
 t_sih.Scale(sf_st)
 t_sih.SetFillColor(tsColor)
 print('  '+str(t_sihSize))
 print('  '+str(t_sihSizePart))
 t_sc.Fill(i,t_sihSize)
 t_sc.SetFillColor(tsColor)
 ###
 print('tb s Iso')
 tb_sih,tb_sihSize,tb_sihSizePart,tb_sihEntries = h.gram(tb_s_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_sih.SetName('tb_sih')
 tb_sih.Scale(sf_st)
 tb_sih.SetFillColor(tsColor)
 print('  '+str(tb_sihSize))
 print('  '+str(tb_sihSizePart))
 tb_sc.Fill(i,tb_sihSize)
 tb_sc.SetFillColor(tsColor)
 ###
 print('t tw Iso')
 t_twih,t_twihSize,t_twihSizePart,t_twihEntries = h.gram(t_tw_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 t_twih.SetName('t_twih')
 t_twih.Scale(sf_st)
 t_twih.SetFillColor(ttwColor)
 print('  '+str(t_twihSize))
 print('  '+str(t_twihSizePart))
 t_twc.Fill(i,t_twihSize)
 t_twc.SetFillColor(ttwColor)
 ###
 print('tb tw Iso')
 tb_twih,tb_twihSize,tb_twihSizePart,tb_twihEntries = h.gram(tb_tw_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 tb_twih.SetName('tb_twih')
 tb_twih.Scale(sf_st)
 tb_twih.SetFillColor(ttwColor)
 print('  '+str(tb_twihSize))
 print('  '+str(tb_twihSizePart))
 tb_twc.Fill(i,tb_twihSize)
 tb_twc.SetFillColor(ttwColor)
#### TTbar
 print('ttb Iso')
 ttbih,ttbihSize,ttbihSizePart,ttbihEntries = h.gram(ttb_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 ttbih.Draw("hist")
 ttbih.SetName('ttbih')
 ttbih.Scale(sf_ttbar)
 ttbih.SetFillColor(ttbColor)
 print('  '+str(ttbihSize))
 print('  '+str(ttbihSizePart))
 ttbc.Fill(i,ttbihSize)
 ttbc.SetFillColor(ttbColor)
#### W + Jets
 print('wl n Iso')
 wlnih,wlnihSize,wlnihSizePart,wlnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wlnih.SetName('wlnih')
 wlnih.Scale(sf_wjets)
 print('  '+str(wlnihSize))
 print('  '+str(wlnihSizePart))
 ####
 print('wc n Iso')
 wcnih,wcnihSize,wcnihSizePart,wcnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wcnih.SetName('wcnih')
 wcnih.Scale(sf_wjets)
 print('  '+str(wcnihSize))
 print('  '+str(wcnihSizePart))
 ####
 print('wcc n Iso')
 wccnih,wccnihSize,wccnihSizePart,wccnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wccnih.SetName('wccnih')
 wccnih.Scale(sf_wjets)
 print('  '+str(wccnihSize))
 print('  '+str(wccnihSizePart))
 ####
 print('wbb n Iso')
 wbbnih,wbbnihSize,wbbnihSizePart,wbbnihEntries = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbbnih.SetName('wbbnih')
 wbbnih.Scale(sf_wjets)
 print('  '+str(wbbnihSize))
 print('  '+str(wbbnihSizePart))
#####
 print('wl 1 Iso')
 wl1ih,wl1ihSize,wl1ihSizePart,wl1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl1ih.SetName('wl1ih')
 wl1ih.Scale(sf_wjets)
 print('  '+str(wl1ihSize))
 print('  '+str(wl1ihSizePart))
 ####
 print('wc 1 Iso')
 wc1ih,wc1ihSize,wc1ihSizePart,wc1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc1ih.SetName('wc1ih')
 wc1ih.Scale(sf_wjets)
 print('  '+str(wc1ihSize))
 print('  '+str(wc1ihSizePart))
 ####
 print('wcc 1 Iso')
 wcc1ih,wcc1ihSize,wcc1ihSizePart,wcc1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc1ih.SetName('wcc1ih')
 wcc1ih.Scale(sf_wjets)
 print('  '+str(wcc1ihSize))
 print('  '+str(wcc1ihSizePart))
 ####
 print('wbb 1 Iso')
 wbb1ih,wbb1ihSize,wbb1ihSizePart,wbb1ihEntries = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb1ih.SetName('wbb1ih')
 wbb1ih.Scale(sf_wjets)
 print('  '+str(wbb1ihSize))
 print('  '+str(wbb1ihSizePart))
#####
 print('wl 2 Iso')
 wl2ih,wl2ihSize,wl2ihSizePart,wl2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl2ih.SetName('wl2ih')
 wl2ih.Scale(sf_wjets)
 print('  '+str(wl2ihSize))
 print('  '+str(wl2ihSizePart))
 ####
 print('wc 2 Iso')
 wc2ih,wc2ihSize,wc2ihSizePart,wc2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc2ih.SetName('wc2ih')
 wc2ih.Scale(sf_wjets)
 print('  '+str(wc2ihSize))
 print('  '+str(wc2ihSizePart))
 ####
 print('wcc 2 Iso')
 wcc2ih,wcc2ihSize,wcc2ihSizePart,wcc2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc2ih.SetName('wcc2ih')
 wcc2ih.Scale(sf_wjets)
 print('  '+str(wcc2ihSize))
 print('  '+str(wcc2ihSizePart))
 ####
 print('wbb 2 Iso')
 wbb2ih,wbb2ihSize,wbb2ihSizePart,wbb2ihEntries = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb2ih.SetName('wbb2ih')
 wbb2ih.Scale(sf_wjets)
 print('  '+str(wbb2ihSize))
 print('  '+str(wbb2ihSizePart))
#####
 print('wl 3 Iso')
 wl3ih,wl3ihSize,wl3ihSizePart,wl3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl3ih.SetName('wl3ih')
 wl3ih.Scale(sf_wjets)
 print('  '+str(wl3ihSize))
 print('  '+str(wl3ihSizePart))
 ####
 print('wc 3 Iso')
 wc3ih,wc3ihSize,wc3ihSizePart,wc3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc3ih.SetName('wc3ih')
 wc3ih.Scale(sf_wjets)
 print('  '+str(wc3ihSize))
 print('  '+str(wc3ihSizePart))
 ####
 print('wcc 3 Iso')
 wcc3ih,wcc3ihSize,wcc3ihSizePart,wcc3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc3ih.SetName('wcc3ih')
 wcc3ih.Scale(sf_wjets)
 print('  '+str(wcc3ihSize))
 print('  '+str(wcc3ihSizePart))
 ####
 print('wbb 3 Iso')
 wbb3ih,wbb3ihSize,wbb3ihSizePart,wbb3ihEntries = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb3ih.SetName('wbb3ih')
 wbb3ih.Scale(sf_wjets)
 print('  '+str(wbb3ihSize))
 print('  '+str(wbb3ihSizePart))
#####
 print('wl 4 Iso')
 wl4ih,wl4ihSize,wl4ihSizePart,wl4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl4ih.SetName('wl4ih')
 wl4ih.Scale(sf_wjets)
 print('  '+str(wl4ihSize))
 print('  '+str(wl4ihSizePart))
 ####
 print('wc 4 Iso')
 wc4ih,wc4ihSize,wc4ihSizePart,wc4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc4ih.SetName('wc4ih')
 wc4ih.Scale(sf_wjets)
 print('  '+str(wc4ihSize))
 print('  '+str(wc4ihSizePart))
 ####
 print('wcc 4 Iso')
 wcc4ih,wcc4ihSize,wcc4ihSizePart,wcc4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc4ih.SetName('wcc4ih')
 wcc4ih.Scale(sf_wjets)
 print('  '+str(wcc4ihSize))
 print('  '+str(wcc4ihSizePart))
 ####
 print('wbb 4 Iso')
 wbb4ih,wbb4ihSize,wbb4ihSizePart,wbb4ihEntries = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb4ih.SetName('wbb4ih')
 wbb4ih.Scale(sf_wjets)
 print('  '+str(wbb4ihSize))
 print('  '+str(wbb4ihSizePart))

 wlc.Fill(i,wlnihSize+wl1ihSize+wl2ihSize+wl3ihSize+wl4ihSize) 
 wlc.SetFillColor(wlColor)
 wcc.Fill(i,wcnihSize+wc1ihSize+wc2ihSize+wc3ihSize+wc4ihSize) 
 wcc.SetFillColor(wcColor)
 wccc.Fill(i,wccnihSize+wcc1ihSize+wcc2ihSize+wcc3ihSize+wcc4ihSize) 
 wccc.SetFillColor(wccColor)
 wbbc.Fill(i,wbbnihSize+wbb1ihSize+wbb2ihSize+wbb3ihSize+wbb4ihSize) 
 wbbc.SetFillColor(wbbColor)

 ### 
 wlih = wlnih.Clone()
 wlih.SetName('wlih')
 wlih.Add(wl1ih)
 wlih.Add(wl2ih)
 wlih.Add(wl3ih)
 wlih.Add(wl4ih)
 wlih.SetFillColor(wlColor)
 wlih.Draw()
 ###
 wcih = wcnih.Clone()
 wcih.SetName('wcih')
 wcih.Add(wc1ih)
 wcih.Add(wc2ih)
 wcih.Add(wc3ih)
 wcih.Add(wc4ih)
 wcih.SetFillColor(wcColor)
 wcih.Draw()
 ###
 wccih = wccnih.Clone()
 wccih.SetName('wccih')
 wccih.Add(wcc1ih)
 wccih.Add(wcc2ih)
 wccih.Add(wcc3ih)
 wccih.Add(wcc4ih)
 wccih.SetFillColor(wccColor)
 wccih.Draw()
 ###  
 wbbih = wbbnih.Clone()
 wbbih.SetName('wbbih')
 wbbih.Add(wbb1ih)
 wbbih.Add(wbb2ih)
 wbbih.Add(wbb3ih)
 wbbih.Add(wbb4ih)
 wbbih.SetFillColor(wbbColor)
 wbbih.Draw()
 ####
 dih = wwih.Clone()
 dih.SetName('dih')
 dih.Add(wzih)
 dih.Add(zzih)
 dih.Draw()
 #### 
 stsih = t_sih.Clone()
 stsih.SetName('stsih')
 stsih.Add(tb_sih)
 stsih.Draw()
 #### 
 sttih = t_tih.Clone()
 sttih.SetName('sttih')
 sttih.Add(tb_tih)
 sttih.Draw()
 #### 
 sttwih = t_twih.Clone()
 sttwih.SetName('sttwih')
 sttwih.Add(tb_twih)
 sttwih.Draw()

 c = TCanvas('c','Canvas Named c',canx,cany)
 p1 = TPad('p1','p1',0,0.3,1,1)
 p1.SetBottomMargin(0.08)
 p1.Draw()
 p1.cd()

 hs = THStack('hs','')
 hs.SetTitle('')
 if drawQCD:
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
 hs.GetXaxis().SetRangeUser(xmin,xmax)
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
 leg.AddEntry(sttwih,'t_tW','f')
 leg.AddEntry(stsih,'t_s','f')
 leg.AddEntry(sttih,'t_t','f')
 leg.AddEntry(dih,'WW,WZ,ZZ','f')
 leg.AddEntry(zih,'Drell-Yan','f')
 if drawQCD:
  leg.AddEntry(qh,'QCD','f')
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 
 theMax = hsmax 
 if drawData:
  theMax = max(dimax,hsmax) 
 hs.SetMaximum(1.2*theMax)
 c.cd()
 p1.cd()
 hs.Draw("hist")
 if drawData:
  dataih.Draw('sames')
 leg.Draw('sames')
 cpr.prelim_alt(19429.)
 tex.SetTextAlign(11)#left, bottom
 tex.DrawLatex(0.17,0.9,title)

 c.cd()
 p2 = TPad('p2','p2',0,0,1,0.3)
 p2.SetTopMargin(0.1)
 p2.Draw()
 p2.cd()

 datar = TH1F('datar','datar',steps,xmin,xmax)
 hh = TH1F('hh','hh',steps,xmin,xmax)
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
#
 if drawData:
  datar = dataih.Clone()
 else:
  datar = hh.Clone()
 datar.SetName('datar')
 datar.GetYaxis().SetRangeUser(0.6,1.4) 
 datar.GetYaxis().SetLabelSize(0.11)
 datar.Divide(hh)
 datar.Draw('ep')
 
 l = TLine(xmin,1,xmax,1)
 l.SetLineStyle(3)
 l.Draw()
 c.Update()
 print('you just read '+leaf)
 if saveAsk:
  save2 = raw_input ('Press Enter to Continue (type save to save)\n')
  if save2 == 'save':
   c.Print(path+extraName+'_'+leaf+'_Round'+str(i)+'.png')
 else:
   c.Print(path+extraName+'_'+leaf+'_Round'+str(i)+'.png')
 

 log.write('Round '+str(i)+'\n')
 log.write('------------------------------------------------\n')
 log.write('Non Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  '+str(CutsMCn)+'\n\n')
 log.write(' Cuts Data: '+str(CutsDatan)+'\n\n')
 log.write('Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  '+str(CutsMCi)+'\n\n')
 log.write(' Cuts Data: '+str(CutsDatai)+'\n\n')
 log.write(' Cuts Wbb: '+str(CutsMCiwbb)+'\n\n')
 log.write(' Cuts Wcc: '+str(CutsMCiwcc)+'\n\n')
 log.write(' Cuts Wc: '+str(CutsMCiwc)+'\n\n')
 log.write(' Cuts Wl: '+str(CutsMCiwl)+'\n\n')
 if drawQCD:
  log.write('Anti-Isolated Sizes\n')
  log.write('---------------------------\n')
  log.write(' Wn Size:--------'+str(wnnhSize)+'\n')
  log.write(' W1 Size:--------'+str(w1nhSize)+'\n')
  log.write(' W2 Size:--------'+str(w2nhSize)+'\n')
  log.write(' W3 Size:--------'+str(w3nhSize)+'\n')
  log.write(' W4 Size:--------'+str(w4nhSize)+'\n')
  log.write(' tt Size:--------'+str(ttbnhSize)+'\n')
  log.write(' t_t Size:-------'+str(t_tnhSize)+'\n')
  log.write(' tb_t Size:------'+str(tb_tnhSize)+'\n')
  log.write(' t_s Size:-------'+str(t_snhSize)+'\n')
  log.write(' tb_s Size:------'+str(tb_snhSize)+'\n')
  log.write(' t_tw Size:------'+str(t_twnhSize)+'\n')
  log.write(' tb_tw Size:-----'+str(tb_twnhSize)+'\n')
  log.write(' WW Size:--------'+str(wwnhSize)+'\n')
  log.write(' WZ Size:--------'+str(wznhSize)+'\n')
  log.write(' ZZ Size:--------'+str(zznhSize)+'\n')
  log.write(' Drell-Yan Size:-'+str(znhSize)+'\n')
  log.write(' QCD Size:-------'+str(qhSize)+'\n')
  log.write(' Data Size:      '+str(datanhSize)+'\n')
 else:
  log.write('no qcd drawn\n\n')
 log.write('---------------------------------------------\n')
 log.write('Isolated Sizes\n')
 log.write('---------------------------\n')
 log.write('W:\n')
 log.write('  Wn+light:--------'+str(wlnihSize)+'\n')
 log.write('  W1+light:--------'+str(wl1ihSize)+'\n')
 log.write('  W2+light:--------'+str(wl2ihSize)+'\n')
 log.write('  W3+light:--------'+str(wl3ihSize)+'\n')
 log.write('  W4+light:--------'+str(wl4ihSize)+'\n\n')
 log.write('  Wn+c:------------'+str(wcnihSize)+'\n')
 log.write('  W1+c:------------'+str(wc1ihSize)+'\n')
 log.write('  W2+c:------------'+str(wc2ihSize)+'\n')
 log.write('  W3+c:------------'+str(wc3ihSize)+'\n')
 log.write('  W4+c:------------'+str(wc4ihSize)+'\n\n')
 log.write('  Wn+cc:-----------'+str(wccnihSize)+'\n')
 log.write('  W1+cc:-----------'+str(wcc1ihSize)+'\n')
 log.write('  W2+cc:-----------'+str(wcc2ihSize)+'\n')
 log.write('  W3+cc:-----------'+str(wcc3ihSize)+'\n')
 log.write('  W4+cc:-----------'+str(wcc4ihSize)+'\n\n')
 log.write('  Wn+bb:-----------'+str(wbbnihSize)+'\n')
 log.write('  W1+bb:-----------'+str(wbb1ihSize)+'\n')
 log.write('  W2+bb:-----------'+str(wbb2ihSize)+'\n')
 log.write('  W3+bb:-----------'+str(wbb3ihSize)+'\n')
 log.write('  W4+bb:-----------'+str(wbb4ihSize)+'\n')
 log.write('tt Size:--------'+str(ttbihSize)+'\n')
 log.write('t_t Size:-------'+str(t_tihSize)+'\n')
 log.write('tb_t Size:------'+str(tb_tihSize)+'\n')
 log.write('t_s Size:-------'+str(t_sihSize)+'\n')
 log.write('tb_s Size:------'+str(tb_sihSize)+'\n')
 log.write('t_tw Size:------'+str(t_twihSize)+'\n')
 log.write('tb_tw Size:-----'+str(tb_twihSize)+'\n')
 log.write('WW Size:--------'+str(wwihSize)+'\n')
 log.write('WZ Size:--------'+str(wzihSize)+'\n')
 log.write('ZZ Size:--------'+str(zzihSize)+'\n')
 log.write('Drell-Yan Size:-'+str(zihSize)+'\n')
 if drawData:
  log.write('Data Size:          '+str(dataihSize)+'\n')
 else:
  log.write('No Data Drawn :(\n')
 log.write('---------------------------\n')
 log.write('Isolated Number of Entries\n')
 log.write('---------------------------\n')
 log.write('W:\n')
 log.write('  Wn+light:--------'+str(wlnihEntries)+'\n')
 log.write('  W1+light:--------'+str(wl1ihEntries)+'\n')
 log.write('  W2+light:--------'+str(wl2ihEntries)+'\n')
 log.write('  W3+light:--------'+str(wl3ihEntries)+'\n')
 log.write('  W4+light:--------'+str(wl4ihEntries)+'\n\n')
 log.write('  Wn+c:------------'+str(wcnihEntries)+'\n')
 log.write('  W1+c:------------'+str(wc1ihEntries)+'\n')
 log.write('  W2+c:------------'+str(wc2ihEntries)+'\n')
 log.write('  W3+c:------------'+str(wc3ihEntries)+'\n')
 log.write('  W4+c:------------'+str(wc4ihEntries)+'\n\n')
 log.write('  Wn+cc:-----------'+str(wccnihEntries)+'\n')
 log.write('  W1+cc:-----------'+str(wcc1ihEntries)+'\n')
 log.write('  W2+cc:-----------'+str(wcc2ihEntries)+'\n')
 log.write('  W3+cc:-----------'+str(wcc3ihEntries)+'\n')
 log.write('  W4+cc:-----------'+str(wcc4ihEntries)+'\n\n')
 log.write('  Wn+bb:-----------'+str(wbbnihEntries)+'\n')
 log.write('  W1+bb:-----------'+str(wbb1ihEntries)+'\n')
 log.write('  W2+bb:-----------'+str(wbb2ihEntries)+'\n')
 log.write('  W3+bb:-----------'+str(wbb3ihEntries)+'\n')
 log.write('  W4+bb:-----------'+str(wbb4ihEntries)+'\n')
 log.write('tt Entries:--------'+str(ttbihEntries)+'\n')
 log.write('t_t Entries:-------'+str(t_tihEntries)+'\n')
 log.write('tb_t Entries:------'+str(tb_tihEntries)+'\n')
 log.write('t_s Entries:-------'+str(t_sihEntries)+'\n')
 log.write('tb_s Entries:------'+str(tb_sihEntries)+'\n')
 log.write('t_tw Entries:------'+str(t_twihEntries)+'\n')
 log.write('tb_tw Entries:-----'+str(tb_twihEntries)+'\n')
 log.write('WW Entries:--------'+str(wwihEntries)+'\n')
 log.write('WZ Entries:--------'+str(wzihEntries)+'\n')
 log.write('ZZ Entries:--------'+str(zzihEntries)+'\n')
 log.write('Drell-Yan Entries:-'+str(zihEntries)+'\n')
 if drawData:
  log.write('Data Entries:          '+str(dataihEntries)+'\n')
 log.write('---------------------------------------------\n\n')

 print('\nFinished '+str(i)+' of '+str(nrplots-1)+'\n')

###########################################################

can = TCanvas('can','Canvas Named can',canx,cany)
pad1 = TPad('pad1','pad1',0,0.3,1,1)
pad1.SetBottomMargin(0.08)
pad1.Draw()
pad1.cd()

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
hc.GetXaxis().SetRangeUser(xmin,xmax)
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
c.cd()
p1.cd()
hc.Draw("hist")
if drawData:
 datac.Draw('sames')
leg.Draw('sames')
cpr.prelim_alt(19429.)
tex.SetTextAlign(11)#left, bottom
tex.DrawLatex(0.17,0.9,title)

can.cd()
pad2 = TPad('pad2','pad2',0,0,1,0.3)
pad2.SetTopMargin(0.1)
pad2.Draw()
pad2.cd()

datarc = TH1F('datarc','datarc',nrplots,0,nrplots)
hhc = TH1F('hhc','hhc',nrplots,0,nrplots)
if drawQCD:
 hhc.Add(qc)
hhc.Add(zc)
hhc.Add(dc)
hhc.Add(sttc)
hhc.Add(stsc)
hhc.Add(sttwc)
hhc.Add(ttbc)
hhc.Add(wbbc)
hhc.Add(wccc)
hhc.Add(wcc)
hhc.Add(wlc)

if drawData:
 datarc = datac.Clone()
else:
 datarc = hhc.Clone()
datarc.SetName('datarc')
datarc.GetYaxis().SetRangeUser(0.6,1.4) 
datarc.GetYaxis().SetLabelSize(0.11)
datarc.Divide(hhc)
datarc.Draw('ep')

l = TLine(0,1,nrplots,1)
l.SetLineStyle(3)
l.Draw()
can.Update()
print('you just read '+leaf)
if saveAsk:
 save = raw_input ('Press Enter to Continue (type save to save)\n')
 if save == 'save':
  can.Print(path+extraName+'_'+leaf+'_Effects.png')
else:
  can.Print(path+extraName+'_'+leaf+'_Effects.png')

outFile.Write()
print('')
print('Your File is here: '+path+extraName+'_'+leaf+'.root')
print('')

