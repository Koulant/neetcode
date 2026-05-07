class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Use a hash set to track consecutive numbers
        # Iterate nums once
        # Identify start of sequence
        # If sequence start + 1 in set, incremement len 

        seen = set()
        start = []
        longest = 0

        for num in nums:
            seen.add(num)

        for num in seen:
            if num - 1 not in seen: # start of the sequence
                length = 1
                while num + length in seen:
                    length += 1
                longest = max(longest, length)

        return longest

