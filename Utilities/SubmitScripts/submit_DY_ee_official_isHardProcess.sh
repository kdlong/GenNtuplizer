#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=10 \
    --input-file-list=../../MetaData/Drell-Yan/DY_ee_powheg_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $1 \
    powhegOff_DYeeM50_GenNtuples_isHardProcess_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=DYeeM50 \
    isHardProcess=1 \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
