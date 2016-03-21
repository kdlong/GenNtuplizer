#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=10 \
    --input-file-list=../../MetaData/ZZ/ZZto2e2mu_8TeV_powheg_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    powhegOff_GenNtuples_ZZto2e2mu8TeV_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ZZto2e2mu-8TeV-PWG \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
