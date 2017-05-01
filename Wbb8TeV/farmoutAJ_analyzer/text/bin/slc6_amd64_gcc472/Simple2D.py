import ROOT
from ROOT import THStack,TH1F,TH2F,TFile
import makeFunctions as make

path = "/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/data/post_synch_v0/"

theFile = TFile(path+"Data.root")
theTree = theFile.Get("muNuEventTree/eventTree")

histo = TH2F('histo','histo',50,0.,200.,50,0.,3.)
theTree.Draw('muNuRelPFIsoDB_A:mt>>histo',"",'colz')

raw_input()
