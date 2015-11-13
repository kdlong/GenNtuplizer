#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=1 \
    --input-file-list=../../MetaData/ZZ/ZZ_mg5amcatnlo_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    MGNLO_Off_GenNtuples_isHardProcess \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ZZ-MGNLO-Off \
    submit=1 \
    hardProcess=0 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
