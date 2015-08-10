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
lep     = sys.argv[6]
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

 if (
  fnm.fnmatch(hname,"*qcd*") 
 ) :
  htom = tfile.Get(hname+"_Wi")
  htom.SetName(hname+"_"+lep+"_Wi")
  htom_size_inp = htom.Integral(-1,-1)

  hgiu = gfile.Get(hname+"_Tr")
  hgiu.SetName(hname+"_"+lep+"_Tr")
  hgiu_size_inp = hgiu.Integral(-1,-1)
 else:
  htom = tfile.Get(hname+"_Wi")
  htom.SetName(hname+"_Wi")
  htom_size_inp = htom.Integral(-1,-1)

  hgiu = tfile.Get(hname+"_Tr")
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

 htom.Write()
 hgiu.Write()

 log.write("  %s \n"%( hname )  )
 log.write("    \t  Wisconsin Size Input %.2f   \t Output %.2f\n"%( htom_size_inp,htom_size_scl ) ) 
 log.write("    \t  Trieste   Size Input %.2f   \t Output %.2f\n"%( hgiu_size_inp,hgiu_size_scl ) ) 
log.close()
outfile.Close()



#
#
#
#
#
#
#
##!/usr/bin/env python
#'''
#Dump a .png for evey histogram in file
#Author: T.M.Perry
#'''
#import ROOT
#from ROOT import TH1F,TFile,gROOT, TCanvas, TLegend, gStyle
#import sys 
#import fnmatch as fnm 
#
#infileG = sys.argv[1] 
#infileT = sys.argv[2]
#path    = sys.argv[3]
#runname = sys.argv[4] 
#sample  = sys.argv[5]
#logname=path+"/"+runname+sample+"_comparison"
#outname=path+"/"+runname+sample+"_comparison"
#
#qcd = "h_TTqcd"
#if ( sample=="wbb" ):
# qcd = "h_qcd"
#
#rebin = 1
#stom = 1
#sgiu = 1
#
#gStyle.SetOptStat('')
#gStyle.SetLineWidth(3)
#gStyle.SetPadTickY(1)
#
#gfile = TFile(path+"/"+infileG+".root")
#tfile = TFile(path+"/"+infileT+".root")
#
#canx = 900 
#cany = 900
#c = TCanvas('c','Canvas Named c',canx,cany)
#
#histnames = [
#"data_obs",
#   qcd,
#"h_Drell",
#"h_VV",
#"h_T",
#"h_TTbar",
#"h_Wl"
#"h_Wcc",
#"h_Wbb4F",
#"h_Wbb5F",
#]
#
#log = open(logname+'.log','w')
#log.write('\n\n') 
#log.write('  infileG %s \n'%( infileG ) )  
#log.write('  infileT %s \n'%( infileT ) ) 
#log.write('  path    %s \n'%( path    ) ) 
#log.write('  runname %s \n'%( runname ) ) 
#log.write('  sample  %s \n'%( sample  ) ) 
#
#outfile=gROOT.FindObject(outname+'.root')
#if outfile : outFile.Close()
#outfile = TFile(outname+'.root','RECREATE','WI/TR Comparison Histograms')
#
#for hname in histnames:
# pngname=path+"/"+runname+sample+"_"+hname+"_comparison"
#
# htom = tfile.Get(hname)
#
# htom.SetFillColor(0)
# htom.SetLineColor(2)
# htom.SetLineWidth(3)
# htom.Scale(stom)
# htom_size_inp = htom.Integral(1,-1)
# if ( nToOne and htom_size_inp>0.1 ) :
#  htom.Scale(1/htom_size_inp)
# if ( nToGiu ) :
#  htom.Scale( sf_nToGiu )
# htom_size_scl = htom.Integral(1,-1)
# htom_max = htom.GetMaximum()
#
# hgiu = gfile.Get(hname)
# hgiu.SetFillColor(0)
# hgiu.SetLineColor(1)
# hgiu.SetLineWidth(2)
# hgiu_size_inp = hgiu.Integral(1,-1)
# hgiu.Scale(sgiu)
# if ( fnm.fnmatch(hname,"h_*qcd") ):
#  hgiu.Scale( sf_qToTom )
# if ( nToOne and hgiu_size_inp>0.1 ) :
#  hgiu.Scale(1/hgiu_size_inp)
# hgiu_size_scl = hgiu.Integral(1,-1)
# hgiu_max = hgiu.GetMaximum()
#
# leg=TLegend(0.58,0.7,0.78,0.88)
# leg.SetFillColor(0)
# leg.SetBorderSize(0)
# leg.AddEntry(htom,"Wisconsin")
# leg.AddEntry(hgiu,"Trieste")
#
# htom.GetXaxis().SetLabelSize(0.03)
# htom.GetYaxis().SetLabelSize(0.03)
# htom.GetYaxis().SetTitleOffset(1.5)
# htom.GetYaxis().SetTitle( "Events / %s GeV"%(htom.GetBinWidth(1)) )
# htom.SetMaximum(1.2*max(htom_max,hgiu_max))
# htom.GetXaxis().SetTitle( "Transverse Mass, GeV" )
# htom.SetTitle( hname )
#
# htom.Draw("hist")
# hgiu.Draw("hist,sames")
# leg.Draw('sames')
# c.Print(pngname+".png")
#
# htom.SetName(hname+"_Wi")
# htom.Write()
# hgiu.SetName(hname+"_Tr")
# hgiu.Write()
#
# log.write("  %s \n"%( hname )  )
# log.write("    \t  Wisconsin Size Input %.2f   \t Output %.2f\n"%( htom_size_inp,htom_size_scl ) ) 
# log.write("    \t  Trieste   Size Input %.2f   \t Output %.2f\n"%( hgiu_size_inp,hgiu_size_scl ) ) 
#log.close()
#outfile.Close()
#
#
#
#
#
###!/usr/bin/env python
##'''
##Rebin histograms for 8TeV datacards 
##Author: T.M.Perry
##'''
##import ROOT
##from ROOT import TH1F,TFile,gROOT
##import sys 
##import fnmatch as fnm 
##
##
##infileG = sys.argv[1] 
##infileT = sys.argv[2]
##path    = sys.argv[3]
##runname = sys.argv[4] 
##sample  = sys.argv[5]
##nToOne = False
##nToGiu = True
##logname=path+"/"+runname+sample+"_comparison"
##outname=path+"/"+runname+sample+"_comparison"
##
##inFile = TFile(inFileName+".root")
##
##outFile=gROOT.FindObject(prefix+inFileName+".root")
##if outFile : outFile.Close()
##outFile = TFile(prefix+inFileName+".root",'RECREATE','rebinned')
##
##for key in inFile.GetListOfKeys():
## obj = key.ReadObj()
## if(obj.IsA().InheritsFrom("TH1")):
##  h_name = obj.GetName()
##  h_new = obj.Clone()
##  if(fnm.fnmatch(h_name,"data_obs") or fnm.fnmatch(h_name,"*qcd*")): 
##   outFile.cd()
##   h_new.Write()
##  elif(fnm.fnmatch(h_name,"*_*_*") and not fnm.fnmatch(h_name,"*JES*")):
##   outFile.cd()
##   h_new.Write()
##  elif(not fnm.fnmatch(h_name,"*_*_*")):
##   print("  Rescaling JES for: "+h_name)
##   h_down = h_new 
##   h_down.SetName(h_name+"_JESDown")
##   h_norm = inFile.Get(h_name+"_JESUp")
##   h_norm.SetName(h_name)
## 
##   h_diff = h_norm.Clone()
##   h_diff.Add(h_down,-1)
## 
##   h_up = h_norm.Clone()
##   h_up.Add(h_diff)
##   h_up.SetName(h_name+"_JESUp")
## 
##   outFile.cd()
##   h_down.Write()
##   h_norm.Write()
##   h_up.Write()
