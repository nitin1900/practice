#my solution written purely myself
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)==len(t):
            return sorted(s)==sorted(t)

#suggest by ai:
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return len(s)==len(t) and sorted(s)==sorted(t)

#another optimal solution...
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


#pattern: counter/hashmap -> useful when I need frequencies/counts.