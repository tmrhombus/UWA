#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00

cat Mu-Pat_Data.py  > Mu-PATData.py
cat CONDOR_DATA.py >> Mu-PATData.py
cat Ele-Pat_Data.py > Ele-PATData.py
cat CONDOR_DATA.py >> Ele-PATData.py

# muons
farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 --use-osg \
  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012A-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
  OSG_${version}_DataA_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Mu-PATData.py

farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012B-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
  ${version}_DataB_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Mu-PATData.py

farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
  ${version}_DataC_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Mu-PATData.py

farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012D-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
  ${version}_DataD_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Mu-PATData.py

## electrons
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataA_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataA_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Ele-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataB_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataB_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Ele-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataC_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataC_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Ele-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=5000 --vsize-limit=5000 \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataD_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataD_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/Ele-PATData.py

rm Mu-PATData.py
rm Ele-PATData.py
