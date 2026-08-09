26. Remove Duplicates from Sorted Array (https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        l=0

        for i in range (len(nums)):
            if nums[i]!=nums[k-1]:
                nums[i],nums[k]=nums[k],nums[i]
                k+=1
        return k
