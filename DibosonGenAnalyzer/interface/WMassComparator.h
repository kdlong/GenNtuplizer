#ifndef WMassComparator_h
#define WMassComparator_h
/** \class PtComparator
 *
 * compare by pt
 * 
 * \author Luca Lista, INFN
 *         numeric safe implementation by Fedor Ratnikov, FNAL
 *
 * \version $Revision: 1.4 $
 *
 * $Id: PtComparator.h,v 1.4 2007/04/23 20:54:26 llista Exp $
 *
 */

const float WMASS = 80.385;

template<typename T>
struct BestWCand {
  typedef T first_argument_type;
  typedef T second_argument_type;
  bool operator()( const T & t1, const T & t2 ) const {
    return std::abs(t1.mass() - WMASS) < std::abs(t2.mass() - WMASS);
  }
};

template<typename T>
struct WorstWCand {
  typedef T first_argument_type;
  typedef T second_argument_type;
  bool operator()( const T & t1, const T & t2 ) const {
    return std::abs(t1.mass() - WMASS) > std::abs(t2.mass() - WMASS);
  }
};
#endif
