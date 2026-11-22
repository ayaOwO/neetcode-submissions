class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        max_water = 0
        while end != start:
            width = end - start
            max_water = max(max_water, width * min(heights[end], heights[start]))
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_water
