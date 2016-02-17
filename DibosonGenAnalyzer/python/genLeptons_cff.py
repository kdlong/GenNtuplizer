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

radiatedElectrons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 11 && isPromptFinalState() && !fromHardProcessFinalState()")
)

radiatedMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 13 && isPromptFinalState() && !fromHardProcessFinalState()")
)
if options.includeTaus:
    selectedTaus = cms.EDFilter("GenParticleSelector",
        src = cms.InputTag(genParticlesLabel),
        cut = cms.string("abs(pdgId) == 15 && %s" %
            ("statusFlags().fromHardProcess && isLastCopy" if not options.isHardProcess else "isHardProcess()"))  
    )

hpleptons = cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("selectedElectrons", "selectedMuons")
) if not options.includeTaus else cms.EDProducer("CandViewMerger",
    src = cms.VInputTag("selectedElectrons", 
        "selectedMuons",
        "selectedTaus"
    )
)
selectLeptons = cms.Sequence(
    (selectedMuons + selectedElectrons) if not options.includeTaus else
    (selectedMuons + selectedElectrons + selectedTaus)
)

if options.includeRadiated:
    radiatedLeptons = cms.EDProducer("CandViewMerger",
        src = cms.VInputTag("radiatedElectrons", "radiatedMuons")
    )
    allleptons = cms.EDProducer("CandViewMerger",
        src = cms.VInputTag("radiatedLeptons", "hpleptons")
    )
    selectLeptons += ((radiatedMuons + radiatedElectrons)*hpleptons*radiatedLeptons*allleptons)
else:
    selectLeptons += hpleptons
sortedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("hpleptons" if not options.includeRadiated else "allleptons"),
    maxNumber = cms.uint32(10)
)
selectLeptons += sortedLeptons
