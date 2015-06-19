#ifndef BASIC_PARTICLE_ENTRY_H
#define BASIC_PARTICLE_ENTRY_H

// system include files
#include <memory>
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "SimDataFormats/GeneratorProducts/interface/LHEEventProduct.h"
#include "FWCore/ServiceRegistry/interface/Service.h"
#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "DataFormats/HepMCCandidate/interface/GenParticle.h"
#include "DataFormats/Math/interface/deltaR.h"
#include "SimDataFormats/GeneratorProducts/interface/GenRunInfoProduct.h"


// user include files
#include "TTree.h"
//#include "FWCore/Framework/interface/Frameworkfwd.h"
//#include "DataFormats/Candidate/interface/Candidate.h"
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
