def getSampleInfo(options):
    sample_info = { 
        'WZ-MGLO-Phys14' : {
            "inputFiles" :
                """/store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/243769ED-4C6B-E411-A87D-000F530E4774.root
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/3AB77DFA-306B-E411-B601-000F530E4790.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/3EBD7BC1-526B-E411-BF6A-D4AE52E945A0.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/B63AEDB9-396B-E411-9695-0002C94CD0EC.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/F20317FD-306B-E411-80F0-0026B95CD6D9.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/FCE80F2E-316B-E411-B867-AC853DA0692A.root""",
            "crossSection" : 1.634, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/WZ012j_LO_SUSY_PHYS14/MGLO_WZ012j_SUSYPhys14_pythia8_Ntuple.root",
            "isMiniAOD" : 1,
            "redoJets" : 1
        },
        'WZto2L2Q-PWG': {
            "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/POWHEG_WZto2L2Q/WZto2L2Q_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 6.789, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/POWHEG_WZto2L2Q/WZto2L2Q_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZto2E1Mu1Nu-8TeV-NewPDFs-PWG': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZ_8TeV/Newest_PDFs/WZto2E1Mu1Nu_8TeV_newpdfs_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 0.076555, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZ_8TeV/Newest_PDFs/WZto2E1Mu1Nu_8TeV_newpdfs_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "is8TeV" : 1
        },
        'WZto2Mu1E1Nu-8TeV-2013PDFs-PWG': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZ_8TeV/2013_PDFs/WZto2Mu1E1Nu_8TeV_2013pdfs_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 0.077067, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZ_8TeV/2013_PDFs/WZto2Mu1E1Nu_8TeV_2013pdfs_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZto2L2Q-PWG-neg': {
            "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/POWHEG_WZto2L2Q/mll4_negweights/WZto2L2Q_powheg_negweights_pythia8_CUETP8M1.root",
            "crossSection" : 6.789, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/POWHEG_WZto2L2Q/WZto2L2Q_powheg_negweights_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        "ZZto2e2mu-8TeV-PWG" : {
            "inputFiles" : "/store/mc/Summer12_DR53X/ZZTo2e2mu_8TeV-powheg-pythia6/AODSIM/PU_RD1_START53_V7N-v2/10000/02A8AB2C-7DD0-E211-9200-00266CFFC7CC.root",
            "crossSection" : 0.1767, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ/ZZto2e2mu_8TeV_powheg_pythia6.root",
            "isMiniAOD" : 0
        },
        "ZZto2e2mu-7TeV-PWG" : {
            "inputFiles" : "/store/mc/Summer11LegDR/ZZTo2e2mu_mll4_7TeV-powheg-pythia6/AODSIM/PU_S13_START53_LV6-v1/00000/0A571FF3-6392-E411-AB3D-0025904B12FC.root",
            "crossSection" : 0.152, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ/ZZto2e2mu_7TeV_powheg_pythia6.root",
            "isMiniAOD" : 0
        },
        "ZZto4e-8TeV-PWG" : {
            "inputFiles" : "/store/mc/Summer12_DR53X/ZZTo4e_8TeV-powheg-pythia6/AODSIM/PU_RD1_START53_V7N-v2/20000/022A8CC0-3ED2-E211-B800-00266CFF0234.root",
            "crossSection" : 0.07691, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ/ZZto4e_8TeV_powheg_pythia6.root",
            "isMiniAOD" : 0
        },
        "ZZto4e-7TeV-PWG" : {
            "inputFiles" : "/store/mc/Summer11LegDR/ZZTo4e_mll4_7TeV-powheg-pythia6/AODSIM/PU_S13_START53_LV6-v1/00000/02DBA701-3392-E411-B8FF-1CC1DE04FF98.root",
            "crossSection" : 0.06609, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ/ZZto4e_7TeV_powheg_pythia6.root",
            "isMiniAOD" : 0
        },
        'DYm10-50': {
            "inputFiles" : """/store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/2699AF1F-9F6D-E511-BDD8-0025901D4AF0.root,
                /store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8E01AB4A-9E6D-E511-A8F9-0025901D4C44.root,
                /store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/8E646CF8-9E6D-E511-993C-0025907DBA06.root,
                /store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/92A460D0-9D6D-E511-8B8E-0025907DC9BE.root,
                /store/mc/RunIISpring15MiniAODv2/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/30000/00D1FF52-036F-E511-A7F8-047D7B881D90.root""",
            "crossSection" : 18610, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/DrellYan-ZZselection/DYJetsToLL_M-10to50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_Ntuple.root",
            "isMiniAOD" : 1,
            "includeRadiated" : 1,
            "isHardProcess" : 0
        },
        'DYm50': {
            "inputFiles" : "/store/mc/RunIISpring15DR74/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v3/10000/009D49A5-7314-E511-84EF-0025905A605E.root",
            "crossSection" : 6025.2, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/DrellYan-ZZselection/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_Ntuple.root",
            "isMiniAOD" : 1,
            "includeRadiated" : 1,
            "isHardProcess" : 0
        },
        'DYeeM50': {
            "inputFiles" : "/store/mc/RunIISpring15DR74/DYToEE_NNPDF30_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/FA2E71F8-D55F-E511-80BC-0CC47A0AD704.root",
            "crossSection" : 1997.4, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/DrellYan-ZZselection/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8_Ntuple.root",
            "isMiniAOD" : 1,
            "isHardProcess" : 1
        },
        'pp_2e2mu-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.1922, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'pp_2e2mu-MGNLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/ZZ_br_studies/pp_2e2mu_mg5amcatnlo_NLO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.2790,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/ZZ_br_studies/pp_2e2mu_mg5amcatnlo_NLO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 0
        },
        'pp_ZZ_2e2mu-MGNLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/ZZ_br_studies/pp_ZZ_2e2mu_mg5amcatnlo_NLO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.03238,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/ZZ_br_studies/pp_ZZ_2e2mu_mg5amcatnlo_NLO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 0
        },
        'pp_2e2mu_singleres-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_2e2mu_singleres_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.1009,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_2e2mu_singleres_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'pp_2e2mu_doubleres-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_2e2mu_doubleres_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.08718,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_2e2mu_doubleres_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'pp_Z_2e2mu-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_Z_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.1344,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_Z_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'pp_Z-a_2e2mu-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_Z-a_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.3059, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_Z-a_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'pp_ZZ_2e2mu-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_ZZ_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.02209,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_ZZ_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'pp_ZZ-aa_2e2mu-MGLO': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_ZZ-Za-aa_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1.root",
            "crossSection" : 0.4176, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/Z4l_MG5aMCatNLO/pp_ZZ-Za_2e2mu_mg5amcatnlo_LO_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0,
            "isHardProcess" : 1
        },
        'WZto2L2Q-MGNLO-Off' : { "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/00456448-0734-E511-BABA-002618943982.root,
                /store/mc/RunIISpring15DR74/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/04BFCB9E-E82F-E511-A94B-00A0D1EE8AF0.root,
                /store/mc/RunIISpring15DR74/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/04DC406D-9531-E511-9B30-001E6739702B.root""",
            "crossSection" : 5.593, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto2L2Q_Official/MG5aMCatNLO_WZTo2L2Q_Official_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'WZto1L1Nu2Q-MGNLO-Off' : { "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/00949148-3813-E511-BEA1-F45214938690.root,
                /store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/063EC4F5-3413-E511-88BB-00259059642A.root,
                /store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0857B822-3513-E511-AC33-002590596490.root,
                /store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0A553E15-3513-E511-898C-0025905A613C.root""",
            "crossSection" : 10.71, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto1L1Nu2Q_Official/MG5aMCatNLO_WZTo1L1Nu2Q_Official_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'WZto1L3Nu-MGNLO-Off' : { "inputFiles" : 
            """/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/640F0CA0-5841-E511-92B5-B083FECF83AB.root""",
            "crossSection" : 3.06, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto1L3Nu_Official/test.root",
            "isMiniAOD" : 1
        },
        'WZto2L2Q-MGNLO-inc' : { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto2L2Q_Incl/MG5aMCatNLO_WZto2L2Q_Incl_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.493, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto2L2Q_Incl/MG5aMCatNLO_WZto2L2Q_Incl_pythia8_TuneCUETP8M1_Ntuple.root",  
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-inc' : { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j/MG5aMCatNLO_WZ0j_pythia8_TuneCUETP8M1.root",
            "crossSection" : 4.415, 
            "outputFile" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j/MG5aMCatNLO_WZ0j_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-inc-ERROR' : { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j_OfficialGridpack/MG5aMCatNLO_WZ0j_OfficialGridpack_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.246, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j_OfficialGridpack/MG5aMCatNLO_WZ0j_OfficialGridpack_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-01j' : { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialGridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.300, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialGridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGLO-inc': { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MGLO_WZ0j/MGLO_WZ0j_10E5ev_pythia8_MLM.root",
            "crossSection" : 1.333, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MGLO_WZ0j/MGLO_WZ0j_10E5ev_pythia8_MLM_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-Off' : {
            "inputFiles" :
                """/store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/002CAF8C-3A26-E511-B14A-0025905A607E.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/00F5EF70-3326-E511-8AFF-0025905A6066.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/06F9B6E2-A629-E511-B9E2-B083FED76637.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/0A80F6F9-2D2A-E511-88E0-008CFA1111E0.root""",
            "crossSection" : 5.289, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialSample/MG5aMCatNLO_WZ01j_OfficialSample_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'WZ-MGNLO-Off-New' : {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialGridpack/new_gridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_new_pythia8_TuneCUETP8M1.root",
            "crossSection" : 4.712, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialGridpack/new_gridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_new_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-PWG-Off': {
            "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/008E7FBF-9218-E511-81E0-001E675A5244.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0473AA1C-AE18-E511-A22A-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0C4172B8-9218-E511-B9C9-001E675A58D9.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1299A85E-9E18-E511-AE6C-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/20469B1E-9F18-E511-A402-0002C94CD12E.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/260EDE5C-9618-E511-9769-001517E74088.root""",
            "crossSection" : 4.430, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/POWHEG_WZ/WZ_powheg_pythia8_CUETP8M1_officialSample_Ntuple.root",
            "isMiniAOD" : 1
        },
        'ZZ-MGNLO-Off' : {
            "inputFiles" :    
                """/store/mc/RunIISpring15DR74/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25nsRaw_MCRUN2_74_V9-v1/00000/0425A914-C418-E511-A263-001E675A6C2A.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25nsRaw_MCRUN2_74_V9-v1/00000/0AF7C688-CF16-E511-AB82-BC305B390A59.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25nsRaw_MCRUN2_74_V9-v1/00000/12E42C96-F316-E511-8140-0025905C3E36.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25nsRaw_MCRUN2_74_V9-v1/00000/148A64B2-3218-E511-954E-0025905C3D98.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt25nsRaw_MCRUN2_74_V9-v1/00000/14EF82CE-1518-E511-84A8-02163E011BAC.root""",
            "crossSection" : 1.191, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_ZZ01j_OfficialSample/MG5aMCatNLO_ZZ01j_OfficialSample_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'ZZ-PWG-Off': {
            "inputFiles" : 
                """/store/mc/RunIISpring15DR74/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/20D8A050-8216-E511-8497-0025905B8562.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/22F87455-8216-E511-8CFC-003048FF9AC6.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/2C0279E7-9B16-E511-B5FF-90B11C2ACF20.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/2C89C1AB-7B16-E511-8BE9-00266CF9AFF0.root,
                /store/mc/RunIISpring15DR74/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/00000/34EA7F00-9116-E511-9ABD-AC853D9DAC1D.root""",
            "crossSection" : 1.256, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ/ZZ_powheg_pythia8_CUETP8M1_officialSample_Ntuple.root",
            "isMiniAOD" : 1
        },
        'ZZeemm-PWG-lowmass': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ_lowmass/ZZeemm_lowmass_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 0.241305,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ_lowmass/ZZeemm_lowmass_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'ZZeemm-PWG-DoubleRes': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ_doubleRes/ZZ_eemm_doubleresonant_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 0.1491, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ_doubleRes/ZZ_eemm_doubleresonant_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'ZZeeee-PWG-DoubleRes': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ_doubleRes/ZZ_eeee_doubleresonant_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 0.057643,
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_ZZ_doubleRes/ZZ_eeee_doubleresonant_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WW-PWG-Off': {
            "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/082EF100-DC05-E511-AD3F-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1A158D26-E005-E511-BD80-00074305CDC0.root,
                /store/mc/RunIISpring15DR74/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/22314C20-7A07-E511-989B-A0040420FE80.root""",
            "crossSection" : 10.481, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/POWHEG_WW/test.root",
            "isMiniAOD" : 1
        },
        'WW-MGNLO-inc': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/WW_nodecay/WW_MG5aMC_nodecay_pdf_pythia8_TuneCUETP8M1.root",
            "crossSection" : 100.12, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/WW_nodecay/WW_MG5aMC_nodecay_pdf_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'ZZ-MGNLO-inc' : { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/ZZTo4LNu0j_5f_NLO_FXFX/MG5aMCatNLO_ZZTo4LNu0j_muMass_pythia8_TuneCUETP8M1.root",
            "crossSection" : 1.181, 
            "outputFile" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/ZZTo4LNu0j_5f_NLO_FXFX/MG5aMCatNLO_ZZTo4LNu0j_muMass_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'ZZ-MGNLO-Off-mumass' : { "inputFiles" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_ZZ01j_OfficialSample/MG5aMCatNLO_ZZ01j_OfficialSample_mumass_pythia8_TuneCUETP8M1.root",
            "crossSection" : 1.208, 
            "outputFile" : "/nfs_scratch/kdlong/DibosonGenAnalysisSamples/MG5aMCatNLO_ZZ01j_OfficialSample/MG5aMCatNLO_ZZ01j_OfficialSample_mumass_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'ggZZ4e-Off' : { "inputFiles" : 
                """/store/mc/RunIISpring15MiniAODv2/GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM/MINIAODSIM/Asympt50ns_74X_mcRun2_asymptotic50ns_v0-v1/50000/30874BFE-8875-E511-8BBD-0025905A60E4.root,
                /store/mc/RunIISpring15MiniAODv2/GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM/MINIAODSIM/Asympt50ns_74X_mcRun2_asymptotic50ns_v0-v1/50000/6AD05CB5-2975-E511-AA0F-FA163E67EB6F.root,
                /store/mc/RunIISpring15MiniAODv2/GluGluToZZTo4e_BackgroundOnly_13TeV_MCFM/MINIAODSIM/Asympt50ns_74X_mcRun2_asymptotic50ns_v0-v1/50000/76FECEFE-8875-E511-A056-0025905AA9CC.root""",
            "crossSection" : 0.001586,
            "outputFile" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/ZZTo4LNu0j_5f_NLO_FXFX/ggZZ4e_MCFM_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'ggZZ2e2mu-Off' : { "inputFiles" : 
                """/store/mc/RunIISpring15MiniAODv2/GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/D23334DE-4871-E511-A11E-0025905B8562.root,
                /store/mc/RunIISpring15MiniAODv2/GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/E2F9EED9-4871-E511-B690-002618943966.root,
                /store/mc/RunIISpring15MiniAODv2/GluGluToZZTo2e2mu_BackgroundOnly_13TeV_MCFM/MINIAODSIM/74X_mcRun2_asymptotic_v2-v1/10000/FAC51CE1-4871-E511-B8E2-003048FFCC2C.root""",
            "crossSection" : 0.003194,
            "outputFile" : "file:/nfs_scratch/kdlong/DibosonGenAnalysisSamples/ZZTo4LNu0j_5f_NLO_FXFX/ggZZ2e2mu_MCFM_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        }
    }

    name = options.useDefaultDataset
    if name not in sample_info.keys():
        print "Invalid default datafile. Valid options are:"
        print options
        exit(0)
    return sample_info[name]
