#!/usr/bin/env python
'''
Makes a root file containing histograms for later plotting
Author: T.M.Perry UW
'''
import ROOT
from ROOT import TGraph,THStack,TLegend,TCanvas,TFile,TH1F, TPad
from ROOT import TLatex
from ROOT import gROOT,gStyle
from ROOT import *

import aHisto as h #function to make histograms
import histoRange as hr #manages range, lables for plots

leaf = "mt"
steps, xmin, xmax, xtitle, xunits, setLogY = hr.ranger(leaf)

W4F_filename       = '/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/data/post_synch_v6/Wbb4F.root'
W4F_file        = TFile( W4F_filename   )

path = '../plots/PS5_22aout_Wbb4F_%s'%leaf
outFile=gROOT.FindObject(path+'.root')
if outFile : outFile.Close()
outFile = TFile(path+'.root','RECREATE','4Flavor Histograms')

cut='(((weightFactor * 19775 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFl)))) * ((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired) && ((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) )))'
 #cut='(((weightFactor * 19775 * weightEtaMuonID * weightEtaMuonIso * weightEtaMuonTrig) * ((((abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFb)+(!(abs(J1_partonFlavour)==5 || abs(J1_partonFlavour)==4) * J1_CSVT_SFl)) * (((abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFb)+(!(abs(J2_partonFlavour)==5 || abs(J2_partonFlavour)==4) * J2_CSVM_SFl)))) * ((muNuRelPFIsoDB_A<0.12 && HLT_IsoMu24_eta2p1_v_fired) && ((abs(muon_eta)<2.1 && muon_pt>30) && (nrMuLoose==1 && nrEle==0) && (J1_pt>25 && abs(J1_eta)<2.4 && J1_idLooseJet) && (J2_pt>25 && abs(J2_eta)<2.4 && J2_idLooseJet) && (J3_pt<25) && (nJets24Pt25==0) && (J1_CSVbtag>0.898) && (J2_CSVbtag>0.898) && (mt>45))))'

I=-1
F=-1

eventTreeLocations = [
'muNuEventTree/eventTree',
'muNuEventTreeMuonUp/eventTree',
'muNuEventTreeMuonDown/eventTree',
'muNuEventTreeJetUp/eventTree',
'muNuEventTreeJetDown/eventTree',
'muNuEventTreeUCEUp/eventTree',
'muNuEventTreeUCEDown/eventTree'
]
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
print('')
print('Your File is here: '+path+'.root')
print('')
