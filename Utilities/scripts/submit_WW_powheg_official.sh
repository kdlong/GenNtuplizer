#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=10 \
    --input-file-list=../../MetaData/WZ/WZ_powheg_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $1 \
    powhegOff_GenNtuples_isHardProcess_$DATE \
    ../../DibosonGenAnalyzer/test/wwGen_cfg.py \
    useDefaultDataset=WW-PWG-Off \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
