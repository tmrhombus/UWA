#!/usr/bin/env python
'''
Makes nice plots with ratio from histograms made using makeHistos.py
Author: T.M.Perry UW
'''
import ROOT
from ROOT import THStack,TH1F,TFile
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
from ROOT import gROOT,gStyle
import sys
import cmsPrelim as cpr
import time

wflav = sys.argv[1]
ttsample = sys.argv[2]
lep = sys.argv[4]
version = sys.argv[5]
runname = sys.argv[6]
loc = sys.argv[7]
sample = sys.argv[8]
where = './allFits/%s'%(version)

#print("./allFits/%s/%s.root"%(version,sys.argv[3]))
dataFile_tt  = TFile("./allFits/%s/%s.root"%(version,sys.argv[3]))
theFile  = TFile("./allFits/%s/mlfit_%s_full_h_Wjets%s_%s_%s%s.root"%(version,runname,wflav,ttsample,lep,loc))
biasFile = TFile("./allFits/%s/mlfit_%s_full_h_Wjets%s_%s_%s%s_fitbias.root"%(version,runname,wflav,ttsample,lep,loc))

ratioRange = 0.3
errorBand = True
#canvas attributes
canx = 900 
cany = 1200

#color scheme
c_data = 1
c_qcd =   ROOT.EColor.kRed+1
c_z =   ROOT.EColor.kOrange-3
c_vv =   ROOT.EColor.kYellow-3
c_t =  ROOT.EColor.kGreen+1
c_tb =  ROOT.EColor.kGreen-5
c_ttb = ROOT.EColor.kGreen-9
c_wl =  ROOT.EColor.kAzure+10
c_wc =  ROOT.EColor.kBlue+0
c_wcc = ROOT.EColor.kBlue-9
c_wbb = 51

fillStyle = 1
fillStyleTTs = 1
fillStyleTTf = 1

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')
gStyle.SetLineWidth(3)
gStyle.SetPadTickY(1)

#
title = "Transverse Mass"
xlabel = "Transverse Mass [GeV]"

# rebin factor
rebin = 1

# scale factors ... careful 
sf_qcd = 1.  
sf_z = 1.   
sf_vv = 1.  
sf_t = 1.  
sf_tb = 1.  
sf_ttb = 1. 
sf_wl = 1.  
sf_wc = 1.  
sf_wcc = 1. 
sf_wbb = 1.

shapes = ["shapes_prefit","shapes_fit_s"]
#samples = ["UUbb",]
#samples = ["TTbr",]
#samples = ["TTbr","UUbb"]
I = -1
F = -1

fit_s = theFile.Get("fit_s")
fpf_s = fit_s.floatParsFinal()
nuis_s = fpf_s.find('r')
r = nuis_s.getVal()
r_error = nuis_s.getError()

bias_s = biasFile.Get("fit_s")
bpf_s = bias_s.floatParsFinal()
b_bias_s = bpf_s.find('r')
bias = b_bias_s.getVal()
bias_error = b_bias_s.getError()

sizes_wbb_prefit = []
sizes_wbb_part_prefit = []
sizes_tt_prefit = []
sizes_tt_part_prefit = []
sizes_wbb_fitted = []
sizes_wbb_part_fitted = []
sizes_tt_fitted = []
sizes_tt_part_fitted = []

sample_names = []

