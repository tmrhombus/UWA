echo
echo "version: ${version}"
echo "runname: ${runname}"


##### for checking individual files
# "DataA_8TeVMu" \
# "DataB_8TeVMu" \
# "DataC_8TeVMu" \
# "DataD_8TeVMu" \
# "DataA_8TeVEle" \
# "DataB_8TeVEle" \
# "DataC_8TeVEle" \
for sample in \
 "DataD_8TeVEle"

do


 grep -l "exited with status 0" /nfs_scratch/tperry/Interlochen_${runname}-${sample}_callHistoFillerTTbarProgression/*/*out > ${sample}_good.txt
 ls /nfs_scratch/tperry/Interlochen_${runname}-${sample}_callHistoFillerTTbarProgression/*/*out > ${sample}_all.txt
 grep -Fvf ${sample}_good.txt ${sample}_all.txt > ${sample}_bad.txt

done
