class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums2 = [target-nums[i] for i in range(len(nums))]
        checked={}
        for i in range(len(nums)):
            checked[nums[i]]=i
        for i in range(len(nums2)):
            if nums2[i] in checked:
                if i!= checked[nums2[i]]:
                    return [min(i, checked[nums2[i]]), max(i,checked[nums2[i]])]