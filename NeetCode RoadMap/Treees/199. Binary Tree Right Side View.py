# https://leetcode.com/problems/binary-tree-right-side-view/

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Time complexity is O(n), where n is all nodes. Space complexity is O(n/2)=O(n) for queue.
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        queue = collections.deque([root] if root else [])
        while queue:
            current_node = queue[0]
            for _ in range(len(queue)):
                current_node = queue.popleft()
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(current_node.val)
        return result
