import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("WGenAnalyze")

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load("GenNtuplizer.DibosonGenAnalyzer.genNeutrinos_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genWCands_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genJets_cff")

options = ComLineArgs.getArgs()
process.load("GenNtuplizer.DibosonGenAnalyzer.%sLeptons_cff" % 
    ("dressedGen" if options.leptonType == "dressed" else "gen"))
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.analyzeW = cms.EDAnalyzer("DibosonGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sorted%sLeptons" % 
        ("Dressed" if options.leptonType == "dressed" else "")),
    wCands = cms.untracked.InputTag("sortedWCands"),
    extraParticle = cms.untracked.InputTag("sortedNeutrinos"),
    lheSource = cms.untracked.string(options.lheSource),
    nKeepZs = cms.untracked.uint32(0),
    nKeepLeps = cms.untracked.uint32(1),
    nKeepJets = cms.untracked.uint32(4),
    nKeepExtra = cms.untracked.uint32(1),
    extraName = cms.untracked.string("Nu"),
    metSource = cms.untracked.string("slimmedMETs" if options.isMiniAOD else "genMetTrue"),
    nKeepWs = cms.untracked.uint32(1),
    xSec = cms.untracked.double(options.crossSection)
)
process.p = cms.Path(process.dressLeptons if options.leptonType == "dressed" \
    else process.selectLeptons)
process.p *= (
    process.selectJets *
    process.selectNeutrinos * 
    process.selectWCands * 
    process.analyzeW
)
