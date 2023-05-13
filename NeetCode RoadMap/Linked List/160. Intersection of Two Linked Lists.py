# https://leetcode.com/problems/intersection-of-two-linked-lists/

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        length_a = self.get_linked_list_length(headA)
        length_b = self.get_linked_list_length(headB)
        walker_a = headA
        walker_b = headB
        steps_number = abs(length_a - length_b)
        cur_steps = 0
        if length_a > length_b:
            walker_a = self.walk_steps(walker_a, steps_number)
        else:
            walker_b = self.walk_steps(walker_b, steps_number)
        while walker_a and walker_b:
            if walker_a == walker_b:
                return walker_a
            walker_a = walker_a.next
            walker_b = walker_b.next        

    def get_linked_list_length(self, head: ListNode) -> int:
        count = 0
        while head:
            head = head.next
            count += 1
        return count

    def walk_steps(self, head: ListNode, steps: int) -> Optional[ListNode]:
        cur_steps = 0
        while head and cur_steps < steps:
            head = head.next
            cur_steps += 1
        return head
