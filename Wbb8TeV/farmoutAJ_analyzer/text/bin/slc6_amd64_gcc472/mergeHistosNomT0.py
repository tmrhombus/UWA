#!/usr/bin/env python
'''
 Merges histograms from the output of
 callHistoFiller.cc into one file
 Author: T.M.Perry UW-Madison
'''
import ROOT
from ROOT import TH1F,TFile,gROOT
import fnmatch as fnm

#version="CestPiVV"
#runname="vvQCDb_mT0"
version="CestPi"
#runname="stmMVmT0"
runname="stdMVmT0"
#runname="vvQCDprime"

in_path = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Analyzed_%s/'%(version,runname)
out_path = '/Users/rhombus/Documents/Madison/CMS/WbbAnalysis/UWAnalysis/CRAB/MuNu/SampleInfo/%s/Plots_%s/NoMT0bin'%(version,runname)

leps = ['mu','ele']
#cuts = ['dyjj', 'dybb']
#cuts = ['wbb', 'wjj']
#cuts = ['wbb', 'ttjjj', 'wjj', 'stt',]
cuts = ['wbb', 'ttme', 'ttjjj',]# 'wjj', 'stt', 'dyjj', 'dybb']
variables = [ 
 "mt",
# "met",
# "goodLep_pt",
# "goodJ1_pt",
## "goodJ2_pt",
# "goodJ1J2_dR",
# "goodJ1J2_mass",
# "goodJ1_CSV",
#### "goodJ1_mass_SV_unweighted",
# "goodJ1_mass_SV_corrected",
# "goodL1L2_pt",
# "goodL1L2_eta",
# "goodL1L2_phi",
# "goodL1L2_mass",
### "goodJ1_mass_SV_weighted",
# "goodJ2_CSV",
## "goodJ3J4_mass" 
]
#sf_qcds_mu =  [1.,1.,1.,1.,1.,1.,1.]
#sf_qcds_ele = [1.,1.,1.,1.,1.,1.,1.]

######## CestPi stmMVmT0/NoMT0bin
#sf_qcds_mu =  [,0.0001,]
#sf_qcds_ele = [,0.0001,]

####### CestPi stdMVmT0/NoMT0bin
sf_qcds_mu =  [0.0542896543442,0.0001,0.0704911113063]
sf_qcds_ele = [0.0769050835644,0.0001,0.0838942482509]

####### CestPiVV vvQCDb_mT0
#sf_qcds_mu =  [0.0339794632542,1.,]
#sf_qcds_ele = [0.0045045566299,1.,]

###### CestPi stmMVmT0
#sf_qcds_mu =  [0.0792590530607,0.0001,0.0782985599037,0.319729310871,0.464453792832,0.0001,0.0001]
#sf_qcds_ele = [0.0831075549922,0.0001,0.0781574905681,0.148591364130,0.344877255024,0.0001,0.0001]

###### CestPi stdMVmT0
#sf_qcds_mu =  [0.0550685257774,0.0001,0.0692824317954,0.319729310871,0.403221508677,0.0001,0.0001]
#sf_qcds_ele = [0.0783490310082,0.0001,0.0876429087303,0.148591364130,0.358284113517,0.0001,0.0001]

##### CestPi vvWbbQcd
#sf_qcds_mu =  [1.,1.]
#sf_qcds_ele = [1.,1.]

##### CestPi typical
#sf_qcds_mu  = [0.0551389394204,0.0001,0.0693614244721,0.298622956253,0.406475652308,0.0001,0.0001] 
#sf_qcds_ele = [0.0776675734412,0.0001,0.0868203188800,0.133244670647,0.351225939489,0.0001,0.0001] 

#### Valentine nobSF
#sf_qcds_mu =  [0.0001,0.0434536744249]   # ttme,ttjjj
#sf_qcds_ele = [0.0001,0.0572101352183]
#sf_qcds_mu =  [0.0476937786749,0.320111297459]   # wbb,wjj
#sf_qcds_ele = [0.0694167731886,0.148566349842]

## VVCheckExtended_vvCheck
#sf_qcds_mu =  [4.50160114845]
#sf_qcds_ele = [1.57328287813]

