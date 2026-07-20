class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = "abcdefghijklmnopqrstuvwxyz"
        maps = {l: 0  for l in a}
        mapt = {l: 0  for l in a}

        for sc in s:
            maps[sc] += 1

        for tc in t:
            mapt[tc] += 1

        return maps == mapt