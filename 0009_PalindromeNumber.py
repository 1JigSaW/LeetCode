class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        if len(x) == 1 or len(x) == 0:
            return True
        elif x[0] == x[-1]:
            return Solution.isPalindrome(self, x[1:-1])
        else:
            return False