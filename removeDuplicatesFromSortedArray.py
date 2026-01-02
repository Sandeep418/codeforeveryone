Remove Duplicates From Sorted Array
Easy
Acceptance: 46.6%
Given a sorted array nums, remove the duplicates in-place such that each element appears only once and returns the new length. Do not allocate extra space for another array; you must do this by modifying the input array in-place with O(1) extra memory.

# Note : -
# - Modify the function or parameters if needed.
# - Signatures function may vary, adjust parameters if required.
  Example 1:

Input: [1,1,2]
Output: 2
Explanation: Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.
Example 2:

Input: [0,0,1,1,1,2,2,3,3,4]
Output: 5

class Solution:
    def removeDuplicatesFromSortedArray(self, nums: List[int]) -> List[int]:

        k=1
        new=[]

        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k #nums[:k]             



        # flag=0
        # result=[]
        # for i in range(len(nums)-1):
        #     for j in range(i+1,len(nums)):
                
        #         if nums[i]==nums[j]:
        #             flag=1
        #             break
        #     if flag==0:
        #         result.append(nums[i])
        #     flag=0
        # return result            

