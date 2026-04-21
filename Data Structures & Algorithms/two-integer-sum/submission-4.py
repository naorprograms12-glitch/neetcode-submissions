class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        delta = [target-nums[i] for i in range(len(nums))]
        for i in range(len(nums)):
            for j in range(i+1,len(delta)):
                if(nums[i]==delta[j]):
                    return [min(i,j),max(i,j)]