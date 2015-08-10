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
hadd ../data/Valentine/Analyzed/Analyzed_${samplename}_${myshift}.root /nfs_scratch/tperry/Valentine/Dupid/${samplename}/*/${samplename}_${myshift}*.root
 done
done

for datasample in \
"DataA_Mu" \
"DataB_Mu" \
"DataC_Mu" \
"DataD_Mu" \
"DataA_Ele" \
"DataB_Ele" \
"DataC_Ele" \
"DataD_Ele" 
do
hadd ../data/Valentine/Analyzed/Analyzed_${samplename}.root /nfs_scratch/tperry/Valentine/Dupid/${samplename}/*/${samplename}*.root
done

hadd ../data/Valentine/Analyzed/Analyzed_Data_mu.root ../data/Valentine/Analyzed/Analyzed_Data*_Mu*root
hadd ../data/Valentine/Analyzed/Analyzed_Data_ele.root ../data/Valentine/Analyzed/Analyzed_Data*_Ele*root
