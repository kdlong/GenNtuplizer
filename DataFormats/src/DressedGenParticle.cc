#include "GenNtuplizer/DataFormats/interface/DressedGenParticle.h"
#include "DataFormats/Candidate/interface/CompositeRefCandidateT.h"

int DressedGenParticle::dressParticle() {
    return 0;
}
DressedGenParticle::~DressedGenParticle() { }

DressedGenParticle::DressedGenParticle( Charge q, const LorentzVector & p4, 
              const Point & vtx, int pdgId, int status, bool integerCharge ) : 
    reco::GenParticle( q, p4, vtx, pdgId, status, integerCharge ) {
}

DressedGenParticle::DressedGenParticle( Charge q, const PolarLorentzVector & p4, 
              const Point & vtx, int pdgId, int status, bool integerCharge ) : 
    reco::GenParticle( q, p4, vtx, pdgId, status, integerCharge ) {
}
DressedGenParticle* DressedGenParticle::clone() const {
  return new DressedGenParticle( * this );
}
