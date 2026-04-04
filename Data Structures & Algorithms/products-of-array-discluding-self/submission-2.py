class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums
        # [1, 2, 4, 6]
        # prefix
        # [1, 1, 2, 8]
        # postfix
        # [48, 24, 12, 8]

        l = len(nums)
        prefix = 1
        res = [0] * l
        for i in range(l):
            res[i] = prefix
            prefix = prefix * nums[i]

        print(res)

        postfix = 1
        for i in range(l-1, -1, -1):
            res[i] = res[i] * postfix
            postfix = postfix * nums[i]
        return res







            
            
        