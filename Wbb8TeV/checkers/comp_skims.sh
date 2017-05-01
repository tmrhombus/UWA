#!/bin/bash

otot=0 
stot=0

printf "\n                sample   orig   skims    diff\n"
printf "%s" " -----------------------------------------"
printf "%s\n" "-----------------------------------------"

#####
## Count MC
#####
#for sample in \
# "TTbar_semi" \
# "TTbar_full" \
# "Wbb4F" \
# "WJets_p1" \
# "WJets_p2" \
# "W1Jet_p1" \
# "W1Jet_p2" \
# "W2Jet_p1" \
# "W2Jet_p2" \
# "W3Jet_p1" \
# "W3Jet_p2" \
# "W4Jet" \
# "Drell" \
# "T_s" \
# "T_t" \
# "T_tW" \
# "Tbar_s" \
# "Tbar_t" \
# "Tbar_tW" \
# "WW" \
# "WZ" \
# "ZZ" \
# "GJ40to100" \
# "GJ100to200" \
# "GJ200to400" \
# "GJ400toInf" \
# "QCDBCtoE20to30"   \
# "QCDBCtoE30to80"   \
# "QCDBCtoE80to170"  \
# "QCDBCtoE170to250" \
# "QCDBCtoE250to350" \
# "QCDBCtoE350toInf" 

for sample in \
 "SingleMuA" \
 "SingleMuB" \
 "SingleMuC" \
 "SingleMuD" \
 "SingleEleA" \
 "SingleEleB" \
 "SingleEleC" \
 "SingleEleD" \
 "QCD2030"   \
 "QCD3080"   \
 "QCD80170"  \
 "QCD170250" \
 "QCD250350" \
 "QCD350Inf" \
 "GJ40100"   \
 "GJ100200"  \
 "GJ200400"  \
 "GJ400Inf"  \
 "WJetsp1"   \
 "WJetsp2"   \
 "W1Jetp1"   \
 "W1Jetp2"   \
 "W2Jetp1"   \
 "W2Jetp2"   \
 "W3Jetp1"   \
 "W3Jetp2"   \
 "W4Jet"     \
 "Wbb"       \
 "Tt"        \
 "Tbart"     \
 "Ts"        \
 "Tbars"   

