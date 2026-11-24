import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        val = heapq.nlargest(k, nums)

        return val[-1]