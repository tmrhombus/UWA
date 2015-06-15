#!/bin/bash

PATH=/afs/hep.wisc.edu/cms/cmsprod/farmoutCmsJobs/:$PATH

for sample in \
 DataA \
 DataB \
 DataC \
 DataD 
 
do
  jobReportSummary.py /nfs_scratch/${USER}/${version}_${sample}_8TeVMu-Mu-PATData/*/*.xml   --json-out ${version}_${sample}_mu.json
  jobReportSummary.py /nfs_scratch/${USER}/${version}_${sample}_8TeVEle-Ele-PATData/*/*.xml --json-out ${version}_${sample}_ele.json
done

mergeJSON.py ${version}_DataA_mu.json  ${version}_DataB_mu.json  ${version}_DataC_mu.json  ${version}_DataD_mu.json  --output=${version}_DataABCD_mu.json
mergeJSON.py ${version}_DataA_ele.json ${version}_DataB_ele.json ${version}_DataC_ele.json ${version}_DataD_ele.json --output=${version}_DataABCD_ele.json
