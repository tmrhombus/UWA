pushd $CMSSW_BASE/src
addpkg DataFormats/PatCandidates V06-05-06-06

cvs co -r V02-02-03 HiggsAnalysis/CombinedLimit
cvs co -r V00-02-06 HiggsAnalysis/HiggsToTauTau

addpkg PhysicsTools/PatAlgos V08-09-52
addpkg DataFormats/StdDictionaries V00-02-14
addpkg PhysicsTools/PatUtils V03-09-26
addpkg CommonTools/ParticleFlow V00-03-16
addpkg FWCore/GuiBrowsers V00-00-70
addpkg RecoParticleFlow/PFProducer V15-02-06
addpkg CommonTools/RecoUtils V00-00-12
cvs up -r 1.4 CommonTools/RecoUtils/BuildFile.xml
addpkg DataFormats/HLTReco V02-06-05
addpkg JetMETCorrections/Type1MET V04-06-09
cvs co -r V08-03-19      PhysicsTools/Utilities

addpkg RecoBTag/SecondaryVertex V01-10-01  # Update in Evan's
addpkg RecoVertex/AdaptiveVertexFinder V02-02-00

cvs co -r V02-02-00      RecoVertex/AdaptiveVertexFinder
cvs co -d ZSV/BAnalysis UserCode/ZSV/BAnalysis/

cvs co -r V09-00-01 RecoEgamma/EgammaTools
cvs co -r V00-00-30-00 -d EGamma/EGammaAnalysisTools UserCode/EGamma/EGammaAnalysisTools
cvs up -r 1.4 EGamma/EGammaAnalysisTools/interface/ElectronEffectiveArea.h
cvs co -r Moriond_2013_V01-1 EgammaAnalysis/ElectronTools

# Add MVA MET Has to go before TauId because this is painful...

cvs co -r METPU_5_3_X_v9 JetMETCorrections/METPUSubtraction
popd
pushd $CMSSW_BASE/src/JetMETCorrections/METPUSubtraction/test/
./setup.sh
popd
pushd $CMSSW_BASE/src
patch -p0 -N < UWAnalysis/patches/fixMVAMET_CVSConflicts.patch
cvs up -r 1.6 PhysicsTools/PatAlgos/plugins/PATMHTProducer.h

cvs co -r V01-04-23 RecoTauTag/RecoTau #equivalent to 04-14
cvs co -r V01-04-10 RecoTauTag/Configuration
cvs co -r V00-04-00 CondFormats/EgammaObjects

cvs co -r bMinimalSVfit-08-03-11 AnalysisDataFormats/TauAnalysis
cvs co -r bMinimalSVfit_2012May13 TauAnalysis/CandidateTools
cvs co -r V04-01-03      RecoLuminosity/LumiDB

cvs co PhysicsTools/PythonAnalysis
cvs co FWCore/PythonUtilities
popd
