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
leaf = 'Mt'
#leaf = 'MtCal'

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
I = xmin
F = xmax
print(' n Iso')
hn,hnSize,hnSizePart,hnEvents = h.gram(wn_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
hn.SetName('hn')
print('  '+str(hnSize))
print('  '+str(hnSizePart))
####
print(' 1 Iso')
h1,h1Size,h1SizePart,h1Events = h.gram(w1_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
h1.SetName('h1')
print('  '+str(h1Size))
print('  '+str(h1SizePart))
####
print(' 2 Iso')
h2,h2Size,h2SizePart,h2Events = h.gram(w2_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
h2.SetName('h2')
print('  '+str(h2Size))
print('  '+str(h2SizePart))
####
print(' 3 Iso')
h3,h3Size,h3SizePart,h3Events = h.gram(w3_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
h3.SetName('h3')
print('  '+str(h3Size))
print('  '+str(h3SizePart))
####
print(' 4 Iso')
h4,h4Size,h4SizePart,h4Events = h.gram(w4_tree,leaf,xmin,xmax,steps,CutsMCi,I,F)
h4.SetName('h4')
print('  '+str(h4Size))
print('  '+str(h4SizePart))

outFile.Write()
print('')
print('Your File is here: '+path+leaf+extraName+'.root')
print('')

