import FWCore.ParameterSet.Config as cms

process = cms.Process("WZGenAnalyze")

# parse variables from cmsRun
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.inputFiles = "file:/afs/cern.ch/user/k/kelong/work/WZ_MCAnalysis/POWHEG_WZ/WZ_powheg_pythia8_CUETP8M1_10E5ev.root"
options.outputFile = ""
options.maxEvents = -1
options.parseArguments() 

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(options.inputFiles)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.selectedGenParticles = cms.EDFilter("CandViewShallowCloneProducer",
    src = cms.InputTag("genParticles"),
    cut = cms.string("pt > 0")                           
)

process.leptons = cms.EDFilter("PdgIdAndStatusCandSelector",
                           src = cms.InputTag("selectedGenParticles"),
                           pdgId = cms.vint32( 11, 13 ),
                           status = cms.vint32( 1 )                          
)

process.sortedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("leptons"),
    maxNumber = cms.uint32(3)
)

process.jets = cms.EDProducer("GenJetShallowCloneProducer",
                              src = cms.InputTag("ak4GenJets")
)

process.selectedJets = cms.EDFilter("CandSelector",
    src = cms.InputTag("jets"),
    cut = cms.string("pt > 20")
)

process.sortedJets = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("selectedJets"),
    maxNumber = cms.uint32(10)
)

process.analyzeWZ = cms.EDAnalyzer("WZGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sortedLeptons"),
)

process.p = cms.Path(((process.selectedGenParticles*process.leptons*process.sortedLeptons)+ 
    (process.jets*process.selectedJets*process.sortedJets)) *
    process.analyzeWZ
)
