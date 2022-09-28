def isSubsequence(s, t):
	if len(s) == 0:
		return True
	ind = 0
	flag = 0
	for let in t:
		if s[ind] == let:
			flag += 1 
			if ind + 1 < len(s):
				ind +=1
			else:
				return True
	return flag == len(s)


s = "b"
t = "abc"
print(isSubsequence(s, t))