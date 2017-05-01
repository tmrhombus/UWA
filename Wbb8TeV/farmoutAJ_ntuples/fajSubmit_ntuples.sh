#!/bin/bash
#voms-proxy-init --voms cms --valid 100:00

#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg --memory-requirements=6000 --vsize-limit=6000  \

#/hdfs/store/user/nsmith/DYJetsToLL_M-10To50filter_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/ZHinv2015

####
# Submit MC Samples
####
cat MuEle-PatMCs.py > MuEle-PATMCs.py
cat CONDOR.py >>      MuEle-PATMCs.py
cat MuEle-PatMCl.py > MuEle-PATMCl.py
cat CONDOR.py >>      MuEle-PATMCl.py

##  WJets Scales
## WJets Up
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/WJetsToLNu_scaleup_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Fall2015PATTuples_vX \
#  ${version}_WnJsclUp $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py

farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/WJetsToLNu_scaledown_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v1 \
  ${version}_WnJsclDown $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py

## W1Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W1JetsToLNu_scaleup_TuneZ2Star_8TeV-madgraph/Summer12-START53_V7C_FSIM-v1/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W1JsclUp $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W1JetsToLNu_scaledown_TuneZ2Star_8TeV-madgraph/Summer12-START53_V7C_FSIM-v1/AODSIM/Fall2015PATTuples_v1 \
  ${version}_W1JsclDown $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## W2Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W2JetsToLNu_scaleup_8TeV-madgraph/Summer12-START53_V7C_FSIM-v5/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W2JsclUp $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py

#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W2JetsToLNu_scaledown_8TeV-madgraph/Summer12-START53_V7C_FSIM-v4/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W2JsclDown $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## W3Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W3JetsToLNu_scaleup_8TeV-madgraph/Summer12-START53_V7C_FSIM-v4/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W3JsclUp $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W3JetsToLNu_scaledown_8TeV-madgraph/Summer12-START53_V7C_FSIM-v4/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W3JsclDown $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## W4Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W4JetsToLNu_scaleup_8TeV-madgraph/Summer12-START53_V7C_FSIM-v4/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W4JsclUp $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py

#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tuanqui/W4JetsToLNu_scaledown_8TeV-madgraph/Summer12-START53_V7C_FSIM-v4/AODSIM/Fall2015PATTuples_v1 \
#  ${version}_W4JsclDown $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py



##  QCD
#######

# QCD BCtoE
## BCtoE 20-30
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_QCDBCtoE20to30 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## BCtoE 30-80
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/QCD_Pt_30_80_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_QCDBCtoE30to80 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## BCtoE 80-170
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_QCDBCtoE80to170 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## BCtoE 170-250
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/QCD_Pt_170_250_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_QCDBCtoE170to250 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## BCtoE 250-350
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/QCD_Pt_250_350_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_QCDBCtoE250to350 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## BCtoE 350-Inf
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/QCD_Pt_350_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_QCDBCtoE350toInf $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py

##Gamma+Jets
## GJ 40-100
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/GJets_HT-40To100_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_GJ40to100 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## GJ 100-200
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/GJets_HT-100To200_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_GJ100to200 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## GJ 200-400
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/GJets_HT-200To400_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_GJ200to400 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## GJ 400-Inf
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/PatTuples_8TeV/GJets_HT-400ToInf_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0 \
#  ${version}_GJ400toInf $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py

##TTbar
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_FullLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v2/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_TTbar_full $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/TTJets_SemiLeptMGDecays_8TeV-madgraph-tauola/Summer12_DR53X-PU_S10_START53_V7C-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_TTbar_semi $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#
## W Jets
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1  --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJets_p1_s-skimpattuple_cfg \
#  ${version}_WJets_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1  --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/WJets_p2_s-skimpattuple_cfg \
#  ${version}_WJets_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
##
## W1 Jet
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1Jet_p1_s-skimpattuple_cfg \
#  ${version}_W1Jet_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
##farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W1Jet_p2_l-skimpattuple_cfg \
#  ${version}_W1Jet_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## W2 Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2Jet_p1_s-skimpattuple_cfg \
#  ${version}_W2Jet_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W2Jet_p2_l-skimpattuple_cfg \
#  ${version}_W2Jet_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## W3 Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3Jet_p1_s-skimpattuple_cfg \
#  ${version}_W3Jet_p1 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W3Jet_p2_l-skimpattuple_cfg \
#  ${version}_W3Jet_p2 $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCl.py
#
## W4 Jet
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/W4Jet_p1_s-skimpattuple_cfg \
#  ${version}_W4Jet $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#
##Wbb 4Flavor
#farmoutAnalysisJobs $1 --input-files-per-job=1  --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_Wbb4F $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## Drell
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/dntaylor/DYJetsToLL_M-50_TuneZ2Star_8TeV-madgraph-tarball/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_Drell $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/nsmith/DYJetsToLL_M-10To50filter_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/ZHinv2015 \
#  ${version}_DrellLM $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
## Single Top
##tW
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/Tbar_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_Tbar_tW $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/mcepeda/T_tW-channel-DR_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_T_tW $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
##tt
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/TToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_T_t $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/TBarToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
# ${version}_Tbar_t $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
##ts
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/T_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_T_s $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1 \
#  ${version}_Tbar_s $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
##Diboson
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/aglevine/WW_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATuples_V1 \
#  ${version}_WW $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/aglevine/WZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATuples_V1 \
#  ${version}_WZ $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
#
#farmoutAnalysisJobs $1 --input-files-per-job=1 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/aglevine/ZZ_TuneZ2star_8TeV_pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATuples_V1 \
#  ${version}_ZZ $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/MuEle-PATMCs.py
# 
rm MuEle-PATMCs.py
rm MuEle-PATMCl.py

######
### Submit Data Samples
######
#
#cat Mu-Pat_Data.py  > Mu-PATData.py
#cat CONDOR.py      >> Mu-PATData.py
#cat Ele-Pat_Data.py > Ele-PATData.py
#cat CONDOR.py      >> Ele-PATData.py
#
## muons
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012A-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
#  ${version}_DataA_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Mu-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012B-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
#  ${version}_DataB_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Mu-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
#  ${version}_DataC_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Mu-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/SingleMu/Run2012D-22Jan2013-v1/AOD/Spring2014PATTuples_v3/ \
#  ${version}_DataD_8TeVMu $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Mu-PATData.py
#
## electrons
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataA_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataA_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Ele-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataB_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataB_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Ele-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataC_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataC_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Ele-PATData.py
#
#farmoutAnalysisJobs --input-files-per-job=1 --shared-fs --memory-requirements=3000 --vsize-limit=3000 --use-osg \
#  --input-dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/DataD_8TeVEle-skimpattuple_cfg/ \
#  ${version}_DataD_8TeVEle $CMSSW_BASE $CMSSW_BASE/src/UWAnalysis/Wbb8TeV/farmoutAJ_ntuples/Ele-PATData.py
#
#rm Mu-PATData.py
#rm Ele-PATData.py

