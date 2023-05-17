# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n). Space complexity O(1).
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        left, right = prev, slow
        
        max_sum = left.val + right.val
        while left:
            max_sum = max(max_sum, left.val + right.val)
            left = left.next
            right = right.next
        return max_sum