for shape in shapes:
 c = TCanvas('c','Canvas Named c',canx,cany)
 c.cd()
 p1 = TPad('p1','p1',0,0.25,1,1)
 p1.SetBottomMargin(0.04)
 p1.Draw()
 p1.SetLogy(0)
 p1.SetFrameLineWidth(2)
 c.cd()
 p2 = TPad('p2','p2',0,0,1,0.25)
 p2.SetTopMargin(0.02)
 p2.SetBottomMargin(0.3)
 p2.SetFrameLineWidth(2)
 p2.Draw()

 c.cd()
 p1.cd()
 if shape=="shapes_fit_s": shp = "Fitted"
 if shape=="shapes_prefit": shp = "PreFit"
 if sample=="TTbar" or sample=="TTbr":
  smp="TTbar"

 data_obs = dataFile_tt.Get("data_obs")
 data_obs.Rebin( rebin )
 data_obs.SetMarkerStyle(22)
 data_obs.SetMarkerSize(1.2)
 data_obs.SetMarkerSize(2)
 data_obs.SetTitle("")
 data_obs.Draw()
 if sample=="TTbr":
  tt_dh_size = data_obs.Integral()
  tt_dh_size_part = data_obs.Integral(I,F)
 if sample=="UUbb":
  wbb_dh_size = data_obs.Integral()
  wbb_dh_size_part = data_obs.Integral(I,F)
 max_data = data_obs.GetMaximum()
 
 h_TTbar = theFile.Get("%s/%s/h_TTbar%s"%(shape,sample,loc))
 h_TTbar.SetFillColor( c_ttb )
 h_TTbar.SetFillStyle( fillStyleTTf )
 h_TTbar.Rebin( rebin )
 h_TTbar.Scale( sf_ttb )
 h_TTbar.Draw("GOFF")
 if (shp=="PreFit" and sample=="UUbb"):
  sizes_wbb_prefit.append(
   h_TTbar.Integral() )
  sizes_wbb_part_prefit.append(
   h_TTbar.Integral(I,F) )
 elif (shp=="PreFit" and sample=="TTbr"): 
  sizes_tt_prefit.append(
   h_TTbar.Integral() )
  sizes_tt_part_prefit.append(
   h_TTbar.Integral(I,F) )
  TTbar_prefit_size = h_TTbar.Integral()
 elif (shp=="Fitted" and sample=="UUbb"):
  sizes_wbb_fitted.append(
   h_TTbar.Integral() )
  sizes_wbb_part_fitted.append(
   h_TTbar.Integral(I,F) )
 elif (shp=="Fitted" and sample=="TTbr"): 
  sizes_tt_fitted.append(
   h_TTbar.Integral() )
  sizes_tt_part_fitted.append(
   h_TTbar.Integral(I,F) )
  TTbar_fitted_size = h_TTbar.Integral()
 sample_names.append("TTbar   ")

 if sample=="UUbb": 
  h_qcd = theFile.Get("%s/%s/h_qcd%s"%(shape,sample,loc))
 if sample=="TTbr": 
  h_qcd = theFile.Get("%s/%s/h_TTqcd%s"%(shape,sample,loc))
 h_qcd.SetName("h_qcd")
 h_qcd.SetFillColor( c_qcd )
 h_qcd.SetFillStyle( fillStyle )
 h_qcd.Rebin( rebin )
 h_qcd.Scale( sf_qcd )
 h_qcd.Draw("GOFF")
 if (shp=="PreFit" and sample=="UUbb"):
  sizes_wbb_prefit.append(h_qcd.Integral())
  sizes_wbb_part_prefit.append(h_qcd.Integral(I,F))
 elif (shp=="PreFit" and sample=="TTbr"): 
  sizes_tt_prefit.append(h_qcd.Integral())
  sizes_tt_part_prefit.append(h_qcd.Integral(I,F))
 elif (shp=="Fitted" and sample=="UUbb"):
  sizes_wbb_fitted.append(h_qcd.Integral())
  sizes_wbb_part_fitted.append(h_qcd.Integral(I,F))
 elif (shp=="Fitted" and sample=="TTbr"): 
  sizes_tt_fitted.append(h_qcd.Integral())
  sizes_tt_part_fitted.append(h_qcd.Integral(I,F))
 sample_names.append("QCD     ")

 h_Drell = theFile.Get("%s/%s/h_Drell%s"%(shape,sample,loc))
 h_Drell.SetFillColor( c_z )
 h_Drell.Rebin( rebin )
 h_Drell.Scale( sf_z )
 h_Drell.Draw("GOFF")
 if (shp=="PreFit" and sample=="UUbb"):
  sizes_wbb_prefit.append(h_Drell.Integral())
  sizes_wbb_part_prefit.append(h_Drell.Integral(I,F))
 elif (shp=="PreFit" and sample=="TTbr"): 
  sizes_tt_prefit.append(h_Drell.Integral())
  sizes_tt_part_prefit.append(h_Drell.Integral(I,F))
 elif (shp=="Fitted" and sample=="UUbb"):
  sizes_wbb_fitted.append(h_Drell.Integral())
  sizes_wbb_part_fitted.append(h_Drell.Integral(I,F))
 elif (shp=="Fitted" and sample=="TTbr"): 
  sizes_tt_fitted.append(h_Drell.Integral())
  sizes_tt_part_fitted.append(h_Drell.Integral(I,F))
 sample_names.append("Drell   ")
 
 h_T = theFile.Get("%s/%s/h_T%s"%(shape,sample,loc))
 h_T.SetFillColor( c_t )
 h_T.SetFillStyle( fillStyle )
 h_T.Rebin( rebin )
 h_T.Scale( sf_t )
 h_T.Draw("GOFF")
 if (shp=="PreFit" and sample=="UUbb"):
  sizes_wbb_prefit.append( 
   h_T.Integral() )
  sizes_wbb_part_prefit.append( 
   h_T.Integral(I,F) )
 elif (shp=="PreFit" and sample=="TTbr"): 
  sizes_tt_prefit.append(
   h_T.Integral() )
  sizes_tt_part_prefit.append(
   h_T.Integral(I,F) )
 elif (shp=="Fitted" and sample=="UUbb"):
  sizes_wbb_fitted.append(
   h_T.Integral() )
  sizes_wbb_part_fitted.append(
   h_T.Integral(I,F) )
 elif (shp=="Fitted" and sample=="TTbr"): 
  sizes_tt_fitted.append(
   h_T.Integral() )
  sizes_tt_part_fitted.append(
   h_T.Integral(I,F) )
 sample_names.append("Single T")
 
 h_VV = theFile.Get("%s/%s/h_VV%s"%(shape,sample,loc))
 h_VV.SetFillColor( c_vv )
 h_VV.SetFillStyle( fillStyle )
 h_VV.Rebin( rebin )
 h_VV.Scale( sf_vv )
 h_VV.Draw("GOFF")
 if (shp=="PreFit" and sample=="UUbb"):
  sizes_wbb_prefit.append( h_VV.Integral() )
  sizes_wbb_part_prefit.append( h_VV.Integral(I,F) )
 elif (shp=="PreFit" and sample=="TTbr"): 
  sizes_tt_prefit.append( h_VV.Integral() )
  sizes_tt_part_prefit.append( h_VV.Integral(I,F) )
 elif (shp=="Fitted" and sample=="UUbb"):
  sizes_wbb_fitted.append( h_VV.Integral() )
  sizes_wbb_part_fitted.append( h_VV.Integral(I,F) )
 elif (shp=="Fitted" and sample=="TTbr"): 
  sizes_tt_fitted.append( h_VV.Integral() )
  sizes_tt_part_fitted.append( h_VV.Integral(I,F) )
 sample_names.append("Diboson ")
 
 h_Wjets = theFile.Get("%s/%s/h_Wjets%s%s"%(shape,sample,wflav,loc))
 h_Wjets.SetName("h_Wjets")
 h_Wjets.SetFillColor( c_wbb )
 h_Wjets.SetFillStyle( fillStyle )
 h_Wjets.Rebin( rebin )
 h_Wjets.Scale( sf_wbb )
 h_Wjets.Draw("GOFF")
 if (shp=="PreFit" and sample=="UUbb"):
  sizes_wbb_prefit.append(h_Wjets.Integral())
  sizes_wbb_part_prefit.append(h_Wjets.Integral(I,F))
  Wbb_prefit_size = h_Wjets.Integral()
 elif (shp=="PreFit" and sample=="TTbr"): 
  sizes_tt_prefit.append(h_Wjets.Integral())
  sizes_tt_part_prefit.append(h_Wjets.Integral(I,F))
 elif (shp=="Fitted" and sample=="UUbb"):
  sizes_wbb_fitted.append(h_Wjets.Integral())
  sizes_wbb_part_fitted.append(h_Wjets.Integral(I,F))
  Wbb_fitted_size = h_Wjets.Integral()
 elif (shp=="Fitted" and sample=="TTbr"): 
  sizes_tt_fitted.append(h_Wjets.Integral())
  sizes_tt_part_fitted.append(h_Wjets.Integral(I,F))
 sample_names.append("W+bb    ")
 
 
 sample_names.append("Total MC")
 # make a stack to draw with
 s_mc = THStack('hs','')
 s_mc.SetTitle('')
 s_mc.Add(h_qcd)
 s_mc.Add(h_Drell)
 s_mc.Add(h_VV)
 s_mc.Add(h_T)
 s_mc.Add(h_TTbar)
 s_mc.Add(h_Wjets)
 s_mc.Draw("GOFF")
 max_mc = s_mc.GetMaximum()
 
 # add all MC for ratio plot
 h_mc = h_qcd.Clone()
 h_mc.SetName("h_mc")
 h_mc.Add(h_Drell)
 h_mc.Add(h_VV)
 h_mc.Add(h_T)
 h_mc.Add(h_TTbar)
 h_mc.Add(h_Wjets)
 if errorBand:
  h_mc_err = h_mc.Clone()
  h_mc_err.SetName('h_mc_err')
  h_mc_err.SetFillColor(ROOT.EColor.kBlue-6)
  h_mc_err.SetFillStyle(3001)
 # make ratio plot
 h_r = data_obs.Clone()
 h_r.SetName("h_r")
 #print(h_r.GetNbinsX())
 #print(h_mc.GetNbinsX())
 h_r.Divide(h_mc)
 if errorBand:
  h_r_err = h_mc.Clone()
  h_r_err.SetName("h_r_err")
  h_r_err.SetFillColor(ROOT.EColor.kBlue-6)
  h_r_err.SetFillStyle(3001)
  h_r_errDivisor = h_mc.Clone()
  for i in range( h_r_err.GetNbinsX() + 1 ):
   h_r_errDivisor.SetBinError( i, 0 )
  h_r_err.Divide(h_r_errDivisor)
 
 # set p1 title and axis labels
 s_mc.GetXaxis().SetLabelSize(0.03)
 s_mc.GetYaxis().SetLabelSize(0.03)
 s_mc.GetYaxis().SetTitleOffset(1.5)
 for i in range(1,h_mc.GetNbinsX()+1):
  s_mc.GetXaxis().SetBinLabel(i,"%s"%(i*8) )
 s_mc.GetYaxis().SetTitle( "Events / 8 GeV" )
 the_max = max( max_mc,max_data )
 #if ttsample=="ttme":   s_mc.SetMaximum( 130 )
 #if ttsample=="ttjjj":  s_mc.SetMaximum( 2000 )
 s_mc.SetMaximum( 900 )
 #s_mc.SetMaximum( 1.1*the_max )
 
 # set p2 y ranges
 h_r.GetYaxis().SetRangeUser(1.-ratioRange,1+ratioRange)
 h_r.GetYaxis().SetLabelSize(0.10)
 h_r.GetXaxis().SetLabelSize(0.10)
 h_r.GetYaxis().SetTitleSize(0.10)
 h_r.GetXaxis().SetTitleSize(0.10)
 h_r.GetYaxis().SetTitle("Data / MC")
 h_r.GetYaxis().SetTitleOffset(0.5)
 h_r.GetXaxis().SetTitle( xlabel )
 for i in range(1,h_r.GetNbinsX()+1):
  h_r.GetXaxis().SetBinLabel(i,"%s"%(i*8) )
 
 # fill legend
 leg=TLegend(0.68,0.3,0.88,0.88)
 leg.AddEntry(data_obs,"Data")
 leg.AddEntry(h_Wjets,"W+jets","f")
 leg.AddEntry(h_TTbar,"t#bar{t}","f")
 leg.AddEntry(h_T,"Single T","f")
 leg.AddEntry(h_VV,"Diboson","f")
 leg.AddEntry(h_Drell,"Drell-Yan","f")
 leg.AddEntry(h_qcd,"QCD","f")
 leg.SetFillColor(0)
 leg.SetBorderSize(0)
 
 # and draw
 c.cd()
 p1.cd()
 s_mc.Draw('hist,GOFF')
 if errorBand: h_mc_err.Draw('sames,E2,GOFF')
 data_obs.Draw('sames,E1,GOFF')
 leg.Draw('sames,GOF')
 
 cpr.prelim_alt(19700,0.05)
 tex.SetTextAlign(11) #left, bottom
 tex.DrawLatex(0.1,0.9,title)
 
 c.cd()
 p2.cd() 
 h_r.Draw("ep,GOFF")
 if errorBand: h_r_err.Draw("sames,E2,GOFF")
 
 l = TLine(h_r.GetXaxis().GetXmin(),1,h_r.GetXaxis().GetXmax(),1)
 l.SetLineStyle(3)
 l.Draw("GOFF")
 c.Update()
 time.sleep(1)
 
 c.Print(where+"/Wjets%s_%s_%s_%s_%s_%s%s.png"%(wflav,ttsample,sample,shp,lep,runname,loc))
 print(  where+"/Wjets%s_%s_%s_%s_%s_%s%s.png"%(wflav,ttsample,sample,shp,lep,runname,loc))
 c.Clear()