# Valentine_vvCheck
#sf_qcds_mu =  [5.16914212941]
#sf_qcds_ele = [4.26953102447]
#sf_qcds_mu =  [5.52805795336,5.16914212941]
#sf_qcds_ele = [2.20511309022,4.26953102447]

#sf_qcds_mu = [    # avecDY
#0.0563010513262,
#0.0001,
#0.070411479377,
#0.320111297459,
#0.426624507532,
#0.0001,
#0.0001
#]
#sf_qcds_ele = [
#0.080243772149,
#0.0001,
#0.0882905889167,
#0.148566349842,
#0.382149316526,
#0.0001,
#0.0001
#]

#sf_qcds_mu = [ Tout_MET30
#0.0943412763668,
#0.0001,
#0.124285746954,
#0.425070941618,
#0.0001,
#0.425070941618,
#0.0943412763668
#]
#sf_qcds_ele = [
#0.0976281482439,
#0.0001,
#0.0943862016004,
#0.204358310995,
#0.0001,
#0.204358310995,
#0.0976281482439
#]

#sf_qcds_mu = [   # Tout
#0.0557697059171,
#0.0001,
#0.0721159071322,
#0.354371987082,
#0.0001,
#0.354371987082,
#0.0557697059171
#]
#sf_qcds_ele = [
#0.0783754613046,
#0.0001,
#0.0847777439671,
#0.156115497598,
#0.0001,
#0.156115497598,
#0.0783754613046
#]

#sf_qcds_ele = [  # LTCetHLT
#0.044306186087,
#0.0001,
#0.0464475750008,
#0.13468693853
#]
#sf_qcds_mu = [
#0.0025003326262,
#0.0001,
#0.0025624456794,
#0.045202842707
#]

#sf_qcds_ele = [  # LTC
#0.0443818212615,
#0.0001,
#0.0467579189152,
#0.136127603726  
#]
#sf_qcds_mu = [
#0.00250049468503,
#0.0001,
#0.00256475829152,
#0.0453652337467
#]

#sf_qcds_mu = [  # old numbers
#0.00241743995384,
#0.0001,
#0.00248665468022,
#0.135402481304
#]
#sf_qcds_ele = [
#0.0416766785783,
#0.0001,
#0.0619185561595,
#0.301375411905
#]

