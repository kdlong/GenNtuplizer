#include "GenNtuplizer/DibosonGenAnalyzer/interface/helpers.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

namespace helpers {
    bool isHardProcess(const reco::Candidate* particle) {
        if (const reco::GenParticle* part = dynamic_cast<const reco::GenParticle*>(particle))
            return part->isHardProcess();
        return -1;
    }
    bool fromHardProcessFinalState(const reco::Candidate* particle) {
        if (const reco::GenParticle* part = dynamic_cast<const reco::GenParticle*>(particle))
            return part->fromHardProcessFinalState();
        return -1;
    }

    const reco::Candidate& getFirstDistinctMother(const reco::Candidate& cand) {
        reco::Candidate* mother = const_cast<reco::Candidate*>(&cand);
        while (mother->numberOfMothers() > 0 
                && mother->pdgId() == cand.pdgId())
            mother = const_cast<reco::Candidate*>(mother->mother(0));
        return *mother;
    }

    bool sameKinematics(const reco::Candidate& cand1, 
                            const reco::Candidate& cand2) {
        return ((std::abs(cand1.pt() - cand2.pt()) < 0.001)
                && (std::abs(cand1.eta() - cand2.eta()) < 0.001)
                && (std::abs(cand1.phi() - cand2.phi()) < 0.001));
    }

    bool sameGenParticle(const reco::Candidate& cand1, 
                            const reco::Candidate& cand2) {
        return (cand1.pdgId() == cand2.pdgId() && sameKinematics(cand1, cand2));
    }
}
