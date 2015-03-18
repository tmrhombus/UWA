process.source = cms.Source("PoolSource",
         fileNames = cms.untracked.vstring(
          $inputFileNames ),
         inputCommands=cms.untracked.vstring(
          'keep *',
          'drop *_finalState*_*_*',
          'drop *_patFinalStateEvent*_*_*'
         )
)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
)

process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.cerr.FwkReport.reportEvery = 10000000

process.TFileService.fileName=cms.string("$outputFileName")

