#voms-proxy-init --voms cms --valid 100:00

START=$(date +%s);
echo "Started at `date`"

mkdir -p ../SampleInfo/${version}/Lists
mkdir -p ./Submit_${version}

# general parameters
#lumi_mu="19730" # VVCheckExtended
lumi_mu="19778" #Valentine
#lumi_ele="19631" # VVCheckExtended
lumi_ele="19757" # Valentine

shifts[0]="SFs"
shifts[1]="JESUp"
shifts[2]="JESDown"
shifts[3]="LESUp"
shifts[4]="LESDown"

# choose sample
for samplename in \
 "Drell" \
 "TTbar_full" \
 "TTbar_semi" \
 "T_s" \
 "T_t" \
 "T_tW" \
 "Tbar_s" \
 "Tbar_t" \
 "Tbar_tW" \
 "W1Jet" \
 "W2Jet" \
 "W3Jet" \
 "W4Jet" \
 "WJets" \
 "Wbb4F" \
 "WW" \
 "WZ" 
# "ZZ" 

do
 echo "${samplename}"
 # count the total number of events, put in a file if it's not there
 if ! grep -F "${samplename} " ../SampleInfo/${version}/Lists/initialEvents.txt
 then 
  echo "Need to count events.. making list"
  # make a list of all the sample filenames
  #find ${hdfs}/${version}_${samplename}*/*root > \ # unmerged samples
  if ! [[ ${samplename} == W*Jet* ]] || [[ ${samplename} == W4Jet ]]
  then
   find ${hdfs}/${version}_${samplename}-mergeFilesJob/*root > \
    ../SampleInfo/${version}/Lists/list_${samplename}.txt #
  else 
   find ${hdfs}/${version}_${samplename}_p1-mergeFilesJob/*root > \
    ../SampleInfo/${version}/Lists/list_${samplename}.txt #
   find ${hdfs}/${version}_${samplename}_p2-mergeFilesJob/*root >> \
    ../SampleInfo/${version}/Lists/list_${samplename}.txt #
  fi
  
  cp "../SampleInfo/${version}/Lists/list_${samplename}.txt" \
     "../SampleInfo/${version}/Lists/xrd_list_${samplename}.txt" #
  # format as xrootd
  mylist="../SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"
  sed -i 's@/hdfs/@root://cmsxrootd.hep.wisc.edu//@g' $mylist #

  echo "                    .. counting events"
  python ./eventCounter.py ${samplename} \
     ../SampleInfo/${version}/Lists/list_${samplename}.txt \
     ../SampleInfo/${version}/Lists/initialEvents.txt
  echo "                    .. counted events"
 else
  mylist="../SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"
 fi
 # or just set it by hand(:
 #mylist="../SampleInfo/${version}/xrd_list_${samplename}.txt" 

 # set up sample specific stuff from initialEvents.txt
 nrE="$(grep -P ${samplename} ../SampleInfo/Valentine/Lists/initialEvents.txt | sed -n -e "s@${samplename} Events: @@p")"
 xc="$(grep -P ${samplename}  ../SampleInfo/Valentine/Lists/initialEvents.txt | sed -n -e "s@${samplename} XC: @@p")"
 isMC="kTRUE"
 ## or put it in by hand
 #nrE="1234567" 
 #xc="12.34"
 echo "Line85"
 if [[ ${samplename} == W*Jet* ]]
  then isW="kTRUE"
  else isW="kFALSE"
 fi

 echo $nrE
 echo $xc

 # for shift in list above
 for theshift in "${shifts[@]}"
 do

  if [[ ${theshift} == SFs ]]     ; then treename="muEleEventTree/eventTree"         ; fi
  if [[ ${theshift} == JESUp ]]   ; then treename="muEleEventTreeJetUp/eventTree"    ; fi
  if [[ ${theshift} == JESDown ]] ; then treename="muEleEventTreeJetDown/eventTree"  ; fi
  if [[ ${theshift} == LESUp ]]   ; then treename="muEleEventTreeMuonUp/eventTree"   ; fi
  if [[ ${theshift} == LESDown ]] ; then treename="muEleEventTreeMuonDown/eventTree" ; fi

  # make correct executable xx_callHistoFiller()
  cp template_callHistoFiller.cc                    "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@PSANDSHIFT@${samplename}_${theshift}@g" "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@PSNAME@${samplename}@g"                 "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@LUMIMU@${lumi_mu}@g"                    "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@LUMIELE@${lumi_ele}@g"                  "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@NREVENTS@${nrE}@g"                      "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@CROSSSEC@${xc}@g"                       "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@ISMC@${isMC}@g"                         "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@ISW@${isW}@g"                           "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@SHIFT@${theshift}@g"                    "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
  sed -i "s@TREENAME@${treename}@g"                 "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"

  farmoutAnalysisJobs \
   --infer-cmssw-path \
   --fwklite \
   --input-file-list=${mylist} \
   --use-hdfs \
   --extra-inputs=${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.C,${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.h \
   ${version}_${runname} \
   "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"

 done # theshift in shifts[@]
done # samplename in mc_samples


for samplename in \
 "DataA_8TeVMu" \
 "DataA_8TeVEle" \
 "DataB_8TeVMu" \
 "DataC_8TeVMu" \
 "DataD_8TeVMu" \
 "DataB_8TeVEle" \
 "DataC_8TeVEle" \
 "DataD_8TeVEle"

do
 echo "${samplename}"
 # make a list of all the sample filenames

 find ${hdfs}/${version}_${samplename}-mergeFilesJob/*root > \
  ../SampleInfo/${version}/Lists/list_${samplename}.txt #

 cp "../SampleInfo/${version}/Lists/list_${samplename}.txt" \
    "../SampleInfo/${version}/Lists/xrd_list_${samplename}.txt" #
 # format as xrootd
 mylist="../SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"
 sed -i 's@/hdfs/@root://cmsxrootd.hep.wisc.edu//@g' $mylist #

 # we shouldn't scale data..
 nrE="100"
 xc="-1"
 isMC="kFALSE"
 isW="kFALSE"
 theshift=""

 if [[ ${samplename} == *Mu ]];  then treename="muonEventTree/eventTree"     ; fi
 if [[ ${samplename} == *Ele ]]; then treename="electronEventTree/eventTree" ; fi

 # make correct executable xx_callHistoFiller()
 cp template_callHistoFiller.cc                   "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@PSANDSHIFT@${samplename}${theshift}@g" "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@PSNAME@${samplename}@g"                "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@LUMIMU@${lumi_mu}@g"                   "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@LUMIELE@${lumi_ele}@g"                 "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@NREVENTS@${nrE}@g"                     "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@CROSSSEC@${xc}@g"                      "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@ISMC@${isMC}@g"                        "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@ISW@${isW}@g"                          "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@SHIFT@${theshift}@g"                   "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"
 sed -i "s@TREENAME@${treename}@g"                "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"

 farmoutAnalysisJobs \
  --infer-cmssw-path \
  --fwklite \
  --use-hdfs \
  --input-file-list=${mylist} \
  --extra-inputs=${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.C,${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.h \
  ${version}_${runname} \
  "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"

done # samplename in data_samples

END=$(date +%s);
echo "Finished at `date`"
echo $((END-START)) | awk '{print int($1/60)":"int($1%60)}'
