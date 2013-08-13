#!/usr/bin/env python
'''
Parameters for TError...py 
Author: T.M.Perry UW
'''

def arams():
 
 leaf ='highestJetPt'
 
 Control = False #one muon
 Signal = False
 noMT = False # control but no mT cut
 TT_m = True #1 mu, 2b's, 4 j
 TT_me = False #no b's, 1mu 1e

 bNr = 0
 jNr = 2
 jetVeto = False

 if Signal:
  bNr = 2
  jNr = 2
  jetVeto = True
 elif Control or noMT:
  bNr = 0 
  jNr = 2
  jetVeto = False
 elif TT_m:
  bNr = 2
  jNr = 4
  jetVeto = True
 elif TT_me:
  bNr = 0 
  jNr = 4
  jetVeto = False

 path = '../plots/TTbarError_new_'
 extraName='_'+str(jNr)+'j_'+str(bNr)+'b'
 name = path+extraName+'_'+leaf

 return leaf,name,bNr,jNr,jetVeto,Signal,Control,TT_m,TT_me,noMT
