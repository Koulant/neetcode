class Solution:
    def isValid(self, s: str) -> bool:
        # Check each char in s
        # Ensure each opening bracket has a corresponding closing bracket
        # How to ensure ordering?
        # Use a stack!
        # If left bracket push onto stack
        # If right bracket, check if top of stack matched
        # If matches, continue
        # If not matches, return False
        # return True if stack is empty, otherwise return false

        bracket_stack = []
        bracket_map = { # close : open
            "]" : "[", 
            "}" : "{",
            ")" : "(",
        }

        for b in s:
            if b in bracket_map:
                if bracket_stack and bracket_stack[-1] == bracket_map[b]:
                    bracket_stack.pop()
                else:
                    return False
            else:
                bracket_stack.append(b)
            
        return True if not bracket_stack else False

        # Time: O(n)
        # Space: O(n)