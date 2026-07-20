class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        c =0
        while n:
            res <<= 1
            if n%2 == 1:
                res |= 1
            else:
                res
            n >>= 1
            c+=1
        return res << 32 - c