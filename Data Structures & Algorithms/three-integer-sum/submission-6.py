class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Use two pointers to find -nums[i] equal to nums[j] + nums[k]
        # Sort array
        nums.sort()
        result = []

        for i in range(len(nums)):

            # Don't check the same num twice
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # Reset pointers for each nums[i]
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                    result.append([nums[i], nums[j], nums[k]])
                
                    j += 1
                    k -= 1
                    # Don't check the same nums[j] twice 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                elif total < 0:
                    j += 1
                else:
                    k -= 1
        
        return result

        # Time: 
