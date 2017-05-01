echo
echo "version: ${version}"
echo "runname: ${runname}"

mkdir -p ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}
mkdir -p ${wbbzone}/SampleInfo/${version}/Plots_${runname}

for samplename in \
 "Drell" \
 "DrellLM" \
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
 "WZ" \
 "ZZ" \
 "GJ40to100" \
 "GJ100to200" \
 "GJ200to400" \
 "GJ400toInf" \
 "QCDBCtoE20to30"   \
 "QCDBCtoE30to80"   \
 "QCDBCtoE80to170"  \
 "QCDBCtoE170to250" \
 "QCDBCtoE250to350" \
 "QCDBCtoE350toInf" 

do
 #for myshift in "noshift"
 for myshift in "SFs" "JESUp" "JESDown" "MESUp" "MESDown" "EESUp" "EESDown"
 do
  hadd \
   ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_${samplename}_${myshift}.root \
    ${hdfs}/${version}_${runname}-${samplename}_${myshift}_callHistoFiller*/*.root 
    #${hdfs}/${version}/roots/${runname}/${version}_${runname}-${samplename}_${myshift}_callHistoFiller*/*.root
 done
done

for datasample in \
"DataA_8TeVMu" \
"DataB_8TeVMu" \
"DataC_8TeVMu" \
"DataD_8TeVMu" \
"DataA_8TeVEle" \
"DataB_8TeVEle" \
"DataC_8TeVEle" \
"DataD_8TeVEle" 

do
  hadd \
   ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_${datasample}.root \
    ${hdfs}/${version}_${runname}-${datasample}_callHistoFiller*/*.root
    #${hdfs}/${version}/roots/${runname}/${version}_${runname}-${datasample}_callHistoFiller*/*.root
done

hadd ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data_mu.root \
 ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data*_8TeVMu*root

hadd ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data_ele.root \
 ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data*_8TeVEle*root

for myshift in "SFs" "JESUp" "JESDown" "MESUp" "MESDown" "EESUp" "EESDown"
do
 hadd \
  ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_DYan_${myshift}.root \
   ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Drell*${myshift}*root
done

echo
echo "${wbbzone}/SampleInfo/${version}/Analyzed_${runname}"
