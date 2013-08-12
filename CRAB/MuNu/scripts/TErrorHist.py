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
import TErrorCuts as ct  #function which makes cut strings
import histoRange as hr #manages range, lables for plots

CutMc,CutMcUp,CutMcDown = ct.cutmaker()

ttbar_filename  = '../data/v0/TTbar_hadd.root'

ttbar_file = TFile( ttbar_filename   )

eventTreeLocation = 'muNuEventTree/eventTree'

ttbar_tree    =  ttbar_file.Get(eventTreeLocation)

#Start the Plotting Program
leaf = 'Mt'
#leaf = 'MtCal'

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

path = '../plots/TTbarError'
extraName=''
outFile=gROOT.FindObject(path+extraName+'_'+leaf+'.root')
if outFile : outFile.Close()
outFile = TFile(path+extraName+'_'+leaf+'.root','RECREATE','TTbar +- error')

log = open(path+extraName+'_'+leaf+'.log','w')

print('----------------------------')
print('      --'+leaf+'--')
print('----------------------------')

####
I = xmin
F = xmax
print(' ttbar weighted')
httbar,httbarSize,httbarSizePart,httbarEvents = h.gram(ttbar_tree,leaf,xmin,xmax,steps,CutMc,I,F)
httbar.SetName('httbar')
print('  '+str(httbarSize))
print('  '+str(httbarSizePart))
####
print(' ttbar up')
httbarUp,httbarUpSize,httbarUpSizePart,httbarEvents = h.gram(ttbar_tree,leaf,xmin,xmax,steps,CutMcUp,I,F)
httbarUp.SetName('httbarUp')
print('  '+str(httbarUpSize))
print('  '+str(httbarUpSizePart))
####
print(' ttbar down')
httbarDown,httbarDownSize,httbarDownSizePart,httbarDownEvents = h.gram(ttbar_tree,leaf,xmin,xmax,steps,CutMcDown,I,F)
httbarDown.SetName('httbarDown')
print('  '+str(httbarDownSize))
print('  '+str(httbarDownSizePart))
####

outFile.Write()
print('')
print('Your File is here: '+path+extraName+'_'+leaf+'.root')
print('')

