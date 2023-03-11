# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree
# The solution is, we halve the ListNode and cut off the middle, then recursively call for the two sides.


from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None

        if not head.next:
            return TreeNode(head.val)

        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next

        pre.next = None
        result = TreeNode(slow.val)
        result.left = self.sortedListToBST(head)
        result.right = self.sortedListToBST(slow.next)
        return result
        
