def twoSum(numbers, target):
	left, right = 0, len(numbers)-1
	while left <= right:
		if (numbers[left] + numbers[right]) > target:
			right -= 1
		elif (numbers[left] + numbers[right]) < target:
			left += 1
		else:
			return [left+1, right+1]
		

numbers = [5, 25, 75]
target = 80
print(twoSum(numbers, target))