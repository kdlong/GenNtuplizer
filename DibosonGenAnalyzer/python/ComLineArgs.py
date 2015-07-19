# parse variables from cmsRun
import os
import sys
from FWCore.ParameterSet.VarParsing import VarParsing
import GenNtuplizer.DibosonGenAnalyzer.default_datasets as default_datasets
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

options.register('useDefaultDataset',
    '', # Default value
    options.multiplicity.singleton,
    options.varType.string,
    "use default dataset. Valid options are: \n"
    "'PWG-Off': POWHEG Official RunII MiniAOD Sample \n"
    "'MGNLO-inc': MG5_aMC@NLO inclusive NLO sample \n"
    "'MGNLO-01j': MG5_aMC@NLO 0,1j NLO FxFx Merged sample \n"
    "'MGLO-inc': MG5_aMC@NLO inclusive NLO sample \n"
)

options.outputFile = "test.root"
options.maxEvents = -1
options.parseArguments() 

if options.inputFiles == "" and options.useDefaultDataset == "":
    sys.stderr.write("You need to enter an inputFile name!")
if options.useDefaultDataset != "":
    sample_info = default_datasets.getSampleInfo(options)
    options.inputFiles = sample_info["inputFiles"]
    options.crossSection = sample_info["crossSection"]
    options.isMiniAOD = sample_info["isMiniAOD"]
    if options.outputFile == "test.root" or "test_numEvent" in options.outputFile:
        if not os.path.isfile(sample_info["outputFile"]): 
            print "Did it"
            options.outputFile = sample_info["outputFile"]    
        else:
            sys.stderr.write('This file already exists! Overwrite? (y/n) ')
            if "Y" in raw_input().upper():
                options.outputFile = sample_info["outputFile"]    
print options.outputFile
if options.outputFile == "test.root":
    sys.stderr.write("You didn't enter an output file name. Using default"
          " name 'test.root'")
if "PWG-Off" in options.useDefaultDataset:
    options.isMiniAOD = 1
elif options.useDefaultDataset != "":
    options.isMiniAOD = 0

def getArgs():
    return options
