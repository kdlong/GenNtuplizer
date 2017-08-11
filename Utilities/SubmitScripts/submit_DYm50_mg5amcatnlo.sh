#!/bin/bash
cd ${0%/*}
# Condor submission script
DATE=`date +%Y-%m-%d`
farmoutAnalysisJobs \
    --infer-cmssw-path \
    --input-files-per-job=5 \
    --input-file-list=../../MetaData/Drell-Yan/DYJetsToLL_Inclusive.txt \
    --assume-input-files-exist \
    --input-dir=root://cmsxrootd.fnal.gov/ \
    $2 \
    DY_MLL-50_Official_mg5amcatnloFxFx_GenNtuples_leptonType-$1_$DATE \
    ../../DibosonGenAnalyzer/test/dyGen_cfg.py \
    useDefaultDataset=DYm50 \
    submit=1 \
    leptonType=$1 \
    isMinAOD=1 \
    'inputFiles=$inputFileNames' \
    'outputFile=$outputFileName'
