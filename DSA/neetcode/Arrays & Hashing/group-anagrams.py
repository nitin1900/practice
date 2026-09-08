#ask explain and debugged the question and code to ai and all done myself...
#this is how hashmap is done simple bus use dict....
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen={}
        for i in strs:
            word=''.join(sorted(i))
            if word in seen:
                seen[word].append(i)
            else:
                seen[word]=[i] #mc ye squarer bracket nahi diya toh dimag kha gaya...
        return list(seen.values())

#pattern: Hashmap