import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('/eos/user/k/kelong/WZGenStudies/GENTEST_WZ_relaxed.root')
handle  = Handle ('std::vector<reco::GenParticle>')
label = ("genParticles")

ROOT.gROOT.SetStyle('Plain') # white background

hmqq = ROOT.TH1F("hmqq","m_{jj}",30,0,3000)   
hdeta = ROOT.TH1F("hdeta","#Delta#eta(j_{1}, j_{2})",30,0,12)   
heta  = ROOT.TH1F("heta","#eta(3l)",30,-6,6)
hpt = ROOT.TH1F("hpt","p_{T}(3l)",30,0,300)
hptq1 = ROOT.TH1F("hptq1","p_{T}(q_{1})",50,0,500)
hptq2 = ROOT.TH1F("hptq2","p_{T}(q_{2})",30,0,300)
hetaq1 = ROOT.TH1F("hetaq1","#eta(q_{1})",30,-6,6)
hetaq2 = ROOT.TH1F("hetaq2","#eta(q_{2})",30,-6,6)

hptlw = ROOT.TH1F("hptlw","p_{T}(l_{W})",30,0,600)
hptnw = ROOT.TH1F("hptnw","p_{T}(#nu)",30,0,600)
hptlzp = ROOT.TH1F("hptzp","p_{T}(l^{+}_{Z})",30,0,600)
hptlzm = ROOT.TH1F("hptzm","p_{T}(l^{-}_{Z})",30,0,600)

hetalw = ROOT.TH1F("hetalw","#eta(l^{-}_{W})",30,-6,6)
hetanw = ROOT.TH1F("hetanw","#eta(#nu))",30,-6,6)
hetalzp = ROOT.TH1F("hetazp","#eta(l^{+}_{Z})",30,-6,6)
hetalzm = ROOT.TH1F("hetazm","#eta(l^{-}_{Z})",30,-6,6)

hmz = ROOT.TH1F("hmz","m_{Z}",30,0,150)
hyz = ROOT.TH1F("hyz","#eta(Z)",30,-6,6)
hptz = ROOT.TH1F("hptz","p_{T}(Z)",30,0,600)

hmw = ROOT.TH1F("hmw","m_{W}",30,0,150)
hmwz = ROOT.TH1F("hmwz","m_{WZ}",50,0,1000)
hyw = ROOT.TH1F("hyw","y(W)",30,-6,6)
hptw = ROOT.TH1F("hptw","p_{T}(W)",30,0,600)
hmwq1 = ROOT.TH1F("hmwq1","m_{W+q1}",60,0,1800)
hmwq2 = ROOT.TH1F("hmwq2","m_{W+q2}",60,0,1800)

first = True
 
nPass = 0 
nEvents = 0 
for event in events:
    nEvents += 1

    event.getByLabel (label, handle)
    
    genps = handle.product()

    found=0
    nfound=0
    q1=ROOT.TLorentzVector(0.,0.,0.,0.)
    q2=ROOT.TLorentzVector(0.,0.,0.,0.)
    wl=ROOT.TLorentzVector(0.,0.,0.,0.)
    wn=ROOT.TLorentzVector(0.,0.,0.,0.)
    zp=ROOT.TLorentzVector(0.,0.,0.,0.)
    zm=ROOT.TLorentzVector(0.,0.,0.,0.)
    for genp in genps:
        if abs(genp.pdgId())==6:
            print "TOP EVENT!"
        if (genp.status()==1 and abs(genp.pdgId())<7):
            if found!=0 :
                q2.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                nfound=nfound+1
            else:
                q1.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                found=1
                nfound=nfound+1

        if (genp.status()==1 and genp.pdgId()==-11):
            wl.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        if (genp.status()==1 and genp.pdgId()==12):
            wn.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        if (genp.status()==1 and genp.pdgId()==13):
            zp.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        if (genp.status()==1 and genp.pdgId()==-13):
            zm.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        
    
    if nfound != 2:
        print "number of quarks !=2 ????"
        continue
    if abs(q1.Eta() - q2.Eta()) < 3.0: continue
    if (q1+q2).M() < 500.0: continue
    if (zp + zm).M() < 60: continue
    if wl.Perp() < 10: continue
    if zm.Perp() < 10: continue
    if zp.Perp() < 10: continue
    #if q1.Perp() < 30: continue
    #if q2.Perp() < 30: continue
    if abs(q1.Rapidity()) > 4.5: continue
    if abs(q2.Rapidity()) > 4.5: continue
    if abs(wl.Rapidity()) > 2.5: continue
    if abs(zm.Rapidity()) > 2.5: continue
    if abs(zp.Rapidity()) > 2.5: continue
    nPass +=1

    hptlw.Fill(wl.Perp())
    hetalw.Fill(wl.Eta())
    hptnw.Fill(wn.Perp())
    hetanw.Fill(wn.Eta())
    hptlzp.Fill(zp.Perp())
    hetalzp.Fill(zp.Eta())
    hptlzm.Fill(zm.Perp())
    hetalzm.Fill(zm.Eta())

    leadq = q1 if q1.Perp() > q2.Perp() else q2
    subleadq = q2 if q1.Perp() > q2.Perp() else q1
    hptq1.Fill(leadq.Perp())
    hptq2.Fill(subleadq.Pt())
    hetaq1.Fill(leadq.Eta())
    hetaq2.Fill(subleadq.Eta())
    hpt.Fill((wn+wl+zm+zp).Perp())
    heta.Fill((wn+wl+zm+zp).Eta())

    hmqq.Fill((q1+q2).M())
    hdeta.Fill(abs(q1.Eta() - q2.Eta()) )           

    hmw.Fill((wn+wl).M())
    hptw.Fill((wn+wl).Perp())
    hyw.Fill((wn+wl).Eta())

    hmz.Fill((zm+zp).M())
    hptz.Fill((zm+zp).Perp())
    hyz.Fill((zm+zp).Eta())
    hmwq1.Fill((wn+wl+leadq).M())
    hmwq2.Fill((wn+wl+subleadq).M())
    hmwz.Fill((wn+wl+zm+zp).M())
    
print "From %i total events" % nEvents
print "%i passed selection" % nPass
rfile = ROOT.TFile.Open("VBFNLOplots.root","RECREATE")

hmqq.Write()
heta.Write()
hdeta.Write()
hptq1.Write()
hptq2.Write()
hetaq1.Write()
hetaq2.Write()
hpt.Write()

hptlw.Write()
hptnw.Write()
hptlzp.Write()
hptlzm.Write()

hetalw.Write()
hetanw.Write()
hetalzp.Write()
hetalzm.Write()

hmz.Write()
hyz.Write()
hptz.Write()

hmw.Write()
hmwz.Write()
hyw.Write()
hptw.Write()

hmwq1.Write()
hmwq2.Write()

rfile.Close()

