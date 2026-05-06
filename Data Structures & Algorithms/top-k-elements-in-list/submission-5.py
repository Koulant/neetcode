class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count number of occurences for each
        # map count to nums array
        # return top two lists (k)

        nums_count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            nums_count[n] = nums_count.get(n, 0) + 1

        for n, c in nums_count.items():
            freq[c].append(n)

        result = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                result.append(n)

            if len(result) == k:
                return result

            

        