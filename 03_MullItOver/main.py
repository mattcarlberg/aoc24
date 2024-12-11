import sys
import re

def mul(a, b):
	return a*b

def sum_of_products(text):
	pattern = r"mul\(\d{0,9},\d{0,9}\)"
	match = re.findall(pattern, text)
	return sum([eval(a) for a  in match])


def strip_off_segments(text):
	pattern = r"don't\(\).*?do\(\)"
	while True:
		match = re.search(pattern, text)
		if match:
			text = text[:match.start()] + text[match.end():]
		else:
			break
	#but what if the string ends in a don't()....need to strip off the end
	pattern = r"don't().*"
	match = re.search(pattern, text)
	if match:
		text = text[:match.start()]
	return text

lines = [line.strip() for line in sys.stdin]
memory = "".join(lines).strip() 
memory = strip_off_segments(memory)
result = sum_of_products(memory)




print(result)
