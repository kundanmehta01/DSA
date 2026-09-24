# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/

class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        n=len(nums)
        window = 0
        freq={}
        ans=0

        for i in range(k):
            window+=nums[i]
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1

        if len(freq)==k:
            ans = window

        for i in range(k,n):
            window+=nums[i]

            if nums[i] in freq:
                freq[nums[i]] += 1
            else:
                freq[nums[i]] = 1

            window-=nums[i-k]
            freq[nums[i-k]] -=1 

            if freq[nums[i-k]] == 0:
                del freq[nums[i-k]]

            if len(freq)==k:
                 ans = max(ans , window)

        return ans
