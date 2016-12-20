#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=20 \
    --input-file-list=../../MetaData/Drell-Yan/DYm50_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $1 \
    DrellYan_m50_mg5amcatnlo_GenNtuples_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=DYm50\
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
