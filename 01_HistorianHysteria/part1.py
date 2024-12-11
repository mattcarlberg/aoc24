import sys

x = [] 
y = [] 
for line in sys.stdin:
    line = line.strip().split() 
    x.append(int(line[0]))
    y.append(int(line[1]))

x.sort() 
y.sort() 

dist = sum([abs(a - b) for a, b in zip(x, y)]) 
print(dist)


 
