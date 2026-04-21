class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        delta = {}
        for i in range(len(nums)):
            delta[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in delta and i!=delta[nums[i]]:
                return [min(i,delta[nums[i]]),max(i,delta[nums[i]])]
        return []