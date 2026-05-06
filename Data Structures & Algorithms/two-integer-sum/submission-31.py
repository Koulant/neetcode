class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # One pass hash map approach
        num_index = {}

        for i, n in enumerate(nums):

            diff = target - n # Find the complement

            if diff in num_index: # If complement is in the hash map, return complement index, i
                return [num_index[diff], i]

            num_index[n] = i # Add the number : index mapping we already checked to hash map
            # This way, if we already passed the complement, we know both indicies in a single pass
        return []

        # Time: O(n)
        # Space: O(n)

        



        