class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        res = []
        out = []
        count = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                res.append(mat[i][j])
                count +=1 

                if(count == c):
                    out.append(res)
                    res = []
                    count = 0 

        if(len(out)!=r or len(out[0]) != c):
            return mat 
        else:
            return out
        