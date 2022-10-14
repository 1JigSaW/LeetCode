class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        arr1 = []
        arr2 = []
        for i in s:
            if i != '#':
                arr1.append(i)
            else:
                if len(arr1) != 0:
                    arr1.pop()
        for j in t:
            if j != '#':
                arr2.append(j)
            else:
                if len(arr2) != 0:
                    arr2.pop()
        return arr1 == arr2


s = "a##c"
t = "#a#c"
print(Solution().backspaceCompare(s, t))