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
    produces<edm::OwnVector<reco::Candidate>>();
    //produces<DressedGenParticleCollection>();
}

void DressedGenParticlesProducer::produce(edm::Event& event, const edm::EventSetup& es) {
    //std::auto_ptr<edm::OwnVector<DressedGenParticle>> dressedCollection(new edm::OwnVector<DressedGenParticle>);
    //std::auto_ptr<DressedGenParticleCollection> dressedCollection(new DressedGenParticleCollection);
    std::auto_ptr<edm::OwnVector<reco::Candidate>> dressedCollection(new edm::OwnVector<reco::Candidate>);
    
    edm::Handle<reco::GenParticleCollection> baseCollection;
    event.getByToken(baseCollectionToken_, baseCollection);
    
    edm::Handle<reco::GenParticleCollection> associates;
    event.getByToken(associatesToken_, associates);

    for (const auto& base_particle : *baseCollection) {
        DressedGenParticle dressed_part = DressedGenParticle(base_particle,
            *associates, dRmax_);
        dressedCollection->push_back(dressed_part);
        if (dressed_part.numAssociated() > 0) {
            std::cout << "the pdgid was " << dressed_part.pdgId() << std::endl;
            std::cout << "the pt was " << dressed_part.pt() << std::endl;
            std::cout << "the undressed pt was " << dressed_part.undressedPt() << std::endl;
            std::cout << "number of associated photons is" << dressed_part.numAssociated() << std::endl;
        }
    }
    event.put(dressedCollection);
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(DressedGenParticlesProducer);
