# O(n^2)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for num1 in range(len(nums)):
            for num2 in range(len(nums)):
                if num1 != num2:
                    if nums[num1] + nums[num2] == target:
                        result.append(num1)
                        result.append(num2)
                        return result

# O(n)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        curr = 0
        for i in range(len(nums)):
            curr = i
            if ((target - nums[i]) in nums[i+1:]):
                res.append(i)
                break
        print(res)
        for i in range(len(nums)):
            if (nums[i] == (target - nums[res[0]])) and (res[0] != i):
                res.append(i)
                break
        return res
            