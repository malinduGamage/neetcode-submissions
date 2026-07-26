class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        map = dict()
        res = 0
        l=0

        for r in range(len(s)):
            map[s[r]] = map.get(s[r],0) +1
            mc = max(map.values())
            if(r-l+1 - mc <= k):
                res = max(r-l+1,res)
            else:
                while(r-l+1 -mc>k and l<r):
                    map[s[l]] -=1
                    l+=1
            r+=1

        return res