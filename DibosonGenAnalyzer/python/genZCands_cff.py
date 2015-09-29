from genLeptons_cff import *

zMuMuCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('selectedMuons@+ selectedMuons@-'),
    cut = cms.string('charge=0'),
    minNumber = cms.uint32(2)
)

zeeCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('selectedElectrons@+ selectedElectrons@-'),
    cut = cms.string('charge=0'),
    minNumber = cms.uint32(2)
)
if options.includeTaus:
    zttCands = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string('selectedTaus@+ selectedTaus@-'),
        cut = cms.string('charge=0'),
        minNumber = cms.uint32(2)
    )

combinedZCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", "zeeCands")
)
combinedZCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", "zeeCands")
) if not options.includeTaus else cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", 
        "zeeCands",
        "zttCands"
    )
)
sortedZCands = cms.EDFilter("BestZCandSelector",
    src = cms.InputTag("combinedZCands"),
    maxNumber = cms.uint32(10)
)

trueZs = cms.EDFilter("CandViewSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("pdgId == 23 && isHardProcess")  
)

selectZCands = cms.Sequence((zMuMuCands + zeeCands) if not options.includeTaus else
    (zMuMuCands + zeeCands + zttCands))

selectZCands += cms.Sequence(trueZs + combinedZCands*sortedZCands)
