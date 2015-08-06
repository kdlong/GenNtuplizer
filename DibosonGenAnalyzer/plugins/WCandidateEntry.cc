#include "WCandidateEntry.h"

WCandidateEntry::WCandidateEntry(std::string name, unsigned int nKeep) :
    BasicParticleEntry(name, nKeep, false) {}

bool 
WCandidateEntry::isTrueW(const reco::Candidate& wCand) {
    if (wCand.numberOfDaughters() != 2) {
        std::cout << "Invalid Z Candidate! Must be formed from two objects";
        exit(0);
    }
    const reco::Candidate& daughter1 = *wCand.daughter(0);
    const reco::Candidate& daughter2 = *wCand.daughter(1);
    if (daughter1.numberOfMothers() > 0 && daughter2.numberOfMothers() > 0) {
        const reco::Candidate& dau1mother = getFirstDistinctMother(daughter1);
        const reco::Candidate& dau2mother = getFirstDistinctMother(daughter2);
        return ((abs(daughter1.pdgId() + daughter2.pdgId()) == 1) 
//                && daughter1.fromHardProcessFinalState()
//                && daughter2.fromHardProcessFinalState()
                && (dau1mother.pdgId() == dau2mother.pdgId())
                && sameKinematics(dau1mother, dau2mother));
    }
    std::cout << "Why don't the leptons have mothers?" << std::endl;
    return false;    
}

bool 
WCandidateEntry::hasUniqueDaughters(const reco::Candidate& cand, 
                              size_t idx,
                              reco::CandidateCollection compCands) {
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

void
WCandidateEntry::createNtupleEntry(TTree* ntuple) {
    BasicParticleEntry::createNtupleEntry(ntuple);
    isTrueWValues_.resize(nKeep_, -999);
    isUniqueValues_.resize(nKeep_, -999);
    masses_.resize(nKeep_, -999);
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_ + std::to_string(i);
        ntuple->Branch((particleName + "mass").c_str(), &masses_[i-1]);
        ntuple->Branch((particleName + "isUnique").c_str(), &isUniqueValues_[i-1]);
        ntuple->Branch((particleName + "isTrueW").c_str(), &isTrueWValues_[i-1]);
    }
}
void
WCandidateEntry::fillNtupleInfo() {
    BasicParticleEntry::fillNtupleInfo();
    isUniqueValues_.assign(nKeep_, -999);
    isTrueWValues_.assign(nKeep_, -999); 
    masses_.assign(nKeep_, -999); 
    
    for(size_t i = 0; i < particles_.size(); i++) {
        if (i == nKeep_)
            break;
        const reco::Candidate& particle = particles_[i];
        isUniqueValues_[i] = hasUniqueDaughters(particle, i, particles_);
        isTrueWValues_[i] = isTrueW(particle);
        masses_[i] = particle.mass();
    }
}

