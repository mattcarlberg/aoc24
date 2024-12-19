import sys


def corrected(nums, rules):


	trimmed_rules = {} 
	for k in rules:
		vals = list(filter(lambda x: x in nums, rules[k]))
		print(len(vals))
		if k in nums and len(vals) > 0:
			trimmed_rules[k] = vals



	first_num = list(filter(lambda x: x not in trimmed_rules, nums))
	# print(f"first: {first_num}")

	# print(f"untrimmed {rules}")
	# print(f"trimmed {trimmed_rules}")
	a = sorted(list(trimmed_rules.keys()), key=lambda k: len(trimmed_rules[k]))
	a.insert(0, first_num)


	# for num in alist:
	# 	adict.pop(num, None)
	# 	for k in adict:
	# 		adict[k] = 

	return a


	pass


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
			pass
			#result = result + nums[len(nums)//2]
		if not valid:
			correct = corrected(nums, rules)
			result = result + correct[len(correct)//2]

print(result)



		