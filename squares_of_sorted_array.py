'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Examples:
Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100]. After sorting, it becomes [0,1,9,16,100].
'''

class Solution:
    def squaresOfASortedArray(self, nums: List[int]) -> List[int]:
        results=[]
        for num in nums:
            n=num*num
            results.append(n)
        results.sort()  // o(n log(n))
        return results

// o(n)
from typing import List

class Solution:
    def squaresOfASortedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[pos] = nums[left] * nums[left]
                left += 1
            else:
                result[pos] = nums[right] * nums[right]
                right -= 1
            pos -= 1

        return result




