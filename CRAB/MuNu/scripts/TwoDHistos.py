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

import makeFunctions as make #function to make histograms
import TheCuts as ct  #function which makes cut strings
import histoRange as hr #manages range, lables for plots
import TheParameters as p

#import scaleqcd as qs

qcdRescale = False
tRescale = False
ttRescale = False
vRescale = False
dRescale = False
sf_qcd = 1.
sf_drell = 1.
sf_st = 1.   
sf_st_t = 1.#1.025431/2.497226   
sf_ttbar = 1.
sf_wjets = 1.
sf_vv = 1.

#get parameters (used in cutmaker)
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

CutsMCn, CutsMCnW, CutsMCi,CutsDatan,CutsDatai,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb,CutsMCnT,CutsMCiT,CutsMCnTup,CutsMCiTup,CutsMCnTdn,CutsMCiTdn = ct.cutmaker(
 iso_value,antiIso_value,lumi,bNr,btype,jNr,njetcut,jetcut,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,extraCut
)

data_filename     = '../data/moreSV_two/Data.root'
t_t_filename      = '../data/moreSV_two/T_t.root'
t_s_filename      = '../data/moreSV_two/T_s.root'
t_tw_filename     = '../data/moreSV_two/T_tW.root'
tb_t_filename     = '../data/moreSV_two/Tbar_t.root'
tb_s_filename     = '../data/moreSV_two/Tbar_s.root'
tb_tw_filename    = '../data/moreSV_two/Tbar_tW.root'
tt_semi_filename  = '../data/moreSV_two/TTbar_semi.root'
tt_full_filename  = '../data/moreSV_two/TTbar_full.root'
ww_filename       = '../data/moreSV_two/WW.root'
wz_filename       = '../data/moreSV_two/WZ.root'
zz_filename       = '../data/moreSV_two/ZZ.root'
wn_filename       = '../data/moreSV_two/WJets.root'
w1_filename       = '../data/moreSV_two/W1Jet.root'
w2_filename       = '../data/moreSV_two/W2Jet.root'
w3_filename       = '../data/moreSV_two/W3Jet.root'
w4_filename       = '../data/moreSV_two/W4Jet.root'
z_filename        = '../data/moreSV_two/Drell.root'

data_file      = TFile( data_filename )
t_t_file       = TFile( t_t_filename  )
t_s_file       = TFile( t_s_filename  )
t_tw_file      = TFile( t_tw_filename )
tb_t_file      = TFile( tb_t_filename )
tb_s_file      = TFile( tb_s_filename )
tb_tw_file     = TFile( tb_tw_filename)
tt_semi_file   = TFile( tt_semi_filename  )
tt_full_file   = TFile( tt_full_filename  )
ww_file        = TFile( ww_filename   )
wz_file        = TFile( wz_filename   )
zz_file        = TFile( zz_filename   )
wn_file        = TFile( wn_filename   )
w1_file        = TFile( w1_filename   )
w2_file        = TFile( w2_filename   )
w3_file        = TFile( w3_filename   )
w4_file        = TFile( w4_filename   )
z_file         = TFile( z_filename    )

eventTreeLocationNoShift = 'muNuEventTree/eventTree'

data_tree     =  data_file.Get(eventTreeLocationNoShift) 
t_t_tree      =  t_t_file.Get(eventTreeLocation)
t_s_tree      =  t_s_file.Get(eventTreeLocation)
t_tw_tree     =  t_tw_file.Get(eventTreeLocation)
tb_t_tree     =  tb_t_file.Get(eventTreeLocation)
tb_s_tree     =  tb_s_file.Get(eventTreeLocation)
tb_tw_tree    =  tb_tw_file.Get(eventTreeLocation)
tt_semi_tree  =  tt_semi_file.Get(eventTreeLocation)
tt_full_tree  =  tt_full_file.Get(eventTreeLocation)
ww_tree       =  ww_file.Get(eventTreeLocation)
wz_tree       =  wz_file.Get(eventTreeLocation)
zz_tree       =  zz_file.Get(eventTreeLocation)
wn_tree       =  wn_file.Get(eventTreeLocation)
w1_tree       =  w1_file.Get(eventTreeLocation)
w2_tree       =  w2_file.Get(eventTreeLocation)
w3_tree       =  w3_file.Get(eventTreeLocation)
w4_tree       =  w4_file.Get(eventTreeLocation)
z_tree        =  z_file.Get(eventTreeLocation)

