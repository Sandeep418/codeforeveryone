***
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Examples:
Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Merge intervals [1,3] and [2,6] into [1,6].
***
# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

from typing import List 

class Solution:
    def mergeIntervals(self, nums: List[int]) -> List[int]:

        nums.sort(key=lambda x : x[0])

        prev_end=[nums[0]]

        for st,en in nums[1:]:

            prev_end_last_element=prev_end[-1][1]

            if st<=prev_end_last_element:

                prev_end[-1][1]=max(prev_end_last_element,en)
            else:

                prev_end.append([st,en])

        return prev_end



        
