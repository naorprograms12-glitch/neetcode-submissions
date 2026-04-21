class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cnt = {}
        for i in range(len(nums)):
            if nums[i] in cnt:
                return True
            
            else:
                cnt[nums[i]]=1
            
        return False;