class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use two pointers
        # Check each char in s 
        # Add chars to set
        # If char already in set
        # Check len of set
        # Set longest
        seen = set()
        l = 0
        longest = 0

        for r, c in enumerate(s):
            while c in seen:
                seen.remove(s[l])  # shrink from left until duplicate is removed
                l += 1
            seen.add(c)
            longest = max(longest, r - l + 1)

        return longest

        # Time: O(n)
        # Space: O(m)