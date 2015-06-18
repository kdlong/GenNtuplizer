class BasicParticleEntry {
    public:
        BasicParticleEntry(const reco::Candidate&);
        ~BasicParticleEntry();
        void addToNtuple(TFileService);
        void fillNtuple(TFileService);
    private:
        std::string name_;
        unsigned int num_;
        unsigned int nKeep_;
        std::vector<float> pts_;
        std::vector<float> etas_;
        std::vector<float> pdgids_;
}        
