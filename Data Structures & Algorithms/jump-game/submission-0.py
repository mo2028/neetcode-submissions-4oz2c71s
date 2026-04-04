class Solution:
    def canJump(self, nums: List[int]) -> bool:

        # The furthest position we can reach so far
        max_reach = 0
        
        # Iterate through the array, but only up to the furthest position we can reach
        # This is crucial - if we can't reach a position, we don't need to check it
        for i in range(len(nums)):
            # If we can't reach the current position, return False
            if i > max_reach:
                return False
                
            # Update the furthest position we can reach from our current position
            # We take the maximum of:
            # 1. Our previous furthest reach (max_reach)
            # 2. The furthest we can jump from our current position (i + nums[i])
            max_reach = max(max_reach, i + nums[i])
            
            # If we can reach the last index, we can return True early
            if max_reach >= len(nums) - 1:
                return True
        
        return True
        