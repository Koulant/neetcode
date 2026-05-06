class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Use hash map to store value : index
        # iterate nums array and check if the complement of current element exists
        # complement must be at different index, can't use same element twice

        num_index = {}

        for i, n in enumerate(nums):

            diff = target - n

            if diff in num_index:
                return [num_index[diff], i]

            num_index[n] = i
        return []

        



        