#!/usr/bin/env python
'''
Define the qcd scale given Isolation, nr of jets, nr of bs
'''
def scaleMe(isNr,jNr,bNr,xmin,xmax,d,m,dm):
 if dm:
  if jNr==2:
   if bNr==0:
    if isNr==2:
     if xmin==0:
      if xmax==20:
       qcdScale = 0.707092#0.631696
      elif xmax==30:
       qcdScale = 0.723064#0.647732
      elif xmax==40:
       qcdScale = 0.778217#0.685517
      elif xmax==70:
       qcdScale = 0.808664#100
      elif xmax==200:
       qcdScale = 0.802429#0.68908
#     elif xmin==30:
#      if xmax==80:
#       qcdScale = 100
#    elif isNr==3:
#     if xmin==0:
#      if xmax==20:
#       qcdScale = 0.847802
#      elif xmax==30:
#       qcdScale = 0.868652
#      elif xmax==40:
#       qcdScale = 0.918515
#      elif xmax==70:
#       qcdScale = 100
#      elif xmax==200:
#       qcdScale = 0.925656
#     elif xmin==30:
#      if xmax==80:
#       qcdScale = 100
#    elif isNr==4:
#     if xmin==0:
#      if xmax==20:
#       qcdScale = 1.3489
#      elif xmax==30:
#       qcdScale = 1.38055
#      elif xmax==40:
#       qcdScale = 1.45912
#      elif xmax==70:
#       qcdScale = 100
#      elif xmax==200:
#       qcdScale = 1.47088
#     elif xmin==30:
#      if xmax==80:
#       qcdScale = 100
 
  elif jNr==3:
   if bNr==1:
    if isNr==2:
     if xmin==0:
      if xmax==20:
       qcdScale = 1.03649#0.833011
      elif xmax==30:
       qcdScale = 1.07354#0.870236
      elif xmax==40:
       qcdScale = 1.19864#0.985917
      elif xmax==70:
       qcdScale = 1.45047#100
      elif xmax==200:
       qcdScale = 1.65729#1.25107
#    elif isNr==3:
#     if xmin==0:
#      if xmax==20:
#       qcdScale = 1.06599
#      elif xmax==30:
#       qcdScale = 1.10606
#      elif xmax==40:
#       qcdScale = 1.25504
#      elif xmax==70:
#       qcdScale = 100
#      elif xmax==200:
#       qcdScale = 1.67063
#    elif isNr==4:
#     if xmin==0:
#      if xmax==20:
#       qcdScale = 1.5889
#      elif xmax==30:
#       qcdScale = 1.63237
#      elif xmax==40:
#       qcdScale = 1.84801
#      elif xmax==70:
#       qcdScale = 100
#      elif xmax==200:
#       qcdScale = 2.66928

  
  elif jNr==4:
   if bNr==1:
    if isNr==2:
     if xmin==0:
      if xmax==20:
       qcdScale = 1.58605#1.06208#
      elif xmax==30:
       qcdScale = 1.9404#1.25593#
      elif xmax==40:
       qcdScale = 2.11776#1.66191#
      elif xmax==70:
       qcdScale = 2.43802#2.07335#
      elif xmax==200:
       qcdScale = 3.66367#3.97309#
