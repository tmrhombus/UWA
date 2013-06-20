import ROOT
from ROOT import TLatex
tex = ROOT.TLatex()
tex.SetNDC(True)
def prelim(lumi):
 tex.SetTextSize(0.07)
 tex.SetTextAlign(31) #right, bottom 
 tex.DrawLatex(0.9,0.9,'#font[32]{CMS Preliminary}')
 tex.SetTextSize(0.03)
 tex.SetTextAlign(33)
 lumiTitle = '#int L dt = %.1f fb^{-1}' %(lumi/1000.)
 tex.DrawLatex(0.87,0.87,lumiTitle)

def prelim_alt(lumi):
 tex.SetTextSize(0.07)
 tex.SetTextAlign(13) #left, top 
 tex.DrawLatex(0.11,0.89,'#font[32]{CMS Preliminary}')
 tex.SetTextSize(0.03)
 tex.SetTextAlign(33)
 lumiTitle = '#int L dt = %.1f fb^{-1}' %(lumi/1000.)
 tex.DrawLatex(0.87,0.87,lumiTitle)
