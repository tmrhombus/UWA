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
logname=path+"/"+runname+infileT
outname=path+"/"+runname+infileT

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
"h_TTbar",
   qcd,
"h_Drell",
"h_T",
"h_VV",
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
 pngname=outname+"_"+hname

 if not (
  fnm.fnmatch(hname,"data_obs") or
  fnm.fnmatch(hname,"*qcd*") 
 ) :
  htom = tfile.Get(hname+"_Wi")
  htom.SetName(hname+"_Wi")
  htom_size_inp = htom.Integral(-1,-1)
  htom.Scale(stom)
 else:
  htom = tfile.Get(hname+"_Wi")
  htom.SetName(hname+"_Wi")
  htom_size_inp = htom.Integral(-1,-1)
 htom_size_scl = htom.Integral(-1,-1)
 htom_max = htom.GetMaximum()
 htom.SetFillColor(0)
 htom.SetLineColor(2)
 htom.SetLineWidth(3)

 if not (
  fnm.fnmatch(hname,"data_obs") or
  fnm.fnmatch(hname,"*qcd*") 
 ) :
  hgiu = tfile.Get(hname+"_Tr")
  hgiu.SetName(hname+"_Tr")
  hgiu_size_inp = hgiu.Integral(-1,-1)
  hgiu.Scale(sgiu)
 else:
  hgiu = tfile.Get(hname+"_Tr")
  hgiu.SetName(hname+"_Tr")
  hgiu_size_inp = hgiu.Integral(-1,-1)
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

# merge Wjets separately


flavors = ["4","5"]

for flavor in flavors:
 pngname=outname+"_Wjets%s"%(flavor)
 
 htom = tfile.Get("h_Wbb%sF_Wi"%(flavor))
 htom.SetName("h_Wjets%s_Wi"%(flavor))
 htom.Add( tfile.Get("h_Wcc_Wi").Clone() )
 htom.Add( tfile.Get("h_Wl_Wi").Clone() )
 htom.Scale( stom )
 htom_max = htom.GetMaximum()
 
 htom.SetFillColor(0)
 htom.SetLineColor(2)
 htom.SetLineWidth(3)
 
 htom_size_inp = htom.Integral(-1,-1)
 htom_size_scl = htom.Integral(-1,-1)
 
 hgiu = tfile.Get("h_Wbb4F_Tr")
 hgiu.SetName("h_Wjets%s_Tr"%(flavor))
 hgiu.Add( tfile.Get("h_Wcc_Tr").Clone() )
 hgiu.Add( tfile.Get("h_Wl_Tr").Clone() )
 hgiu.Scale( sgiu )
 hgiu_max = hgiu.GetMaximum()
 
 hgiu.SetFillColor(0)
 hgiu.SetLineColor(1)
 hgiu.SetLineWidth(3)
 
 hgiu_size_inp = hgiu.Integral(-1,-1)
 hgiu_size_scl = hgiu.Integral(-1,-1)
 
 #
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
 htom.SetTitle( "WJets (%sF Wbb)"%(flavor) )
 
 htom.Draw("hist")
 hgiu.Draw("hist,sames")
 leg.Draw('sames')
 time.sleep(1)
 c.Print(pngname+".png")
 
 htom.Write()
 hgiu.Write()
 
 log.write("  WJets %s \n"%( flavor )  )
 log.write("    \t  Wisconsin Size Input %.2f   \t Output %.2f\n"%( htom_size_inp,htom_size_scl ) ) 
 log.write("    \t  Trieste   Size Input %.2f   \t Output %.2f\n"%( hgiu_size_inp,hgiu_size_scl ) ) 


log.close()
outfile.Close()

