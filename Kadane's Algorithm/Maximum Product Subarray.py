# 152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        cur_max = nums[0]
        cur_min = nums[0]
        answer = nums[0]

        for num in nums[1:]:
            old_max = cur_max
            old_min = cur_min

            cur_max = max(
                num,
                num * old_max,
                num * old_min
            )

            cur_min = min(
                num,
                num * old_max,
                num * old_min
            )

            answer = max(answer, cur_max)

        return answer