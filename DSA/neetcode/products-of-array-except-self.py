#my code...
#pattern: Prefix / Suffix Pattern
import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        for i in nums:
            arr=set(nums.copy())
            arr.remove(i)
            res.append(math.prod(arr))
        return res



import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            arr = nums[:i] + nums[i+1:]
            res.append(math.prod(arr))

        return res
#refine version...⬆️⬇️
import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            arr = nums.copy()
            arr.pop(i)
            res.append(math.prod(arr))

        return res


#optimized
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        prefix = 1

        # Left → Right
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        # Right → Left
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
