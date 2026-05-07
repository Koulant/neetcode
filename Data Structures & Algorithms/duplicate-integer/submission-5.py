class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Return if any num in nums appears more than once
        # nums ordering is no guaranteed
        # Iterate nums
        # Use a set to store seen num in nums
        # If a num already in the set, return True
        # Return false

        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
        
        # Time: O(n)
        # Space: O(n)