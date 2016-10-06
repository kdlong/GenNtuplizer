#ifndef W_CANDIDATE_ENTRY_H
#define W_CANDIDATE_ENTRY_H

#include "GenNtuplizer/DibosonGenAnalyzer/interface/BasicParticleEntry.h"
#include "DataFormats/METReco/interface/GenMET.h"

class WCandidateEntry : public BasicParticleEntry {
    public:
        WCandidateEntry(std::string name, unsigned int nKeep);
        bool hasUniqueDaughters(const reco::Candidate& cand, 
                               size_t idx,
                               reco::CandidateCollection compCands);
        bool isTrueW(const reco::Candidate& zCand);
        void setGenMET(const reco::Candidate* genMet);
        void createNtupleEntry(TTree* ntuple);
        void fillNtupleInfo();
    private:
        std::vector<int> isTrueWValues_;
        std::vector<int> isUniqueValues_;
        std::vector<float> masses_;
        std::vector<float> mTsTrue_;
        std::vector<float> mTsGenMET_;
        const reco::Candidate* genMET_;
        float masslessMT(const reco::Candidate::LorentzVector& a, 
            const reco::Candidate::LorentzVector& b);
};
#endif
