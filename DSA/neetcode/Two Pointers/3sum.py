#my code...
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j<k:
                if nums[i]+nums[j]+nums[k]==0:
                    res.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    while j<k and nums[j]==nums[j-1]:
                        j+=1
                    while j<k and nums[k]==nums[k+1]:
                        k-=1
                elif nums[i]+nums[j]+nums[k]<0:
                    j+=1
                else:
                    k-=1
        return res

#more faster code...
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums)):
            # Skip duplicate values for i
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1

                elif total > 0:
                    k -= 1

                else:
                    res.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate values for j
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    # Skip duplicate values for k
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

        return res
