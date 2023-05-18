# https://leetcode.com/problems/course-schedule/

# Time complexity O(E+V). Space complexity O(E+V).
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = {course: [] for course in range(numCourses)}
        visit = set()
        for from_i, to_i in prerequisites:
            adjacency_list[from_i].append(to_i)

        def dfs(node):
            if node in visit:
                return False
            visit.add(node)
            for _ in range(len(adjacency_list[node])):
                neighbor = adjacency_list[node].pop()
                if not dfs(neighbor):
                    return False
            visit.remove(node)
            return True

        for node in adjacency_list:
            if not dfs(node):
                return False
        return True
