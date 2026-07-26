class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT,window = {},{}

        for ti in t:
            countT[ti] = countT.get(ti,0)+1

        have,need = 0,len(countT)
        res = [0,0]
        resLen = float("infinity")
        l=0
        for r in range(len(s)):

            window[s[r]] = window.get(s[r],0)+1

            if s[r] in countT and countT[s[r]] == window[s[r]]:
                have +=1
            
            while have == need:

                if r-l+1 < resLen:
                    res = [r,l]
                    resLen = r-l+1

                window[s[l]] -=1

                if s[l] in countT and countT[s[l]] > window[s[l]]:
                    have -=1

                l+=1
        print(s[res[1]:res[0]+1])
        return s[res[1]:res[0]+1] if resLen != float("infinity") else ""


