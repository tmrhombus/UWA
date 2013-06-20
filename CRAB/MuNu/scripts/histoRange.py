

def ranger(leaf): 
 steps = None
 xmin = None
 xmax = None
# lumi = 13498.
 if leaf=='Mt' or leaf == 'muonPt' :
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
   xmax = 60.
   xtitle = 'Nr. Vertices'
   xunits = 'xx'
 elif leaf == 'DiMuonMass':
   steps = 100
   xmin = 0.
   xmax = 200.
   xtitle = 'Mass Di-Muon'
   xunits = 'GeV'
 elif leaf == 'muonEta':
   steps = 20
   xmin = -3.
   xmax = 3.
   xtitle = 'Muon #Eta'
   xunits = 'xx'
 elif leaf == 'muonPhi':
   steps = 20
   xmin = -3.5
   xmax = 6.5
   xtitle = 'Muon #Phi'
   xunits = 'xx'
 elif leaf == 'ht':
   steps = 100
   xmin = 0.
   xmax = 200.
   xtitle = 'ht'
   xunits = 'GeV'
 elif leaf == 'highestJetEta' or leaf=='secondJetEta' or leaf == 'thirdJetEta':
   steps = 20
   xmin = -3.
   xmax = 3.
   xtitle = 'Jet #Eta'
   xunits = 'xx'
 elif leaf == 'highestJetPhi' or leaf=='secondJetPhi' or leaf=='thirdJetPhi':
   steps = 20
   xmin = -4.5
   xmax = 6.5
   xtitle = 'Jet Phi'
   xunits = 'xx'
 elif leaf == 'highestJetPt' or leaf=='secondJetPt' or leaf=='thirdJetPt':
   steps = 100
   xmin = 0.
   xmax = 200
   xtitle = 'Jet Pt'
   xunits = 'GeV'
 elif leaf == 'mjj' or leaf == 'mJ3J4':
   steps = 100
   xmin = 0.
   xmax = 300.
   xtitle = 'Dijet Mass'
   xunits = 'GeV'
 elif leaf == 'ptJJ':
   steps = 100
   xmin = 0.
   xmax = 300.
   xtitle = 'Dijet Pt'
   xunits = 'GeV'
 elif leaf == 'WPt':
   steps = 100
   xmin = 0.
   xmax = 300.
   xtitle = 'W Pt'
   xunits = 'GeV'
 else :
   print("\n\n")
   print "YOU ARE A NINNY! The leaf's name isn't valid"
   print("\n\n")
   steps = 100
   xmin = 0.
   xmax = 200.
   xtitle = leaf
   xunits = 'xxx'

# print leaf
# print steps
# print xmin
# print xmax

 return steps,xmin,xmax,xtitle,xunits
