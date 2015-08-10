for sample in 2j3030_2bt_1m1e 2j3535_2bt_1m1e 2j4040_2bt_1m1e
do
 for var in mt_new vertices
 do
  hadd "../plots/Halloween_tot_"$sample"_"$var".root" "../plots/Halloween_0_"$sample"_"$var".root" "../plots/Halloween_1_"$sample"_"$var".root"

 done
done
