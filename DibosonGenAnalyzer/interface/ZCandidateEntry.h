#ifndef Z_CANDIDATE_ENTRY_H
#define Z_CANDIDATE_ENTRY_H

#include "GenNtuplizer/DibosonGenAnalyzer/interface/BasicParticleEntry.h"

class ZCandidateEntry : public BasicParticleEntry {
    public:
        ZCandidateEntry(std::string name, unsigned int nKeep);
        bool hasUniqueDaughters(const reco::Candidate& cand, 
                               size_t idx,
                               reco::CandidateCollection compCands);
        bool isTrueDecay(const reco::Candidate& zCand);
        bool isRadiated(const reco::Candidate& zCand);
        void createNtupleEntry(TTree* ntuple);
        void fillNtupleInfo();
    private:
        std::vector<int> isTrueDecayValues_;
        std::vector<int> isRadiatedValues_;
        std::vector<int> isUniqueValues_;
        std::vector<float> masses_;
};
#endif
