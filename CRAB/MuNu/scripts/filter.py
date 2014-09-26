#CutNtuple.py
#Author: Aaron Levine, T.M.Perry UW Madison
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

# recursively loops through directories
# adding dirnames to an array
def tree_finder(key,dirs):
 obj = key.ReadObj()
 if(obj.IsA().InheritsFrom("TDirectory")):
  dirs.append(obj.GetName())
  for key2 in obj.GetListOfKeys():
   tree_finder(key2,dirs)
   return 
 else:
  dirs.append(obj.GetName())

#define the file(s) + cuts
dir='/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/CRAB/MuNu/data/2014sptr25/'
fname = "list.txt"
cut_str = "(((abs(muon_eta)<2.1 && muon_pt>30) && (J1_pt>25) && (J2_pt>25) && ((J1_CSVbtag>0.898) || (J2_CSVbtag>0.898)) ))"
numfiles = file_len(dir+fname)

with open(dir+fname) as f:
 for x in f:
  print "Reading " +dir+x
  if counter % 5 == 0: 
   print "Processed " + str(counter) + " out of " + str(numfiles) + " files"
  #get file of current ntuples from input directory
  x = x.rstrip()
  new_fname = "Filtered_"+x
  print "Writing "+new_fname
  ntuple_file = ROOT.TFile(dir+x)

  Smalltree_file = ROOT.TFile(dir+new_fname,"RECREATE")
  for key in ntuple_file.GetListOfKeys():
   ntuple_file.cd()
   dirnames = []
   morekeys = tree_finder(key,dirnames)
   if dirnames[0]=="summary": continue
   ntuple_file_spot = "/".join(dirnames)
   print ntuple_file_spot
   tree = ntuple_file.Get(ntuple_file_spot)
   tree.SetName("tree")
   print("Before: %s"%tree.GetEntries())
   Smalltree_file.cd()
   new_ttree = ROOT.TTree(dirnames[0],dirnames[0])
   new_ttree = tree.CopyTree(cut_str)
   new_ttree.SetName(dirnames[0])
   print("After: %s"%new_ttree.GetEntries())
   tree.Delete()
   #new_ttree.Write("eventTree")
  Smalltree_file.Write()
  Smalltree_file.Close()
  counter = counter+1

