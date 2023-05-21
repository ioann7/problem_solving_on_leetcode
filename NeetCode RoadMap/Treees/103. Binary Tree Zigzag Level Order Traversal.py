# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/


# Time complexity O(n) where n is vertex. Space O(n) for result just.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return root
        queue = deque((root,))
        result = []
        level = 0
        while queue:
            zigzag_queue = queue if level % 2 == 0 else reversed(queue)
            result.append(list())
            for node in zigzag_queue:
                result[level].append(node.val)
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            level += 1
        return result
