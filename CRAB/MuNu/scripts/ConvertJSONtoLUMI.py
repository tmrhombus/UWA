#!/usr/bin/env python

import os, re, sys, json

if len(sys.argv) != 3:
 print "Usage: ConvertJSONtoLUMI.py [inputFile.json] [outputFile.lumi]"
 sys.exit(0)

input_file = open(sys.argv[1],'r')

if os.path.exists(sys.argv[2]):
 print "Output file '%s' already exists.\nRename it or delete it first!!" % (sys.argv[2])
 sys.exit(-1)

output_file = open(sys.argv[2],'w')
line_to_write ="import FWCore.ParameterSet.Config as cms\n"
line_to_write +='source = cms.Source("PoolSource",\n'
line_to_write +='fileNames = cms.untracked.vstring(),\n'
line_to_write +=")\n"
line_to_write += "source.lumisToProcess = cms.untracked.VLuminosityBlockRange()\n"
output_file.write(line_to_write)

entry = json.load(input_file)
for run in sorted(entry):
 #print "Run %s >>>" % (run)
 for lumirange in entry[run]:
  #print "\tLuminosity section %s" % (lumirange)
  line_to_write = "source.lumisToProcess.append('%s:%s-%s:%s')\n" % (run, lumirange[0], run, lumirange[1])
  output_file.write(line_to_write)
