#!/bin/bash

path_scr="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/scripts"
path_dat="/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/Schweincomp/TFit_01_bsf_nToGiu"


for lep in "ele" "mu"
do
 for ps in "wbb" "ttme" "ttjjj"
 do
  
 Gname="Mrgd_Samed_Giuseppe_${ps}_mt_${lep}"
 Tname="Samed_Tom_${ps}_mt_${lep}"
 
 rescaleJES="RescaleJES_"

 python "${path_scr}/rescaleJES.py" $Gname $rescaleJES  
 python "${path_scr}/rescaleJES.py" $Tname $rescaleJES 

 done #for ps in "wbb" "ttme" "ttjjj"
done #for lep in "ele" "mu"









