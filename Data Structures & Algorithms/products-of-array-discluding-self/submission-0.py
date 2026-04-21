class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        l = len(nums)
        left=[0 for i in range(l)]
        right=[0 for i in range(l)]
        n=1
        for i in range(l):
            n*=nums[i]
            left[i]=n
        n=1
        for i in range(l-1,-1,-1):
            n*=nums[i]
            right[i]=n
        res = [right[1]]+[left[i-1]*right[i+1] for i in range(1,l-1)]+[left[l-2]]
        return res



