class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Given nums and k, return k most frequent elements
        # Use a map of num : count to store element counts
        # Use map to produce array sorted by count
        # Return k most frequent

        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        nums_desc = sorted(num_count.keys(), key=lambda x: num_count[x], reverse=True )

        return nums_desc[:k]

        # Time: O(n log n)
        # Space O(n)