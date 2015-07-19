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
combinedZCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("zMuMuCands", "zeeCands")
)
sortedZCands = cms.EDFilter("BestZCandSelector",
    src = cms.InputTag("combinedZCands"),
    maxNumber = cms.uint32(10)
)

selectZCands = cms.Sequence(
        (zMuMuCands + zeeCands)
        * combinedZCands
        * sortedZCands)
