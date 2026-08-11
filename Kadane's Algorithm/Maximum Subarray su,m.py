# 53. Maximum Subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current =0
        largest=float("-inf")

        

        for  i in range(len(nums)):
            current +=nums[i]
            largest = max(largest , current)

            if current<0:
                current=0
        return largest