echo
echo "version: ${version}"
echo "runname: ${runname}"

  countmerged="True"
countanalyzed="True"

shifts[0]="SFs"
shifts[1]="JESUp"
shifts[2]="JESDown"
shifts[3]="MESUp"
shifts[4]="MESDown"
shifts[5]="EESUp"
shifts[6]="EESDown"

tabs 15

####
# Count MC
####
for MCsample in \
 "WJets_p1" \
 "WJets_p2" \
 "W1Jet_p1" \
 "W1Jet_p2" \
 "W2Jet_p1" \
 "W2Jet_p2" \
 "W3Jet_p1" \
 "W3Jet_p2" \
 "W4Jet" \
 "Wbb4F" \
 "TTbar_full" \
 "TTbar_semi" \
 "Drell" \
 "T_s" \
 "T_t" \
 "T_tW" \
 "Tbar_s" \
 "Tbar_t" \
 "Tbar_tW" \
 "WW" \
 "WZ" \
 "ZZ"

do
 # ntuples
 nfs_full=$(ls -d /nfs_scratch/tperry/${version}_${MCsample}-MuEle-PATMC*/*/ | wc -l)
 nfs_mergecount=`python -c "from math import ceil; print ceil(${nfs_full}/50.)"`
 #hdfs_full=$(ls -1 /hdfs/store/user/tperry/${version}/${version}_${MCsample}-MuEle-PATMC*/*.root | wc -l)
 hdfs_full=$(ls -1 /hdfs/store/user/tperry/${version}_${MCsample}-MuEle-PATMC*/*.root | wc -l)
 hdfs_mergecount=`python -c "from math import ceil; print ceil(${hdfs_full}/50.)"`
 hdfs_mc_full_total=$(($hdfs_mc_full_total+$hdfs_full)) 
 nfs_mc_full_total=$(($nfs_mc_full_total+$nfs_full)) 
 
 failed_jobs=$((${nfs_full}-${hdfs_full}))
 percent_completed=`echo "${hdfs_full} ${nfs_full}" | awk '{printf "%.5f \n", 100*$1/$2}'`

 echo -e "${MCsample}\t /nfs\t /hdfs"
 echo -e "  full\t ${nfs_full}\t ${hdfs_full}\t  ${percent_completed}% Complete"
 echo -e "  full/50\t ${nfs_mergecount}\t ${hdfs_mergecount}\t ${failed_jobs} failed jobs"

 # merged 
 if [ "$countmerged" = "True" ]
 then
  #hdfs_merged=$(ls -1 /hdfs/store/user/tperry/${version}/${version}_${MCsample}-mergeFilesJob/*.root | wc -l)
  hdfs_merged=$(ls -1 /hdfs/store/user/tperry/${version}_${MCsample}-mergeFilesJob/*.root | wc -l)
  nfs_merged=$(ls -d /nfs_scratch/tperry/${version}_${MCsample}-mergeFilesJob/*/ | wc -l)
  hdfs_mc_merged_total=$(($hdfs_mc_merged_total+$hdfs_merged)) 
  nfs_mc_merged_total=$(($nfs_mc_merged_total+$nfs_merged)) 
  merged_diff=$(($nfs_merged-$hdfs_merged))
  echo -e "  merged\t ${nfs_merged}\t ${hdfs_merged}\t ${merged_diff} failed merges"
 fi

 # analyzed
 if [ "$countanalyzed" = "True" ]
 then
  # drop _p1 or _p2 from end of samplename
  MCsample=${MCsample%_p1}
  MCsample=${MCsample%_p2}
  for myshift in "${shifts[@]}" 
   do
   nfs_analyzed=$(ls -d /nfs_scratch/tperry/${version}_${runname}-${MCsample}_${myshift}_callHistoFiller*/*/ | wc -l)
   hdfs_analyzed=$(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${MCsample}_${myshift}_callHistoFiller*/*.root | wc -l) 
   analyzed_diff=$(($nfs_analyzed-$hdfs_analyzed))
  echo -e "  ${myshift}\t ${nfs_analyzed}\t ${hdfs_analyzed}\t ${analyzed_diff} failed analyzers"
  done
 fi
 echo
