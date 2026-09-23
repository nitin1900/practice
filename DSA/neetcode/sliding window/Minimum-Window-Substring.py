#copy-paste from ai...
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s or len(s) < len(t):
            return ""

        # Frequency map for characters in t
        count_t = {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        window = {}
        have, need = 0, len(count_t)
        res, res_len = [-1, -1], float("infinity")
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            # If the current character meets the required frequency in t
            if c in count_t and window[c] == count_t[c]:
                have += 1

            # When all character conditions are satisfied, try shrinking from the left
            while have == need:
                # Update smallest window found so far
                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                # Pop from the left of the window
                left_char = s[l]
                window[left_char] -= 1
                if left_char in count_t and window[left_char] < count_t[left_char]:
                    have -= 1
                l += 1

        l, r = res
        return s[l : r + 1] if res_len != float("infinity") else ""