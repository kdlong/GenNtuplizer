#!/bin/bash
#./fixGen.sh <name> <filelist> <extra_args>
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=10 \
    --input-file-list=$2 \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $3 \
    $1_$DATE \
    ../../DibosonGenAnalyzer/test/fixGen_cfg.py \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
