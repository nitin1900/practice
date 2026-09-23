#copy-paste from ai...
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = {}
        s2_count = {}

        # Fill target frequency map for s1
        for ch in s1:
            s1_count[ch] = 1 + s1_count.get(ch, 0)

        left = 0

        for right in range(len(s2)):
            # 1. Expand window to the right
            char_right = s2[right]
            s2_count[char_right] = 1 + s2_count.get(char_right, 0)

            # 2. Shrink window from the left if it exceeds len(s1)
            if (right - left + 1) > len(s1):
                left_char = s2[left]
                s2_count[left_char] -= 1
                if s2_count[left_char] == 0:
                    del s2_count[left_char]
                left += 1  # Must increment on every shrink

            # 3. Check if current window matches s1
            if s1_count == s2_count:
                return True

        return False