#!/usr/bin/env python
# Prints out met info saved in a patTuple
import ROOT
import sys
import math
import json
import re
from optparse import OptionParser

ROOT.gROOT.SetBatch(1)

##____________________________________________________________________________||
parser = OptionParser()
parser.add_option('-i', '--inputPath', default = './cecile_mvamet_test.root', action = 'store', type = 'string')
(options, args) = parser.parse_args(sys.argv)
inputPath = options.inputPath

##____________________________________________________________________________||
def main():
    
    printHeader()
    if getNEvents(inputPath):
        count(inputPath)

##____________________________________________________________________________||
def printHeader():
    print '%6s'  % 'run',
    print '%10s' % 'lumi',
    print '%9s'  % 'event',
    print '%35s' % 'module',
    print '%15s' % 'pt',
    print '%10s' % 'phi',
    print

##____________________________________________________________________________||
def count(inputPath):

    files = [inputPath]

    events = Events(files)

    handlePatMETs  = Handle("std::vector<pat::MET>") 
    handlePFMETs   = Handle("std::vector<reco::PFMET>") 
    handleLeafCand = Handle("std::vector<reco::LeafCandidate>")


    METCollections = (
        ("pfMet",             "", "RECO",  handlePFMETs  ),
        ("patPfMet",          "", "TUPLE", handlePatMETs ),
        ("patPfMetT1",        "", "TUPLE", handlePatMETs ),
        ("systematicsMETMVA", "", "TUPLE", handlePatMETs ),
        )


    eventcount = 0
    for event in events:
        eventcount += 1
        run = event.eventAuxiliary().run()
        lumi = event.eventAuxiliary().luminosityBlock()
        eventId = event.eventAuxiliary().event()

        for METCollection in METCollections:
            handle = METCollection[3]

            event.getByLabel(METCollection[0:3], handle)
            met = handle.product().front()
             
            print '%6d'    % run,
            print '%10d'   % lumi,
            print '%9d'    % eventId,
            print '%35s'   % METCollection[0],
            print '%15.8f' % met.pt(),
            print '%10.3f' % met.phi(),
            print
        print
    print eventcount 


##____________________________________________________________________________||
def getNEvents(inputPath):
    file = ROOT.TFile.Open(inputPath)
    events = file.Get('Events')
    return events.GetEntries()

##____________________________________________________________________________||
def loadLibraries():
    argv_org = list(sys.argv)
    sys.argv = [e for e in sys.argv if e != '-h']
    ROOT.gSystem.Load("libFWCoreFWLite")
    ROOT.AutoLibraryLoader.enable()
    ROOT.gSystem.Load("libDataFormatsFWLite")
    ROOT.gSystem.Load("libDataFormatsPatCandidates")
    sys.argv = argv_org

##____________________________________________________________________________||
loadLibraries()
from DataFormats.FWLite import Events, Handle

##____________________________________________________________________________||
if __name__ == '__main__':
    main()
