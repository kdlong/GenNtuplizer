import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()

leptonOpts = {"hardProcess" : "isHardProcess",
        "fromHardProcessFS" : "fromHardProcessFinalState", 
        "pythia6HardProcess" :  "status() == 3",
        "finalstate" : "status() == 1",
        "herwig" : "status() == 11",
        "rivet" : "status() == 1",
}
try:
    leptonsFlag = leptonOpts[options.leptonType]
except:
    print "Invalid lepton type choice '%s'. Please choose from" % options.leptonType
    print leptonOpts.keys()
    exit(0)
leptonsSource = "genParticles"
if options.leptonType == "rivet":
    leptonsSource = "particleLevel:leptons"
    from GeneratorInterface.RivetInterface.particleLevel_cfi import particleLevel

    if options.isMiniAOD:
        from GeneratorInterface.RivetInterface.mergedGenParticles_cfi import mergedGenParticles
        from GeneratorInterface.RivetInterface.genParticles2HepMC_cff import *
        genParticles2HepMC.genParticles = cms.InputTag("mergedGenParticles")
        rivetSequence = cms.Sequence(mergedGenParticles * genParticles2HepMC)
    else:
        from SimGeneral.HepPDTESSource.pythiapdt_cfi import *
        particleLevel.src = cms.InputTag("generator")
        rivetSequence = cms.Sequence(particleLevel)

    particleLevel.particleMinPt  = cms.double(0.)
    particleLevel.particleMaxEta = cms.double(999.) # HF range. Maximum 6.0 on MiniAOD
    particleLevel.lepMinPt = cms.double(0.)
    particleLevel.lepMaxEta = cms.double(999)
    particleLevel.jetMaxEta = cms.double(4.7)

elif options.isMiniAOD:
    leptonsSource = "prunedGenParticles"

selectedLeptons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag(leptonsSource),
    cut = cms.string("abs(pdgId) = 11 || abs(pdgId) = 13 && %s" % leptonsFlag)
)

sortedLeptons = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("selectedLeptons"),
    # This needs to be set specifically for ZZ and WZ
    #maxNumber = cms.uint32(3 if options.channel == 'WZ' else 4),
    maxNumber = cms.uint32(5),
)

selectedElectrons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("sortedLeptons"),
    cut = cms.string("abs(pdgId) = 11")
    maxNumber = cms.uint32(5),
)

selectedMuons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("sortedLeptons"),
    cut = cms.string("abs(pdgId) = 13")
    maxNumber = cms.uint32(5),
)

if options.leptonType == "rivet":
    selectLeptons = cms.Sequence(rivetSequence*selectedLeptons*sortedLeptons*(selectedElectrons + selectedMuons))
else:
    selectLeptons = cms.Sequence(selectedLeptons*sortedLeptons*(selectedElectrons + selectedMuons))
