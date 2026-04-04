class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(", "]":"[", "}":"{"}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    # can only pop if there is already something in stack and the top is complement of closing c 
                    stack.pop()
                else:
                    return False


            # must be an opening 
            else:
                stack.append(c)
    
        return not stack

                

        