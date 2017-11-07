import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
leptonOpts = {"hardProcess" : "isHardProcess",
        "fromHardProcessFS" : "fromHardProcessFinalState", 
        "pythia6HardProcess" :  "status() == 3",
        "finalstate" : "status() == 1",
        "herwig" : "status() == 11",
}
try:
    leptonsFlag = leptonOpts[options.leptonType]
except:
    print "Invalid lepton type choice '%s'. Please choose from" % options.leptonType
    print leptonOpts.keys()
    exit(0)
tauFlag = leptonsFlag.replace("fromHardProcessFinalState", "statusFlags().fromHardProcess && isLastCopy")

selectedElectrons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 11 && %s" %
    #cut = cms.string("(abs(pdgId) == 11 || abs(pdgId) == 12 || abs(pdgId) == 14 || abs(pdgId) == 16) && %s" %
            leptonsFlag)
)
selectedMuons = cms.EDFilter("GenParticleSelector",
    src = cms.InputTag(genParticlesLabel),
    cut = cms.string("abs(pdgId) == 13 && %s" % 
            leptonsFlag)
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
        cut = cms.string("abs(pdgId) == 15 && %s" % tauFlag)
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
