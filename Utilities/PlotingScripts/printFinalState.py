from DataFormats.FWLite import Events, Handle
import ROOT

#file_name="/afs/cern.ch/work/k/kelong/MCContactTests/WW_semileptonic/HIG-RunIISummer15wmLHEGS-02047_fixGen.root"
#file_name="/eos/user/k/kelong/LesHouchesVBSstudy/WpZ_VBFNLO/WpZTo1E1Nu2Mu_VBFNLO_100000_numEvent100000.root"
file_name="/hdfs/store/user/dteague/delphes_WZ_YR/EDM_WZ_EWK/lhe.root"
#file_name="root://cms-xrd-global.cern.ch///store/mc/RunIISummer16MiniAODv2/ChargedHiggsToWZTo3LNu_M1000_13TeV-madgraph-pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v3/10000/1ED09DA6-86F8-E711-A681-0025B3E025B6.root"

lorentz = ROOT.TLorentzVector
def lhep4(i, lheParticles):
    px = lheParticles.PUP.at(i)[0]
    py = lheParticles.PUP.at(i)[1]
    pz = lheParticles.PUP.at(i)[2]
    pE = lheParticles.PUP.at(i)[3]
    return lorentz(px, py, pz, pE)

def getLHEParticles(event):
    lheHandle = Handle('LHEEventProduct')
    label = "externalLHEProducer"
    label = 'source' 
    event.getByLabel(label, lheHandle)
    lhe = lheHandle.product()

    lheParticles = lhe.hepeup()

    nleps = 0
    print "Weight is", lheParticles.XWGTUP
    for i in range(lheParticles.NUP):
        p4 = lhep4(i, lheParticles)
        if (abs(lheParticles.IDUP[i]) in [11,13,15]):
            nleps+=1
            print "Found a lepton! PDG Id is", lheParticles.IDUP[i], "pt is", p4.Perp()
    return nleps

def getHepMCParticles(event):
    handle  = Handle ('std::vector<reco::GenParticle>')
    label = ("genParticles" if "MINIAOD" not in file_name else "prunedGenParticles")
    event.getByLabel (label, handle)
    
    genps = handle.product()

    nleps = 0
    for genp in genps:
        if (genp.isHardProcess() and abs(genp.pdgId()) in [11, 13, 15]):
            nleps+=1
            print "Found a lepton! PDG Id is", genp.pdgId()
        #if genp.isHardProcess() and abs(genp.pdgId()):
        #    print "Found a HP particle! PDG Id is", genp.pdgId()
    return nleps

events = Events(file_name)
nEvents = 1
fromLHE = True

for iev, event in enumerate(events):
    nEvents += 1
    if nEvents > 100:
        exit(0)
    print "-"*80
    nleps = getLHEParticles(event) if fromLHE else getHepMCParticles(event)

    print "Found %i leptons" % nleps
