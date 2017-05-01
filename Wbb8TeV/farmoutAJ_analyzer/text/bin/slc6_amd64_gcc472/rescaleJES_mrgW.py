#!/usr/bin/env python
'''
Dump a .png for evey histogram in file
Author: T.M.Perry
'''
import ROOT
from ROOT import TH1F,TFile,gROOT, TCanvas, TLegend, gStyle
import sys 
import fnmatch as fnm 

infileG = sys.argv[1] 
infileT = sys.argv[2]
path    = sys.argv[3]
runname = sys.argv[4] 
sample  = sys.argv[5]
stom    = float(sys.argv[6])
sgiu    = float(sys.argv[7])
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
"h_Wjets4",
"h_Wjets5",
]

if sample=="wbb":
 sf_samples = [
 0.00,           #"data_obs",
 0.9459 - 1,     #"h_TTbar",
 0.0,            #   qcd,
 0.9818 - 1,     #"h_Drell",
 0.9599 - 1,     #"h_T",
 0.9857 - 1,     #"h_VV",
 0.9848 - 1,     #"h_Wbb4F",
 0.9848 - 1,     #"h_Wbb5F",
 ]

if sample=="ttme":
 sf_samples = [
 0.0,            #"data_obs",
 0.9742 - 1,     #"h_TTbar",
 0.0,            #   qcd,
 0.0,            #"h_Drell",
 1.0210 - 1,     #"h_T",
 0.0,            #"h_VV",
 0.0,            #"h_Wbb4F",
 0.0,            #"h_Wbb5F",
 ]

if sample=="ttjjj":
 sf_samples = [
 0.0,            #"data_obs",
 0.9892 - 1,     #"h_TTbar",
 0.0,            #   qcd,
 0.9995 - 1,     #"h_Drell",
 0.00761829051,  #"h_T",
 0.03187113153,  #"h_VV",
 0.03648462248,  #"h_Wbb4F",
 0.03648462248,  #"h_Wbb5F",
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

for hname,sf_sample in zip(histnames,sf_samples):
 pngname=path+"/"+runname+sample+"_"+hname+"_comparison"

 sf_tom = 1 + stom * sf_sample
 sf_giu = 1 + sgiu * sf_sample

 if not (
  fnm.fnmatch(hname,"data_obs") or
  fnm.fnmatch(hname,"*qcd*") 
 ) :
  htom_Down = tfile.Get(hname+"_Wi")
  htom_Down.SetName(hname+"_Wi_CSVDown")
  htom_size_inp = htom_Down.Integral(-1,-1)
  htom = htom_Down.Clone()
  htom.SetName(hname+"_Wi")
  htom.Scale(sf_tom)
  htdf = htom.Clone()
  htdf.Add(htom_Down,-1)
  htom_Up = htom_Down.Clone()
  htom_Up.SetName(hname+"_Wi_CSVUp")
  htom_Up.Add(htdf,2)
  htom_Up.Write()
  htom_Down.Write()
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
  hgiu_Down = tfile.Get(hname+"_Tr")
  hgiu_Down.SetName(hname+"_Tr_CSVDown")
  hgiu_size_inp = hgiu_Down.Integral(-1,-1)
  hgiu = hgiu_Down.Clone()
  hgiu.SetName(hname+"_Tr")
  hgiu.Scale(sf_giu)
  htdf = hgiu.Clone()
  htdf.Add(hgiu_Down,-1)
  hgiu_Up = hgiu_Down.Clone()
  hgiu_Up.SetName(hname+"_Tr_CSVUp")
  hgiu_Up.Add(htdf,2)
  hgiu_Up.Write()
  hgiu_Down.Write()
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


