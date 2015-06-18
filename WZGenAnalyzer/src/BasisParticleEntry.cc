#include "BasicParticleEntry.h"

BasicParticleEntry::BasicParticleEntry(const std::string name, 
        const unsigned int nKeep) : 
            nKeep_ = nKeep, 
            name_ = name {}

void 
BasicParticleEntry::createNtupleEntry(TTree& ntuple) {
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_ + std::to_string(i);
        ntuple_->Branch((particleName + "Pt").c_str(), &pts_[i-1]);
        ntuple_->Branch((particleName + "Eta").c_str(), &etas_[i-1]);
        ntuple_->Branch((particleName + "pdgId").c_str(), &pdgids_[i-1]);
    }
    ntuple_->Branch((std::string("n") + name_).c_str(), &num_);
}
void
BasicParticleEntry::fillNtupleInfo() {
    etas_.clear();
    etas_.resize(nKeep_, -999);
    pts_.clear();
    pts_.resize(nKeep_, -999);
    pdgids_.clear();
    pdgids_.resize(nKeep_, -999);

    num_ = particles->size();
    for(size_t i = 0; i < particles->size(); i++) {
        if (i > nKeep_)
            break;
        const reco::Candidate& particle = (*particles)[i];
        pts_[i] = particle.pt();
        etas_[i] = particle.eta();
        pdgids_[i] = particle.pdgId();
    }
} 
void
BasicParticleEntry::setCollection(edm::Handle<reco::CandidateView> particles) {
    particles_ = particles;
}

