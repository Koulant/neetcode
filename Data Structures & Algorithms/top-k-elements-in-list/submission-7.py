class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count number of occurences for each
        # map count to nums array
        # return top two lists (k)

        # count number of occurences for each number in nums
        nums_count = {}
        # use list comp to create a list of frequencies of each number list
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            nums_count[n] = nums_count.get(n, 0) + 1 # adding count of ecah num to dict

        for n, c in nums_count.items():
            freq[c].append(n) # adding each number to its respective list at that freq count/index

        # build results set
        result = []
        for i in range(len(freq) - 1, 0, -1): # start, stop, step used to start at end, stop at 0, step backwards
            for n in freq[i]: # add the numbers at that freq index to the result array
                result.append(n)

            if len(result) == k: # once result array is equal to k, return it
                return result

        return [0] # Fix linter error

    # Time: O(n)
    # Space: O(n)


            

        