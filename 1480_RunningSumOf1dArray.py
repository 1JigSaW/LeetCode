# Me solution

def runningSum(nums):
	for i in range(1, len(nums)):
		nums[i] = nums[i] + nums[i - 1]
	return nums

def runningSum(nums):
    i = 1
    while i<len(nums):
        nums[i]+=nums[i-1]
        i+=1
    return nums


nums = [3,1,2,10,1]
print(runningSum(nums))