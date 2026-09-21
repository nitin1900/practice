#copy-paste from ai also this optimal from my leetcode file there is...
#btw.. this was my brute force but i don't remember my my code and can't understand too lol...
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {}
        l = 0
        max_len = 0
        for r, char in enumerate(s):
            if char in last_seen and last_seen[char] >= l:
                l = last_seen[char] + 1
            last_seen[char] = r
            max_len = max(max_len, r - l + 1)
        return max_len