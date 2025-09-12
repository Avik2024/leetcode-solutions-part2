# 1049. Last Stone Weight II
class Solution:
    def lastStoneWeightII(self, stones: List[int] ) -> int:
        total = sum(stones)
        target = total // 2 # half partition 
        dp = [0] * (target + 1)
        
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        
        return total - 2 * dp[target]
        
# Time Complexity - O(n * target)
# Space Complexity - O(target)
