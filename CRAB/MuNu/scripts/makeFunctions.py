#!/usr/bin/env python  
'''
Some useful functions that keep coming up
Author: T.M.Perry UW
'''
import ROOT
from ROOT import *

def hist1D(tree,leaf,xmin=0,xmax=200,steps=20,cuts='(2>1)',I=-1,F=-1):
 ''' 1D Histogram '''

 histo = TH1F('histo','histo',steps,xmin,xmax)
 tree.Draw(leaf+'>>histo',cuts,'')

 histo.SetTitle('') 
 histo.Sumw2()
 gStyle.SetOptStat('')
 gROOT.SetStyle('Plain')

 bmin = histo.GetXaxis().FindBin(xmin)
 bmax = histo.GetXaxis().FindBin(xmax)
 if I == -1 and F == -1: 
  I = xmin
  F = xmax
 bminI = histo.GetXaxis().FindBin(I)
 bmaxF = histo.GetXaxis().FindBin(F)
 size = histo.Integral(bmin,bmax)
 sizePart = histo.Integral(bminI,bmaxF)
 entries = histo.GetEntries()
 return histo,size,sizePart,entries


def hist2D(tree,leafX,leafY,minX,maxX,stepsX,minY,maxY,stepsY,cuts):
 ''' 2D Histogram '''
 
 histo = TH2F('histo','histo',stepsX,minX,maxX,stepsY,minY,maxY)
 tree.Draw(leafY+':'+leafX+'>>histo',cuts,'colz')
 histo.SetTitle('')
 gStyle.SetOptStat('')
 gROOT.SetStyle('Plain')
 
 size = histo.Integral()
 entries = histo.GetEntries()
 
 return histo,size,entries
