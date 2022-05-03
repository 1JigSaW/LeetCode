class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if needle == '':
            return 0
        if len(haystack) < len(needle):
            return -1
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                ind = i
                j = 0
                new_i = i
                while j < len(needle):
                    if len(haystack) == new_i:
                        flag = False
                        break
                    if haystack[new_i] == needle[j]:
                        j += 1
                        new_i += 1
                        flag = True
                    else:
                        flag = False
                        break
                if flag == True:
                    return ind
            i += 1
        return -1
        