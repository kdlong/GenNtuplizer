import FWCore.ParameterSet.Config as cms

genParticlesLabel = "prunedGenParticles"
massCut = "4"

genElectrons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 11 && isHardProcess()")
)
genMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 13 && isHardProcess()")
)

genZmmCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('genMuons@+ genMuons@-'),
    cut = cms.string('charge=0 && mass > %s' % massCut),
)

genZeeCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('genElectrons@+ genElectrons@-'),
    cut = cms.string('charge=0 && mass > %s' % massCut),
)

genZCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("genZmmCands", "genZeeCands"),
)

zCandsCounter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("genZCands"),
    minNumber = cms.uint32(1)
)

Zmassfilter = cms.Sequence(
    (genElectrons + genMuons)*
    (genZmmCands + genZeeCands)*
    genZCands*
    ~zCandsCounter
)
