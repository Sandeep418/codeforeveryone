'''
3Sum Closest
Medium
Acceptance: 45.8%
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Examples:
Example 1:

Input: [-1,2,1,-4], 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
'''

class Solution:
    def sumClosest(self, nums: List[int], target: int) -> List[int]:

        nums.sort()
        closet_sum=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):

            left=i+1
            right=len(nums)-1
            while(left<right):
                s=nums[i]+nums[left]+nums[right]

                if abs(target-s)<abs(target-closet_sum):
                    closet_sum=s
                
                if s<target:
                    left+=1
                elif s>target:
                    right-=1
                else:
                    return s
        return closet_sum
