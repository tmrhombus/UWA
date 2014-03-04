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
dir="/afs/hep.wisc.edu/cms/tperry/CMSSW_5_3_9/src/UWAnalysis/CRAB/MuNu/data/SV_3/"
fname = "list.txt"
numfiles = file_len(fname)
with open(fname) as f:
        for x in f:
                print "Reading " +dir+x
                if counter % 10 == 0:
                        print "Processed " + str(counter) + " out of " + str(numfiles) + " files"
                #get file of current ntuples from input directory
                x = x.rstrip()
                new_fname = "Filtered_1tag_"+x
                print "Writing "+new_fname
                ntuple_file = ROOT.TFile(dir+x)
                ntuple_file_spot = 'muNuEventTree/eventTree'
                tree = ntuple_file.Get(ntuple_file_spot)
                tree.SetName("tree")
                print tree.GetEntries()
                cut_str="muon_pt>=25&&abs(muon_eta)<2.1&&HLT_IsoMu24_eta2p1_v_fired&&(J1_mass_SV_weighted>0||J2_mass_SV_weighted>0||J1_CSVbtag>0.6||J2_CSVbtag>0.6)"
                #cut_str  ="HLT_IsoMu24_eta2p1_v_fired&&(nrMu>1||nrEle>0)"
                #cut_str = "nJetsPt25>=4&&muon_pt>=30&&abs(muon_eta)<2.1&&HLT_IsoMu24_eta2p1_v_fired" 
                #cut_str ="HLT_IsoMu24_eta2p1_v_fired&&mt>50&&muon_pt>=30&&abs(muon_eta)<2.1&&muNuRelPFIsoDB<0.12&&nJetsPt25>=2"
                #cut_str ="mt>50&&muon_pt>=30&&abs(muon_eta)<2.1&&muNuRelPFIsoDB>0.2&&nJetsPt25>=2"
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



