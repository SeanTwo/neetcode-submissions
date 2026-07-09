class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n-1
        output = 0
        while left < right:
            temp = min(heights[left], heights[right])*(right-left)
            if output < temp:
                output  = temp
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return output