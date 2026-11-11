class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        subset = []

        def dfs(i, total):
            if total == target:
                res.append(subset.copy())
                return
            elif i>= len(nums) or total > target:
                return
            val = nums[i]
            subset.append(val)
            total += val
            dfs(i, total)
            
            subset.pop()
            total -= val
            dfs(i+1, total)
        
        dfs(0,0)
        return res