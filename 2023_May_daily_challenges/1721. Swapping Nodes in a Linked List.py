# https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Time complexity O(n). Space complexity O(1).
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        for _ in range(k - 1):
            current = current.next
        node1 = current
        node2 = head
        while current.next:
            current = current.next
            node2 = node2.next
        node1.val, node2.val = node2.val, node1.val
        return head        
