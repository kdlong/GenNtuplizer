// -*- C++ -*-
//
// Package:    GenNtuplizer/WZGenAnalyzer
// Class:      WZGenAnalyzer
// 
/**\class WZGenAnalyzer WZGenAnalyzer.cc GenNtuplizer/WZGenAnalyzer/plugins/WZGenAnalyzer.cc

 Description: [one line class summary]

 Implementation:
     [Notes on implementation]
*/
//
// Original Author:  Kenneth David Long
//         Created:  Wed, 10 Jun 2015 12:29:36 GMT
//
//


// system include files
#include <memory>

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"

#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"
#include "DataFormats/METReco/interface/GenMET.h"
#include "DataFormats/METReco/interface/GenMETCollection.h"

#include "BasicParticleEntry.h"
#include "TTree.h"
#include <vector>
//
// class declaration
//


class WZGenAnalyzer : public edm::EDAnalyzer {
    public:
        explicit WZGenAnalyzer(const edm::ParameterSet&);
        ~WZGenAnalyzer();
        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        edm::EDGetTokenT<reco::CandidateCollection> genLeptonsToken_;
        edm::EDGetTokenT<reco::CandidateCollection> genJetsToken_;
        edm::EDGetTokenT<reco::GenMETCollection> genMETToken_;
        edm::EDGetTokenT<reco::CandidateCollection> extraParticleToken_;
        edm::EDGetTokenT<reco::CandidateView> zMuMuCandsToken_;
        edm::EDGetTokenT<reco::CandidateView> zeeCandsToken_;
        edm::Service<TFileService> fileService_;
        TTree* ntuple_;
        std::map<std::string, BasicParticleEntry*> particleEntries_;
        double crossSection_;
        unsigned int nKeepLeps_;
        unsigned int nKeepExtra_;
        float zMass_;
        float zPt_;
        float MET_;
        bool isZMuMu_;
        unsigned int eventid_;
        unsigned int nProcessed_;
        unsigned int nPass_;
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;
        void addParticlesToNtuple();
        const reco::Candidate& chooseBestZ(reco::CandidateView, reco::CandidateView);
        void fillNtuple(float, const reco::Candidate&);
        bool overlapsCollection(const reco::Candidate& cand, 
                                reco::CandidateCollection collection,
                                const float deltaRCut,
                                const unsigned int maxCompare);
        reco::CandidateCollection cleanJets(reco::CandidateCollection, reco::CandidateCollection);
        virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

        // ----------member data ---------------------------
};
WZGenAnalyzer::WZGenAnalyzer(const edm::ParameterSet& cfg) :
    genLeptonsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("leptons"))),
    genJetsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("jets"))),
    genMETToken_(consumes<reco::GenMETCollection>(cfg.getParameter<edm::InputTag>("met"))),
    extraParticleToken_(consumes<reco::CandidateCollection>(cfg.getUntrackedParameter<edm::InputTag>(
        "extraParticle", edm::InputTag("genParticles")))),
    zMuMuCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("zMuMuCands"))),
    zeeCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("zeeCands")))
{
    nProcessed_ = 0;
    nPass_ = 0;
    
    unsigned int nJets = cfg.getUntrackedParameter<unsigned int>("nKeepJets", 0);
    std::string jetsName = cfg.getUntrackedParameter<std::string>("jetsName", "j");
    particleEntries_["jets"] = new BasicParticleEntry(jetsName, nJets);
    
    nKeepLeps_ = cfg.getUntrackedParameter<unsigned int>("nKeepLeps", 0);
    std::string lepsName = cfg.getUntrackedParameter<std::string>("lepsName", "l");
    particleEntries_["leps"] = new BasicParticleEntry(lepsName, nKeepLeps_);
    
    nKeepExtra_ = cfg.getUntrackedParameter<unsigned int>("nKeepExtra", 0);
    if (nKeepExtra_ > 0) {
        std::string extraName = cfg.getUntrackedParameter<std::string>("extraName", "x");
        particleEntries_["extra"] = new BasicParticleEntry(extraName, nKeepExtra_);
    }
}

