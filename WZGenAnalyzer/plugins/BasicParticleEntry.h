#ifndef BASIC_PARTICLE_ENTRY_H
#define BASIC_PARTICLE_ENTRY_H

// system include files
#include <memory>
#include "DataFormats/Candidate/interface/Candidate.h"
// user include files
#include "TTree.h"
#include <vector>
#include <string>

class BasicParticleEntry {
    public:
        BasicParticleEntry();
        BasicParticleEntry(std::string name, unsigned int nKeep);
        ~BasicParticleEntry();
        void setCollection(reco::CandidateView);
        void createNtupleEntry(TTree* ntuple);
        void fillNtupleInfo();
    private:
        reco::CandidateView particles_;
        std::string name_;
        unsigned int num_;
        unsigned int nKeep_;
        std::vector<float> pts_;
        std::vector<float> etas_;
        std::vector<float> pdgids_;
};

#endif
