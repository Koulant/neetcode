class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Use Binary Search
        # For each number, need to find target - numbers[i] 
        # Loop through each index
        # Check the compliment
        # Binary search on the subarray from i + 1 to end

        for i in range(len(numbers)):
            l = i + 1
            r = len(numbers) - 1
            compliment = target - numbers[i]

            while l <= r:
                middle = (l + r) // 2

                if numbers[middle] == compliment:
                    return [i + 1, middle + 1]

                elif numbers[middle] < compliment:
                    l = middle + 1

                else:
                    r = middle - 1

        return []
