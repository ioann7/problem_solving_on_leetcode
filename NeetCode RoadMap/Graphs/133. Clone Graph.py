# https://leetcode.com/problems/clone-graph/

# Time complexity O(V + E). Space complexity O(V) for hashmap and O(E) for recursive stack.
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        old_to_new = {}

        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            old_to_new[node] = Node(node.val)
            for neighbor in node.neighbors:
                old_to_new[node].neighbors.append(dfs(neighbor))
            return old_to_new[node]

        return dfs(node) if node else None
