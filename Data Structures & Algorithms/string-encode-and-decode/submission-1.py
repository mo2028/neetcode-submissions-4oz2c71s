class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s))+'#'+s
        # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        # 5#Hello5#World
        i = 0
        while i < len(s):
            # get to the start of a # so basically consume lenght
            j = i
            while s[j] != '#':
                j+=1

            length = int(s[i:j])
            # consume '#'
            i = j+1
            word = s[i: i+length]
            res.append(word)
            i += length
        print(res)

        return res



        
