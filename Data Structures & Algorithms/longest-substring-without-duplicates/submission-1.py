class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        seen = set()
        max_v = 0
        if n==0:
            return 0
        else :
            if n == 1:
                return 1
            else:
                l=0 
                r=1
                seen.add(s[l])
                while r<n:
                    if s[r] in seen:
                        max_v = max(len(seen), max_v)
                        while(s[r] != s[l]):
                            seen.remove(s[l])
                            l+=1
                        l+=1
                        r+=1
                        if l == r:
                            r+=1
                    else: 
                        seen.add(s[r])
                        r+=1
                max_v = max(max_v, len(seen))

                return max_v
                    


