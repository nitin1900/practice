# code that i have submitted in leetcode first wriiten my code then convert into this pattern:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i

# code that i have written my self with liitle help of logic by ai:
num = [3, 3]
target = 6
sum = []

for i, x in enumerate(num):
    for j in range(i + 1, len(num)):
        y = num[j]

        if x + y == target:
            sum.append(x)
            sum.append(y)

print(sum)

