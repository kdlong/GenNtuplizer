import ROOT
import math
import glob
from DataFormats.FWLite import Events, Handle

nTopEvents = 0 
nTopEventsPassed = 0 
def getHepMCParticles(event):
    handle  = Handle ('std::vector<reco::GenParticle>')
    label = ("genParticles")
    event.getByLabel (label, handle)
    
    genps = handle.product()

    geninfo = Handle("GenEventInfoProduct")
    event.getByLabel ("generator", geninfo)
    weight = geninfo.product().weights()[0]
    nfound=0
    q1=ROOT.TLorentzVector(0.,0.,0.,0.)
    q2=ROOT.TLorentzVector(0.,0.,0.,0.)
    wl=ROOT.TLorentzVector(0.,0.,0.,0.)
    wn=ROOT.TLorentzVector(0.,0.,0.,0.)
    zp=ROOT.TLorentzVector(0.,0.,0.,0.)
    zm=ROOT.TLorentzVector(0.,0.,0.,0.)
    topEvent = False
    for genp in genps:
        if abs(genp.pdgId())==6:
            topEvent = True
        if (genp.status()==1 and abs(genp.pdgId())<7):
            if nfound!=0 :
                q2.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                nfound=nfound+1
            else:
                q1.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
                nfound=nfound+1

        wlep = [11, -11]
        wnu = [12, -12]
        if restrictChan == "wp":
            wlep = [-11]
            wnu = [12]
        elif restrictChan == "wm":
            wlep =[ 11]
            wnu = [-12]
        if (genp.status()==1 and genp.pdgId() in wlep):
            wl.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        if (genp.status()==1 and genp.pdgId() in wnu):
            wn.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        if (genp.status()==1 and genp.pdgId()==13):
            zp.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
        if (genp.status()==1 and genp.pdgId()==-13):
            zm.SetPxPyPzE(genp.px(),genp.py(),genp.pz(),genp.energy())
    
    if nfound != 2:
        raise RuntimeError("Number of quarks != 2! Found "+nfound)
    return zp,zm,wl,wn,q1,q2,topEvent,weight

def getLHEParticles(event):
    lheHandle = Handle('LHEEventProduct')
    #label = 'source' if "MiniAOD" not in file_names[0] else "externalLHEProducer"
    #label = "externalLHEProducer"
    label = "source"
    event.getByLabel(label, lheHandle)
    lhe = lheHandle.product()

    lheParticles = lhe.hepeup()

    nfound=0
    isTopEvent = False
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
            isTopEvent = True
        if (abs(lheParticles.IDUP[i])<6 and i > 1):
            if abs(lheParticles.IDUP[i]) == 5:
                bq =lhep4(i, lheParticles)
                print "Found a b quark!"
                isTopEvent=True
            if nfound!=0 :
                q2 =lhep4(i, lheParticles)
                nfound=nfound+1
            else:
                q1 =lhep4(i, lheParticles)
                nfound=nfound+1
        wlep = [11, -11]
        wnu = [12, -12]
        if restrictChan == "wp":
            wlep = [-11]
            wnu = [12]
        elif restrictChan == "wm":
            wlep =[ 11]
            wnu = [-12]
        if (lheParticles.IDUP[i] in wlep):
            wl = lhep4(i, lheParticles)
        if (lheParticles.IDUP[i] in wnu):
            wn = lhep4(i, lheParticles)
        if (lheParticles.IDUP[i]==13):
            zp = lhep4(i, lheParticles)
        if (lheParticles.IDUP[i]==-13):
            zm = lhep4(i, lheParticles)

    # Check other Z definition
    if (wn.Pt() < 0.001 and False):
        wl=ROOT.TLorentzVector(0.,0.,0.,0.)
        for i in range(lheParticles.NUP):
            p4 = lhep4(i, lheParticles)
            wlep = [13, -13]
            wnu = [14, -14]
            if restrictChan == "wp":
                wlep = [-13]
                wnu = [14]
            elif restrictChan == "wm":
                wlep =[ 13]
                wnu = [-14]
            if (lheParticles.IDUP[i] in wnu):
                wn = lhep4(i, lheParticles)
            if (lheParticles.IDUP[i] in wlep):
                wl = lhep4(i, lheParticles)
            if (lheParticles.IDUP[i]==11):
                zp = lhep4(i, lheParticles)
            if (lheParticles.IDUP[i]==-11):
                zm = lhep4(i, lheParticles)

    if nfound != 2:
        raise RuntimeError("Number of quarks != 2! Found "+nfound)
    return zp,zm,wl,wn,q1,q2,isTopEvent,lheParticles.XWGTUP