done


percent_mc_completed_total=`echo "${hdfs_mc_full_total} ${nfs_mc_full_total}" | awk '{printf "%.5f \n", 100*$1/$2}'`
echo
echo "Total MC"
echo "/nfs ${nfs_mc_full_total}   /hdfs ${hdfs_mc_full_total}  ${percent_mc_completed_total}% Completed"
echo
echo


#for sample in \
# "DataA_8TeVMu" \
# "DataB_8TeVMu" \
# "DataC_8TeVMu" \
# "DataD_8TeVMu" \
# "DataA_8TeVEle" \
# "DataB_8TeVEle" \
# "DataC_8TeVEle" \
# "DataD_8TeVEle" 
#
#do
# 
# nfs_full=$(ls -d /nfs_scratch/tperry/${version}_${sample}-*-PATData/*/ | wc -l)
# nfs_mergecount=`python -c "from math import ceil; print ceil(${nfs_full}/100.)"`
# hdfs_full=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-*-PATData/*.root | wc -l)
# hdfs_mergecount=`python -c "from math import ceil; print ceil(${hdfs_full}/100.)"`
# hdfs_data_full_total=$(($hdfs_data_full_total+$hdfs_full)) 
# nfs_data_full_total=$(($nfs_data_full_total+$nfs_full)) 
#
# failed_jobs=$((${nfs_full}-${hdfs_full}))
# percent_completed=`echo "${hdfs_full} ${nfs_full}" | awk '{printf "%.5f \n", 100*$1/$2}'`
#
# echo -e "${sample}\t /nfs\t /hdfs"
# echo -e "  full\t ${nfs_full}\t ${hdfs_full}\t  ${percent_completed}% Complete"
# echo -e "  full/100\t ${nfs_mergecount}\t ${hdfs_mergecount}\t ${failed_jobs} failed jobs"
#
# if [ "$countmerged" = "True" ]
# then
#  nfs_merged=$(ls -d /nfs_scratch/tperry/${version}_${sample}-mergeFilesJob/*/ | wc -l)
#  hdfs_merged=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-mergeFilesJob/*.root | wc -l)
#  hdfs_data_merged_total=$(($hdfs_data_merged_total+$hdfs_merged)) 
#  nfs_data_merged_total=$(($nfs_data_merged_total+$nfs_merged)) 
#  echo -e "  merged\t ${nfs_merged}\t ${hdfs_merged}"
# fi
#
# if [ "$countanalyzed" = "True" ]
# then
#  nfs_analyzed=$(ls -d /nfs_scratch/tperry/${version}_${runname}-${sample}_callHistoFiller*/*/ | wc -l)
#  hdfs_analyzed=$(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${sample}_callHistoFiller*/*.root | wc -l) 
#  echo -e "  \t ${nfs_analyzed}\t ${hdfs_analyzed} "
# fi
# echo
#done
#
#percent_data_completed_total=`echo "${hdfs_data_full_total} ${nfs_data_full_total}" | awk '{printf "%.5f \n", 100*$1/$2}'`
#echo
#echo "Total Data"
#echo "/nfs ${nfs_data_full_total}   /hdfs ${hdfs_data_full_total}  ${percent_data_completed_total}% Completed"
#echo
#echo



## for checking individual files
# grep -l "exited with status 0" /nfs_scratch/tperry/Earth_DataA_8TeVEle-Ele-PATData/*/*out > dataAEle_good.txt
# ls /nfs_scratch/tperry/Earth_DataA_8TeVEle-Ele-PATData/*/*out > dataAEle_all.txt
# grep -Fvf good_dataAEle.txt all_dataAEle.txt > dataAEle_bad.txt
