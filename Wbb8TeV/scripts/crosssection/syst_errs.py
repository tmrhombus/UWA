import math
# Removing the following systematic gives this fit
#

 # EES      1.2870e+00 +/- 0.220
 # EMu      1.2874e+00 +/- 0.220
 # JES      1.2703e+00 +/- 0.209
 # MES      1.2746e+00 +/- 0.216
 # UES      1.2882e+00 +/- 0.218
 # bgCSVsf  1.2545e+00 +/- 0.144
 # bgDY     1.2871e+00 +/- 0.220
 # bgGJ     1.2888e+00 +/- 0.220
 # bgJESsf  1.2981e+00 +/- 0.216
 # bgQCDele 1.3105e+00 +/- 0.220
 # bgQCDmu  1.2124e+00 +/- 0.214
 # bgTTbar  1.2150e+00 +/- 0.175
 # bgT      1.2824e+00 +/- 0.217
 # bgVV     1.2873e+00 +/- 0.220
 # bgWcc    1.2869e+00 +/- 0.220
 # bgWl     1.2746e+00 +/- 0.220
 # full     1.2870e+00 +/- 0.221

 # stats    1.3231e+00 +/-  4.65e-02


systs=[
 "EES      ",    
 "EMu      ",   
 "JES      ", 
 "MES      ",
 "UES      ",
 "bgCSVsf  ",
 "bgDY     ",
 "bgGJ     ",
 "bgJESsf  ",
 "bgQCDele ",
 "bgQCDmu  ",
 "bgTTbar  ",
 "bgT      ",
 "bgVV     ",
 "bgWcc    ",
 "bgWl     ",
 "full     "
]

uncs=[
0.220,
0.220,
0.209,
0.216,
0.218,
0.144,
0.220,
0.220,
0.216,
0.220,
0.214,
0.175,
0.217,
0.220,
0.220,
0.220,
0.221
]

for syst,unc in zip(systs,uncs):
 print(" %s %.4f"%(syst, math.sqrt(abs((pow(0.220,2) - pow(unc,2))))/1.287   )  )


#print(" Syst Mu  :  %.4f"%( 0.51 * math.sqrt(abs((pow(0.239,2) - pow(0.0610,2))))/1.2147   )  )
#print(" Syst Ele :  %.4f"%( 0.51 * math.sqrt(abs((pow(0.280,2) - pow(0.0717,2))))/1.3492   )  )
#print(" Syst Comb:  %.4f"%( 0.51 * math.sqrt(abs((pow(0.220,2) - pow(0.0465,2))))/1.2870   )  )


#print("")
#print(" Syst Mu  :  %.4f"%( 0.51 * 0.0610 ) )
#print(" Syst Ele :  %.4f"%( 0.51 * 0.0717 ) )
#print(" Syst Comb:  %.4f"%( 0.51 * 0.0465 ) )
 
