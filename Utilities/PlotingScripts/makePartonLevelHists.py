import ROOT
import math
from DataFormats.FWLite import Events, Handle

def getHepMCParticles(event):
    handle  = Handle ('std::vector<reco::GenParticle>')
    label = ("genParticles")
    event.getByLabel (label, handle)
    
    genps = handle.product()

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
            if nfound!=0 :
                q2.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                nfound=nfound+1
            else:
                q1.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
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
        raise RuntimeError("Number of quarks != 2! Found "+nfound)
    return zp,zm,wl,wn,q1,q2

def getLHEParticles(event):
    lheHandle = Handle('LHEEventProduct')
    label = 'source' if "MiniAOD" not in file_names else "externalLHEProducer"
    event.getByLabel(label, lheHandle)
    lhe = lheHandle.product()

    lheParticles = lhe.hepeup()

    nfound=0
    q1=ROOT.TLorentzVector(0.,0.,0.,0.)
    q2=ROOT.TLorentzVector(0.,0.,0.,0.)
    bq=ROOT.TLorentzVector(0.,0.,0.,0.)
    wl=ROOT.TLorentzVector(0.,0.,0.,0.)
    wn=ROOT.TLorentzVector(0.,0.,0.,0.)
    zp=ROOT.TLorentzVector(0.,0.,0.,0.)
    zm=ROOT.TLorentzVector(0.,0.,0.,0.)
    for i in range(lheParticles.NUP):
        p4 = lhep4(i, lheParticles)
        if abs(lheParticles.IDUP[i]) == 6:
            nTopEvents += 1
        if (abs(lheParticles.IDUP[i])<6 and i > 1):
            if abs(lheParticles.IDUP[i]) == 5:
                bq =lhep4(i, lheParticles)
            if nfound!=0 :
                q2 =lhep4(i, lheParticles)
                nfound=nfound+1
            else:
                q1 =lhep4(i, lheParticles)
                nfound=nfound+1
        if (lheParticles.IDUP[i]==-11):
            wl = lhep4(i, lheParticles)
        if (lheParticles.IDUP[i]==12):
            wn = lhep4(i, lheParticles)
        if (lheParticles.IDUP[i]==13):
            zp = lhep4(i, lheParticles)
        if (lheParticles.IDUP[i]==-13):
            zm = lhep4(i, lheParticles)
    if nfound != 2:
        raise RuntimeError("Number of quarks != 2! Found "+nfound)
    return zp,zm,wl,wn,q1,q2

def dR(p1, p2):
    return math.sqrt((p1.PseudoRapidity()-p2.PseudoRapidity())**2 + (p1.Phi()-p2.Phi())**2) 

def lhep4(i, lheParticles):
    px = lheParticles.PUP.at(i)[0]
    py = lheParticles.PUP.at(i)[1]
    pz = lheParticles.PUP.at(i)[2]
    pE = lheParticles.PUP.at(i)[3]
    return lorentz(px, py, pz, pE)

