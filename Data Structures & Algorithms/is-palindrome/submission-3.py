class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Use two pointer approach
        # One pointer starts at left another starts at right right
        # Pointers move inwards by 1
        # Compare values at pointers
        # Return true if they match, false if they dont match

        l = 0
        r = len(s) - 1

        while l < r:
            while l < r and not s[l].isalnum():
                l += 1

            while r > l and not s[r].isalnum():
                r -= 1
            
            # Now both are on a valid character
            if s[l].lower() != s[r].lower():
                return False
            
            # Move them inward by 1 and keep going
            l += 1
            r -= 1
        
        return True

        # Time: O(n)
        # Space: O(n)            
