import math
# 超时1
class Solution_1:
    def countPrimes(self, n: int) -> int:
        def isPrime(val):
            if val <= 1:
                return False
            for i in range(2, val):
                if val % i == 0:
                    return False
            return True
        count = 0
        for i in range(n):
            if isPrime(i):
                count += 1
        return count
# 超时2
class Solution_2:
    def countPrimes(self, n: int) -> int:
        def isPrime(val):
            if val <= 1:
                return False
            for i in range(2, int(math.sqrt(val)) + 1):
                if val % i == 0:
                    return False
            return True
        count = 0
        for i in range(n):
            if isPrime(i):
                count += 1
        return count

class Solution_3:
    def countPrimes(self, n: int) ->int:
        nums = [0] * n
        res = 0
        for i in range(2, n):
            if nums[i] == 0:
                mul = 2
                res += 1
                while mul * i < n:
                    nums[mul * i] += 1
                    mul += 1
        return res

class Solution_4:
    def countPrimes(self, n: int) ->int:
        nums = [0] * n
        res = 0
        for i in range(2, n):
            if nums[i] == 0:
                res += 1
                nums[2*i : n : i] = [1]*len(nums[2*i : n : i])
        return res

class Solution:
    def countPrimes(self, n: int) ->int:
        if n < 2:
            return 0
        nums = [0] * n
        nums[1] = nums[0] = 1
        for i in range(2, int(math.sqrt(n)) + 1):
            if nums[i] == 0:
                nums[i*i : n : i] = [1]*len(nums[i*i : n : i])
        return n - sum(nums)


s = Solution()
print(s.countPrimes(999983))