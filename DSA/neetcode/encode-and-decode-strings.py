#my code i didn't understand the question after that i try to solve question with ai...
#pattern: Length-Prefix Framing

class Solution:
    def encode(self, strs: List[str]) -> str:
        s=''
        for i in strs:
            s+=f'{len(i)}#{i}'
        return s
    def decode(self, s: str) -> List[str]:
        sta=0
        result=[]
        #ai
        while sta < len(s):
            j = sta
            while s[j] != '#':
                j += 1
            length = int(s[sta:j])
            word = s[j + 1 : j + 1 + length]
            result.append(word)
            sta = j + 1 + length
        #ai
        return result

#optimized(idk man):
class Solution:
    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res