#Start the Plotting Program
for leafPair in leafs:

 leafA = leafPair[0]
 leafB = leafPair[1]
 stepsA, minA, maxA, titleA, unitsA, setLogYA = hr.ranger(leafA)
 stepsB, minB, maxB, titleB, unitsB, setLogYB = hr.ranger(leafB)
 
 outFile=gROOT.FindObject(path+extraName+'_'+leafA+'_'+leafB+'.root')
 if outFile : outFile.Close()
 outFile = TFile(path+extraName+'_'+leafA+'_'+leafB+'.root','RECREATE','Demo ROOT file')
 
 log = open(path+extraName+'_'+leafA+'_'+leafB+'.log','w')
 
 print('----------------------------')
 print(leafA+' - '+leafB+'')
 print(extraName)
 print('----------------------------')
 
 if drawQCD:
  ###
  datanh,datanhSize,datanhEntries = make.hist2D(data_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsDatan)
  print('For QCD Shape')
  print('data nonIso')
  datanh.SetName('datanh')
  print('  '+str(datanhSize))
 ####  Drell
  print('  z nonIso')
  znh,znhSize,znhEntries = make.hist2D(z_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  znh.SetName('znh')
  znh.Scale(sf_drell)
  print('    '+str(znhSize))
 ####  Dibosons
  print('  ww nonIso')
  wwnh,wwnhSize,wwnhEntries = make.hist2D(ww_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  wwnh.SetName('wwnh')
  wwnh.Scale(sf_vv)
  print('    '+str(wwnhSize))
  ###
  print('  wz nonIso')
  wznh,wznhSize,wznhEntries = make.hist2D(wz_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  wznh.SetName('wznh')
  wznh.Scale(sf_vv)
  print('    '+str(wznhSize))
  ###
  print('  ww nonIso')
  zznh,zznhSize,zznhEntries = make.hist2D(zz_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  zznh.SetName('zznh')
  zznh.Scale(sf_vv)
  print('    '+str(zznhSize))
 ####  Single Top
  print('  t t nonIso')
  t_tnh,t_tnhSize,t_tnhEntries = make.hist2D(t_t_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  t_tnh.SetName('t_tnh')
  t_tnh.Scale(sf_st_t)
  print('    '+str(t_tnhSize))
  ###
  print('  tb t nonIso')
  tb_tnh,tb_tnhSize,tb_tnhEntries = make.hist2D(tb_t_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  tb_tnh.SetName('tb_tnh')
  tb_tnh.Scale(sf_st)
  print('    '+str(tb_tnhSize))
  ###
  print('  t s nonIso')
  t_snh,t_snhSize,t_snhEntries = make.hist2D(t_s_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  t_snh.SetName('t_snh')
  t_snh.Scale(sf_st)
  print('    '+str(t_snhSize))
  ###
  print('  tb s nonIso')
  tb_snh,tb_snhSize,tb_snhEntries = make.hist2D(tb_s_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  tb_snh.SetName('tb_snh')
  tb_snh.Scale(sf_st)
  print('    '+str(tb_snhSize))
  ###
  print('  t tw nonIso')
  t_twnh,t_twnhSize,t_twnhEntries = make.hist2D(t_tw_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  t_twnh.SetName('t_twnh')
  t_twnh.Scale(sf_st)
  print('    '+str(t_twnhSize))
  ###
  print('  tb tw nonIso')
  tb_twnh,tb_twnhSize,tb_twnhEntries = make.hist2D(tb_tw_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCn)
  tb_twnh.SetName('tb_twnh')
  tb_twnh.Scale(sf_st)
  print('    '+str(tb_twnhSize))
 ####  TTbar
  print('  ttbar semi nonIso')
  tt_seminh,tt_seminhSize,tt_seminhEntries = make.hist2D(tt_semi_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnT)
  tt_seminh.SetName('tt_seminh')
  tt_seminh.Scale(sf_ttbar)
  print('    '+str(tt_seminhSize))
  ###
  print('  ttbar full nonIso')
  tt_fullnh,tt_fullnhSize,tt_fullnhEntries = make.hist2D(tt_full_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnT)
  tt_fullnh.SetName('tt_fullnh')
  tt_fullnh.Scale(sf_ttbar)
  print('    '+str(tt_fullnhSize))
 ####  W
  print('  wn nonIso')
  wnnh,wnnhSize,wnhEntries = make.hist2D(wn_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnW)
  wnnh.SetName('wnnh')
  wnnh.Scale(sf_wjets)
  print('    '+str(wnnhSize))
  print('  w1 nonIso')
  ###
  w1nh,w1nhSize,w1nhEntries = make.hist2D(w1_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnW)
  w1nh.SetName('w1nh')
  w1nh.Scale(sf_wjets)
  print('    '+str(w1nhSize))
  print('  w2 nonIso')
  ###
  w2nh,w2nhSize,w2nhEntries = make.hist2D(w2_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnW)
  w2nh.SetName('w2nh')
  w2nh.Scale(sf_wjets)
  print('    '+str(w2nhSize))
  print('  w3 nonIso')
  ###
  w3nh,w3nhSize,w3nhEntries = make.hist2D(w3_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnW)
  w3nh.SetName('w3nh')
  w3nh.Scale(sf_wjets)
  print('    '+str(w3nhSize))
  print('  w4 nonIso')
  ###
  w4nh,w4nhSize,w4nhEntries = make.hist2D(w4_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCnW)
  w4nh.SetName('w4nh')
  w4nh.Scale(sf_wjets)
  print('    '+str(w4nhSize))
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
  qh.Add(tt_seminh,-1)  #TTbar
  qh.Add(tt_fullnh,-1)  #TTbar
  qh.Add(wnnh,-1)   #W
  qh.Add(w1nh,-1)
  qh.Add(w2nh,-1)
  qh.Add(w3nh,-1)
  qh.Add(w4nh,-1)
 
  print('qcd')
  qh.SetTitle('')
  #bminq = qh.GetXaxis().FindBin(xmin)
  #bmaxq = qh.GetXaxis().FindBin(xmax)
  #bIq = qh.GetXaxis().FindBin(I)
  #bFq = qh.GetXaxis().FindBin(F)
  #qhSizePart = qh.Integral(bIq,bFq)
  qh.Scale(sf_qcd)
  #qhSize = qh.Integral(bminq,bmaxq)
  qhSize = -1
  qhEntries = qh.GetEntries()
  print('  '+str(qhSize))
 ####################################
 if drawData:
  ### Data
  print('')
  print('Isolated Variables Now')
  print("data Iso") 
  dataih,dataihSize,dataihEntries = make.hist2D(data_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsDatai)
  dataih.SetName('dataih')
  print('  '+str(dataihSize))
  dimax = dataih.GetMaximum()
#### Drell
 print("z Iso")
 zih,zihSize,zihEntries = make.hist2D(z_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 zih.SetName('zih')
 zih.Scale(sf_drell)
 print('  '+str(zihSize))
#### Diboson
 print("ww Iso")
 wwih,wwihSize,wwihEntries = make.hist2D(ww_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 wwih.SetName('wwih')
 wwih.Scale(sf_vv)
 print('  '+str(wwihSize))
 ###
 print("wz Iso")
 wzih,wzihSize,wzihEntries = make.hist2D(wz_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 wzih.SetName('wzih')
 wzih.Scale(sf_vv)
 print('  '+str(wzihSize))
 ###
 print("zz Iso")
 zzih,zzihSize,zzihEntries = make.hist2D(zz_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 zzih.SetName('zzih')
 zzih.Scale(sf_vv)
 print('  '+str(zzihSize))
#### Single Top
 print('t t Iso')
 t_tih,t_tihSize,t_tihEntries = make.hist2D(t_t_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 t_tih.SetName('t_tih')
 t_tih.Scale(sf_st_t)
 print('  '+str(t_tihSize))
 ###
 print('tb t Iso')
 tb_tih,tb_tihSize,tb_tihEntries = make.hist2D(tb_t_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 tb_tih.SetName('tb_tih')
 tb_tih.Scale(sf_st)
 print('  '+str(tb_tihSize))
 ###
 print('t s Iso')
 t_sih,t_sihSize,t_sihEntries = make.hist2D(t_s_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 t_sih.SetName('t_sih')
 t_sih.Scale(sf_st)
 print('  '+str(t_sihSize))
 ###
 print('tb s Iso')
 tb_sih,tb_sihSize,tb_sihEntries = make.hist2D(tb_s_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 tb_sih.SetName('tb_sih')
 tb_sih.Scale(sf_st)
 print('  '+str(tb_sihSize))
 ###
 print('t tw Iso')
 t_twih,t_twihSize,t_twihEntries = make.hist2D(t_tw_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 t_twih.SetName('t_twih')
 t_twih.Scale(sf_st)
 print('  '+str(t_twihSize))
 ###
 print('tb tw Iso')
 tb_twih,tb_twihSize,tb_twihEntries = make.hist2D(tb_tw_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCi)
 tb_twih.SetName('tb_twih')
 tb_twih.Scale(sf_st)
 print('  '+str(tb_twihSize))
#### TTbar
 print('ttb semi Iso')
 tt_semiih,tt_semiihSize,tt_semiihEntries = make.hist2D(tt_semi_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiT)
 tt_semiih.SetName('tt_semiih')
 tt_semiih.Scale(sf_ttbar)
 print('  '+str(tt_semiihSize))
 ###
 print('ttb full Iso')
 tt_fullih,tt_fullihSize,tt_fullihEntries = make.hist2D(tt_full_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiT)
 tt_fullih.SetName('tt_fullih')
 tt_fullih.Scale(sf_ttbar)
 print('  '+str(tt_fullihSize))
#### W + Jets
 print('wl n Iso')
 wlnih,wlnihSize,wlnihEntries = make.hist2D(wn_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwl)
 wlnih.SetName('wlnih')
 wlnih.Scale(sf_wjets)
 print('  '+str(wlnihSize))
 ####
 print('wc n Iso')
 wcnih,wcnihSize,wcnihEntries = make.hist2D(wn_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwc)
 wcnih.SetName('wcnih')
 wcnih.Scale(sf_wjets)
 print('  '+str(wcnihSize))
 ####
 print('wcc n Iso')
 wccnih,wccnihSize,wccnihEntries = make.hist2D(wn_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwcc)
 wccnih.SetName('wccnih')
 wccnih.Scale(sf_wjets)
 print('  '+str(wccnihSize))
 ####
 print('wbb n Iso')
 wbbnih,wbbnihSize,wbbnihEntries = make.hist2D(wn_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwbb)
 wbbnih.SetName('wbbnih')
 wbbnih.Scale(sf_wjets)
 print('  '+str(wbbnihSize))
#####
 print('wl 1 Iso')
 wl1ih,wl1ihSize,wl1ihEntries = make.hist2D(w1_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwl)
 wl1ih.SetName('wl1ih')
 wl1ih.Scale(sf_wjets)
 print('  '+str(wl1ihSize))
 ####
 print('wc 1 Iso')
 wc1ih,wc1ihSize,wc1ihEntries = make.hist2D(w1_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwc)
 wc1ih.SetName('wc1ih')
 wc1ih.Scale(sf_wjets)
 print('  '+str(wc1ihSize))
 ####
 print('wcc 1 Iso')
 wcc1ih,wcc1ihSize,wcc1ihEntries = make.hist2D(w1_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwcc)
 wcc1ih.SetName('wcc1ih')
 wcc1ih.Scale(sf_wjets)
 print('  '+str(wcc1ihSize))
 ####
 print('wbb 1 Iso')
 wbb1ih,wbb1ihSize,wbb1ihEntries = make.hist2D(w1_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwbb)
 wbb1ih.SetName('wbb1ih')
 wbb1ih.Scale(sf_wjets)
 print('  '+str(wbb1ihSize))
#####
 print('wl 2 Iso')
 wl2ih,wl2ihSize,wl2ihEntries = make.hist2D(w2_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwl)
 wl2ih.SetName('wl2ih')
 wl2ih.Scale(sf_wjets)
 print('  '+str(wl2ihSize))
 ####
 print('wc 2 Iso')
 wc2ih,wc2ihSize,wc2ihEntries = make.hist2D(w2_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwc)
 wc2ih.SetName('wc2ih')
 wc2ih.Scale(sf_wjets)
 print('  '+str(wc2ihSize))
 ####
 print('wcc 2 Iso')
 wcc2ih,wcc2ihSize,wcc2ihEntries = make.hist2D(w2_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwcc)
 wcc2ih.SetName('wcc2ih')
 wcc2ih.Scale(sf_wjets)
 print('  '+str(wcc2ihSize))
 ####
 print('wbb 2 Iso')
 wbb2ih,wbb2ihSize,wbb2ihEntries = make.hist2D(w2_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwbb)
 wbb2ih.SetName('wbb2ih')
 wbb2ih.Scale(sf_wjets)
 print('  '+str(wbb2ihSize))
#####
 print('wl 3 Iso')
 wl3ih,wl3ihSize,wl3ihEntries = make.hist2D(w3_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwl)
 wl3ih.SetName('wl3ih')
 wl3ih.Scale(sf_wjets)
 print('  '+str(wl3ihSize))
 ####
 print('wc 3 Iso')
 wc3ih,wc3ihSize,wc3ihEntries = make.hist2D(w3_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwc)
 wc3ih.SetName('wc3ih')
 wc3ih.Scale(sf_wjets)
 print('  '+str(wc3ihSize))
 ####
 print('wcc 3 Iso')
 wcc3ih,wcc3ihSize,wcc3ihEntries = make.hist2D(w3_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwcc)
 wcc3ih.SetName('wcc3ih')
 wcc3ih.Scale(sf_wjets)
 print('  '+str(wcc3ihSize))
 ####
 print('wbb 3 Iso')
 wbb3ih,wbb3ihSize,wbb3ihEntries = make.hist2D(w3_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwbb)
 wbb3ih.SetName('wbb3ih')
 wbb3ih.Scale(sf_wjets)
 print('  '+str(wbb3ihSize))
#####
 print('wl 4 Iso')
 wl4ih,wl4ihSize,wl4ihEntries = make.hist2D(w4_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwl)
 wl4ih.SetName('wl4ih')
 wl4ih.Scale(sf_wjets)
 print('  '+str(wl4ihSize))
 ####
 print('wc 4 Iso')
 wc4ih,wc4ihSize,wc4ihEntries = make.hist2D(w4_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwc)
 wc4ih.SetName('wc4ih')
 wc4ih.Scale(sf_wjets)
 print('  '+str(wc4ihSize))
 ####
 print('wcc 4 Iso')
 wcc4ih,wcc4ihSize,wcc4ihEntries = make.hist2D(w4_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwcc)
 wcc4ih.SetName('wcc4ih')
 wcc4ih.Scale(sf_wjets)
 print('  '+str(wcc4ihSize))
 ####
 print('wbb 4 Iso')
 wbb4ih,wbb4ihSize,wbb4ihEntries = make.hist2D(w4_tree,leafA,leafB,minA,maxA,stepsA,minB,maxB,stepsB,CutsMCiwbb)
 wbb4ih.SetName('wbb4ih')
 wbb4ih.Scale(sf_wjets)
 print('  '+str(wbb4ihSize))
 
 outFile.Write()
 print('')
 print('Your File is here: '+path+extraName+'_'+leafA+'_'+leafB+'.root')
 print('')
 
 log.write('------------------------------------------------\n')
 log.write('---------------------------\n')
 log.write('Non Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:      \n'+str(CutsMCn)+'\n\n')
 log.write(' Cuts MC Top:  \n'+str(CutsMCnT)+'\n\n')
 log.write(' Cuts Data:    \n'+str(CutsDatan)+'\n\n')
 log.write('Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  \n'+str(CutsMCi)+'\n\n')
 log.write(' Cuts MC Top:  \n'+str(CutsMCiT)+'\n\n')
 log.write(' Cuts Data: \n'+str(CutsDatai)+'\n\n')
 log.write(' Cuts Wbb: \n'+str(CutsMCiwbb)+'\n\n')
 log.write(' Cuts Wcc: \n'+str(CutsMCiwcc)+'\n\n')
 log.write(' Cuts Wc: \n'+str(CutsMCiwc)+'\n\n')
 log.write(' Cuts Wl: \n'+str(CutsMCiwl)+'\n\n')
 if drawQCD:
  log.write('Anti-Isolated Sizes\n')
  log.write('---------------------------\n')
  log.write(' Wn Size:--------'+str(wnnhSize)+'\n')
  log.write(' W1 Size:--------'+str(w1nhSize)+'\n')
  log.write(' W2 Size:--------'+str(w2nhSize)+'\n')
  log.write(' W3 Size:--------'+str(w3nhSize)+'\n')
  log.write(' W4 Size:--------'+str(w4nhSize)+'\n')
  log.write(' tt semi Size:---'+str(tt_seminhSize)+'\n')
  log.write(' tt full Size:---'+str(tt_fullnhSize)+'\n')
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
  log.write('---------------------------\n')
  log.write('QCD Scale:   '+str(sf_qcd)+'\n')
  log.write('Drell Scale: '+str(sf_drell)+'\n')
  log.write('t Scale:     '+str(sf_st)+'\n')
  log.write('t_t Scale:   '+str(sf_st_t)+'\n')
  log.write('tt Scale:    '+str(sf_ttbar)+'\n')
  log.write('W+x Scale:   '+str(sf_wjets)+'\n')
  log.write('---------------------------------------------\n\n')
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
 log.write('tt semi Size:------'+str(tt_semiihSize)+'\n')
 log.write('tt full Size:------'+str(tt_fullihSize)+'\n')
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
 log.write('---------------------------------------------\n')
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
 log.write('tt semi Entries:---'+str(tt_semiihEntries)+'\n')
 log.write('tt full Entries:---'+str(tt_fullihEntries)+'\n')
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
 log.write('---------------------------------------------\n')
 
 print(".log written")
 log.close()
