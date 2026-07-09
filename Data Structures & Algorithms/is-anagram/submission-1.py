class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        is_anagram = True
        leng = len(s)
        map_s = {}
        map_t = {}
        
        if leng == len(t):
            for i in range (0, leng):
                if map_s.get(s[i]) == None:
                    map_s[s[i]] = 1
                else:
                    map_s[s[i]] = map_s[s[i]] + 1
                
                if map_t.get(t[i]) == None:
                    map_t[t[i]] = 1
                else:
                    map_t[t[i]] = map_t[t[i]] + 1
        else:
            is_anagram = False
        
        if map_s != map_t:
            is_anagram = False
        
        return is_anagram
        