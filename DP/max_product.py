class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = min_prod = max_so_far = nums[0]  # O(1) space Complexity
        for num in nums[1:]:                        # O(n) Time Complexity 
            if num < 0:
                max_prod, min_prod = min_prod, max_prod 
            max_prod = max(num, max_prod * num)
            min_prod = min(num, min_prod * num)
            max_so_far = max(max_so_far, max_prod)
        return max_so_far

# Time Complexity: O(n)
# Space Complexity: O(1)
