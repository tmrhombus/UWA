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

import aHisto as h #function to make histograms
import cuts as ct  #function which makes cut strings
import histoRange as hr #manages range, lables for plots

#import scaleqcd as qs

# define some parameters to be used in ct.cutmaker
iso_value = 0.12
antiIso_value = 0.2
lumi = 13498. #luminosity 
mt = 50. #transverse mass cut
bNr = 0 #number of btags
btype = 't' # t , m , l
jNr = 2 #number of jets
I = 0 # for integration initial bin
F = 20 # final bin
 
qcdFromData = False 
qcdFromMC = False
qcdFromDsubMC=True

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

#isolationValue,antiIsoValue,lumi,massTrans,bnr,btype,jnr
CutsMCn,CutsMCi,CutsDatan,CutsDatai,CutsMCnw,CutsMCiw,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb = ct.cutmaker(
 iso_value,antiIso_value,lumi,mt,0,'t',2
 )

datafilename = '../data/wMuNuData.root'
sttfilename = '../data/SingleTop/SingleTop_t.root'
stsfilename = '../data/SingleTop/SingleTop_s.root'
sttwfilename = '../data/SingleTop/SingleTop_tW.root'
#stfilename = '../data/SingleTop.root'
ttbfilename = '../data/TTbar.root'
dfilename = '../data/VV.root'
#wfilename = '../data/W.root'
wnfilename = '../data/W/WJets.root'
w1filename = '../data/W/W1Jet.root'
w2filename = '../data/W/W2Jet.root'
w3filename = '../data/W/W3Jet.root'
w4filename = '../data/W/W4Jet.root'
zfilename = '../data/Drell.root'

datafile = TFile(datafilename)
sttfile = TFile(sttfilename)
stsfile = TFile(stsfilename)
sttwfile = TFile(sttwfilename)
#stfile = TFile(stfilename)
ttbfile = TFile(ttbfilename)
dfile = TFile(dfilename)
#wfile = TFile(wfilename)
wnfile = TFile(wnfilename)
w1file = TFile(w1filename)
w2file = TFile(w2filename)
w3file = TFile(w3filename)
w4file = TFile(w4filename)
zfile = TFile(zfilename)

eventTreeLocation = 'muNuEventTree/eventTree'

dataTree = datafile.Get(eventTreeLocation)
sttTree = sttfile.Get(eventTreeLocation)    #T(bar)_t
stsTree = stsfile.Get(eventTreeLocation)    #T(bar)_s
sttwTree = sttwfile.Get(eventTreeLocation)  #T(bar)_tW
#stTree = stfile.Get(eventTreeLocation)      #SingleTop all
ttbTree = ttbfile.Get(eventTreeLocation)    #TTbar
dTree = dfile.Get(eventTreeLocation)        #Diboson
#wTree = wfile.Get(eventTreeLocation)        #Combined W
wnTree = wnfile.Get(eventTreeLocation)      #W + nJets
w1Tree = w1file.Get(eventTreeLocation)      #W + 1Jets
w2Tree = w2file.Get(eventTreeLocation)      #W + 2Jets
w3Tree = w3file.Get(eventTreeLocation)      #W + 3Jets
w4Tree = w4file.Get(eventTreeLocation)      #W + 4Jets
zTree = zfile.Get(eventTreeLocation)        #Drell-Yan

#naming where output goes
fitrange = '_'+str(I)+'_'+str(F)
re = 'unscaled'
if qcdRescale:
 re = 'rescaled'
path = '../plots/'
extraName = str(jNr)+'j'+str(bNr)+'b'#+str(antiIso_value)+re+fitrange

