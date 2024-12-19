import sys
import math
from dataclasses import dataclass


lines = [list(line.strip()) for line in sys.stdin]



@dataclass
class Guard:
    row: int
    column: int
    direction: float 

    def next_move(self):
    	dc = int(math.cos(self.direction))  #columns are your x-axis
    	dr = int(math.sin(self.direction))  #rows are your y-axis
    	return (self.row + dr, self.column + dc)
    def move(self):
    	dc = int(math.cos(self.direction))  #columns are your x-axis
    	dr = int(math.sin(self.direction))  #rows are your y-axis
    	self.row = self.row + dr 
    	self.column = self.column + dc 
    def turn(self):
    	self.direction = self.direction + math.pi/2


obstacles = [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "#"]

person =  [(i, j) for i in range(len(lines)) for j in range(len(lines[i])) if lines[i][j] == "^"][0]
guard = Guard(person[0], person[1], -math.pi/2)

while True: 
	lines[guard.row][guard.column] = "X"
	nm = guard.next_move() 
	if nm in obstacles:
		guard.turn() 
	elif nm[0] < 0 or nm[0] >= len(lines) or nm[1] < 0 or nm[1] >= len(lines[0]):
		break
	else:
		guard.move() 


print(sum([line.count("X") for line in lines]))





