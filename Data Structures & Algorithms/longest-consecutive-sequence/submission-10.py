class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        
        maxCount = 0
        for num in nums:
            count = 0
            if num - 1 not in numSet:
                while num in numSet:
                    num += 1
                    count +=1
                    
            # print(maxCount)
            maxCount = max(count, maxCount)

        return maxCount
        
