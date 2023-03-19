from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Here is my first idea
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
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
