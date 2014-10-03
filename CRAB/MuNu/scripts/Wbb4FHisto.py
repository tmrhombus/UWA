#!/usr/bin/env python
'''
Makes a root file of Wbb 4 Flavor histograms
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *
import os

import aHisto as h #function to make histograms
import histoRange as hr #manages range, lables for plots

leafs = ["J1_pt",
         "J2_pt",
         "met_pt",
         "muon_pt",
         "mt_new"
]
cutnames = ['Wbb',
            'TT_1m1e',
            'TT_3j',
]
eventTreeLocations = [
'muNuEventTree/eventTree',
'muNuEventTreeMuonUp/eventTree',
'muNuEventTreeMuonDown/eventTree',
'muNuEventTreeJetUp/eventTree',
'muNuEventTreeJetDown/eventTree',
'muNuEventTreeUCEUp/eventTree',
'muNuEventTreeUCEDown/eventTree'
]
I=-1
F=-1
for leaf in leafs:
 print("------------")
 print(leaf)
 print("------------")
 for cutname in cutnames:
  print(cutname) 
  steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)
  version = os.environ.get('version')
  W4F_filename       = '/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/data/%s/Wbb4F.root'%(version)
  W4F_file        = TFile( W4F_filename )
  
  path = '../plots/%s_%s_4F_%s'%(version,cutname,leaf)
  outFile=gROOT.FindObject(path+'.root')
  if outFile : outFile.Close()
  outFile = TFile(path+'.root','RECREATE','4Flavor Histograms')
  
  #if leaf=="mt": cutmt = '(mt>45)'
  if leaf=="mt_new": cutmt = '(2 > 1)'
  else: cutmt = '(mt_new>45)'
  if cutname == 'Wbb': cut='(((QweightFactor * 19775 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFl)))) * ((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired) && ((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && %s)))'%cutmt
  if cutname == 'TT_3j': cut='(((QweightFactor * 19774 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFl)))) * ((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired) && ((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt>25 && abs(J3_eta)<2.4 && J3_idLooseJet) && (nJets24Pt25==0) && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && %s)))'%cutmt
  if cutname == 'TT_1m1e': cut='(((QweightFactor * 19774 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFl)))) * ((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired) && ((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==1 && ele_pt>30) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && %s)))'%cutmt
  
  for eventTreeLocation in eventTreeLocations:
   W4F_tree       =  W4F_file.Get(eventTreeLocation)
   if eventTreeLocation == 'muNuEventTree/eventTree' : ps = 'No'
   if eventTreeLocation == 'muNuEventTreeMuonUp/eventTree' : ps ='muonUp'
   if eventTreeLocation == 'muNuEventTreeMuonDown/eventTree' : ps ='muonDown'
   if eventTreeLocation == 'muNuEventTreeJetUp/eventTree' : ps ='jetUp'
   if eventTreeLocation == 'muNuEventTreeJetDown/eventTree' : ps ='jetDown'
   if eventTreeLocation == 'muNuEventTreeUCEUp/eventTree': ps = 'UCEUp'
   if eventTreeLocation == 'muNuEventTreeUCEDown/eventTree': ps = 'UCEDown'
   
   w4fh,w4fhSize,w4fhSizePart,w4fhEntries = h.gram(W4F_tree,leaf,xmin,xmax,steps,cut,I,F)
   w4fh.SetName("W4F_%s"%(ps))
   print('  '+str(w4fhSize))
   
   outFile.Write()
  outFile.Close()
  print('')
  print('Your File is here: '+path+'.root')
  print('') 
