import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("ZZGenAnalyze")

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.load("GenNtuplizer.DibosonGenAnalyzer.genZCands_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genJets_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.Filters.Zmassfilter_cff")

options = ComLineArgs.getArgs()
process.load("GenNtuplizer.DibosonGenAnalyzer.%sLeptons_cff" % 
    ("dressedGen" if options.leptonType == "dressed" else "gen"))
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

if "WZ" in options.useDefaultDataset:
    print "WARNING! You are using WZ dataset with ZZ analysis settings." \
        "Do you really want to do this?"

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    inputCommands = cms.untracked.vstring('keep *', 'drop LHERunInfoProduct_*_*_*'),
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.analyzeZZ = cms.EDAnalyzer("DibosonGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sorted%sLeptons" % 
        ("Dressed" if options.leptonType == "dressed" else "")),
    zCands = cms.InputTag("sortedZCands"),
    lheSource = cms.untracked.string(options.lheSource),
    nKeepZs = cms.untracked.uint32(4),
    nKeepLeps = cms.untracked.uint32(4),
    nKeepJets = cms.untracked.uint32(4),
    xSec = cms.untracked.double(options.crossSection)
)
process.p = cms.Path(process.dressLeptons if options.leptonType == "dressed" \
    else process.selectLeptons)
process.p *= (process.selectZCands * 
    process.selectJets *
    process.analyzeZZ
)
