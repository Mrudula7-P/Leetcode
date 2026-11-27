class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        copies = [0] * n
        min_price = float('inf')
        for i in range(n):
            copy = 0
            for j in range(n):
                if i == j:
                    continue

                if items[j][0] % items[i][0] == 0:
                    copy += 1
            min_price = min(min_price, items[i][1])
            copies[i] = copy
        t = [[-1] * (budget + 1) for _ in range(n + 1)]
        
        return self.solve(n, budget, min_price, items, copies, t)
    
    def solve(self, n, budget, min_price, items, copies, t):
        if n == 0:
            return budget // min_price

        if t[n][budget] != -1:
            return t[n][budget]

        take = 0
        price = items[n-1][1]
        if price <= budget:
            take = 1 + copies[n-1] + self.solve(n-1, budget - price, min_price, items, copies, t)
        skip = self.solve(n-1, budget, min_price, items, copies, t)

        t[n][budget] = max(take, skip)
        return t[n][budget]
