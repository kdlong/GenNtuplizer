import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs
from genNeutrinos_cff import *

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
decay_string = "sortedNeutrinos {type}Leptons@{sign}"
lep_type = "dressed" if options.leptonType == "dressed" else "sorted"

print decay_string.format(type=lep_type, sign="+")
wpCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string(decay_string.format(type=lep_type, sign="+")),
    cut = cms.string('charge=1'),
    checkCharge = cms.bool(False),
    minNumber = cms.uint32(2)
)

wmCands = cms.EDProducer("CandViewShallowCloneCombiner",
    decay = cms.string(decay_string.format(type=lep_type, sign="-")),
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
