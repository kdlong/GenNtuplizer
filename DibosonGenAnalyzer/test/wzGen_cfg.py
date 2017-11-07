import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("WZGenAnalyze")
options = ComLineArgs.setChannel('WZ')
options = ComLineArgs.getArgs()

process.options = cms.untracked.PSet(
    allowUnscheduled = cms.untracked.bool(True),
    wantSummary      = cms.untracked.bool(True)
)

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

rivet = (options.leptonType == "rivet") 

if rivet:
    process.load("GeneratorInterface.RivetInterface.mergedGenParticles_cfi")
    process.load("GeneratorInterface.RivetInterface.genParticles2HepMC_cff")
    process.load("GeneratorInterface.RivetInterface.particleLevel_cfi")
    process.genParticles2HepMC.genParticles = cms.InputTag("mergedGenParticles")
    process.particleLevel.particleMinPt  = cms.double(0.)
    process.particleLevel.particleMaxEta = cms.double(999.) # HF range. Maximum 6.0 on MiniAOD
    process.particleLevel.lepMinPt = cms.double(0.)
    process.particleLevel.lepMaxEta = cms.double(999)
    process.particleLevel.jetMaxEta = cms.double(4.7)

process.load("GenNtuplizer.DibosonGenAnalyzer.%sLeptons_cff" % 
        ("dressedGen" if options.leptonType == "dressed" else "gen"))
process.load("GenNtuplizer.DibosonGenAnalyzer.genZCands_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genJets_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genNeutrinos_cff")
process.load("GenNtuplizer.DibosonGenAnalyzer.genWCands_cff")

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.TFileService = cms.Service("TFileService",
    inputCommands = cms.untracked.vstring('keep *', 'drop LHERunInfoProduct_*_*_*'),
    fileName = cms.string(options.outputFile)
)

process.analyzeWZ = cms.EDAnalyzer("DibosonGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sorted%sLeptons" % 
        ("Dressed" if options.leptonType == "dressed" else "")),
    extraParticle = cms.untracked.InputTag("sortedNeutrinos"),
    lheSource = cms.untracked.string(options.lheSource),
    zCands = cms.untracked.InputTag("sortedZCands"),
    wCands = cms.untracked.InputTag("sortedWCands"),
    nKeepZs = cms.untracked.uint32(2),
    nKeepLeps = cms.untracked.uint32(3),
    nKeepJets = cms.untracked.uint32(4),
    nKeepExtra = cms.untracked.uint32(1),
    extraName = cms.untracked.string("Nu"),
    metSource = cms.untracked.string("slimmedMETs" if options.isMiniAOD else "genMetTrue"),
    nKeepWs = cms.untracked.uint32(3),
    xSec = cms.untracked.double(options.crossSection)
)

if rivet:
    process.p = cms.Path(
        process.mergedGenParticles *
        process.genParticles2HepMC *
        process.particleLevel *
        process.selectedLeptons
    )
else:
    process.p = cms.Path(process.dressLeptons if options.leptonType == "dressed" \
            else process.selectLeptons)

if options.leptonType == "finalstate" or rivet:
    process.load("GenNtuplizer.DibosonGenAnalyzer.Filters.genTauFilter_cff")
    process.p *= process.filterGenTaus

process.p *= (
    process.selectZCands * 
    process.selectNeutrinos * 
    process.selectWCands *
    process.selectJets *
    process.analyzeWZ
)
