# https://leetcode.com/problems/swap-nodes-in-pairs/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n). Space complexity O(1).
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prev, first = dummy, head
        while first and first.next:
            third = first.next.next
            second = first.next

            first.next = third
            second.next = first
            prev.next = second

            prev = first
            first = third
        return dummy.next
