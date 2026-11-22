import heapq
from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def euc_dist(point):
            x, y = point
            exp1 = x**2
            exp2 = y**2
            dist = sqrt(exp1 + exp2)
            return dist
        
        res = heapq.nsmallest(k, points, euc_dist)
        return res
        