class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0

        for i in hashset:
            if i - 1 not in hashset:
                current = i
                length = 1

                while current + 1 in hashset:
                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest