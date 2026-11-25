class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        base = max(nums) + 1
        n = len(nums)
        l = 1
        r = n
        result = n

        while l <= r:
            mid = l + (r - l) // 2
            if self.check(nums, mid, base):
                result = mid
                r = mid - 1
            else:
                l = mid + 1
            
        return result
    
    def check(self, nums, size, base):
        MOD = 10 ** 9 + 7
        has = 0
        mp = {}

        def findpower(a, base):
            if base == 0:
                return 1
            
            half = findpower(a, base // 2)
            res = (half * half) % MOD
            
            if base % 2 == 1:
                res = (res * a) % MOD
            return res

        p = findpower(base, size - 1)
        
        n = len(nums)
        i = 0
        j = 0

        while j < n:
            has = (has * base + nums[j]) % MOD

            if j - i + 1 < size:
                j += 1
            
            else:
                mp[has] = mp.get(has, 0) + 1
                has = (has - (p * nums[i]) % MOD + MOD) % MOD
                i += 1
                j += 1
        
        for i, j in mp.items():
            if j == 1:
                return True
        return False




