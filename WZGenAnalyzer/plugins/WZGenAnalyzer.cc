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
#include <DataFormats/Candidate/interface/CompositeCandidate.h>
#include "DataFormats/Math/interface/deltaR.h"
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
        edm::EDGetTokenT<reco::CandidateView> zMuMuCandsToken_;
        edm::EDGetTokenT<reco::CandidateView> zeeCandsToken_;
        edm::Service<TFileService> fileService_;
        unsigned int nKeepLeps_;
        unsigned int nKeepJets_;
        std::string jetsName_;
        std::string lepsName_;
        TTree* ntuple_;
        double crossSection_;
        float zMass_;
        float zPt_;
        bool isZMuMu_;
        unsigned int eventid_;
        unsigned int nProcessed_;
        unsigned int nPass_;
        unsigned int nLeps_;
        unsigned int nJets_;
        std::vector<float> leptonPts_;
        std::vector<float> leptonEtas_;
        std::vector<float> leptonPdgIds_;
        std::vector<float> jetPts_;
        std::vector<float> jetEtas_;
        std::vector<float> jetPdgIds_;
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;
        void addParticlesToNtuple();
        const reco::Candidate& chooseBestZ(edm::Handle<reco::CandidateView>,
                                           edm::Handle<reco::CandidateView>);
        void fillNtuple(edm::Handle<reco::CandidateCollection>,
                        edm::Handle<reco::CandidateCollection>,
                        const reco::Candidate&);
        bool overlapsCollection(const reco::Candidate& cand, 
                                edm::Handle<reco::CandidateCollection>& collection,
                                const float deltaRCut,
                                const unsigned int maxCompare);
 
        //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

            // ----------member data ---------------------------
};
WZGenAnalyzer::WZGenAnalyzer(const edm::ParameterSet& cfg) :
    genLeptonsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("leptons"))),
    genJetsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("jets"))),
    zMuMuCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("zMuMuCands"))),
    zeeCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("zeeCands"))),
    nKeepLeps_(cfg.getUntrackedParameter<unsigned int> ("nKeepLeps", 3)),
    nKeepJets_(cfg.getUntrackedParameter<unsigned int> ("nKeepJets", 4)),
    jetsName_(cfg.getUntrackedParameter<std::string> ("jetsName", "jet")),
    lepsName_(cfg.getUntrackedParameter<std::string> ("lepsName", "lep")),
    crossSection_(cfg.getParameter<double> ("crossSection"))
{
    nProcessed_ = 0;
    nLeps_ = 0;
    nPass_ = 0;
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
    edm::Handle<reco::CandidateCollection> genJets;
    event.getByToken(genJetsToken_, genJets);   
   
    edm::Handle<reco::CandidateView> zMuMuCands;
    event.getByToken(zMuMuCandsToken_, zMuMuCands); 
    edm::Handle<reco::CandidateView> zeeCands;
    event.getByToken(zeeCandsToken_, zeeCands);

    if (zeeCands->empty() && zMuMuCands->empty()) {
        return;
    }
    //if (genLeptons->size() >= nKeepLeps_) {
        fillNtuple(genLeptons, genJets, chooseBestZ(zMuMuCands, zeeCands));
        eventid_ = event.id().event();
        nPass_++;
    //}
}

// ------------ method called once each job just before starting event loop  ------------

//const reco::CandidateBaseRef&
const reco::Candidate&
WZGenAnalyzer::chooseBestZ(edm::Handle<reco::CandidateView> zMuMuCands,
                           edm::Handle<reco::CandidateView> zeeCands) { 
    const float ZMASS = 91.1876;
    if (zeeCands->empty()) {
        isZMuMu_ = true;
        return (*zMuMuCands)[0];
    }
    else if (zMuMuCands->empty()) {
        isZMuMu_ = false;
        return (*zeeCands)[0];
    }
    if ((*zeeCands)[0].numberOfDaughters() != 2 || (*zMuMuCands)[0].numberOfDaughters() != 2) 
        throw cms::Exception("CorruptData") << "Z constructed from wrong number of daughters\n";
    if (((*zMuMuCands)[0].mass() - ZMASS) < ((*zeeCands)[0].mass() - ZMASS)) {
        isZMuMu_ = false;
        return (*zMuMuCands)[0];
    }
    isZMuMu_ = false;
    return (*zeeCands)[0];
}       

