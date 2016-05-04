import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
leptonsFlag = "status = 3" if options.isPythia6 else "fromHardProcessFinalState"

fromHPFSleptons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("(abs(pdgId) == 11 || abs(pdgId) = 13) && %s" %
            leptonsFlag)
)
promptPhotons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("pdgId = 22 && isPromptFinalState")
)
dressedLeptons = cms.EDProducer("DressedGenParticlesProducer",
    baseCollection = cms.InputTag("fromHPFSleptons"),
    associates = cms.InputTag("promptPhotons"),
    dRmax = cms.untracked.double(0.1)
)
#sortedDressedLeptons = cms.EDFilter("LargestPtCandSelector",
#    src = cms.InputTag("dressedLeptons"),
#    maxNumber = cms.uint32(10)
#)

dressLeptons = cms.Sequence((fromHPFSleptons + promptPhotons)
        *dressedLeptons)#*sortedDressedLeptons)
