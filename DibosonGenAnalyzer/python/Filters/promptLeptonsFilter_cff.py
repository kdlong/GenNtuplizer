import FWCore.ParameterSet.Config as cms

promptMus = cms.EDFilter("GenParticleSelector",
        src = cms.InputTag("prunedGenParticles"),
        cut = cms.string("abs(pdgId) == 13 && isPromptFinalState()")
)
promptEs = cms.EDFilter("GenParticleSelector",
        src = cms.InputTag("prunedGenParticles"),
        cut = cms.string("abs(pdgId) == 11 && isPromptFinalState()")
)
promptLeps = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("promptEs", "promptMus")
)
promptLepsFilter = cms.EDFilter("CandViewCountFilter",
    src = cms.InputTag("promptLeps"),
    minNumber = cms.uint32(4)
)

filterPromptLeps = cms.Sequence(
    (promptMus + promptEs)*
    promptLeps*
    promptLepsFilter
    #~tauFilter
)

