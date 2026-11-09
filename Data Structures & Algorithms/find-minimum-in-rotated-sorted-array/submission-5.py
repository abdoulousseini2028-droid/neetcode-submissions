class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
    

        left, right = 0, len(nums)-1
        min_ = float("inf")

        while left < right:
            mid = (left + right)//2
            if nums[left] <= nums[mid]:
                min_ = min(min_, nums[left])
                left = mid +1
            else:
                min_ = min(min_, nums[mid])
                right = mid -1

        return min(min_,nums[left])