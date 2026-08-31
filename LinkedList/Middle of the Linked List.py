# https://leetcode.com/problems/middle-of-the-linked-list/description/

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        curr = head

        while curr != None:
            length += 1
            curr = curr.next

        mid = length // 2

        curr = head
        for i in range(mid):
            curr = curr.next

        return curr