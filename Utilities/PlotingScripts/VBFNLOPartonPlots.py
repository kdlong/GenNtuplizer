import ROOT
from DataFormats.FWLite import Events, Handle

events = Events ('/data/kelong/DibosonGenAnalysisSamples/WZJJ_VBFNLO/GENTEST_WZ_relaxed.root')
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
hmwq1 = ROOT.TH1F("hmwq1","hmwq1",60,0,1800)
hmwq2 = ROOT.TH1F("hmwq2","hmwq2",60,0,1800)

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
    nPass +=1
    
    hptlw.Fill(wl.Perp())
    hetalw.Fill(wl.Eta())
    hptnw.Fill(wn.Perp())
    hetanw.Fill(wn.Eta())
    hptlzp.Fill(zp.Perp())
    hetalzp.Fill(zp.Eta())
    hptlzm.Fill(zm.Perp())
    hetalzm.Fill(zm.Eta())
        

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
    hmwq1.Fill((wn+wl+q1).M())
    hmwq2.Fill((wn+wl+q2).M())

print "From %i total events" % nEvents
print "%i passed selection" % nPass
rfile = ROOT.TFile.Open("VBFNLOplots.root","RECREATE")

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

hmwq1.Write()
hmwq2.Write()

rfile.Close()

