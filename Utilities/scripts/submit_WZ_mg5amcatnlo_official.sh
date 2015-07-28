#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=5 \
    --input-file-list=../../MetaData/WZ/WZ_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    MGNLO_Off_GenNtuples_weights \
    ../../DibosonGenAnalyzer/test/wzGen_cfg.py \
    useDefaultDataset=WZ-MGNLO-Off \
    submit=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
