class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Let n be the len of the input array 
        # Create results array result of size n
        # Iterate all nums by index
        # Calculate product for all nums other than i 
        # Set result indicies to product 
        n = len(nums)
        result = [0] * n

        for i in range(n): 
            prod = 1

            for j in range(n):
                if i == j:
                    continue
                prod *= nums[j]

            result[i] = prod

        return result