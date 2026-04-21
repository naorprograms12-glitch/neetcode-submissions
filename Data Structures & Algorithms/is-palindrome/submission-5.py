class Solution:
    def isPalindrome(self, s: str) -> bool:
        i=0
        j=len(s)-1
        cnt=0
        for ch in s:
            if(self.isAlphaNumerical(ch)):
                cnt+=1
        if cnt == 0:
            return True
        while(i<j):
            while(not self.isAlphaNumerical(s[i])):
                  i+=1
            while(not self.isAlphaNumerical(s[j])):
                  j-=1
            if(i>=j):
                return True
            if(s[i].lower()!=s[j].lower()):
                return False
            i+=1
            j-=1
        return True
            


    def isAlphaNumerical(self,n: int) -> bool:
        p = ord(n)
        return 65 <= p <= 90 or 97<= p <= 122 or 48 <= p <= 57