#Start the Plotting Program
#leafs = ['Mt']
#leafs = ['vertices']
#leafs = ['mJJ','J1CVSbtag','J1CSVMVAbtag','J2CVSbtag','J2CSVMVAbtag','J1DR','J2DR']
leafs = ['muonPt','MET','J1CSVbtag','J2CSVbtag','vertices','muonPhi','J1DR','J2DR','WPt','DiMuonMass','mJ3J4','ptJJ','met','MtCal','muonEta','ht','highestJetEta','secondJetEta','thirdJetEta','highestJetPhi','secondJetPhi','thirdJetPhi','highestJetPt','secondJetPt','thirdJetPt']
for leaf in leafs:

 steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
 
 outFile=gROOT.FindObject(path+leaf+extraName+'.root')
 if outFile : outFile.Close()
 outFile = TFile(path+leaf+extraName+'.root','RECREATE','Demo ROOT file')
 
 log = open(path+leaf+extraName+'.log','w')
 
 print('----------------------------')
 print('      --'+leaf+'--')
 print(extraName)
 print('----------------------------')
 
 ###
 datanh,datanhSize,datanhSizePart = h.gram(dataTree,leaf,xmin,xmax,steps,CutsDatan,I,F)
 print('For QCD Shape')
 print('data nonIso')
 datanh.SetName('datanh')
 print('  '+str(datanhSize))
 print('  '+str(datanhSizePart))
