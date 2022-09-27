# My sol 1
def pivotIndex(nums):
	for i in range(len(nums)):
		if sum(nums[:i]) == sum(nums[i+1:]):
			return i
	return -1

# My sol 2
def pivotIndex(nums):
	sum1 = 0
	sum2 = 0
	for i in range(len(nums)):
		for j in range(len(nums)): 
			if j < i:
				sum1 += nums[j]
			elif j > i:
				sum2 += nums[j]
		if sum1 == sum2:
			return i
		sum1 = 0
		sum2 = 0
	return -1

def pivotIndex(nums):
	all_sum = 0
	left = 0
	for i in nums:
		all_sum += i
	for i in range(len(nums)):
		if left == all_sum - left - nums[i]:
			return i
		left += nums[i]
	return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))