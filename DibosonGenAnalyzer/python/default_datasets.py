def getSampleInfo(options):
    sample_info = { 
        'MGLO-Phys14' : {
            "inputFiles" :
                """/store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/243769ED-4C6B-E411-A87D-000F530E4774.root
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/3AB77DFA-306B-E411-B601-000F530E4790.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/3EBD7BC1-526B-E411-BF6A-D4AE52E945A0.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/B63AEDB9-396B-E411-9695-0002C94CD0EC.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/F20317FD-306B-E411-80F0-0026B95CD6D9.root,
                /store/mc/Spring14miniaod/WZJetsTo3LNu_Tune4C_13TeV-madgraph-tauola/MINIAODSIM/141029_PU40bx50_PLS170_V6AN2-v1/20000/FCE80F2E-316B-E411-B867-AC853DA0692A.root""",
            "crossSection" : 1.634, 
            "outputFile" : "/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/WZ012j_LO_SUSY_PHYS14/MGLO_WZ012j_SUSYPhys14_pythia8_Ntuple.root",
            "isMiniAOD" : 1,
            "redoJets" : 1
        },
        'MGNLO-inc' : { "inputFiles" : "file:/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/MG5aMCatNLO_WZ0j_OfficialGridpack/MG5aMCatNLO_WZ0j_OfficialGridpack_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.246, 
            "outputFile" : "/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/MG5aMCatNLO_WZ0j_OfficialGridpack/MG5aMCatNLO_WZ0j_OfficialGridpack_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'MGNLO-01j' : { "inputFiles" : "file:/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/MG5aMCatNLO_WZ01j_OfficialGridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_pythia8_TuneCUETP8M1.root",
            "crossSection" : 5.300, 
            "outputFile" : "/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/MG5aMCatNLO_WZ01j_OfficialGridpack/MG5aMCatNLO_WZ01j_OfficialGridpack_pythia8_TuneCUETP8M1_Ntuple.root",
            "isMiniAOD" : 0
        },
        'MGLO-inc': { "inputFiles" : "file:/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/MGLO_WZ0j/MGLO_WZ0j_10E5ev_pythia8_MLM.root",
            "crossSection" : 1.333, 
            "outputFile" : "/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/MGLO_WZ0j/MGLO_WZ0j_10E5ev_pythia8_MLM_Ntuple.root",
            "isMiniAOD" : 0
        },
        'PWG-Off': {
            "inputFiles" : 
                """/store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/008E7FBF-9218-E511-81E0-001E675A5244.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0473AA1C-AE18-E511-A22A-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/0C4172B8-9218-E511-B9C9-001E675A58D9.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/1299A85E-9E18-E511-AE6C-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/20469B1E-9F18-E511-A402-0002C94CD12E.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/260EDE5C-9618-E511-9769-001517E74088.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/2653E331-AE18-E511-9446-0002C94D54CE.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/347C949C-9718-E511-ABFB-001E675A6C2A.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/348F76E6-9E18-E511-BDBA-0002C90B7F3C.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/3635C2B8-9218-E511-AF21-001E67A3EF70.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/36598113-9B18-E511-8E1E-001E675A6AB3.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/40CA9C13-9B18-E511-8042-001E675A6AB3.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/4226BF30-B218-E511-8072-001E67A400F0.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/44B40256-9618-E511-A24C-001E67A40523.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/56CC4156-9618-E511-978A-001E675A690A.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5CCAD500-A918-E511-9D7F-001E675A6D10.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/5E631894-9218-E511-BAFB-90B11C08CA45.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/665BA553-9618-E511-BCDC-001E67A401B3.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/66793415-9B18-E511-9F01-90B11C050395.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6A16B7D8-D618-E511-B9A8-90B11C06BDDA.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/6AD101BD-9218-E511-A127-90B11C0701C1.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/72E3871E-9B18-E511-8737-0026181D28F0.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7AE00CF3-9618-E511-9462-001517E74088.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7C75509A-9718-E511-BC88-001E67A3EAB1.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/7CDD84CD-AE18-E511-A3AA-A0040420FE80.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/88DDFA13-9B18-E511-8979-001E675A4759.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/8E4F6434-CA19-E511-A31A-0025905A60B8.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/906441C1-AE18-E511-865C-0002C94CD12E.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/9C466C9C-9718-E511-BCEF-001E675A6653.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A0630AC4-9218-E511-9396-90B11C0506C6.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A2FE9D53-9618-E511-96D0-001E67583BE0.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/A4E6745B-9618-E511-9245-90B11C050429.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/AC716F3E-CA19-E511-95C6-0025905B855E.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B000DE1E-3E19-E511-B439-001E673974EA.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B0187C3B-B218-E511-BB6F-001517E7410C.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/B61B81F3-9618-E511-B184-001E675A58D9.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/C05F5D30-B218-E511-941B-0002C94D54CE.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/D88CD7B8-9218-E511-AD96-001E67A3FBAA.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/DA59AFB7-9218-E511-964D-001E675A68BF.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EAD9F3BA-9218-E511-997B-001E675A68C4.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/EE054C19-9318-E511-8DA3-001E675A68C4.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F031E722-9318-E511-B114-001E67A406E0.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F2451D5B-9618-E511-81E2-001517E741C8.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F26D92CC-9B18-E511-922E-001E675A6D10.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F2FAFEB8-9218-E511-A27E-001E67A40523.root,
                /store/mc/RunIISpring15DR74/WZTo3LNu_TuneCUETP8M1_13TeV-powheg-pythia8/MINIAODSIM/Asympt25ns_MCRUN2_74_V9-v1/60000/F8BB8C56-9618-E511-B715-001E67A3EAB1.root""",
            "crossSection" : 4.428, 
            "outputFile" : "/afs/cern.ch/work/k/kelong/WZ_MCAnalysis/POWHEG_WZ/WZ_powheg_pythia8_CUETP8M1_officialSample_Ntuple.root",
            "isMiniAOD" : 1
        }
    }
    name = options.useDefaultDataset
    if name not in sample_info.keys():
        print "Invalid default datafile. Valid options are:"
        print options
        exit(0)
    return sample_info[name]
