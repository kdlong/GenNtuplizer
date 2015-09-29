#include "GenMetEntry.h"
#include "DataFormats/PatCandidates/interface/MET.h"

GenMetEntry::GenMetEntry(std::string name) :
    BasicParticleEntry(name, 1, false) {}

void
GenMetEntry::fillNtupleInfo() {
    phis_.assign(nKeep_, -999);
    pts_.assign(nKeep_, -999); 
    num_ = particles_.size();
    
    const pat::MET& particle = static_cast<const pat::MET&>(particles_[0]);
    pts_[0] = particle.genMET()->pt();
    phis_[0] = particle.genMET()->pt();
} 

void
GenMetEntry::createNtupleEntry(TTree* ntuple) {
    pts_.resize(nKeep_, -999);
    phis_.resize(nKeep_, -999);
    
    std::string particleName = name_;
    ntuple->Branch((particleName + "Pt").c_str(), &pts_[0]);
    ntuple->Branch((particleName + "Phi").c_str(), &phis_[0]);
    ntuple->Branch((std::string("n") + name_).c_str(), &num_);
}
