class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthestIndex = 0
        for i in range(len(nums)):
            if i > farthestIndex:
                return False
            farthestIndex = max(farthestIndex, i + nums[i])
            if(farthestIndex >= len(nums) - 1):
                return True
        return True
#My initial focus was so much on the path and counting along so i was following individual paths and that is so confusing and time ocmplexity high. focus needs to be shifted to each index, whats the furthest index i can go to overall? that is a global variable.


        