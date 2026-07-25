class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        count = 0
        res = 0
        l,r = 0,0

        while r<len(s):
            if s[r] not in se:
                se.add(s[r])
                count +=1
                r+=1
            else:
                res = max(count,res)
                
                while s[l]!=s[r]:
                    se.remove(s[l])
                    l+=1
                    count -=1
                se.remove(s[l])
                l+=1
                count -=1
        return max(count,res)