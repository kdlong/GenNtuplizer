#include "GenNtuplizer/DibosonGenAnalyzer/interface/BasicParticleEntry.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "GenNtuplizer/DibosonGenAnalyzer/interface/helpers.h"

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
    phis_.resize(nKeep_, -999);
    if (storeGenInfo_) {
        statuses_.resize(nKeep_, -999);
        isHPvals_.resize(nKeep_, -999);
        fromHPFSvals_.resize(nKeep_, -999);
        pdgids_.resize(nKeep_, -999);
        motherIds_.resize(nKeep_, -999);
    }
    for (unsigned int i = 1; i <= nKeep_; i++)
    {
        std::string particleName = name_;
        if (nKeep_ != 1)
            particleName += std::to_string(i);
        ntuple->Branch((particleName + "Pt").c_str(), &pts_[i-1]);
        ntuple->Branch((particleName + "Eta").c_str(), &etas_[i-1]);
        ntuple->Branch((particleName + "Phi").c_str(), &phis_[i-1]);
        if (storeGenInfo_) {
            ntuple->Branch((particleName + "Status").c_str(), &statuses_[i-1]);
            ntuple->Branch((particleName + "fromHardProcessFS").c_str(), &fromHPFSvals_[i-1]);
            ntuple->Branch((particleName + "isHardProcess").c_str(), &isHPvals_[i-1]);
            ntuple->Branch((particleName + "pdgId").c_str(), &pdgids_[i-1]);
            ntuple->Branch((particleName + "motherId").c_str(), &motherIds_[i-1]);
        } 
    }
    ntuple->Branch((std::string("n") + name_).c_str(), &num_);
}

void
BasicParticleEntry::fillNtupleInfo() {
    etas_.assign(nKeep_, -999);
    pts_.assign(nKeep_, -999); 
    phis_.assign(nKeep_, -999); 
    if (storeGenInfo_) {
        statuses_.assign(nKeep_, -999); 
        isHPvals_.assign(nKeep_, -999);
        fromHPFSvals_.assign(nKeep_, -999);
        pdgids_.assign(nKeep_, -999);
        motherIds_.assign(nKeep_, -999);
    }
    num_ = particles_.size();
    for(size_t i = 0; i < particles_.size(); i++) {
        if (i == nKeep_)
            break;
        const reco::Candidate& particle = particles_[i];
        pts_[i] = particle.pt();
        etas_[i] = particle.eta();
        phis_[i] = particle.phi();
        if (storeGenInfo_) {
            statuses_[i] = particle.status();
            isHPvals_[i] = helpers::isHardProcess(&particle);
            fromHPFSvals_[i] = helpers::fromHardProcessFinalState(&particle);
            pdgids_[i] = particle.pdgId();
            motherIds_[i] = helpers::getFirstDistinctMother(particle).pdgId();
        }
    }
} 

void
BasicParticleEntry::setCollection(reco::CandidateCollection particles) {
    particles_ = particles;
}

void
BasicParticleEntry::setCollection(const reco::GenParticleCollection& particles) {
    for (const auto& particle : particles)
    particles_.push_back(particle);
}

void
BasicParticleEntry::setCollection(const reco::CompositeCandidateCollection& particles) {
    for (const auto& particle : particles)
    particles_.push_back(particle);
}

