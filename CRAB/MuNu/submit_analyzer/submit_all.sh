## choose sample
#for samplename in \
#"W1Jet" \
#"W2Jet" \
#"W3Jet" \
#"W4Jet" \
#"WJets" \
#"Wbb4F" \
#"WW" \
#"WZ" \
#"ZZ" 
#
#
##"Drell" \
##"TTbar_full" \
##"TTbar_semi" \
##"T_s" \
##"T_t" \
##"T_tW" \
##"Tbar_s" \
##"Tbar_t" \
##"Tbar_tW" \
#
#do 
# cp template_submitter.sh ${samplename}_submitter.sh
# sed -i "s@THESAMPLE@${samplename}@g" ${samplename}_submitter.sh
# nohup bash ${samplename}_submitter.sh > ${samplename}_submit.out 2>&1&
#done
#

for samplename_mu in \
 "DataA_Mu" \
 "DataB_Mu" \
 "DataC_Mu" \
 "DataD_Mu"

do 
 cp template_data_submitter.sh           ${samplename_mu}_submitter.sh
 sed -i "s@THESAMPLE@${samplename_mu}@g" ${samplename_mu}_submitter.sh
 sed -i "s@LEPTON@Mu@g"                  ${samplename_mu}_submitter.sh
 nohup bash ${samplename_mu}_submitter.sh > ${samplename_mu}_submit.out 2>&1&
done

for samplename_ele in \
 "DataA_Ele" \
 "DataB_Ele" \
 "DataC_Ele" \
 "DataD_Ele"

do 
 cp template_data_submitter.sh           ${samplename_ele}_submitter.sh
 sed -i "s@THESAMPLE@${samplename_ele}@g" ${samplename_ele}_submitter.sh
 sed -i "s@LEPTON@Ele@g"                  ${samplename_ele}_submitter.sh
 nohup bash ${samplename_ele}_submitter.sh > ${samplename_ele}_submit.out 2>&1&
done
