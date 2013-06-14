

def ranger(leaf): 
 steps = None
 xmin = None
 xmax = None
 lumi = 4895.
 if leaf=='mt':
   steps =50 
   xmin = 0.
   xmax = 200.
   xtitle = 'Transverse Mass'
   xunits = 'GeV'
 elif leaf == 'met' or leaf == 'metjesMpt' or leaf == 'metjesPpt' or leaf =='metonept' or leaf=='meta':
   steps = 50
   xmin = 0.
   xmax = 200.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'massDiMuon':
   steps = 50
   xmin = 0.
   xmax = 200.
   xtitle ='diMuon Mass'
   xunits = 'GeV'
 elif leaf == 'jet1BTag_CSV':
   steps = 40
   xmin = 0.
   xmax = 1.
   xtitle = 'Jet 1 bTag CSV'
   xunits = 'none'
 elif leaf == 'jet2BTag_CSV':
   steps =40
   xmin = 0.
   xmax = 1.
   xtitle = 'Jet 2 bTag CSV'
   xunits = 'none'
 elif leaf == 'ptMu':
   steps = 50
   xmin = 0.
   xmax = 250.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'isoMuPF':
   steps = 30
   xmin = 0.
   xmax = 1.5
   xtitle = 'Isolation'
   xunits = 'none'
 elif leaf == 'massDiJets':
   steps = 50
   xmin = 0.
   xmax = 700.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'ptDiJets':
   steps = 50
   xmin = 0.
   xmax = 350.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'isoMuPFIsoRho':
   steps = 15
   xmin = 0.
   xmax = 0.15
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'etaMu':
   steps = 50
   xmin = -3.
   xmax = 5.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'jet1eta':
   steps = 50
   xmin = -3.
   xmax = 3.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'jet2eta':
   steps = 50
   xmin = -3.
   xmax = 3.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'massDiNoBJets':
   steps = 50#100
   xmin = 0.
   xmax = 200.#1000.
   xtitle = 'Mass Di NoB Jets'
   xunits = 'GeV'
 elif leaf == 'jet1pt':
   steps = 100
   xmin = 30.
   xmax = 130.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'jet2pt':
   steps = 100
   xmin = 30.
   xmax = 130.
   xtitle = 'MET'
   xunits = 'GeV'
 elif leaf == 'jet1BTag_SSVMass':
   steps = 10
   xmin = -1.5
   xmax = 1.5
   xtitle = 'Jet 1 BTag SSV Mass'
   xunits = 'no units'
 else :
   steps = 0
   print("\n\n")
   print "YOU ARE A NINNY! The leaf's name isn't valid"
   print("\n\n")

# print leaf
# print steps
# print xmin
# print xmax

 return lumi,steps,xmin,xmax,xtitle,xunits
