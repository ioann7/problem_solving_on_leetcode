# https://leetcode.com/problems/generate-parentheses

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        self.generate_parenthesis(n * 2, '', 0, result)
        return result

    def generate_parenthesis(
            self, n: int, prefix: str,
            opened_parenthesis: int, result: List[str]) -> None:
        if n == 0:
            result.append(prefix)
            return
        if opened_parenthesis:
            self.generate_parenthesis(n - 1, prefix + ')', opened_parenthesis - 1, result)
        if n - opened_parenthesis > 1:
            self.generate_parenthesis(n - 1, prefix + '(', opened_parenthesis + 1, result)
