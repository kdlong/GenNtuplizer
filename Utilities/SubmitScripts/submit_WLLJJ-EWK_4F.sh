#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=3 \
    --input-file-list=../../MetaData/WZJJ_VBS/WLLJJ-EWK_4F_files.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $2 \
    WLLJJ_WToLNu_EWK_4F-MGLO_Off_GenNtuples_leptonType-$1_$DATE \
    ../../DibosonGenAnalyzer/test/wzGen_cfg.py \
    useDefaultDataset=WLLJJ_EWK_4F-MGLO \
    submit=1 \
    leptonType=$1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
