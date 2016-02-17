#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=10 \
    --input-file-list=../../MetaData/ZZ/ZZ_powheg_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    powhegOff_GenNtuples_isHardProcess_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ZZ-PWG-Off \
    submit=1 \
    isHardProcess=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
