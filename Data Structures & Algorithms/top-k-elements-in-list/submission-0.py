class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for n in nums:
            if n not in freq:
                freq[n]=1
            else:
                freq[n]+=1
        res = sorted(freq, key=lambda x: freq[x])
        return res[-k:]