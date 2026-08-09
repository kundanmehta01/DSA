 643. Maximum Average Subarray I (https://leetcode.com/problems/maximum-average-subarray-i/description/)

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n=len(nums)
        w=0
        for i in range(k):
            w+=nums[i]

        ans=w

        for i in range(k,n):
            w+=nums[i]
            w-=nums[i-k]
            ans=max(ans,w)
        return ans/k


