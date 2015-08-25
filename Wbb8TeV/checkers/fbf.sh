
filename="TTbar_full"

# for checking ntuples
 grep -l "exited with status 0" /nfs_scratch/tperry/${version}*${filename}*/*/*out > ${filename}_good.txt
 ls /nfs_scratch/tperry/${version}*${filename}*/*/*out > ${filename}_all.txt
 grep -Fvf ${filename}_good.txt ${filename}_all.txt > ${filename}_bad.txt


# for checking analyzers
 grep -l "exited with status 0" /nfs_scratch/tperry/${version}*${runname}*${filename}*/*/*out > "./test/${filename}_good.txt"
 ls /nfs_scratch/tperry/${version}*${runname}*${filename}*/*/*out > "./test/${filename}_all.txt"
 grep -Fvf "./test/${filename}_good.txt" "./test/${filename}_all.txt" > "./test/${filename}_bad.txt"


