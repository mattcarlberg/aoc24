import sys
import re

def mul(a, b):
	return a*b

lines = [line.strip() for line in sys.stdin]

memory = "".join(lines).strip() 

pattern = r"mul\(\d{0,9},\d{0,9}\)"

match = re.findall(pattern, memory)

print(sum([eval(a) for a  in match]))
