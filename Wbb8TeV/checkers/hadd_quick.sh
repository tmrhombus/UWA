
rebase="/afs/hep.wisc.edu/cms/tperry/Wbb_CMSSW_5_3_14_patch1/src/UWAnalysis/Wbb8TeV"

mkdir -p ${rebase}/SampleInfo/${version}/Analyzed_typical
mkdir -p ${rebase}/SampleInfo/${version}/Plots_typical

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
"WZ" \
"ZZ" 

do
 for myshift in "SFs" "JESUp" "JESDown" "LESUp" "LESDown"
 do
hadd ${rebase}/SampleInfo/${version}/Analyzed_typical/Analyzed_${samplename}_${myshift}.root \
 ${hdfs}/${version}_typical-${samplename}_${myshift}_callHistoFiller/*.root
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
 hadd ${rebase}/SampleInfo/${version}/Analyzed_typical/Analyzed_${datasample}.root ${hdfs}/${version}_typical-${datasample}_callHistoFiller/*.root
done

hadd ${rebase}/SampleInfo/${version}/Analyzed_typical/Analyzed_Data_mu.root \
 ${rebase}/SampleInfo/${version}/Analyzed_typical/Analyzed_Data*_8TeVMu*root
hadd ${rebase}/SampleInfo/${version}/Analyzed_typical/Analyzed_Data_ele.root \
 ${rebase}/SampleInfo/${version}/Analyzed_typical/Analyzed_Data*_8TeVEle*root
