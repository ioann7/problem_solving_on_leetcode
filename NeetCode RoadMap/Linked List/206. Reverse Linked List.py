from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Here is my first idea. Time complexity O(n); Space complexity O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        son = None
        next_node = head.next if head else None
        while next_node:
            next_node = head.next
            head.next = son
            son = head
            head = next_node if next_node else head
        return head


# Here is neetcode idea which looks prettier to me
# Using two pointers. Time complexity O(n); Space complexity O(1)
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous
