class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(subset, choices):
            if not choices:
                res.append(subset.copy())
            for _ in range(len(choices)):
                val = choices.popleft()
                subset.append(val)
                dfs(subset, choices)
                choices.append(val)
                subset.pop()
        
        dfs([], deque(nums))
        return res
                