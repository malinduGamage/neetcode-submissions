class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        m = 0
        
        for n in nums:
            if n-1 not in s:
                l = 1
                while n+l in s:
                    l+=1
                if (m<l) :
                    m = l
        return m