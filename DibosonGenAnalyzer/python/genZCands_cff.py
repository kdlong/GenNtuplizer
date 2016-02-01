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

_combinedHPCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", "zeeCands")
) if not options.includeTaus else cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", 
        "zeeCands",
        "zttCands"
    )
)

trueZs = cms.EDFilter("CandViewSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("pdgId == 23 && isHardProcess")  
)

selectZCands = cms.Sequence(((zMuMuCands + zeeCands) if not options.includeTaus else
    (zMuMuCands + zeeCands + zttCands))*trueZs)


if options.includeRadiated:
    radMuMuCands = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string('radiatedMuons@+ radiatedMuons@-'),
        cut = cms.string('charge=0'),
        minNumber = cms.uint32(2)
    )
    radEECands = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string('radiatedElectrons@+ radiatedElectrons@-'),
        cut = cms.string('charge=0'),
        minNumber = cms.uint32(2)
    )
    combinedRadCands = cms.EDProducer("CandViewMerger",
        src = cms.VInputTag("radMuMuCands", "radEECands")
    )
    sortedRadCands = cms.EDFilter("BestZCandSelector",
        src = cms.InputTag("combinedRadCands"),
        maxNumber = cms.uint32(10)
    )
    combinedZCands = cms.EDProducer("CandViewMerger",
        src = cms.VInputTag("combinedZCands", "combinedRadCands")
    )
    selectZCands += (radMuMuCands+radEECands)*combinedRadCands*_combinedHPCands
else:
    combinedZCands = _combinedHPCands
sortedZCands = cms.EDFilter("BestZCandSelector",
    src = cms.InputTag("combinedZCands"),
    maxNumber = cms.uint32(10)
)
selectZCands += cms.Sequence(combinedZCands*sortedZCands)

