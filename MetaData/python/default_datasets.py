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
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/WZ012j_LO_SUSY_PHYS14/MGLO_WZ012j_SUSYPhys14_pythia8_Ntuple.root",
            "isMiniAOD" : 1,
            "redoJets" : 1
        },
        'WZto2L2Q-PWG': {
            "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZto2L2Q/WZto2L2Q_powheg_pythia8_CUETP8M1.root",
            "crossSection" : 6.789, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZto2L2Q/WZto2L2Q_powheg_pythia8_CUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZto2L2Q-MGNLO-Off' : { "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/00456448-0734-E511-BABA-002618943982.root,
                /store/mc/RunIISpring15DR74/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/04BFCB9E-E82F-E511-A94B-00A0D1EE8AF0.root,
                /store/mc/RunIISpring15DR74/WZTo2L2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v2/20000/04DC406D-9531-E511-9B30-001E6739702B.root""",
            "crossSection" : 5.593, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto2L2Q_Official/MG5aMCatNLO_WZTo2L2Q_Official_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'WZto1L1Nu2Q-MGNLO-Off' : { "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/00949148-3813-E511-BEA1-F45214938690.root,
                /store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/063EC4F5-3413-E511-88BB-00259059642A.root,
                /store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0857B822-3513-E511-AC33-002590596490.root,
                /store/mc/RunIISpring15DR74/WZTo1L1Nu2Q_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/00000/0A553E15-3513-E511-898C-0025905A613C.root""",
            "crossSection" : 10.71, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto1L1Nu2Q_Official/MG5aMCatNLO_WZTo1L1Nu2Q_Official_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
        },
        'WZto1L3Nu-MGNLO-Off' : { "inputFiles" : 
            """/store/mc/RunIISpring15DR74/WZTo1L3Nu_13TeV_amcatnloFXFX_madspin_pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/40000/640F0CA0-5841-E511-92B5-B083FECF83AB.root""",
            "crossSection" : 3.06, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto1L3Nu_Official/test.root",
            "isMiniAOD" : 1
        },
        'WZto2L2Q-MGNLO-inc' : { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto2L2Q_Incl/MG5aMCatNLO_WZto2L2Q_Incl_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.493, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZto2L2Q_Incl/MG5aMCatNLO_WZto2L2Q_Incl_pythia8_TuneCUETP8M1_Ntuple.root",  
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-inc' : { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j/MG5aMCatNLO_WZ0j_pythia8_TuneCUETP8M1.root",
            "crossSection" : 4.415, 
            "outputFile" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j/MG5aMCatNLO_WZ0j_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-inc-ERROR' : { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j_OfficialGridpack/MG5aMCatNLO_WZ0j_OfficialGridpack_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.246, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ0j_OfficialGridpack/MG5aMCatNLO_WZ0j_OfficialGridpack_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-01j' : { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialGridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.300, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialGridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGLO-inc': { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MGLO_WZ0j/MGLO_WZ0j_10E5ev_pythia8_MLM.root",
            "crossSection" : 1.333, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MGLO_WZ0j/MGLO_WZ0j_10E5ev_pythia8_MLM_Ntuple.root",
            "isMiniAOD" : 0
        },
        'WZ-MGNLO-Off' : {
            "inputFiles" :
                """/store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/002CAF8C-3A26-E511-B14A-0025905A607E.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/00CA6490-0C2F-E511-9A70-001E67398D72.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/00F5EF70-3326-E511-8AFF-0025905A6066.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/06F9B6E2-A629-E511-B9E2-B083FED76637.root,
                /store/mc/RunIISpring15DR74/WZJets_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/Asympt50ns_MCRUN2_74_V9A-v1/30000/0A80F6F9-2D2A-E511-88E0-008CFA1111E0.root""",
            "crossSection" : 5.289, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_WZ01j_OfficialSample/MG5aMCatNLO_WZ01j_OfficialSample_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 1
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
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_WZ/WZ_powheg_pythia8_CUETP8M1_officialSample_Ntuple.root",
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
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_ZZ01j_OfficialSample/MG5aMCatNLO_ZZ01j_OfficialSample_pythia8_TuneCUETP8M1_Ntuple.root",
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
        'WW-PWG-Off': {
            "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/082EF100-DC05-E511-AD3F-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/1A158D26-E005-E511-BD80-00074305CDC0.root,
                /store/mc/RunIISpring15DR74/WWTo2L2Nu_13TeV-powheg/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/50000/22314C20-7A07-E511-989B-A0040420FE80.root""",
            "crossSection" : 10.481, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/POWHEG_WW/test.root",
            "isMiniAOD" : 1,
            "hardProcess" : 0
        },
        'ZZ-MGNLO-inc' : { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/ZZTo4LNu0j_5f_NLO_FXFX/MG5aMCatNLO_ZZTo4LNu0j_muMass_pythia8_TuneCUETP8M1.root",
            "crossSection" : 1.181, 
            "outputFile" : "file:/data/kelong/DibosonGenAnalysisSamples/ZZTo4LNu0j_5f_NLO_FXFX/MG5aMCatNLO_ZZTo4LNu0j_muMass_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'ZZ-MGNLO-Off-mumass' : { "inputFiles" : "file:/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_ZZ01j_OfficialSample/MG5aMCatNLO_ZZ01j_OfficialSample_mumass_pythia8_TuneCUETP8M1.root",
            "crossSection" : 1.208, 
            "outputFile" : "/data/kelong/DibosonGenAnalysisSamples/MG5aMCatNLO_ZZ01j_OfficialSample/MG5aMCatNLO_ZZ01j_OfficialSample_mumass_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        }
    }

    name = options.useDefaultDataset
    if name not in sample_info.keys():
        print "Invalid default datafile. Valid options are:"
        print options
        exit(0)
    return sample_info[name]
