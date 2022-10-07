class Solution(object):
    def firstBadVersion(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            mid = left + (right - left) // 2
            if isBadVersion(mid) == False:
                left = mid + 1
            else:
                right = mid - 1
        if isBadVersion(mid) == False:
            return mid + 1
        else:
            return mid

        