
def actor(rescale=False):

 # pre-fit (wbb)
 Pre_QCD   = 192.1
 Pre_Drell = 164.5
 Pre_T     = 605.7
 Pre_TTbar = 2465.4
 Pre_Tbar  = 206.9
 Pre_VV    = 109.7
 Pre_Wbb   = 883.6
 Pre_Wcc   = 54.2
 Pre_tW    = 82.5

# # pre-fit (ttbar)
# Pre_QCD   = 15.7
# Pre_T     = 51.4
# Pre_TTbar = 2679.5
# Pre_Tbar  = 17.3
# Pre_Wbb   = 22.5
# Pre_tW    = 54.9

# # post-fit (wbb only) 
# Wbb_QCD   = 377.807
# Wbb_Drell = 149.581
# Wbb_T     = 617.394
# Wbb_TTbar = 2618.356
# Wbb_Tbar  = 206.375
# Wbb_VV    = 103.731
# Wbb_Wbb   = 1154.425
# Wbb_Wcc   =  82.523
# Wbb_tW    =  86.123
 
# # post-fit (ttbar only)
# TTbar_QCD   =  15.700
# TTbar_T     =  52.968
# TTbar_TTbar = 3009.716
# TTbar_Tbar  =  18.192
# TTbar_Wbb   =  39.784
# TTbar_tW    =  67.068

 # post-fit (both)
 TTbar_QCD   =  15.700
 TTbar_T     =  52.833
 TTbar_TTbar = 3010.031
 TTbar_Tbar  =  17.941
 TTbar_Wbb   =  38.987
 TTbar_tW    =  67.760
 Wbb_QCD     = 498.875
 Wbb_Drell   = 147.860
 Wbb_T       = 533.457
 Wbb_TTbar   = 2408.834
 Wbb_Tbar    = 192.626
 Wbb_VV      = 103.599
 Wbb_Wbb     = 1311.936
 Wbb_Wcc     = 106.215
 Wbb_tW      =  85.207
 
 sf_Signal_QCD   = 1. 
 sf_Signal_Drell = 1. 
 sf_Signal_T     = 1. 
 sf_Signal_TTbar = 1. 
 sf_Signal_Tbar  = 1. 
 sf_Signal_VV    = 1. 
 sf_Signal_Wbb   = 1. 
 sf_Signal_Wcc   = 1. 
 sf_Signal_tW    = 1. 

 sf_TTbar_QCD    = 1. 
 sf_TTbar_T      = 1. 
 sf_TTbar_TTbar  = 1. 
 sf_TTbar_Tbar   = 1. 
 sf_TTbar_Wbb    = 1. 
 sf_TTbar_tW     = 1. 

 if rescale:
  sf_Signal_QCD   = Wbb_QCD   / Pre_QCD  
  sf_Signal_Drell = Wbb_Drell / Pre_Drell
  sf_Signal_T     = Wbb_T     / Pre_T    
  sf_Signal_TTbar = Wbb_TTbar / Pre_TTbar
  sf_Signal_Tbar  = Wbb_Tbar  / Pre_Tbar 
  sf_Signal_VV    = Wbb_VV    / Pre_VV   
  sf_Signal_Wbb   = Wbb_Wbb   / Pre_Wbb  
  sf_Signal_Wcc   = Wbb_Wcc   / Pre_Wcc  
  sf_Signal_tW    = Wbb_tW    / Pre_tW   

  sf_TTbar_QCD    = TTbar_QCD   / Pre_QCD   
  sf_TTbar_T      = TTbar_T     / Pre_T     
  sf_TTbar_TTbar  = TTbar_TTbar / Pre_TTbar 
  sf_TTbar_Tbar   = TTbar_Tbar  / Pre_Tbar  
  sf_TTbar_Wbb    = TTbar_Wbb   / Pre_Wbb   
  sf_TTbar_tW     = TTbar_tW    / Pre_tW    

 print(sf_Signal_QCD  ) 
 print(sf_Signal_Drell) 
 print(sf_Signal_T    ) 
 print(sf_Signal_TTbar) 
 print(sf_Signal_Tbar ) 
 print(sf_Signal_VV   ) 
 print(sf_Signal_Wbb  ) 
 print(sf_Signal_Wcc  ) 
 print(sf_Signal_tW   ) 

 print(sf_TTbar_QCD   ) 
 print(sf_TTbar_T     ) 
 print(sf_TTbar_TTbar ) 
 print(sf_TTbar_Tbar  ) 
 print(sf_TTbar_Wbb   ) 
 print(sf_TTbar_tW    ) 

 return sf_Signal_QCD, sf_Signal_Drell, sf_Signal_T, sf_Signal_TTbar, sf_Signal_Tbar, sf_Signal_VV, sf_Signal_Wbb, sf_Signal_Wcc, sf_Signal_tW, sf_TTbar_QCD, sf_TTbar_T, sf_TTbar_TTbar, sf_TTbar_Tbar, sf_TTbar_Wbb, sf_TTbar_tW 
