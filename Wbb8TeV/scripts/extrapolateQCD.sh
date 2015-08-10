#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/03T_fitTTme"

for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="03_jes_${lep}_${ps}_comparison"
 Tname="03_jes_${lep}_${ps}_comparison"
 
  python \
    "${path_scr}/extrapolateQCD.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "04_qcd_${lep}_" \
    "${ps}" \

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"

