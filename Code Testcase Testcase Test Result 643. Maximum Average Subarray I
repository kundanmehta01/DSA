643. Maximum Average Subarray I
Solved
Easy
Topics
premium lock icon
Companies
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        ans=0
        left=0
        maximum = float('-inf')

        for right in range(len(nums)):
            ans += nums[right]

            if right-left+1 ==k:
                maximum=max(maximum , ans/k)

                ans-=nums[left]
                left+=1
        return maximum


