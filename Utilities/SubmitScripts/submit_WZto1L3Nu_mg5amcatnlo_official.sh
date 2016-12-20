#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=1 \
    --input-file-list=../../MetaData/WZ/WZto1L3Nu_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    MGNLO_Off_1L3Nu_GenNtuples \
    ../../DibosonGenAnalyzer/test/wz1l3nuGen_cfg.py \
    useDefaultDataset=WZto1L3Nu-MGNLO-Off \
    submit=1 \
    includeTaus=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
