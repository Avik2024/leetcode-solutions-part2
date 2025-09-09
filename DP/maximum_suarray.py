def max_subarray_sum(nums):
    max_so_far = nums[0]    # Maximum sum found so far (O(1) space)
    current_sum = nums[0]   # Sum ending at current index (O(1) space)
    
    for num in nums[1:]:
        # Either include the current num in the previous subarray or start fresh
        current_sum = max(num, current_sum + num)
        # Update overall maximum if current subarray sum is better 
        max_so_far = max(max_so_far, current_sum)
        
    return max_so_far 

# Example Usage     
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(max_subarray_sum(nums))   # Output: 6

# Time Complexiy: O(n)
# Space Complexity: O(1)
