#my code...
#pattern: "Find the beginning of a sequence."
nums = [2,20,4,10,3,4,5]
val={}
dum=sorted(set(nums))
for i in dum:
    k=0
    for j in dum:
        if i+k==j:
            k+=1
        else:
            val[i]=k
print(max(val.values()))

#improved...
nums = [2,20,4,10,3,4,5]

dum = sorted(set(nums))

longest = 1
current = 1

for i in range(1, len(dum)):
    if dum[i] == dum[i-1] + 1:
        current += 1
    else:
        current = 1

    longest = max(longest, current)

print(longest)


#solution submitted written by AI...
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # num is the beginning of a sequence
            if num - 1 not in numSet:
                current = 1

                while num + current in numSet:
                    current += 1

                longest = max(longest, current)

        return longest
