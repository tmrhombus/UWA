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
import TErrorParameters as p # parameters

leaf,name,bNr,jNr,jetVeto,Signal,Control,TT_m,TT_me,noMT=p.arams()

CutMc,CutMcUp,CutMcDown = ct.cutmaker(bNr,jNr,jetVeto)
print('cuts')
print(CutMc)
print(' ')
print(CutMcUp)
print(' ')
print(CutMcDown)
print('')

ttbar_filename  = '../data/v0/TTbar_hadd.root'
ttbar_file = TFile( ttbar_filename   )
eventTreeLocation = 'muNuEventTree/eventTree'
ttbar_tree    =  ttbar_file.Get(eventTreeLocation)

#Start the Plotting Program

steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

outFile=gROOT.FindObject(name+'.root')
if outFile : outFile.Close()
outFile = TFile(name+'.root','RECREATE','TTbar +- error')

log = open(name+'.log','w')

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
print('Your File is here: '+name+'.root')
print('')
log.write('Cuts:\n')
log.write('Cut MC:\n')
log.write(CutMc)
log.write('\nCut MC Up:\n')
log.write(CutMcUp)
log.write('\nCut MC Down:\n')
log.write(CutMcDown)
log.close()
