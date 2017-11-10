import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

hardProcessElectrons = cms.EDFilter("CandViewSelector",
        src = cms.InputTag(genParticlesLabel),
        cut = cms.string("abs(pdgId) == 11 && isHardProcess()")
)

hardProcessMuons = cms.EDFilter("CandViewSelector",
        src = cms.InputTag(genParticlesLabel),
        cut = cms.string("abs(pdgId) == 13 && isHardProcess()")
)

muSameFlavorFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("hardProcessMuons"),
    minNumber = cms.uint32(3)
)

eSameFlavorFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("hardProcessElectrons"),
    minNumber = cms.uint32(3)
)

filterSameFlavorChans = cms.Sequence(
    (hardProcessElectrons + hardProcessMuons)*
    ~eSameFlavorFilter*
    ~muSameFlavorFilter
)
