#!/usr/bin/env python
'''
Dump a .png for evey histogram in file
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT, TCanvas, TLegend, gStyle
import sys 
import fnmatch as fnm 
import time

infileG = sys.argv[1] 
infileT = sys.argv[2]
path    = sys.argv[3]
runname = sys.argv[4] 
sample  = sys.argv[5]
logname=path+"/"+runname+sample+"_comparison"
outname=path+"/"+runname+sample+"_comparison"

qcd = "h_TTqcd"
if ( sample=="wbb" ):
 qcd = "h_qcd"

rebin = 1
stom = 1
sgiu = 1

gStyle.SetOptStat('')
gStyle.SetLineWidth(3)
gStyle.SetPadTickY(1)

gfile = TFile(path+"/"+infileG+".root")
tfile = TFile(path+"/"+infileT+".root")

canx = 900 
cany = 900
c = TCanvas('c','Canvas Named c',canx,cany)

histnames = [
"data_obs",
"h_Wbb5F",
"h_Wbb4F",
"h_Wcc",
"h_TTbar",
   qcd,
"h_Drell",
"h_T",
"h_VV",
"h_Wl"
]


log = open(logname+'.log','w')
log.write('\n\n') 
log.write('  infileG %s \n'%( infileG ) )  
log.write('  infileT %s \n'%( infileT ) ) 
log.write('  path    %s \n'%( path    ) ) 
log.write('  runname %s \n'%( runname ) ) 
log.write('  sample  %s \n'%( sample  ) ) 
log.write('  gsfTom  %.4f\n'%( stom ) ) 
log.write('  gsfGiu  %.4f\n'%( sgiu ) ) 
log.write('\n') 

outfile=gROOT.FindObject(outname+'.root')
if outfile : outFile.Close()
outfile = TFile(outname+'.root','RECREATE','WI/TR Comparison Histograms')

for hname in histnames:
 pngname=path+"/"+runname+sample+"_"+hname+"_comparison"
 if ( fnm.fnmatch(hname,"*qcd*") ) :
  hdown = gfile.Get(hname+"_Tr")
  hdown.SetName(hname+"_QCDDown")
  hdown_size_inp = hdown.Integral(-1,-1)
  hdown_size_scl = hdown.Integral(-1,-1)
  hdown.Write()

  hup = tfile.Get(hname+"_Wi")
  hup.SetName(hname+"_QCDUp")
  hup_size_inp = hup.Integral(-1,-1)
  hup_size_scl = hup.Integral(-1,-1)
  hup.Write()

  hmed = hup.Clone()
  hmed.SetName( hname )
  hmed.Add( hdown.Clone() )
  hmed.Scale( 0.5 )
  hmed.SetLineColor(ROOT.kGreen)
  hmed_size_inp = hmed.Integral(-1,-1)
  hmed_size_scl = hmed.Integral(-1,-1)
  hmed.Write()

  leg=TLegend(0.58,0.7,0.78,0.88)
  leg.SetFillColor(0)
  leg.SetBorderSize(0)
  leg.AddEntry(hup,"Wisconsin")
  leg.AddEntry(hmed,"Average")
  leg.AddEntry(hdown,"Trieste")
 
  hup.GetXaxis().SetLabelSize(0.03)
  hup.GetYaxis().SetLabelSize(0.03)
  hup.GetYaxis().SetTitleOffset(1.5)
  hup.GetYaxis().SetTitle( "Events / %s GeV"%(hup.GetBinWidth(1)) )
  #hup.SetMaximum( 1.2 * hdown.GetMaximum() )
  hup.SetMaximum( 1.2 * 232.966809082031233 )
  hup.GetXaxis().SetTitle( "Transverse Mass, GeV" )
  hup.SetTitle( hname )
 
  hup.Draw("hist")
  hdown.Draw("hist,sames")
  hmed.Draw("hist,sames")
  leg.Draw('sames')
  time.sleep(1)
  c.Print(pngname+".png")

  log.write("  %s \n"%( hname )  )
  log.write("    \t  Wisconsin(up) Size Input %.2f   \t Output %.2f\n"%( hup_size_inp,hup_size_scl ) ) 
  log.write("    \t  Average   Size Input %.2f   \t Output %.2f\n"%( hmed_size_inp,hmed_size_scl ) ) 
  log.write("    \t  Trieste(down)   Size Input %.2f   \t Output %.2f\n"%( hdown_size_inp,hdown_size_scl ) ) 

 else:
  htom = tfile.Get(hname+"_Wi")
  htom.SetName(hname+"_Wi")
  htom_size_inp = htom.Integral(-1,-1)

  hgiu = gfile.Get(hname+"_Tr")
  hgiu.SetName(hname+"_Tr")
  hgiu_size_inp = hgiu.Integral(-1,-1)

  htom_size_scl = htom.Integral(-1,-1)
  htom_max = htom.GetMaximum()
  htom.SetFillColor(0)
  htom.SetLineColor(2)
  htom.SetLineWidth(3)
 
  hgiu_size_scl = hgiu.Integral(-1,-1)
  hgiu_max = hgiu.GetMaximum()
  hgiu.SetFillColor(0)
  hgiu.SetLineColor(1)
  hgiu.SetLineWidth(2)

  leg=TLegend(0.58,0.7,0.78,0.88)
  leg.SetFillColor(0)
  leg.SetBorderSize(0)
  leg.AddEntry(htom,"Wisconsin")
  leg.AddEntry(hgiu,"Trieste")

  htom.GetXaxis().SetLabelSize(0.03)
  htom.GetYaxis().SetLabelSize(0.03)
  htom.GetYaxis().SetTitleOffset(1.5)
  htom.GetYaxis().SetTitle( "Events / %s GeV"%(htom.GetBinWidth(1)) )
  htom.SetMaximum(1.2*max(htom_max,hgiu_max))
  htom.GetXaxis().SetTitle( "Transverse Mass, GeV" )
  htom.SetTitle( hname )

  htom.Draw("hist")
  hgiu.Draw("hist,sames")
  leg.Draw('sames')
  time.sleep(1)
  c.Print(pngname+".png")

  htom.SetName(hname+"_Wi")
  htom.Write()
  hgiu.SetName(hname+"_Tr")
  hgiu.Write()

  log.write("  %s \n"%( hname )  )
  log.write("    \t  Wisconsin Size Input %.2f   \t Output %.2f\n"%( htom_size_inp,htom_size_scl ) ) 
  log.write("    \t  Trieste   Size Input %.2f   \t Output %.2f\n"%( hgiu_size_inp,hgiu_size_scl ) ) 
log.close()
outfile.Close()


