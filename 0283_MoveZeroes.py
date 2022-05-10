class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        found = 0;
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[found] = nums[i]
                found += 1
        for i in range(found, len(nums)):
            nums[i] = 0
        return nums