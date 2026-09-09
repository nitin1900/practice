#solution...(by ai)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]
            elif total < target:
                left += 1
            else:
                right -= 1
        return []

#my code what i tried and failed...
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        res=[]
        while left<right:
            while left<right:
                if numbers[left]+numbers[right]==target:
                    res.append(left)
                    res.append(right)
                    right-=1
            left+=1
        return res