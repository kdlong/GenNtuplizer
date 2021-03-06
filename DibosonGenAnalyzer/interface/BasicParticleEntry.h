#ifndef BASIC_PARTICLE_ENTRY_H
#define BASIC_PARTICLE_ENTRY_H

// system include files
#include <memory>
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/PatCandidates/interface/CompositeCandidate.h"
// user include files
#include "TTree.h"
#include <vector>
#include <string>

class BasicParticleEntry {
    public:
        BasicParticleEntry();
        BasicParticleEntry(std::string name, unsigned int nKeep, bool);
        ~BasicParticleEntry();
        void setCollection(reco::CandidateCollection);
        void setCollection(const reco::GenParticleCollection& cands);
        void setCollection(const reco::CompositeCandidateCollection& cands);
        void createNtupleEntry(TTree* ntuple);
        void fillNtupleInfo();
    protected:
        reco::CandidateCollection particles_;
        std::string name_;
        unsigned int num_;
        unsigned int nKeep_;
        bool storeGenInfo_;
        std::vector<float> pts_;
        std::vector<float> etas_;
        std::vector<float> phis_;
        std::vector<int> statuses_;
        std::vector<int> pdgids_;
        std::vector<int> motherIds_;
        std::vector<int> isHPvals_;
        std::vector<int> fromHPFSvals_;
};

#endif
