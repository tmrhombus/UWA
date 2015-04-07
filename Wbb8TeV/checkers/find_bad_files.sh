echo
echo "${version} ${runname}"

tabs 15

####
# Count MC
####
for MCsample in \
 "DataA_8TeVMu" \
 "DataB_8TeVMu" \
 "DataC_8TeVMu" \
 "DataD_8TeVMu" \
 "DataA_8TeVEle" \
 "DataB_8TeVEle" \
 "DataC_8TeVEle" \
 "DataD_8TeVEle" \
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
 
#  echo $MCsample
#  outfile="/afs/hep.wisc.edu/home/tperry/www/scrap/BadFiles/${version}_${MCsample}.sh.txt"
#  touch ${outfile}
#
#  grep -r "was not found, could not be opened, or is corrupted" '/nfs_scratch/tperry/'"${version}"'_'"${MCsample}"*/*/*err > ${outfile}
#
# sed -i 's@^.*//store@# gsido rm /hdfs/store@g' "${outfile}"
# sed -i 's@was not found, could not be opened, or is corrupted.@@g' "${outfile}"

 
  echo $MCsample
  outfile="/afs/hep.wisc.edu/home/tperry/www/scrap/BadFiles/rm_nfs_${version}_${MCsample}.sh.txt"
  touch ${outfile}

  grep -r "was not found, could not be opened, or is corrupted" '/nfs_scratch/tperry/'"${version}"'_'"${MCsample}"*/*/*err > ${outfile}

  sed -i 's@/nfs_scratch/'"${USER}"'/'"${version}"'_'"${MCsample}"'\(.*\)/.*err:Input.*@rm -rf /nfs_scratch/'"${USER}"'/'"${version}"'_'"${MCsample}"'\1@g' ${outfile}

 echo
done

