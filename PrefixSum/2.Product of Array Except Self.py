# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        productbefore = 1
        productafter = 1

        for i in range(n):
            answer[i] = productbefore
            productbefore *= nums[i]

        for i in range(n - 1, -1, -1):
            answer[i] *= productafter
            productafter *= nums[i]

        return answer