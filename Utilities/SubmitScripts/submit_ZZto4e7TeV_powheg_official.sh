#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=5 \
    --input-file-list=../../MetaData/ZZ/ZZto4e_7TeV_powheg_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    powhegOff_GenNtuples_ZZto4e7TeV_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ZZto4e-7TeV-PWG \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
