#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/03T_fitTTme_v2"

for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="02_csvgsf_${lep}_${ps}_comparison"
 Tname="02_csvgsf_${lep}_${ps}_comparison"
 
  sf_Wi_mu=1.628
  sf_Tr_mu=2.171
  sf_Wi_ele=1.628
  sf_Tr_ele=2.171

  if [ ${lep} == "ele" ]
  then
   sf_Wi=${sf_Wi_ele}
   sf_Tr=${sf_Tr_ele}
  else 
   sf_Wi=${sf_Wi_mu}
   sf_Tr=${sf_Tr_mu}
  fi


  python \
    "${path_scr}/rescaleJES.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "03_jest_${lep}_" \
    "${ps}" \
    ${sf_Wi} \
    ${sf_Tr} 

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"