####
 print('  z nonIso')
 znh,znhSize,znhSizePart = h.gram(zTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 znh.SetName('znh')
 znh.Scale(sf_drell)
 print('    '+str(znhSize))
 print('    '+str(znhSizePart))
####
 print('  d nonIso')
 dnh,dnhSize,dnhSizePart = h.gram(dTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 dnh.SetName('dnh')
 dnh.Scale(sf_vv)
 print('    '+str(dnhSize))
 print('    '+str(dnhSizePart))
####
 print('  singletop t nonIso')
 sttnh,sttnhSize,sttnhSizePart = h.gram(sttTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 sttnh.SetName('sttnh')
 sttnh.Scale(sf_st)
 print('    '+str(sttnhSize))
 print('    '+str(sttnhSizePart))
 ###
 print('  singletop s nonIso')
 stsnh,stsnhSize,stsnhSizePart = h.gram(stsTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 stsnh.SetName('stsnh')
 stsnh.Scale(sf_st)
 print('    '+str(stsnhSize))
 print('    '+str(stsnhSizePart))
 ###
 print('  singletop tw nonIso')
 sttwnh,sttwnhSize,sttwnhSizePart = h.gram(sttwTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 sttwnh.SetName('sttwnh')
 sttwnh.Scale(sf_st)
 print('    '+str(sttwnhSize))
 print('    '+str(sttwnhSizePart))
####
 print('  ttbar nonIso')
 ttbnh,ttbnhSize,ttbnhSizePart = h.gram(ttbTree,leaf,xmin,xmax,steps,CutsMCn,I,F)
 ttbnh.SetName('ttbnh')
 ttbnh.Scale(sf_ttbar)
 print('    '+str(ttbnhSize))
 print('    '+str(ttbnhSizePart))
####
 print('  wn nonIso')
 wnnh,wnnhSize,wnnhSizePart = h.gram(wnTree,leaf,xmin,xmax,steps,CutsMCnw,I,F)
 wnnh.SetName('wnnh')
 wnnh.Scale(sf_wjets)
 print('    '+str(wnnhSize))
 print('    '+str(wnnhSizePart))
 print('  w1 nonIso')
 ###
 w1nh,w1nhSize,w1nhSizePart = h.gram(w1Tree,leaf,xmin,xmax,steps,CutsMCnw,I,F)
 w1nh.SetName('w1nh')
 w1nh.Scale(sf_wjets)
 print('    '+str(w1nhSize))
 print('    '+str(w1nhSizePart))
 print('  w2 nonIso')
 ###
 w2nh,w2nhSize,w2nhSizePart = h.gram(w2Tree,leaf,xmin,xmax,steps,CutsMCnw,I,F)
 w2nh.SetName('w2nh')
 w2nh.Scale(sf_wjets)
 print('    '+str(w2nhSize))
 print('    '+str(w2nhSizePart))
 print('  w3 nonIso')
 ###
 w3nh,w3nhSize,w3nhSizePart = h.gram(w3Tree,leaf,xmin,xmax,steps,CutsMCnw,I,F)
 w3nh.SetName('w3nh')
 w3nh.Scale(sf_wjets)
 print('    '+str(w3nhSize))
 print('    '+str(w3nhSizePart))
 print('  w4 nonIso')
 ###
 w4nh,w4nhSize,w4nhSizePart = h.gram(w4Tree,leaf,xmin,xmax,steps,CutsMCnw,I,F)
 w4nh.SetName('w4nh')
 w4nh.Scale(sf_wjets)
 print('    '+str(w4nhSize))
 print('    '+str(w4nhSizePart))
#
 print('subtracting non-iso MC from Data ')
 qh = datanh.Clone()
 qh.SetName('qh')
 qh.Add(znh,-1)
 qh.Add(dnh,-1)
 qh.Add(sttnh,-1)
 qh.Add(stsnh,-1)
 qh.Add(sttwnh,-1)
 qh.Add(ttbnh,-1)
 qh.Add(wnnh,-1)
 qh.Add(w1nh,-1)
 qh.Add(w2nh,-1)
 qh.Add(w3nh,-1)
 qh.Add(w4nh,-1)

 print('qcd')
 qh.SetTitle('')
 bminq = qh.GetXaxis().FindBin(xmin)
 bmaxq = qh.GetXaxis().FindBin(xmax)
 bIq = qh.GetXaxis().FindBin(I)
 bFq = qh.GetXaxis().FindBin(F)
 qhSizePart = qh.Integral(bIq,bFq)
 qh.Scale(sf_qcd)
 qhSize = qh.Integral(bminq,bmaxq)
 print('  '+str(qhSize))
 print('  '+str(qhSizePart))
 ###
 ###
 print('')
 print('Isolated Variables Now')
 print("data Iso") 
 dataih,dataihSize,dataihSizePart = h.gram(dataTree,leaf,xmin,xmax,steps,CutsDatai,I,F)
 dataih.SetName('dataih')
 print('  '+str(dataihSize))
 print('  '+str(dataihSizePart))
 dimax = dataih.GetMaximum()
####
 print("z Iso")
 zih,zihSize,zihSizePart = h.gram(zTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 zih.SetName('zih')
 zih.Scale(sf_drell)
 print('  '+str(zihSize))
 print('  '+str(zihSizePart))
####
 print("d Iso")
 dih,dihSize,dihSizePart = h.gram(dTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 dih.SetName('dih')
 dih.Scale(sf_vv)
 print('  '+str(dihSize))
 print('  '+str(dihSizePart))
####
 print('single top s Iso')
 stsih,stsihSize,stsihSizePart = h.gram(stsTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 stsih.SetName('stsih')
 stsih.Scale(sf_st)
 print('  '+str(stsihSize))
 print('  '+str(stsihSizePart))
 ###
 print('single top t Iso')
 sttih,sttihSize,sttihSizePart = h.gram(sttTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 sttih.SetName('sttih')
 sttih.Scale(sf_st)
 print('  '+str(sttihSize))
 print('  '+str(sttihSizePart))
 ###
 print('single top tW Iso')
 sttwih,sttwihSize,sttwihSizePart = h.gram(sttwTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 sttwih.SetName('sttwih')
 sttwih.Scale(sf_st)
 print('  '+str(sttwihSize))
 print('  '+str(sttwihSizePart))
####
 print('ttb Iso')
 ttbih,ttbihSize,ttbihSizePart = h.gram(ttbTree,leaf,xmin,xmax,steps,CutsMCi,I,F)
 ttbih.SetName('ttbih')
 ttbih.Scale(sf_ttbar)
 print('  '+str(ttbihSize))
 print('  '+str(ttbihSizePart))
####
####
 print('wl n Iso')
 wlnih,wlnihSize,wlnihSizePart = h.gram(wnTree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wlnih.SetName('wlnih')
 wlnih.Scale(sf_wjets)
 print('  '+str(wlnihSize))
 print('  '+str(wlnihSizePart))
 ####
 print('wc n Iso')
 wcnih,wcnihSize,wcnihSizePart = h.gram(wnTree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wcnih.SetName('wcnih')
 wcnih.Scale(sf_wjets)
 print('  '+str(wcnihSize))
 print('  '+str(wcnihSizePart))
 ####
 print('wcc n Iso')
 wccnih,wccnihSize,wccnihSizePart = h.gram(wnTree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wccnih.SetName('wccnih')
 wccnih.Scale(sf_wjets)
 print('  '+str(wccnihSize))
 print('  '+str(wccnihSizePart))
 ####
 print('wbb n Iso')
 wbbnih,wbbnihSize,wbbnihSizePart = h.gram(wnTree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbbnih.SetName('wbbnih')
 wbbnih.Scale(sf_wjets)
 print('  '+str(wbbnihSize))
 print('  '+str(wbbnihSizePart))
#####
 print('wl 1 Iso')
 wl1ih,wl1ihSize,wl1ihSizePart = h.gram(w1Tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl1ih.SetName('wl1ih')
 wl1ih.Scale(sf_wjets)
 print('  '+str(wl1ihSize))
 print('  '+str(wl1ihSizePart))
 ####
 print('wc 1 Iso')
 wc1ih,wc1ihSize,wc1ihSizePart = h.gram(w1Tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc1ih.SetName('wc1ih')
 wc1ih.Scale(sf_wjets)
 print('  '+str(wc1ihSize))
 print('  '+str(wc1ihSizePart))
 ####
 print('wcc 1 Iso')
 wcc1ih,wcc1ihSize,wcc1ihSizePart = h.gram(w1Tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc1ih.SetName('wcc1ih')
 wcc1ih.Scale(sf_wjets)
 print('  '+str(wcc1ihSize))
 print('  '+str(wcc1ihSizePart))
 ####
 print('wbb 1 Iso')
 wbb1ih,wbb1ihSize,wbb1ihSizePart = h.gram(w1Tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb1ih.SetName('wbb1ih')
 wbb1ih.Scale(sf_wjets)
 print('  '+str(wbb1ihSize))
 print('  '+str(wbb1ihSizePart))
#####
 print('wl 2 Iso')
 wl2ih,wl2ihSize,wl2ihSizePart = h.gram(w2Tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl2ih.SetName('wl2ih')
 wl2ih.Scale(sf_wjets)
 print('  '+str(wl2ihSize))
 print('  '+str(wl2ihSizePart))
 ####
 print('wc 2 Iso')
 wc2ih,wc2ihSize,wc2ihSizePart = h.gram(w2Tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc2ih.SetName('wc2ih')
 wc2ih.Scale(sf_wjets)
 print('  '+str(wc2ihSize))
 print('  '+str(wc2ihSizePart))
 ####
 print('wcc 2 Iso')
 wcc2ih,wcc2ihSize,wcc2ihSizePart = h.gram(w2Tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc2ih.SetName('wcc2ih')
 wcc2ih.Scale(sf_wjets)
 print('  '+str(wcc2ihSize))
 print('  '+str(wcc2ihSizePart))
 ####
 print('wbb 2 Iso')
 wbb2ih,wbb2ihSize,wbb2ihSizePart = h.gram(w2Tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb2ih.SetName('wbb2ih')
 wbb2ih.Scale(sf_wjets)
 print('  '+str(wbb2ihSize))
 print('  '+str(wbb2ihSizePart))
#####
 print('wl 3 Iso')
 wl3ih,wl3ihSize,wl3ihSizePart = h.gram(w3Tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl3ih.SetName('wl3ih')
 wl3ih.Scale(sf_wjets)
 print('  '+str(wl3ihSize))
 print('  '+str(wl3ihSizePart))
 ####
 print('wc 3 Iso')
 wc3ih,wc3ihSize,wc3ihSizePart = h.gram(w3Tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc3ih.SetName('wc3ih')
 wc3ih.Scale(sf_wjets)
 print('  '+str(wc3ihSize))
 print('  '+str(wc3ihSizePart))
 ####
 print('wcc 3 Iso')
 wcc3ih,wcc3ihSize,wcc3ihSizePart = h.gram(w3Tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc3ih.SetName('wcc3ih')
 wcc3ih.Scale(sf_wjets)
 print('  '+str(wcc3ihSize))
 print('  '+str(wcc3ihSizePart))
 ####
 print('wbb 3 Iso')
 wbb3ih,wbb3ihSize,wbb3ihSizePart = h.gram(w3Tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb3ih.SetName('wbb3ih')
 wbb3ih.Scale(sf_wjets)
 print('  '+str(wbb3ihSize))
 print('  '+str(wbb3ihSizePart))
#####
 print('wl 4 Iso')
 wl4ih,wl4ihSize,wl4ihSizePart = h.gram(w4Tree,leaf,xmin,xmax,steps,CutsMCiwl,I,F)
 wl4ih.SetName('wl4ih')
 wl4ih.Scale(sf_wjets)
 print('  '+str(wl4ihSize))
 print('  '+str(wl4ihSizePart))
 ####
 print('wc 4 Iso')
 wc4ih,wc4ihSize,wc4ihSizePart = h.gram(w4Tree,leaf,xmin,xmax,steps,CutsMCiwc,I,F)
 wc4ih.SetName('wc4ih')
 wc4ih.Scale(sf_wjets)
 print('  '+str(wc4ihSize))
 print('  '+str(wc4ihSizePart))
 ####
 print('wcc 4 Iso')
 wcc4ih,wcc4ihSize,wcc4ihSizePart = h.gram(w4Tree,leaf,xmin,xmax,steps,CutsMCiwcc,I,F)
 wcc4ih.SetName('wcc4ih')
 wcc4ih.Scale(sf_wjets)
 print('  '+str(wcc4ihSize))
 print('  '+str(wcc4ihSizePart))
 ####
 print('wbb 4 Iso')
 wbb4ih,wbb4ihSize,wbb4ihSizePart = h.gram(w4Tree,leaf,xmin,xmax,steps,CutsMCiwbb,I,F)
 wbb4ih.SetName('wbb4ih')
 wbb4ih.Scale(sf_wjets)
 print('  '+str(wbb4ihSize))
 print('  '+str(wbb4ihSizePart))
 
 outFile.Write()
 print('')
 print('Your File is here: '+path+leaf+extraName+'.root')
 print('')
 
CutsMCn,CutsMCi,CutsDatan,CutsDatai,CutsMCnw,CutsMCiw,CutsMCnwl,CutsMCiwl,CutsMCnwc,CutsMCiwc,CutsMCnwcc,CutsMCiwcc,CutsMCnwbb,CutsMCiwbb = ct.cutmaker(
 print('    '+str(wnnhSize))
 log.write('------------------------------------------------\n')
 log.write('QCD from Data:    '+str(qcdFromData)+'\n')
 log.write('Non Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  '+str(CutsMCn)+'\n\n')
 log.write(' Cuts Data: '+str(CutsDatan)+'\n\n')
 log.write(' Cuts MCw:  '+str(CutsMCnw)+'\n\n')
 log.write('Isolated\n')
 log.write('---------------------------\n')
 log.write(' Cuts MC:  '+str(CutsMCi)+'\n\n')
 log.write(' Cuts Data: '+str(CutsDatai)+'\n\n')
 log.write(' Cuts Wbb: '+str(CutsMCiwbb)+'\n\n')
 log.write(' Cuts Wcc: '+str(CutsMCiwcc)+'\n\n')
 log.write(' Cuts Wc: '+str(CutsMCiwc)+'\n\n')
 log.write(' Cuts Wl: '+str(CutsMCiwl)+'\n\n')
 log.write('Anti-Isolated Sizes\n')
 log.write('---------------------------\n')
 log.write(' Wn Size:--------'+str(wnnhSize)+'\n')
 log.write(' W1 Size:--------'+str(w1nhSize)+'\n')
 log.write(' W2 Size:--------'+str(w2nhSize)+'\n')
 log.write(' W3 Size:--------'+str(w3nhSize)+'\n')
 log.write(' W4 Size:--------'+str(w4nhSize)+'\n')
 log.write(' tt Size:--------'+str(ttbnhSize)+'\n')
 log.write(' singletop Size:-'+str(stnhSize)+'\n')
 log.write(' WW,WZ,ZZ Size:--'+str(dnhSize)+'\n')
 log.write(' Drell-Yan Size:-'+str(znhSize)+'\n')
 log.write(' QCD Size:-------'+str(qhSize)+'\n')
 log.write(' Data Size:      '+str(datanhSize)+'\n')
 log.write('---------------------------\n')
 log.write('Anti-Isolated Sizes from '+str(I)+' to '+str(F)+'\n')
 log.write('---------------------------\n')
 log.write(' Wn Size:--------'+str(wnnhSizePart)+'\n')
 log.write(' W1 Size:--------'+str(w1nhSizePart)+'\n')
 log.write(' W2 Size:--------'+str(w2nhSizePart)+'\n')
 log.write(' W3 Size:--------'+str(w3nhSizePart)+'\n')
 log.write(' W4 Size:--------'+str(w4nhSizePart)+'\n')
 log.write(' tt Size:--------'+str(ttbnhSizePart)+'\n')
 log.write(' singletop Size:-'+str(stnhSizePart)+'\n')
 log.write(' WW,WZ,ZZ Size:--'+str(dnhSizePart)+'\n')
 log.write(' Drell-Yan Size:-'+str(znhSizePart)+'\n')
 log.write(' QCD Size:-------'+str(qhSizePart)+'\n')
 log.write(' Data Size:      '+str(datanhSizePart)+'\n')
 log.write('---------------------------------------------\n')
 log.write('QCD Scale:   '+str(sf_qcd)+'\n')
 log.write('Drell Scale: '+str(sf_drell)+'\n')
 log.write('t Scale:     '+str(sf_st)+'\n')
 log.write('tt Scale:    '+str(sf_ttbar)+'\n')
 log.write('W+x Scale:   '+str(sf_wjets)+'\n')
 log.write('---------------------------------------------\n\n')
 log.write('Isolated Sizes from '+str(I)+' to '+str(F)+'\n')
 log.write('---------------------------\n')
 log.write('W:\n')
 log.write('  W+light:--------'+str(wlnihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl1ihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl2ihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl3ihSizePart)+'\n')
 log.write('  W+light:--------'+str(wl4ihSizePart)+'\n\n')
 log.write('  W+c:------------'+str(wcnihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc1ihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc2ihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc3ihSizePart)+'\n')
 log.write('  W+c:------------'+str(wc4ihSizePart)+'\n\n')
 log.write('  W+cc:-----------'+str(wccnihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc1ihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc2ihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc3ihSizePart)+'\n')
 log.write('  W+cc:-----------'+str(wcc4ihSizePart)+'\n\n')
 log.write('  W+bb:-----------'+str(wbbnihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb1ihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb2ihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb3ihSizePart)+'\n')
 log.write('  W+bb:-----------'+str(wbb4ihSizePart)+'\n')
 log.write('tt Size:--------'+str(ttbihSizePart)+'\n')
 log.write('t_tW Size:------'+str(ttwihSizePart)+'\n')
 log.write('t_s Size:-------'+str(tsihSizePart)+'\n')
 log.write('t_t Size:-------'+str(ttihSizePart)+'\n')
 log.write('WW,WZ Size:-----'+str(dihSizePart)+'\n')
 log.write('Drell-Yan Size:-'+str(zihSizePart)+'\n')
 log.write('Data Size:          '+str(dataihSizePart)+'\n')
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
 log.write('t_tW Size:------'+str(ttwihSize)+'\n')
 log.write('t_s Size:-------'+str(tsihSize)+'\n')
 log.write('t_t Size:-------'+str(ttihSize)+'\n')
 log.write('WW,WZ Size:-----'+str(dihSize)+'\n')
 log.write('Drell-Yan Size:-'+str(zihSize)+'\n')
 log.write('Data Size:          '+str(dataihSize)+'\n')
 log.write('---------------------------\n')
 log.write('---------------------------------------------\n')
 
 log.close()
 
