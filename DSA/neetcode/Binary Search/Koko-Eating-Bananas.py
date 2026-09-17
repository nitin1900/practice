#my code but heavily used in degubbing and logic mostly code by ai only...
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left,right=1,max(piles)
        #left is lowest and right is highest speed possible
        #and h is deadline
        #left,right,mid-speedometer & totalh,h-clock(hour)
        while left<=right:
            mid=(left+right)//2 #k:-guess of eating speed
            totalh=0
            for p in piles: #no. of banana in bowl
                totalh+=(p+mid-1)//mid#p//mid #totalh is time taken acc. to k
            if totalh<=h:
                right=mid-1
            else:
                left=mid+1
        return left