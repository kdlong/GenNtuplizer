#ifndef HELPERS_H
#define HELPERS_H

#include "DataFormats/Candidate/interface/Candidate.h"

namespace helpers {
    bool isHardProcess(const reco::Candidate* particle);
    bool fromHardProcessFinalState(const reco::Candidate* particle);
    const reco::Candidate& getFirstDistinctMother(const reco::Candidate& cand);
    bool sameKinematics(const reco::Candidate& cand1, const reco::Candidate& cand2);
    bool sameGenParticle(const reco::Candidate& cand1, const reco::Candidate& cand2);
}

#endif
