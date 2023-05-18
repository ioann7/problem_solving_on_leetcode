# https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

# Time complexity O(V). Space complexity O(V).
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        vertices = [0] * n
        for from_i, to_i in edges:
            vertices[to_i] = 1
        result = []
        for vertex, has_path_before in enumerate(vertices):
            if not has_path_before:
                result.append(vertex)
        return result
