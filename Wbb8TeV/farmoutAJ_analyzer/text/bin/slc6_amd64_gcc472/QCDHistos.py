#!/usr/bin/env python
'''
 Merges histograms from the output of
 callHistoFiller.cc into one file
 Author: T.M.Perry UW-Madison
'''
import ROOT
from ROOT import TH1F,THStack,TFile,gROOT,gStyle
from ROOT import TLegend,TCanvas,TPad,TLatex,TLine
import fnmatch as fnm
import cmsPrelim as cpr

version="CestPiVV"
runname="vvQCDa"
#runname="diboson"
#runname="vvWbbQCD"
#runname="typical"

#version="Valentine"
#runname="avecDY"
#version="VVCheckExtended"
#runname="vvCheck"
#runname="fullCnob"

in_path = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Analyzed_%s/'%(version,runname)
out_path = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s/'%(version,runname)

leps = ['mu','ele']
cuts = ['wjj']
#cuts = ['wbb', 'ttme', 'ttjjj', 'wjj', 'stt', 'dyjj', 'dybb']
variables = [ 
 #"goodJ1_pt",
 "mt",
]

rebin = 1
#canvas size
canx = 1200 
cany = 900

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

tex = ROOT.TLatex()
tex.SetTextSize(0.07)
tex.SetTextAlign(13)
tex.SetNDC(True)
gStyle.SetOptStat('')
gStyle.SetLineWidth(3)
gStyle.SetPadTickY(1)

