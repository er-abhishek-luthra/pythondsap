from typing import List

"""
Problem Statement #
Given a list of intervals, merge all the overlapping intervals to produce a list that has only mutually exclusive intervals.

Example 1:

Intervals: [[1,4], [2,5], [7,9]]
Output: [[1,5], [7,9]]
Explanation: Since the first two intervals [1,4] and [2,5] overlap, we merged them into
one [1,5].

Example 2:

Intervals: [[6,7], [2,4], [5,9]]
Output: [[2,4], [5,9]]
Explanation: Since the intervals [6,7] and [5,9] overlap, we merged them into one [5,9].

Example 3:

Intervals: [[1,4], [2,6], [3,5]]
Output: [[1,6]]
Explanation: Since all the given intervals overlap, we merged them into one.
"""

class Interval :
    def __init__(self, start,end) :
        self.start = start
        self.end = end

    def __repr__(self):
        return f"({self.start} , {self.end})"
    
    def __eq__(self, other):
        if(isinstance(other,Interval)):
            return other.start == self.start and other.end == self.end 
        return False
    

def merge_intervals(interval_list : List[Interval]) -> List[Interval] :
    """
    merge the list of overlapping intervals. An interval is defined as overlapping interval if the start
    of the interval falls before the end of the interval 

    Parameters:
    interval_list ( List[Interval]) : The list of intervals ( in unsorted format)

    Return:
    List[Interval] : The list with non overlapping merged intervals
    """
    interval_list.sort(key = lambda x: x.start)
    merged_list = []
    active_interval = None
    for i in range(len(interval_list)):
        if active_interval == None : 
            active_interval = interval_list[i]
        else :
            next_interval = interval_list[i]
            if next_interval.start < active_interval.end :
                active_interval.end = next_interval.end
            else : 
                merged_list.append(active_interval)
                active_interval = next_interval

    if  active_interval != None :
        merged_list.append(active_interval)

    return merged_list

if __name__ == '__main__':
    # Create a list of intervals
    intervals = [Interval(1, 3), Interval(8, 10), Interval(15, 18), Interval(2, 6), Interval(17, 20)]

    # Call the merge_intervals function
    merged_intervals = merge_intervals(intervals)
    print(merged_intervals)
