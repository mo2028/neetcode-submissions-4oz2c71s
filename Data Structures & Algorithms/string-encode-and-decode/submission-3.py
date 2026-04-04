class Solution:

    def encode(self, strs: List[str]) -> str:
        length = 0
        combinedWord = ""
        for word in strs:
            combinedWord =   combinedWord + str(len(word)) + ":" + word
        print(combinedWord)
        return combinedWord

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # read until the delimiter since it starts with a number
            length = ""
            j = i
            while s[j] != ':':
                length = length + s[j]
                j +=1
            numberLen = int(length)
            
            # skip the delimiter
            i = j+1

            word = ""
            numberLen += i
            while i < numberLen:
                word = word + s[i] 
                i+=1 
            res.append(word)

        return res 