def dR(p1, p2):
    return math.sqrt((p1.PseudoRapidity()-p2.PseudoRapidity())**2 + (p1.Phi()-p2.Phi())**2) 

def lhep4(i, lheParticles):
    px = lheParticles.PUP.at(i)[0]
    py = lheParticles.PUP.at(i)[1]
    pz = lheParticles.PUP.at(i)[2]
    pE = lheParticles.PUP.at(i)[3]
    return lorentz(px, py, pz, pE)

fromLHE = True
#fromLHE = False 
restrictChan = "wp"
#file_names = [ "/eos/user/k/kelong/WZGenStudies/WZJJ_VBFNLO_fromauthors/lhelevel/WZJJ_VBFNLO_fromauthors.root" ]
path = ""
if restrictChan == "wm":
    path = "/eos/user/k/kelong/LesHouchesVBSstudy/WmZ_VBFNLO/" 
elif restrictChan == "wp":
    path = "/eos/user/k/kelong/LesHouchesVBSstudy/WpZ_VBFNLO/" 
#dyn
path = "/eos/user/k/kelong/LesHouchesVBSstudy/WmZ_VBFNLO/MaxPtJScale/"
output_file = "VBFNLOHists/VBFNLO-fromauthors_maxPtJ.root"
file_names = glob.glob(path + "*")
#output_file = "VBFNLOHists/VBFNLO-fromauthors-ptj30.root"
#import subprocess
#file_names = subprocess.check_output(["dasgoclient", '--query', 
#    "file dataset=/WZJJToENu2MuJJ_EWK_LHConfig_FixedMW_AllCuts_13TeV-madgraph-pythia8/kelong-RunIISummer15wmLHEGS_RAWSIMoutput-ee1553652ca86b53d96b9f25026a7c7d/USER instance=prod/phys03"]).split()
##    "file dataset=/WZJJToENu2MuJJ_EWK_LHConfig_13TeV-madgraph-pythia8/kelong-RunIISummer15wmLHEGS_LHEoutput-d2e0e496a649ec0c95f66a2596eade31/USER instance=prod/phys03"]).split()
#file_names = ["/eos/cms/" + f for f in file_names[:800]] 
#output_file = "MGHists/MGPartonPlots-mathieusSetup_AllCuts.root"
#file_names = [ "/eos/user/k/kelong/LesHouchesVBSstudy/MadGraph/MathieusConfiguration/EDM/WZTo1E1Nu2Mu_MathieusSetup_looseCuts_madgraph_HepMC.root" ]
#file_names = [ "/eos/user/k/kelong/LesHouchesVBSstudy/MadGraph/MathieusConfiguration/EDM/WpZTo1E1Nu2Mu_MathieusSetup_noetajj_madgraph_EDM.root" ]
#output_file = "MGPartonPlots-mathieusSetup.root"
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
#output_file = "MGPartonPlots-nobquarks-ptj30.root"
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
#output_file = "MGPartonPlots-ptj30.root"
#file_names = ["/data/kelong/DibosonGenAnalysisSamples/VBFNLO_fromMatthias/testWZ.root"]
#output_file = "newVFNLO.root"
restrictChan = "wp"
file_names = ["/hdfs/store/user/dteague/delphes_WZ_YR/EDM_WZ_EWK/lhe.root"]
output_file = "WpZJJ_14TeV_fromDylan.root"
files = [Events (x) for x in file_names]
lorentz = ROOT.TLorentzVector

ROOT.gROOT.SetStyle('Plain') # white background


