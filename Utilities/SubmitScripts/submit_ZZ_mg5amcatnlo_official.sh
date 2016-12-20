#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=5 \
    --input-file-list=../../MetaData/ZZ/ZZ_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $2 \
    MGNLO_Off_GenNtuples_leptonType-$1_$DATE \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ZZ-MGNLO-Off \
    submit=1 \
    leptonType=$1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
