
 #"8TeVMu"

for sample in \
 "8TeVMu" 
 do

 for cut in \
  "mcut1" \
  "mcut2" \
  "mcut3" \
  "mcut4" \
  "mcut5" 

 do

#sed -n -e 's/^.*'"${cut}"'://p' /nfs_scratch/tperry/Interlochen_cutfloat-Data*${sample}_callHistoFiller/Data*_${sample}*/*${sample}*.root.log > ${cut}_${sample}.py

  echo $cut
  python ${cut}_${sample}.py

 done
done

