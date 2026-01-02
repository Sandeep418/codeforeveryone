Acceptance: 26.6%
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

  # Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.

class Solution:
    def sum(self, nums: List[int]) -> List[int]:
        nums.sort()
        results=[]
        for i in range(len(nums)-2):
            if (i>0 and nums[i]==nums[i-1]):
                continue

            left=i+1;right=len(nums)-1
            while(left<right):
                s=nums[i]+nums[left]+nums[right]
                if s==0:
                    results.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while(left<right and  nums[left]==nums[left-1]):
                        left=left+1
                        #right--

                    while(left<right and  nums[right]==nums[right-1]):
                        right-=1
                        #left++
                elif s<0:
                    left+=1;
                else:
                    right-=1
        return results

            
            
            
