class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        l,r = [nums[0]],[nums[ln-1]]
        res = []
        
        for i in range(1,ln-1):
            print(nums[i],nums[ln - i -1])
            l.append(nums[i] * l[i-1]) 
            r.append(nums[ln - i -1]*r[i-1]) 

        l.insert(0, 1)
        r.append(1)

        for i in range(ln):
            res.append(l[i]*r[ln-i-2])
        return res
