class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        candidates.sort()

        def dfs(i, total, lst):
            if total == target:
                res.append(lst.copy())
                return
            if total>target or i >= len(candidates):
                return
            
            val = candidates[i]
            lst.append(val)
            total += val
            dfs(i+1, total, lst)

            lst.pop()
            total -= val

            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i+1, total, lst)
        
        dfs(0, 0, [])
        return res