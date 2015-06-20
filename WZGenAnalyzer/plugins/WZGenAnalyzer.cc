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
        edm::EDGetTokenT<reco::CandidateView> genLeptonsToken_;
        edm::EDGetTokenT<reco::CandidateView> genJetsToken_;
        edm::EDGetTokenT<reco::CandidateView> extraParticleToken_;
        edm::EDGetTokenT<reco::CandidateView> zMuMuCandsToken_;
        edm::EDGetTokenT<reco::CandidateView> zeeCandsToken_;
        edm::Service<TFileService> fileService_;
        TTree* ntuple_;
        std::map<std::string, BasicParticleEntry*> particleEntries_;
        double crossSection_;
        unsigned int nKeepLeps_;
        float zMass_;
        float zPt_;
        bool isZMuMu_;
        unsigned int eventid_;
        unsigned int nProcessed_;
        unsigned int nPass_;
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;
        void addParticlesToNtuple();
        const reco::Candidate& chooseBestZ(reco::CandidateView, reco::CandidateView);
        void fillNtuple(const reco::Candidate&);
        bool overlapsCollection(const reco::Candidate& cand, 
                                edm::Handle<reco::CandidateView>& collection,
                                const float deltaRCut,
                                const unsigned int maxCompare);
 
        virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

        // ----------member data ---------------------------
};
WZGenAnalyzer::WZGenAnalyzer(const edm::ParameterSet& cfg) :
    genLeptonsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("leptons"))),
    genJetsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("jets"))),
    extraParticleToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("extraParticle"))),
    zMuMuCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("zMuMuCands"))),
    zeeCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("zeeCands")))
{
    nProcessed_ = 0;
    nPass_ = 0;
    
    unsigned int nJets = cfg.getUntrackedParameter<unsigned int>("nKeepJets", 0);
    if (nJets > 0) {
        std::string jetsName = cfg.getUntrackedParameter<std::string>("jetsName", "j");
        particleEntries_["jets"] = new BasicParticleEntry(jetsName, nJets);
    }
    nKeepLeps_ = cfg.getUntrackedParameter<unsigned int>("nKeepLeps", 0);
    if (nKeepLeps_ > 0) {
        std::string lepsName = cfg.getUntrackedParameter<std::string>("lepsName", "l");
        particleEntries_["leps"] = new BasicParticleEntry(lepsName, nKeepLeps_);
    }
    unsigned int nExtra = cfg.getUntrackedParameter<unsigned int>("nKeepExtra", 0);
    if (nExtra > 0) {
        std::string extraName = cfg.getUntrackedParameter<std::string>("extraName", "g");
        particleEntries_["extra"] = new BasicParticleEntry(extraName, nExtra);
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
    edm::Handle<reco::CandidateView> genLeptons;
    event.getByToken(genLeptonsToken_, genLeptons);
    particleEntries_["leps"]->setCollection(*genLeptons);
    
    edm::Handle<reco::CandidateView> genJets;
    event.getByToken(genJetsToken_, genJets);
    particleEntries_["jets"]->setCollection(*genJets);
    
    edm::Handle<reco::CandidateView> extraParticle;
    event.getByToken(extraParticleToken_, extraParticle);
    particleEntries_["extra"]->setCollection(*extraParticle);
    
    edm::Handle<reco::CandidateView> zMuMuCands;
    event.getByToken(zMuMuCandsToken_, zMuMuCands); 
    edm::Handle<reco::CandidateView> zeeCands;
    event.getByToken(zeeCandsToken_, zeeCands);

    if (genLeptons->size() < nKeepLeps_)
        std::cout << "Didn't find " << nKeepLeps_ << " leptons";
        return;    
        
    if (zeeCands->size() == 0 && zMuMuCands->size() == 0) {
        return;
    }
    if (genLeptons->size() >= nKeepLeps_) {
        fillNtuple(chooseBestZ(*zMuMuCands, *zeeCands));
        eventid_ = event.id().event();
        nPass_++;
    }
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
    ntuple_->Branch("isZMuMu", &isZMuMu_);
}

void
<<<<<<< HEAD
WZGenAnalyzer::fillNtuple(edm::Handle<reco::CandidateCollection> leps,
                          edm::Handle<reco::CandidateCollection> jets,
                          const reco::Candidate& bestZ) {
    nJets_ = 0;
    std::cout << "Filling\n";
    for(size_t i = 0; i < jets->size(); ++i) {
        if (nJets_ > nKeepJets_)
            break;
        const reco::Candidate& jet = (*jets)[i];
        if (overlapsCollection(jet, leps, 0.5, 3))
            continue;
        jetPts_[nJets_] = jet.pt();
        jetEtas_[nJets_] = jet.eta();
        jetPdgIds_[nJets_] = jet.pdgId();
        nJets_++;
    }
    for(size_t i = 0; i < leps->size(); ++i) {
        if (i > nKeepLeps_)
            break;
        const reco::Candidate& lep = (*leps)[i];
        leptonPts_[i] = lep.pt();
        leptonEtas_[i] = lep.eta();
        leptonPdgIds_[i] = lep.pdgId();
    }
WZGenAnalyzer::fillNtuple(const reco::Candidate& bestZ) {
    for (auto& particleEntry : particleEntries_)
        particleEntry.second->fillNtupleInfo();
    zMass_ = bestZ.mass();
    zPt_ = bestZ.pt();
    ntuple_->Fill();
}
// ------------ method called once each job just after ending the event loop  ------------
bool
WZGenAnalyzer::overlapsCollection(const reco::Candidate& cand, 
                                  edm::Handle<reco::CandidateView>& collection,
                                  const float deltaRCut,
                                  const unsigned int maxCompare) {
    for(size_t i = 0; i < collection->size(); ++i) {
        if (i == maxCompare)
            break;
        if (reco::deltaR((*collection)[i], cand) < deltaRCut) {
            std::cout << "\nFailed dR cut. dR was " << reco::deltaR((*collection)[i], cand) << std::endl;
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
