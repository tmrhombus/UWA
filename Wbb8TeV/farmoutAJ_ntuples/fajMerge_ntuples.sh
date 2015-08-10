#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00

####
# Merge MC Samples
####
for sample_s in \
 "WJets_p1" \
 "WJets_p2" \
 "W1Jet_p1" \
 "W2Jet_p1" \
 "W3Jet_p1" \
 "W4Jet" \
 "Wbb4F" \
 "TTbar_full" \
 "TTbar_semi" \
 "Drell" \
 "DrellLM" \
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
 farmoutAnalysisJobs \
  --merge \
  --input-files-per-job=50 \
  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${sample_s}-MuEle-PATMCs" \
  "${version}_${sample_s}" \
  ${CMSSW_BASE}
done

for sample_l in \
 "W1Jet_p2" \
 "W2Jet_p2" \
 "W3Jet_p2" 
do
 farmoutAnalysisJobs \
  --merge \
  --input-files-per-job=50 \
  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${sample_l}-MuEle-PATMCl" \
  "${version}_${sample_l}" \
  ${CMSSW_BASE}
done
#
#
#####
## Merge Data Samples
#####
#for DMuSample in \
# "DataA_8TeVMu" \
# "DataB_8TeVMu" \
# "DataC_8TeVMu" \
# "DataD_8TeVMu" 
#do
# farmoutAnalysisJobs \
#  --merge \
#  --input-files-per-job=100 \
#  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${DMuSample}-Mu-PATData" \
#  "${version}_${DMuSample}" \
#  ${CMSSW_BASE}
#done
#
#for DEleSample in \
# "DataC_8TeVEle" \
# "DataA_8TeVEle" \
# "DataB_8TeVEle" \
# "DataD_8TeVEle"
#do
# farmoutAnalysisJobs \
#  --merge \
#  --input-files-per-job=100 \
#  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${DEleSample}-Ele-PATData" \
#  "${version}_${DEleSample}" \
#  ${CMSSW_BASE}
#done

