import FWCore.ParameterSet.Config as cms

process = cms.Process("WZGenAnalyze")

# parse variables from cmsRun
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.inputFiles = ""
options.outputFile = ""
options.maxEvents = -1

options.parseArguments() 

process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = 1000

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    # replace 'myfile.root' with the source file you want to use
    fileNames = cms.untracked.vstring(inputFiles)
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.selectedGenParticles = cms.EDFilter("CandViewShallowCloneProducer",
    src = cms.InputTag("packedGenParticles"),
    cut = cms.string("")                           
)

process.leptons = cms.EDFilter("PdgIdAndStatusCandSelector",
                           src = cms.InputTag("selectedGenParticles"),
                           pdgId = cms.vint32( 11, 13 ),
                           status = cms.vint32( 1 ),
                           cut = cms.string("")                           
)

process.neutrinos = cms.EDFilter("PdgIdAndStatusCandSelector",
                           src = cms.InputTag("selectedGenParticles"),
                           pdgId = cms.vint32( 12, 14, 16 ),
                           status = cms.vint32( 1 )                          
)

process.sortedNeutrinos = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("neutrinos"),
    maxNumber = cms.uint32(10)
)

process.sortedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("leptons"),
    maxNumber = cms.uint32(10)
)

process.muons = cms.EDFilter("PdgIdAndStatusCandSelector",
    src = cms.InputTag("selectedGenParticles"),
    pdgId = cms.vint32( 13 ),
    status = cms.vint32( 1 )                          
)

process.electrons = cms.EDFilter("PdgIdAndStatusCandSelector",
    src = cms.InputTag("selectedGenParticles"),
    pdgId = cms.vint32( 11 ),
    status = cms.vint32( 1 )                          
)

process.zMuMuCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('muons@+ muons@-'),
    cut = cms.string('60 < mass < 120 & charge=0'),
)

process.zeeCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('electrons@+ electrons@-'),
    cut = cms.string('60 < mass < 120 & charge=0'),
)

process.sortedZeeCands = cms.EDFilter("BestZCandSelector",
    src = cms.InputTag("zeeCands"),
    maxNumber = cms.uint32(3),
)

process.sortedZMuMuCands = cms.EDFilter("BestZCandSelector",
    src = cms.InputTag("zMuMuCands"),
    maxNumber = cms.uint32(3),
    minNumber = cms.uint32(2)
)
#import RecoJets.Configuration.GenJetParticles_cff as GenJetParticles
process.genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
    src = cms.InputTag("packedGenParticles"),
    ignoreParticleIDs = cms.vuint32(
         1000022,
         1000012, 1000014, 1000016,
         2000012, 2000014, 2000016,
         1000039, 5100039,
         4000012, 4000014, 4000016,
         9900012, 9900014, 9900016,
         39,
         12, 14, 16),
    partonicFinalState = cms.bool(False),
    excludeResonances = cms.bool(False),
    excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
    tausAsJets = cms.bool(False)
)

import RecoJets.Configuration.RecoGenJets_cff as RecoGenJets
process.ak4GenJetsNoNu = RecoGenJets.ak4GenJetsNoNu

process.selectedJets = cms.EDFilter("EtaPtMinCandViewSelector",
    src = cms.InputTag("ak4GenJetsNoNu"),
    ptMin   = cms.double(30),
    etaMin = cms.double(-4.7),
    etaMax = cms.double(4.7)
)

process.sortedJets = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("selectedJets"),
    maxNumber = cms.uint32(10)
)

process.analyzeWZ = cms.EDAnalyzer("WZGenAnalyzer",
    jets = cms.InputTag("sortedJets"),
    leptons = cms.InputTag("sortedLeptons"),
    met = cms.InputTag("sortedNeutrinos"),
    zMuMuCands = cms.InputTag("zMuMuCands"),
    zeeCands = cms.InputTag("zeeCands"),
    nKeepLeps = cms.untracked.uint32(3),
    nKeepJets = cms.untracked.uint32(2),
    nKeepExtra = cms.untracked.uint32(0)
)

process.p = cms.Path(((process.selectedGenParticles*process.leptons*process.sortedLeptons)+ 
    ((process.muons*process.zMuMuCands) + (process.electrons*process.zeeCands)) +
    (process.genParticlesForJetsNoNu*process.ak4GenJetsNoNu)*
    (process.neutrinos*process.sortedNeutrinos) *
    (process.selectedJets*process.sortedJets)) *
    (process.sortedZMuMuCands + process.sortedZeeCands) * 
    process.analyzeWZ
)