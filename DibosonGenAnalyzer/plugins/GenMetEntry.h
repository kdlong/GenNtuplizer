#ifndef GEN_MET_ENTRY_H
#define GEN_MET_ENTRY_H

#include "BasicParticleEntry.h"

class GenMetEntry : public BasicParticleEntry {
    public:
        GenMetEntry(std::string name); 
        void fillNtupleInfo();
        void createNtupleEntry(TTree* ntuple);
    private:
        std::vector<float> phis_;
};
#endif
