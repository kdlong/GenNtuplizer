#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDProducer.h"
#include "GenNtuplizer/DataFormats/interface/DressedGenParticle.h"

class DressedGenParticlesProducer : public edm::EDProducer {
    public:

        DressedGenParticlesProducer(const edm::ParameterSet& cfg);
        virtual ~DressedGenParticlesProducer(){}
        void produce(edm::Event& event, const edm::EventSetup& es);
    private:
        edm::EDGetTokenT<reco::GenParticleCollection> baseCollectionToken_;
        edm::EDGetTokenT<reco::GenParticleCollection> associatesToken_;
        double dRmax_;
};

DressedGenParticlesProducer::DressedGenParticlesProducer(
        const edm::ParameterSet& cfg):
        baseCollectionToken_(consumes<reco::GenParticleCollection>(
            cfg.getParameter<edm::InputTag>("baseCollection"))),
        associatesToken_(consumes<reco::GenParticleCollection>(
            cfg.getParameter<edm::InputTag>("associates"))),
        dRmax_(cfg.getUntrackedParameter<double>("dRmax", 0.1)) {
    produces<DressedGenParticleCollection>();
}

void DressedGenParticlesProducer::produce(edm::Event& event, const edm::EventSetup& es) {
    std::auto_ptr<DressedGenParticleCollection> dressedCollection(new DressedGenParticleCollection);
    
    edm::Handle<reco::GenParticleCollection> baseCollection;
    event.getByToken(baseCollectionToken_, baseCollection);
    
    edm::Handle<reco::GenParticleCollection> associates;
    event.getByToken(associatesToken_, associates);

    for (const auto& base_particle : *baseCollection) {
        DressedGenParticle dressed_part = DressedGenParticle(base_particle,
            *associates, dRmax_);
        dressedCollection->push_back(dressed_part);
    }
    event.put(dressedCollection);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DressedGenParticlesProducer);
