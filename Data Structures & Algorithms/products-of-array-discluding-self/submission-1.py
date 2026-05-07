class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Key insight: Can do this in O(n) time using prefix/suffix approach
        # Product will be whats to the left of i and whats to the right of i
        # Iterate nums with index
        # Collect nums to left of i
        # Collect nums to right of i
        # Get product as you go 
        # Return result
        len_nums = len(nums)
        left, right,  = [1] * len_nums, [1] * len_nums
        result = [0] * len_nums

        prefix = 1
        for i in range(len_nums):
            left[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(len_nums - 1, -1, -1):
            right[i] = suffix
            suffix *= nums[i]

        for i in range(len_nums):
            result[i] = left[i] * right[i]

        return result
        
