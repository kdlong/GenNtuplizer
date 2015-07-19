#include "FWCore/Framework/interface/Event.h"
#include "FWCore/MessageLogger/interface/MessageLogger.h"
#include "DataFormats/Common/interface/Handle.h"

// user include files
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/Framework/interface/EDAnalyzer.h"
#include "FWCore/Framework/interface/MakerMacros.h"

#include "DataFormats/Candidate/interface/CompositeCandidate.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

#include <map>
#include <memory>

class ZCandTest : public edm::EDAnalyzer {
    public:
        explicit ZCandTest(const edm::ParameterSet&);
        ~ZCandTest();
        static void fillDescriptions(edm::ConfigurationDescriptions& descriptions);

    private:
        edm::EDGetTokenT<reco::CandidateView> zCandsToken_;
        bool hasUniqueDaughters(const reco::Candidate&,
                                size_t, reco::CandidateView);
        bool isTrueZ(const reco::Candidate& zCand);
        bool sameKinematics(const reco::Candidate&, const reco::Candidate&);
        const reco::Candidate& getFirstDistinctMother(const reco::Candidate& cand);
        virtual void beginJob() override;
        virtual void analyze(const edm::Event&, const edm::EventSetup&) override;
        virtual void endJob() override;
        //virtual void beginRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void endRun(edm::Run const&, edm::EventSetup const&) override;
        //virtual void beginLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;
        //virtual void endLuminosityBlock(edm::LuminosityBlock const&, edm::EventSetup const&) override;

        // ----------member data ---------------------------
};

ZCandTest::ZCandTest( const edm::ParameterSet & cfg ) :
    zCandsToken_(consumes<reco::CandidateView>(cfg.getParameter<edm::InputTag>("src")))
{
}

ZCandTest::~ZCandTest()
{
}

void ZCandTest::beginJob() {
}

void ZCandTest::endJob() {
}

void ZCandTest::analyze(const edm::Event& event, const edm::EventSetup& evSetup) {
    edm::Handle<reco::CandidateView> zCands;
    event.getByToken(zCandsToken_, zCands);

    std::cout << "Num Z candidates in event is: " << zCands->size() << std::endl;
    size_t i = 0;
    for (const auto& cand : (*zCands)) {
        std::cout << "Pt is: " << cand.pt() << std::endl;
        std::cout << "Mass is: " << cand.mass() << std::endl; 
        std::cout << "isUnique? " << hasUniqueDaughters(cand, i++, (*zCands)) << std::endl; 
        std::cout << "istrueZ? " << isTrueZ(cand) << std::endl; 
        std::cout << std::endl << std::endl;
    }
}
// ------------ method fills 'descriptions' with the allowed parameters for the module  ------------

bool 
ZCandTest::hasUniqueDaughters(const reco::Candidate& cand, 
                                   size_t idx,
                                   reco::CandidateView compCands) {
    for(size_t i = 0; i < idx; i++) {
        const reco::Candidate& prevCand = compCands[i];
        for(size_t j = 0; j < prevCand.numberOfDaughters(); j++) {
            const reco::Candidate& compCandDaughter = *prevCand.daughter(j);
            for(size_t k = 0; k < cand.numberOfDaughters(); k++) {
                const reco::Candidate& candDaughter = *cand.daughter(k);
                if ((compCandDaughter.pdgId() == candDaughter.pdgId())
                        && sameKinematics(compCandDaughter, candDaughter))
                    return false;    
            }
        }
    }
    return true;
}

const reco::Candidate& 
ZCandTest::getFirstDistinctMother(const reco::Candidate& cand) {
    reco::Candidate* mother = const_cast<reco::Candidate*>(&cand);
    while (mother->numberOfMothers() > 0 
            && mother->pdgId() == cand.pdgId())
        mother = const_cast<reco::Candidate*>(mother->mother(0));
    return *mother;
}
bool 
ZCandTest::sameKinematics(const reco::Candidate& cand1, 
                          const reco::Candidate& cand2) {
    return ((std::abs(cand1.pt() - cand2.pt()) < 0.001)
            && (std::abs(cand1.eta() - cand2.eta()) < 0.001)
            && (std::abs(cand1.phi() - cand2.phi()) < 0.001));
}
bool 
ZCandTest::isTrueZ(const reco::Candidate& zCand) {
    if (zCand.numberOfDaughters() != 2) {
        std::cout << "Invalid Z Candidate! Must be formed from two objects";
        exit(0);
    }
   // const reco::GenParticle& daughter1 =
   //     *dynamic_cast<const reco::GenParticle*>(zCand.daughter(0));
   // const reco::GenParticle& daughter2 =
   //     *dynamic_cast<const reco::GenParticle*>(zCand.daughter(1));
    const reco::Candidate& daughter1 = *zCand.daughter(0);
    const reco::Candidate& daughter2 = *zCand.daughter(1);
    if (daughter1.numberOfMothers() > 0 && daughter2.numberOfMothers() > 0) {
        const reco::Candidate& dau1mother = getFirstDistinctMother(daughter1);
        const reco::Candidate& dau2mother = getFirstDistinctMother(daughter2);
        std::cout << "daughter1 mother = " << dau1mother.pdgId() << std::endl;
        std::cout << "daughter2 mother = " << dau2mother.pdgId() << std::endl;
        std::cout << "same kinematics = " << sameKinematics(dau1mother, dau2mother);
        return ((daughter1.pdgId() + daughter2.pdgId() == 0) 
//                && daughter1.fromHardProcessFinalState()
//                && daughter2.fromHardProcessFinalState()
                && (dau1mother.pdgId() == dau2mother.pdgId())
                && sameKinematics(dau1mother, dau2mother));
    }
    std::cout << "Why don't the leptons have mothers?" << std::endl;
    return false;
    
}
void
ZCandTest::fillDescriptions(edm::ConfigurationDescriptions& descriptions) {
    //The following says we do not know what parameters are allowed so do no validation
    // Please change this to state exactly what you do use, even if it is no parameters
    edm::ParameterSetDescription desc;
    desc.setUnknown();
    descriptions.addDefault(desc);
}

DEFINE_FWK_MODULE(ZCandTest);
