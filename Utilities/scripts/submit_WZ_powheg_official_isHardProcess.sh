#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=1 \
    --input-file-list=../../MetaData/WZ/WZ_powheg_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $1 \
    powhegOff_GenNtuples_isHardProcess \
    ../../DibosonGenAnalyzer/test/wzGen_cfg.py \
    useDefaultDataset=WZ-PWG-Off \
    isHardProcess=1 \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
