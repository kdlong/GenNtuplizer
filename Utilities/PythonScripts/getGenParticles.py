# coding: utf-8

from DataFormats.FWLite import Handle, Events
events = Events("/data/kelong/DibosonGenAnalysisSamples/WZJJ_VBFNLO/gentest_WZ-fixGen.root")
handle = Handle("std::vector<reco::GenParticle>")
genParticles = []
for i,event in enumerate(events):
    events.getByLabel("genParticles", handle)
    genParticles = handle.product()
    j=0
    print "-"*20 + ("Event %i" % i) + "-"*20
    for part in genParticles:
        if part.isHardProcess() and part.pdgId() <= 5 and part.pdgId() >= -5:
        #if part.status() == 1 and part.pdgId() <= 5 and part.pdgId() >= -5:
            j += 1
            print "ME level parton %i in event %i" % (j, i)
            print " --> pdgId() == %i, pt == %f, eta == %f" % (part.pdgId(), part.pt(), part.eta())
