echo
echo "version: ${version}"
echo "runname: ${runname}"

mkdir -p ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}
mkdir -p ${wbbzone}/SampleInfo/${version}/Plots_${runname}

for samplename in \
"W1Jet" \
"W2Jet" \
"W3Jet" \
"W4Jet" \
"WJets" \
"Drell" \
"TTbar_full" \
"TTbar_semi" \
"T_s" \
"T_t" \
"T_tW" \
"Tbar_s" \
"Tbar_t" \
"Tbar_tW" \
"Wbb4F" \
"WW" \
"WZ" \
"ZZ" 

do
 echo "copying ${samplename}"
 for myshift in "SFs" "JESUp" "JESDown" "MESUp" "MESDown" "EESUp" "EESDown"
 do
#cp ${hdfs}/${version}/${version}_${runname}-${samplename}_${myshift}_callHistoFiller*/*.root \
cp ${hdfs}/${version}_${runname}-${samplename}_${myshift}_callHistoFiller*/*.root \
 ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_${samplename}_${myshift}.root
 done
done

#for datasample in \
#"DataA_8TeVMu" \
#"DataB_8TeVMu" \
#"DataC_8TeVMu" \
#"DataD_8TeVMu" \
#"DataA_8TeVEle" \
#"DataB_8TeVEle" \
#"DataC_8TeVEle" \
#"DataD_8TeVEle" 
#
#do
# echo "copying ${datasample}"
# #cp ${hdfs}/${version}/${version}_${runname}-${datasample}_callHistoFiller*/*.root \
# cp ${hdfs}/${version}_${runname}-${datasample}_callHistoFiller*/*.root \
#  ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_${datasample}.root
#done
#
#hadd ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data_mu.root \
# ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data*_8TeVMu*root
# hadd ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data_ele.root \
#  ${wbbzone}/SampleInfo/${version}/Analyzed_${runname}/Analyzed_Data*_8TeVEle*root
#
#echo
#echo "${wbbzone}/SampleInfo/${version}/Analyzed_${runname}"
