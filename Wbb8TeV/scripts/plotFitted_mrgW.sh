for lep in "ele"  "mu" 
do

  wbb_file="mrgW_03_jes_${lep}_wbb_comparison"        
 ttme_file="mrgW_03_jes_${lep}_ttme_comparison"       
ttjjj_file="mrgW_03_jes_${lep}_ttjjj_comparison"      

#  wbb_file="mrgW_02_csv_${lep}_wbb_comparison"        
# ttme_file="mrgW_02_csv_${lep}_ttme_comparison"       
#ttjjj_file="mrgW_02_csv_${lep}_ttjjj_comparison"      
 
#  wbb_file="mrgW_Oflo_01_nToGiu_${lep}_wbb_comparison"        
# ttme_file="mrgW_Oflo_01_nToGiu_${lep}_ttme_comparison"       
#ttjjj_file="mrgW_Oflo_01_nToGiu_${lep}_ttjjj_comparison"      

#version="04T_fitWbb"
#runname="04_WbbAsT"
#runname="03_WbbAsG"

#version="mrgW_02T_fitTTme" # folder
#runname="03_mrgW_TTme" # mlfit_XXXX_full

version="mrgW_03T_fitWbb" # folder
runname="04_mrgW_Wbb" # mlfit_XXXX_full

 ##  plots
 for loc in "_Wi" "_Tr" 
 do
  for wbb in '4' '5'
  do
   for ttsample in  'ttme' #'ttjjj'  
   do  
  
    if [ "$ttsample" = "ttme" ]
    then 
     tt_file=$ttme_file
    else 
     tt_file=$ttjjj_file
    fi  

    #python plotFitted_mrgW.py \
    # $wbb \
    # $ttsample \
    # $tt_file${loc} \
    # $lep \
    # $version \
    # $runname \
    # $loc \
    # "TTbr"
  
    python plotFitted_mrgW.py \
     $wbb \
     $ttsample \
     $wbb_file${loc} \
     $lep \
     $version \
     $runname \
     $loc \
     "UUbb"
 
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
#h_Wbb4F_Tr->Integral()
#h_Wcc_Tr->Integral()
#h_TTbar_Tr->Integral()
#h_TTqcd_Tr->Integral()
#h_Drell_Tr->Integral()
#h_T_Tr->Integral()
#h_VV_Tr->Integral()
#h_Wl_Tr->Integral()
#
