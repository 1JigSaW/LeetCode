class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for i in range(1, numRows+1):
            res.append([1]*i)
            for j in range(1, len(res[i-1])-1):
                res[i-1][j] = res[i-2][j-1] + res[i-2][j]
        return res