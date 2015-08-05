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
        BasicParticleEntry(std::string name, unsigned int nKeep, bool);
        ~BasicParticleEntry();
        bool sameKinematics(const reco::Candidate& cand1, 
                            const reco::Candidate& cand2);
        void setCollection(reco::CandidateCollection);
        void createNtupleEntry(TTree* ntuple);
        void fillNtupleInfo();
        const reco::Candidate& getFirstDistinctMother(const reco::Candidate& cand);
    protected:
        reco::CandidateCollection particles_;
        std::string name_;
        unsigned int num_;
        unsigned int nKeep_;
        bool storeGenInfo_;
        std::vector<float> pts_;
        std::vector<float> etas_;
        std::vector<int> pdgids_;
        std::vector<int> motherIds_;
};

#endif
