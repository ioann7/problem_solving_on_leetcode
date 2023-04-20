# https://leetcode.com/problems/maximum-width-of-binary-tree/

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time and Space complexity like BFS. time O(n). space O(n).
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = collections.deque([(root, 1)] if root else [])
        result = 1
        while queue:
            start = queue[0]
            for _ in range(len(queue)):
                current = queue.popleft()
                if current[0].left:
                    queue.append((current[0].left, current[1] * 2))
                if current[0].right:
                    queue.append((current[0].right, (current[1] * 2) + 1))
            result = max(result, current[1] - start[1] + 1)
        return result
