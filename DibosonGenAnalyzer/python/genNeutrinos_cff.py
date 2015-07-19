import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

neutrinos = cms.EDFilter("CandViewSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("(abs(pdgId) == 12 || abs(pdgId) == 14 || abs(pdgId) == 16)" 
                     " && fromHardProcessFinalState")  
)

sortedNeutrinos = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("neutrinos"),
    maxNumber = cms.uint32(10)
)

selectNeutrinos = cms.Sequence(neutrinos*sortedNeutrinos)
