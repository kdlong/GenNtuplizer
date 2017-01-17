# coding: utf-8

from DataFormats.FWLite import Handle, Events
events = Events("root://cmsxrootd.hep.wisc.edu//store/user/kelong/ZZTo4L_PDF4LHC_13TeV-powheg-pythia8_2017-01-14-fixGen_cfg/fixGen_cfg-HIG-RunIISummer15wmLHEGS-00441_993.root")
handle = Handle("std::vector<reco::GenParticle>")
genParticles = []
nEvents = 0
j=0
for i,event in enumerate(events):
    events.getByLabel("genParticles", handle)
    genParticles = handle.product()
    nEvents +=1
    tauEvent = False
    for part in genParticles:
        if part.isHardProcess() and abs(part.pdgId()) == 15:
            tauEvent = True
            continue
    if not tauEvent:
        j += 1
print "Processed %i events" % nEvents
print "%i had no hard process taus" % j
