from genLeptons_cff import *
from genNeutrinos_cff import *

#wCands = cms.EDProducer("CandViewShallowCloneCombiner",
#    decay = cms.string('sortedNeutrinos sortedLeptons'),
#    cut = cms.string('charge=1 || charge=-1'),
#    checkCharge = cms.bool(False),
#    minNumber = cms.uint32(2)
#)
#
wpCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('sortedNeutrinos sortedLeptons@+'),
    #decay = cms.string('sortedNeutrinos selectedMuons@+'),
    cut = cms.string('charge=1'),
    checkCharge = cms.bool(False),
    minNumber = cms.uint32(2)
)

wmCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string('sortedNeutrinos sortedLeptons@-'),
    #decay = cms.string('sortedNeutrinos selectedMuons@-'),
    cut = cms.string('charge=-1'),
    checkCharge = cms.bool(False),
    minNumber = cms.uint32(2)
)

combinedWCands = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("wmCands", "wpCands")
)

sortedWCands = cms.EDFilter("BestWCandSelector",
    src = cms.InputTag("combinedWCands"),
    maxNumber = cms.uint32(10)
)

trueWs = cms.EDFilter("CandViewSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 24 && isHardProcess")  
)
selectWCands = cms.Sequence(
        (wpCands + wmCands + trueWs)
        * combinedWCands
        * sortedWCands)
