class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = 0
        for i in range(low+1, high):
            if i % 2 != 0:
                count += 1