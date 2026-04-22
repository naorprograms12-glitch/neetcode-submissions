class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0 , len(nums)-1
        mid = (l+r)//2

        while l < r:
            if nums[mid] == target:
                return mid

            if nums[l] <= nums[mid]: #אני בחצי השמאלי
                if nums[mid]<target:
                    l = mid +1
                else:
                    if nums[l] <= target:
                        r =mid-1
                    else:
                        l = mid +1

            else:
                if target < nums[mid]:
                    r = mid -1
                else:
                    if target <= nums[r]:
                        l = mid +1
                    else:
                        r = mid -1

            mid = (l+r)//2

        if nums[mid] == target:
            return mid
        return -1

                

        