#my solution...
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        add=[]
        for i,num in enumerate(nums):
            for j,numu in enumerate(nums):
                if num+numu==target and i!=j and i not in add and j not in add:
                    add.append(i)
                    add.append(j)
        return add

#ai:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i


#pattern: hashmap/dict pattern -> Useful have I seen the number I need before, and where?