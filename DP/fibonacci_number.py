class Solution(object):
	def fib(self, n):
		if n == 0:	# Handle base case 
			return 0
		one, two = 0, 1
		for i in range(2, n + 1):
			temp = two
			two = one + two
			one = temp
		return two

# Time Complexity - O(n)
# Space Complexity - O(1)

	
