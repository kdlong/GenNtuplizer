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
        unsigned int nKeepLeps_;
        unsigned int nKeepJets_;
        const std::string jetsName_;
        const std::string lepsName_;
        TTree* ntuple_;
        unsigned int eventid_;
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
        void fillNtuple(edm::Handle<edm::OwnVector<reco::Candidate>>,
                        edm::Handle<edm::OwnVector<reco::Candidate>>);

        //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

            // ----------member data ---------------------------
};
WZGenAnalyzer::WZGenAnalyzer(const edm::ParameterSet& cfg) :
    genLeptonsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("leptons"))),
    genJetsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("jets"))),
    nKeepLeps_(cfg.getUntrackedParameter<unsigned int> ("nKeepLeps", 3)),
    nKeepJets_(cfg.getUntrackedParameter<unsigned int> ("nKeepJets", 4)),
    jetsName_(cfg.getUntrackedParameter<std::string> ("jetsName", "jet")),
    lepsName_(cfg.getUntrackedParameter<std::string> ("lepsName", "lep"))
{
    nLeps_ = 0;
    nJets_ = 0;
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
    edm::Handle<reco::CandidateCollection> genLeptons;
    event.getByToken(genLeptonsToken_, genLeptons);
    edm::Handle<reco::CandidateCollection> genJets;
    event.getByToken(genJetsToken_, genJets);

    if (genLeptons->size() >= nKeepLeps_) {
        fillNtuple(genLeptons, genJets);
        eventid_ = event.id().event();
        nPass_++;
    }
}

// ------------ method called once each job just before starting event loop  ------------
void 
WZGenAnalyzer::beginJob()
{
    jetPts_.resize(nKeepJets_, -999);
    jetEtas_.resize(nKeepJets_, -999);
    jetPdgIds_.resize(nKeepJets_, -999);
    leptonPts_.resize(nKeepLeps_, -999);
    leptonEtas_.resize(nKeepLeps_, -999);
    leptonPdgIds_.resize(nKeepLeps_, -999);

    edm::Service<TFileService> fs;
    ntuple_ = fs->make<TTree>("Ntuple", "Ntuple");
    
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
    ntuple_->Branch((std::string("n") + jetsName_).c_str(), &nJets_);
    for (unsigned int i = 1; i <= nKeepLeps_; i++)
    {
        std::string particleName = lepsName_ + std::to_string(i);
        ntuple_->Branch((particleName + "Pt").c_str(), &leptonPts_[i-1]);
        ntuple_->Branch((particleName + "Eta").c_str(), &leptonEtas_[i-1]);
        ntuple_->Branch((particleName + "pdgId").c_str(), &leptonPdgIds_[i-1]);
    }
    ntuple_->Branch((std::string("n") + lepsName_).c_str(), &nLeps_);
}

void
WZGenAnalyzer::fillNtuple(edm::Handle<edm::OwnVector<reco::Candidate>> leps,
                          edm::Handle<edm::OwnVector<reco::Candidate>> jets) {
    for(size_t i = 0; i < jets->size(); ++i) {
        const reco::Candidate& jet = (*jets)[i];
        jetPts_[i] = jet.pt();
        jetEtas_[i] = jet.eta();
        jetPdgIds_[i] = jet.pdgId();
    }
    for(size_t i = 0; i < leps->size(); ++i) {
        const reco::Candidate& lep = (*leps)[i];
        leptonPts_[i] = lep.pt();
        leptonEtas_[i] = lep.eta();
        leptonPdgIds_[i] = lep.pdgId();
    }
    nLeps_ = leps->size();
    nJets_ = jets->size();
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
void 
WZGenAnalyzer::endJob() 
{    
    //ntuple_->Branch("nPass", &nPass_);
    //ntuple_->Fill();
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
