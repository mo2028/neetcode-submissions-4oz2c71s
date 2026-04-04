class Solution:
    def isValid(self, s: str) -> bool:
        # you basically just go through the s and add into the stack until its not a closing bracket, once it is then you start popping from teh stack
        # once you see a mismatch that you know that it is not valid 
        m = {")": "(", "}":"{", "]":"["}

        stk = []
        c = 0
        for i in range(len(s)):
            if s[i] not in m:
                
                stk.append(s[i])
                c +=1
                print(stk)
            else:
                if stk:
                    print(stk)
                    popped = stk.pop()
                    print(popped, m[s[i]])
                    if popped != m[s[i]]:
                        return False
                    c-=1
                else:
                    return False
        print(c)
        return c==0
                   




        

        # for p in s:
        #     if p in m:
        #         stk.append(p)
        # while stk:
        #     opening = stk.pop()
        #     if opening == 




        
        