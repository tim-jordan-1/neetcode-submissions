class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0 for _ in range(len(temperatures))]
        for i in range(1, len(temperatures)):
            curr_temp = temperatures[i]

            while stack and temperatures[stack[-1]] < curr_temp:
                day = stack.pop()
                delta = i - day
                res[day] = delta
            stack.append(i)
        return res