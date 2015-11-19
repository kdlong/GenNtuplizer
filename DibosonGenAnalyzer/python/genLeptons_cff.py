import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"

selectedElectrons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 11 && %s" %
        ("fromHardProcessFinalState" if not options.isHardProcess else "isHardProcess()")) #"statusFlags().fromHardProcessBeforeFSR()"))  
)

selectedMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 13 && %s" %
        ("fromHardProcessFinalState" if not options.isHardProcess else "isHardProcess()")) #"statusFlags().fromHardProcessBeforeFSR()"))  
)

if options.includeTaus:
    selectedTaus = cms.EDFilter("GenParticleSelector",
        src = cms.InputTag(genParticlesLabel),
        cut = cms.string("abs(pdgId) == 15 && isLastCopy && %s" %
            ("statusFlags().fromHardProcess" if not options.isHardProcess else "isHardProcess()"))  
    )

leptons = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("selectedElectrons", "selectedMuons")
) if not options.includeTaus else cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("selectedElectrons", 
        "selectedMuons",
        "selectedTaus"
    )
)

sortedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("leptons"),
    maxNumber = cms.uint32(10)
)
selectLeptons = cms.Sequence(
    (selectedMuons + selectedElectrons) if not options.includeTaus else
    (selectedMuons + selectedElectrons + selectedTaus)
)

selectLeptons += cms.Sequence(leptons*sortedLeptons)
