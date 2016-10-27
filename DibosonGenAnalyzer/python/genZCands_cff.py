import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
decay_string = "{type}{part}@- {type}{part}@+"
#decay_string = "{type}{part} {type}{part}"
lep_type = "dressed" if options.leptonType == "dressed" else "selected"
zMuMuCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string(decay_string.format(type=lep_type, part="Muons")),
    cut = cms.string('charge=0'),
    minNumber = cms.uint32(2)
)

zeeCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string(decay_string.format(type=lep_type, part="Electrons")),
    cut = cms.string("charge=0"),
    minNumber = cms.uint32(2)
)
if options.includeTaus:
    zttCands = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string(decay_string.format(type="selected", part="Taus")),
        cut = cms.string('charge=0'),
        minNumber = cms.uint32(2)
    )

combinedHPCands = cms.EDProducer("CandViewMerger",
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
        decay = cms.string(decay_string.format(type="radiated", part="Muons")),
        cut = cms.string('charge=0'),
        minNumber = cms.uint32(2)
    )
    radEECands = cms.EDProducer("CandViewShallowCloneCombiner",
        decay = cms.string(decay_string.format(type="radiated", part="Electrons")),
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
        src = cms.VInputTag("combinedHPCands", "combinedRadCands")
    )
    selectZCands += (radMuMuCands+radEECands)*combinedRadCands*combinedHPCands*combinedZCands
else:
    selectZCands += combinedHPCands
sortedZCands = cms.EDFilter("BestZCandSelector",
    src = cms.InputTag("combinedZCands" if options.includeRadiated else "combinedHPCands"),
    maxNumber = cms.uint32(10)
)
selectZCands *= sortedZCands

