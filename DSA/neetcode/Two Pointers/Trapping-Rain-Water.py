#solution... by ai
class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        filled = 0

        while left < right:
            if height[left] <= height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    filled += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    filled += right_max - height[right]
                right -= 1

        return filled

#my code...
class Solution:
    def trap(self, height: List[int]) -> int:
        left=0
        right=len(height)-1
        filled=0
        while left<right:
            short=min(height[left],height[right]-height[left])#copy-paste from hint not mine
            if short>0:
                filled+=short
                left+=1
                right-=1
            else:
                left+=1
                right-=1
        return filled
