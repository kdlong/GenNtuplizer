#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/EDProducer.h"

#include "CommonTools/Utils/interface/PtComparator.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/PATObject.h"

class OSSFLeptonCollectionProducer : public edm::EDProducer {
    public:

        OSSFLeptonCollectionProducer(const edm::ParameterSet& cfg);
        virtual ~OSSFLeptonCollectionProducer(){}
        void produce(edm::Event& event, const edm::EventSetup& es);
    private:
        edm::EDGetTokenT<reco::CandidateCollection> srcToken_;
};

OSSFLeptonCollectionProducer::OSSFLeptonCollectionProducer(
        const edm::ParameterSet& cfg):
        srcToken_(consumes<reco::CandidateCollection>(
            cfg.getParameter<edm::InputTag>("src"))) {
    produces<reco::CandidateCollection>();
}

void OSSFLeptonCollectionProducer::produce(edm::Event& event, const edm::EventSetup& es) {
    std::unique_ptr<reco::CandidateCollection> outputCollection(new reco::CandidateCollection);

    edm::Handle<reco::CandidateCollection> srcCollection;
    event.getByToken(srcToken_, srcCollection);
    int sumPdgIds = 0;

    std::vector<const reco::Candidate*> tempCollection;
    // Expects that the passed selection is sorted!!!
    for (auto& part : *srcCollection ) {
        if (std::abs(part.pdgId()) != 11 && std::abs(part.pdgId()) != 13)
            continue;
        if (outputCollection->size() < 2)
            outputCollection->push_back(part);
        else {
            sumPdgIds = outputCollection->front().pdgId() + outputCollection->back().pdgId() + part.pdgId();
            if (std::abs(sumPdgIds) == 11 || std::abs(sumPdgIds) == 13) {
                // This only works for WZ, will need logic changes to support ZZ
                outputCollection->push_back(part);
                break;
            }
            // Keep looking for an OSSF pair if not found
            else if (tempCollection.size() == 0)
                tempCollection.push_back(&part);
            else {
                for (auto tempPart : tempCollection) {
                    if (tempPart == nullptr)
                        std::cout << "Oui, c'est ca le problem";
                    if (part.pdgId())
                        std::cout << "no mais c'est ca le problem";
                    if (&part == nullptr)
                        std::cout << "mais d'ailleurs c'est ca";
                    if (tempPart->pdgId() + part.pdgId() == 0) {
                        //remove 2nd lepton and replace with OSSF pair
                        outputCollection->pop_back();
                        outputCollection->push_back(*tempPart);
                        outputCollection->push_back(part);
                        break;
                    }
                    else
                        tempCollection.push_back(&part);
                }
            }
        }
    }
    if (outputCollection->size() != 3) {
        std::cout << "-------------------------" << std::endl;
        std::cout << "output collection" << std::endl;
        std::cout << "sumPdgIds" << sumPdgIds << std::endl;
        for (auto& part : *outputCollection) 
            std::cout << "pdgId is " << part.pdgId() << "pt is " << part.pt() << std::endl;
        std::cout << "input collection size" << srcCollection->size() << std::endl;
        for (auto& part : *srcCollection) 
            std::cout << "pdgId is " << part.pdgId() << "pt is " << part.pt() << std::endl;
    }
    
    event.put(std::move(outputCollection));
}

#include "FWCore/Framework/interface/MakerMacros.h"
DEFINE_FWK_MODULE(OSSFLeptonCollectionProducer);
