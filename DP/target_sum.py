class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        # Check visibility 
        if total < abs(target) or (target + total) % 2 == 1:
            return 0 
        
        subset_sum = (target + total) // 2 
        dp = [0] * (subset_sum + 1)
        dp[0] = 1 # one way to form 0 sum 
        
        for num in nums:
            for j in range(subset_sum, num - 1, -1):
                dp[j] += dp[j - num]
        
        return dp[subset_sum]

# Time complexity - O(n * subset_sum)
# Space Complexity - O(subset_sum)
