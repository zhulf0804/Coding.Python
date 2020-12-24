from typing import List

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        for cuboid in cuboids:
            cuboid.sort()
        cuboids.sort()
        n, ans = len(cuboids), 0
        dp = [cuboid[2] for cuboid in cuboids]
        for i in range(n):
            for j in range(i):
                if cuboids[j][0] <= cuboids[i][0] and \
                    cuboids[j][1] <= cuboids[i][1] and \
                    cuboids[j][2] <= cuboids[i][2]:
                    dp[i] = max(dp[i], cuboids[i][2] + dp[j])
            ans = max(ans, dp[i])
        return ans

a = Solution()
cuboids = [[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]
print(a.maxHeight(cuboids))