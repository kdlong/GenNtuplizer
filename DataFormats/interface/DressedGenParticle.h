#ifndef DressedGenParticle_h
#define DressedGenParticle_h

#include "GenNtuplizer/DataFormats/interface/DressedGenParticleFwd.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"

class DressedGenParticle : public reco::GenParticle {
    public:
        DressedGenParticle() {}
        virtual ~DressedGenParticle();
        DressedGenParticle(const LeafCandidate & c) : 
            reco::GenParticle(c) { }
        DressedGenParticle(Charge q, const LorentzVector & p4, const Point & vtx, 
            int pdgId, int status, bool integerCharge);
        DressedGenParticle(Charge q, const PolarLorentzVector & p4, const Point & vtx, 
            int pdgId, int status, bool integerCharge);
        DressedGenParticle * clone() const;
    private:
        int dressParticle();
};

#endif
