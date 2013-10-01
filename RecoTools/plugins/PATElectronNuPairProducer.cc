#include "UWAnalysis/RecoTools/interface/CompositePtrCandidateTMEtProducer.h"

#include "DataFormats/PatCandidates/interface/Electron.h"

typedef CompositePtrCandidateTMEtProducer<pat::Electron> PATElectronNuPairProducer;
#include "FWCore/Framework/interface/MakerMacros.h"

DEFINE_FWK_MODULE(PATElectronNuPairProducer);
