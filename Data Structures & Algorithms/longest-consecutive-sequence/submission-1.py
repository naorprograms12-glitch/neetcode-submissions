class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0
        m = min(nums)
        d = set(nums)
        curr_cnt=0
        max_cnt=0
        while(d):
            while(d and m in d):
                d.remove(m)
                m+=1
                curr_cnt+=1
            if(d):   
                m = min(d)
            if curr_cnt > max_cnt:
                max_cnt = curr_cnt
            curr_cnt=0
        return max_cnt