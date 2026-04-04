class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if nums[0] > 0:
                return res
            # skip same ones, but make sure you are not going out of bounds error
            # so check i > 0 so that nums[i-1] never errors out
            if i > 0 and nums[i-1] == nums[i]:
                continue

            l, r = i+1, len(nums)-1

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total < 0:
                    l += 1
                elif total > 0:
                    r -=1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1

                    while l < r and nums[l-1] == nums[l]:
                        l+=1
                    while l < r and nums[r+1] == nums[r]:
                        r-=1
        return res

       