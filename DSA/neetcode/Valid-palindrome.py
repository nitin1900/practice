#my code...
#pattern: Two pointer...
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.strip().lower()
        new=[x for x in s if x.isalnum()]
        new=''.join(new)
        if new==new[::-1]:
            return True
        else:
            return False

# refine...
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]


#solution...(not done myself by ai...)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


# note:
# isalpha() for letters only
# isdigit() for digits only
# isalnum() for letters and/or digits