#my code...(struggle at advance section and everything was great)

try:
    x,y=input("Enter the coordinate(x,y) : ").split(",")
    direction=input("Enter the direction of robot facing now: ").lower()
    nx,ny=int(x),int(y)
    while True:
        user=input("command for the robot: ").lower()
        if user=="turn right" or user=="r":
            if direction=="north":
                direction="east"
            elif direction=="east":
                direction="south"
            elif direction=="south":
                direction="west"
            elif direction=="west":
                direction="north"
        if user=="turn left" or user=="l":
            if direction=="north":
                direction="west"
            elif direction=="west":
                direction="south"
            elif direction=="south":
                direction="east"
            elif direction=="east":
                direction="north"
        if user == "advance" or user == "a":
            if direction == "north":
                ny += 1  
            elif direction == "south":
                ny -= 1  
            elif direction == "east":
                nx += 1  
            elif direction == "west":
                nx -= 1
        print(f"postion: {nx},{ny} and facing is {direction}")
except EOFError:
    print("No input received. Have a good day!")


#solution...

"""
Created on Thu Feb 16 22:43:27 2017 updated for new tests Sat Mar 6 05:07:17 2021

@author: bethanyg
"""

NORTH, SOUTH, EAST, WEST = 0, 180, 90, 270


class Robot:
    def __init__(self, direction=NORTH, x=0, y=0):
        self._x = x
        self._y = y
        self.direction = direction
        self._instructions = {'A': self.advance,
                              'L': self.turn_left,
                              'R': self.turn_right}


    @property
    def coordinates(self):
        return (self._x, self._y)


    def advance(self):
        moves = {NORTH: 1, SOUTH: -1, EAST: 1, WEST: -1}

        if self.direction in (NORTH, SOUTH):
            self._y += moves[self.direction]

        if self.direction in (EAST, WEST):
            self._x += moves[self.direction]


    def turn_left(self):
        self.direction = (self.direction -90) % 360


    def turn_right(self):
        self.direction = (self.direction + 90) % 360


    def move(self, directions):
        for item in directions:
            self._instructions[item]()