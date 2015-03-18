#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00


# "W1Jet_p1" \
# "W2Jet_p1" \
# "W3Jet_p1" \
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


# MC
####
for v7ASample in \
 "WJets_p1" \
 "WJets_p2" 
do
 farmoutAnalysisJobs \
  --merge \
  --input-files-per-job=50 \
  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${v7ASample}-MuEle-PATMC_V7A" \
  "${version}_${v7ASample}" \
  ${CMSSW_BASE}
done

#for v19Sample in \
# "W1Jet_p2" \
# "W2Jet_p2" \
# "W3Jet_p2" 
#do
# farmoutAnalysisJobs \
#  --merge \
#  --input-files-per-job=50 \
#  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${v19Sample}-MuEle-PATMC_V19" \
#  "${version}_${v19Sample}" \
#  ${CMSSW_BASE}
#done
#
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
# "DataA_8TeVEle" \
# "DataB_8TeVEle" \
# "DataC_8TeVEle" \
# "DataD_8TeVEle"
#do
# farmoutAnalysisJobs \
#  --merge \
#  --input-files-per-job=100 \
#  --input-dir="root://cmsxrootd.hep.wisc.edu//store/user/${USER}/${version}_${DEleSample}-Ele-PATData" \
#  "${version}_${DEleSample}" \
#  ${CMSSW_BASE}
#done
#
