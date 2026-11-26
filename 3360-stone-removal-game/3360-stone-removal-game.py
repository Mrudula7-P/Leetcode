class Solution:
    def canAliceWin(self, n: int) -> bool:
        take = 10
        steps = 0
        while n >= take:
            n -= take
            take -= 1
            steps += 1
        return steps % 2 == 1