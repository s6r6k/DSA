class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in dict:
                v = dict[comp]
                return [v, i]
            dict[nums[i]] = i