void 
WZGenAnalyzer::beginJob()
{
    jetPts_.resize(nKeepJets_, -999);
    jetEtas_.resize(nKeepJets_, -999);
    jetPdgIds_.resize(nKeepJets_, -999);
    leptonPts_.resize(nKeepLeps_, -999);
    leptonEtas_.resize(nKeepLeps_, -999);
    leptonPdgIds_.resize(nKeepLeps_, -999);

    ntuple_ = fileService_->make<TTree>("Ntuple", "Ntuple");
    
    addParticlesToNtuple();
    ntuple_->Branch("evtid", &eventid_);
}

void
WZGenAnalyzer::addParticlesToNtuple() {
    for (unsigned int i = 1; i <= nKeepJets_; i++)
    {
        std::string particleName = jetsName_ + std::to_string(i);
        ntuple_->Branch((particleName + "Pt").c_str(), &jetPts_[i-1]);
        ntuple_->Branch((particleName + "Eta").c_str(), &jetEtas_[i-1]);
        ntuple_->Branch((particleName + "pdgId").c_str(), &jetPdgIds_[i-1]);
    }
    ntuple_->Branch("nJets", &nJets_);
    for (unsigned int i = 1; i <= nKeepLeps_; i++)
    {
        std::string particleName = lepsName_ + std::to_string(i);
        ntuple_->Branch((particleName + "Pt").c_str(), &leptonPts_[i-1]);
        ntuple_->Branch((particleName + "Eta").c_str(), &leptonEtas_[i-1]);
        ntuple_->Branch((particleName + "pdgId").c_str(), &leptonPdgIds_[i-1]);
    }
    ntuple_->Branch((std::string("n") + lepsName_).c_str(), &nLeps_);
    ntuple_->Branch("zMass", &zMass_);
    ntuple_->Branch("zPt", &zPt_);
    ntuple_->Branch("isZMuMu", &isZMuMu_);
}

void
WZGenAnalyzer::fillNtuple(edm::Handle<reco::CandidateCollection> leps,
                          edm::Handle<reco::CandidateCollection> jets,
                          const reco::Candidate& bestZ) {
    nJets_ = 0;
    for(size_t i = 0; i < jets->size(); ++i) {
        if (i > nKeepJets_)
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
    zMass_ = bestZ.mass();
    zPt_ = bestZ.pt();
    nLeps_ = leps->size();
    ntuple_->Fill();
    leptonEtas_.clear();
    leptonEtas_.resize(nKeepLeps_, -999);
    leptonPts_.clear();
    leptonPts_.resize(nKeepLeps_, -999);
    leptonPdgIds_.clear();
    leptonPdgIds_.resize(nKeepLeps_, -999);

    jetEtas_.clear();
    jetEtas_.resize(nKeepJets_, -999);
    jetPts_.clear();
    jetPts_.resize(nKeepJets_, -999);
    jetPdgIds_.clear();
    jetPdgIds_.resize(nKeepJets_, -999);
}
// ------------ method called once each job just after ending the event loop  ------------
bool
WZGenAnalyzer::overlapsCollection(const reco::Candidate& cand, 
                                  edm::Handle<reco::CandidateCollection>& collection,
                                  const float deltaRCut,
                                  const unsigned int maxCompare) {
    for(size_t i = 0; i < collection->size(); ++i) {
        if (i == maxCompare)
            break;
        if (reco::deltaR((*collection)[i], cand) > deltaRCut) {
            std::cout << "Failed dR cut\n";
            return false;
        }
    }
    return true;
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
/*
void 
WZGenAnalyzer::beginRun(edm::Run const&, edm::EventSetup const&)
{
}
*/

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
