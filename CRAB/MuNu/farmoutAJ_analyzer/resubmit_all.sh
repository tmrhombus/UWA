#voms-proxy-init --voms cms --valid 100:00

mkdir -p ../SampleInfo/${version}/Lists
mkdir -p ./Submit_${version}

# general parameters
lumi_mu="19778"
lumi_ele="19757"

#shifts[0]="LESDown"
#
##shifts[0]="SFs"
##shifts[1]="JESUp"
##shifts[2]="JESDown"
##shifts[3]="LESUp"
##shifts[4]="LESDown"
#
## choose sample
#for samplename in \
# "W2Jet" 
#
#
## "TTbar_full" \
## "TTbar_semi" \
## "T_s" \
## "T_t" \
## "T_tW" \
## "Tbar_s" \
## "Tbar_t" \
## "Tbar_tW" \
## "W1Jet" \
## "W2Jet" \
## "W3Jet" \
## "W4Jet" \
## "WJets" \
## "Wbb4F" \
## "WW" \
## "WZ" \
## "ZZ" 
#
# #"Drell" 
#
#do
# echo "${samplename}"
# # count the total number of events, put in a file if it's not there
# if ! grep -F "${samplename} " ../SampleInfo/${version}/initialEvents.txt
# then 
#  echo "You sure you should be resubmitting? No entry in SampleInfo/${version}/initialEvents.txt"
# fi
# mylist="../SampleInfo/${version}/xrd_list_${samplename}.txt"
#
# # set up sample specific stuff from initialEvents.txt
# nrE="$(grep -P ${samplename} ../SampleInfo/Valentine/Lists/initialEvents.txt | sed -n -e "s@${samplename} Events: @@p")"
# xc="$(grep -P ${samplename}  ../SampleInfo/Valentine/Lists/initialEvents.txt | sed -n -e "s@${samplename} XC: @@p")"
# isMC="kTRUE"
# ## or put it in by hand
# #nrE="1234567" 
# #xc="12.34"
# if [[ ${samplename} == W*Jet* ]]
#  then isW="kTRUE"
#  else isW="kFALSE"
# fi
#
# echo $nrE
# echo $xc
#
# # for shift in list above
# for theshift in "${shifts[@]}"
# do
#
#  if [[ ${theshift} == SFs ]]     ; then treename="muEleEventTree/eventTree"         ; fi
#  if [[ ${theshift} == JESUp ]]   ; then treename="muEleEventTreeJetUp/eventTree"    ; fi
#  if [[ ${theshift} == JESDown ]] ; then treename="muEleEventTreeJetDown/eventTree"  ; fi
#  if [[ ${theshift} == LESUp ]]   ; then treename="muEleEventTreeMuonUp/eventTree"   ; fi
#  if [[ ${theshift} == LESDown ]] ; then treename="muEleEventTreeMuonDown/eventTree" ; fi
#
#  # make correct executable xx_callHistoFiller()
#  cp template_callHistoFiller.cc                    "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@PSANDSHIFT@${samplename}_${theshift}@g" "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@PSNAME@${samplename}@g"                 "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@LUMIMU@${lumi_mu}@g"                    "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@LUMIELE@${lumi_ele}@g"                  "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@NREVENTS@${nrE}@g"                      "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@CROSSSEC@${xc}@g"                       "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@ISMC@${isMC}@g"                         "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@ISW@${isW}@g"                           "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@SHIFT@${theshift}@g"                    "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#  sed -i "s@TREENAME@${treename}@g"                 "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#
#  farmoutAnalysisJobs \
#   --resubmit-failed-jobs --memory-requirements=5000 --vsize-limit=5000 \
#   --infer-cmssw-path \
#   --fwklite \
#   --input-file-list=${mylist} \
#   --extra-inputs=${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.C,${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.h \
#   ${runname} \
#   "./Submit_${version}/${samplename}_${theshift}_callHistoFiller.cc"
#
# done # theshift in shifts[@]
#done # samplename in mc_samples


for samplename in \
 "DataA_8TeVMu" \
 "DataB_8TeVMu" \
 "DataC_8TeVMu" \
 "DataD_8TeVMu" 

# "DataA_8TeVEle" \
# "DataB_8TeVEle" \
# "DataC_8TeVEle" \
# "DataD_8TeVEle"

do

 echo "${samplename}"
 # make a list of all the sample filenames

 mylist="../SampleInfo/${version}/Lists/xrd_list_${samplename}.txt"

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
  --resubmit-failed-jobs --memory-requirements=5000 --vsize-limit=5000 \
  --infer-cmssw-path \
  --fwklite \
  --input-file-list=${mylist} \
  --extra-inputs=${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.C,${CMSSW_BASE}/src/UWAnalysis/CRAB/MuNu/farmoutAJ_analyzer/histoFiller.h \
  ${runname} \
  "./Submit_${version}/${samplename}${theshift}_callHistoFiller.cc"

done # samplename in data_samples

