from collections import Counter
from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n = len(s)
        m = len(p)
        
        p = Counter(p)                 
        ans = []
           
        window = None
        for i in range(0,n-m+1):
            if i == 0: 
                window = Counter(s[:m])
            else:    
                window[s[i-1]] -= 1s
                window[s[i+m-1]] += 1
            if len(window - p) == 0:
                ans.append(i)
                
        return ans





s = "cbaebabacd"
p = "abc"
print(Solution().findAnagrams(s, p))