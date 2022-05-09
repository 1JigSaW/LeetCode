class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        ind = 0
        for i in range(len(matrix)):
            if matrix[i][-1] >= target and matrix[i][0] <= target:
                ind = i
        left, right = 0, len(matrix[ind]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if matrix[ind][mid] == target:
                return True
            elif matrix[ind][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return False