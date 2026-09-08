#my code but took the help of ai to heavely debug most things..
#pattern: hashmap
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        seen[k] = []
        #copy-pasted the line 9 from ai sorted(...) but counter(num)was mine hehehe...
        for element, frequency in sorted(Counter(nums).items(),key=lambda x: x[1],reverse=True):
            if len(seen[k]) == k:
                break
            seen[k].append(element)
        return seen[k]

#suggested by ai to more efficent...
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        buckets = [[] for _ in range(len(nums) + 1)]

        for num, freq in count.items():
            buckets[freq].append(num)

        result = []

        for freq in range(len(nums), 0, -1):
            for num in buckets[freq]:
                result.append(num)

                if len(result) == k:
                    return result

        return result
