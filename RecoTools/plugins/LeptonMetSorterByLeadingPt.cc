#include "UWAnalysis/RecoTools/plugins/PATTauMatchSelector.h"
#include "FWCore/Framework/interface/MakerMacros.h"
#include "FWCore/PluginManager/interface/ModuleDef.h"
#include "UWAnalysis/DataFormats/interface/CompositePtrCandidateTMEt.h"
//#include "UWAnalysis/DataFormats/interface/CompositePtrCandidateT1T2MEtFwd.h"
#include "UWAnalysis/RecoTools/plugins/LeptonMetSorterByLeadingPt.h"

typedef LeptonMetSorterByLeadingPt<PATMuonNuPair> PATMuonNuPairSorter;

DEFINE_FWK_MODULE(PATMuonNuPairSorter);
