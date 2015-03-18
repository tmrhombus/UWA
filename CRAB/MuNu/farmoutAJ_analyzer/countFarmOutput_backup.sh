
echo ${version}_${runname}

shifts[0]="SFs"
shifts[1]="JESUp"
shifts[2]="JESDown"
shifts[3]="LESUp"
shifts[4]="LESDown"

## choose sample
#for samplename in \
# "Drell" \
# "TTbar_full" \
# "TTbar_semi" \
# "T_s" \
# "T_t" \
# "T_tW" \
# "Tbar_s" \
# "Tbar_t" \
# "Tbar_tW" \
# "W1Jet" \
# "W2Jet" \
# "W3Jet" \
# "W4Jet" \
# "WJets" \
# "Wbb4F" \
# "WW" \
# "WZ" \
# "ZZ"


#"SFs" "JESUp" "JESDown" "LESUp" "LESDown"

for v7ASample in \
 "ZZ" 

# "W4Jet" \
# "Wbb4F" \
# "TTbar_full" \
# "TTbar_semi" \
# "Drell" \
# "T_s" \
# "T_t" \
# "T_tW" \
# "Tbar_s" \
# "Tbar_t" \
# "Tbar_tW" \
# "WW" \
# "WZ" \
# "ZZ"
do
 echo "${v7ASample}"
 for myshift in "${shifts[@]}" 
  do
  echo " ${myshift}"
  #nf=(($(ls -1 /nfs_scratch/tperry/${version}_${v7ASample}-MuEle-PATMC_V7A/ | wc -l)-3))
  #echo $nf
  echo "/nfs  full $((($(ls -1 /nfs_scratch/tperry/${version}_${v7ASample}-MuEle-PATMC_V7A/ | wc -l)-3)))" \
      "(/50 = $(((($(ls -1 /nfs_scratch/tperry/${version}_${v7ASample}-MuEle-PATMC_V7A/ | wc -l)-3)/50+1))))" \
           "merged $(ls -d /nfs_scratch/tperry/${version}_${v7ASample}-mergeFilesJob/*/ | wc -l)" \
         "analyzed $(ls -d /nfs_scratch/tperry/${version}_${runname}-${v7ASample}_${myshift}_callHistoFiller/*/ | wc -l)"

  echo "/hdfs full $(ls -1 /hdfs/store/user/tperry/${version}_${v7ASample}-MuEle-PATMC_V7A/*.root | wc -l)" \
      "(/50 = $(((($(ls -1 /hdfs/store/user/tperry/${version}_${v7ASample}-MuEle-PATMC_V7A/*.root | wc -l)/50)+1))))" \
           "merged $(ls -1 /hdfs/store/user/tperry/${version}_${v7ASample}-mergeFilesJob/*.root | wc -l)" \
         "analyzed $(ls -1 /hdfs/store/user/tperry/${version}_${runname}-${v7ASample}_${myshift}_callHistoFiller/*.root | wc -l)" 
 done
done


           #"merged $(ls -1 /nfs_scratch/tperry/${version}_${v7ASample}-mergeFilesJob/*/ | wc -l)" \

# "WJets_p1" \
# "WJets_p2" \
# "W1Jet_p1" \
# "W2Jet_p1" \
# "W3Jet_p1" \
#for v19Sample in \
# "W1Jet_p2" \
# "W2Jet_p2" \
# "W3Jet_p2" 
#
#for DMuSample in \
# "DataA_8TeVMu" \
# "DataB_8TeVMu" \
# "DataC_8TeVMu" \
# "DataD_8TeVMu" 
