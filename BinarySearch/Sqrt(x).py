# https://leetcode.com/problems/sqrtx/description/

class Solution:
    def mySqrt(self, x: int) -> int:
        if x <2:
            return x

        left=1
        right = x // 2

        while left<=right:
            mid = (left+right)//2

            sqr = mid*mid
            if sqr == x:
                return mid
            elif sqr < x:
                left = mid+1
            else:
                right = right-1
        return right
            