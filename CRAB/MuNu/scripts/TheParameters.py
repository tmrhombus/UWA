#!/usr/bin/env python
'''
Parameters to be read by TheHistos.py and ThePlot.py
Author: T.M.Perry
'''

def arams():
 #lumi = 20090. # delivered for SV_3
 #lumi = 19742. # recorded for SV_3
 #lumi = 19488. #  for jresMet
 #lumi = 18027. # for moreSV_toe
 #lumi = 18589. # for looseID  19488.
 lumi = 19751. # NewPat
 #lumi = 19548. #post_synch_v0 

 btype = 't'
 njetcut = '25' #20,25,26,30,40
 jetcut = '25'
 I = 0
 F = 20
 iso_value = 0.12
 antiIso_value = 0.2
 extraCut = '(2>1)'
 #extraCut = '(J1SVMassb > 0 && J2SVMassb > 0)'
 #extraCut = '(vertixces > 25)'
 #extraCut = '(vertixces < 15)'

 #naming where output goes
 path = '../plots/NewlyRanged_'
 extraName = ''

 drawQCD = True
 drawData = True

 noMT = False # control but no mT cut
 Control = False # 1 mu, 0b, 2+ jets
 Ctl_Andrea = False # 1 mu, 1+ b, 2+ jets 
 Signal = True # 1 mu, 2bs, 2 jets
 TT_m = False #1 mu, 2b, 4 j
 TT_me = False # 1mu, 1e
 ST = False
 Z_Region = False # two muons, no mT cut
 Legacy = False #voids everything else and puts parametrs from 7Tev analysis
 Tomislav = False

 DataCard = True

 #eventTreeLocation = 'New_Tree'
 eventTreeLocation = 'muNuEventTree/eventTree'
 #eventTreeLocation = 'muNuEventTreeMuonUp/eventTree'
 #eventTreeLocation = 'muNuEventTreeMuonDown/eventTree'
 #eventTreeLocation = 'muNuEventTreeJetUp/eventTree'
 #eventTreeLocation = 'muNuEventTreeJetDown/eventTree'
 #eventTreeLocation = 'muNuEventTreeUCEUp/eventTree'
 #eventTreeLocation = 'muNuEventTreeUCEDown/eventTree'

 bNr = 0
 jNr = 2
 jetVeto = False

 if Signal or Legacy:
  bNr = 2
  #bNr = 2
  jNr = 2
  jetVeto = True
 elif Control or noMT:
  bNr = 0 
  jNr = 2
  jetVeto = False
 elif Ctl_Andrea:
  bNr = 1 
  jNr = 2
  jetVeto = False
 elif TT_m:
  bNr = 2
  jNr = 4
  jetVeto = True
 elif TT_me:
  bNr = 2 
  jNr = 2
  jetVeto = False
 elif Z_Region:
  bNr = 2
  jNr = 2
  jetVeto = False
 elif ST:
  bNr = 1
  jNr = 2
  jetVeto = True
 elif Tomislav:
  bNr = 0
  jNr = 2
  jetVeto = False
  njetcut = '20'
  jetcut = '20'

 drawW = False # line at W when plotting
 drawZ = False # line at Z when plotting

 if not DataCard:
  if eventTreeLocation == 'muNuEventTreeMuonUp/eventTree'  : extraName += 'mUP_'  
  if eventTreeLocation == 'muNuEventTreeMuonDown/eventTree': extraName += 'mDN_'  
  if eventTreeLocation == 'muNuEventTreeJetUp/eventTree'   : extraName += 'jUP_'  
  if eventTreeLocation == 'muNuEventTreeJetDown/eventTree' : extraName += 'jDN_'  
  if eventTreeLocation == 'muNuEventTreeUCEUp/eventTree'   : extraName += 'uUP_'
  if eventTreeLocation == 'muNuEventTreeUCEDown/eventTree' : extraName += 'uDN_'
 extraName += str(jNr)+'j'+njetcut+jetcut+'_'+str(bNr)+'b'+btype
 if Tomislav: extraName += '_tomi'
 if Z_Region: extraName += '_2mu'
 if noMT: extraName += '_noMT'
 if DataCard: extraName = 'Datacard_'+extraName
 if TT_me: extraName += '_1m1e'

 jet1_2dr2 = '(((J1_eta-J2_eta)*(J1_eta-J2_eta))+((J1_phi-J2_phi)*(J1_phi-J2_phi)))'

 leafs = [
#'J1_idBetaPu',
#'J1_idBetaClassicPu',
#'J1_idBetaStarPu',
#'J1_idBetaStarClassicPu',
#'J1_idBetaStarClassicModPu',
#'J1_PUID_fullDiscriminant',
#'J1_PUID_philv1Discriminant',
#'J1_fullIdLoosePu',
#'J2_fullIdLoosePu',
#'mt',
#'DiSVMass',
#'vertices',
#'(J1_mass_SSV+J2_mass_SSV)',
#'J2_mass_SSV',
#'J1_nTracks_SV',
#'J2_nTracks_SV',
#'J1_mass_SV_weighted',
#'J1_mass_SSV_alt',
#'J1_mass_SSV',
#'J1_mass_SV_unweighted',
#'J2_mass_SV_unweighted',
#'J2_mass_SV_weighted',
#'J1_normChi2_SV',
#'J2_normChi2_SV',
#'J1_flightDistance',
#'J1_flightDistanceError',
#'J1_normChi2_SV',
#'J1_pt_SSV',
#'J1_phi_SSV',
#'J1_eta_SSV',
#'J1_pt_PV',
#'J1_phi_PV',
#'J1_eta_PV',
#'J1_mass_PV',
#'J1_pt',
#'(J1_mass_SV_weighted+J2_mass_SV_weighted)',
#'J1_eta',
#'J1_phi',
#'muon_pt',
#'muon_eta',
#'muon_phi',
#'muonCharge',
#'J2_pt',
#'J2_eta',
#'J2_phi',
#'J2_mass_SSV_alt',
#'J2_mass_SSV',
#'J2_pt_SSV',
#'J2_phi_SSV',
#'J2_eta_SSV',
#'J2_pt_PV',
#'J2_phi_PV',
#'J2_eta_PV',
#'J2_mass_PV',
#'J3_pt',
#'J3_eta',
#'J3_phi',
#'J4_pt',
#'J4_eta',
#'J4_phi',
#'J1DR',
#'J2DR',
#'ht',
'met_pt',
#'met_phi',
#'DiMuonMass',
#'nJetsPt25',
#'nJetsPt30',
#'J1CSVbtag',
#'J2CSVbtag',
#jet1_2dr2,
#'dz',
#'Wpt',
#'ptJJ',
#'mJJ',
#'mJ3J4',
]

 return lumi,bNr,btype,jNr,njetcut,jetcut,I,F,iso_value,antiIso_value,path,extraName,leafs,drawW,drawZ,drawQCD,drawData,jetVeto,Control,Z_Region,Legacy,noMT,TT_m,TT_me,ST,Signal,Tomislav,eventTreeLocation,extraCut,Ctl_Andrea
