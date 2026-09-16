#solution... by ai
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        fleets = 0
        previous = 0
        for pos, spd in cars:
            current = (target - pos) / spd
            if current > previous:
                fleets += 1
                previous = current
        return fleets

#my code..it is still incorrect lol...
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times=[]
        fleet=0
        if len(position)==len(speed):
            for i in range(len(position)):
                time=(target-position[i])/speed[i]
                times.append(time)
        previous=0
        for current in times:
            if current<=previous:
                fleet+=0
            elif current>previous:
                fleet+=1
                previous=current
        return fleet