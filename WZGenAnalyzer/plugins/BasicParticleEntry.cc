#include "BasicParticleEntry.h"

BasicParticleEntry::BasicParticleEntry(std::string name, 
        unsigned int nKeep) : 
            name_(name),
            nKeep_(nKeep) {}

//BasicParticleEntry::BasicParticleEntry() {
//    BasicParticleEntry("",0);
//}

void
BasicParticleEntry::createNtupleEntry(TTree* ntuple) {
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_ + std::to_string(i);
        ntuple->Branch((particleName + "Pt").c_str(), &pts_[i-1]);
        ntuple->Branch((particleName + "Eta").c_str(), &etas_[i-1]);
        ntuple->Branch((particleName + "pdgId").c_str(), &pdgids_[i-1]);
    }
    ntuple->Branch((std::string("n") + name_).c_str(), &num_);
}
void
BasicParticleEntry::fillNtupleInfo() {
    etas_.clear();
    etas_.resize(nKeep_, -999);
    pts_.clear();
    pts_.resize(nKeep_, -999);
    pdgids_.clear();
    pdgids_.resize(nKeep_, -999);

    num_ = particles_.size();
    for(size_t i = 0; i < particles_.size(); i++) {
        if (i > nKeep_)
            break;
        const reco::Candidate& particle = particles_[i];
        pts_[i] = particle.pt();
        etas_[i] = particle.eta();
        pdgids_[i] = particle.pdgId();
    }
} 
void
BasicParticleEntry::setCollection(reco::CandidateView particles) {
    particles_ = particles;
}

