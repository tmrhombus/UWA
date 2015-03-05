#!/bin/bash

echo "Data"
date +"%T"
find /hdfs/store/user/tperry/${version}_DataA_8TeVMu-Mu-PATData/*root > data/${version}/list_DataA_Mu.txt
find /hdfs/store/user/tperry/${version}_DataB_8TeVMu-Mu-PATData/*root > data/${version}/list_DataB_Mu.txt
find /hdfs/store/user/tperry/${version}_DataC_8TeVMu-Mu-PATData/*root > data/${version}/list_DataC_Mu.txt
find /hdfs/store/user/tperry/${version}_DataD_8TeVMu-Mu-PATData/*root > data/${version}/list_DataD_Mu.txt

find /hdfs/store/user/tperry/${version}_DataA_8TeVEle-Ele-PATData/*root > data/${version}/list_DataA_Ele.txt
find /hdfs/store/user/tperry/${version}_DataB_8TeVEle-Ele-PATData/*root > data/${version}/list_DataB_Ele.txt
find /hdfs/store/user/tperry/${version}_DataC_8TeVEle-Ele-PATData/*root > data/${version}/list_DataC_Ele.txt
find /hdfs/store/user/tperry/${version}_DataD_8TeVEle-Ele-PATData/*root > data/${version}/list_DataD_Ele.txt


# WJets
echo "Making WJets Lists "
date +"%T"
find /hdfs/store/user/tperry/"$version"_WJets_p1-MuEle-PATMC_V7A/*root >  data/"$version"/list_WJets.txt
find /hdfs/store/user/tperry/"$version"_WJets_p2-MuEle-PATMC_V7A/*root >> data/"$version"/list_WJets.txt
find /hdfs/store/user/tperry/"$version"_W1Jet_p1-MuEle-PATMC_V7A/*root >  data/"$version"/list_W1Jet.txt
find /hdfs/store/user/tperry/"$version"_W1Jet_p2-MuEle-PATMC_V19/*root >> data/"$version"/list_W1Jet.txt
find /hdfs/store/user/tperry/"$version"_W2Jet_p1-MuEle-PATMC_V7A/*root >  data/"$version"/list_W2Jet.txt
find /hdfs/store/user/tperry/"$version"_W2Jet_p2-MuEle-PATMC_V19/*root >> data/"$version"/list_W2Jet.txt
find /hdfs/store/user/tperry/"$version"_W3Jet_p1-MuEle-PATMC_V7A/*root >  data/"$version"/list_W3Jet.txt
find /hdfs/store/user/tperry/"$version"_W3Jet_p2-MuEle-PATMC_V19/*root >> data/"$version"/list_W3Jet.txt
find /hdfs/store/user/tperry/"$version"_W4Jet-MuEle-PATMC_V7A/*root > data/"$version"/list_W4Jet.txt
find /hdfs/store/user/tperry/"$version"_Wbb4F-MuEle-PATMC_V7A/*root > data/"$version"/list_Wbb4F.txt
#Top
echo "Making Top Lists"
date +"%T"
find /hdfs/store/user/tperry/"$version"_TTbar_full-MuEle-PATMC_V7A/*root > data/"$version"/list_TTbar_full.txt
find /hdfs/store/user/tperry/"$version"_TTbar_semi-MuEle-PATMC_V7A/*root > data/"$version"/list_TTbar_semi.txt
find /hdfs/store/user/tperry/"$version"_T_s-MuEle-PATMC_V7A/*root >  data/"$version"/list_T_s.txt
find /hdfs/store/user/tperry/"$version"_T_t-MuEle-PATMC_V7A/*root >  data/"$version"/list_T_t.txt
find /hdfs/store/user/tperry/"$version"_T_tW-MuEle-PATMC_V7A/*root > data/"$version"/list_T_tW.txt
find /hdfs/store/user/tperry/"$version"_Tbar_s-MuEle-PATMC_V7A/*root >  data/"$version"/list_Tbar_s.txt
find /hdfs/store/user/tperry/"$version"_Tbar_t-MuEle-PATMC_V7A/*root >  data/"$version"/list_Tbar_t.txt
find /hdfs/store/user/tperry/"$version"_Tbar_tW-MuEle-PATMC_V7A/*root > data/"$version"/list_Tbar_tW.txt
#DY/VV
echo "Making DY/VV Lists"
date +"%T"
find /hdfs/store/user/tperry/"$version"_Drell-MuEle-PATMC_V7A/*root > data/"$version"/list_Drell.txt
find /hdfs/store/user/tperry/"$version"_WW-MuEle-PATMC_V7A/*root > data/"$version"/list_WW.txt
find /hdfs/store/user/tperry/"$version"_WZ-MuEle-PATMC_V7A/*root > data/"$version"/list_WZ.txt
find /hdfs/store/user/tperry/"$version"_ZZ-MuEle-PATMC_V7A/*root > data/"$version"/list_ZZ.txt

touch data/"$version"/initialEvents.txt

for list in \
'data/'"$version"'/list_W1Jet.txt' \
'data/'"$version"'/list_W2Jet.txt' \
'data/'"$version"'/list_W3Jet.txt' \
'data/'"$version"'/list_W4Jet.txt' \
'data/'"$version"'/list_WJets.txt' \
'data/'"$version"'/list_Drell.txt' \
'data/'"$version"'/list_TTbar_full.txt' \
'data/'"$version"'/list_TTbar_semi.txt' \
'data/'"$version"'/list_T_s.txt' \
'data/'"$version"'/list_T_t.txt' \
'data/'"$version"'/list_T_tW.txt' \
'data/'"$version"'/list_Tbar_s.txt' \
'data/'"$version"'/list_Tbar_t.txt' \
'data/'"$version"'/list_Tbar_tW.txt' \
'data/'"$version"'/list_WW.txt' \
'data/'"$version"'/list_WZ.txt' \
'data/'"$version"'/list_Wbb4F.txt' \
'data/'"$version"'/list_ZZ.txt' 

do
 echo "Reading Nr. Events found in " $list
 date +"%T"
 echo $list >> data/"$version"/initialEvents.txt
 python scripts/eventCounter.py $list >> data/"$version"/initialEvents.txt
done