sizes_wbb_prefit.append(sum(sizes_wbb_prefit))
sizes_wbb_part_prefit.append(sum(sizes_wbb_prefit))
sizes_tt_prefit.append(sum(sizes_tt_prefit))
sizes_tt_part_prefit.append(sum(sizes_tt_prefit))
sizes_wbb_fitted.append(sum(sizes_wbb_fitted))
sizes_wbb_part_fitted.append(sum(sizes_wbb_part_fitted))
sizes_tt_fitted.append(sum(sizes_tt_fitted))
sizes_tt_part_fitted.append(sum(sizes_tt_part_fitted))


#
isTT = False
if sample=="TTbr": isTT=True
if ttsample=="ttme":
 ttname = "multi-lepton"
if ttsample=="ttjjj":
 ttname = "multi-jet"

if isTT:
 tt_dratio = tt_dh_size / sizes_tt_fitted[-1]
 tt_dratio_part = tt_dh_size_part / sizes_tt_part_fitted[-1]
 log = open(where+"/Wjets%s_%s_%s%s.tex"%(wflav,ttsample,lep,loc),'w')
 #log.write("\documentclass{article}\n")
 log.write("\documentclass{standalone}\n")
 #log.write("\input{/Users/rhombus/Documents/Madison/Latex/style}\n")
 log.write("\\begin{document}\n\n")
 log.write("\\begin{tabular}{r|l|l|l|l|l|l}\n")
 log.write("$W+b\\bar{b}$ %s & \multicolumn{6}{c}{Fit Result: r = %.3f $\pm$ %.3f}\\\\ \n"%(wflav,r,r_error))
 log.write("in $t\\bar{t}$-%s & \multicolumn{6}{c}{Fit Bias: %.4f $\pm$ %.3f}\\\\ \n"%(ttname,bias,bias_error))
 log.write('$t\\bar{t}$-%s & \multicolumn{3}{c|}{Integral()} & \multicolumn{3}{c}{Integral(-1,-1)}\\\\ \n'%(ttname))
 log.write('{} & PreFit & PostFit & Ratio & PreFit & PostFit & Ratio \\\\ \hline \n')
 for i,j,k,l,m in zip(sample_names,sizes_tt_prefit,sizes_tt_fitted,sizes_tt_part_prefit,sizes_tt_part_fitted):
  log.write('%s  & %i\t & %i\t & %.4f\t& %i\t  & %i\t & %i\\\\ \n'%(i,j,k,k/j,l,m,m/l))
  #log.write('%s  & %.2f\t & %.2f\t & %.2f\t & %.2f\t & %.2f\t & %.2f\\\\ \n'%(i,j,k,k/j,l,m,m/l))
 log.write('\hline \hline \n')
 log.write('Data & \multicolumn{2}{c}{%s} & %.3f & \multicolumn{2}{c}{%s} & %.3f \n'%(tt_dh_size,tt_dratio,tt_dh_size_part,tt_dratio_part))
 log.write("\\end{tabular}\\\n")
 log.write("\end{document}")
 log.close()

 logb = open(where+"/Wjets%s_%s_%s%s_b.tex"%(wflav,ttsample,lep,loc),'w')

 #logb.write('Data      %i\t%i\n\n\n'%(tt_dh_size,tt_dh_size))
 logb.write('%i\t%i\n\n\n'%(tt_dh_size,tt_dh_size))
 #for i,j,k in zip(sample_names,sizes_tt_prefit,sizes_tt_fitted):
 # logb.write('%s  %i\t%i \n\n\n'%(i,j,k))
 for i,j in zip(sizes_tt_prefit,sizes_tt_fitted):
  logb.write('%i\t%i \n\n\n'%(i,j))
  #logb.write('%s  %i\t%i\t%.4f \n\n\n'%(i,j,k,k/j))
 logb.write("\t%.3f(%.3f) %.3f\n"%(r,r_error,TTbar_fitted_size/TTbar_prefit_size))
 #logb.write("          \t%.3f(%.3f) %.3f\n"%(r,r_error,TTbar_fitted_size/TTbar_prefit_size))


 logb.close()


