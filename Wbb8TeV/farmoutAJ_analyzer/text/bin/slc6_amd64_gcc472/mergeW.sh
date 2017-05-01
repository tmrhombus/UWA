#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/00_initial"

for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="Oflo_01_nToGiu_${lep}_${ps}_comparison"
 Tname="Oflo_01_nToGiu_${lep}_${ps}_comparison"
 
  sf_Wi_ele=2.39
  sf_Tr_ele=2.49
  sf_Wi_mu=2.32
  sf_Tr_mu=2.02

  if [ ${lep} == "ele" ]
  then
   sf_Wi=${sf_Wi_ele}
   sf_Tr=${sf_Tr_ele}
  else 
   sf_Wi=${sf_Wi_mu}
   sf_Tr=${sf_Tr_mu}
  fi


  python \
    "${path_scr}/mergeW.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "mrgW_" \
    "${ps}"

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"

