import sys


rules = {}
valid_updates = [] 

result = 0 
for line in sys.stdin:
	if "|" in line:
		before = int(line.split("|")[0])
		after = int(line.split("|")[1])
		if after in rules:
			rules[after].append(before)
		else:
			rules[after] = [before]
	if "," in line:
		nums = [int(num) for num in line.strip().split(",")]
		valid = True
		for i in range(len(nums)):
			num = nums[i]
			if num in rules:
				if all([x in nums[:i] or x not in nums for x in rules[num]]):
					continue
				else:
					valid = False
					break
		if valid:
			result = result + nums[len(nums)//2]
		if not valid:
			print(nums)
			print(rules)
			print("@@@@@@@")
print(result)



		