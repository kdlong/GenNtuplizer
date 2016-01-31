# parse variables from cmsRun
import os
import sys
from FWCore.ParameterSet.VarParsing import VarParsing
import GenNtuplizer.MetaData.default_datasets as default_datasets
options = VarParsing ('analysis')

options.register ('crossSection',
    -1,
    VarParsing.multiplicity.singleton,
    VarParsing.varType.float,
    "Process cross section"
)
options.register('isMiniAOD',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "is MiniAOD file (run over prunedGenParticles"
    " rather than genParticles)"
)
options.register('includeTaus',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "include gen taus in ntuple"
)
options.register('genMet',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "Use genMET instead of neutrinos"
)
options.register('isHardProcess',
    1, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "require leptons be from hard process"
)
options.register('includeRadiated',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "Include leptons from radiated gamma*"
)
options.register('submit',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "is MiniAOD file (use input_file_list rather"
    " than those specficed useby DefaultDataset)"
)
options.register('redoJets',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "Remake GenJetsNoNu (only valid for miniAOD,"
    " and only necessary for Phys14 samples)"
)
options.register('is8TeV',
    0, # Default value
    options.multiplicity.singleton,
    options.varType.int,
    "use 8 TeV setup (for jets)"
)
options.register('useDefaultDataset',
    '', # Default value
    options.multiplicity.singleton,
    options.varType.string,
    "use default dataset. Valid options are: \n"
    "'PWG-Off': POWHEG Official RunII MiniAOD Sample \n"
    "'MGNLO-inc': MG5_aMC@NLO inclusive NLO sample \n"
    "'MGNLO-01j': MG5_aMC@NLO 0,1j NLO FxFx Merged sample \n"
    "'MGLO-inc': MG5_aMC@NLO inclusive NLO sample \n"
    "'MGLO-Phys14': MG5_aMC@NLO LO 012j SUSY Phys14 sample \n"
)

options.outputFile = "test.root"
options.maxEvents = -1
options.parseArguments() 


def getArgs():
    if options.inputFiles == "" and options.useDefaultDataset == "":
        sys.stderr.write("You need to enter an inputFile name!")
    if options.useDefaultDataset != "":
        sample_info = default_datasets.getSampleInfo(options)
        if not options.submit:
            options.inputFiles = sample_info["inputFiles"]
        options.crossSection = sample_info["crossSection"]
        options.isMiniAOD = sample_info["isMiniAOD"]
        if "isHardProcess" in sample_info.keys():
            options.isHardProcess = sample_info["isHardProcess"]
        if "includeRadiated" in sample_info.keys():
            options.includeRadiated = sample_info["includeRadiated"]
        if "redoJets" in sample_info.keys():
            options.redoJets = sample_info["redoJets"]
        if "is8TeV" in sample_info.keys():
            options.is8TeV = sample_info["is8TeV"]
        if options.outputFile == "test.root" or "test_numEvent" in options.outputFile:
            if not os.path.isfile(sample_info["outputFile"]): 
                options.outputFile = sample_info["outputFile"]    
            else:
                sys.stderr.write('The file %s already exists! Overwrite? (y/n) ' % sample_info["outputFile"])
                if "Y" in raw_input().upper():
                    options.outputFile = sample_info["outputFile"]    
                else:
                    exit(0)
    if options.outputFile == "test.root":
        sys.stderr.write("You didn't enter an output file name. Using default"
            " name 'test.root'")    
    return options
