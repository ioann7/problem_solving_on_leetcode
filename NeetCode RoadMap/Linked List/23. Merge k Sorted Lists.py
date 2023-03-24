# https://leetcode.com/problems/merge-k-sorted-lists

from typing import List, Optional


# Solution for time complexity O(N*logK). And space complexity O(K) because we use recursion
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.merge(lists, 0, len(lists) - 1)
    
    def merge(self, lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return lists[left]
        middle = (left + right) // 2
        left_list = self.merge(lists, left, middle)
        right_list = self.merge(lists, middle + 1, right)
        return self.merge_two_lists(left_list, right_list)

    def merge_two_lists(self, list1: Optional[ListNode],
                        list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next


# Solution for time complexity O(N * K).
class Solution:
    def merge_lists(self, list1: Optional[ListNode],
                    list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        else:
            tail.next = list2
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        elif len(lists) == 1:
            return lists[0]
        first = lists[0]
        for second in lists[1:]:
            first = self.merge_lists(first, second)
        return first


# Solution for time complexity O(N * K)
class Solution:
    def getMinIndex(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_value = float('inf')
        min_index = None
        for index, list_node in enumerate(lists):
            if list_node and list_node.val < min_value:
                min_value = list_node.val
                min_index = index
        return min_index

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode()
        walker = dummy
        min_index = self.getMinIndex(lists)
        while min_index is not None:
            walker.next = lists[min_index]
            walker = walker.next
            lists[min_index] = lists[min_index].next
            walker.next = None
            min_index = self.getMinIndex(lists)
        return dummy.next
