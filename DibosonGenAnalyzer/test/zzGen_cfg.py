import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("ZZGenAnalyze")

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load("GenNtuplizer.DibosonGenAnalyzer.genLeptons_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genZCands_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genJets_cff")

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

if "WZ" in options.useDefaultDataset:
    print "WARNING! You are using WZ dataset with ZZ analysis settings." \
        "Do you really want to do this?"

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.analyzeZZ = cms.EDAnalyzer("DibosonGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sortedLeptons"),
    zCands = cms.InputTag("sortedZCands"),
    lheSource = cms.InputTag("externalLHEProducer" if options.isMiniAOD else "source"),
    nKeepZs = cms.untracked.uint32(4),
    nKeepLeps = cms.untracked.uint32(4),
    nKeepJets = cms.untracked.uint32(2),
    xSec = cms.untracked.double(options.crossSection)
)
process.p = cms.Path(process.selectLeptons * 
    process.selectZCands * 
    process.selectJets *
    process.analyzeZZ
)
