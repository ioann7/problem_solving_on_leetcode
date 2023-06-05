# https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        first, second = coordinates[0], coordinates[1]
        vector = (second[0] - first[0], second[1] - first[1])
        for index in range(2, len(coordinates)):
            coord = coordinates[index]
            if ((coord[0] - first[0]) * vector[1]) != ((coord[1] - first[1]) * vector[0]):
                return False
        return True
