# my code with little help in degubbing the code i got the core logic and most syntax by myself:
nums1 = [100, 200]
nums2 = [300,400]

num = sorted(nums1 + nums2)
n = len(num)

if n % 2 == 1:
    median = float(num[n // 2]) #in this and else part i wrote n/2 as it provide index not value point out by ai and gave this code
else:
    median = (num[(n // 2) - 1] + num[n // 2]) / 2.0

print(median)

# submitted in leetcode:
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        num = sorted(nums1 + nums2)
        n = len(num)
        
        # If odd, take the middle element
        if n % 2 == 1:
            return float(num[n // 2])
        
        # If even, take the average of the two middle elements
        return (num[(n // 2) - 1] + num[n // 2]) / 2.0
