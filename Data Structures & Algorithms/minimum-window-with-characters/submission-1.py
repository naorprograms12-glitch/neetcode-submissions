class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if s == "":
            return ""
        req_freq = {}
        i = 0
        j = len(s)-1
        cnt = 0
        for char in t:
            if char in req_freq:
                req_freq[char]+=1
            else:
                req_freq[char] = 1

        print(req_freq)
        
        requirements = len(req_freq)

        freq = {}
        flag = False
        l = 0
        r = 1
        if s[l] in req_freq:
            freq[s[l]] = 1
            if freq[s[l]] == req_freq[s[l]]:
                cnt += 1
                if cnt == requirements:
                    return s[l]
        while r < len(s):
            if s[r] in req_freq:
                if s[r] in freq:
                    freq[s[r]] += 1
                else:
                    freq[s[r]] = 1
                
                if freq[s[r]] == req_freq[s[r]]:
                    cnt+=1
                    if cnt == requirements:
                        flag = True

            if flag:
                while s[l] not in req_freq or freq[s[l]] > req_freq[s[l]]:
                    if s[l] in freq:
                        if freq[s[l]] > req_freq[s[l]]:
                            freq[s[l]]-=1
                    l+=1
                
                if (r-l)<(j-i):
                    j=r
                    i=l

            r+=1

        if flag:
            return s[i: j+1]
        return ""
            
