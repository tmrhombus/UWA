#!/bin/sh
#voms-proxy-init --voms cms --valid 100:00

cat MuEle-PatMC_V19.py > MuEle-PATMC_V19.py
cat CONDOR_MC.py >> MuEle-PATMC_V19.py
cat MuEle-PatMC_V7A.py > MuEle-PATMC_V7A.py
cat CONDOR_MC.py >> MuEle-PATMC_V7A.py

##TTbar
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_TTbar_full $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_TTbar_semi $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
 # W Jets
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_WJets_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py

 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJetsToLNu_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Fall2014PATTuples_V1 \
   ${version}_WJets_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py

 # W1 Jet
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_W1Jet_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
 
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_W1Jet_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V19.py
 
 # W2 Jet
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_W2Jet_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
 
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_W2Jet_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V19.py
 
 # W3 Jet
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_W3Jet_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
 
 farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2014PATTuples_V1 \
   ${version}_W3Jet_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V19.py
 
# # W4 Jet
# farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=5000 --vsize-limit=5000 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W4JetsToLNu_TuneZ2Star_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_W4Jet $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
# #Wbb 4Flavor
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_Wbb4F $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
# 
# # Drell
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/dntaylor/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_Drell $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
# # Single Top
# #tW
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_Tbar_tW $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
# 
# #farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg --memory-requirements=6000 --vsize-limit=6000  \
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_T_tW $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
# #tt
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/TToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_T_t $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
# 
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/TBarToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_Tbar_t $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
# #ts
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/T_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_T_s $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#   ${version}_Tbar_s $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
#
# #Diboson
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/aglevine/WW_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATuples_V1 \
#   ${version}_WW $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
# 
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/aglevine/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATuples_V1 \
#   ${version}_WZ $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
# 
# farmoutAnalysisJobs $1 --input-files-per-job=1 \
#   --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/aglevine/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATuples_V1 \
#   ${version}_ZZ $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/CRAB/MuNu/farmoutAJ_ntuples/MuEle-PATMC_V7A.py
 
rm MuEle-PATMC_V19.py
rm MuEle-PATMC_V7A.py

