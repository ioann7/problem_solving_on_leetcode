# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Here is i am using not recursive. Time comp is O(n). Space comp O(n) for stack.
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = 1
        stack = []

        current = root
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                node = stack.pop()
                if count == k:
                    return node.val
                count += 1
                current = node.right


# Time comp is O(n). Space comp O(n) for recursive stack.
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        result = None
        count = 0

        def inorder(root: TreeNode) -> int:
            nonlocal count, k, result
            if root.left:
                inorder(root.left)
            count += 1
            if count == k:
                result = root.val
                return
            if root.right:
                inorder(root.right)

        inorder(root)
        return result
