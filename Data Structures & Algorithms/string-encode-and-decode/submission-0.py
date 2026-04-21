class Solution:

    def encode(self, strs: list[str]) -> str:
        res = []
        for st in strs:
            res.append("0")
            for ch in st:
                res.append("1")
                res.append(ch)
        return "".join(res)


    def decode(self, s: str) -> list[str]:
        res=[]
        word =""
        i=0
        while i<len(s):
            if s[i] == "0":
                res.append(word)
                word=""
            else:
                i+=1
                word+=s[i]
            i+=1
        res.append(word)
        return res[1:]

sol = Solution()
print(sol.decode(sol.encode(["neet","code","love","you"])))