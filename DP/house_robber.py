class Solution:
	def rob(self, nums: List[int]) -> int:
		if not nums:
			return 0
		prev2, prev1 = 0, 0
		for num in nums:
			curr = max(prev1, prev2 + num)
			prev2, prev1 = prev1, curr 
		return prev1 

# Time Complexity - O(n)
# Space Complexity - O(1)
# Recurrence Relation - dp[i]=max(dp[i−1],dp[i−2]+nums[i])
