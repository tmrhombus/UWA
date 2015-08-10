#!/bin/sh

# just to get rid of annoying output from pushing/popping
pushd () { 
 command pushd "$@" > /dev/null 
}
popd () {
 command popd "$@" > /dev/null
}

runname="Dupid" #=$version

base_in_dir=root://cmsxrootd.hep.wisc.edu//store/user/tperry/
base_submit_dir=/nfs_scratch/tperry/$version/$runname/

shifts[0]="SFs"
shifts[1]="JESUp"
shifts[2]="JESDown"
shifts[3]="LESUp"
shifts[4]="LESDown"

samplename=TTbar_semi
 
psdir=""
nrE=""
xc=""
# copy file list generated by countEvents.sh
cp '../data/'"$version"'/list_'"$samplename"'.txt' \
   '../data/'"$version"'/ez_list_'"$samplename"'.txt'
# cp '../data/'"$version"'/list_'"$samplename"'TEST.txt' \
#    '../data/'"$version"'/ez_list_'"$samplename"'.txt'
mylist='../data/'"$version"'/ez_list_'"$samplename"'.txt'

# relevant parameters for this sample
if [[ "$samplename" == "Drell" ]]
then
 psdir[0]="$version"'_Drell-MuEle-PATMC_V7A/'
 nrE="29997285"
 xc="3531.9" 
elif [[ "$samplename" == "TTbar_full" ]]
then
 psdir[0]="$version"'_TTbar_full-MuEle-PATMC_V7A/'
 nrE="10429331"
 xc="25.257" #240.6*0.324*0.324
elif [[ "$samplename" == "TTbar_semi" ]]
then
 psdir[0]="$version"'_TTbar_semi-MuEle-PATMC_V7A/'
 nrE="23492957"
 xc="105.394" #240.6*0.324*0.676*2
elif [[ "$samplename" == "T_s" ]]
then
 psdir[0]="$version"'_T_s-MuEle-PATMC_V7A/'
 nrE="259961"
 xc="3.79"
elif [[ "$samplename" == "T_t" ]]
then
 psdir[0]="$version"'_T_t-MuEle-PATMC_V7A/'
 nrE="3915598"
 xc="18.44" #56.4*0.327
elif [[ "$samplename" == "T_tW" ]]
then
 psdir[0]="$version"'_T_tW-MuEle-PATMC_V7A/'
 nrE="476173"
 xc="11.1" 
elif [[ "$samplename" == "Tbar_s" ]]
then
 psdir[0]="$version"'_Tbar_s-MuEle-PATMC_V7A/'
 nrE="139974"
 xc="1.76"
elif [[ "$samplename" == "Tbar_t" ]]
then
 psdir[0]="$version"'_Tbar_t-MuEle-PATMC_V7A/'
 nrE="1711403"
 xc="10.04"
elif [[ "$samplename" == "Tbar_tW" ]]
then
 psdir[0]="$version"'_Tbar_tW-MuEle-PATMC_V7A/'
 nrE="484502"
 xc="11.1" 
elif [[ "$samplename" == "W1Jet" ]]
then
 psdir[0]="$version"'_W1Jet_p1-MuEle-PATMC_V7A'
 psdir[1]="$version"'_W1Jet_p2-MuEle-PATMC_V19'
 nrE="12345" # doesn't matter, hardcoded in histoFiller.C
 xc="36703.2" 
elif [[ "$samplename" == "W2Jet" ]]
then
 psdir[0]="$version"'_W2Jet_p1-MuEle-PATMC_V7A'
 psdir[1]="$version"'_W2Jet_p2-MuEle-PATMC_V19'
 nrE="12345" # doesn't matter, hardcoded in histoFiller.C
 xc="36703.2" 
elif [[ "$samplename" == "W3Jet" ]]
then
 psdir[0]="$version"'_W3Jet_p1-MuEle-PATMC_V7A'
 psdir[1]="$version"'_W3Jet_p2-MuEle-PATMC_V19'
 nrE="12345" # doesn't matter, hardcoded in histoFiller.C
 xc="36703.2" 
elif [[ "$samplename" == "W4Jet" ]]
then
 psdir[0]="$version"'_W4Jet-MuEle-PATMC_V7A'
 nrE="12345" # doesn't matter, hardcoded in histoFiller.C
 xc="36703.2" 
