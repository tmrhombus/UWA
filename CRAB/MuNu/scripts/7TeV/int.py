#!/usr/bin/env python
'''
Integrate the premade histogram for a set range
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *

path = '../DsubMC/'

jNr = 3
bNr = 1

filename=[]
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_20')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_30')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_40')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso2rescaled_0_200')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_20')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_30')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_40')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso3rescaled_0_200')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_20')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_30')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_40')
filename.append('mt'+str(jNr)+'j'+str(bNr)+'bIso4rescaled_0_200')


first = 0
last = 150

for i in filename:
 theFile = TFile(path+i+'.root')
 print('-------------------')
 print('In Range '+str(first)+' to '+str(last))
 print(i)

 hh = theFile.Get('hh')
 bminh = hh.GetXaxis().FindBin(first)
 bmaxh = hh.GetXaxis().FindBin(last)
 sizeh = hh.Integral(bminh,bmaxh)
 print('MC (with QCD):  '+str(sizeh))

 datah = theFile.Get('dataih')
 bmindat = datah.GetXaxis().FindBin(first)
 bmaxdat = datah.GetXaxis().FindBin(last)
 sizedat = datah.Integral(bmindat,bmaxdat)
 print('Data Size:      '+str(sizedat))

 qh = theFile.Get('qh')
 bminq = qh.GetXaxis().FindBin(first)
 bmaxq = qh.GetXaxis().FindBin(last)
 sizeq = qh.Integral(bminq,bmaxq)
 print('QCD:            '+str(sizeq))
 print('-------------------')
 

