class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Sort by position in reverse and calculate time for each car
        times = [(target - p)/s for p, s in sorted(zip(position, speed), reverse=True)]
        
        # If car takes longer than car in front, it's a new fleet
        stack = []
        for time in times:
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)
        