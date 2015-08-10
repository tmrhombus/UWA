#CutNtuple.py
#Author: Aaron Levine, UW Madison
#Produces reduced ntuples, to speed up the analysis

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
dir='/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/data/2014sptr25/'
fname = "list8.txt"
numfiles = file_len(fname)
with open(fname) as f:
 for x in f:
  print "Reading " +dir+x
  if counter % 5 == 0: 
   print "Processed " + str(counter) + " out of " + str(numfiles) + " files"
  #get file of current ntuples from input directory
  x = x.rstrip()
  new_fname = "Fltd_"+x
  print "Writing "+new_fname
  ntuple_file = ROOT.TFile(dir+x)
  #ntuple_file_spot = 'New_Tree'
  ntuple_file_spot = 'muNuEventTree/eventTree'
  tree = ntuple_file.Get(ntuple_file_spot)
  tree.SetName("tree")
  print tree.GetEntries()
  cut_str = "(((abs(muon_eta)<2.1 && muon_pt>30) && (J1_pt>25) && (J2_pt>25) && ((J1_CSVbtag>0.898) || (J2_CSVbtag>0.898)) ))"
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

