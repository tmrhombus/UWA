#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/TFit_02_JESbsf"


for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="RescaleJES_Mrgd_Samed_Giuseppe_${ps}_mt_${lep}"
 Tname="RescaleJES_Samed_Tom_${ps}_mt_${lep}"
 
##
  sf_Tr_mu=1.1237
  un_Tr_mu=0.0146
  
  sf_Tr_ele=1.1512
  un_Tr_ele=0.0157
   
  sf_Wi_mu=1.1413
  un_Wi_mu=0.0150
  
  sf_Wi_ele=1.1469
  un_Wi_ele=0.0149

  if [ ${lep} == "ele" ]
  then
   sf_Wi=${sf_Wi_ele}
   sf_Tr=${sf_Tr_ele}
 else 
   sf_Wi=${sf_Wi_mu}
   sf_Tr=${sf_Tr_mu}
  fi


  python \
    "${path_scr}/applyBsf.py" \
    "${Gname}" \
    "${Tname}" \
    "${path_dat}"  \
    "05_JESbsf_${lep}_" \
    "${ps}" \
    ${sf_Wi} \
    ${sf_Tr} 


    #"01_unnorm_${lep}_" \
    #"01_nToGiu_${lep}_" \
    #"01_nToOne_${lep}_" \
  
 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"









