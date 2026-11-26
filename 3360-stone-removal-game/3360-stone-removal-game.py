class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
            
        rem = 10
        turn = 1
        while n > 0:
            # alice
            if turn == 1:
                if n - rem < 0:
                    return False
                else:
                    n -= rem
                turn = 0
                
            # bob
            else:
                if n - rem < 0:
                    return True
                else:
                    n -= rem
                turn = 1
            rem -= 1
        
        return turn == 0