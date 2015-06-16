/* \class BestZCandSelector
 * 
 * Buit from example of LargestPtCandSelector
 * Keep the maxNumber biggest (in respect to Pt) Candidates from myCollection
 * Usage:
 *
 *
 *  module McPartonSele = BestZCandSelector {
 *      InputTag src     = myCollection
 *      uint32 maxNumber = 3    
 * } 
 *
 * \author: Kenneth Long, UW
 *
 */

#include "FWCore/Framework/interface/MakerMacros.h"
#include "CommonTools/UtilAlgos/interface/ObjectSelector.h"
#include "CommonTools/UtilAlgos/interface/SortCollectionSelector.h"
#include "GenNtuplizer/WZGenAnalyzer/interface/ZMassComparator.h"
#include "DataFormats/Candidate/interface/Candidate.h"

typedef ObjectSelector<
          SortCollectionSelector<
            reco::CandidateCollection,
            BestZCand<reco::Candidate>
          >
        > BestZCandSelector;

DEFINE_FWK_MODULE( BestZCandSelector );
