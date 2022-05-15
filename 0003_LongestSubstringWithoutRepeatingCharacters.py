# O(n2)

def lengthOfLongestSubstring(s: str) -> int:
	d = {}
	pointer = 0
	maxx = 0
	ind = 0
	while pointer != len(s)-1:
		for i in range(pointer, len(s)):
			if s[i] not in d:
				d[s[i]] = 1
			else:
				if maxx < len(d):
					maxx = len(d)
				d = {}
				pointer += 1
				continue
	if maxx < len(d):
		maxx = len(d)
	return maxx

# O(n)

def lengthOfLongestSubstring(s: str) -> int:
	n = len(s)
	ans = 0
	mp = {}

	i = 0
	for j in range(n):
		if s[j] in mp:
			i = max(mp[s[j]], i)
		print(ans)
		ans = max(ans, j - i + 1)
		mp[s[j]] = j + 1

	return ans

s = "pwwkew"
print(lengthOfLongestSubstring(s))