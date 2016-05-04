#ifndef W_CANDIDATE_ENTRY_H
#define W_CANDIDATE_ENTRY_H

#include "GenNtuplizer/DibosonGenAnalyzer/interface/BasicParticleEntry.h"

class WCandidateEntry : public BasicParticleEntry {
    public:
        WCandidateEntry(std::string name, unsigned int nKeep);
        bool hasUniqueDaughters(const reco::Candidate& cand, 
                               size_t idx,
                               reco::CandidateCollection compCands);
        bool isTrueW(const reco::Candidate& zCand);
        void createNtupleEntry(TTree* ntuple);
        void fillNtupleInfo();
    private:
        std::vector<int> isTrueWValues_;
        std::vector<int> isUniqueValues_;
        std::vector<float> masses_;
};
#endif
