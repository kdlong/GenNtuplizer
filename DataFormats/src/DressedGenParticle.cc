#include "GenNtuplizer/DataFormats/interface/DressedGenParticle.h"
#include "DataFormats/Candidate/interface/CompositeRefCandidateT.h"
#include "DataFormats/Math/interface/deltaR.h"

void DressedGenParticle::dressParticle() {
    this->setP4(p4_undressed);
    for (const auto& associated : associates) {
        this->setP4(this->p4() + associated.p4());
    }
}
DressedGenParticle::~DressedGenParticle() { }

DressedGenParticle::DressedGenParticle( Charge q, const LorentzVector & p4, 
              const Point & vtx, int pdgId, int status, bool integerCharge ) : 
    reco::GenParticle( q, p4, vtx, pdgId, status, integerCharge ),
    p4_undressed(p4) {
}
DressedGenParticle::DressedGenParticle( Charge q, const PolarLorentzVector & p4, 
              const Point & vtx, int pdgId, int status, bool integerCharge ) : 
    reco::GenParticle( q, p4, vtx, pdgId, status, integerCharge ), 
    p4_undressed(p4) {
}
DressedGenParticle::DressedGenParticle(const reco::GenParticle& cand, 
    const reco::GenParticleCollection assocCollection, 
    const float dRmax) :
        reco::GenParticle(cand), p4_undressed(cand.p4()) {
    for (const auto& associated : assocCollection) {
        if (reco::deltaR(cand.p4(), associated.p4()) < dRmax) {
            this->setP4(this->p4() + associated.p4());
            associates.push_back(associated);
        }
    }
}
DressedGenParticle* DressedGenParticle::clone() const {
    return new DressedGenParticle( * this );
}
const reco::Candidate::LorentzVector DressedGenParticle::undressedP4() const {
    return p4_undressed;
}
float DressedGenParticle::undressedPt() const {
    return p4_undressed.pt();
}
float DressedGenParticle::numAssociated() const {
    return associates.size();
}
reco::GenParticleCollection DressedGenParticle::getAssociated() const {
    return associates;
}
bool DressedGenParticle::dissociate(const reco::GenParticle& associated) {
    if (!isAssociated(associated)) {
        return false;
    }
    return true;
//    associates.erase(std::remove(associates.begin(), 
//        associates.end(), associated), associates.end());
//    this->setP4(this->p4() - associated.p4());
//    return true;
}
bool DressedGenParticle::isAssociated(reco::GenParticle associated) const{
    return true;
    //return (std::find(associates.begin(), associates.end(), 
    //    associated) != associates.end());
}
