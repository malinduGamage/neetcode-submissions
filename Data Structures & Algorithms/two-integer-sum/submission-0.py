class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = dict()
        for i in range(len(nums)):
            if(nums[i] in s): return [s[nums[i]],i]
            s[target - nums[i]] = i
        return []
        