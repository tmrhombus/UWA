'''
Look Up Table for plotting info
Author: T.M.Perry UW
'''

def ranger(leaf): 
 steps = None
 xmin = None
 xmax = None
 setLogY = False
 if leaf=='muon_pt':
   steps = 50
   xmin = 0.
   xmax = 200.
   xtitle = 'p_{T}^{#mu}'
   xunits = 'GeV'
 elif leaf=='mt' or leaf == 'MtCal':
   steps =50 
   xmin = 0.
   xmax = 200.
   xtitle = 'Transverse Mass'
   xunits = 'GeV'
 elif leaf == 'MET' or leaf == 'met':
   steps = 50
   xmin = 0.
   xmax = 200.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'vertices':
   steps = 60
   xmin = 0.
   xmax = 40.
   xtitle = 'Nr. Vertices'
   xunits = None
 elif leaf == 'DiMuonMass':
   steps = 100
   xmin = 0.
   xmax = 200.
   xtitle = 'm^{#mu#mu}'
   xunits = 'GeV'
 elif leaf == 'muon_eta':
   steps = 20
   xmin = -3.
   xmax = 5.
   xtitle = '#eta^{#mu}'
   xunits = None
 elif leaf == 'muon_phi':
   steps = 31
   xmin = -3.45
   xmax = 5.85
   xtitle = '#phi^{#mu}'
   xunits = None
 elif leaf == 'ht':
   steps = 50
   xmin = 50.
   xmax = 400.
   xtitle = 'h_{T}'
   xunits = 'GeV'
 elif leaf == 'J1_eta' or leaf=='J2_eta' or leaf == 'J3_eta':
   steps = 20
   xmin = -3.
   xmax = 5.
   xtitle = leaf
   xunits = None
 elif leaf == 'J1_phi' or leaf=='J2_phi' or leaf=='J3_phi':
   steps = 31
   xmin = -3.45
   xmax = 5.85
   xtitle = leaf
   xunits = None
 elif leaf=='Wpt' or leaf == 'J1_pt' or leaf=='J2_pt' or leaf=='J3_pt' or leaf=='J4_pt':
   steps = 50
   xmin = 0.
   xmax = 350.
   #xmax = 200.
   xtitle = leaf
   xunits = 'GeV'
 elif leaf == 'mJJ':
   steps = 100
   xmin = 1.
   xmax = 300.
   xtitle = 'm^{JJ}'
   xunits = 'GeV'
# elif leaf == 'mJJ':
#   steps = 200
#   xmin = 150.
#   xmax = 550.
#   xtitle = 'm^{JJ}'
#   xunits = 'GeV'
 elif leaf == 'mJ3J4':
   steps = 100
   xmin = 1.
   xmax = 300.
   xtitle = 'm^{J_{3}J_{4}}'
   xunits = 'GeV'
# elif leaf == 'ptJJ':
#   steps = 200
#   xmin = 150.
#   xmax = 550.
#   xtitle = 'p_{T}^{JJ}'
#   xunits = 'GeV'
 elif leaf == 'ptJJ':
   steps = 50
   xmin = 0.
   xmax = 300.
   xtitle = 'p_{T}^{JJ}'
   xunits = 'GeV'
 elif leaf == 'Wpt':
   steps = 50
   xmin = 0.
   xmax = 300.
   xtitle = 'p_{T}^{W}'
   xunits = 'GeV'
 elif leaf == 'LHEProduct':
   steps = 7
   xmin = 4.
   xmax = 11.
   xtitle = leaf
   xunits = None
 elif leaf=='J1CSVbtag'or leaf=='J1CSVMVAbtag'\
  or leaf=='J2CSVbtag'or leaf=='J2CSVMVAbtag'\
  or leaf=='J1_idBetaPu' or leaf=='J2_idBetaPu'\
  or leaf=='J1_idBetaStarPu' or leaf=='J2_idBetaStarPu':
   steps = 20
   xmin = 0.
   xmax = 1.
   xtitle = leaf
   xunits = None
   setLogY = True
 elif leaf=='J1DR'or leaf=='J2DR':
   steps = 80
   xmin = 0.3
   xmax = 0.7
   xtitle = leaf
   xunits = None
   setLogY = True
 elif leaf=='J1JetParton' or leaf =='J2JetParton':
   steps = 14
   xmin = -7.
   xmax = 7.
   xtitle = leaf
   xunits = 'flavor'
 elif leaf=='J1_mass_SSV' or leaf =='J2_mass_SSV':
   steps = 32
   xmin = 0.
   xmax = 8.
   xtitle = leaf
   xunits = 'GeV'
 elif leaf=='(J1SVMassb+J2SVMassb)':
   steps = 45
   xmin = 0.
   xmax = 15.
   xtitle = '(J1SV_mass + J1SV_mass)'
   xunits = 'GeV'
 elif leaf=='muonCharge':
   steps = 5
   xmin = -2.
   xmax = 2.
   xtitle = leaf
   xunits = 'e'
 elif leaf == '(((J1_eta-J2_eta)*(J1_eta-J2_eta))+((J1_phi-J2_phi)*(J1_phi-J2_phi)))':
   steps = 20
   xmin = 0.
   xmax = 5.
   xtitle = '#Delta #phi^{2}_{j1j2}+#Delta #eta^{2}_{j1j2}'
   xunits = None
 elif leaf=='dz':
   steps = 40
   xmin = -0.2
   xmax = 0.2
   xtitle = leaf
   xunits = None
 elif leaf=='nJetsPt20' or leaf=='nJetsPt30' or leaf=='nJetsPt40' or leaf=='nJetsPt25':
   steps = 8
   xmin = 2.
   xmax = 10.
   xtitle = leaf
   xunits = None
   setLogY = True
 elif leaf=='J1_nTracksSSV' or leaf=='J2_nTracksSSV':
   steps = 30
   xmin = 0.
   xmax = 30
   xtitle = leaf
   xunits = None
 else :
   print("\n\n")
   print "YOU ARE A NINNY! The leaf's name isn't valid"
   print("\n\n")
   steps = 20
   xmin = 0.
   xmax = 1.
   xtitle = leaf
   xunits = None

# print leaf
# print steps
# print xmin
# print xmax

 return steps,xmin,xmax,xtitle,xunits,setLogY
