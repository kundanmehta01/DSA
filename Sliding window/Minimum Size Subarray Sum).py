209. Minimum Size Subarray Sum (https://leetcode.com/problems/minimum-size-subarray-sum/)
Solved
Medium
Topics
premium lock icon
Companies
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window_sum = 0
        minimum = float('inf')

        for right in range(len(nums)):
            window_sum += nums[right]

            while window_sum >= target:
                minimum = min(minimum, right - left + 1)

                window_sum -= nums[left]
                left += 1

        if minimum == float('inf'):
            return 0

        return minimum
 
