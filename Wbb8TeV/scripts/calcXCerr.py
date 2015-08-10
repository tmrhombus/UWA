import math

# W Jets
xc_WJets = 12234.4 # ( *3 )
scalesUp_WJets = 45.3
scalesDn_WJets = 21.3
pdf_WJets = 241.3

# TTbar from data 

# Drell
xc_Drell = 1177.3 # ( *3 )
scalesUp_Drell = 5.9
scalesDn_Drell = 3.6
pdf_Drell = 38.8

# T_t
xc_T_t = 56.4 # ( *0.327 )
scalesUp_T_t = 2.1
scalesDn_T_t = 0.3
pdf_T_t = 1.1

# Tbar_t 
xc_Tbar_t = 30.7
scalesUp_Tbar_t = 0.9
scalesDn_Tbar_t = 1.1
pdf_Tbar_t = 0.7

# T_s
xc_T_s = 3.79
scalesUp_T_s = 0.07
scalesDn_T_s = 0.07
pdf_T_s = 0.13

# Tbar_s
xc_Tbar_s = 1.76
scalesUp_Tbar_s = 0.01
scalesDn_Tbar_s = 0.01
pdf_Tbar_s = 0.08

# T_tW
xc_T_tW = 11.1
scalesUp_T_tW = 0.3
scalesDn_T_tW = 0.3
pdf_T_tW = 0.7

# Tbar_tW
xc_Tbar_tW = 11.1
scalesUp_Tbar_tW = 0.3
scalesDn_Tbar_tW = 0.3
pdf_Tbar_tW = 0.7

# WW
xc_WW = 56
scalesUp_WW = 2.3
scalesDn_WW = 2.3
pdf_WW = 2.

# WZ 
xc = 33.21 #CTEQ
xc = 33.85 #MSTW
xc = 33.72 #NNPDF

# ZZ
xc_ZZ = 8.2
scalesUp_ZZ = 0.3
scalesDn_ZZ = 0.3
pdf_ZZ = 0.3

scales_WJets   = max(scalesUp_WJets,scalesDn_WJets)
scales_Drell   = max(scalesUp_Drell,scalesDn_Drell)
scales_T_t     = max(scalesUp_T_t,scalesDn_T_t)
scales_Tbar_t  = max(scalesUp_Tbar_t,scalesDn_Tbar_t)
scales_T_s     = max(scalesUp_T_s,scalesDn_T_s)
scales_Tbar_s  = max(scalesUp_Tbar_s,scalesDn_Tbar_s)
scales_T_tW    = max(scalesUp_T_tW,scalesDn_T_tW)
scales_Tbar_tW = max(scalesUp_Tbar_tW,scalesDn_Tbar_tW)
scales_WW      = max(scalesUp_WW,scalesDn_WW)
scales_ZZ      = max(scalesUp_ZZ,scalesDn_ZZ)

err_WJets = math.sqrt(scales_WJets**2 + pdf_WJets**2) / xc_WJets
err_Drell = math.sqrt(scales_Drell**2 + pdf_Drell**2) / xc_Drell
err_T_t = math.sqrt(scales_T_t**2 + pdf_T_t**2) / xc_T_t
err_Tbar_t = math.sqrt(scales_Tbar_t**2 + pdf_Tbar_t**2) / xc_Tbar_t
err_T_s = math.sqrt(scales_T_s**2 + pdf_T_s**2) / xc_T_s
err_Tbar_s = math.sqrt(scales_Tbar_s**2 + pdf_Tbar_s**2) / xc_Tbar_s
err_T_tW = math.sqrt(scales_T_tW**2 + pdf_T_tW**2) / xc_T_tW
err_Tbar_tW = math.sqrt(scales_Tbar_tW**2 + pdf_Tbar_tW**2) / xc_Tbar_tW
err_WW = math.sqrt(scales_WW**2 + pdf_WW**2) / xc_WW
err_ZZ = math.sqrt(scales_ZZ**2 + pdf_ZZ**2) / xc_ZZ

print("WJets: %s"%err_WJets)
print("Drell: %s"%err_Drell)
print("T_t: %s"%err_T_t)
print("Tbar_t: %s"%err_Tbar_t)
print("T_s: %s"%err_T_s)
print("Tbar_s: %s"%err_Tbar_s)
print("T_tW: %s"%err_T_tW)
print("Tbar_tW: %s"%err_Tbar_tW)
print("WW: %s"%err_WW)
print("ZZ: %s"%err_ZZ)


