import sys
import math
from dataclasses import dataclass


lines = [list(line.strip()) for line in sys.stdin]



@dataclass
class Guard:
    row: int
    column: int
    direction: int 
    stuck: bool
    history: list 

    def next_move(self):
    	dc = int(math.cos(math.radians(self.direction)))  #columns are your x-axis
    	dr = int(math.sin(math.radians(self.direction)))  #rows are your y-axis
    	return (self.row + dr, self.column + dc)
    def move(self):
    	dc = int(math.cos(math.radians(self.direction)))  #columns are your x-axis
    	dr = int(math.sin(math.radians(self.direction)))  #rows are your y-axis
    	self.row = self.row + dr 
    	self.column = self.column + dc
    	if (self.row, self.column, self.direction) in self.history:
    		self.stuck = True
    	self.history.append((self.row, self.column, self.direction)) 
    def turn(self):
    	self.direction = (self.direction + 90)%360


def simulation_results_in_cycle(start, obstacles):
	guard = Guard(start[0], start[1], 270, False, [])
	while True: 
		nm = guard.next_move() 
		if nm in obstacles:
			guard.turn() 
		elif nm[0] < 0 or nm[0] >= len(lines) or nm[1] < 0 or nm[1] >= len(lines[0]):
			return False
		else:
			guard.move()
			#print(guard.history)
			if guard.stuck:
				return True  


obstacles = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "#"]

person =  [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "^"][0]


## run the first simulation to see which squares are marked as X in the path
guard = Guard(person[0], person[1], 270, False, [])
while True: 
	lines[guard.row][guard.column] = "X"
	nm = guard.next_move() 
	if nm in obstacles:
		guard.turn() 
	elif nm[0] < 0 or nm[0] >= len(lines) or nm[1] < 0 or nm[1] >= len(lines[0]):
		break
	else:
		guard.move() 

guard_path = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "X"]
#print(guard_path)



## run the new simulations 
count = 0 
repeat = 0 
for (i, j) in guard_path:
		repeat = repeat + 1
		print(f"repeat {repeat} of {len(guard_path)}")
		if not (i == person[0] and j == person[1]):
			#print(i,j)
			obstacles.append((i, j))
			if simulation_results_in_cycle(person, obstacles):
				count+=1
			obstacles.pop(-1)
print(count)










