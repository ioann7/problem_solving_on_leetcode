# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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
