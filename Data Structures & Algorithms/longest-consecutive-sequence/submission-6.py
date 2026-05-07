class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a hash set to track consecutive numbers
        # Iterate nums once
        # Identify start of sequence
        # If sequence start + 1 in set, incremement len 

        num_set = set(nums)
        longest = 0 # start at 0 in case of nums = []

        for num in num_set:
            if num - 1 not in num_set: # then num is the start of the sequence
                length = 1 # min length of sequence is 1
                while num + length in num_set: # while consecutive nums is in seen, advance length 
                    length += 1
                longest = max(longest, length)

        return longest

        # Time: O(n)
        # Space: O(n)
