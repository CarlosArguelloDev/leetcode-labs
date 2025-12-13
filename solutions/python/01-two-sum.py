class Solution(object):
    def twoSum(self, nums, target):
        numsLength = len(nums)
        for i in range (numsLength):
            for j in range (i + 1, numsLength):
                if nums[i] + nums[j] == target:
                    return[i,j]