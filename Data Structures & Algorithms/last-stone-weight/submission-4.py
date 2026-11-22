import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 1. create a max heap
        # 2. pop the two largest values
        # 3. make calculation
        # 4. push remainder
        # 5. repeat

        heapq.heapify_max(stones)

        while len(stones) > 1:
            print(stones)
            x = heapq.heappop_max(stones)
            y = heapq.heappop_max(stones)
            if (x-y) > 0:
                heapq.heappush_max(stones, x-y)
        
        return stones[0] if stones else 0