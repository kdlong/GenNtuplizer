import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genJetsLabel = "slimmedGenJets" if (options.isMiniAOD and not options.redoJets) else \
    "ak4GenJetsNoNu" if not options.is8TeV else "ak5GenJetsNoNu"

selectJets = cms.Sequence()
if not options.isMiniAOD or options.redoJets:
    genParticlesLabel = "packedGenParticles" if options.isMiniAOD else "genParticles"
    genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
        src = cms.InputTag(genParticlesLabel),
        ignoreParticleIDs = cms.vuint32(
            1000022,
            1000012, 1000014, 1000016,
            2000012, 2000014, 2000016,
            1000039, 5100039,
            4000012, 4000014, 4000016,
            9900012, 9900014, 9900016,
            39,
            12, 14, 16),
        partonicFinalState = cms.bool(False),
        excludeResonances = cms.bool(False),
        excludeFromResonancePids = cms.vuint32(12, 13, 14, 16),
        tausAsJets = cms.bool(False)
    )

    import RecoJets.Configuration.RecoGenJets_cff as RecoGenJets

    if not options.is8TeV:
        ak4GenJetsNoNu = RecoGenJets.ak4GenJets.clone( 
                src = cms.InputTag("genParticlesForJetsNoNu") )
        selectJets += cms.Sequence(genParticlesForJetsNoNu*ak4GenJetsNoNu)
    else:
        ak5GenJetsNoNu = RecoGenJets.ak5GenJets.clone( 
                src = cms.InputTag("genParticlesForJetsNoNu") )
        selectJets += cms.Sequence(genParticlesForJetsNoNu*ak5GenJetsNoNu)

selectedJets = cms.EDFilter("EtaPtMinCandViewSelector",
    src = cms.InputTag(genJetsLabel),
    ptMin   = cms.double(30),
    etaMin = cms.double(-4.7 if not options.is8TeV else -2.5),
    etaMax = cms.double(4.7 if not options.is8TeV else 2.5)
)

sortedJets = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("selectedJets"),
    maxNumber = cms.uint32(10)
)

selectJets += cms.Sequence(selectedJets* sortedJets)
