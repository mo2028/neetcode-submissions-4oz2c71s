class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = []
        for p, s in zip(position, speed):
            pair.append((p,s))

        pair.sort(reverse=True)
        stack = []
        
        
        for eachPair in pair:
            print(eachPair)
            timeToTarget = (target - eachPair[0]) / eachPair[1]
            print(timeToTarget)
            while stack and timeToTarget <= stack[-1]:
                popped= stack.pop()
                timeToTarget = popped
                print("popped:", popped)
            stack.append(timeToTarget)
            print("appended:", timeToTarget)

        return len(stack)

            


        
        