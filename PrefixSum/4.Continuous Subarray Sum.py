# https://leetcode.com/problems/continuous-subarray-sum/description/

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:

        remainder_map = {0: -1}
        total = 0

        for i in range(len(nums)):
            total += nums[i]

            remainder = total % k

            if remainder in remainder_map:
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                remainder_map[remainder] = i

        return False