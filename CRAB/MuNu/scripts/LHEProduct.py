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
import LHEProductCuts as ct  #function which makes cut strings
import histoRange as hr #manages range, lables for plots

#import scaleqcd as qs


CutsMCi = ct.cutmaker()
print(CutsMCi)

wn_filename    = '../data/v5/WJets.root'
w1_filename    = '../data/v5/W1Jet.root'
w2_filename    = '../data/v5/W2Jet.root'
w3_filename    = '../data/v5/W3Jet.root'
w4_filename    = '../data/v5/W4Jet.root'

wn_file    = TFile( wn_filename   )
w1_file    = TFile( w1_filename   )
w2_file    = TFile( w2_filename   )
w3_file    = TFile( w3_filename   )
w4_file    = TFile( w4_filename   )

eventTreeLocation = 'muNuEventTree/eventTree'

wn_tree    =  wn_file.Get(eventTreeLocation)
w1_tree    =  w1_file.Get(eventTreeLocation)
w2_tree    =  w2_file.Get(eventTreeLocation)
w3_tree    =  w3_file.Get(eventTreeLocation)
w4_tree    =  w4_file.Get(eventTreeLocation)

#Start the Plotting Program
leaf = 'LHEProduct'

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

path = '../plots/'
extraName=''
outFile=gROOT.FindObject(path+leaf+extraName+'.root')
if outFile : outFile.Close()
outFile = TFile(path+leaf+extraName+'.root','RECREATE','Demo ROOT file')

print('----------------------------')
print('      --'+leaf+'--')
print('----------------------------')

### W + Jets
####
I = 4
F = 10
print('wbb n Iso')
wbbnih,wbbnihSize,wbbnihSizePart,wbbnihEvents = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
wbbnih.SetName('wbbnih')
print('  '+str(wbbnihSize))
print('  '+str(wbbnihSizePart))
####
print('wbb 1 Iso')
wbb1ih,wbb1ihSize,wbb1ihSizePart,wbb1inEvents = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
wbb1ih.SetName('wbb1ih')
print('  '+str(wbb1ihSize))
print('  '+str(wbb1ihSizePart))
####
print('wbb 2 Iso')
wbb2ih,wbb2ihSize,wbb2ihSizePart,wbb2ihEvents = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
wbb2ih.SetName('wbb2ih')
print('  '+str(wbb2ihSize))
print('  '+str(wbb2ihSizePart))
####
print('wbb 3 Iso')
wbb3ih,wbb3ihSize,wbb3ihSizePart,wbb3ihEvents = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
wbb3ih.SetName('wbb3ih')
print('  '+str(wbb3ihSize))
print('  '+str(wbb3ihSizePart))
####
print('wbb 4 Iso')
wbb4ih,wbb4ihSize,wbb4ihSizePart,wbb4ihEvents = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
wbb4ih.SetName('wbb4ih')
print('  '+str(wbb4ihSize))
print('  '+str(wbb4ihSizePart))

outFile.Write()
print('')
print('Your File is here: '+path+leaf+extraName+'.root')
print('')

