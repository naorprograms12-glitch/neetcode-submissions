class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 1
        for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" :
            l=0
            r=1
            cnt = 0
            length = 1
            if len(s) == 0:
                return 0
            if s[l] != letter:
                if cnt<k:
                    cnt+=1
                else:
                    while s[l] != letter and l<len(s)-1:
                        l+=1
                    r = l+1
            while r < len(s):
                if s[r] == letter:
                    r+=1
                    length+=1
                else:
                    if cnt < k:
                        cnt+=1
                        r+=1
                        length+=1
                    else:
                        max_len = max(max_len, length)
                        print(max_len)
                        while cnt == k:
                            if s[l] != letter:
                                cnt-=1
                            l+=1
                            length-=1
                        r+=1
                        cnt+=1
                        length+=1
            max_len = max(max_len, length)

        return max_len