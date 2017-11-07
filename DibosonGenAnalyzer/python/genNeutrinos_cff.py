import FWCore.ParameterSet.Config as cms
import GenNtuplizer.DibosonGenAnalyzer.ComLineArgs as ComLineArgs

options = ComLineArgs.getArgs()
genParticlesLabel = "genParticles" if not options.isMiniAOD else "prunedGenParticles"
neuOpts = {"hardProcess" : "isHardProcess()",
        "fromHardProcessFS" : "statusFlags().fromHardProcess() && status() == 1",
        "pythia6HardProcess" :  "status() == 1",
        "dressed" : "statusFlags().fromHardProcess() && status() == 1",
        "finalstate" : "status() == 1",
        "herwig" : "status() == 11",
        "rivet" : "",
}
try:
    neutrinoFlag = neuOpts[options.leptonType]
except:
    print "Invalid lepton type choice '%s'. Please choose from" % options.leptonType
    print neuOpts.keys()
    exit(0)

neutrino_cut = "" if options.leptonType == "rivet" else \
        "(abs(pdgId) == 12 || abs(pdgId) == 14 || abs(pdgId) == 16) && %s" % neutrinoFlag
neutrinos = cms.EDFilter("CandViewSelector",
    src = cms.InputTag(genParticlesLabel if options.leptonType != "rivet" else "particleLevel:neutrinos"),
    cut = cms.string(neutrino_cut)
)

sortedNeutrinos = cms.EDFilter("LargestPtCandSelector",
    src = cms.InputTag("neutrinos"),
    maxNumber = cms.uint32(10)
)

selectNeutrinos = cms.Sequence(neutrinos*sortedNeutrinos)
