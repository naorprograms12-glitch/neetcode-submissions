class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        def getLetters(word) -> List[int]:
            letters = [0 for i in range(27)]
            for ch in word:
                letters[ord(ch)-96]+=1
            return letters

        mySet=set()
        for word in strs:
            mySet.add(tuple(getLetters(word)))
        lst = list(mySet)
        res = [[] for i in range(len(lst))]
        for word in strs:
            for i in range(len(lst)):
                if tuple(getLetters(word))==lst[i]:
                    res[i].append(word)
                    break
                
        return res