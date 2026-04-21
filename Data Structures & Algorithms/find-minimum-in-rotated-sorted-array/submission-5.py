class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        mid = (r+l+1)//2

        while nums[mid] > nums[mid -1]:
            if nums[l] < nums[r]:
                return nums[l]
            if nums[mid] < nums[l]:
                r = mid
            if nums[mid] > nums[r]:
                l =mid
            mid = (r+l+1)//2

        
        return nums[mid]