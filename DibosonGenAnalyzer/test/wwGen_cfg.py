import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("WWGenAnalyze")

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load("GenNtuplizer.DibosonGenAnalyzer.genLeptons_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genZCands_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genJets_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genNeutrinos_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genWCands_cff")

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

process.analyzeWW = cms.EDAnalyzer("DibosonGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sortedLeptons"),
    extraParticle = cms.untracked.InputTag("sortedNeutrinos" if not options.genMet else "slimmedMETs"),
    lheSource = cms.InputTag("externalLHEProducer" if options.isMiniAOD else "source"),
    zCands = cms.InputTag("sortedZCands"),
    wCands = cms.untracked.InputTag("trueWs"),
    nKeepZs = cms.untracked.uint32(0),
    nKeepLeps = cms.untracked.uint32(2),
    nKeepJets = cms.untracked.uint32(2),
    nKeepExtra = cms.untracked.uint32(2),
    extraName = cms.untracked.string("Nu" if not options.genMet else "genMET"),
    nKeepWs = cms.untracked.uint32(2),
    xSec = cms.untracked.double(options.crossSection)
)
process.p = cms.Path(process.selectLeptons if not options.includeRadiated else
        process.selectLeptons*process.selectRadiatedLeptons)
process.p *= (process.selectZCands * 
    process.selectNeutrinos * 
    process.selectWCands *
    process.selectJets *
    process.analyzeWW
)