mc_samples = [
 "Drell",
 "TTbar_full", 
 "TTbar_semi", 
 "T_s", 
 "T_t", 
 "T_tW", 
 "Tbar_s", 
 "Tbar_t", 
 "Tbar_tW", 
 "W1Jet",
 "W2Jet",
 "W3Jet",
 "W4Jet",
 "WJets",
 "Wbb4F", 
 "WW", 
 "WZ", 
 "ZZ" 
]
for lep in leps:
 if lep=='ele': sf_qcds = sf_qcds_ele
 if lep=='mu': sf_qcds = sf_qcds_mu
 for variable in variables: 
  for sf_qcd,cut in zip(sf_qcds,cuts):
   sf_shifts = [ "", "_CSVUp", "_CSVDown", "_EMuUp", "_EMuDown", "_UESUp", "_UESDown" ]
   es_shifts = [ "_SFs", "_JESUp", "_JESDown", "_LESUp", "_LESDown" ]
   print("%s, %s, %s"%(variable, cut, lep))
   
   outname = "%sHistograms_%s_%s_%s"%(out_path,cut,variable,lep)
   
   outfile=gROOT.FindObject('%s_temp.root'%(outname))
   if outfile : outfile.Close()
   outfile = TFile('%s_temp.root'%(outname),'RECREATE','Histograms')
   log = open('%s.log'%(outname),'w')
   
   #### DATA ####
   name = "Analyzed_Data_%s"%(lep)
   inFile = TFile('%s%s.root'%(in_path,name))
   data_good_mt020 = 0.  
   data_qcd_mt020 = 0.  
   for key in inFile.GetListOfKeys():
    obj = key.ReadObj()
    if(obj.IsA().InheritsFrom("TH1")):
     h_name = obj.GetName() 
     if( fnm.fnmatch( h_name,"h_%s_%s_good_%s"%(cut,lep,variable) ) ):
      obj.Draw()
      obj.SetName("data_obs")
      obj.SetBinContent(1,0) #######
      if variable=="mt":
       bmin = obj.GetXaxis().FindBin(0)
       bmax = obj.GetXaxis().FindBin(20)
       data_good_mt020 = obj.Integral(bmin,bmax)  # total data in 0<mt<20
       log.write("Data good in 0 < mT < 20: %s \n"%(data_good_mt020))
      outfile.cd()
      obj.Write()
     if( fnm.fnmatch( h_name,"h_%s_%s_qcd_%s"%(cut,lep,variable) ) ):
      obj.Draw()
      obj.SetName("data_qcd")
      obj.SetBinContent(1,0) #######
      if variable=="mt":
       bmin = obj.GetXaxis().FindBin(0)
       bmax = obj.GetXaxis().FindBin(20)
       data_qcd_mt020 = obj.Integral(bmin,bmax)  # total data in 0<mt<20
       log.write("Data qcd in 0 < mT < 20: %s \n\n"%(data_qcd_mt020))
      outfile.cd()
      obj.Write()
   inFile.Close()
   
   #### MC ####
   mc_good_mt020 = 0. # total mc in 0<mt<20
   for mc_sample in mc_samples: # for each of the normal MC samples
    for es_shift in es_shifts:    # for Energy Scale Shift (appened to filename)
     name = "Analyzed_%s%s"%(mc_sample,es_shift)
     inFile = TFile(in_path+name+'.root')

     if( fnm.fnmatch(mc_sample, "W*Jet*") ):
      q_flavors = ["_Wbb","_Wcc","_Wc","_Wl"]
     else: 
      q_flavors = ["",]
     for q_flavor in q_flavors: # for "" or "_Wbb","_Wcc","_Wc","_Wl"
      if( fnm.fnmatch(es_shift,"_SFs") ): # if SFs 
       for sf_shift in sf_shifts:   
        for key in inFile.GetListOfKeys():
         obj = key.ReadObj()
         if(obj.IsA().InheritsFrom("TH1")):
          h_name = obj.GetName() 
          obj.SetBinContent(1,0) #######
          if( fnm.fnmatch(h_name,"h_%s_%s_good_%s%s%s"%(cut,lep,variable,sf_shift,q_flavor)) ):
           obj.Draw()
           if( fnm.fnmatch(sf_shift,"") 
            and fnm.fnmatch(variable,"mt") 
            and not fnm.fnmatch(mc_sample,"Wbb4F") ): # add up mt from 0-20 for all good mc
            mc_good_mt020 += obj.Integral(bmin,bmax)
            log.write("Size of %s in 0 < mT < 20: %s \n"
             %(mc_sample+q_flavor+sf_shift,obj.Integral(bmin,bmax)) )
            log.write("Size of %s in full range: %s \n"
             %(mc_sample+q_flavor+sf_shift,obj.Integral(-1,300)) )
           # end if shift=="", variable=="mt"
           obj.SetName( "h_%s%s%s"%(mc_sample,q_flavor,sf_shift) )
           outfile.cd()
           obj.Write()
          # end if obj has good name
          if( fnm.fnmatch(h_name,"h_%s_%s_qcd_%s%s%s"%(cut,lep,variable,sf_shift,q_flavor)) ):
           obj.Draw()
           obj.SetName( "h_%s%s_qcd%s"%(mc_sample,q_flavor,sf_shift) )
           outfile.cd()
           obj.Write()
          # end if obj has qcd name
         # end if obj is TH1
        # end for key in inFile.GetListOfKeys()
       # end for sf_shift in sf_shifts
      # end if SFs
      if( fnm.fnmatch(es_shift,"_*ES*") ):  
       for key in inFile.GetListOfKeys():
        obj = key.ReadObj()
        if(obj.IsA().InheritsFrom("TH1")):
         h_name = obj.GetName() 
         #obj.SetBinContent(1,0) #######
         if( fnm.fnmatch(h_name,"h_%s_%s_good_%s%s"%(cut,lep,variable,q_flavor)) ):
          obj.Draw()
          obj.SetName( "h_%s%s%s"%(mc_sample,q_flavor,es_shift) )
          outfile.cd()
          obj.Write()
         # end if name matches good
         if( fnm.fnmatch(h_name,"h_%s_%s_qcd_%s%s"%(cut,lep,variable,q_flavor)) ):
          obj.Draw()
          obj.SetName( "h_%s%s_qcd%s"%(mc_sample,q_flavor,es_shift) )
          outfile.cd()
          obj.Write()
         # end if name matches qcd
        # end if obj is TH1
       # end for key in inFile.GetListOfKeys()
      # end if es_shift=="_*ES*"
     # end for q_flavor in q_flavors
     inFile.Close()
    # end for es_shift in es_shifts
   # end for mc_sample in mc_samples
   outfile.Close()
   
   # make new file - merge wjets, else copy 
   # yes I got lazy here
   outfile=gROOT.FindObject(outname+'.root')
   if outfile : outfile.Close()
   outfile = TFile('%s.root'%(outname),'RECREATE','Histograms')
   inFile = TFile('%s_temp.root'%(outname))
   data_qcd = inFile.Get("data_qcd")
   # just for initializing Wsample histograms to right size
   h_Wbb5F = data_qcd.Clone()
   h_Wbb5F.Reset()

   h_Wcc = h_Wbb5F.Clone()
   h_Wc = h_Wbb5F.Clone()
   h_Wl = h_Wbb5F.Clone()
   h_Wbb5F_CSVUp = h_Wbb5F.Clone()
   h_Wcc_CSVUp = h_Wbb5F.Clone()
   h_Wc_CSVUp = h_Wbb5F.Clone()
   h_Wl_CSVUp = h_Wbb5F.Clone()
   h_Wbb5F_CSVDown = h_Wbb5F.Clone()
   h_Wcc_CSVDown = h_Wbb5F.Clone()
   h_Wc_CSVDown = h_Wbb5F.Clone()
   h_Wl_CSVDown = h_Wbb5F.Clone()
   h_Wbb5F_EMuUp = h_Wbb5F.Clone()
   h_Wcc_EMuUp = h_Wbb5F.Clone()
   h_Wc_EMuUp = h_Wbb5F.Clone()
   h_Wl_EMuUp = h_Wbb5F.Clone()
   h_Wbb5F_EMuDown = h_Wbb5F.Clone()
   h_Wcc_EMuDown = h_Wbb5F.Clone()
   h_Wc_EMuDown = h_Wbb5F.Clone()
   h_Wl_EMuDown = h_Wbb5F.Clone()
   h_Wbb5F_JESUp = h_Wbb5F.Clone()
   h_Wcc_JESUp = h_Wbb5F.Clone()
   h_Wc_JESUp = h_Wbb5F.Clone()
   h_Wl_JESUp = h_Wbb5F.Clone()
   h_Wbb5F_JESDown = h_Wbb5F.Clone()
   h_Wcc_JESDown = h_Wbb5F.Clone()
   h_Wc_JESDown = h_Wbb5F.Clone()
   h_Wl_JESDown = h_Wbb5F.Clone()
   h_Wbb5F_LESUp = h_Wbb5F.Clone()
   h_Wcc_LESUp = h_Wbb5F.Clone()
   h_Wc_LESUp = h_Wbb5F.Clone()
   h_Wl_LESUp = h_Wbb5F.Clone()
   h_Wbb5F_LESDown = h_Wbb5F.Clone()
   h_Wcc_LESDown = h_Wbb5F.Clone()
   h_Wc_LESDown = h_Wbb5F.Clone()
   h_Wl_LESDown = h_Wbb5F.Clone()
   h_Wbb5F_UESUp = h_Wbb5F.Clone()
   h_Wcc_UESUp = h_Wbb5F.Clone()
   h_Wc_UESUp = h_Wbb5F.Clone()
   h_Wl_UESUp = h_Wbb5F.Clone()
   h_Wbb5F_UESDown = h_Wbb5F.Clone()
   h_Wcc_UESDown = h_Wbb5F.Clone()
   h_Wc_UESDown = h_Wbb5F.Clone()
   h_Wl_UESDown = h_Wbb5F.Clone()
   # don't forget QCD
   h_qcd = data_qcd.Clone()
   h_qcd.SetName("h_qcd")
   h_qcd_CSVUp = h_qcd.Clone()
   h_qcd_CSVUp.SetName("h_qcd_CSVUp")
   h_qcd_CSVDown = h_qcd.Clone()
   h_qcd_CSVDown.SetName("h_qcd_CSVDown")
   h_qcd_EMuUp = h_qcd.Clone()
   h_qcd_EMuUp.SetName("h_qcd_EMuUp")
   h_qcd_EMuDown = h_qcd.Clone()
   h_qcd_EMuDown.SetName("h_qcd_EMuDown")
   h_qcd_JESUp = h_qcd.Clone()
   h_qcd_JESUp.SetName("h_qcd_JESUp")
   h_qcd_JESDown = h_qcd.Clone()
   h_qcd_JESDown.SetName("h_qcd_JESDown")
   h_qcd_LESUp = h_qcd.Clone()
   h_qcd_LESUp.SetName("h_qcd_LESUp")
   h_qcd_LESDown = h_qcd.Clone()
   h_qcd_LESDown.SetName("h_qcd_LESDown")
   h_qcd_UESUp = h_qcd.Clone()
   h_qcd_UESUp.SetName("h_qcd_UESUp")
   h_qcd_UESDown = h_qcd.Clone()
   h_qcd_UESDown.SetName("h_qcd_UESDown")
   
   for key in inFile.GetListOfKeys():
    obj = key.ReadObj()
    if(obj.IsA().InheritsFrom("TH1")):
     h_name = obj.GetName() 
     ## MOST THINGS   if not WJets, QCD just copy it
     if ( not (fnm.fnmatch(h_name,'h_W*Jet*') )  # not WJets, not QCD
          and not fnm.fnmatch(h_name, '*qcd*') ):
      obj.Draw()
      outfile.cd()
      obj.Write()
     ## QCD  if not data/Wbb4F and is QCD, subtract from QCD
     if( (not fnm.fnmatch(h_name,'data*'))    # not data, is QCD, not Wbb4F
          and fnm.fnmatch(h_name, '*qcd*') 
          and not fnm.fnmatch(h_name,'h_Wbb4F*') ): 
      if( fnm.fnmatch(h_name,"*qcd") ):
       h_qcd.Add(obj, -1)
       if variable=="mt":
        log.write("Size of %s in 0 < mT < 20: %s \n"
         %(h_name,obj.Integral(bmin,bmax)) )
        log.write("Size of %s in full range: %s \n"
         %(h_name,obj.Integral(-1,300)) )
      # end if "*qcd"
      if( fnm.fnmatch(h_name,"qcd_CSVUp") ):   h_qcd_CSVUp.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_CSVDown") ): h_qcd_CSVDown.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_EMuUp") ):   h_qcd_EMuUp.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_EMuDown") ): h_qcd_EMuDown.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_JESUp") ):   h_qcd_JESUp.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_JESDown") ): h_qcd_JESDown.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_LESUp") ):   h_qcd_LESUp.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_LESDown") ): h_qcd_LESDown.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_UESUp") ):   h_qcd_UESUp.Add(obj, -1)
      if( fnm.fnmatch(h_name,"qcd_UESDown") ): h_qcd_UESDown.Add(obj, -1)
     # end if not data/Wbb4F and is QCD
     ## WJETS
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb' ) ): h_Wbb5F.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc' ) ): h_Wcc.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc'  ) ): h_Wc.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl'  ) ): h_Wl.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_CSVUp' ) ): h_Wbb5F_CSVUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_CSVUp' ) ): h_Wcc_CSVUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_CSVUp'  ) ): h_Wc_CSVUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_CSVUp'  ) ): h_Wl_CSVUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_CSVDown' ) ): h_Wbb5F_CSVDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_CSVDown' ) ): h_Wcc_CSVDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_CSVDown'  ) ): h_Wc_CSVDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_CSVDown'  ) ): h_Wl_CSVDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_EMuUp' ) ): h_Wbb5F_EMuUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_EMuUp' ) ): h_Wcc_EMuUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_EMuUp'  ) ): h_Wc_EMuUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_EMuUp'  ) ): h_Wl_EMuUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_EMuDown' ) ): h_Wbb5F_EMuDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_EMuDown' ) ): h_Wcc_EMuDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_EMuDown'  ) ): h_Wc_EMuDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_EMuDown'  ) ): h_Wl_EMuDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_JESUp' ) ): h_Wbb5F_JESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_JESUp' ) ): h_Wcc_JESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_JESUp'  ) ): h_Wc_JESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_JESUp'  ) ): h_Wl_JESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_JESDown' ) ): h_Wbb5F_JESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_JESDown' ) ): h_Wcc_JESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_JESDown'  ) ): h_Wc_JESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_JESDown'  ) ): h_Wl_JESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_LESUp' ) ): h_Wbb5F_LESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_LESUp' ) ): h_Wcc_LESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_LESUp'  ) ): h_Wc_LESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_LESUp'  ) ): h_Wl_LESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_LESDown' ) ): h_Wbb5F_LESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_LESDown' ) ): h_Wcc_LESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_LESDown'  ) ): h_Wc_LESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_LESDown'  ) ): h_Wl_LESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_UESUp' ) ): h_Wbb5F_UESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_UESUp' ) ): h_Wcc_UESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_UESUp'  ) ): h_Wc_UESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_UESUp'  ) ): h_Wl_UESUp.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wbb_UESDown' ) ): h_Wbb5F_UESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wcc_UESDown' ) ): h_Wcc_UESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wc_UESDown'  ) ): h_Wc_UESDown.Add(obj)
     if( fnm.fnmatch(h_name, 'h_W*Jet*Wl_UESDown'  ) ): h_Wl_UESDown.Add(obj)
    # end if obj = TH1
   # end for key in inFile.GetListOfKeys()
   h_Wbb5F.SetName("h_Wbb5F")
   h_Wcc.SetName("h_Wcc")
   h_Wc.SetName("h_Wc")
   h_Wl.SetName("h_Wl")
   h_Wbb5F_CSVUp.SetName("h_Wbb5F_CSVUp")
   h_Wcc_CSVUp.SetName("h_Wcc_CSVUp")
   h_Wc_CSVUp.SetName("h_Wc_CSVUp")
   h_Wl_CSVUp.SetName("h_Wl_CSVUp")
   h_Wbb5F_CSVDown.SetName("h_Wbb5F_CSVDown")
   h_Wcc_CSVDown.SetName("h_Wcc_CSVDown")
   h_Wc_CSVDown.SetName("h_Wc_CSVDown")
   h_Wl_CSVDown.SetName("h_Wl_CSVDown")
   h_Wbb5F_EMuUp.SetName("h_Wbb5F_EMuUp")
   h_Wcc_EMuUp.SetName("h_Wcc_EMuUp")
   h_Wc_EMuUp.SetName("h_Wc_EMuUp")
   h_Wl_EMuUp.SetName("h_Wl_EMuUp")
   h_Wbb5F_EMuDown.SetName("h_Wbb5F_EMuDown")
   h_Wcc_EMuDown.SetName("h_Wcc_EMuDown")
   h_Wc_EMuDown.SetName("h_Wc_EMuDown")
   h_Wl_EMuDown.SetName("h_Wl_EMuDown")
   h_Wbb5F_JESUp.SetName("h_Wbb5F_JESUp")
   h_Wcc_JESUp.SetName("h_Wcc_JESUp")
   h_Wc_JESUp.SetName("h_Wc_JESUp")
   h_Wl_JESUp.SetName("h_Wl_JESUp")
   h_Wbb5F_JESDown.SetName("h_Wbb5F_JESDown")
   h_Wcc_JESDown.SetName("h_Wcc_JESDown")
   h_Wc_JESDown.SetName("h_Wc_JESDown")
   h_Wl_JESDown.SetName("h_Wl_JESDown")
   h_Wbb5F_LESUp.SetName("h_Wbb5F_LESUp")
   h_Wcc_LESUp.SetName("h_Wcc_LESUp")
   h_Wc_LESUp.SetName("h_Wc_LESUp")
   h_Wl_LESUp.SetName("h_Wl_LESUp")
   h_Wbb5F_LESDown.SetName("h_Wbb5F_LESDown")
   h_Wcc_LESDown.SetName("h_Wcc_LESDown")
   h_Wc_LESDown.SetName("h_Wc_LESDown")
   h_Wl_LESDown.SetName("h_Wl_LESDown")
   h_Wbb5F_UESUp.SetName("h_Wbb5F_UESUp")
   h_Wcc_UESUp.SetName("h_Wcc_UESUp")
   h_Wc_UESUp.SetName("h_Wc_UESUp")
   h_Wl_UESUp.SetName("h_Wl_UESUp")
   h_Wbb5F_UESDown.SetName("h_Wbb5F_UESDown")
   h_Wcc_UESDown.SetName("h_Wcc_UESDown")
   h_Wc_UESDown.SetName("h_Wc_UESDown")
   h_Wl_UESDown.SetName("h_Wl_UESDown")
   outfile.cd()
   h_Wbb5F.Write()
   h_Wcc.Write()
   h_Wc.Write()
   h_Wl.Write()
   h_Wbb5F_CSVUp.Write()
   h_Wcc_CSVUp.Write()
   h_Wc_CSVUp.Write()
   h_Wl_CSVUp.Write()
   h_Wbb5F_CSVDown.Write()
   h_Wcc_CSVDown.Write()
   h_Wc_CSVDown.Write()
   h_Wl_CSVDown.Write()
   h_Wbb5F_EMuUp.Write()
   h_Wcc_EMuUp.Write()
   h_Wc_EMuUp.Write()
   h_Wl_EMuUp.Write()
   h_Wbb5F_EMuDown.Write()
   h_Wcc_EMuDown.Write()
   h_Wc_EMuDown.Write()
   h_Wl_EMuDown.Write()
   h_Wbb5F_JESUp.Write()
   h_Wcc_JESUp.Write()
   h_Wc_JESUp.Write()
   h_Wl_JESUp.Write()
   h_Wbb5F_JESDown.Write()
   h_Wcc_JESDown.Write()
   h_Wc_JESDown.Write()
   h_Wl_JESDown.Write()
   h_Wbb5F_LESUp.Write()
   h_Wcc_LESUp.Write()
   h_Wc_LESUp.Write()
   h_Wl_LESUp.Write()
   h_Wbb5F_LESDown.Write()
   h_Wcc_LESDown.Write()
   h_Wc_LESDown.Write()
   h_Wl_LESDown.Write()
   h_Wbb5F_UESUp.Write()
   h_Wcc_UESUp.Write()
   h_Wc_UESUp.Write()
   h_Wl_UESUp.Write()
   h_Wbb5F_UESDown.Write()
   h_Wcc_UESDown.Write()
   h_Wc_UESDown.Write()
   h_Wl_UESDown.Write()
   
   h_qcdUNSCALED = h_qcd.Clone()
   h_qcdUNSCALED.SetName("h_qcdUNSCALED")
   h_qcdUNSCALED.Write()
   h_qcd.Scale( sf_qcd )
   if variable=="mt":
    mc_qcd_mt020=h_qcd.Integral(bmin,bmax)
   h_qcd.Write()
    
   if variable=="mt":
    if( mc_qcd_mt020 > 0.1 ):
     log.write("\n%s  : QCD Scale = ( data - mc )/qcd in 0<mt<20 \n" \
          %( (data_good_mt020 - mc_good_mt020)/mc_qcd_mt020 ) )
    else: log.write("\nUse 0.1  : QCD Scale = ( data - mc )/qcd in 0<mt<20 \n")
    log.write("This will be negative for mc > data, take QCD=0\n")
    log.write("data = %s\n"%(data_good_mt020))
    log.write("mc   = %s\n"%(mc_good_mt020))
    log.write("qcd  = %s\n"%(mc_qcd_mt020))
    log.write("qcd scaled = %s\n"%(h_qcd.Integral(bmin,bmax)))
   
    print "\n%s.log"%(outname)
    if( mc_qcd_mt020 > 0.1 ):
     print ("%s  : QCD Scale = ( data - mc )/qcd in 0<mt<20 \n" \
          %( (data_good_mt020 - mc_good_mt020)/mc_qcd_mt020 ) )
    else: print("0.0001 : QCD Scale for mc_qcd_mt020 < 0.1 \n")

   log.close()   
   outfile.Close()
