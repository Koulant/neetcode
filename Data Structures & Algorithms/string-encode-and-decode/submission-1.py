class Solution:

    def encode(self, strs: List[str]) -> str:
        # Take a list of strings and produce a single string
        # Iterate each str in list
        # Append a custom delimiter to the end
        # return a single string
        result = ""
        for s in strs:
            result += f"{len(s)}#{s}"
        
        return result



    def decode(self, s: str) -> List[str]:
        # Take a single string and produce a list of strings
        # Iterate each char in s
        # If custom delimiter is encountered
        # Add all chars up to but no including delimiter to make a string and add it to list
        result = []
        i = 0
        while i < len(s):
            j = i # Start j at the same index as i
            while s[j] != "#": # Incrememnt j until we find the "#" delimiter
                j += 1
            # Once "#" is encountered, get the number before, which is between i and j
            str_len = int(s[i:j]) # Get len of string
            result.append(s[j + 1 : j + 1 + str_len]) # Add string to result array
            i = j + 1 + str_len # Move i to end of this string, ahead of j

        return result

        # Time: O(m) for each encode() and decode() call
        # Space: O(m + n) for each encode() and decode() call













