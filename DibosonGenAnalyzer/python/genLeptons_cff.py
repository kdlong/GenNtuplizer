import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

selectedElectrons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 11 && fromHardProcessFinalState")  
)

selectedMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 13 && fromHardProcessFinalState")  
)

leptons = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("selectedElectrons", "selectedMuons")
)

sortedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("leptons"),
    maxNumber = cms.uint32(10)
)

selectLeptons = cms.Sequence( 
        (selectedMuons + selectedElectrons)
        * leptons
        * sortedLeptons)
