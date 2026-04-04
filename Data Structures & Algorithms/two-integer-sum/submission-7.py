class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, val in enumerate(nums):
            valTwo = target - val
            if valTwo in prevMap:
                return [prevMap[valTwo], i]
            prevMap[val] = i
        





        