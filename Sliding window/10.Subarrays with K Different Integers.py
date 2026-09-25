# https://leetcode.com/problems/subarrays-with-k-different-integers/description/

class Solution:
    def subarraysWithKDistinct(self, nums, k):

        def atMost(k):
            count = {}
            left = 0
            ans = 0

            for right in range(len(nums)):

                if nums[right] in count:
                    count[nums[right]] += 1
                else:
                    count[nums[right]] = 1

                while len(count) > k:

                    count[nums[left]] -= 1

                    if count[nums[left]] == 0:
                        del count[nums[left]]

                    left += 1

                ans += right - left + 1

            return ans

        return atMost(k) - atMost(k - 1)