mc_samples = [
 "Drell",
 "TTbar_full", 
 "TTbar_semi", 
 "T_s", 
 "T_t", 
 "T_tW", 
 "Tbar_s", 
 "Tbar_t", 
 "Tbar_tW", 
 "W1Jet",
 "W2Jet",
 "W3Jet",
 "W4Jet",
 "WJets",
 "Wbb4F", 
 "WW", 
 "WZ", 
 "ZZ" 
]
for lep in leps:
 for variable in variables: 
  for cut in cuts:
   print("%s, %s, %s"%(variable, cut, lep))
   
   outname = "%sQCDShape_%s_%s_%s"%(out_path,cut,variable,lep)
   
   outFile=gROOT.FindObject('%s_temp.root'%(outname))
   if outFile : outFile.Close()
   outFile = TFile('%s.root'%(outname),'RECREATE','Histograms')
   log = open('%s.log'%(outname),'w')
   
   #### DATA ####
   name = "Analyzed_Data_%s"%(lep)
   inFile = TFile('%s%s.root'%(in_path,name))
   for key in inFile.GetListOfKeys():
    obj = key.ReadObj()
    if(obj.IsA().InheritsFrom("TH1")):
     h_name = obj.GetName() 
     if( fnm.fnmatch( h_name,"h_%s_%s_qcd_%s"%(cut,lep,variable) ) ):
      obj.Draw("GOFF")
      obj.SetName("data_qcd")
      outFile.cd()
      obj.Write()
   inFile.Close()
   
   #### MC ####
   for mc_sample in mc_samples: # for each of the normal MC samples
    name = "Analyzed_%s_SFs"%(mc_sample)
    inFile = TFile(in_path+name+'.root')
    if( fnm.fnmatch(mc_sample, "W*Jet*") ):
     q_flavors = ["_Wbb","_Wcc","_Wc","_Wl"]
    else: 
     q_flavors = ["",]
    for q_flavor in q_flavors: # for "" or "_Wbb","_Wcc","_Wc","_Wl"
     for key in inFile.GetListOfKeys():
      obj = key.ReadObj()
      if(obj.IsA().InheritsFrom("TH1")):
       h_name = obj.GetName() 
       if( fnm.fnmatch(h_name,"h_%s_%s_qcd_%s%s"%(cut,lep,variable,q_flavor)) ):
        obj.Draw("GOFF")
        obj.SetName( "h_%s%s_qcd"%(mc_sample,q_flavor) )
        outFile.cd()
        obj.Write()
       # end if obj has qcd name
      # end if obj is TH1
     # end for key in inFile.GetListOfKeys()
    # end for q_flavor in q_flavors
    inFile.Close()
   # end for mc_sample in mc_samples
   outFile.Close()
   

   #### ###
   # Plot #
   #### ###
   inFile = TFile('%s.root'%(outname))

   c = TCanvas('c','QCD Distributions',canx,cany)
   c.SetFrameLineWidth(2)

   #### Data
   data_qcd = inFile.Get('data_qcd')
   data_qcd.Rebin(rebin)
   data_qcd.SetMarkerStyle(22)
   data_qcd.SetMarkerSize(1.2)
   dmax = data_qcd.GetMaximum()
  
   #### Drell
   h_Drell_qcd = inFile.Get('h_Drell_qcd')
   h_Drell_qcd.SetFillColor(c_z)
   h_Drell_qcd.Rebin(rebin)
   h_Drell_qcd.Draw("GOFF")

   #### WW
   h_WW_qcd = inFile.Get('h_WW_qcd')
   h_WW_qcd.SetFillColor(c_vv)
   h_WW_qcd.Rebin(rebin)
   h_WW_qcd.Draw("GOFF")

   #### WZ
   h_WZ_qcd = inFile.Get('h_WZ_qcd')
   h_WZ_qcd.SetFillColor(c_vv)
   h_WZ_qcd.Rebin(rebin)
   h_WZ_qcd.Draw("GOFF")

   #### ZZ
   h_ZZ_qcd = inFile.Get('h_ZZ_qcd')
   h_ZZ_qcd.SetFillColor(c_vv)
   h_ZZ_qcd.Rebin(rebin)
   h_ZZ_qcd.Draw("GOFF")

   #### T_s
   h_T_s_qcd = inFile.Get('h_T_s_qcd')
   h_T_s_qcd.SetFillColor(c_t)
   h_T_s_qcd.Rebin(rebin)
   h_T_s_qcd.Draw("GOFF")

   #### T_t
   h_T_t_qcd = inFile.Get('h_T_t_qcd')
   h_T_t_qcd.SetFillColor(c_t)
   h_T_t_qcd.Rebin(rebin)
   h_T_t_qcd.Draw("GOFF")

   #### T_tW
   h_T_tW_qcd = inFile.Get('h_T_tW_qcd')
   h_T_tW_qcd.SetFillColor(c_t)
   h_T_tW_qcd.Rebin(rebin)
   h_T_tW_qcd.Draw("GOFF")

   #### Tbar_s
   h_Tbar_s_qcd = inFile.Get('h_Tbar_s_qcd')
   h_Tbar_s_qcd.SetFillColor(c_tb)
   h_Tbar_s_qcd.Rebin(rebin)
   h_Tbar_s_qcd.Draw("GOFF")

   #### Tbar_t
   h_Tbar_t_qcd = inFile.Get('h_Tbar_t_qcd')
   h_Tbar_t_qcd.SetFillColor(c_tb)
   h_Tbar_t_qcd.Rebin(rebin)
   h_Tbar_t_qcd.Draw("GOFF")

   #### Tbar_tW
   h_Tbar_tW_qcd = inFile.Get('h_Tbar_tW_qcd')
   h_Tbar_tW_qcd.SetFillColor(c_tb)
   h_Tbar_tW_qcd.Rebin(rebin)
   h_Tbar_tW_qcd.Draw("GOFF")
  
   #### TTbar_full
   h_TTbar_full_qcd = inFile.Get('h_TTbar_full_qcd')
   h_TTbar_full_qcd.SetFillColor(c_ttb)
   h_TTbar_full_qcd.Rebin(rebin)
   h_TTbar_full_qcd.Draw("GOFF")
  
   #### TTbar_semi
   h_TTbar_semi_qcd = inFile.Get('h_TTbar_semi_qcd')
   h_TTbar_semi_qcd.SetFillColor(c_ttb)
   h_TTbar_semi_qcd.Rebin(rebin)
   h_TTbar_semi_qcd.Draw("GOFF")

   #### Wbb
   h_WJets_Wbb_qcd = inFile.Get('h_WJets_Wbb_qcd')
   h_WJets_Wbb_qcd.SetFillColor(c_wbb)
   h_WJets_Wbb_qcd.Rebin(rebin)
   h_WJets_Wbb_qcd.Draw("GOFF")

   h_W1Jet_Wbb_qcd = inFile.Get('h_W1Jet_Wbb_qcd')
   h_W1Jet_Wbb_qcd.SetFillColor(c_wbb)
   h_W1Jet_Wbb_qcd.Rebin(rebin)
   h_W1Jet_Wbb_qcd.Draw("GOFF")

   h_W2Jet_Wbb_qcd = inFile.Get('h_W2Jet_Wbb_qcd')
   h_W2Jet_Wbb_qcd.SetFillColor(c_wbb)
   h_W2Jet_Wbb_qcd.Rebin(rebin)
   h_W2Jet_Wbb_qcd.Draw("GOFF")

   h_W3Jet_Wbb_qcd = inFile.Get('h_W3Jet_Wbb_qcd')
   h_W3Jet_Wbb_qcd.SetFillColor(c_wbb)
   h_W3Jet_Wbb_qcd.Rebin(rebin)
   h_W3Jet_Wbb_qcd.Draw("GOFF")

   h_W4Jet_Wbb_qcd = inFile.Get('h_W4Jet_Wbb_qcd')
   h_W4Jet_Wbb_qcd.SetFillColor(c_wbb)
   h_W4Jet_Wbb_qcd.Rebin(rebin)
   h_W4Jet_Wbb_qcd.Draw("GOFF")

   h_Wbb_qcd = h_WJets_Wbb_qcd.Clone()
   h_Wbb_qcd.SetName("h_Wbb_qcd")
   h_Wbb_qcd.Add(h_W1Jet_Wbb_qcd)
   h_Wbb_qcd.Add(h_W2Jet_Wbb_qcd)
   h_Wbb_qcd.Add(h_W3Jet_Wbb_qcd)
   h_Wbb_qcd.Add(h_W4Jet_Wbb_qcd)
   h_Wbb_qcd.Draw("GOFF")

   #### Wcc
   h_WJets_Wcc_qcd = inFile.Get('h_WJets_Wcc_qcd')
   h_WJets_Wcc_qcd.SetFillColor(c_wcc)
   h_WJets_Wcc_qcd.Rebin(rebin)
   h_WJets_Wcc_qcd.Draw("GOFF")

   h_W1Jet_Wcc_qcd = inFile.Get('h_W1Jet_Wcc_qcd')
   h_W1Jet_Wcc_qcd.SetFillColor(c_wcc)
   h_W1Jet_Wcc_qcd.Rebin(rebin)
   h_W1Jet_Wcc_qcd.Draw("GOFF")

   h_W2Jet_Wcc_qcd = inFile.Get('h_W2Jet_Wcc_qcd')
   h_W2Jet_Wcc_qcd.SetFillColor(c_wcc)
   h_W2Jet_Wcc_qcd.Rebin(rebin)
   h_W2Jet_Wcc_qcd.Draw("GOFF")

   h_W3Jet_Wcc_qcd = inFile.Get('h_W3Jet_Wcc_qcd')
   h_W3Jet_Wcc_qcd.SetFillColor(c_wcc)
   h_W3Jet_Wcc_qcd.Rebin(rebin)
   h_W3Jet_Wcc_qcd.Draw("GOFF")

   h_W4Jet_Wcc_qcd = inFile.Get('h_W4Jet_Wcc_qcd')
   h_W4Jet_Wcc_qcd.SetFillColor(c_wcc)
   h_W4Jet_Wcc_qcd.Rebin(rebin)
   h_W4Jet_Wcc_qcd.Draw("GOFF")

   h_Wcc_qcd = h_WJets_Wcc_qcd.Clone()
   h_Wcc_qcd.SetName("h_Wcc_qcd")
   h_Wcc_qcd.Add(h_W1Jet_Wcc_qcd)
   h_Wcc_qcd.Add(h_W2Jet_Wcc_qcd)
   h_Wcc_qcd.Add(h_W3Jet_Wcc_qcd)
   h_Wcc_qcd.Add(h_W4Jet_Wcc_qcd)
   h_Wcc_qcd.Draw("GOFF")

   #### Wc
   h_WJets_Wc_qcd = inFile.Get('h_WJets_Wc_qcd')
   h_WJets_Wc_qcd.SetFillColor(c_wc)
   h_WJets_Wc_qcd.Rebin(rebin)
   h_WJets_Wc_qcd.Draw("GOFF")

   h_W1Jet_Wc_qcd = inFile.Get('h_W1Jet_Wc_qcd')
   h_W1Jet_Wc_qcd.SetFillColor(c_wc)
   h_W1Jet_Wc_qcd.Rebin(rebin)
   h_W1Jet_Wc_qcd.Draw("GOFF")

   h_W2Jet_Wc_qcd = inFile.Get('h_W2Jet_Wc_qcd')
   h_W2Jet_Wc_qcd.SetFillColor(c_wc)
   h_W2Jet_Wc_qcd.Rebin(rebin)
   h_W2Jet_Wc_qcd.Draw("GOFF")

   h_W3Jet_Wc_qcd = inFile.Get('h_W3Jet_Wc_qcd')
   h_W3Jet_Wc_qcd.SetFillColor(c_wc)
   h_W3Jet_Wc_qcd.Rebin(rebin)
   h_W3Jet_Wc_qcd.Draw("GOFF")

   h_W4Jet_Wc_qcd = inFile.Get('h_W4Jet_Wc_qcd')
   h_W4Jet_Wc_qcd.SetFillColor(c_wc)
   h_W4Jet_Wc_qcd.Rebin(rebin)
   h_W4Jet_Wc_qcd.Draw("GOFF")

   h_Wc_qcd = h_WJets_Wc_qcd.Clone()
   h_Wc_qcd.SetName("h_Wc_qcd")
   h_Wc_qcd.Add(h_W1Jet_Wc_qcd)
   h_Wc_qcd.Add(h_W2Jet_Wc_qcd)
   h_Wc_qcd.Add(h_W3Jet_Wc_qcd)
   h_Wc_qcd.Add(h_W4Jet_Wc_qcd)
   h_Wc_qcd.Draw("GOFF")

   #### Wl
   h_WJets_Wl_qcd = inFile.Get('h_WJets_Wl_qcd')
   h_WJets_Wl_qcd.SetFillColor(c_wl)
   h_WJets_Wl_qcd.Rebin(rebin)
   h_WJets_Wl_qcd.Draw("GOFF")

   h_W1Jet_Wl_qcd = inFile.Get('h_W1Jet_Wl_qcd')
   h_W1Jet_Wl_qcd.SetFillColor(c_wl)
   h_W1Jet_Wl_qcd.Rebin(rebin)
   h_W1Jet_Wl_qcd.Draw("GOFF")

   h_W2Jet_Wl_qcd = inFile.Get('h_W2Jet_Wl_qcd')
   h_W2Jet_Wl_qcd.SetFillColor(c_wl)
   h_W2Jet_Wl_qcd.Rebin(rebin)
   h_W2Jet_Wl_qcd.Draw("GOFF")

   h_W3Jet_Wl_qcd = inFile.Get('h_W3Jet_Wl_qcd')
   h_W3Jet_Wl_qcd.SetFillColor(c_wl)
   h_W3Jet_Wl_qcd.Rebin(rebin)
   h_W3Jet_Wl_qcd.Draw("GOFF")

   h_W4Jet_Wl_qcd = inFile.Get('h_W4Jet_Wl_qcd')
   h_W4Jet_Wl_qcd.SetFillColor(c_wl)
   h_W4Jet_Wl_qcd.Rebin(rebin)
   h_W4Jet_Wl_qcd.Draw("GOFF")

   h_Wl_qcd = h_WJets_Wl_qcd.Clone()
   h_Wl_qcd.SetName("h_Wl_qcd")
   h_Wl_qcd.Add(h_W1Jet_Wl_qcd)
   h_Wl_qcd.Add(h_W2Jet_Wl_qcd)
   h_Wl_qcd.Add(h_W3Jet_Wl_qcd)
   h_Wl_qcd.Add(h_W4Jet_Wl_qcd)
   h_Wl_qcd.Draw("GOFF")

   ### Stack MC
   MCStack = THStack("MCStack","")
   MCStack.SetTitle("")
   MCStack.Add(h_Drell_qcd)
   MCStack.Add(h_WW_qcd)
   MCStack.Add(h_WZ_qcd)
   MCStack.Add(h_ZZ_qcd)
   MCStack.Add(h_T_s_qcd)
   MCStack.Add(h_T_t_qcd)
   MCStack.Add(h_T_tW_qcd)
   MCStack.Add(h_Tbar_s_qcd)
   MCStack.Add(h_Tbar_t_qcd)
   MCStack.Add(h_Tbar_tW_qcd)
   MCStack.Add(h_TTbar_full_qcd)
   MCStack.Add(h_TTbar_semi_qcd)
   MCStack.Add(h_Wl_qcd)
   MCStack.Add(h_Wc_qcd)
   MCStack.Add(h_Wcc_qcd)
   MCStack.Add(h_Wbb_qcd)

   ### QCD
   h_QCD = data_qcd.Clone()
   h_QCD.SetName("h_QCD")
   h_QCD.Add(h_Drell_qcd,-1)
   h_QCD.Add(h_TTbar_full_qcd,-1)
   h_QCD.Add(h_TTbar_semi_qcd,-1)
   h_QCD.Add(h_T_s_qcd,-1)
   h_QCD.Add(h_T_t_qcd,-1)
   h_QCD.Add(h_T_tW_qcd,-1)
   h_QCD.Add(h_Tbar_s_qcd,-1)
   h_QCD.Add(h_Tbar_t_qcd,-1)
   h_QCD.Add(h_Tbar_tW_qcd,-1)
   h_QCD.Add(h_Wbb_qcd,-1)
   h_QCD.Add(h_Wcc_qcd,-1)
   h_QCD.Add(h_Wc_qcd,-1)
   h_QCD.Add(h_Wl_qcd,-1)
   h_QCD.Add(h_WW_qcd,-1)
   h_QCD.Add(h_WZ_qcd,-1)
   h_QCD.Add(h_ZZ_qcd,-1)
   h_QCD.SetLineColor(c_qcd)
   h_QCD.SetLineWidth(3)

   # fill legend
   leg=TLegend(0.68,0.3,0.88,0.88)
   leg.AddEntry(data_qcd,"Data")
   leg.AddEntry(h_Wbb_qcd,"W+b#bar{b}","f")
   leg.AddEntry(h_Wcc_qcd,"W+c#bar{c}","f")
   leg.AddEntry(h_Wc_qcd,"W+c","f")
   leg.AddEntry(h_Wl_qcd,"W+udsg","f")
   leg.AddEntry(h_TTbar_full_qcd,"t#bar{t}","f")
   leg.AddEntry(h_Tbar_s_qcd,"#bar{t}","f")
   leg.AddEntry(h_T_s_qcd,"t","f")
   leg.AddEntry(h_WW_qcd,"WW,WZ,ZZ","f")
   leg.AddEntry(h_Drell_qcd,"Drell-Yan","f")
   leg.AddEntry(h_QCD,"QCD","f")
   leg.SetFillColor(0)
   leg.SetBorderSize(0)

   ## Draw it

   xlabel = data_qcd.GetTitle()
   title =  cut+" "+lep+" "+xlabel
   data_qcd.GetXaxis().SetTitle( xlabel )
   data_qcd.SetTitle("")
   data_qcd.GetYaxis().SetRangeUser(0,1.1*dmax)

   data_qcd.Draw()
   MCStack.Draw("sames,hist")
   h_QCD.Draw("sames,hist")   
   leg.Draw()
   cpr.prelim_alt(19700,0.05)
   tex.SetTextAlign(11) #left, bottom
   tex.DrawLatex(0.1,0.9,title)

   c.Print(outname+".png")

