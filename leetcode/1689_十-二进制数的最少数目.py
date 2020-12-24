class Solution:
    def minPartitions(self, n: str) -> int:
        v = [int(item) for item in n]
        return max(v)

a = Solution()
n = '27346209830709182346'
print(a.minPartitions(n))