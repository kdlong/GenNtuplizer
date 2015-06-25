import FWCore.ParameterSet.Config as cms

process = cms.Process("Demo")

process.load("FWCore.MessageService.MessageLogger_cfi")
process.load("PhysicsTools.HepMCCandAlgos.genParticles_cfi")
process.load("SimGeneral.HepPDTESSource.pythiapdt_cfi")

# parse variables from cmsRun
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')

options.inputFiles = ""
options.outputFile = ""
options.maxEvents = -1
options.parseArguments() 

#process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet(input=cms.untracked.int32(options.maxEvents))

process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
        'file:/afs/cern.ch/user/k/kelong/work/WZ_MCAnalysis/POWHEG_WZ/WZ_powheg_pythia8_CUETP8M1_10E5ev.root'
    )
)

process.TFileService = cms.Service("TFileService",
    fileName = cms.string(options.outputFile)
)

process.genParticlesClone = cms.EDFilter("CandViewShallowCloneProducer",
                             src = cms.InputTag("genParticles"),
    cut = cms.string("pt > 10 & abs( eta ) < 2.4")                           
                             )


process.rawmuons = cms.EDFilter("PdgIdAndStatusCandSelector",
                           src = cms.InputTag("genParticlesClone"),
                           pdgId = cms.vint32( 13 ),
                           status = cms.vint32( 1 )                          
)


process.rawelectrons = cms.EDFilter("PdgIdAndStatusCandSelector",
                           src = cms.InputTag("genParticlesClone"),
                           pdgId = cms.vint32( 11 ),
                           status = cms.vint32( 1 )                          
)

process.jets = cms.EDProducer("GenJetShallowCloneProducer",
                              src = cms.InputTag("ak5GenJets")
                              )

process.selectedMuons = cms.EDFilter("CandSelector",
    src = cms.InputTag("rawmuons"),
    cut = cms.string("pt > 10 & abs( eta ) < 2.4")
  )

process.selectedElectrons = cms.EDFilter("CandSelector",
    src = cms.InputTag("rawelectrons"),
    cut = cms.string("pt > 15 & abs( eta ) < 2.5")
  )

# should require e/mu to be isolated

process.selectedJets = cms.EDFilter("CandSelector",
    src = cms.InputTag("jets"),
    cut = cms.string("pt > 50 & abs( eta ) < 2.5")
  )


process.countFilter = cms.EDFilter("CandCountFilter",
                                   src = cms.InputTag("selectedJets"),
                                   minNumber = cms.uint32(3)
                                   )


process.electronVeto = cms.EDFilter("CandCountFilter",
                                   src = cms.InputTag("selectedElectrons"),
                                   minNumber = cms.uint32(1)
                                   )


process.muonVeto = cms.EDFilter("CandCountFilter",
                                   src = cms.InputTag("selectedMuons"),
                                   minNumber = cms.uint32(1)
                                   )


process.demo= cms.EDAnalyzer("CandViewHistoAnalyzer",
#                           src = cms.InputTag("ak5GenJetsClone"),
                            src = cms.InputTag("selectedElectrons"),                             
      # weights = cms.untracked.InputTag("myProducerLabel"),                               
     histograms = cms.VPSet(
        cms.PSet(
            itemsToPlot = cms.untracked.int32(1),
            min = cms.untracked.double(0.0),
            max = cms.untracked.double(1000.0),
            nbins = cms.untracked.int32(100),
            name = cms.untracked.string("missing_pT"),
            description = cms.untracked.string("pT [GeV/c]"),
            plotquantity = cms.untracked.string("pt")
        ),
        cms.PSet(
            itemsToPlot = cms.untracked.int32(1),
            min = cms.untracked.double(0.0),
            max = cms.untracked.double(1000.0),
            nbins = cms.untracked.int32(100),
            name = cms.untracked.string("electronEta"),
            description = cms.untracked.string("eta [GeV]"),
            plotquantity = cms.untracked.string("eta")
        )
    )
)
        

process.p = cms.Path(
    process.genParticles*
    process.genParticlesClone *

process.rawmuons *

process.rawelectrons *

process.jets *

process.selectedMuons *

process.selectedElectrons *

process.selectedJets *

                     process.demo)
