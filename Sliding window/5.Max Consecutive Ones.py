# https://leetcode.com/problems/max-consecutive-ones/description/

class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        window = 0
        ans = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                window += 1
                ans = max(ans, window)
            else:
                window = 0

        return ans