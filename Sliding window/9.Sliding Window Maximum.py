# https://leetcode.com/problems/sliding-window-maximum/description/


#Sliding window way - But it will not pass all test cases , hence we need to solve using queue
# class Solution:
#     def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
#         n = len(nums)
#         left = 0
#         res = []

#         for right in range(n):
#             if  right - left+1 == k:
#                 maximum = nums[left]

#                 for i in range(left , right+1):
#                     maximum = max(maximum , nums[i])

#                 res.append(maximum)
#                 left+=1
#         return res


from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        left = 0
        dq = deque()
        res = []

        for right in range(len(nums)):

            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            if dq[0] < left:
                dq.popleft()

            if right - left + 1 == k:
                res.append(nums[dq[0]])
                left += 1

        return res
        