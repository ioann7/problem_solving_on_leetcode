# https://leetcode.com/problems/add-two-numbers/


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def add_two_numbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        current_node = head
        accumulation = 0
        while l1 or l2 or accumulation:
            first_number = l1.val if l1 else 0
            second_number = l2.val if l2 else 0
            accumulation, value  = divmod(first_number + second_number + accumulation, 10)
            current_node.next = ListNode(value)
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head.next
