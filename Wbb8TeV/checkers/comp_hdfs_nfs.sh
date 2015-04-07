echo
echo "${version} ${runname}"

shifts[0]="SFs"
shifts[1]="JESUp"
shifts[2]="JESDown"
shifts[3]="LESUp"
shifts[4]="LESDown"

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
 nfs_full=$(ls -d /nfs_scratch/tperry/${version}_${MCsample}-MuEle-PATMC*/*/ | wc -l)
 nfs_ful5=$((((${nfs_full}+49)/50)))
 nm=$(ls -d /nfs_scratch/tperry/${version}_${MCsample}-mergeFilesJob/*/ | wc -l)

 hf=$(ls -1 /hdfs/store/user/tperry/${version}_${MCsample}-MuEle-PATMC*/*.root | wc -l)
 h5=$((((${hf}+49)/50)))
 hm=$(ls -1 /hdfs/store/user/tperry/${version}_${MCsample}-mergeFilesJob/*.root | wc -l)

 hmcf=$(($hmcf+$hf)) 
 nmcf=$(($nmcf+$nfs_full)) 
 hmcm=$(($hmcm+$hm)) 
 nmcm=$(($nmcm+$nm)) 
 
 df=$((${nfs_full}-${hf}))
 pf=`echo "${hf} ${nfs_full}" | awk '{printf "%.5f \n", 100*$1/$2}'`

 echo -e "${MCsample}\t /nfs\t /hdfs"
 echo -e "  full\t ${nfs_full}\t ${hf}\t  ${pf}% Complete"
 echo -e "  full/50\t ${nfs_ful5}\t ${h5}\t ${df} failed jobs"
 echo -e "  merged\t ${nm}\t ${hm}"

# if [[ $MCsample == *"_p"* ]]
# then
#  MCsample=${MCsample%_p1}
#  MCsample=${MCsample%_p2}
# fi
# for myshift in "${shifts[@]}" 
#  do
#  na=$(ls -d /nfs_scratch/tperry/${version}_${runname}-${MCsample}_${myshift}_callHistoFiller/*/ | wc -l)
#  ha=$(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${MCsample}_${myshift}_callHistoFiller/*.root | wc -l) 
#  echo -e "  ${myshift}\t ${na}\t ${ha} "
# done
 echo
done


pmcf=`echo "${hmcf} ${nmcf}" | awk '{printf "%.5f \n", 100*$1/$2}'`
echo
echo "Total MC"
echo "/nfs ${nmcf}   /hdfs ${hmcf}  ${pmcf}% Completed"
echo
echo


for sample in \
 "DataA_8TeVMu" \
 "DataB_8TeVMu" \
 "DataC_8TeVMu" \
 "DataD_8TeVMu" \
 "DataA_8TeVEle" \
 "DataB_8TeVEle" \
 "DataC_8TeVEle" \
 "DataD_8TeVEle" 

do
 
 # 
 nfs_full=$(ls -d /nfs_scratch/tperry/${version}_${sample}-*-PATData/*/ | wc -l)
 nfs_ful5=$((((${nfs_full}+99)/100)))
 nm=$(ls -d /nfs_scratch/tperry/${version}_${sample}-mergeFilesJob/*/ | wc -l)

 hf=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-*-PATData/*.root | wc -l)
 h5=$((((${hf}+99)/100)))
 hm=$(ls -1 /hdfs/store/user/tperry/${version}_${sample}-mergeFilesJob/*.root | wc -l)

 hdf=$(($hdf+$hf)) 
 ndf=$(($ndf+$nfs_full)) 
 hdm=$(($hdm+$hm)) 
 ndm=$(($ndm+$nm)) 

 df=$((${nfs_full}-${hf}))
 pf=`echo "${hf} ${nfs_full}" | awk '{printf "%.5f \n", 100*$1/$2}'`

 echo -e "${sample}\t /nfs\t /hdfs"
 echo -e "  full\t ${nfs_full}\t ${hf}\t  ${pf}% Complete"
 echo -e "  full/100\t ${nfs_ful5}\t ${h5}\t ${df} failed jobs"
 echo -e "  merged\t ${nm}\t ${hm}"

#  na=$(ls -d /nfs_scratch/tperry/${version}_${runname}-${sample}_callHistoFiller/*/ | wc -l)
#  ha=$(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${sample}_callHistoFiller/*.root | wc -l) 
#  echo -e "  \t ${na}\t ${ha} "
 echo
done

pdf=`echo "${hdf} ${ndf}" | awk '{printf "%.5f \n", 100*$1/$2}'`
echo
echo "Total Data"
echo "/nfs ${ndf}   /hdfs ${hdf}  ${pdf}% Completed"
echo
echo


