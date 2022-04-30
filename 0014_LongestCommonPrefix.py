def longestCommonPrefix(strs):
	if len(strs) == 0:
		return ""
	for i in range(len(strs[0])):
		c = strs[0][i]
		for j in range(len(strs)):
			print(c)
			if i == len(strs[j]) or strs[j][i] != c:
				return strs[0][:i]         
	return strs[0]

	
strs = ["flower","flow","flight"]
print(longestCommonPrefix(strs))