else:
 wbb_dratio = wbb_dh_size / sizes_wbb_fitted[-1]
 wbb_dratio_part = wbb_dh_size_part / sizes_wbb_part_fitted[-1]
 log = open(where+"/Wjets%s_%s_%s%s.tex"%(wflav,ttsample,lep,loc),'w')
 #log.write("\documentclass{article}\n")
 log.write("\documentclass{standalone}\n")
 #log.write("\input{/Users/rhombus/Documents/Madison/Latex/style}\n")
 log.write("\\begin{document}\n\n")
 log.write("\\begin{tabular}{r|l|l|l|l|l|l}\n")
 log.write("$W+b\\bar{b}$ %s & \multicolumn{6}{c}{Fit Result: r = %.3f $\pm$ %.3f}\\\\ \n"%(wflav,r,r_error))
 log.write("in $t\\bar{t}$-%s & \multicolumn{6}{c}{Fit Bias: %.4f $\pm$ %.3f}\\\\ \n"%(ttname,bias,bias_error))
 log.write('$t\\bar{t}$-%s & \multicolumn{3}{c|}{Integral()} & \multicolumn{3}{c}{Integral(-1,-1)}\\\\ \n'%(ttname))
 log.write('{} & PreFit & PostFit & Ratio & PreFit & PostFit & Ratio \\\\ \hline \n')
 #for i,j,k,l,m in zip(sample_names,sizes_tt_prefit,sizes_tt_fitted,sizes_tt_part_prefit,sizes_tt_part_fitted):
 for i,j,k,l,m in zip(sample_names,sizes_wbb_prefit,sizes_wbb_fitted,sizes_wbb_part_prefit,sizes_wbb_part_fitted):
  #log.write('%s  & %i\t & %i\t & %i\t & %i\t & %i\t & %i\\\\ \n'%(i,j,k,k/j,l,m,m/l))
  log.write('%s  & %.2f\t & %.2f\t & %.2f\t & %.2f\t & %.2f\t & %.2f\\\\ \n'%(i,j,k,k/j,l,m,m/l))
 log.write('\hline \hline \n')
 log.write('Data & \multicolumn{2}{c}{%s} & %.3f & \multicolumn{2}{c}{%s} & %.3f \n'%(wbb_dh_size,wbb_dratio,wbb_dh_size_part,wbb_dratio_part))
 #log.write('Data & \multicolumn{2}{c}{%s} & %.3f & \multicolumn{2}{c}{%s} & %.3f \n'%(tt_dh_size,tt_dratio,tt_dh_size_part,tt_dratio_part))
 log.write("\\end{tabular}\\\n")
 log.write("\end{document}")
 log.close()

 logb = open(where+"/Wjets%s_%s_%s%s_b.tex"%(wflav,ttsample,lep,loc),'w')

 #logb.write('Data      %i\t%i\n\n\n'%(tt_dh_size,tt_dh_size))
 logb.write('%i\t%i\n\n\n'%(wbb_dh_size,wbb_dh_size))
 #for i,j,k in zip(sample_names,sizes_tt_prefit,sizes_tt_fitted):
 # logb.write('%s  %i\t%i \n\n\n'%(i,j,k))
 for i,j in zip(sizes_wbb_prefit,sizes_wbb_fitted):
  logb.write('%i\t%i \n\n\n'%(i,j))
  #logb.write('%s  %i\t%i\t%.4f \n\n\n'%(i,j,k,k/j))
 logb.write("\t%.3f(%.3f) %.3f\n"%(r,r_error,Wbb_fitted_size/Wbb_prefit_size))
 #logb.write("          \t%.3f(%.3f) %.3f\n"%(r,r_error,TTbar_fitted_size/TTbar_prefit_size))


 logb.close()