fromLHE = True
file_names = [ "/eos/user/k/kelong/WZGenStudies/WZJJ_VBFNLO_fromauthors/lhelevel/WZJJ_VBFNLO_fromauthors.root" ]
output_file = "VBFNLO-fromauthors-ptj30.root"
#output_file = "MGPartonPlots-nobquarks-ptj30.root"
#file_names = [
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev0_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev10000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev20000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev30000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev40000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev50000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev60000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev70000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev80000_numEvent10000.root",
#    "/eos/user/k/kelong/WZGenStudies/WZJJ_noBquarks/WZJJTo1E1Nu2MuJJ_noBquarks-madgraph-pythia8_ev90000_numEvent10000.root",
#]
#file_names = [
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/3630ED78-EAC9-E611-9C25-0CC47A4C8EA8.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/8C4C505E-DAC9-E611-81F3-0CC47A4D7628.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6918F82-EAC9-E611-8EB3-0CC47A4C8E66.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/A6AC4F85-DAC9-E611-A885-0CC47A4C8F06.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/C4D37387-CEC9-E611-A61B-0CC47A78A440.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/D8815485-CEC9-E611-BBFE-0CC47A7C3610.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/088F80B8-FDC6-E611-AA43-484D7E8DF0AC.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/24D563C8-FDC6-E611-A803-001E67E71381.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/32B5B70D-FEC6-E611-BA5F-002590FD5A72.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/50000/4A7D818C-FDC6-E611-A230-0025905B857C.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/70000/EC38D34B-0DC6-E611-A610-D067E5F90F2A.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/146CDD40-C7C5-E611-98B7-001E67DDBFC5.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/2A78F7A3-87C5-E611-8996-0242AC130002.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/2C706EBE-00C6-E611-8DBC-0025905A60DE.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/3E3CF09B-2CC6-E611-8B4A-0025905A60DA.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4C2E1A37-49C6-E611-AAE6-B083FED177B1.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/4E9A26AD-EFC5-E611-ADE0-0CC47AD991FA.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/5E94E7F5-54C5-E611-A659-24BE05CE3C91.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/947B138D-14C6-E611-9E71-0CC47A7C35C8.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/9872AB08-88C6-E611-87D8-0CC47A4D766C.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/9E6893D6-5DC6-E611-B1A3-002590D9D980.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C27E1FD3-C8C5-E611-8E3C-0CC47A4D7692.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/C4F44187-88C6-E611-8450-001E67A406E0.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/E4BE1945-40C6-E611-A86C-00259073E4DA.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/EA51B8A9-7CC5-E611-8719-6C3BE5B5A308.root",
#    "root://cms-xrd-global.cern.ch//store/mc/RunIISummer16MiniAODv2/WLLJJ_WToLNu_EWK_TuneCUETP8M1_13TeV_madgraph-madspin-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/90000/F892C761-4CC6-E611-8C29-6C3BE5B5B108.root",
#]
files = [Events (x) for x in file_names]
lorentz = ROOT.TLorentzVector
#label = 'externalLHEProducer'

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
nTopEvents = 0 
nEvents = 0 
nSingleChan = 0 
nPass = 0 
for events in files:
    for iev, event in enumerate(events):
        nEvents += 1

        if fromLHE:
            zp,zm,wl,wn,q1,q2 = getLHEParticles(event)
        else:
            zp,zm,wl,wn,q1,q2 = getHepMCParticles(event)
        if wn.Perp() < 0.001 or zp.Perp() < 0.001 or zm.Perp() < 0.001 or wl.Perp() < 0.001:
            continue
        nSingleChan +=1
        evPass = True
        log = ""
        if abs(q1.Eta() - q2.Eta()) < 3.0: 
            log += "Failed dEtajj cut\n"
            log += "dEtajj was %0.1f \n" % abs(q1.Eta() - q2.Eta())
            evPass = False
        if (q1+q2).M() < 500.0: 
            log += "Failed mjj cut\n"
            evPass = False
        if (zp + zm).M() < 76 or (zp + zm).M():
            log += "Failed mZ cut\n"
            evPass = False
        if wl.Perp() < 20:
            log += "Failed pT(lw) cut\n"
            evPass = False
        if zm.Perp() < 20:
            log += "Failed pT(lZ-) cut\n"
            evPass = False
        if zp.Perp() < 20: 
            log += "Failed pT(lZ+) cut\n"
            evPass = False
        if q1.Perp() < 30: 
            evPass = False
            log += "Failed q1 pT cut\n"
        if q2.Perp() < 30: 
            evPass = False
            log += "Failed q2 pT cut\n"
        if abs(q1.Rapidity()) > 4.5:
            log += "Failed pT(j1) cut\n"
            evPass = False
        if abs(q2.Rapidity()) > 4.5:
            log += "Failed pT(j2) cut\n"
            evPass = False
        if abs(wl.Rapidity()) > 2.5:
            log += "Failed y(lw) cut\n"
            evPass = False
        if abs(zm.Rapidity()) > 2.5:
            log += "Failed y(lz-) cut\n"
            evPass = False
        if abs(zp.Rapidity()) > 2.5:
            log += "Failed y(lz+) cut\n"
            evPass = False
        if dR(zm,q1) < 0.1 or dR(zm,q2) < 0.1 or dR(zp, q1) > 0.1 or dR(zp, q2) > 0.1 or dR(wl, q1) > 0.1 or dR(wl, q2) > 0.1:
            log += "Failed dR(l, j) cut\n"
        if not evPass:
            print "-"*80
            print log
            continue
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

#rfile = ROOT.TFile.Open("MGPartonPlots-OfficialSample-ptj30.root","RECREATE")
rfile = ROOT.TFile.Open(output_file,"RECREATE")
print "Found %i top events" % nTopEvents
print "From %i total events" % nEvents
print "%i in eem+ chan" % nSingleChan
print "%i passed selection" % nPass
hmqq.Write()
heta.Write()
hdeta.Write()
hpt.Write()
hptq1.Write()
hptq2.Write()
hetaq1.Write()
hetaq2.Write()

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

