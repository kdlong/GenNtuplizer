import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

sortedDressedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("particleLevel:neutrinos"),
    maxNumber = cms.uint32(10),
)
dressedElectrons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("sortedDressedLeptons"),
    cut = cms.string("abs(pdgId) = 11")
)
dressedMuons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("sortedDressedLeptons"),
    cut = cms.string("abs(pdgId) = 13")
)

rivetDressLeptons = cms.Sequence(sortedDressedLeptons*(dressedElectrons + dressedMuons))
