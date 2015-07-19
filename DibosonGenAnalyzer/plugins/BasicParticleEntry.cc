#include "BasicParticleEntry.h"

BasicParticleEntry::BasicParticleEntry(std::string name, 
        unsigned int nKeep, 
        bool storeGenInfo) : 
            name_(name),
            nKeep_(nKeep),
            storeGenInfo_(storeGenInfo) {}

//BasicParticleEntry::BasicParticleEntry() {
//    BasicParticleEntry("",0);
//}

void
BasicParticleEntry::createNtupleEntry(TTree* ntuple) {
    etas_.resize(nKeep_, -999);
    pts_.resize(nKeep_, -999);
    if (storeGenInfo_) {
        pdgids_.resize(nKeep_, -999);
        motherIds_.resize(nKeep_, -999);
    }
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_ + std::to_string(i);
        ntuple->Branch((particleName + "Pt").c_str(), &pts_[i-1]);
        ntuple->Branch((particleName + "Eta").c_str(), &etas_[i-1]);
        if (storeGenInfo_) {
            ntuple->Branch((particleName + "pdgId").c_str(), &motherIds_[i-1]);
            ntuple->Branch((particleName + "motherId").c_str(), &motherIds_[i-1]);
        } 
    }
    ntuple->Branch((std::string("n") + name_).c_str(), &num_);
}
void
BasicParticleEntry::fillNtupleInfo() {
    etas_.clear();
    etas_.resize(nKeep_, -999);
    pts_.clear();
    pts_.resize(nKeep_, -999); 
    if (storeGenInfo_) {
        pdgids_.clear();
        pdgids_.resize(nKeep_, -999);
        motherIds_.clear();
        motherIds_.resize(nKeep_, -999);
    }
    num_ = particles_.size();
    for(size_t i = 0; i < particles_.size(); i++) {
        if (i == nKeep_)
            break;
        const reco::Candidate& particle = particles_[i];
        pts_[i] = particle.pt();
        etas_[i] = particle.eta();
        if (storeGenInfo_) {
            pdgids_[i] = particle.pdgId();
            motherIds_[i] = getFirstDistinctMother(particle).pdgId();
        }
    }
} 
void
BasicParticleEntry::setCollection(reco::CandidateCollection particles) {
    particles_ = particles;
}

const reco::Candidate& 
BasicParticleEntry::getFirstDistinctMother(const reco::Candidate& cand) {
    reco::Candidate* mother = const_cast<reco::Candidate*>(&cand);
    while (mother->numberOfMothers() > 0 
            && mother->pdgId() == cand.pdgId())
        mother = const_cast<reco::Candidate*>(mother->mother(0));
    return *mother;
}