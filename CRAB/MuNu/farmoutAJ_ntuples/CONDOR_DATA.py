process.source.fileNames= cms.untracked.vstring($inputFileNames)

process.maxEvents = cms.untracked.PSet(
        input = cms.untracked.int32(-1)
        )

process.MessageLogger.cerr.threshold = 'ERROR'
process.MessageLogger.cerr.FwkReport.reportEvery = 10000000

process.TFileService.fileName=cms.string("$outputFileName")
