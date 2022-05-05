class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d.append(nums[i])
            else:
                return True
        return False