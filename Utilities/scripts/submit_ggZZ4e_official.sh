#!/bin/bash
cd ${0%/*}
# Condor submission script
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=1 \
    --input-file-list=../../MetaData/ZZ/ggZZ4e_files.txt \
    --assume-input-files-exist \
    $1 \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    ggZZ4e_GenNtuples_isHardProcess \
    ../../DibosonGenAnalyzer/test/zzGen_cfg.py \
    useDefaultDataset=ggZZ4e-Off \
    submit=1 \
    hardProcess=0 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
