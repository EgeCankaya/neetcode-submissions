class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)
        
        fleets = 0
        slowest_time_ahead = 0.0
        
        for p, s in cars:
            # Calculate the time this car needs to reach the target
            time = (target - p) / s
            
            if time > slowest_time_ahead:
                fleets += 1
                slowest_time_ahead = time # This car is now the bottleneck for cars behind it
                
        return fleets