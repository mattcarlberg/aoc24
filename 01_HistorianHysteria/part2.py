import sys

x = [] 
y = [] 
for line in sys.stdin:
    line = line.strip().split() 
    x.append(int(line[0]))
    y.append(int(line[1]))



x.sort() 
y.sort() 


dist = sum([y.count(a)*a for a in x]) 
print(dist)


 