do



 if [ "$sample" = "SingleMuA"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/SingleMu/Run2012A-22Jan2013-v1/AOD/Spring2014PATTuples_v3/*root"
  outpath="/hdfs/store/user/tuanqui/SingleMu_Run2012A-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "SingleMuB"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/SingleMu/Run2012B-22Jan2013-v1/AOD/Spring2014PATTuples_v3/*root"
  outpath="/hdfs/store/user/tuanqui/SingleMu_Run2012B-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "SingleMuC"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/SingleMu/Run2012C-22Jan2013-v1/AOD/Spring2014PATTuples_v3/*root"
  outpath="/hdfs/store/user/tuanqui/SingleMu_Run2012C-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "SingleMuD"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/SingleMu/Run2012D-22Jan2013-v1/AOD/Spring2014PATTuples_v3/*root"
  outpath="/hdfs/store/user/tuanqui/SingleMu_Run2012D-skimpattuple_cfg/*root"
 fi


 if [ "$sample" = "SingleEleA"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/DataA_8TeVEle-skimpattuple_cfg/*root"
  outpath="/hdfs/store/user/tuanqui/DataA_8TeV_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "SingleEleB"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/DataB_8TeVEle-skimpattuple_cfg/*root"
  outpath="/hdfs/store/user/tuanqui/DataB_8TeV_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "SingleEleC"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/DataC_8TeVEle-skimpattuple_cfg/*root"
  outpath="/hdfs/store/user/tuanqui/DataC_8TeV_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "SingleEleD"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/DataD_8TeVEle-skimpattuple_cfg/*root"
  outpath="/hdfs/store/user/tuanqui/DataD_8TeV_skimpattuple-skimpattuple_cfg/*root"
 fi


 if [ "$sample" = "QCD2030"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/QCD_Pt_20_30_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0/*root"
  outpath="/hdfs/store/user/tuanqui/QCD_Pt_20_30_BCtoE-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "QCD3080"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/QCD_Pt_30_80_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0/*root"
  outpath="/hdfs/store/user/tuanqui/QCD_Pt_30_80_BCtoE-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "QCD80170"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/QCD_Pt_80_170_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0/*root"
  outpath="/hdfs/store/user/tuanqui/QCD_Pt_80_170_BCtoE-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "QCD170250"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/QCD_Pt_170_250_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0/*root"
  outpath="/hdfs/store/user/tuanqui/QCD_Pt_170_250_BCtoE-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "QCD250350"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/QCD_Pt_250_350_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0/*root"
  outpath="/hdfs/store/user/tuanqui/QCD_Pt_250_350_BCtoE-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "QCD350Inf"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/QCD_Pt_350_BCtoE_TuneZ2star_8TeV_pythia6/Summer12_DR53X-PU_S10_START53_V7A-v2/AODSIM/Fall2015PATTuples_v0/*root"
  outpath="/hdfs/store/user/tuanqui/QCD_Pt_350_BCtoE-skimpattuple_cfg/*root"
 fi


 if [ "$sample" = "GJ40100"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/GJets_HT-40To100_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2015PATTuples_v0"
  outpath="/hdfs/store/user/tuanqui/GJets_HT_40To100_V19-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "GJ100200"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/GJets_HT-100To200_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V19-v1/AODSIM/Fall2015PATTuples_v0"
  outpath="/hdfs/store/user/tuanqui/GJets_HT_100To200_V19-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "GJ200400"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/GJets_HT-200To400_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0"
  outpath="/hdfs/store/user/tuanqui/GJets_HT_200To400_V7A-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "GJ400Inf"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/GJets_HT-400ToInf_8TeV-madgraph/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2015PATTuples_v0"
  outpath="/hdfs/store/user/tuanqui/GJets_HT_400ToInf_V7A-skimpattuple_cfg/*root"
 fi


 if [ "$sample" = "WJetsp1"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/WJets_p1_s-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/WJets_p1_s_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "WJetsp2"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/WJets_p2_s-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/WJets_p2_s_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W1Jetp1"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W1Jet_p1_s-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W1Jet_p1_s_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W1Jetp2"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W1Jet_p2_l-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W1Jet_p2_l_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W2Jetp1"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W2Jet_p1_s-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W2Jet_p1_s_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W2Jetp2"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W2Jet_p2_l-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W2Jet_p2_l_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W3Jetp1"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W3Jet_p1_s-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W3Jet_p1_s_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W3Jetp2"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W3Jet_p2_l-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W3Jet_p2_l_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "W4Jet"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/W4Jet_p1_s-skimpattuple_cfg"
  outpath="/hdfs/store/user/tuanqui/W4Jet_p1_s_skimpattuple-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "Wbb"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/WbbJetsToLNu_Massive_TuneZ2star_8TeV-madgraph-pythia6_tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1"
  outpath="/hdfs/store/user/tuanqui/WbbJetsToLNu-skimpattuple_cfg/*root"
 fi


 if [ "$sample" = "Tt"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/TToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1"
  outpath="/hdfs/store/user/tuanqui/TToLeptons_t-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "Tbart"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/TBarToLeptons_t-channel_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1"
  outpath="/hdfs/store/user/tuanqui/TBarToLeptons-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "Ts"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/T_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1"
  outpath="/hdfs/store/user/tuanqui/T_s-skimpattuple_cfg/*root"
 fi

 if [ "$sample" = "Tbars"  ]
 then
  inpath="/hdfs/store/user/tperry/PatTuples_8TeV/Tbar_s-channel_TuneZ2star_8TeV-powheg-tauola/Summer12_DR53X-PU_S10_START53_V7A-v1/AODSIM/Fall2014PATTuples_V1"
  outpath="/hdfs/store/user/tuanqui/TBar_s-skimpattuple_cfg/*root"
 fi




  ocount=$(ls  $inpath | wc -l)
  scount=$(ls $outpath | wc -l)

  thisdiff=$(($ocount-$scount))

  otot=$(($otot+$ocount)) 
  stot=$(($stot+$scount)) 
  totdiff=$(($otot-$stot))

  printf "  %20s %6s %6s %6s incomplete analyzers  (%5s)\n" ${sample} ${ocount} ${scount} ${thisdiff} ${totdiff}

done
printf "%s" " -----------------------------------------"
printf "%s\n" "-----------------------------------------"
printf "  Totals  orignals: $otot  skims: $stot  diff: $totdiff\n\n" 

