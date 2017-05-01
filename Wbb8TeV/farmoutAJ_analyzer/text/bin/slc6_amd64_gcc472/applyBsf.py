#!/usr/bin/env python
'''
Dump a .png for evey histogram in file
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT, TCanvas, TLegend, gStyle
import sys 
import fnmatch as fnm 
import math

infileG = sys.argv[1] 
infileT = sys.argv[2]
path    = sys.argv[3]
runname = sys.argv[4] 
sample  = sys.argv[5]
stom    = float(sys.argv[6])
sgiu    = float(sys.argv[7])
bsf_T   = sys.argv[6]
bsf_G   = sys.argv[7]
nToOne = False
nToGiu = True
logname=path+"/"+runname+sample+"_comparison"
outname=path+"/"+runname+sample+"_comparison"

qcd = "h_TTqcd"
if ( sample=="wbb" ):
 qcd = "h_qcd"

rebin = 1
#stom = 1
#sgiu = 1

gStyle.SetOptStat('')
gStyle.SetLineWidth(3)
gStyle.SetPadTickY(1)

gfile = TFile(infileG+".root")
tfile = TFile(infileT+".root")

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
log.write('  nToOne  %s \n'%( nToOne  ) ) 

tfile.Get("data_obs").Draw("hist")
sf_nToGiu = gfile.Get("data_obs").Integral(-1,-1) / tfile.Get("data_obs").Integral(-1,-1) 
sf_qToTom = tfile.Get( qcd ).Integral(-1,-1) / gfile.Get( qcd ).Integral(-1,-1) 
log.write('  nToGiu  %s   %.4f\n'%( nToGiu,sf_nToGiu ) ) 
log.write('  qToTom  %.4f\n'%( sf_qToTom ) ) 
log.write('  bsfTom  %.4f\n'%( stom ) ) 
log.write('  bsfGiu  %.4f\n'%( sgiu ) ) 
log.write('\n') 

outfile=gROOT.FindObject(outname+'.root')
if outfile : outFile.Close()
outfile = TFile(outname+'.root','RECREATE','WI/TR Comparison Histograms')

for hname in histnames:
 pngname=path+"/"+runname+sample+"_"+hname+"_comparison"

 htom = tfile.Get(hname)

 htom.SetFillColor(0)
 htom.SetLineColor(2)
 htom.SetLineWidth(3)
 htom_size_inp = htom.Integral(-1,-1)
 if (
  fnm.fnmatch(hname,"h_Wbb*") or
  fnm.fnmatch(hname,"h_TTbar*")
 ) : htom.Scale(stom)
 elif (
  fnm.fnmatch(hname,"h_T*")
 ) : htom.Scale(math.sqrt(stom))
 if ( nToOne and htom_size_inp>0.1 ) :
  htom.Scale(1/htom_size_inp)
 if ( nToGiu ) :
  htom.Scale( sf_nToGiu )
 htom_size_scl = htom.Integral(-1,-1)
 htom_max = htom.GetMaximum()

 hgiu = gfile.Get(hname)
 hgiu.SetFillColor(0)
 hgiu.SetLineColor(1)
 hgiu.SetLineWidth(2)
 hgiu_size_inp = hgiu.Integral(-1,-1)
 if (
  fnm.fnmatch(hname,"h_Wbb*") or
  fnm.fnmatch(hname,"h_TTbar*")
 ) : hgiu.Scale(sgiu)
 elif (
  fnm.fnmatch(hname,"h_T*")
 ) : hgiu.Scale(math.sqrt(sgiu))
 if ( fnm.fnmatch(hname,"h_*qcd") ):
  hgiu.Scale( sf_qToTom )
 if ( nToOne and hgiu_size_inp>0.1 ) :
  hgiu.Scale(1/hgiu_size_inp)
 hgiu_size_scl = hgiu.Integral(-1,-1)
 hgiu_max = hgiu.GetMaximum()

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
