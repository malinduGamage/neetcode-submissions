class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = dict()
        for num in nums:
            map[num] = map.get(num,0)+1

        return sorted(map, key=map.get, reverse=True)[:k]