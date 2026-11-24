import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # keep track of occurrences for each task
        # create a min heap queue for values based on how many cycles they have and number of occurrences
        # while there is still an occurrence that is not 0 in occ

        counter = Counter(tasks)
        freq = [value for value in counter.values()]

        queue = deque()
        
        heapq.heapify_max(freq)
        
        time = 0

        while freq or queue:

            time += 1

            if freq:
                # get top value
                cnt = heapq.heappop_max(freq)

                # append the value and time until next line into queue
                if cnt - 1 > 0:
                    queue.append((cnt-1, time + n))
            
            if queue and queue[0][1] <= time:
                val, curr_time = queue.popleft()
                heapq.heappush_max(freq, val)
            
        return time

                

        