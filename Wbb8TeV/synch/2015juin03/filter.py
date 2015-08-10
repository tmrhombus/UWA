#CutNtuple.py
#Author: A.Levine, T.M.Perry UW Madison
#Produces reduced ntuples

from sys import argv, stdout, stderr
import ROOT
import math
#Returns the number of lines in the files
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

counter = 0

#define the file
dir='/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/synch/NouvelleYear/'
fname = "list.txt"
numfiles = file_len(fname)
with open(fname) as f:
 for x in f:
  print "Reading " +dir+x
  if counter % 5 == 0: 
   print "Processed " + str(counter) + " out of " + str(numfiles) + " files"
  #get file of current ntuples from input directory
  x = x.rstrip()
  new_fname = "C1_ele03_"+x
  print "Writing "+new_fname
  #ntuple_file_spot = 'muEleEventTree/eventTree'
  #ntuple_file_spot = 'muonEventTree/eventTree'
  ntuple_file_spot = 'electronEventTree/eventTree'
  ntuple_file = ROOT.TFile(dir+x)
  tree = ntuple_file.Get(ntuple_file_spot)
  tree.SetName("tree")
  print tree.GetEntries()

  #cut_str = "(HLT_IsoMu24_eta2p1_v_fired && nrGoodMu==1 && nrVetoMu<=1 && nrVetoEle==0 && nrGoodJets==2 && nrFwdJets==0)"
  #cut_str = "(HLT_IsoMu24_eta2p1_v_fired && nrGoodMu==1 && nrVetoMu<=1 && nrVetoEle==0 && nrGoodJets==2 && nrFwdJets==0 && mt_goodMuon>45)"
  #cut_str = "(HLT_IsoMu24_eta2p1_v_fired && nrGoodMu==1 && nrVetoMu<=1 && nrVetoEle==0 && nrGoodJets==2 && nrFwdJets==0 && mt_goodMuon>45 && goodJ1_CSV>0.898 && goodJ2_CSV>0.898)"

  #cut_str = "(HLT_Ele27_WP80_fired && nrGoodEle==1 && goodEle_Iso04_vec[0]<0.10 && nrVetoEle<=1 && nrVetoMu==0 && nrGoodJets==2 && nrFwdJets==0)"
  cut_str = "(HLT_Ele27_WP80_fired && nrGoodEle==1 && goodEle_Iso03_vec[0]<0.10 && nrVetoEle<=1 && nrVetoMu==0 && nrGoodJets==2 && nrFwdJets==0)"

  #cut_str = "(HLT_Ele27_WP80_fired && nrGoodEle==1 && goodEle_Iso03_vec[0]<0.10 && nrVetoEle<=1 && nrVetoMu==0 && nrGoodJets==2 && nrFwdJets==0 && mt_goodElectron>45)"
  #cut_str = "(HLT_Ele27_WP80_fired && nrGoodEle==1 && goodEle_Iso03_vec[0]<0.10 && nrVetoEle<=1 && nrVetoMu==0 && nrGoodJets==2 && nrFwdJets==0 && mt_goodElectron>45 && goodJ1_CSV>0.898 && goodJ2_CSV>0.898)"

  Smalltree_file = ROOT.TFile(new_fname,"RECREATE")
  Smalltree_file.cd()
  new_ttree = ROOT.TTree("new_ttree","new_ttree")
  new_ttree = tree.CopyTree(cut_str)
  new_ttree.SetName("New_Tree")
  print new_ttree.GetEntries()
  tree.Delete()
  #new_ttree.Write("eventTree")
  Smalltree_file.Write()
  Smalltree_file.Close()
  
  counter = counter+1
 
 
 
