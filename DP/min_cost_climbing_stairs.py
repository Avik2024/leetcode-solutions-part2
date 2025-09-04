class Solution(object):
	def minCostClimbingStairs(self, n):
		n = len(cost)
		one, two = cost[0], cost[1]
		
		for i in range(2, n):
			curr = cost[i] + min(one, two)
			one, two = two, curr
		return min(one, two)

# Time Complexity - O(n)
# Space Complexity - O(1)
