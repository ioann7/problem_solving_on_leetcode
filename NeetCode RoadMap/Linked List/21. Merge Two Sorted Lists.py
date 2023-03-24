# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# In the both solutions. Time complexity is O(n). Space complexity is O(n). Where `n` sum of two linked lists.
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val < list2.val:
                current.next = ListNode(list1.val)
                list1 = list1.next
            else:
                current.next = ListNode(list2.val)
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        else:
            current.next = list2
        return dummy.next


# My first solution. Here i am not create new nodes. 
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        def result_append(
                result: Optional[ListNode],
                linked_list: Optional[ListNode]) -> Tuple[Optional[ListNode]]:
            result.next = linked_list
            return result.next, linked_list.next

        if list1 and list2:
            if list1.val < list2.val:
                head = list1
                list1 = list1.next
            else:
                head = list2
                list2 = list2.next
        elif list1 and not list2:
            return list1
        else:
            return list2
        
        result = head
        while list1 and list2:
            if list1.val < list2.val:
                result, list1 = result_append(result, list1)
            else:
                result, list2 = result_append(result, list2)
        
        while list1:
            result, list1 = result_append(result, list1)
        while list2:
            result, list2 = result_append(result, list2)
        return head
