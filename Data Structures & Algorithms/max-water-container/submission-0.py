class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i,j = 0,len(heights)-1

        while(i<j):
            a = min(heights[i],heights[j])*(j-i)
            res = max(res,a)

            if(heights[i]>heights[j]):
                j-=1
            elif(heights[i]<heights[j]):
                i+=1
            else:
                i+=1

        return res