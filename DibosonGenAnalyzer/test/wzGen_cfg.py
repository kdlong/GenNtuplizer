import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

process = cms.Process("WZGenAnalyze")
options = ComLineArgs.setChannel('WZ')
options = ComLineArgs.getArgs()

process.options = cms.untracked.PSet(
    #wantSummary      = cms.untracked.bool(True)
    #allowUnscheduled  = cms.untracked.bool(True)
)

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

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
    leptons = cms.InputTag("sortedDressedLeptons" if \
            options.leptonType == "dressed" else "ossfLeptons"),
            #options.leptonType == "dressed" else "sortedLeptons"),
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

if options.leptonType in ["rivet", "finalstate"] and not options.includeTaus:
    process.load("GenNtuplizer.DibosonGenAnalyzer.Filters.genTauFilter_cff")
    process.load("GenNtuplizer.DibosonGenAnalyzer.Filters.wzOppositeFlavorFilter_cff")
    process.p = cms.Path(process.filterGenTaus*
                        # Only take emm and eem chans
                        # process.filterSameFlavorChans*
                        process.selectLeptons
    )
else:
    process.p = cms.Path(process.dressLeptons)

process.p *= (
    process.selectZCands * 
    process.selectNeutrinos * 
    process.selectWCands *
    process.selectJets *
    process.analyzeWZ
)
