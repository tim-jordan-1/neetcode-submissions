class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        subset = []

        def palindrome(s):
            l, r = 0, len(s)-1
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        def search(i, j ):
        
            if j == len(s):
                res.append(subset.copy())
                return
            if i == len(s):
                return

            # skip partitioning at current index
            search(i+1, j)
            
            slice = s[j:i+1]
            # check if slice is a palindrome
            if palindrome(slice):
                subset.append(slice)
                search(i+1, i+1)
                subset.pop()
        
        search(0,0)
        return res