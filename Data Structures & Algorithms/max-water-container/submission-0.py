class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # Use two pointers
        # Find the area (width * height)
        # Move pointer with smaller height (cause its less area)
        # Return max area

        l = 0 
        r = len(heights) - 1
        max_area = 0

        while l < r:
            # Find area
            # lower height
            h = min(heights[l], heights[r])
            w = len(heights[l:r])
            area = w * h

            if area > max_area:
                max_area = area
            
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        
        return max_area


