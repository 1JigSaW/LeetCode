class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
        for v,k in d.items():
            if k == 1:
                for i in range(len(s)):
                    if v == s[i]:
                        return i
        return -1
        