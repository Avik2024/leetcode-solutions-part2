class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		total = sum(nums)
		if total % 2 != 0:
			return False 
		
		target = total // 2 
		dp = [False] * (target + 1)
		dp[0] = True					# Zero sum is always possible
		
		for num in nums:
			for j in range(target, num - 1, -1):	# Go backwards to always reuse 
				dp[j] = dp[j] or dp[j - num]
		
		return dp[target]

# Time Complexity - O(n * k) ; where n is the size of array and k is the target i.e total // 2
# Space Complexity - O(k)

