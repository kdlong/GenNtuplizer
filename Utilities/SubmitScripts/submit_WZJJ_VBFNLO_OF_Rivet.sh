#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=5 \
    --input-file-list=../../MetaData/WZJJ_VBS/WZJJ_OF_VBFNLO_GS.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $1 \
    WZJJ_VBS_OF-VBFNLO_GenNtuples_leptonType-rivet_$DATE \
    ../../DibosonGenAnalyzer/test/wzGen_cfg.py \
    useDefaultDataset=WZJJ_OF-VBFNLO-riv \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
