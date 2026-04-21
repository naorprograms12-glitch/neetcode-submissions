class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False 
        
        chars_s = {}
        chars_t = {}
        for c in s:
            if(c not in chars_s):
                chars_s[c]=1
            else:
                chars_s[c]+=1
        for c in t:
            if not (c  in chars_t):
                chars_t[c] = 1
            else:
                chars_t[c]+=1
        for c in s:
            if not (c in chars_t):
                return False
            if chars_s[c] != chars_t[c]:
                return False
        return True