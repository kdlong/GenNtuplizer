import ROOT
from DataFormats.FWLite import Events, Handle

file_names = [
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3630ED78-EAC9-E611-9C25-0CC47A4C8EA8.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C4C505E-DAC9-E611-81F3-0CC47A4D7628.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6918F82-EAC9-E611-8EB3-0CC47A4C8E66.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6AC4F85-DAC9-E611-A885-0CC47A4C8F06.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C4D37387-CEC9-E611-A61B-0CC47A78A440.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8815485-CEC9-E611-BBFE-0CC47A7C3610.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/088F80B8-FDC6-E611-AA43-484D7E8DF0AC.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/24D563C8-FDC6-E611-A803-001E67E71381.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/32B5B70D-FEC6-E611-BA5F-002590FD5A72.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4A7D818C-FDC6-E611-A230-0025905B857C.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4EDBE273-FDC6-E611-92FF-001E675A58D9.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/58C1355F-DAC5-E611-BF2E-24BE05C656A1.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/A4419616-A5C6-E611-87CD-24BE05CE1E31.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/BE36EBCE-E2C6-E611-AA0C-0CC47AA98B8C.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C47B06E5-B6C6-E611-92CA-001E674FB207.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/C65D73D4-FDC6-E611-BAF1-B083FED18596.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/D8E6F86D-FDC6-E611-B587-0025905B8582.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/E6C97442-D1C5-E611-8569-A0000420FE80.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/FC332C88-FDC6-E611-B86C-A0369F7FC714.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/610000/AE7B9A89-04CA-E611-A4E5-001E67A3FD26.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0889D9B1-53C5-E611-9056-B499BAABF37A.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/0A6FE368-F5C5-E611-9F7C-782BCB20E48C.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/16B9A01D-64C6-E611-9AC9-0025907D2502.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/1A95882D-64C6-E611-9437-0CC47A4C8F30.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/38FC1CB9-64C6-E611-8242-003048FFD7A4.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/4AAD347E-0CC5-E611-9245-001E67396DBA.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/5EE4810F-2DC6-E611-84C0-001CC4A6ABA8.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/96AC44E5-66C6-E611-9F40-0CC47AD98F74.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9ACF920A-50C5-E611-94DD-B499BAAC09C8.root',
    '/store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/9CF42702-64C6-E611-8148-A0369F7F9324.root',
]
files = [Events ('root://cms-xrd-global.cern.ch/%s' % x) for x in file_names]
handle  = Handle ('std::vector<reco::GenParticle>')
label = ("prunedGenParticles")

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
nTopEvents = 0 
nEvents = 0 
nSingleChan = 0 
nPass = 0 
for events in files:
    for event in events:
        nEvents += 1

        event.getByLabel (label, handle)
        
        genps = handle.product()

        found=0
        nfound=0
        q1=ROOT.TLorentzVector(0.,0.,0.,0.)
        q2=ROOT.TLorentzVector(0.,0.,0.,0.)
        bq=ROOT.TLorentzVector(0.,0.,0.,0.)
        wl=ROOT.TLorentzVector(0.,0.,0.,0.)
        wn=ROOT.TLorentzVector(0.,0.,0.,0.)
        zp=ROOT.TLorentzVector(0.,0.,0.,0.)
        zm=ROOT.TLorentzVector(0.,0.,0.,0.)
        topEvent=False
        toPrint = []
        for genp in genps:
            if genp.isHardProcess():
                toPrint += genp
            if (genp.isHardProcess() and abs(genp.pdgId())==6):
                #print "-"*20
                #for p in toPrint:
                    #print "pdg id is %f, pt is %f, mother %i" %( p.pdgId(), p.pt(), p.mother().pdgId())
                topEvent=True
                nTopEvents += 1
            #if topEvent and genp.isHardProcess():
                    #print "pdg id is %f, pt is %f, mother %i" %( genp.pdgId(), genp.pt(), genp.mother().pdgId())
            if (genp.isHardProcess() and abs(genp.pdgId())<6 and genp.pt() > 0.001):
                if abs(genp.pdgId()) == 5:
                    bq.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                if found!=0 :
                    q2.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                    nfound=nfound+1
        #            print "pdg id is %f, pt is %f" %( genp.pdgId(), genp.pt())
                else:
                    q1.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                    found=1
                    nfound=nfound+1
        #            print "pdg id is %f, pt is %f" %( genp.pdgId(), genp.pt())
            if (genp.isHardProcess() and genp.pdgId()==-11):
                wl.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
            if (genp.isHardProcess() and genp.pdgId()==12):
                wn.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
            if (genp.isHardProcess() and genp.pdgId()==13):
                zp.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
            if (genp.isHardProcess() and genp.pdgId()==-13):
                zm.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
    
        if nfound != 2:
            print "number of quarks !=2 ????"
            print "Number is ", nfound
            continue
        if wn.Perp() < 0.001 or zp.Perp() < 0.001 or zm.Perp() < 0.001 or wl.Perp() < 0.001:
            continue
        nSingleChan +=1
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

rfile = ROOT.TFile.Open("MGPartonPlots.root","RECREATE")
print "Found %i top events" % nTopEvents
print "From %i total events" % nEvents
print "%i in eem+ chan" % nSingleChan
print "%i passed selection" % nPass
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

