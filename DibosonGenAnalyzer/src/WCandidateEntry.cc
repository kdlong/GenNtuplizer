#include "GenNtuplizer/DibosonGenAnalyzer/interface/WCandidateEntry.h"

WCandidateEntry::WCandidateEntry(std::string name, unsigned int nKeep) :
    BasicParticleEntry(name, nKeep, false) {}

bool 
WCandidateEntry::isTrueW(const reco::Candidate& wCand) {
    if (wCand.numberOfDaughters() != 2) {
        if (std::abs(wCand.pdgId()) == 24)
            return true;
        std::cerr << "Z candidate not formed from two objects";
        return false;
    }
    const reco::Candidate& daughter1 = *wCand.daughter(0);
    const reco::Candidate& daughter2 = *wCand.daughter(1);
    if (daughter1.numberOfMothers() > 0 && daughter2.numberOfMothers() > 0) {
        const reco::Candidate& dau1mother = getFirstDistinctMother(daughter1);
        const reco::Candidate& dau2mother = getFirstDistinctMother(daughter2);
        return ((abs(daughter1.pdgId() + daughter2.pdgId()) == 1) 
                && (dau1mother.pdgId() == dau2mother.pdgId())
                && sameKinematics(dau1mother, dau2mother));
    }
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

// Types A and B must implement X() and Y()
float
WCandidateEntry::masslessMT(const reco::Candidate::LorentzVector& a, 
            const reco::Candidate::LorentzVector& b) {
    float magA = std::sqrt(a.px()*a.px()+a.py()*a.py());
    float magB = std::sqrt(b.px()*b.px()+b.py()*b.py());
    return std::sqrt(2*(magA*magB-a.px()*b.px()-a.py()*b.py()));
}

void
WCandidateEntry::createNtupleEntry(TTree* ntuple) {
    BasicParticleEntry::createNtupleEntry(ntuple);
    isTrueWValues_.resize(nKeep_, -999);
    isUniqueValues_.resize(nKeep_, -999);
    masses_.resize(nKeep_, -999);
    mTsTrue_.resize(nKeep_, -999);
    mTsGenMET_.resize(nKeep_, -999);
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_;
        if (nKeep_ != 1)
            particleName += std::to_string(i);
        ntuple->Branch((particleName + "mass").c_str(), &masses_[i-1]);
        ntuple->Branch((particleName + "isUnique").c_str(), &isUniqueValues_[i-1]);
        ntuple->Branch((particleName + "isTrueW").c_str(), &isTrueWValues_[i-1]);
        ntuple->Branch((particleName + "MTtrue").c_str(), &mTsTrue_[i-1]);
        ntuple->Branch((particleName + "MTGenMET").c_str(), &mTsGenMET_[i-1]);
    }
}

void
WCandidateEntry::setGenMET(const reco::Candidate* genMet) {
    genMET_ = genMet;
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
        const reco::Candidate* lep = (0 || 
                std::abs(particle.daughter(0)->pdgId()) == 11 ||
                std::abs(particle.daughter(0)->pdgId()) == 13 ||
                std::abs(particle.daughter(0)->pdgId()) == 15
            ) ? particle.daughter(0) : particle.daughter(1);
       
        mTsGenMET_[i] = masslessMT(lep->p4(), genMET_->p4());
        mTsTrue_[i] = masslessMT(particle.daughter(0)->p4(), particle.daughter(1)->p4());
    }
}

