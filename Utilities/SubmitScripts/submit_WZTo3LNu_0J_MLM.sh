#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=5 \
    --input-file-list=../../MetaData/WZ/WZTo3LNu_0J_MLM_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $2 \
    WZTo3LNu_0J_MLM_GenNtuples_leptonType-$1_$DATE \
    ../../DibosonGenAnalyzer/test/wzGen_cfg.py \
    useDefaultDataset=WZTo3LNu-0J-MLM \
    submit=1 \
    leptonType=$1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
