# https://leetcode.com/problems/minimum-size-subarray-sum/description/

class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = 0
        current_sum = 0
        min_length = float('inf')

        for right in range(len(nums)):
            current_sum += nums[right]

            while current_sum >= target:

                length = right - left + 1

                if length < min_length:
                    min_length = length

                current_sum -= nums[left]
                left += 1

        if min_length == float('inf'):
            return 0

        return min_length