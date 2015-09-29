#include "ZCandidateEntry.h"

ZCandidateEntry::ZCandidateEntry(std::string name, unsigned int nKeep) :
    BasicParticleEntry(name, nKeep, false) {}

bool 
ZCandidateEntry::isTrueZ(const reco::Candidate& zCand) {
    if (zCand.numberOfDaughters() != 2) {
        if (zCand.pdgId() == 23)
            return true;
        std::cerr << "Z candidate not formed from two objects";
        return false;
    }
    const reco::Candidate& daughter1 = *zCand.daughter(0);
    const reco::Candidate& daughter2 = *zCand.daughter(1);
    if (daughter1.numberOfMothers() > 0 && daughter2.numberOfMothers() > 0) {
        const reco::Candidate& dau1mother = getFirstDistinctMother(daughter1);
        const reco::Candidate& dau2mother = getFirstDistinctMother(daughter2);
        return ((daughter1.pdgId() + daughter2.pdgId() == 0) 
//                && daughter1.fromHardProcessFinalState()
//                && daughter2.fromHardProcessFinalState()
                && (dau1mother.pdgId() == dau2mother.pdgId())
                && sameKinematics(dau1mother, dau2mother));
    }
    std::cout << "Why don't the leptons have mothers?" << std::endl;
    return false;    
}

bool 
ZCandidateEntry::hasUniqueDaughters(const reco::Candidate& cand, 
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
ZCandidateEntry::createNtupleEntry(TTree* ntuple) {
    BasicParticleEntry::createNtupleEntry(ntuple);
    isTrueZValues_.resize(nKeep_, -999);
    isUniqueValues_.resize(nKeep_, -999);
    masses_.resize(nKeep_, -999);
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_;
        if (nKeep_ != 1)
            particleName += std::to_string(i);
        ntuple->Branch((particleName + "mass").c_str(), &masses_[i-1]);
        ntuple->Branch((particleName + "isUnique").c_str(), &isUniqueValues_[i-1]);
        ntuple->Branch((particleName + "isTrueZ").c_str(), &isTrueZValues_[i-1]);
    }
}
void
ZCandidateEntry::fillNtupleInfo() {
    BasicParticleEntry::fillNtupleInfo();
    isUniqueValues_.assign(nKeep_, -999);
    isTrueZValues_.assign(nKeep_, -999); 
    masses_.assign(nKeep_, -999); 
    
    for(size_t i = 0; i < particles_.size(); i++) {
        if (i == nKeep_)
            break;
        const reco::Candidate& particle = particles_[i];
        isUniqueValues_[i] = hasUniqueDaughters(particle, i, particles_);
        isTrueZValues_[i] = isTrueZ(particle);
        masses_[i] = particle.mass();
    }
}