#    elif isNr==3:
#     if xmin==0:
#      if xmax==20:
#       qcdScale = 1.31391#1.05062
#      elif xmax==30:
#       qcdScale = 1.43665#1.30549
#      elif xmax==40:
#       qcdScale = 1.86493#1.90146
#      elif xmax==70:
#       qcdScale = 2.54748#2.66358
#      elif xmax==200:
#       qcdScale = 3.60845#5.15915
#    elif isNr==4:
#     if xmin==0:
#      if xmax==20:
#       qcdScale = 1.65256#1.243
#      elif xmax==30:
#       qcdScale = 1.87195#1.6523
#      elif xmax==40:
#       qcdScale = 3.22785#3.46509
#      elif xmax==70:
#       qcdScale = 4.22678#4.78794
#      elif xmax==200:
#       qcdScale = 7.25228#8.72802
 
  #elif jNr==4:
  # if bNr==2:
  #  if isNr==2:
  #   if xmin==0:
  #    if xmax==20:
  #     qcdScale = 
  #    elif xmax==30:
  #     qcdScale = 
  #    elif xmax==40:
  #     qcdScale = 
  #    elif xmax==70:
  #     qcdScale = 
  #    elif xmax==200:
  #     qcdScale = 
  #  elif isNr==3:
  #   if xmin==0:
  #    if xmax==20:
  #     qcdScale = 
  #    elif xmax==30:
  #     qcdScale = 
  #    elif xmax==40:
  #     qcdScale = 
  #    elif xmax==70:
  #     qcdScale = 
  #    elif xmax==200:
  #     qcdScale = 
  #  elif isNr==4:
  #   if xmin==0:
  #    if xmax==20:
  #     qcdScale = 
  #    elif xmax==30:
  #     qcdScale = 
  #    elif xmax==40:
  #     qcdScale = 
  #    elif xmax==70:
  #     qcdScale = 
  #    elif xmax==200:
  #     qcdScale = 

 elif d:
  print('')
  print('you should probably recompute the qcd scale factor')
  print('')
  #############Isolation > 0.2 b stuff
  ###mT 3j
  #qcdScale=0.0589111#0,120#0.0559659#all
  ###mT 3j1b
  #qcdScale=0.108118#0,120#0.0882448#all
  ###mT 3j2b
  #qcdScale=0.127431#0,120#0.119772#all
  ###mT 4j
  #qcdScale=0.0482024#0,120#0.0449556#all
  ###mT 4j1b
  #qcdScale=0.0856135#0,120
  ###mT 4j2b
  #qcdScale=0.0706503#0,120#0.0596653#all
  
  ################Isolation > 0.2 MT cut
  ### 2j 50+
  #qcdScale=0.0328839002045#0,120#0.0321276905535#all
  ### 3j 50+
  #qcdScale=0.0338264405702#0,120#0.032135322362#all
  ### 3j1b 50+
  #qcdScale=0.0676235689197#0,120#0.0570773236346#all
  ### 3j2b 50+
  #qcdScale=0.0970954465419#0,120#0.0912597100685#all
  ### 4j 50+
  #qcdScale=0.035716244#0,120#0.033310482124#all
  ### 4j1b 50+
  #qcdScale=0.0720848960342#0,120
  ### 4j2b 50+
  #qcdScale=0.0662690824015#0,120#0.0559652916538#all
  
  ############Isolation > 0.2 2j
  ###mT  2j
  #qcdScale=0.0801605#0,120#0.0783171#all
  ###mT  2j 0-20
  #qcdScale=0.169307
  ###mT  2j 0-30
  #qcdScale=0.159932
  ###mT  2j 0-40
  #qcdScale=0.148325
  ###mT  2j 0-70
  #qcdScale=0.101976
  ###mT  2j 30-80
  #qcdScale=0.052359
  
  ###################### Isolation > 0.3
  ###mT  2j
  #qcdScale=
  ###mT  2j 0-20
  #qcdScale=0.169307
  ###mT  2j 0-30
  #qcdScale=0.159961
  ###mT  2j 0-40
  #qcdScale=0.148324
  ###mT  2j 0-70
  #qcdScale=0.101258
  ###mT  2j 30-80
  #qcdScale=0.0535244
  
  ###################### Isolation > 0.4
  ###mT  2j
  #qcdScale=
  ###mT  2j 0-20
  #qcdScale=0.169217
  ###mT  2j 0-30
  #qcdScale=0.159962
  ###mT  2j 0-40
  #qcdScale=0.148308
  ###mT  2j 0-70
  #qcdScale=0.101479
  ###mT  2j 30-80
  #qcdScale=0.0535178

 elif m:
  print('')
  print('you should probably recompute the qcd scale factor')
  print('')
  #qcd from mc
  ###mT 2j 0-20
  #qcdScale =0.165475
  ###mT 2j 0-30
  #qcdScale =0.150013
  ###mT 2j 0-40
  #qcdScale = 0.134459
  ###mT 2j 0-70
  #qcdScale = 0.0819064
  ###mT 2j 30-80
  #qcdScale = 0.0495104 


 return qcdScale
