import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

hardProcessTausP = cms.EDFilter("GenParticleSelector",
        src = cms.InputTag(genParticlesLabel),
        cut = cms.string("pdgId == 15 && isHardProcess()")
)
hardProcessTausM = cms.EDFilter("GenParticleSelector",
        src = cms.InputTag(genParticlesLabel),
        cut = cms.string("pdgId == -15 && isHardProcess()")
)
hardProcessTaus = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("hardProcessTausP", "hardProcessTausM")
)
tauFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("hardProcessTaus"),
    minNumber = cms.uint32(1)
)

filterGenTaus = cms.Sequence(
    (hardProcessTausM + hardProcessTausP)*
    hardProcessTaus*
    ~tauFilter
)
