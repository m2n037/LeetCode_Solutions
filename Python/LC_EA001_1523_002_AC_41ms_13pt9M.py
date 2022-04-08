class Solution:
    def countOdds(self, low: int, high: int) -> int:
        range1 = high - low - 1
        if ((low % 2 != 0) and (high % 2 == 0)) or ((low % 2 == 0) and (high % 2 != 0)):
            count = range1 / 2
        elif (low % 2 != 0) and (high % 2 != 0):
            count = (range1 + 1) / 2
        elif (low % 2 == 0) and (high % 2 == 0):
            count = (range1 - 1) / 2
        return int(count)