WZGenAnalyzer::~WZGenAnalyzer()
{
     // do anything here that needs to be done at desctruction time
     // (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called for each event    ------------
void
WZGenAnalyzer::analyze(const edm::Event& event, const edm::EventSetup& evSetup)
{
    nProcessed_++;
    edm::Handle<reco::CandidateCollection> genLeptons;
    event.getByToken(genLeptonsToken_, genLeptons);
    particleEntries_["leps"]->setCollection(*genLeptons);
    
    edm::Handle<reco::CandidateCollection> genJets;
    event.getByToken(genJetsToken_, genJets);
    
    edm::Handle<reco::GenMETCollection> genMETCol;
    event.getByToken(genMETToken_, genMETCol);
    float genMET = (*genMETCol).front().pt();

    reco::CandidateCollection cleanedJets = cleanJets(*genJets, *genLeptons);
    particleEntries_["jets"]->setCollection(cleanedJets);
    if (nKeepExtra_ > 0) { 
        edm::Handle<reco::CandidateCollection> extraParticle;
        event.getByToken(extraParticleToken_, extraParticle);
        particleEntries_["extra"]->setCollection(*extraParticle);
    }
    edm::Handle<reco::CandidateView> zMuMuCands;
    event.getByToken(zMuMuCandsToken_, zMuMuCands); 
    edm::Handle<reco::CandidateView> zeeCands;
    event.getByToken(zeeCandsToken_, zeeCands);
    if (genLeptons->size() < nKeepLeps_) {
        std::cout << "Failed to find " << nKeepLeps_ << " leptons" << std::endl;
        return;    
    }
    if ((*genLeptons)[0].pt() < 20 || (*genLeptons)[0].pt() < 20) {
        std::cout << "Failed lepton pt cuts";
        return;
    }
    if (zeeCands->size() == 0 && zMuMuCands->size() == 0) {
        std::cout << "Failed Z cut" << std::endl;
        return;
    }
    if (genMET < 30) {
        return;
        std::cout << "Failed MET cut" << std::endl;
    }
    fillNtuple(genMET, chooseBestZ(*zMuMuCands, *zeeCands));
    eventid_ = event.id().event();
    nPass_++;
}

// ------------ method called once each job just before starting event loop  ------------

const reco::Candidate&
WZGenAnalyzer::chooseBestZ(reco::CandidateView zMuMuCands,
                           reco::CandidateView zeeCands) { 
    const float ZMASS = 91.1876;
    if (zeeCands.empty()) {
        isZMuMu_ = true;
        return zMuMuCands[0];
    }
    else if (zMuMuCands.empty()) {
        isZMuMu_ = false;
        return zeeCands[0];
    }
    if (zeeCands[0].numberOfDaughters() != 2 || zMuMuCands[0].numberOfDaughters() != 2) 
        throw cms::Exception("CorruptData") << "Z constructed from wrong number of daughters\n";
    if ((zMuMuCands[0].mass() - ZMASS) < (zeeCands[0].mass() - ZMASS)) {
        isZMuMu_ = false;
        return zMuMuCands[0];
    }
    isZMuMu_ = false;
    return zeeCands[0];
}       

void 
WZGenAnalyzer::beginJob()
{
    ntuple_ = fileService_->make<TTree>("Ntuple", "Ntuple"); 
    addParticlesToNtuple();
    ntuple_->Branch("evtid", &eventid_);
}

void
WZGenAnalyzer::addParticlesToNtuple() {
    for (auto& particleEntry : particleEntries_)
        particleEntry.second->createNtupleEntry(ntuple_);
    ntuple_->Branch("zMass", &zMass_);
    ntuple_->Branch("zPt", &zPt_);
    ntuple_->Branch("MET", &MET_);
    ntuple_->Branch("isZMuMu", &isZMuMu_);
}
/*
void
WZGenAnalyzer::fillNtuple(edm::Handle<reco::CandidateCollection> leps,
                          edm::Handle<reco::CandidateCollection> jets,
                          const reco::Candidate& bestZ) {
    nJets_ = 0;
    std::cout << "Filling\n";
    for(size_t i = 0; i < leps->size(); ++i) {
        if (i > nKeepLeps_)
            break;
        const reco::Candidate& lep = (*leps)[i];
        leptonPts_[i] = lep.pt();
        leptonEtas_[i] = lep.eta();
        leptonPdgIds_[i] = lep.pdgId();
    }
*/
void
WZGenAnalyzer::fillNtuple(float MET, const reco::Candidate& bestZ) {
    for (auto& particleEntry : particleEntries_)
        particleEntry.second->fillNtupleInfo();
    zMass_ = bestZ.mass();
    zPt_ = bestZ.pt();
    MET_ = MET;
    ntuple_->Fill();
}
// ------------ method called once each job just after ending the event loop  ------------
reco::CandidateCollection
WZGenAnalyzer::cleanJets(reco::CandidateCollection jets, reco::CandidateCollection leps) {
    reco::CandidateCollection cleanedJets;
    for(size_t i = 0; i < jets.size(); ++i) {
        const reco::Candidate& jet = jets[i];
        if (overlapsCollection(jet, leps, 0.5, 3))
            continue;
        cleanedJets.push_back(jets[i]);
    }
    return cleanedJets;
}

bool
WZGenAnalyzer::overlapsCollection(const reco::Candidate& cand, 
                                  reco::CandidateCollection collection,
                                  const float deltaRCut,
                                  const unsigned int maxCompare) {
    for(size_t i = 0; i < collection.size(); ++i) {
        if (i == maxCompare)
            break;
        if (reco::deltaR(collection[i], cand) < deltaRCut) {
            return true;
        }
    }
    return false;
}

void 
WZGenAnalyzer::endJob() 
{    
    TTree* metaData = fileService_->make<TTree>("MetaData", "MetaData");
    metaData->Branch("nProcessedEvents", &nProcessed_);
    metaData->Branch("nPass", &nPass_);
    metaData->Branch("inputXSection", &crossSection_);
    float fidXSec = crossSection_ * static_cast<float>(nPass_)/nProcessed_;
    metaData->Branch("fidXSection", &fidXSec);
    metaData->Fill();
}

// ------------ method called when starting to processes a run  ------------

void 
WZGenAnalyzer::beginRun(edm::Run const& iRun, edm::EventSetup const&)
{
    edm::Handle< GenRunInfoProduct > genRunInfoProduct;
    iRun.getByLabel("generator", genRunInfoProduct );
    crossSection_ = (double) genRunInfoProduct->crossSection(); 
}


// ------------ method called when ending the processing of a run  ------------
/*
void 
WZGenAnalyzer::endRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
WZGenAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
WZGenAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
WZGenAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(WZGenAnalyzer);
