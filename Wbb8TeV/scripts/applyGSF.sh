#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/allFits/01T_fitTTjjj"


for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 #Gname="Mrgd_Samed_Giuseppe_${ps}_mt_${lep}"
 #Tname="Samed_Tom_${ps}_mt_${lep}"
 
 Gname="Oflo_01_nToGiu_${lep}_${ps}_comparison"
 Tname="Oflo_01_nToGiu_${lep}_${ps}_comparison"
 
##
  sf_Wi=1.1409 #0.013
  sf_Tr=1.1348 #0.014

  python \
    "${path_scr}/applyGSF.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "02_csvgsf_${lep}_" \
    "${ps}" \
    ${sf_Wi} \
    ${sf_Tr} 

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"