elif [[ "$samplename" == "WJets" ]]
then
 psdir[0]="$version"'_WJets_p1-MuEle-PATMC_V7A'
 psdir[1]="$version"'_WJets_p2-MuEle-PATMC_V7A'
 nrE="12345" # doesn't matter, hardcoded in histoFiller.C
 xc="36703.2" 
elif [[ "$samplename" == "Wbb4F" ]]
then
 psdir[0]="$version"'_Wbb4F-MuEle-PATMC_V7A'
 nrE="20294311"
 xc="138.9" #46.3*3 
elif [[ "$samplename" == "WW" ]]
then
 psdir[0]="$version"'_WW-MuEle-PATMC_V7A'
 nrE="10000431"
 xc="56.75" 
elif [[ "$samplename" == "WZ" ]]
then
 psdir[0]="$version"'_WZ-MuEle-PATMC_V7A'
 nrE="9979363"
 xc="33.21" 
elif [[ "$samplename" == "ZZ" ]]
then
 psdir[0]="$version"'_ZZ-MuEle-PATMC_V7A'
 nrE="9799908"
 xc="8.26" 
fi

# where am I
echo $samplename
echo " "$nrE" events"
echo " "$xc" xc"
for psdir in "${psdir[@]}"
do
 echo " "$psdir
 echo " "
 
 # cut path, .root from file list
 sed -i 's/^.*\(\/MuEle-PATMC\)/MuEle-PATMC/g' $mylist
 sed -i 's/.root//g' $mylist

 # for each file from list... submit
 while read filename
 do

  # initialize submission files
  cp template_runCondor.sh $samplename"_runCondor.sh"
  touch "$samplename"'_runHistoFiller.sh'
  chmod a+x "$samplename"'_runHistoFiller.sh'
  cat >>"$samplename"'_runHistoFiller.sh' <<EOF
#!/bin/sh
EOF
 
  # for shift in list above
  for myshift in "${shifts[@]}"
  do

   inputFileName=$base_in_dir$psdir$filename".root"
   submit_dir=$base_submit_dir$samplename"/"$filename
   mkdir -p $submit_dir 
   
   # callHistoFiller.cc
   # activate correct file, nrEvents, crosssec ... in callHistoFiller.cc
   cp template_callHistoFiller.cc                  $samplename$myshift'_callHistoFiller.cc'
   sed -i 's@PSANDSHIFT@'"$samplename$myshift"'@g' $samplename$myshift"_callHistoFiller.cc"
   sed -i "s@PSNAME@$samplename@g"                 $samplename$myshift"_callHistoFiller.cc"
   sed -i "s@SAMPLENAME@$inputFileName@g"          $samplename$myshift"_callHistoFiller.cc"
   sed -i "s@FILENAME@$filename@g"                 $samplename$myshift"_callHistoFiller.cc"
   sed -i "s@NREVENTS@$nrE@g"                      $samplename$myshift"_callHistoFiller.cc"
   sed -i "s@CROSSSEC@$xc@g"                       $samplename$myshift"_callHistoFiller.cc"
   sed -i "s@SHIFT@$myshift@g"                     $samplename$myshift"_callHistoFiller.cc"
   mv $samplename$myshift"_callHistoFiller.cc" $submit_dir/

   # runHistoFiller.cc
   # add shifted xx_callHistoFiller.cc to _runHistoFiller
   cat >>"$samplename"'_runHistoFiller.sh' <<EOF
root -l -b -q ${samplename}${myshift}_callHistoFiller.cc
EOF
  # runCondor.sh
  sed -i "s@transfer_input_files =@transfer_input_files = ${submit_dir}/${samplename}${myshift}_callHistoFiller.cc,@g" \
   $samplename'_runCondor.sh'
  done #myshift
  
  # bring (executable) _runHistoFiller to submitdir
  mv $samplename"_runHistoFiller.sh" $submit_dir/
  
  # runCondor.sh
  sed -i 's@SUBMITDIR@'"$submit_dir"'@g' $samplename'_runCondor.sh'
  sed -i 's@PSNAME@'"$samplename"'@g'    $samplename'_runCondor.sh'
  mv $samplename'_runCondor.sh' $submit_dir/
  
  # now go to the submit directory and submit
  pushd $submit_dir
  source "$samplename"'_runCondor.sh'
  condor_submit submit > submit.log
  popd
  done < $mylist #filename
 done #psdir
