#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=1 \
    --input-file-list=../../MetaData/WZ/WZto2L2Q_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    MGNLO_Off_GenNtuples_withTausV2 \
    ../../DibosonGenAnalyzer/test/wz2l2qGen_cfg.py \
    includeTaus=1 \
    useDefaultDataset=WZto2L2Q-MGNLO-Off \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
