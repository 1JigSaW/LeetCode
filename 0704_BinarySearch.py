class Solution(object):
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = left + (right - left) // 2
            print(middle)
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1

    def search(self, nums, target):
        if not nums: 
            return -1
        mid = len(nums) // 2 
        num = nums[mid]
        if num == target:
            return mid
        elif num > target:
            return self.search(nums[:mid], target)
        else:
            srch = self.search(nums[mid+1:], target)
            if srch == -1:
                return -1
            return mid + 1 + srch
            


nums = [-1,0,3,5,9,12]
target = 9
print(Solution().search(nums, target))