hmqq = ROOT.TH1F("hmqq","m_{jj}",325,20,13020)   
#hmqq = ROOT.TH1F("hmqq","m_{jj}",313,500,13020)   
hdeta = ROOT.TH1F("hdeta","#Delta#eta(j_{1}, j_{2})",25,2.5,8.75)   
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
nEvents = 0 
nSingleChan = 0 
nPass = 0 
sumWeights = 0 
for events in files:
    for iev, event in enumerate(events):
        nEvents += 1

        weight = 1
        if fromLHE:
            zp,zm,wl,wn,q1,q2,isTop,weight = getLHEParticles(event)
        else:
            zp,zm,wl,wn,q1,q2,isTop,weight = getHepMCParticles(event)
        sumWeights += weight
        if wn.Perp() < 0.001 or zp.Perp() < 0.001 or zm.Perp() < 0.001 or wl.Perp() < 0.001:
            continue
        nSingleChan +=1
        evPass = True
        if isTop:
            nTopEvents+=1
        log = ""
        if abs(q1.Eta() - q2.Eta()) < 2.5: 
            log += "Failed dEtajj cut\n"
            log += "dEtajj was %0.1f \n" % abs(q1.Eta() - q2.Eta())
            evPass = False
        if q1.Eta()*q2.Eta() > 0: 
            log += "Failed eta sign cut\n"
            #evPass = False
        if (q1+q2).M() < 500: 
            log += "Failed dijet mass cut\n"
            evPass = False
        #if (zp + zm).M() > 106.1876 or (zp + zm).M() < 76.1876:
        if (zp + zm).M() > 106 or (zp + zm).M() < 76:
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
        if abs(q1.PseudoRapidity()) > 4.7:
            log += "Failed pT(j1) cut\n"
            evPass = False
        if abs(q2.PseudoRapidity()) > 4.7:
            log += "Failed pT(j2) cut\n"
            evPass = False
        if abs(wl.PseudoRapidity()) > 2.5:
            log += "Failed y(lw) cut\n"
            evPass = False
        if abs(zm.PseudoRapidity()) > 2.5:
            log += "Failed y(lz-) cut\n"
            evPass = False
        if abs(zp.PseudoRapidity()) > 2.5:
            log += "Failed y(lz+) cut\n"
            evPass = False
        if dR(zm,q1) < 0.4 or dR(zm,q2) < 0.4 or dR(zp, q1) < 0.4 or dR(zp, q2) < 0.4 or dR(wl, q1) < 0.4 or dR(wl, q2) < 0.4:
            log += "Failed dR(l, j) cut\n"
            evPass = False
        if dR(q1,q2) < 0.4:
            log += "Failed dR(j1, j2) cut (but accepted anyway)\n"
        #    evPass = False
        if not evPass:
            print "-"*80
            print log
            continue
        nPass +=1
        if isTop:
            nTopEventsPassed+=1
            evPass=False
        
        hptlw.Fill(wl.Perp(), weight)
        hetalw.Fill(wl.Eta(), weight)
        hptnw.Fill(wn.Perp(), weight)
        hetanw.Fill(wn.Eta(), weight)
        hptlzp.Fill(zp.Perp(), weight)
        hetalzp.Fill(zp.Eta(), weight)
        hptlzm.Fill(zm.Perp(), weight)
        hetalzm.Fill(zm.Eta(), weight)

        leadq = q1 if q1.Perp() > q2.Perp() else q2
        subleadq = q2 if q1.Perp() > q2.Perp() else q1
        hptq1.Fill(leadq.Perp(), weight)
        hptq2.Fill(subleadq.Pt(), weight)
        hetaq1.Fill(leadq.Eta(), weight)
        hetaq2.Fill(subleadq.Eta(), weight)
        hpt.Fill((wn+wl+zm+zp).Perp(), weight)
        heta.Fill((wn+wl+zm+zp).Eta(), weight)

        hmqq.Fill((q1+q2).M(), weight)
        hdeta.Fill(abs(q1.Eta() - q2.Eta()) , weight)           

        hmw.Fill((wn+wl).M(), weight)
        hptw.Fill((wn+wl).Perp(), weight)
        hyw.Fill((wn+wl).Eta(), weight)

        hmz.Fill((zm+zp).M(), weight)
        hptz.Fill((zm+zp).Perp(), weight)
        hyz.Fill((zm+zp).Eta(), weight)
        hmwq1.Fill((wn+wl+leadq).M(), weight)
        hmwq2.Fill((wn+wl+subleadq).M(), weight)
        hmwz.Fill((wn+wl+zm+zp).M(), weight)

if restrictChan == "wp":
    output_file = output_file.replace(".root", "_wponly.root")
elif restrictChan == "wm":
    output_file = output_file.replace(".root", "_wmonly.root")
rfile = ROOT.TFile.Open(output_file,"RECREATE")

print "Found %i top events" % nTopEvents
print " --> %i of them passed selection" % nTopEventsPassed
print "From %i total events" % nEvents
print "%i in chan" % nSingleChan
print "%i passed selection" % nPass
print "Weighted events processed %0.3f" % sumWeights
print "Weighted events in selection %0.3f" % hmqq.Integral(0, hmqq.GetNbinsX()+1)
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

sumWeightsHist = ROOT.TH1D("sumweights", "sumweights", 1,0,10)
sumWeightsHist.Fill(1, sumWeights)
sumWeightsHist.Write()

rfile.Close()
