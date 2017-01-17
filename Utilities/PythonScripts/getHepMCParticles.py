# coding: utf-8

from DataFormats.FWLite import Handle, Events
events = Events("/data/kelong/DibosonGenAnalysisSamples/WZJJ_VBFNLO/gentest_WZ-fixGen.root")
handle = Handle("edm::HepMCProduct")
genParticles = []
for i,event in enumerate(events):
    events.getByLabel("source", handle)
    hepMc = handle.product()
    evt = hepMc.GetEvent()
    it = evt.particles_begin()
    for i in range(evt.particles_size()):
        part = it.__deref__()
        it.__preinc__()
        if part.pdg_id() <= 5 and part.pdg_id() >= -5 and part.status() == 1:
            print "-"*20 + "Event " + str(i) + "-"*20
            print "pdgid == %i, status == %i, pt == %f, eta == %f" % (part.pdg_id(), part.status(), part.momentum().perp(), part.momentum().eta())
