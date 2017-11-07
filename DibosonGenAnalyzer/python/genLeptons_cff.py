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
    maxNumber = cms.uint32(10),
)

selectedElectrons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("sortedLeptons"),
    cut = cms.string("abs(pdgId) = 11")
)

selectedMuons = cms.EDFilter("CandViewSelector",
    src = cms.InputTag("sortedLeptons"),
    cut = cms.string("abs(pdgId) = 13")
)

selectLeptons = cms.Sequence(selectedLeptons*sortedLeptons*(selectedElectrons + selectedMuons))
