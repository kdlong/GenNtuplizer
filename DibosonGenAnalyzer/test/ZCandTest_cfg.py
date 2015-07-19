import FWCore.ParameterSet.Config as cms
import GenNtuplizer.WZGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("WZGenAnalyze")

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.selectedElectrons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 11 && fromHardProcessFinalState")  
)

process.selectedMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 13 && fromHardProcessFinalState")  
)

process.leptons = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("selectedElectrons", "selectedMuons")
)
process.zMuMuCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('selectedMuons@+ selectedMuons@-'),
    cut = cms.string('charge=0'),
    minNumber = cms.uint32(2)
)

process.zeeCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('selectedElectrons@+ selectedElectrons@-'),
    cut = cms.string('charge=0'),
    minNumber = cms.uint32(2)
)
process.zCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", "zeeCands")
)
process.sortedZCands = cms.EDFilter("BestZCandViewSelector",
    src = cms.InputTag("zCands"),
    maxNumber = cms.uint32(10)
)
process.testZCands = cms.EDAnalyzer("ZCandTest",
    src = cms.InputTag("sortedZCands"),
)
process.p = cms.Path((process.selectedElectrons + process.selectedMuons)* 
    (process.zMuMuCands + process.zeeCands) *
    process.zCands*process.sortedZCands * 
    process.testZCands
)
