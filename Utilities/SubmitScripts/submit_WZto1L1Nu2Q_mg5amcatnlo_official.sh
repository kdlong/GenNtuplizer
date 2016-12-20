#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=1 \
    --input-file-list=../../MetaData/WZ/WZto1L1Nu2Q_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    MGNLO_Off_1L1Nu2Q_GenNtuples \
    ../../DibosonGenAnalyzer/test/wzTruthGen_cfg.py \
    useDefaultDataset=WZto1L1Nu2Q-MGNLO-Off \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
