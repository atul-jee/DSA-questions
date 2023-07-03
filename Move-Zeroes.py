# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.
# Leetcode Move Zeroes
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        j=0
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[j]=nums[j],nums[i]
                j+=1