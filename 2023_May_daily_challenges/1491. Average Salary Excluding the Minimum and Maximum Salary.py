# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

# Time complexity O(n). Space complexity O(1).
class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        min_salary = salary[0]
        max_salary = salary[0]
        for salary_i in salary:
            if salary_i < min_salary:
                min_salary = salary_i
            elif salary_i > max_salary:
                max_salary = salary_i
            total += salary_i
        total = total - min_salary - max_salary
        return total / (len(salary) - 2)
