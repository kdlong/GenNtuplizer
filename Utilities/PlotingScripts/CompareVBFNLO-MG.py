import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('GENTEST_WZ_relaxed.root')
handle  = Handle ('std::vector<reco::GenParticle>')
label = ("genParticles")

ROOT.gROOT.SetStyle('Plain') # white background


hmqq = ROOT.TH1F("hmqq","hmqq",30,0,3000)   
hdeta = ROOT.TH1F("hdeta","hdeta",30,0,12)   
heta  = ROOT.TH1F("heta","heta",30,-6,6)
hpt = ROOT.TH1F("hpt","hpt",30,0,300)

hptlw = ROOT.TH1F("hptlw","hptlw",30,0,600)
hptnw = ROOT.TH1F("hptnw","hptnw",30,0,600)
hptlzp = ROOT.TH1F("hptzp","hptzp",30,0,600)
hptlzm = ROOT.TH1F("hptzm","hptzm",30,0,600)

hetalw = ROOT.TH1F("hetalw","hetalw",30,-6,6)
hetanw = ROOT.TH1F("hetanw","hetanw",30,-6,6)
hetalzp = ROOT.TH1F("hetazp","hetazp",30,-6,6)
hetalzm = ROOT.TH1F("hetazm","hetazm",30,-6,6)

hmz = ROOT.TH1F("hmz","hmz",30,0,150)
hyz = ROOT.TH1F("hyz","hyz",30,-6,6)
hptz = ROOT.TH1F("hptz","hptz",30,0,600)

hmw = ROOT.TH1F("hmw","hmw",30,0,150)
hyw = ROOT.TH1F("hyw","hyw",30,-6,6)
hptw = ROOT.TH1F("hptw","hptw",30,0,600)


first = True
 
for event in events:

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
            hptlw.Fill(genp.pt())
            hetalw.Fill(genp.eta())
        if (genp.status()==1 and genp.pdgId()==12):
            wn.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
            hptnw.Fill(genp.pt())
            hetanw.Fill(genp.eta())
        if (genp.status()==1 and genp.pdgId()==13):
            zp.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
            hptlzp.Fill(genp.pt())
            hetalzp.Fill(genp.eta())
        if (genp.status()==1 and genp.pdgId()==-13):
            zm.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
            hptlzm.Fill(genp.pt())
            hetalzm.Fill(genp.eta())
        
    
    if nfound != 2:
        print "number of quarks !=2 ????"
        continue

    hpt.Fill(q1.Perp())
    hpt.Fill(q2.Perp())

    hmqq.Fill((q1+q2).M())
    heta.Fill(q1.Eta())
    heta.Fill(q2.Eta())
    hdeta.Fill(abs(q1.Eta() - q2.Eta()) )           

    hmw.Fill((wn+wl).M())
    hptw.Fill((wn+wl).Perp())
    hyw.Fill((wn+wl).Rapidity())

    hmz.Fill((zm+zp).M())
    hptz.Fill((zm+zp).Perp())
    hyz.Fill((zm+zp).Rapidity())


rfile = ROOT.TFile.Open("plots.root","RECREATE")

hmqq.Write()
heta.Write()
hdeta.Write()
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
hyw.Write()
hptw.Write()

rfile.Close()

