#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/mrgW_01T_fitTTjjj"
 

for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="mrgW_Oflo_01_nToGiu_${lep}_${ps}_comparison"
 Tname="mrgW_Oflo_01_nToGiu_${lep}_${ps}_comparison"
 
  sf_Wi_ele=2.41
  sf_Tr_ele=2.53
  sf_Wi_mu=2.32
  sf_Tr_mu=2.04

  if [ ${lep} == "ele" ]
  then
   sf_Wi=${sf_Wi_ele}
   sf_Tr=${sf_Tr_ele}
  else 
   sf_Wi=${sf_Wi_mu}
   sf_Tr=${sf_Tr_mu}
  fi


  python \
    "${path_scr}/rescaleCSV_mrgW.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "mrgW_02_csv_${lep}_" \
    "${ps}" \
    ${sf_Wi} \
    ${sf_Tr} 

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"

