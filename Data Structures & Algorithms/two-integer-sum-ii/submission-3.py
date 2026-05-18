class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Two pointer approach
        # Start pointers and adjust as needed

        l = 0
        r = len(numbers) - 1

        while l < r:
            current_sum = numbers[l] + numbers[r]

            if current_sum == target:
                return [l + 1, r + 1]

            elif current_sum > target: # sum too big, decrement right
                r -= 1

            else: # sum too small, increment left
                l += 1

        return []