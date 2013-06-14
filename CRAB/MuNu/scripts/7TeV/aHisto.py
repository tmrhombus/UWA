#!/usr/bin/env python
'''
Makes a single histogram and gives its total size and over a range
Author: T.M.Perry UW
'''
import ROOT
from ROOT import *

def gram(tree,leaf,xmin,xmax,steps,cuts,I,F):
 
 histo = TH1F('histo','histo',steps,xmin,xmax)
 tree.Draw(leaf+'>>histo',cuts,'')

 histo.SetTitle('') 
 gStyle.SetOptStat('')
 gROOT.SetStyle('Plain')

 bmin = histo.GetXaxis().FindBin(xmin)
 bmax = histo.GetXaxis().FindBin(xmax)
 bminI = histo.GetXaxis().FindBin(I)
 bmaxF = histo.GetXaxis().FindBin(F)
 
 size = histo.Integral(bmin,bmax)
 sizePart = histo.Integral(bminI,bmaxF)
 return histo,size,sizePart
