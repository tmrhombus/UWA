#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/04T_fitWbb_v2"

for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="03_jest_${lep}_${ps}_comparison"
 Tname="03_jest_${lep}_${ps}_comparison"
 

  python \
    "${path_scr}/renameQCD.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "04_qcdd_${lep}_" \
    "${ps}" \
    "${lep}" 

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"

