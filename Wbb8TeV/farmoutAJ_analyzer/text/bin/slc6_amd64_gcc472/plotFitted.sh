for lep in "ele" "mu" 
do

#  wbb_file="04_qcd_${lep}_wbb_comparison"        
# ttme_file="04_qcd_${lep}_ttme_comparison"       
#ttjjj_file="04_qcd_${lep}_ttjjj_comparison"      

#  wbb_file="03_jest_${lep}_wbb_comparison"        
# ttme_file="03_jest_${lep}_ttme_comparison"       
#ttjjj_file="03_jest_${lep}_ttjjj_comparison"      

#  wbb_file="02_csvgsf_${lep}_wbb_comparison"        
# ttme_file="02_csvgsf_${lep}_ttme_comparison"       
#ttjjj_file="02_csvgsf_${lep}_ttjjj_comparison"      
 
  wbb_file="Oflo_01_nToGiu_${lep}_wbb_comparison"        
 ttme_file="Oflo_01_nToGiu_${lep}_ttme_comparison"       
ttjjj_file="Oflo_01_nToGiu_${lep}_ttjjj_comparison"      

#version="04T_fitWbb_v2" #directory
#runname="04_WbbAsT"  #mlfit_XXX_full

#version="03T_fitTTme_v2" #directory
#runname="03_TTmeAsT"  #mlfit_XXX_full

version="01T_fitTTjjj_v2" #directory
runname="02_TTjjjAsT"  #mlfit_XXX_full

 ##  plots
 for loc in "_Wi" "_Tr" 
 do
  for wbb in '4F' '5F'
  do
   for ttsample in  'ttjjj' #'ttme'
   do  
  
    if [ "$ttsample" = "ttme" ]
    then 
     tt_file=$ttme_file
    else 
     tt_file=$ttjjj_file
    fi  
  
    python plotFitted.py \
     $wbb \
     $ttsample \
     $tt_file${loc} \
     $lep \
     $version \
     $runname \
     $loc \
     "TTbr"


     #$tt_file${loc} \
     #$wbb_file${loc} \
 
   done #for ttsample in 'ttjjj' 'ttme'
  done #for wbb in '4F' '5F'
 done #for loc in "_Wi" "_Tr" 

done # for lep in "mu" "ele"


#_file0->cd();
#fit_s->Print();
#
#shapes_prefit->cd();
#TTbr->cd();
#
#h_Wbb4F_Tr->Integral()
#h_Wcc_Tr->Integral()
#h_TTbar_Tr->Integral()
#h_TTqcd_Tr->Integral()
#h_Drell_Tr->Integral()
#h_T_Tr->Integral()
#h_VV_Tr->Integral()
#h_Wl_Tr->Integral()
#
#_file0->cd();
#shapes_fit_s->cd();
#TTbr->cd();
#
#h_Wbb4F_Wi->Integral()
#h_Wcc_Wi->Integral()
#h_TTbar_Wi->Integral()
#h_qcd_mu_Wi->Integral()
#h_Drell_Wi->Integral()
#h_T_Wi->Integral()
#h_VV_Wi->Integral()
#h_Wl_Wi->Integral()

