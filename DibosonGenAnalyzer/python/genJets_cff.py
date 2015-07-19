import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genJetsLabel = "slimmedGenJets" if options.isMiniAOD else "ak4GenJetsNoNu"

selectJets = cms.Sequence()

if not options.isMiniAOD:
    import RecoJets.Configuration.RecoGenJets_cff as RecoGenJets
    ak4GenJetsNoNu = RecoGenJets.ak4GenJetsNoNu
    selectJets += cms.Sequence(ak4GenJetsNoNu)
elif options.redoJets:
    genParticlesForJetsNoNu = cms.EDProducer("InputGenJetsParticleSelector",
        src = cms.InputTag("packedGenParticles"),
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
    ak4GenJetsNoNu = RecoJets.ak4GenJets.clone( 
            src = cms.InputTag("genParticlesForJetsNoNu") )
    selectJets += cms.Sequence(genParticlesForJetsNoNu*ak4GenJetsNoNu)

selectedJets = cms.EDFilter("EtaPtMinCandViewSelector",
    src = cms.InputTag(genJetsLabel),
    ptMin   = cms.double(30),
    etaMin = cms.double(-4.7),
    etaMax = cms.double(4.7)
)

sortedJets = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("selectedJets"),
    maxNumber = cms.uint32(10)
)

selectJets += cms.Sequence(selectedJets* sortedJets)
