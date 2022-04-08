class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        length1 = len(salary) - 2
        avg1 = (sum(salary) - salary[0] - salary[-1]) / length1
        
        return avg1