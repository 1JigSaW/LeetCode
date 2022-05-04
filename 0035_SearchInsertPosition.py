class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        if len(nums) == 1:
            if target < nums[0]:
                return 0
            else:
                return 1
        for i in range(1, len(nums)):
            if nums[i-1] > target:
                return 0
            if nums[-1] < target:
                return len(nums)
            if nums[i-1] <= target and nums[i] >= target:
                return i
