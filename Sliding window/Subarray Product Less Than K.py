# https://leetcode.com/problems/subarray-product-less-than-k/description/

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
           return 0

        n = len(nums)
        left = 0
        product = 1
        count=0
        
        for right in range(n):
            product*= nums[right]

            while product>=k:
                product//=nums[left]
                left+=1

            count +=right - left +1
        return count