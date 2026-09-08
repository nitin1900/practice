#done myself but with some error debugged by ai:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i,num in enumerate(nums):
            for j,numu in enumerate(nums):
                if num==numu and i!=j:
                    return True
        return False #here i have written as else:return false which was wrong like this is correct

#suggusted by ai
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#pattern: set -> Useful when I need to know whether I've seen something before.