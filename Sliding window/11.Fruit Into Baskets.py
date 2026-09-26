# https://leetcode.com/problems/fruit-into-baskets/description/

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        ans = 0

        for right in range(len(fruits)):

            if fruits[right] in count:
                count[fruits[right]] += 1
            else:
                count[fruits[right]] = 1

            while len(count) > 2:

                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            window_size = right - left + 1

            if window_size > ans:
                ans = window_size

        return ans