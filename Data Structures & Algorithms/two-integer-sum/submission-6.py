class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, val in enumerate(nums):
            indices[val] = i
        # print(indices)
        # # want to check if for each val the its complement exists
        for i, val in enumerate(nums):
            val2 = target - val
            if val2 in indices and indices[val2] != i:
                return [i, indices[val2]]
        return []
            





        