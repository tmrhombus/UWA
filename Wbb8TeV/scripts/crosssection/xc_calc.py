# calculate the cross section and errors

import math
#    
#Full Fits
# Mu    1.2142e+00 +/-  2.40e-01
# Ele   1.3489e+00 +/-  2.80e-01
# Comb  1.2870e+00 +/-  2.21e-01

#Stastical only fits
# Mu    1.2557e+00 +/-  6.09e-02
# Ele   1.4135e+00 +/-  7.16e-02
# Comb  1.3231e+00 +/-  4.65e-02
#


leps=["mu","ele","comb"]

# signal strength
sss=[1.2142,1.3489,1.2870]
# signal strength errors
sserrs=[0.240,0.280,0.221]

# signal strength errors from stat only fit
staterrs=[0.0609,0.0716,0.0465]

# theory (5F) xc
xct=0.51
# theory uncertainties
errxct=0.01
erracc=0.1

print("\n")
print("Uncertainties calculated relative to xc_theory x signal strength")
for lep,ss,sserr,staterr in zip(leps,sss,sserrs,staterrs):
 print(" %4s xc:  %.4f +- %.4f (stat) +- %.4f (syst) +- %.4f (theo) +- %.4f (lumi) pb "%( 
   lep,            # name
   ss*xct,         # xc obs
   ss*staterr*xct, # stat error
   math.sqrt( ((ss*sserr*xct)*(ss*sserr*xct)) - ((ss*staterr*xct)*(ss*staterr*xct)) ), # syst err
   ss*xct*math.sqrt( errxct*errxct + erracc*erracc ),
   ss*xct*0.026
   ))
print("\n")
