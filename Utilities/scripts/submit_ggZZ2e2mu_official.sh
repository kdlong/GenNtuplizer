#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=10 \
    --input-file-list=../../MetaData/ZZ/ggZZ2e2mu_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    ggZZ2e2mu_GenNtuples_isHardProcess_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ggZZ2e2mu-Off \
    submit=1 \
    isHardProcess=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
