import ROOT
from ROOT import TH1F,TFile,gROOT

data_filename = 'Data_Pileup_2012_ReReco-600bins.root'
mc_filename = 'MC_Summer12_PU_S10-600bins.root'
data_file = TFile(data_filename)
mc_file = TFile(mc_filename)

data_hist = data_file.Get("pileup")
data_hist.Scale(1./data_hist.Integral())
mc_hist = mc_file.Get("pileup")
mc_hist.Scale(1./mc_hist.Integral())

outFile=gROOT.FindObject('puInfo2012.root')
if outFile : outFile.Close()
outFile = TFile('puInfo2012.root','RECREATE','pu weighting histogram')

weight = data_hist.Clone()
weight.SetName('weight')
weight.Divide(mc_hist)

outFile.Write()
