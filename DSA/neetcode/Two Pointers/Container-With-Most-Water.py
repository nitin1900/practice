#didn't understand the question but took help and somewhat written code by ai with psudeocode...

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxwater=0
        while left<right:
            smallheight=min(heights[left], heights[right])
            width=right-left
            currentwater=smallheight*width
            if currentwater>maxwater:
                maxwater=currentwater
                if heights[left] < heights[right]:
                    left += 1
                else:
                    right -= 1
        return maxwater