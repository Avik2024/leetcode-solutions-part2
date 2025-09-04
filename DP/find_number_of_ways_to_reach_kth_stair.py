import math

class Solution(object):
	def comb(self, n, r):
	
	def waysToReachStair(self, k):
		ans = 0
		#j controls number of jumps(2 ^ j grow fast, so ~32 is enough for int range)
		#LeetCode problems don’t always restrict k to 32-bit.
		#Python supports big integers (arbitrary precision).
		#To be safe, the code runs up to j = 64 so it can cover any realistic k (up to around 10^18 — which matches many problem constraints).
		
		for j in range(0, 64):
			total_up = (1 << j) 	# 2 ^ j
			downs = total_up - k
			if 0 <= downs <= j + 1:
				ans += self.comb(j + 1, downs)
		return ans
		
# Time Complexity - O(64) or O(1)
# Space Complexity - O(1)
