class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}

        def dp(i, j):
            if (i, j) in memo:
                return memo[(i, j)]
            
            if j == len(p):
                ans = i == len(s)
            else:
                first_match = i < len(s) and p[j] in {s[i], '.'}

                if j + 1 < len(p) and p[j+1] == '*':
                    ans = dp(i, j+2) or (first_match and dp(i+1, j))
                    # j+2: skip a* altogether
                    # i+1, j: consume current char
                else:
                    ans = first_match and dp(i+1, j+1)
                
            memo[(i, j)] = ans
            return ans
        
        return dp(0, 0)