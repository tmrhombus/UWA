#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/01G_fitTT"
#path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/00_initial"


for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="02_gsf_${lep}_${ps}_comparison"
 Tname="02_gsf_${lep}_${ps}_comparison"
 
# Gname="Mrgd_Samed_Giuseppe_${ps}_mt_${lep}"
# Tname="Samed_Tom_${ps}_mt_${lep}"

  python \
    "${path_scr}/comp.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "02_gsfcheck_${lep}_" \
    "${ps}"


    #"01_unnorm_${lep}_" \
    #"01_nToOne_${lep}_" \
  
 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"
