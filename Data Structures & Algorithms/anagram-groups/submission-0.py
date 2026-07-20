class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = dict()
        for st in strs:
            s = "".join(sorted(st))
            if s not in map:
                map[s] = [st]
            else:
                map[s].append(st)
            
        return list(map.values())