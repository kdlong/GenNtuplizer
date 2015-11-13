// -*- C++ -*-
//
// Package:    GenNtuplizer/DibosonGenAnalyzer
// Class:      DibosonGenAnalyzer
// 
/**\class DibosonGenAnalyzer DibosonGenAnalyzer.cc GenNtuplizer/DibosonGenAnalyzer/plugins/DibosonGenAnalyzer.cc

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
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "SimDataFormats/GeneratorProducts/interface/GenEventInfoProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "SimDataFormats/GeneratorProducts/interface/LHERunInfoProduct.h"

#include "BasicParticleEntry.h"
#include "ZCandidateEntry.h"
#include "WCandidateEntry.h"
#include "TTree.h"
#include <vector>
//
// class declaration
//


class DibosonGenAnalyzer : public edm::EDAnalyzer {
    public:
        explicit DibosonGenAnalyzer(const edm::ParameterSet&);
        ~DibosonGenAnalyzer();
        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        edm::EDGetTokenT<reco::CandidateCollection> genLeptonsToken_;
        edm::EDGetTokenT<reco::CandidateCollection> genJetsToken_;
        edm::EDGetTokenT<reco::CandidateCollection> extraParticleToken_;
        edm::EDGetTokenT<reco::CandidateCollection> wCandsToken_;
        edm::EDGetTokenT<reco::CandidateCollection> zCandsToken_;
        edm::EDGetTokenT<GenEventInfoProduct> genEventInfoToken_;
        edm::EDGetTokenT<LHERunInfoProduct> lheRunInfoToken_;
        edm::EDGetTokenT<LHEEventProduct> lheEventToken_;
        edm::Service<TFileService> fileService_;
        TTree* ntuple_;
        std::map<std::string, BasicParticleEntry*> particleEntries_;
        std::string lheHeader_;
        double crossSection_;
        std::string extraName_;
        unsigned int nKeepLeps_;
        unsigned int nKeepExtra_;
        unsigned int nKeepWs_;
        unsigned int nZsCut_;
        double initSumWeights_;
        double fidSumWeights_;
        double weight_;
        double XWGTUP_;
        std::vector<std::string> LHEWeightIDs_;
        std::vector<double> LHEWeights_;
        std::vector<double> LHEWeightSums_;
        unsigned int eventid_;
        unsigned int nProcessed_;
        unsigned int nPass_;
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;
        void addParticlesToNtuple();
        void fillNtuple();
        void setWeightInfo(const edm::Event& event);
        double getEventWeight(const edm::Event& event);
        bool overlapsCollection(const reco::Candidate& cand, 
                                reco::CandidateCollection collection,
                                const float deltaRCut,
                                const unsigned int maxCompare);
        reco::CandidateCollection cleanJets(reco::CandidateCollection, reco::CandidateCollection);
        //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

        // ----------member data ---------------------------
};
DibosonGenAnalyzer::DibosonGenAnalyzer(const edm::ParameterSet& cfg) :
    genLeptonsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("leptons"))),
    genJetsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("jets"))),
    extraParticleToken_(consumes<reco::CandidateCollection>(cfg.getUntrackedParameter<edm::InputTag>(
        "extraParticle", edm::InputTag("leptons")))),
    wCandsToken_(consumes<reco::CandidateCollection>(cfg.getUntrackedParameter<edm::InputTag>(
        "wCands", edm::InputTag("zCands")))),
    zCandsToken_(consumes<reco::CandidateCollection>(cfg.getParameter<edm::InputTag>("zCands"))),
    genEventInfoToken_(consumes<GenEventInfoProduct>(edm::InputTag("generator"))),
    lheRunInfoToken_(consumes<LHERunInfoProduct, edm::InRun>(
        cfg.getParameter<edm::InputTag>("lheSource"))),
    lheEventToken_(consumes<LHEEventProduct>(cfg.getParameter<edm::InputTag>("lheSource")))
{
    lheHeader_ = "";
    nProcessed_ = 0;
    initSumWeights_ = 0;
    fidSumWeights_ = 0;
    nPass_ = 0;
    crossSection_ = cfg.getUntrackedParameter<double>("xSec", -1);
    nZsCut_  = cfg.getUntrackedParameter<unsigned int>("nZsCut", 1);
    
    unsigned int nJets = cfg.getUntrackedParameter<unsigned int>("nKeepJets", 0);
    std::string jetsName = cfg.getUntrackedParameter<std::string>("jetsName", "j");
    particleEntries_["jets"] = new BasicParticleEntry(jetsName, nJets, false);
    
    nKeepLeps_ = cfg.getUntrackedParameter<unsigned int>("nKeepLeps", 0);
    std::string lepsName = cfg.getUntrackedParameter<std::string>("lepsName", "l");
    particleEntries_["leps"] = new BasicParticleEntry(lepsName, nKeepLeps_, true);
    
    unsigned int nKeepZs  = cfg.getUntrackedParameter<unsigned int>("nKeepZs", 0);
    std::string ZsName = cfg.getUntrackedParameter<std::string>("ZsName", "Z");
    particleEntries_["Zs"] = new ZCandidateEntry(ZsName, nKeepZs);
    
    nKeepExtra_ = cfg.getUntrackedParameter<unsigned int>("nKeepExtra", 0);
    if (nKeepExtra_ > 0) {
        std::string extraName_ = cfg.getUntrackedParameter<std::string>("extraName", "x");
        particleEntries_["extra"] = new BasicParticleEntry(extraName_, nKeepExtra_, true);
    }
    nKeepWs_ = cfg.getUntrackedParameter<unsigned int>("nKeepWs", 0);
    if (nKeepWs_ > 0) {
        std::string WsName = cfg.getUntrackedParameter<std::string>("WsName", "W");
        particleEntries_["Ws"] = new WCandidateEntry(WsName, nKeepWs_);
    }
    
    ntuple_ = fileService_->make<TTree>("Ntuple", "Ntuple"); 
    addParticlesToNtuple();
    ntuple_->Branch("evtid", &eventid_);
    ntuple_->Branch("weight", &weight_);
    ntuple_->Branch("XWGTUP", &XWGTUP_);
    
    // Raise autosave value to fix annoying issue of ntuple being written 
    // into file multiple times
    ntuple_->SetAutoSave(-30000000000000);
    ntuple_->Branch("LHEweights", &LHEWeights_);
    ntuple_->Branch("LHEweightIDs", &LHEWeightIDs_);
}

DibosonGenAnalyzer::~DibosonGenAnalyzer()
{
     // do anything here that needs to be done at desctruction time
     // (e.g. close files, deallocate resources etc.)
}


//
// member functions
//

// ------------ method called for each event    ------------
void
DibosonGenAnalyzer::analyze(const edm::Event& event, const edm::EventSetup& evSetup)
{
    nProcessed_++;
    initSumWeights_ += getEventWeight(event);
    
    edm::Handle<reco::CandidateCollection> genLeptons;
    event.getByToken(genLeptonsToken_, genLeptons);
    particleEntries_["leps"]->setCollection(*genLeptons);
    
    edm::Handle<reco::CandidateCollection> genJets;
    event.getByToken(genJetsToken_, genJets);

    reco::CandidateCollection cleanedJets = cleanJets(*genJets, *genLeptons);
    particleEntries_["jets"]->setCollection(cleanedJets);
    if (nKeepExtra_ > 0) { 
        edm::Handle<reco::CandidateCollection> extraParticle;
        event.getByToken(extraParticleToken_, extraParticle);
        particleEntries_["extra"]->setCollection(*extraParticle);
    }
    edm::Handle<reco::CandidateCollection> wCands;
    if (nKeepWs_ > 0) { 
        event.getByToken(wCandsToken_, wCands);
        particleEntries_["Ws"]->setCollection(*wCands);
    }
    edm::Handle<reco::CandidateCollection> zCands;
    event.getByToken(zCandsToken_, zCands);
    particleEntries_["Zs"]->setCollection(*zCands);
    
    std::cout << genLeptons->size();
    if (genLeptons->size() < nKeepLeps_) {
        std::cout << "Failed to find " << nKeepLeps_ << " leptons" << std::endl;
        return;    
    }
    //if (wCands->size() != 1)
    //   return; 
    if (zCands->size() < nZsCut_) {
        std::cout << "Failed Z cut" << std::endl;
    }
    setWeightInfo(event);
    fillNtuple();
    eventid_ = event.id().event();
    nPass_++;
}

void 
DibosonGenAnalyzer::beginJob()
{
}

void
DibosonGenAnalyzer::addParticlesToNtuple() {
    for (auto& particleEntry : particleEntries_) {
        if (particleEntry.first == "Zs") {
            static_cast<ZCandidateEntry*>(
                particleEntry.second)->createNtupleEntry(ntuple_);
        }
        else if (particleEntry.first == "Ws") {
            static_cast<WCandidateEntry*>(
                particleEntry.second)->createNtupleEntry(ntuple_);
        }
        else
            particleEntry.second->createNtupleEntry(ntuple_);
    }
}

void
DibosonGenAnalyzer::fillNtuple() {
    for (auto& particleEntry : particleEntries_) {
        if (particleEntry.first == "Zs") {
            static_cast<ZCandidateEntry*>(
                particleEntry.second)->fillNtupleInfo();;
        }
        else if (particleEntry.first == "Ws") {
            static_cast<WCandidateEntry*>(
                particleEntry.second)->fillNtupleInfo();;
        }
        else
            particleEntry.second->fillNtupleInfo();
    }
    ntuple_->Fill();
}

double DibosonGenAnalyzer::getEventWeight(const edm::Event& event) {
    edm::Handle<GenEventInfoProduct> genEventInfo;
    event.getByToken(genEventInfoToken_, genEventInfo);
    return genEventInfo->weights()[0];
} 

void
DibosonGenAnalyzer::setWeightInfo(const edm::Event& event) {
    weight_ = getEventWeight(event);
    fidSumWeights_ += weight_;
    
    edm::Handle<LHEEventProduct> lheEventInfo;
    event.getByToken(lheEventToken_, lheEventInfo);
    XWGTUP_ = lheEventInfo->originalXWGTUP();
   
    LHEWeights_.clear();
    LHEWeightIDs_.clear();
   
    for(const auto& weight : lheEventInfo->weights()) {
        LHEWeightIDs_.push_back(weight.id);
        LHEWeights_.push_back(weight.wgt);
    }
    if (LHEWeightSums_.empty())
        LHEWeightSums_ = LHEWeights_;
    else {
        for (size_t i = 0; i < LHEWeightSums_.size(); i++)
            LHEWeightSums_[i] += LHEWeights_[i];
    }
}
reco::CandidateCollection
DibosonGenAnalyzer::cleanJets(reco::CandidateCollection jets, reco::CandidateCollection leps) {
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
DibosonGenAnalyzer::overlapsCollection(const reco::Candidate& cand,
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
DibosonGenAnalyzer::endJob() 
{    
    TTree* metaData = fileService_->make<TTree>("MetaData", "MetaData");
    metaData->Branch("nProcessedEvents", &nProcessed_);
    metaData->Branch("nPass", &nPass_);
    metaData->Branch("inputXSection", &crossSection_);
    metaData->Branch("initSumWeights", &initSumWeights_);
    metaData->Branch("fidSumWeights", &fidSumWeights_);
    float fidXSec = crossSection_ * fidSumWeights_/initSumWeights_;
    metaData->Branch("fidXSection", &fidXSec);
    metaData->Branch("LHEweightIDs", &LHEWeightIDs_);
    metaData->Branch("LHEheader", &lheHeader_);
    metaData->Branch("LHEweightSums", &LHEWeightSums_);
    metaData->Fill();
}

// ------------ method called when starting to processes a run  ------------

/*
void 
DibosonGenAnalyzer::beginRun(edm::Run const& iRun, edm::EventSetup const&)
{
}
*/
// ------------ method called when ending the processing of a run  ------------
void 
DibosonGenAnalyzer::endRun(edm::Run const& iRun, edm::EventSetup const&)
{   
    if (lheHeader_ != "")
        return; //The LHE header really really really should be the same for each run
    edm::Handle<LHERunInfoProduct> lheRunInfoHandle;
    iRun.getByToken( lheRunInfoToken_, lheRunInfoHandle );

    typedef std::vector<LHERunInfoProduct::Header>::const_iterator headers_const_iterator;
    for (headers_const_iterator iter=lheRunInfoHandle->headers_begin(); iter!=lheRunInfoHandle->headers_end(); iter++){
        for (const auto& line : iter->lines())
            lheHeader_ += line;
    }  
}
// ------------ method called when starting to processes a luminosity block  ------------
/*
void 
DibosonGenAnalyzer::beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method called when ending the processing of a luminosity block  ------------
/*
void 
DibosonGenAnalyzer::endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&)
{
}
*/

// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------
void
DibosonGenAnalyzer::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

//define this as a plug-in
DEFINE_FWK_MODULE(DibosonGenAnalyzer);
