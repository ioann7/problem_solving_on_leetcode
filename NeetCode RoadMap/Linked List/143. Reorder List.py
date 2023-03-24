# https://leetcode.com/problems/reorder-list

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Time complexity O(n). Space complexity O(1)
class Solution:
    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: Optional[ListNode]) -> None:
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

    def merge_lists(self, first: Optional[ListNode], second: Optional[ListNode]) -> None:
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
    
        middle = self.find_middle(head)
        second_list = middle.next
        middle.next = None
        reversed_second_list = self.reverse_list(second_list)
        self.merge_lists(head, reversed_second_list)


# my first version
class Solution:
    def find_middle(self, head: ListNode) -> ListNode:
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def reverse_list(self, head: Optional[ListNode]) -> None:
        previous, current = None, head
        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
        return previous

    def merge_lists(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> None:
        dummy = ListNode()
        tail = dummy
        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = None
            head2.next = None
            tail.next = head1
            tail.next.next = head2
            tail = tail.next.next
            head1 = temp1
            head2 = temp2
        if head1:
            tail.next = head1
        elif head2:
            tail.next = head2

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head
    
        middle = self.find_middle(head)
        second_list = middle.next
        middle.next = None
        reversed_second_list = self.reverse_list(second_list)
        self.merge_lists(head, reversed_second_list)
