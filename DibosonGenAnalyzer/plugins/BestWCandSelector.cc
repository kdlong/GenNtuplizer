/* \class BestWCandSelector
 * 
 * Buit from example of LargestPtCandSelector
 * Keep the maxNumber biggest (in respect to Pt) Candidates from myCollection
 * Usage:
 *
 *
 *  module McPartonSele = BestWCandSelector {
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
#include "GenNtuplizer/DibosonGenAnalyzer/interface/WMassComparator.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "DataFormats/Candidate/interface/CompositeCandidate.h"

typedef ObjectSelector<
          SortCollectionSelector<
            reco::CandidateCollection,
            BestWCand<reco::Candidate>
          >
        > BestWCandSelector;

DEFINE_FWK_MODULE( BestWCandSelector );
