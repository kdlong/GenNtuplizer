from DataFormats.FWLite import Handle, Events
#events = Events("SMP-RunIISummer15wmLHEGS-00053.root")
#events = Events("root://cmsxrootd.fnal.gov///store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_aQGC-FM_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/027561E3-42BE-E611-AB10-001E674DA83D.root")
#events = Events("root://cmsxrootd.fnal.gov///store/mc/RunIISummer16MiniAODv2/WZTo3LNu_PtZ-0To200_aTGC_13TeV-amcatnloFXFX-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/60000/149AD667-A3D7-E611-BEBE-02163E019E5A.root")
#events = Events("root://cmsxrootd.hep.wisc.edu//store/user/kelong/ZZTo4L_PDF4LHC_13TeV-powheg-pythia8_2017-01-14-fixGen_cfg/fixGen_cfg-HIG-RunIISummer15wmLHEGS-00441_993.root")
#events = Events("/afs/cern.ch/user/k/kelong/work/MCContactTests/ZZPowheg/HIG-RunIISummer15wmLHEGS-00441.root")
#events = Events("root://cmsxrootd.fnal.gov///store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_aQGC-FT_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/0885923A-6AC6-E611-8CB7-842B2B42BB8E.root")
events = Events("root://cmsxrootd.fnal.gov///store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_aQGC-FS_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/00AEA2AB-82C5-E611-9920-0CC47A706D40.root")
handle = Handle("LHEEventProduct")
for e in events:
    e.getByLabel("externalLHEProducer", handle)
    prod = handle.product()
    for i,weight in enumerate(prod.weights()):
        print "index %i, index - 8: %i, ID: %s" % (i, i-8, weight.id)
        print "Weight: %f" % weight.wgt
    break
