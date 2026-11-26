class Solution {
public:
    bool canAliceWin(int n) {
        if(n < 10) return false;

        int rem = 10;
        int turn = 1;

        while(n > 0)
        {
            if(turn == 1)
            {
                // Alice turn
                if(n - rem < 0) return false;
                else
                {
                    n -= rem;
                }
                turn = 0;
            }
            else
            {
                // Bob turn
                if(n - rem < 0) return true;
                else
                {
                    n -= rem;
                }
                turn = 1;
            }
            rem--;
        }
        return turn == 0;
    }
};